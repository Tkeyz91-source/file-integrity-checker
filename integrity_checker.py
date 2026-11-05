import hashlib
import json
from pathlib import Path

# Project directories
BASE_DIR = Path(__file__).resolve().parent
SAMPLES_DIR = BASE_DIR / "samples"
REPORTS_DIR = BASE_DIR / "reports"
BASELINE_FILE = REPORTS_DIR / "integrity_baseline.json"


def calculate_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def scan_files():
    """Create a record of all files in the samples directory."""
    results = {}

    SAMPLES_DIR.mkdir(parents=True, exist_ok=True)

    for file_path in SAMPLES_DIR.rglob("*"):
        if file_path.is_file() and not file_path.is_symlink():
            relative_path = str(file_path.relative_to(SAMPLES_DIR))
            results[relative_path] = calculate_hash(file_path)

    return results


def create_baseline():
    """Save the current file hashes as the baseline."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    results = scan_files()

    with open(BASELINE_FILE, "w") as file:
        json.dump(results, file, indent=4)

    print("[SUCCESS] Baseline created.")
    print(f"[INFO] Files recorded: {len(results)}")


def check_integrity():
    """Compare current files against the saved baseline."""
    if not BASELINE_FILE.exists():
        print("[ERROR] No baseline found.")
        print("Run the baseline command first.")
        return

    with open(BASELINE_FILE, "r") as file:
        baseline = json.load(file)

    current = scan_files()

    baseline_files = set(baseline)
    current_files = set(current)

    modified = [
        name for name in baseline_files & current_files
        if baseline[name] != current[name]
    ]

    new_files = current_files - baseline_files
    deleted_files = baseline_files - current_files

    print("\n===== FILE INTEGRITY REPORT =====")

    for name in modified:
        print(f"[MODIFIED] {name}")

    for name in new_files:
        print(f"[NEW] {name}")

    for name in deleted_files:
        print(f"[DELETED] {name}")

    if not modified and not new_files and not deleted_files:
        print("[SAFE] No changes detected.")

    print("\n===== SCAN SUMMARY =====")
    print(f"Modified files: {len(modified)}")
    print(f"New files: {len(new_files)}")
    print(f"Deleted files: {len(deleted_files)}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="SHA-256 File Integrity Checker"
    )

    parser.add_argument(
        "action",
        choices=["baseline", "check"],
        help="Create a baseline or check file integrity"
    )

    args = parser.parse_args()

    if args.action == "baseline":
        create_baseline()
    else:
        check_integrity()


# File Integrity Checker

## Project Overview

The File Integrity Checker is a Python-based defensive cybersecurity tool that uses SHA-256 hashing to monitor files and identify unexpected changes.

## Features

- Calculates SHA-256 file hashes.
- Creates a file integrity baseline.
- Detects modified files.
- Detects newly created files.
- Detects deleted files.
- Displays a scan summary.

## Technologies Used

- Python 3
- Kali Linux
- hashlib
- JSON

## Project Structure

```text
file-integrity-checker/
├── integrity_checker.py
├── README.md
├── requirements.txt
├── reports/
│   └── file-integrity-assessment.md
├── samples/
└── screenshots/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Tkeyz91-source/file-integrity-checker.git
cd file-integrity-checker
```

This project uses Python's standard library, so no third-party packages are required.

## How to Use

Create a sample file:

```bash
mkdir -p samples reports
echo "Original test content" > samples/test_file.txt
```

Create the baseline:

```bash
python3 integrity_checker.py baseline
```

Check file integrity:

```bash
python3 integrity_checker.py check
```

## Test Results

| Test | Result |
|---|---|
| File modification detection | Passed |
| New file detection | Passed |
| Deleted file detection | Passed |

## Security Assessment Report

See the [File Integrity Security Assessment](reports/file-integrity-assessment.md).

## Project Screenshots

### Screenshot 1
![Screenshot 1](screenshots/Screenshot%20From%202026-11-02%2015-34-26.png)

### Screenshot 2
![Screenshot 2](screenshots/Screenshot%20From%202026-11-02%2015-35-13.png)

### Screenshot 3
![Screenshot 3](screenshots/Screenshot%20From%202026-11-02%2015-35-59.png)

### Screenshot 4
![Screenshot 4](screenshots/Screenshot%20From%202026-11-02%2015-36-47.png)

### Screenshot 5
![Screenshot 5](screenshots/Screenshot%20From%202026-11-02%2015-37-46.png)

### Screenshot 6
![Screenshot 6](screenshots/Screenshot%20From%202026-11-02%2015-38-54.png)

### Screenshot 7
![Screenshot 7](screenshots/Screenshot%20From%202026-11-02%2015-39-43.png)

## Limitations

- Monitors only the configured `samples/` directory.
- Detects changes but does not prevent them.
- The baseline file needs separate protection.
- Does not identify who changed a file.

## Author

GitHub: [Tkeyz91-source](https://github.com/Tkeyz91-source)


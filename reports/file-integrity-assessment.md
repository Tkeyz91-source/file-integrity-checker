# File Integrity Checker — Security Assessment Report

## 1. Project Overview

The File Integrity Checker is a Python-based defensive
security tool that uses SHA-256 hashing to monitor files
and identify unauthorized or unexpected changes.

## 2. Objective

To demonstrate how cryptographic hashing can help
identify changes to files and support file integrity
monitoring.

## 3. Tools and Technologies

- Kali Linux
- Python 3
- SHA-256
- hashlib
- JSON

## 4. Testing Methodology

A baseline was created using the original sample file.
The program then compared subsequent file states against
the saved baseline.

Three test scenarios were performed.

## 5. Test Results

| Test | Expected Result | Actual Result |
|---|---|---|
| File modification | Detect modified file | Passed |
| New file creation | Detect new file | Passed |
| File deletion | Detect deleted file | Passed |

## 6. Findings

The application successfully detected:

- Modified files.
- Newly created files.
- Deleted files.

All three functional tests passed.

## 7. Security Recommendations

- Protect the baseline file against unauthorized changes.
- Restrict access to the monitoring directory.
- Store baseline copies securely.
- Run integrity checks regularly.
- Review and investigate unexpected changes.

## 8. Limitations

- The application monitors only its configured samples directory.
- It detects changes but does not prevent them.
- The baseline file must be protected separately.
- The tool does not identify who modified a file.

## 9. Conclusion

The assessment demonstrated that the Python-based
File Integrity Checker can detect file modifications,
new files, and deleted files through SHA-256 hash
comparison.

The project demonstrates practical knowledge of
cryptographic hashing, file monitoring, and defensive
security testing.


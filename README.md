🛡️ ShieldGate: Security & Vulnerability Auditor
ShieldGate is a technical auditing tool designed to evaluate the strength and security of strings (passwords, keys, or tokens). It uses advanced pattern matching to detect vulnerabilities and provides real-time feedback on security compliance.

🛠️ The Technical Logic
This project focuses on Input Validation and Pattern Recognition, two critical pillars of cybersecurity:

Regex Pattern Analysis: Utilizes Regular Expressions (re module) to scan for specific character classes (entropy checks).

Scoring Algorithm: Implements a multi-factor scoring system to categorize inputs as WEAK, MODERATE, or STRONG.

Security Feedback Loop: Generates dynamic error reporting to guide users toward more secure data patterns.

✨ Key Features
Entropy Analysis: Checks for length, casing, numeric presence, and special character density.

Pattern Matching: Employs Regex to identify missing security requirements instantly.

Terminal-Style UI: A high-contrast, "security terminal" inspired dashboard built with Tailwind CSS.

Live Auditing: Instant server-side processing and feedback.

🚀 Tech Stack
Language: Python 3.x

Framework: Flask

Logic Engine: Regular Expressions (Regex)

Frontend: Tailwind CSS (Modern Industrial UI)

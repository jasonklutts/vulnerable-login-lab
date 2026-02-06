# Vulnerable Login Application Lab

Intentionally vulnerable web application for studying authentication attacks and building detection capabilities.

## Overview
This project demonstrates common authentication vulnerabilities and includes analysis tools to identify attack patterns.

## Features
- Flask-based login portal with intentional security flaws
- Comprehensive logging of all authentication attempts
- Python analysis script for identifying brute force patterns
- Detection of common attack signatures

## Components
- `app.py` - Main Flask application
- `templates/login.html` - Login interface
- `analyze_logs.py` - Log analysis and pattern detection tool

## Installation
```bash
pip install -r requirements.txt
python3 app.py
```

## Analysis
Run log analysis:
```bash
python3 analyze_logs.py
```

## ⚠️ Warning
This is an intentionally vulnerable application for educational purposes only. Do not use in production.

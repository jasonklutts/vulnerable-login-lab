#!/usr/bin/env python3
#parse_log_file() - Reads the log and converts each line into structured data
#analyze_by_ip() - Counts attempts from each IP address
#analyze_usernames() - Finds most targeted usernames
#detect_brute_force() - Flags IPs with 5+ attempts
#analyze_passwords() - Shows common password patterns (masked for privacy)
#generate_report() - Prints formatted analysis report


"""
Log Analysis Script for Vulnerable Login Application
Analyzes authentication attempts to identify attack patterns
"""

from datetime import datetime
from collections import defaultdict, Counter
import sys

LOG_FILE = 'logs/attempts.log'

def parse_log_file(log_file):
    """
    Parse the log file and extract login attempts
    Returns a list of dictionaries with parsed data
    """
    attempts = []
    
    try:
        with open(log_file, 'r') as f:
            for line in f:
                # Parse each line: timestamp | IP: x.x.x.x | Username: user | Password: pass | Status: FAILED
                parts = line.strip().split(' | ')
                
                if len(parts) >= 4:
                    attempt = {
                        'timestamp': parts[0],
                        'ip': parts[1].replace('IP: ', ''),
                        'username': parts[2].replace('Username: ', ''),
                        'password': parts[3].replace('Password: ', ''),
                        'status': parts[4].replace('Status: ', '') if len(parts) > 4 else 'FAILED'
                    }
                    attempts.append(attempt)
    
    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found")
        sys.exit(1)
    
    return attempts

def analyze_by_ip(attempts):
    """
    Count failed login attempts by IP address
    """
    ip_counts = Counter(attempt['ip'] for attempt in attempts)
    return ip_counts

def analyze_usernames(attempts):
    """
    Identify most commonly attempted usernames
    """
    username_counts = Counter(attempt['username'] for attempt in attempts)
    return username_counts

def detect_brute_force(attempts, threshold=5):
    """
    Detect potential brute force attacks
    IPs with more than threshold attempts in the log
    """
    ip_counts = analyze_by_ip(attempts)
    brute_force_ips = {ip: count for ip, count in ip_counts.items() if count >= threshold}
    return brute_force_ips

def analyze_passwords(attempts):
    """
    Analyze password patterns (for educational purposes)
    """
    password_counts = Counter(attempt['password'] for attempt in attempts)
    return password_counts

def generate_report(attempts):
    """
    Generate comprehensive analysis report
    """
    print("=" * 60)
    print("VULNERABLE LOGIN APPLICATION - LOG ANALYSIS REPORT")
    print("=" * 60)
    print(f"\nTotal login attempts: {len(attempts)}")
    
    if len(attempts) == 0:
        print("\nNo login attempts found in log file.")
        return
    
    # IP Analysis
    print("\n" + "-" * 60)
    print("TOP 10 SOURCE IPs BY ATTEMPT COUNT")
    print("-" * 60)
    ip_counts = analyze_by_ip(attempts)
    for ip, count in ip_counts.most_common(10):
        print(f"{ip:20} - {count:4} attempts")
    
    # Username Analysis
    print("\n" + "-" * 60)
    print("TOP 10 ATTEMPTED USERNAMES")
    print("-" * 60)
    username_counts = analyze_usernames(attempts)
    for username, count in username_counts.most_common(10):
        print(f"{username:20} - {count:4} attempts")
    
    # Brute Force Detection
    print("\n" + "-" * 60)
    print("BRUTE FORCE DETECTION (5+ attempts)")
    print("-" * 60)
    brute_force = detect_brute_force(attempts, threshold=5)
    if brute_force:
        for ip, count in sorted(brute_force.items(), key=lambda x: x[1], reverse=True):
            print(f"{ip:20} - {count:4} attempts [POTENTIAL BRUTE FORCE]")
    else:
        print("No brute force patterns detected")
    
    # Password Analysis
    print("\n" + "-" * 60)
    print("COMMON PASSWORD PATTERNS")
    print("-" * 60)
    password_counts = analyze_passwords(attempts)
    for password, count in password_counts.most_common(10):
        # Mask passwords for privacy in output
        masked = password[:2] + '*' * (len(password) - 2) if len(password) > 2 else '**'
        print(f"{masked:20} - {count:4} attempts")
    
    # Time-based analysis
    print("\n" + "-" * 60)
    print("TEMPORAL ANALYSIS")
    print("-" * 60)
    if attempts:
        first_attempt = attempts[0]['timestamp']
        last_attempt = attempts[-1]['timestamp']
        print(f"First attempt: {first_attempt}")
        print(f"Last attempt:  {last_attempt}")
    
    print("\n" + "=" * 60)

def main():
    """
    Main function to run log analysis
    """
    print("\nAnalyzing login attempts...\n")
    
    # Parse log file
    attempts = parse_log_file(LOG_FILE)
    
    # Generate report
    generate_report(attempts)
    
    print("\nAnalysis complete.\n")

if __name__ == '__main__':
    main()

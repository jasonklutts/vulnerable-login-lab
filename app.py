from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
import os
import subprocess
import threading

app = Flask(__name__)

# Path to log file
LOG_FILE = 'logs/attempts.log'

# Track running attacks
attack_status = {
    'brute_force': False,
    'credential_stuffing': False,
    'rapid_bot': False
}

@app.route('/')
def index():
    """
    Login page
    """
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    """
    Handle login attempts and log them
    """
    # Get data from the form
    username = request.form.get('username')
    password = request.form.get('password')
    ip_address = request.remote_addr
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Create log entry
    log_entry = f"{timestamp} | IP: {ip_address} | Username: {username} | Password: {password} | Status: FAILED\n"
    
    # Write to log file
    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)
    
    # Always return failure (intentionally vulnerable - no real auth)
    return render_template('login.html', error="Invalid username or password")

@app.route('/dashboard')
def dashboard():
    """
    Attack simulation dashboard
    """
    return render_template('dashboard.html')




@app.route('/api/trigger-attack/<attack_type>', methods=['POST'])
def trigger_attack(attack_type):
    """
    Trigger an attack script
    """
    print(f"DEBUG: Received request for attack type: {attack_type}")
    
    if attack_type not in ['brute_force', 'credential_stuffing', 'rapid_bot']:
        print(f"DEBUG: Invalid attack type")
        return jsonify({'status': 'error', 'message': 'Invalid attack type'}), 400

    if attack_status[attack_type]:
        print(f"DEBUG: Attack already running")
        return jsonify({'status': 'error', 'message': 'Attack already running'}), 400

    # Map attack types to script names
    script_map = {
        'brute_force': 'brute_force_attack.py',
        'credential_stuffing': 'credential_stuffing_attack.py',
        'rapid_bot': 'rapid_bot_attack.py'
    }

    script_name = script_map[attack_type]
    print(f"DEBUG: Running script: {script_name}")

    # Run attack in background thread
    def run_attack():
        attack_status[attack_type] = True
        print(f"DEBUG: Thread started for {attack_type}")
        try:
            # Run the attack script with --auto flag
            result = subprocess.run(
                ['python3', script_name, '--auto'],
                capture_output=True,
                text=True,
                timeout=120,
                cwd='/home/jason/vulnapp'
            )
            print(f"DEBUG: Attack completed with return code: {result.returncode}")
            print(f"DEBUG: stdout: {result.stdout[:200]}")  # First 200 chars
            print(f"DEBUG: stderr: {result.stderr[:200]}")
        except Exception as e:
            print(f"DEBUG: Attack error: {e}")
        finally:
            attack_status[attack_type] = False
            print(f"DEBUG: Thread finished for {attack_type}")

    thread = threading.Thread(target=run_attack)
    thread.start()
    
    print(f"DEBUG: Returning success response")
    return jsonify({'status': 'success', 'message': f'{attack_type} started'})


#stop delete


@app.route('/api/logs', methods=['GET'])
def get_logs():
    """
    Get recent log entries
    """
    try:
        # Read last 50 lines of log file
        with open(LOG_FILE, 'r') as f:
            lines = f.readlines()
            recent_lines = lines[-50:] if len(lines) > 50 else lines
        
        # Parse logs into structured data
        logs = []
        for line in recent_lines:
            parts = line.strip().split(' | ')
            if len(parts) >= 4:
                logs.append({
                    'timestamp': parts[0],
                    'ip': parts[1].replace('IP: ', ''),
                    'username': parts[2].replace('Username: ', ''),
                    'password': parts[3].replace('Password: ', ''),
                    'status': parts[4].replace('Status: ', '') if len(parts) > 4 else 'FAILED'
                })
        
        return jsonify({'status': 'success', 'logs': logs})
    
    except FileNotFoundError:
        return jsonify({'status': 'success', 'logs': []})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/analysis', methods=['GET'])
def get_analysis():
    """
    Run log analysis and return results
    """
    try:
        # Import analysis functions
        from analyze_logs import parse_log_file, analyze_by_ip, analyze_usernames, detect_brute_force, analyze_passwords
        
        # Parse logs
        attempts = parse_log_file(LOG_FILE)
        
        if len(attempts) == 0:
            return jsonify({'status': 'success', 'total': 0, 'data': {}})
        
        # Run analysis
        ip_counts = analyze_by_ip(attempts)
        username_counts = analyze_usernames(attempts)
        brute_force_ips = detect_brute_force(attempts, threshold=5)
        password_counts = analyze_passwords(attempts)
        
        # Format results
        analysis_data = {
            'total_attempts': len(attempts),
            'top_ips': [{'ip': ip, 'count': count} for ip, count in ip_counts.most_common(10)],
            'top_usernames': [{'username': u, 'count': count} for u, count in username_counts.most_common(10)],
            'brute_force_ips': [{'ip': ip, 'count': count} for ip, count in brute_force_ips.items()],
            'top_passwords': [{'password': p[:2] + '*' * (len(p) - 2) if len(p) > 2 else '**', 'count': count} 
                             for p, count in password_counts.most_common(10)],
            'first_attempt': attempts[0]['timestamp'] if attempts else None,
            'last_attempt': attempts[-1]['timestamp'] if attempts else None
        }
        
        return jsonify({'status': 'success', 'data': analysis_data})
    
    except FileNotFoundError:
        return jsonify({'status': 'success', 'total': 0, 'data': {}})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/clear-logs', methods=['POST'])
def clear_logs():
    """
    Clear the log file
    """
    try:
        with open(LOG_FILE, 'w') as f:
            f.write('')
        return jsonify({'status': 'success', 'message': 'Logs cleared'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    # Run Flask on port 5000, accessible from any IP
    app.run(host='0.0.0.0', port=5000, debug=True)

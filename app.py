from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)

# Path to log file
LOG_FILE = 'logs/attempts.log'

@app.route('/')
def index():
    """
    This function runs when someone visits jasonklutts.com/lab
    It shows them the login page (login.html)
    """
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    """
    This function runs when someone submits the login form
    It captures their data and logs it to a file
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

if __name__ == '__main__':
    # Run Flask on port 5000, accessible from any IP
    app.run(host='0.0.0.0', port=5000, debug=True)

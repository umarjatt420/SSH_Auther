import re
import subprocess

# Constants
AUTHORIZED_IPS = ['192.168.10.50', '10.0.0.2']  # Replace with your authorized IP addresses

def detect_unauthorized_ssh_connections():
    # Get the SSH log entries
    ssh_logs = subprocess.check_output(['grep', 'sshd', '/var/log/auth.log']).decode().split('\n')

    # Regular expression pattern to extract IP addresses from log entries
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')

    # Analyze the log entries
    for log_entry in ssh_logs:
        # Extract the IP address from the log entry
        match = ip_pattern.search(log_entry)
        if match:
            ip_address = match.group(0)

            # Check if the IP address is unauthorized
            if ip_address not in AUTHORIZED_IPS:
                print("Unauthorized SSH connection attempt from:", ip_address)

# Run the detection function
detect_unauthorized_ssh_connections()
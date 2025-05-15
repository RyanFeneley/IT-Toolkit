import subprocess
import socket

def ping_test():
    print("\n--- Ping Test ---")
    target = input("Enter domain or IP to ping: ")
    try:
        subprocess.run(["ping", "-n", "4", target], check=True)
    except:
        print("Ping failed.")

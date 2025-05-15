import subprocess

def grab_logs():
    print("\n--- Grabbing System Logs ---")
    try:
        subprocess.run(["wevtutil", "qe", "System", "/c:10", "/f:text"], check=True)
    except:
        print("Unable to retrieve logs. This may require admin rights.")

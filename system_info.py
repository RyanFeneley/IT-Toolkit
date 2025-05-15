import platform
import psutil
import socket
import time

def show_system_info():
    print("\n--- System Information ---")
    print(f"Hostname: {socket.gethostname()}")
    print(f"IP Address: {socket.gethostbyname(socket.gethostname())}")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print(f"RAM Usage: {psutil.virtual_memory().percent}%")
    uptime_seconds = time.time() - psutil.boot_time()
    print(f"Uptime: {uptime_seconds // 3600:.0f} hours")

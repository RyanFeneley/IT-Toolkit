import getpass

def list_users():
    print("\n--- User Accounts ---")
    print(f"Current user: {getpass.getuser()}")
    print("Listing other users requires admin rights or platform-specific tools.")

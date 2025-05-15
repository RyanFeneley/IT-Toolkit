from system_info import show_system_info
from user_utils import list_users
from network_tools import ping_test
from log_grabber import grab_logs

def main():
    while True:
        print("\n=== IT Support Toolkit ===")
        print("1. View System Info")
        print("2. List User Accounts")
        print("3. Ping Test")
        print("4. Grab System Logs")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            show_system_info()
        elif choice == '2':
            list_users()
        elif choice == '3':
            ping_test()
        elif choice == '4':
            grab_logs()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

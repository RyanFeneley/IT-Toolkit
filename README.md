# IT-Toolkit

## Project Overview

This is a modular Python-based toolkit I created to simulate the kinds of tools and diagnostics used by IT support technicians and help desk analysts. The toolkit runs entirely from the command line and is structured as a multi-file CLI suite, offering core functions like system diagnostics, user checks, network testing, and basic log retrieval.

My goal was to build something more realistic and maintainable than a one-off script — something closer to what an actual internal IT support tool might look like. This project helped me deepen my understanding of system internals, Python scripting, and real-world help desk workflows.

## What I Learned

While building this toolkit, I:
- Used `psutil`, `platform`, and `socket` to gather hardware and system info
- Practiced subprocess handling to run OS-level commands like `ping` and `wevtutil`
- Built a basic CLI interface with modular files to simulate a real-world utility
- Learned how to structure a Python project with reusable modules and a main controller
- Gained experience with debugging cross-platform system commands

## Toolkit Features

-  **System Diagnostics**  
  Shows hostname, IP address, OS version, CPU/RAM usage, and system uptime

- **User Utilities**  
  Displays the current logged-in user

- **Network Tools**  
  Performs a ping test to a given domain or IP

- **Log Grabber**  
  Pulls the latest 10 entries from the Windows System Event Log (via `wevtutil`)

## File Structure

```
it_toolkit/
├── main.py              # CLI menu and controller
├── system_info.py       # System info functions
├── user_utils.py        # User account functions
├── network_tools.py     # Ping tool
├── log_grabber.py       # Event log tool
└── requirements.txt     # Dependencies (psutil)
```

## Tools Used

- Python 3.x  
- `psutil`, `platform`, `socket`, `subprocess`  
- Windows CLI commands (`ping`, `wevtutil`)  
- Manual testing and terminal-based interface

## Purpose

This project was built to mimic the practical tasks of an IT support technician: diagnosing system issues, verifying network access, identifying logged-in users, and capturing error logs. I wanted to prove not just that I could write code — but that I could write **support-relevant** tools that solve real-world problems.

It also taught me how to break problems down across modules and how to write reusable, readable code that could realistically be maintained by a team.
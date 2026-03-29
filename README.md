# Port Scanner v1

A simple port scanner written in Python that checks whether port 80 
is open or closed on a target IP address.

## Requirements

- Python 3.x
- IPy library → install with: pip install IPy

## How to Use

1. Clone or download this repository
2. Run the script: python portscanner.py
3. Enter the target IP address when prompted

## Example

[+] Enter Target IP To Scan: 192.168.1.1
[+] Port 80 is open

## How It Works

- Takes a target IP address as user input
- Uses Python's socket module to attempt a connection on port 80
- Reports whether the port is open or closed

## Planned Upgrades (v2)

- Scan a range of ports instead of just port 80
- Add support for scanning multiple targets
- Display results in a cleaner format

## Author

Roshan Ravichandran
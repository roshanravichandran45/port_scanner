# Port Scanner

A Python-based port scanner that scans a range of ports on a target IP or domain name.

## Version History
- **v2.0** - Added port range scanning, domain name support, and timeout
- **v1.0** - Basic single port (80) scanner

## Requirements

- Python 3.x
- IPy library → install with: pip install IPy

## How to Use

1. Clone or download this repository
2. Run the script: python portscanner.py
3. Enter the target IP address or domain name when prompted

## Example
```
[+] Enter Target To Scan: scanme.nmap.org
[-] Port 20 is closed
[-] Port 21 is closed
[+] Port 22 is open
...
[+] Port 80 is open
```

## How It Works

- Accepts both IP addresses and domain names as input
- If a domain name is entered, socket.gethostbyname() converts it to an IP address
- IPy library validates whether the input is already a valid IP address
- Uses Python's socket module to attempt a TCP connection on each port
- A timeout of 1 second per port keeps scans fast
- Reports whether each port is open or closed

## Features

### v2.0
- Scans a range of ports (currently 20-85)
- Accepts domain names as input and converts them to IP addresses
- 1 second timeout per port for faster scanning

### v1.0
- Scans port 80 only on a target IP address

## Tradeoffs
- A 1 second timeout means fast performance but risks missing ports 
that are slow to respond

## Planned Upgrades (v3)
- Let the user define the port range
- Show service names next to open ports (e.g. port 22 = SSH)
- Only print open ports to reduce noise

## Author
Roshan Ravichandran
# Network-Analysis-Tool
Network Analysis Script

Overview

This Python script provides essential network analysis tools, including fetching the IP address of a domain, printing the IPv4 route table, displaying netstat information, performing traceroutes, and executing pings to a given domain.

Features

Get IP of a domain: Retrieves the IP address of a specified domain.

Print IPv4 Route Table: Displays the current routing table.

Netstat Information: Shows active network connections.

Traceroute: Traces the path packets take to reach a domain.

Ping: Sends ICMP echo requests to test connectivity to a domain.

Requirements

Python 3.x

Operating System: Windows, Linux, or macOS

Usage

Clone or download the script.

Open a terminal and navigate to the script’s directory.

Run the script with the command:

python script.py

Enter the domain name when prompted.

The script will execute all network analysis functions sequentially.

Notes

Windows uses tracert instead of traceroute.

The script filters out IPv6 addresses in netstat and the route table.

Ensure you have the necessary permissions to execute network commands.



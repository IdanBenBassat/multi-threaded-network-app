# Multi-Threaded Server-Client Network Application

A concurrent, high-performance network application written in Python that supports multiple simultaneous client connections using TCP/IP protocol. This project demonstrates socket programming, multi-threading for dynamic connection handling, and network traffic optimization.

## Key Features
* **Multi-Threaded Architecture:** Utilizes Python's `threading` library to handle multiple client connections concurrently without blocking the main server process.
* **Socket Programming:** Implemented low-level TCP sockets to manage handshake, data transmission, and connection teardown.
* **Robust Exception Handling:** Gracefully handles unexpected client disconnections and network interruptions.
* **Network Analysis:** Packet transmission, latency, and protocol behaviors were analyzed and verified using Wireshark to ensure data integrity and stream optimization.

## Technologies Used
* **Language:** Python 3.x
* **Core Modules:** `socket`, `threading`, `sys`
* **Tools:** Wireshark (Network Analysis), Terminal / Command Line

## How to Run
Clone the repository:
   ```bash
   git clone [https://github.com/IdanBenBassat/multi-threaded-network-app.git](https://github.com/IdanBenBassat/multi-threaded-network-app.git)

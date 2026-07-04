# 🌐 Network Troubleshooting Simulator

A Python-based GUI application that simulates real-world network diagnostics tools such as Internet connectivity check, Ping test, DNS lookup, and IP configuration viewer. Built using Tkinter with a modular backend design.

---

## 🚀 Features

- 🌍 Internet Connectivity Check
- 📡 Ping Test for any host (IP/Domain)
- 🔎 DNS Lookup (Domain to IP resolution)
- 🧾 IP Configuration Display
- 📊 Progress bar for task tracking
- 📝 Activity logging system
- 💾 Export diagnostic reports
- 🎨 Clean GUI using Tkinter

---

## 🛠️ Tech Stack

- Python 3
- Tkinter (GUI)
- OS / socket libraries (network operations)
- File handling for logging & reports

---

## 📁 Project Structure
project/
│
├── gui.py # Main GUI application
├── network_tools.py # Network functions (ping, dns, internet check)
├── styles.py # UI styling (colors, fonts)
├── report.py # Logging and report generation


---

## ▶️ How to Run

1. Clone the repository:git clone https://github.com/Samruddhi-1605/Network-Troubleshooting-Simulator.git

2. Navigate to project folder:

cd network-simulator

3. Run the application:

python gui.py


---

## 📌 Functional Overview

### 🌍 Internet Check
Checks whether the system is connected to the internet and updates status in real time.

### 📡 Ping Test
Sends ICMP requests to a given host and returns response time or failure message.

### 🔎 DNS Lookup
Resolves domain names into IP addresses using system DNS.

### 🧾 IP Configuration
Displays system network configuration details.

---

## 📊 Logging System

All user actions (tests performed) are automatically logged for tracking and debugging.

---

## 💡 Future Improvements

- Real-time network speed graph
- Dark mode UI
- Advanced traceroute visualization
- API-based network monitoring dashboard

---

import socket
import subprocess
import platform
import requests
import uuid
import speedtest

# ==========================
# Check Internet Connection
# ==========================

def check_internet():

    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True

    except OSError:
        return False


# ==========================
# Ping Test
# ==========================

def ping(host):

    parameter = "-n" if platform.system().lower() == "windows" else "-c"

    command = [
        "ping",
        parameter,
        "4",
        host
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    return result.stdout


# ==========================
# DNS Lookup
# ==========================

def dns_lookup(host):

    try:
        return socket.gethostbyname(host)

    except socket.gaierror:
        return None


# ==========================
# IP Configuration
# ==========================

def ip_config():

    if platform.system().lower() == "windows":

        command = "ipconfig"

    else:

        command = "ifconfig"

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        shell=True
    )

    return result.stdout


# ==========================
# Public IP Address
# ==========================

def public_ip():

    try:

        response = requests.get(
            "https://api.ipify.org",
            timeout=5
        )

        return response.text

    except Exception:

        return "Unable to fetch Public IP"


# ==========================
# System Information
# ==========================

def system_info():

    info = ""

    info += f"Operating System : {platform.system()}\n"

    info += f"Release : {platform.release()}\n"

    info += f"Version : {platform.version()}\n"

    info += f"Machine : {platform.machine()}\n"

    info += f"Processor : {platform.processor()}\n"

    info += f"Python Version : {platform.python_version()}\n"

    return info

def network_information():

    hostname = socket.gethostname()

    try:
        local_ip = socket.gethostbyname(hostname)
    except Exception:
        local_ip = "Unavailable"

    mac = ":".join([
        "{:02X}".format((uuid.getnode() >> ele) & 0xff)
        for ele in range(40, -8, -8)
    ])

    info = (
        f"Computer Name : {hostname}\n\n"
        f"Local IP Address : {local_ip}\n\n"
        f"MAC Address : {mac}"
    )

    return info
# ==========================
# Internet Speed Test
# ==========================

def speed_test():

    try:

        st = speedtest.Speedtest()

        st.get_best_server()

        download = st.download() / 1000000
        upload = st.upload() / 1000000
        ping = st.results.ping

        result = (
            "========== INTERNET SPEED ==========\n\n"
            f"Download Speed : {download:.2f} Mbps\n\n"
            f"Upload Speed : {upload:.2f} Mbps\n\n"
            f"Ping : {ping:.2f} ms"
        )

        return result

    except Exception as e:

        return f"Error:\n\n{e}"
    # ==========================
# Common Port Scanner
# ==========================

def port_scan(host):

    ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        3306: "MySQL",
        3389: "Remote Desktop"
    }

    result = ""

    try:

        ip = socket.gethostbyname(host)

        result += f"Target : {host}\n"
        result += f"IP Address : {ip}\n\n"

        for port, service in ports.items():

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            status = sock.connect_ex((ip, port))

            if status == 0:
                result += f"Port {port:<5} ({service}) : OPEN\n"
            else:
                result += f"Port {port:<5} ({service}) : CLOSED\n"

            sock.close()

    except Exception as e:

        result = f"Error:\n{e}"

    return result
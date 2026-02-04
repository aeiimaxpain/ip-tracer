#!/usr/bin/env python3
# Ethical IP Intelligence Tool – OSINT ONLY

import requests
import socket
import statistics
import sys
import time
from ping3 import ping
from colorama import Fore, Style, init

init(autoreset=True)

API_URL = "https://ipwho.is/{}"
PING_COUNT = 5
PING_TIMEOUT = 2
FADE_DELAY = 0.0001


# ------------------ Animation ------------------
def fade_print(text, delay=FADE_DELAY, color=""):
    for c in text:
        sys.stdout.write(color + c)
        sys.stdout.flush()
        time.sleep(delay)
    print(Style.RESET_ALL)


# ------------------ Utilities ------------------
def resolve_target(target):
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        return None


def reverse_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Unavailable"


def fetch_ip_data(ip):
    try:
        r = requests.get(API_URL.format(ip), timeout=10)
        data = r.json()
        if not data.get("success", True):
            return None
        return data
    except:
        return None


def average_ping(ip):
    results = []
    for _ in range(PING_COUNT):
        res = ping(ip, timeout=PING_TIMEOUT)
        if res:
            results.append(res * 1000)
    return round(statistics.mean(results), 2) if results else None


def classify_network(security):
    if security.get("tor"):
        return "Tor Exit Node"
    if security.get("proxy"):
        return "VPN / Proxy"
    if security.get("hosting"):
        return "Hosting / Datacenter"
    if security.get("mobile"):
        return "Mobile Network"
    return "Residential / ISP"


# ------------------ Report ------------------
def print_report(ip, data, avg_ping):
    security = data.get("security", {})
    conn = data.get("connection", {})

    fade_print("\n========== IP INTELLIGENCE REPORT ==========\n", 0.002, Fore.CYAN)

    fade_print(f"Target IP        : {ip}", color=Fore.GREEN)
    fade_print(f"Reverse DNS      : {reverse_dns(ip)}")
    fade_print(f"ISP              : {data.get('isp', 'Unknown')}")
    fade_print(f"ASN              : {conn.get('asn', 'Unknown')}")
    fade_print(f"Organization     : {conn.get('org', 'Unknown')}")

    fade_print("\n--- Location ---", 0.004, Fore.YELLOW)
    fade_print(f"Country          : {data.get('country')} ({data.get('country_code')})")
    fade_print(f"State / Region   : {data.get('region')}")
    fade_print(f"City / Locality  : {data.get('city')}")
    fade_print(f"Pincode / ZIP    : {data.get('postal')}")
    fade_print(f"Coordinates      : {data.get('latitude')}, {data.get('longitude')}")
    fade_print(f"Timezone         : {data.get('timezone', {}).get('id')}")

    fade_print("\n--- Network Intelligence ---", 0.004, Fore.YELLOW)
    fade_print(f"Network Type     : {classify_network(security)}")
    fade_print(f"Proxy            : {security.get('proxy', False)}")
    fade_print(f"Hosting          : {security.get('hosting', False)}")
    fade_print(f"Mobile           : {security.get('mobile', False)}")
    fade_print(f"Tor              : {security.get('tor', False)}")

    fade_print("\n--- Performance ---", 0.004, Fore.YELLOW)
    if avg_ping:
        fade_print(f"Average Ping     : {avg_ping} ms")
    else:
        fade_print("Average Ping     : ICMP Blocked / Unreachable")

    fade_print("\n===========================================\n", 0.002, Fore.CYAN)


# ------------------ Main ------------------
def main():
    fade_print("Ethical IP Intelligence Tool (OSINT)", 0.004, Fore.YELLOW)
    target = input("Enter IP or Domain: ").strip()

    ip = resolve_target(target) if not target.replace(".", "").isdigit() else target
    if not ip:
        fade_print("Invalid IP or domain.", color=Fore.RED)
        return

    data = fetch_ip_data(ip)
    if not data:
        fade_print("Failed to retrieve intelligence.", color=Fore.RED)
        return

    avg_ping = average_ping(ip)
    print_report(ip, data, avg_ping)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted.")
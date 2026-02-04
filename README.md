
# IP-INTEL 🛰️  
**Ethical IP Intelligence Tool (OSINT-Only)**

A production-ready Python tool for collecting **ethical, open-source intelligence (OSINT)** about an IP address or domain.  
Built for **Termux**, Linux, and security-focused workflows.

> ⚠️ This tool performs **NO scanning, NO exploitation, NO intrusion**.  
> It uses **public OSINT APIs only** and is intended for **education, defense, and research**.

---

## ✨ Features
- IP / Domain resolution  
- ISP, ASN & Organization  
- Country, State, City, ZIP  
- Latitude & Longitude  
- Timezone detection  
- Network classification:
  - Residential
  - Hosting / Datacenter
  - VPN / Proxy
  - Mobile
  - Tor Exit Node
- Security flags (proxy, hosting, mobile, tor)  
- Reverse DNS lookup  
- Average ICMP ping  
- Smooth **fade-in terminal animation**  
- Fully **Termux-compatible**  

---

## 📸 Preview

========== IP INTELLIGENCE REPORT ========== Target IP        : 69.57.xxx.xxx ISP              : Hosting Provider Country          : India (IN) State / Region   : Maharashtra City / Locality  : Navi Mumbai Network Type     : Hosting / Datacenter Average Ping     : 41.23 ms

---

## 🛠 Requirements
- Python **3.8+**
- Internet connection

### Python Dependencies

requests ping3 colorama

---

## 📦 Installation (Termux)

```bash
pkg update -y
pkg install python -y
pip install -r requirements.txt
```

---

▶ Usage

chmod +x ip_intel.py
./ip_intel.py

Then enter:
```

IP address  → 8.8.8.8
or
Domain      → example.com

```
---

🧠 How It Works

Geolocation & ISP data from ipwho.is

Latency measurement using ICMP echo

DNS resolution via Python socket

Network type classification via OSINT security flags


No packets are sent other than:

DNS resolution

ICMP ping (optional, may be blocked)



---

🔐 Ethical & Legal Notice

This tool is designed strictly for:

Defensive security

Research & learning

Network diagnostics

OSINT investigations


🚫 Do NOT use this tool for:

Tracking individuals

Unauthorized monitoring

Harassment or surveillance

Illegal activities


The developer is not responsible for misuse.




🚀 Future Enhancements

Planned upgrades:

JSON / CSV export

AbuseIPDB reputation score

VirusTotal integration

Batch IP scanning

CLI flags (--json, --silent)

pip-installable package

Web dashboard / API


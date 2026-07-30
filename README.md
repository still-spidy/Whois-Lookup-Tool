# WHOIS Lookup Tool

A simple Python-based WHOIS Lookup Tool that retrieves domain registration information using the `python-whois` library.

## Features

- Retrieve domain registration details
- Display:
  - Domain Name
  - Creation Date
  - Updated Date
  - Expiration Date
  - Name Servers
  - Contact Emails (if available)
  - Registrant Information (if available)
- Gracefully handles missing information
- Basic error handling for invalid or unavailable domains

---

## Installation

### Clone the repository

```bash
git clone https://github.com/still-spidy/Whois-Lookup-Tool.git
cd whois-lookup-tool
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Run the program using:

```bash
python main.py
```

Enter a domain name when prompted.

Example:

```text
Enter Domain Name: google.com
```

---

## Example Output

```text
========================
WHOIS Lookup Result
========================

Domain Name:    GOOGLE.COM
Creation On:    1997-09-15 00:00:00
Updated On:     2019-09-09 15:39:04
Expired On:     2028-09-14 04:00:00

Name Servers:
- ns1.google.com
- ns2.google.com
- ns3.google.com
- ns4.google.com

Emails:
dns-admin@google.com

Org:    Google LLC
Country:    US
```

---

## Requirements

- Python 3.8+
- `python-whois`

---

## Project Structure

```
whois-lookup-tool/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Notes

- Some WHOIS records may not contain all fields.
- The available information depends on the domain registrar and registry.
- Some domains may hide registrant details for privacy reasons.

---



## Disclaimer

This project is intended for educational purposes only. Use it only on systems that you own or have permission to test.

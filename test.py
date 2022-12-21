import os

pattern = r"\b\d{1,}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"


output = os.popen("ip route").read()
print("here")

import re


pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

match = re.search(pattern, output)
if match:
    print(match.group())
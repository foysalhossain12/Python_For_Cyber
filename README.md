# -------------------------------- Python Code For Cyber Security -------------------------------

# Base64 decoded from 50 times

import base64

#Open file
with open('b64.txt') as f:
    msg = f.read()

#Decode 50 times
for _ in range(50):
    msg = base64.b64decode(msg)

print(f"The flag is: {msg.decode('utf8')}")

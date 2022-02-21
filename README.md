#  Python Code For Cyber Security And CTF 

# Base64 decoded from 50 times

import base64![github](https://user-images.githubusercontent.com/55437834/155027715-ea73d994-8316-4ae2-80d8-fc051e35fdac.png)



with open('b64.txt') as f:
    msg = f.read()


for _ in range(50):
    msg = base64.b64decode(msg)

print(f"The flag is: {msg.decode('utf8')}")

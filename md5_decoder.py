import hashlib
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Md5 Cracker\n")

print(ascii_banner)

wordlist = str(input("Enter Wordlist file location:"))

hash_value = str(input("Enter Hash to be Cracked:"))

with open(wordlist,'r') as file :

    for line in file.readlines():
        hash_ob = hashlib.md5(line.strip().encode())
        hashed_pass = hash_ob.hexdigest()
        if hashed_pass ==hash_value:
            print('Found cleartext Password:'+line.strip())
            exit(0)

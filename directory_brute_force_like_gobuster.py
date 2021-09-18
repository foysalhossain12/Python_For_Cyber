import requests
import sys

sub_list = open("wordlist2.txt").read()

directories = sub_list.splitlines()


for dir in directories:
    dir_enum = f"http://{sys.argv[1]}/{dir}.html"

    r = requests.get(dir_enum)

    if r.status_code==404:
        pass
    else:
        print("Valid Directory:",dir_enum)

#Run Command :python3 create_python_file target_ip

#!/usr/bin/env python3



#Get any website source code just one click 

import turtle # import package
import urllib.request as u

website_Domain = turtle.textinput("Domain Name ","Url Address") # animation input from user



source_code = u.urlopen(website_Domain)
source_code_read = source_code.read()


print(source_code_read) # print source code

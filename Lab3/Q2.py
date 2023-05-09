import os
import hashlib


with open('Q2hash.txt', 'r') as f:
    oghash = f.read().strip()

for file in os.listdir("/home/cse/Lab3/Q2files"):
    with open(os.path.join("/home/cse/Lab3/Q2files", file), 'rb') as f:
        file_contents = f.read()
        hash_obj = hashlib.sha256()
        hash_obj.update(file_contents)
        hashvalue = hash_obj.hexdigest()
        if hashvalue == oghash:
            print(file)
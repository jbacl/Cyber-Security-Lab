import os

f = open("test.txt", 'w')
for file in os.listdir('/home/cse/Lab2/Solutions'):
    if file.endswith('.py'):
        f.write(file + '\n')


















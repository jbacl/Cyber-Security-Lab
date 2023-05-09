from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Hash import MD5

with open('Encrypted5', 'rb') as file_in:
   iv = file_in.read(AES.block_size)
   encrypted_data = file_in.read()

BLOCKSIZE = 2048
md = MD5.new()
i = 0

with open( 'R5.py' , 'rb') as afile:
   buf = afile.read(BLOCKSIZE)
   while len(buf) > 0:
       md.update(buf)
       buf = afile.read(BLOCKSIZE)
       i += 1

key = md.digest()
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
de_data = cipher.decrypt(encrypted_data)
de_data = unpad(de_data, AES.block_size)

with open('Q5a', 'w') as file_out:
   file_out.write(de_data.decode('utf-8'))

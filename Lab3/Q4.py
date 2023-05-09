from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

with open('.key.txt', 'rb') as k_file:
   k = k_file.read()
with open('Encrypted4', 'rb') as f_in:
   iv = f_in.read(16)
   encrypted_data = f_in.read()

cipher = AES.new(k, AES.MODE_CBC, iv=iv)
d_data = cipher.decrypt(encrypted_data)
d_data = unpad(d_data, AES.block_size)

with open('Q4a', 'w') as file_out:
   file_out.write(d_data.decode('utf-8'))

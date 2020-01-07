
from cryptography.fernet import Fernet

key = Fernet.generate_key()
read_file = open('test.txt', 'r')
write_file = open('unreadable.txt', 'w')

f = Fernet(key)
token = f.encrypt(b"a secret message")
print(token)
print(f.decrypt(token))



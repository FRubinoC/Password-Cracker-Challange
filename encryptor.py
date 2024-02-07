import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
passwd = b"........"
cleartext = b"............."
salt = os.urandom(16)
print('salt = ',salt)
kdf = PBKDF2HMAC(
 algorithm=hashes.SHA256(),
 length=32,
 salt=salt,
 iterations=100000,
)
key = base64.urlsafe_b64encode(kdf.derive(passwd))
f = Fernet(key)
cyphertext = f.encrypt(cleartext)
print('cyphertext = ', cyphertext)
print(f.decrypt(cyphertext))

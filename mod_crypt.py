from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)

with open('FILENAME.DAT', 'rb') as file:
    original = file.read()

# encrypting the file
encrypted = fernet.encrypt(original)

# opening the file in write mode and
# wrigint the encrypted data
with open('FILENAME.DAT', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

# http://geeksforgeeks.org/encrypt-and-decrypt-files-using-python/
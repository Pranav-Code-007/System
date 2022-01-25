import hashlib


# s = "One man"
# s = hashlib.sha256(s.encode())
# print(type(s.hexdigest()))
# print(len(s.hexdigest()))
def encrypt(passwd):
    s = hashlib.sha256(passwd.encode())
    return s.hexdigest()

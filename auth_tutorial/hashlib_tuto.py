import hashlib

pw = input()
print(pw)

hashed_pw = hashlib.sha256(pw.encode("utf-8")).hexdigest()
print(hashed_pw)

import hashlib

lala = hashlib.new("sha384",b'LALALA').hexdigest()

print(lala)
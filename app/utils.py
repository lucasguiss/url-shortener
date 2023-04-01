import hashlib

def hash(text):
    return hashlib.shake_256(text.encode('utf-8')).hexdigest(3)
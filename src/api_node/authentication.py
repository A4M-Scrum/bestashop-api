import os, hashlib

def pass_encode(password:str,salt:bytes|None = None) -> list[bytes]:
    if not salt:
        salt = os.urandom(32) #Numeros aleatorios
    coded_password = hashlib.pbkdf2_hmac("sha256",password.encode(),salt,256)
    return [coded_password.hex(),salt.hex()]

def pass_confirm(password:str,og_info: list):
    salt = bytes.fromhex(og_info[1])
    a_coded_password = og_info[0]
    b_coded_password = hashlib.pbkdf2_hmac("sha256",password.encode(),salt,256).hex()
    return a_coded_password == b_coded_password

if __name__ == "__main__":
    pass_encode('')
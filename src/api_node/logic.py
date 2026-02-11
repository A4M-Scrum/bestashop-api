from dataclasses import dataclass
import os, hashlib

@dataclass
class producto:
    pass

@dataclass
class pedido:
    pass

def pass_confirm():

    pass

def pass_encode(password:str,salt:bytes|None = None) -> list[bytes]:
    if not salt:
        salt = os.urandom(32) #Numeros aleatorios
        print(f'salt: {salt}\n')
    coded_password = hashlib.pbkdf2_hmac("sha256",password.encode(),salt,32)
    return [coded_password,salt]

def pass_decode(password:str,og_info: list):
    b_password = password.encode()
    b_coded_password = hashlib.pbkdf2_hmac("sha256",b_password,og_info[1],32)
    a_coded_password = hashlib.pbkdf2_hmac("sha256",og_info[0],og_info[1],32)
    print(f'A: {a_coded_password}\nB: {b_coded_password}')
    print(a_coded_password == b_coded_password)

if __name__ == "__main__":
    for _ in range(2):
        s = pass_encode("Sasha")
        print(s)
        pass_decode('Sasha',s)
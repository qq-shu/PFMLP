import numpy as np 
from phe import paillier

def create_key_pair():
    public_key, private_key = paillier.generate_paillier_keypair()
    return public_key,private_key

def encrypt_func(public_key,secret_number_list):
    encrypted_number_list = [public_key.encrypt(x) for x in secret_number_list]
    return encrypted_number_list

def decrypt_func(private_key,encrypted_number_list):
    decrypted_number_list = [private_key.decrypt(x) for x in encrypted_number_list]
    return decrypted_number_list

# if __name__ == "__main__":
#     public_key, private_key = create_key_pair()
#     secret_number_list = np.array([3.141592653, 300, -4.6e-12])
#     encrypted_number_list = encrypt_func(public_key,secret_number_list)
#     print('[+] encrypted_number_list: ',encrypted_number_list)
#     decrypted_number_list = decrypt_func(private_key,encrypted_number_list)
#     print('[-] decrypted_number_list: ',decrypted_number_list)
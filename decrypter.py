import os
import pyaes

# Função para descriptografar um arquivo
def decrypt_file(encrypted_file, decryption_key):
    # Abrir o arquivo criptografado
    with open(encrypted_file, "rb") as enc_file:
        encrypted_data = enc_file.read()
    
    # Inicializar o objeto AES com a chave fornecida
    aes_cipher = pyaes.AESModeOfOperationCTR(decryption_key)
    decrypted_data = aes_cipher.decrypt(encrypted_data)
    
    # Retornar os dados descriptografados
    return decrypted_data

# Nome do arquivo criptografado
encrypted_file_name = "teste.txt.ransomwaretroll"
# Chave para a descriptografia
decryption_key = b"testeransomwares"

# Chamar a função de descriptografia
decrypted_content = decrypt_file(encrypted_file_name, decryption_key)

# Remover o arquivo criptografado
os.remove(encrypted_file_name)

# Criar um novo arquivo com os dados descriptografados
with open("teste.txt", "wb") as new_file:
    new_file.write(decrypted_content)

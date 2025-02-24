# Ransomware em Python: Criptografia e Descriptografia de Arquivos

Este repositório contém dois scripts em Python que demonstram a implementação de um ransomware básico, utilizando o algoritmo AES (Advanced Encryption Standard) no modo CTR (Counter) para criptografar e descriptografar arquivos. Os scripts utilizam a biblioteca `pyaes` para realizar a criptografia simétrica, permitindo a proteção de arquivos sensíveis.

# Funcionalidades

1. **Criptografia de Arquivos**:
   - O script `encrypt.py` lê um arquivo de texto (`teste.txt`), criptografa seu conteúdo utilizando uma chave predefinida e salva o resultado em um novo arquivo com a extensão `.ransomwaretroll`.
   - Após a criptografia, o arquivo original é removido, o que é uma característica típica de ransomware.

2. **Descriptografia de Arquivos**:
   - O script `decrypt.py` lê um arquivo criptografado (`teste.txt.ransomwaretroll`), descriptografa seu conteúdo com a mesma chave utilizada na criptografia e salva o resultado em um novo arquivo (`teste.txt`).
   - O arquivo criptografado é removido após a descriptografia.

# Dependências

- Python 3.x
- Biblioteca `pyaes`

# Instalação

Para utilizar os scripts, você precisará ter o Python instalado em sua máquina. Além disso, instale a biblioteca `pyaes` usando o seguinte comando:

```bash
pip install pyaes
```

# Uso

1. Para criptografar um arquivo, execute o script `encrypt.py`.
2. Para descriptografar um arquivo, execute o script `decrypt.py`.

# Atenção
Este repositório contém um exemplo de ransomware, destinado apenas para fins educacionais e de demonstração. O uso de ransomware é ilegal e antiético. Esteja ciente das implicações legais e éticas antes de explorar ou desenvolver software de criptografia.


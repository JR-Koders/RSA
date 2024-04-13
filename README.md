# RSA Python Script

This Python script package contains utilities for RSA encryption and decryption.

## RSA Key Generation (`RSAkeygen.py`)

The `RSAkeygen.py` script is designed to generate RSA key pairs. To execute it, simply run:

```bash
python RSAkeygen.py
```

By default, the script generates RSA keys with a key size of 2048 bits. However, if you wish to specify a different key size, you can use the `-keySize` option. Note that key sizes above 2048 bits may take a significantly longer time to generate.

### Usage:

```bash
python RSAkeygen.py [-keySize <size>]
```
#### Exemple:
```bash
python RSAkeygen.py -1024
```

## RSA Encryption and Decryption (`rsa.py`)

The `rsa.py` script provides functionalities for encrypting and decrypting messages using RSA keys previously generated. It offers options to either encrypt (`e`) or decrypt (`d`) messages.

### Usage:

```bash
python rsa.py
```

You will be prompted wether you want to encrypt or decrypt a message


When encrypting or decrypting, you have the choice to input keys from a file or directly in the terminal.

### Output Options:

- **Terminal:** The encrypted or decrypted message can be output directly to the terminal.
- **File:** Alternatively, you can choose to output the encrypted message to a file named `message.encrypted`.

Feel free to explore and utilize these scripts to secure your communications with RSA encryption! 🔒🔑

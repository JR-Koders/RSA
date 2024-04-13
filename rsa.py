import subprocess
# from StringToDigits import StringToDigits

Digits = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        #   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        #   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
          1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '&', 'é', ' ', '~', '"', '#', "'",
          '{', '(', '[', "-", "|", "è", "`", "_", "\\", "ç", "^", "à", "@",
          ")", "°", "]", "+", "=", "}", "¨", "$", "£", "¤", "%", "ù", "µ",
          "*", "<", ">", ",", "?", ".", ";", ":", "/", "!", "§"]

def StringToDigits(string):
    num = 0
    # check wether a the character is a letter or a digit
    def check(string):
        # return isinstance(string, int)
        try:
            float(string)
            return True
        except ValueError:
            return False
    
    # do this for all characters in the sentence to turn into digits
    for i in string:
        # if it is a digit then turn it into int because else it will be considered a letter
        if (check(i) == True): 
            i = int(i)
        # calculate the number to add using the position in the list + 10 to avoid numbers under 10
        toAdd = str(Digits.index(i.lower()) + 10)
        # if (len(toAdd) < 2):
        #     toAdd = str(0) + toAdd
        # add the toAdd val to the end of the number
        num = int(str(num) + toAdd)
    # return a number
    return num

def DigitsToString(val):
    # from list_string_digits import Digits
    num = str(val)
    # final string
    string = ""
    toAdd = 0
    for i in range (0, int(len(num) / 2)):
        # this line gets the position of the character using the two digits; -10 because at the encoding there was a +10
        toAdd = int(str(num[i*2]) + str(num[i*2+1])) - 10
        # add the value to the final string
        string = str(string) + str(Digits[toAdd])
    # return a string value
    return string


def encrypt():
    message = input("\nWhat do you want to encrypt? ")

    # turn the message into a number
    m = int(StringToDigits(message))
    print("Message to encrypt:", m)

    FileOrTerm = input("\nDo you want to specify the public key from a file (key.pub) or from the terminal? (f/t) ")
   
    while(FileOrTerm != 'f' and FileOrTerm != 't'):
        print("Please enter a valid input!")
        FileOrTerm = input("\nDo you want to specify the public key from a file (key.pub) or from the terminal? (f/t) ")

    if FileOrTerm == 'f':
        publicKeyFile = input('\nEnter your public key file path (should be key.pub) ')
        n, e = getValueFromFile(publicKeyFile, "public")
    else:
        # Encrypt data
        print("\nPlease enter your public keys: ")
        # get the public keys from the user
        e = int(input("Please enter e: ")) # small number
        n = int(input("Please enter n: ")) # big pseudo prime number
    
    # encrypt the data
    c = pow(m, e, n)
    
    FileOrTerm = input("\nDo you want to output the encrypted message to a file or to the terminal? (f/t) ")
   
    while(FileOrTerm != 'f' and FileOrTerm != 't'):
        print("Please enter a valid input!")
        FileOrTerm = input("\nDo you want to output the encrypted message to a file or to the terminal? (f/t) ")

    if FileOrTerm == 'f':
        with open('message.encrypted', 'w') as f:
            f.write('-----BEGIN ENCRYPTED MESSAGE-----')
            f.write(str(c))
            f.write('-----END ENCRYPTED MESSAGE-----')
    else:
        print("\nEncrypted message:", str(c))

def getValueFromFile(file: str, type: str):
    try:
        if type == "private": # if we want the priv keys
            with open(file, 'r') as f:
                content = f.read()
                content = content.split("-----")[2] # should be the content of the file without --begin-- --end--
                d = content.split(":")[1]
            return int(d)
        elif type == "public":
            with open(file, 'r') as f:
                content = f.read()
                content = content.split("-----")[2] # should be the content of the file without --begin-- --end--
                content = content.split(":")
                n = content[1]
                e = content[3]
            return int(n.strip()), int(e.strip())
        elif type == "message": # if we want the priv keys
            with open(file, 'r') as f:
                content = f.read()
                message = content.split("-----")[2] # should be the content of the file without --begin-- --end--
            return int(message)
    except:
        print('\nThere was a problem retrieving the keys from files!\nPlease ensure you didn\'t change the content of the generated files')


def decrypt():
    
    # get the number to decrypt from the user
    FileOrTerm = input("\nDo you want to specify the message from a file or from the terminal? (f/t) ")
   
    while(FileOrTerm != 'f' and FileOrTerm != 't'):
        print("Please enter a valid input!")
        FileOrTerm = input("\nDo you want to specify the message from a file or from the terminal? (f/t) ")

    if FileOrTerm == 'f':
        messageFile = input('\nEnter your message file path (should be message.encrypted) ')
        toDecrypt = getValueFromFile(messageFile, "message")
    else:
        toDecrypt = int(input('What do you want to decrypt? '))

    FileOrTerm = input("\nDo you want to specify the keys from files (key.priv, key.pub) or from the terminal? (f/t) ")
   
    while(FileOrTerm != 'f' and FileOrTerm != 't'):
        print("Please enter a valid input!")
        FileOrTerm = input("\nDo you want to specify the keys from files (key.priv, key.pub) or from the terminal? (f/t) ")

    if FileOrTerm == 'f':
        privateKeyFile = input('\nEnter your private key file path (should be key.priv) ')
        d = getValueFromFile(privateKeyFile, "private")
        publicKeyFile = input('\nEnter your public key file path (should be key.pub) ')
        n = getValueFromFile(publicKeyFile, "public")[0]
    else:
        print("\nPlease enter your private keys:")
        # get the private keys from the user
        d = int(input("Please enter d (private key): ")) # big pseudo prime number
        n = int(input("Please enter n (public key): ")) # big pseudo prime number
    
    # decrypt the number using the private keys
    decrypted = pow(toDecrypt, d, n)

    # print the decrypted number
    print("\nDecrypted value:", decrypted)
    # from StringToDigits import DigitsToString
    # turn the decrypted number into a string
    result = DigitsToString(decrypted)
    print("\nFinal value:", result)


print("\nDon't forget, you need public keys only to encrypt, and private keys only to decrypt. Never share your private key!")
EncryptOrDecrypt = input("\nWhat do you want to do, encrypt or decrypt? (e/d) ")

while(EncryptOrDecrypt != 'e' and EncryptOrDecrypt != 'd'):
    print("\nPlease enter a valid input!")
    EncryptOrDecrypt = input("\nWhat do you want to do, encrypt or decrypt? (e/d) ")

if (EncryptOrDecrypt == 'e'):
    encrypt()
elif(EncryptOrDecrypt == 'd'):
    decrypt()
import subprocess, os, sys
from primeNumGen import getBigPrime

def calculate_d(e, phi):
   def egcd(a, b):
      if a == 0:
         return (b, 0, 1)
      g, y, x = egcd(b%a,a)
      return (g, x - (b//a) * y, y)

   def modinv(a, m):
      g, x, y = egcd(a, m)
      if g != 1:
         raise Exception('No modular inverse')
      return x%m

   return modinv(e, phi)

def execute_python_file(file_path):
   try:
      completed_process = subprocess.run(['python', file_path], capture_output=True, text=True)
      if completed_process.returncode == 0:
         return int(completed_process.stdout)
      else:
         print(f"Error: Failed to execute '{file_path}' .")
         print("Error output:")
         print(completed_process.stderr)
   except FileNotFoundError:
      print(f"Error: The file '{file_path}'  does not exist.")

def calculateKeys():
   # Calculate P, Q, n, and phi
   P = getBigPrime(bits=bits)
   Q = getBigPrime(bits=bits)
   n = P*Q
   phi = (P-1)*(Q-1)

   # Calculate E
   e = 65537

   # Calculate D
   d = calculate_d(e, phi)

   return (n, e, d)


YesOrNo = input("\nDo you want to generate rsa encryption keys? (y/n) ")

try:
   bits = sys.argv[1]
   bits = int(bits[1:])
   print(f"\nYou want {bits} bit keys")
except:
   print(f"\nYou didn't specify a number of bits using -bits, defaulting to 2048")
   bits = 2048

while(YesOrNo != 'y' and YesOrNo != 'n'):
   print("Please enter a valid input!")
   YesOrNo = input("\nDo you want to generate rsa encryption keys? (y/n) ")

if (YesOrNo == 'n'):
   print("\nIf you changed your mind, re-run the script!\n")
   print("Programm killed!\n")
   exit()
elif (YesOrNo == 'y'):

   FileOrTerm = input("\nDo you want to output the keys to files (key.priv, key.pub) or to the terminal? (f/t) ")
   
   while(FileOrTerm != 'f' and FileOrTerm != 't'):
      print("Please enter a valid input!")
      FileOrTerm = input("\nDo you want to output the keys to files (key.priv, key.pub) or to the terminal? (f/t) ")

   print("\n\tCalcultating keys...\n")
   n, e, d = calculateKeys()

   if (FileOrTerm == 'f'):
      print("\nOutputting the keys to files!\n")
      with open('key.pub', 'w') as f:
         f.write("-----PUBLIC KEYS BEGIN-----")
         f.write(f"n:{n}:")
         f.write(f"e:{e}")
         f.write("-----PUBLIC KEYS END-----")
      with open('key.priv', 'w') as f:
         f.write("-----PRIVATE KEY BEGIN-----")
         f.write(f"d:{d}")
         f.write("-----PRIVATE KEY END-----")
   else:
      print("\nOutputting the keys to the terminal!\n")
      print("Public Key:", "\nn :\n", n, "\ne :\n", e)
      print("\nPrivate Key:", "\nd :\n", d)
   print("\n\nPlease keep the private key for you and only give the public key!\n")


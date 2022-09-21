import string as s
import re
string = input("Please enter your string to encrypt: ")
key = input("Please enter your key(all symbols and white spaces will be removed): ")
# alphabet accounting for white space
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
string = string.upper()
key = key.upper()
# removes all symbols except white space
string = re.sub(r'[^\w ]', ' ', string)
# filter through key and check if it is alphabetical, if so add to empty key string
key = "".join(filter(str.isalpha, key))

print("\nInputs\n---------------------\nString after adjustments: ", string)
print("Key after adjustments: ", key)


def iterate_key(string, key):
    key = list(key)  # turning key variable from string to list
    if len(string) == len(key):  # check to see if the string length matches key length
      return key
    else: # if string length does not equal key length, repeat until it does
      for i in range(len(string) - len(key)):  # iterating the amount needed to append to the key list
        key.append(key[i % len(key)])  # using mod to index through key allowing us to repeat once we reach the end of key elements
    return "".join(key)  # joins elements of list together into a string with no delimiter in between each element


def encrypt(string, key):
  cipher = []  # initialize empty list
  for i in range(len(string)):
    cipherElem = alphabet.index(string[i])+alphabet.index(key[i])  # taking string letter and looking for it in alphabet list then returning its index, do the same for the key letter and add the two indexes
    cipher.append(alphabet[cipherElem % 27])  # take the new index and mod 27(for every letter of alphabet accounting for whitespace) it in order for it to be able to loop through alphabet, use the resulting index to search for the letter in alphabet list then append it to the cipher list
  return "".join(cipher)  # join cipher list together into a string with no delimiter


def decrypt(cipher, key):
  decrypted = []
  for i in range(len(cipher)):
    decrypted_elem = alphabet.index(cipher[i])-alphabet.index(key[i])  # taking string letter from cipher text and looking for it in alphabet to return its index, subtract key index to get original string letter
    decrypted.append(alphabet[decrypted_elem % 27])  # mod the new index to loop through alphabet then plug that new index into the alphabet to get its letter
  return "".join(decrypted)  # join decrypted list into a string with no delimiter


key = iterate_key(string, key)  # call iteration function to get formatted key
cipher = encrypt(string, key)  # call encryption function to get cipher
message = decrypt(cipher, key)  # call decrypt function to get original message
print("Iterated Key: ",key)
print("\nOutputs\n---------------------\nCipher: ", cipher)
print("Message: ", message)

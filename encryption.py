from encodings import utf_8
from hashlib import sha256
import os
os.system('cls')
print ("[1] Chiffrer")
print ("[2] Déchiffrer")
option = int(input("Entrez l'option que vous voulez: "))
if option == 1 :
    entree = input("Entrez le nom du fichier a chiffrer : ")
    sortie = input("Entrez le nom du fichier a final : ")
    key = input("Entrez la clé de chiffrement : ")
    keys = sha256(key.encode('utf-8')).digest()
    with open(entree,'rb') as f_entree:
        with open(sortie, 'wb') as f_sortie:
            i = 0
            while f_entree.peek():
                c = ord(f_entree.read(1))
                j = i % len(keys)
                b = bytes([c^keys[j]])
                i = i+1
                f_sortie.write(b) 
                #os.system('cls')
                #print("task completed")
elif option == 2 :
    entree = input("Entrez le nom du fichier a dechiffrer : ")
    sortie = input("Entrez le nom du fichier a final : ")
    key = input("Entrez la clé de chiffrement : ")
    keys = sha256(key.encode('utf-8')).digest()
    with open(entree,'rb') as f_entree:
        with open(sortie, 'wb') as f_sortie:
            i = 0
            while f_entree.peek():
                c = ord(f_entree.read(1))
                j = i % len(keys)
                b = bytes([c^keys[j]])
                i = i+1
                f_sortie.write(b)
                #os.system('cls')
                #print("task completed")
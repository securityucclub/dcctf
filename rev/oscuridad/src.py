#!/usr/bin/python3
from random import randint
from time import sleep

print("Tú eras el elegido! Debías destruir a los Sith, no unirte a su fuerza!")
sleep(1)
print("Ibas a darle equilibrio a la fuerza, no dejarla en la oscuridad!")
sleep(1)
print("...")
sleep(2)
print("Te odio!")
sleep(1)
print("...")

sleep(3)
print("Nunca supiste mi secreto...")

def decrypt_flag(c):
    r = []
    for i in range(len(c)):
        r.append(chr((c[i] ^ 72) - (i ^ 14) + 40))

    return "".join(r)

c = [98, 98, 111, 113, 96, 22, 6, 89, 117, 10, 88, 70, 9, 71, 3, 112, 97, 45, 27, 41, 110, 26, 104, 44, 25, 44, 22, 86, 6, 87, 4, 46]
pw = "".join([chr(randint(0x20,0x73)) for x in range(32)])
inp = input()
if inp == pw:
    print(decrypt_flag(c))

print(decrypt_flag(c))

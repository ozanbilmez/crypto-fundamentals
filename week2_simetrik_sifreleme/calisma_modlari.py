import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

key = os.urandom(16)
blok = b"ATTACK AT DAWN!!"
mesaj = blok * 3

def sifrele(mod):
    c = Cipher(algorithms.AES(key), mod)
    e = c.encryptor()
    return e.update(mesaj) + e.finalize()

def bloklara_bol(veri):
    return [veri[i:i+16].hex() for i in range(0, len(veri), 16)]

print("ECB")
for b in bloklara_bol(sifrele(modes.ECB())):
    print(" ", b)

print("CBC")
for b in bloklara_bol(sifrele(modes.CBC(os.urandom(16)))):
    print(" ", b)

print("CTR")
for b in bloklara_bol(sifrele(modes.CTR(os.urandom(16)))):
    print(" ", b)



print("CTR: nonce tekrari")
nonce = os.urandom(16)
m1 = b"ATTACK AT DAWN!!"
m2 = b"RETREAT AT NOON!"
def ctr(m):
    e = Cipher(algorithms.AES(key), modes.CTR(nonce)).encryptor()
    return e.update(m) + e.finalize()
c1, c2 = ctr(m1), ctr(m2)
xor_c = bytes(a ^ b for a, b in zip(c1, c2))
xor_m = bytes(a ^ b for a, b in zip(m1, m2))
print(" c1 xor c2 == m1 xor m2 :", xor_c == xor_m)

print("GCM: oynama tespiti")
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
aes = AESGCM(key)
gn = os.urandom(12)
ct = aes.encrypt(gn, b"para: 100 TL", None)
bozuk = bytearray(ct)
bozuk[0] ^= 1
try:
    aes.decrypt(gn, bytes(bozuk), None)
    print(" kabul edildi")
except Exception as ex:
    print(" reddedildi:", type(ex).__name__)
"""
Hafta 1 - Matematiksel Temel
Paar Ders 11: Öklid Algoritması, Euler Phi, Euler Teoremi
"""


def gcd(a, b):
    """En büyük ortak bölen — Öklid algoritması."""
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    """gcd(a,b) ve Bézout katsayıları (x,y): a*x + b*y = gcd(a,b)."""
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def mod_inv(a, n):
    """a'nın mod n'deki çarpımsal tersi (gcd(a,n)=1 olmalı)."""
    g, x, _ = extended_gcd(a, n)
    if g != 1:
        raise ValueError(f"{a} ve {n} aralarında asal değil, tersi yok")
    return x % n

if __name__ == "__main__":
    print(gcd(48, 18))   # 6 olmalı
    print(gcd(17, 5))    # 1 olmalı (aralarında asal)

    g, x, y = extended_gcd(35, 15)
    print(g, x, y)               # g=5, ve 35*x + 15*y = 5 olmalı — kontrol et
    print(35*x + 15*y)           # 5 çıkmalı

    print(mod_inv(3, 11))        # 3'ün mod 11'deki tersi
    print((3 * mod_inv(3, 11)) % 11)   # 1 çıkmalı — tersin tanımı gereği
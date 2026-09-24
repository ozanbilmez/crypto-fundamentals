"""
Hafta 1 - Matematiksel Temel
Paar Ders 2: Modüler Aritmetik ve Tarihsel Şifreler
"""


def is_congruent(a, b, n):
    """a ≡ b (mod n) mi? (a-b), n'e tam bölünüyorsa evet."""
    return (a - b) % n == 0


def mod_add(a, b, n):
    """(a + b) mod n"""
    return (a + b) % n


def mod_mul(a, b, n):
    """(a * b) mod n"""
    return (a * b) % n

def fast_pow(base, exp, mod):
    """base^exp mod n, square-and-multiply ile."""
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result

if __name__ == "__main__":
    print(is_congruent(17, 5, 6))   # True  (17 mod 6 = 5)
    print(is_congruent(17, 4, 6))   # False
    print(mod_add(4, 5, 7))   # (4+5)=9, 9 mod 7 = 2
    print(mod_mul(4, 5, 7))   # (4*5)=20, 20 mod 7 = 6
    print(fast_pow(3, 13, 7))       # kendi hesapla, sonra pow(3,13,7) ile karşılaştır
    print(fast_pow(3, 13, 7) == pow(3, 13, 7))   # True olmalı
    print(fast_pow(2, 1000000, 1000000007))

"""
Hafta 1 - Matematiksel Temel
Paar Ders 11 (devamı): Gruplar, Z_n*, Euler Phi Fonksiyonu
"""

from euclidean import gcd


def euler_phi(n):
    """Euler'in phi fonksiyonu: 1..n arasında n'e aralarında asal
    olan sayı adedi — Z_n* grubunun büyüklüğü."""
    count = 0
    for k in range(1, n + 1):
        if gcd(k, n) == 1:
            count += 1
    return count


if __name__ == "__main__":
    print(euler_phi(9))    # 6 olmalı — Z_9* = {1,2,4,5,7,8}
    print(euler_phi(7))    # 6 olmalı — 7 asal, phi(p) = p-1
    print(euler_phi(12))   # 4 olmalı — Z_12* = {1,5,7,11}

    from modular_arithmetic import fast_pow

    n = 9
    phi_n = euler_phi(n)
    for a in [2, 4, 5, 7, 8]:
        print(f"{a}^{phi_n} mod {n} =", fast_pow(a, phi_n, n))
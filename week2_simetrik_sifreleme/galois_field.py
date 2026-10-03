"""
Hafta 2 - Simetrik Sifreleme
Paar Ders 7: Sonlu Cisimler, GF(2^8)
"""


def gf_mul(a, b):
    """GF(2^8) carpma, AES indirgeme polinomu x^8+x^4+x^3+x+1 (0x11B) ile."""
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        hi = a & 0x80
        a = (a << 1) & 0xFF
        if hi:
            a ^= 0x1B          # 0x11B'nin ust biti tasma ile zaten dusuyor
        b >>= 1
    return p & 0xFF


if __name__ == "__main__":
    print(hex(gf_mul(0x57, 0x83)))   # 0xc1 olmali (AES standardinin kendi ornegi)
    print(hex(gf_mul(0x01, 0x57)))
    print(hex(gf_mul(0x02, 0x87)))
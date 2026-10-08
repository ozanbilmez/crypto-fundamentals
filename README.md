# crypto-fundamentals

Kriptografinin matematiksel temeli ve simetrik şifreleme için Python uygulamaları. Her hafta bir konu klasörü olarak ilerliyor.

## İçindekiler

| Hafta | Konu | Dosyalar |
| --- | --- | --- |
| 1 | Matematiksel temel | `modular_arithmetic.py`, `euclidean.py`, `group_theory.py` |
| 2 | Simetrik şifreleme | `galois_field.py`, `calisma_modlari.py`, `week2_ozet.md` |

## Çalıştırma

```
uv venv
uv pip install cryptography
.venv\Scripts\python.exe week2_simetrik_sifreleme\calisma_modlari.py
```

Hafta 1 dosyaları yalnızca standart Python kullanır. `calisma_modlari.py` için `cryptography` paketi gerekir (Python 3.10+).

## Notlar

- Hafta 1: modüler aritmetik, hızlı üs alma, genişletilmiş Öklid, Euler phi.
- Hafta 2: GF(2^8) çarpımı (AES polinomu 0x11B), ECB/CBC/CTR/GCM karşılaştırması. ECB'de aynı bloklar aynı şifreli bloğu verir; CTR'de nonce tekrarı ve GCM'de bozulmuş şifreli metin deneylerle gösterildi.
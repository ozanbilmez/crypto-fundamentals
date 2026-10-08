# Hafta 2 Özeti: Simetrik şifreleme

## Feistel ve DES
Feistel yapısında blok sağ ve sol yarıya bölünür. Her turda `L' = R`, `R' = L XOR F(R, K)` olur. Şifre çözme aynı yapıdır, yalnızca tur anahtarları ters sırada verilir. DES: 64 bit blok, 56 bit anahtar, 16 tur, her tura 48 bitlik alt anahtar. 56 bitlik anahtar uzayı kaba kuvvetle taranabilecek kadar küçük.

## GF(2^8)
Bayt, derecesi 7'ye kadar olan polinom olarak görülür. Toplama XOR'dur. Çarpma `x^8 + x^4 + x^3 + x + 1` (0x11B) polinomuna göre indirgenir. Pratik kural: sola kaydır, taşma olursa 0x1B ile XOR'la. Örnek: `0x02 · 0xD4 = 0xB3`, `0x03 · 0xD4 = 0x67`.

## AES
128 bitlik blok 4x4 bayt durumdur. AES-128'de 10 tur var. Turda SubBytes (S-kutusu), ShiftRows, MixColumns, AddRoundKey uygulanır. Son turda MixColumns yoktur. AddRoundKey ilk adımda ve her turda olmak üzere 11 kez uygulanır, toplam 176 bayt tur anahtarı gerekir.

## Çalışma modları
- **ECB:** aynı düz metin bloğu aynı şifreli bloğa gider, desen sızar. Denemede üç aynı bloğun şifreli hali de aynı çıktı.
- **CBC:** her blok önceki şifreli blokla XOR'lanır, IV rastgele ve öngörülemez olmalı.
- **CTR:** blok şifreyi akış şifresine çevirir. Aynı nonce ikinci kez kullanılırsa iki şifreli metnin XOR'u iki düz metnin XOR'una eşit olur (denemede `True`).
- **GCM:** şifreleme ile birlikte etiket üretir. Şifreli metinde 1 bit değişince `InvalidTag` hatası aldık.

## Takıldığım yer
(buraya kendi cümlelerinle yaz)
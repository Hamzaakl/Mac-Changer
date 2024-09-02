# MAC Adresi Değiştirme Scripti

Python scripti, `eth0` ağ arayüzünün MAC adresini rastgele bir şekilde değiştirmenizi sağlar.

## Gereksinimler

- Python 3.x
- `ifconfig` komut satırı aracı (Unix benzeri işletim sistemlerinde mevcuttur)

## Çalışma 

1. **Rastgele MAC Adresi Oluşturma:** Script, 12 karakterlik bir MAC adresi oluşturur. Adres, 0-9 ve A-F karakterlerinden oluşur.

2. **Mevcut MAC Adresini Alma:** `ifconfig` komutunu kullanarak `eth0` arayüzünün mevcut MAC adresini alır.

3. **MAC Adresini Değiştirme:** 
   - `eth0` arayüzünü devre dışı bırakır.
   - Yeni MAC adresini atar.
   - `eth0` arayüzünü yeniden etkinleştirir.

4. **Sonuç:** Eski ve yeni MAC adreslerini ekrana yazdırır.



 **Scripti Çalıştırın:**

   ```bash
   python3 mac_changer.py
   ```

 **Örnek Çıktı:**

   ```plaintext
   Eski MAC:  00:1a:2b:3c:4d:5e
   Yeni MAC:  A1B2C3D4E5F6
   ```

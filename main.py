# Boş bir dictionary oluşturarak gelir ve giderleri saklayacağız
finanslar = {
    'gelirler': [],
    'giderler': []
}

def gelir_ekle():
    miktar = float(input("Gelir miktarını girin: "))
    aciklama = input("Gelir açıklamasını girin: ")
    finanslar['gelirler'].append({'miktar': miktar, 'aciklama': aciklama})
    print("Gelir başarıyla eklendi!")

def gider_ekle():
    miktar = float(input("Gider miktarını girin: "))
    aciklama = input("Gider açıklamasını girin: ")
    finanslar['giderler'].append({'miktar': miktar, 'aciklama': aciklama})
    print("Gider başarıyla eklendi!")

def bakiye_hesapla():
    gelir_toplam = sum(item['miktar'] for item in finanslar['gelirler'])
    gider_toplam = sum(item['miktar'] for item in finanslar['giderler'])
    bakiye = gelir_toplam - gider_toplam
    return bakiye

def rapor_olustur():
    print("\nGelirler:")
    for gelir in finanslar['gelirler']:
        print(f"{gelir['aciklama']}: {gelir['miktar']}")

    print("\nGiderler:")
    for gider in finanslar['giderler']:
        print(f"{gider['aciklama']}: {gider['miktar']}")

    print("\nToplam Gelir:", sum(item['miktar'] for item in finanslar['gelirler']))
    print("Toplam Gider:", sum(item['miktar'] for item in finanslar['giderler']))
    print("Bakiye:", bakiye_hesapla())

def ana_menu_goster():
    print("\n1. Gelir Ekle\n2. Gider Ekle\n3. Rapor Oluştur\n4. Çıkış")

while True:
    ana_menu_goster()
    secim = input("Yapmak istediğiniz işlemi seçin (1-4): ")

    if secim == '1':
        gelir_ekle()
    elif secim == '2':
        gider_ekle()
    elif secim == '3':
        rapor_olustur()
    elif secim == '4':
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim! Lütfen tekrar deneyin.")
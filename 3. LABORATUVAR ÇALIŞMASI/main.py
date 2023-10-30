ogrenciler = []


def numara_benzersiz_mi(numara):
    global ogrenciler
    for ogrenci in ogrenciler:
        if ogrenci["numara"] == numara:
            return False
    return True


def ogrenci_ekle():
    global ogrenciler

    numara = input("Öğrenci numarasını girin: ")
    try:
        numara = int(numara)
    except ValueError:
        print("Sayı Giriniz!!!")
        return

    if not numara_benzersiz_mi(numara):
        print("Bu numara zaten kullanılıyor. Lütfen benzersiz bir numara girin.")
        return

    ad = input("Öğrencinin adını girin: ")
    soyad = input("Öğrencinin soyadını girin: ")

    ogrenci = {"numara": numara, "ad": ad, "soyad": soyad, "notlar": {}}
    ogrenciler.append(ogrenci)
    print(f"{ad} {soyad} öğrencisi listeye eklendi.")


def not_ekle():
    global ogrenciler

    numara = input("Not eklemek istediğiniz öğrencinin numarasını girin: ")
    try:
        numara = int(numara)
    except ValueError:
        print("Sayı Giriniz!!!")
        return

    if numara_benzersiz_mi(numara):
        print("Bu numara kullanılmıyor.")
        return

    ders = input("Not eklemek istediğiniz dersi girin: ")
    ders_notu = input(f"{ders} dersi notunu girin: ")
    try:
        ders_notu = int(ders_notu)
    except ValueError:
        print("Sayı Giriniz!!!")
        return

    if not 0 <= ders_notu <= 100:
        print("Not 0 ile 100 arasında olmalı!!!")
        return

    for ogrenci in ogrenciler:
        if ogrenci["numara"] == numara:
            ogrenci["notlar"].update({f"{ders}": ders_notu})
            print(f'{ogrenci["ad"]} {ogrenci["soyad"]} öğrencisinin {ders} notu {ders_notu} '
                  f'olarak güncellendi.')


def ogrenci_listesi_goruntule():
    global ogrenciler
    if not ogrenciler:
        print("LİSTEDE ÖĞRENCİ YOK")
        return
    for ogrenci in ogrenciler:
        print(f"Numara:{ogrenci['numara']}, Adı:{ogrenci['ad']}, Soyadı:{ogrenci['soyad']}")
        for ders, notu in ogrenci["notlar"].items():
            print(f"{ders} Notu: {notu}")


def main():
    while True:
        print("\nYapabileceğiniz işlemler:")
        print("1. Yeni öğrenci ekle")
        print("2. Not eklemek")
        print("3. Öğrenci listesini görüntüle")
        print("4. Çıkış")
        secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4): ")
        if secim == "1":
            ogrenci_ekle()
        elif secim == "2":
            not_ekle()
        elif secim == "3":
            ogrenci_listesi_goruntule()
        elif secim == "4":
            break
        else:
            print("Geçersiz bir seçenek girdiniz. Lütfen tekrar deneyin.")

main()

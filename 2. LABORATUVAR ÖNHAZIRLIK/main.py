stok = []
sermaye = 1000
isim = "Migros"


def urun_ekle(urun, birim_alis_fiyati):
    global stok, sermaye
    if urun["urun_miktar"] * birim_alis_fiyati <= sermaye:
        stok.append(urun)
        sermaye -= urun["urun_miktar"] * birim_alis_fiyati
    elif urun["urun_miktar"] * birim_alis_fiyati > sermaye:
        print("SERMAYE YETERSİZ!!!")
    elif urun in stok:
        print("ÜRÜN ZATEN STOKTA VAR!!!")
    else: print("BEKLENMEDİK BİR HATA OLUŞTU!!!")


def urun_sat(urun_id, urun_miktar):
    global stok, sermaye
    satilacak_urun = None
    for urun in stok:
        if urun["urun_id"] == urun_id:
            satilacak_urun = urun

    if satilacak_urun is None:
        print("ÜRÜN STOKTA YOK")
        return

    if satilacak_urun["urun_miktar"] < urun_miktar:
        print("YETERLİ STOK YOK!!!")
        return
    else:
        if satilacak_urun["urun_miktar"] - urun_miktar == 0:
            stok.remove(satilacak_urun)
        sermaye += satilacak_urun["urun_fiyat"] * urun_miktar
        satilacak_urun["urun_miktar"] -= urun_miktar
        return


def urunleri_goster():
    global stok
    if not stok:
        print("STOKTA ÜRÜN YOK")
        return
    for urun in stok:
        print("************************")
        print(urun)
        print(f"Ürün ID:{urun['urun_id']}")
        print(f"Ürün Adı:{urun['urun_adi']}")
        print(f"Ürün Fiyatı:{urun['urun_fiyat']}")
        print(f"Ürün Miktarı:{urun['urun_miktar']}")
        print("************************")


def sermayeyi_gor():
    print(f"Sermaye: {sermaye}")


def sermayeyi_guncelle(yeni_sermaye:int):
    global sermaye
    sermaye = yeni_sermaye


def get_isim():
    print(f"Market ismi:{isim}")



# ayran = {
#     "urun_id": 1,  # ürünün benzersiz kimliği
#     "urun_adi": "Ayran",  # ürünün adı
#     "urun_fiyat": 5,  # ürünün satış fiyatı
#     "urun_miktar": 100  # ürünün stok miktarı
# }
#
# pc = {
#     "urun_id": 2,  # ürünün benzersiz kimliği
#     "urun_adi": "Bilgisayar",  # ürünün adı
#     "urun_fiyat": 30000,  # ürünün satış fiyatı
#     "urun_miktar": 15  # ürünün stok miktarı
# }
#
# telefon = {
#     "urun_id": 3,  # ürünün benzersiz kimliği
#     "urun_adi": "Telefon",  # ürünün adı
#     "urun_fiyat": 18000,  # ürünün satış fiyatı
#     "urun_miktar": 43  # ürünün stok miktarı
# }

#
# sermayeyi_guncelle(1000000)
# sermayeyi_gor()
# urun_ekle(telefon, 15000)
# urunleri_goster()
# sermayeyi_gor()
#
# urun_sat(3, 43)
# sermayeyi_gor()
# urunleri_goster()
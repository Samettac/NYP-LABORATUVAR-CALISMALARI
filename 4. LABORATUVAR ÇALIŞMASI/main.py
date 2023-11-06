from kitap import Kitap


def yazdir_güncel_mi(kitap:Kitap):
    print(f"Güncel mi?: {'Evet' if kitap.guncelMi() else 'Hayır'}")


def yazdır_kalin_mi(kitap:Kitap):
    print(f"Kalın mı?: {'Evet' if kitap.kalinMi() else 'Hayır'}")


if __name__ == "__main__":
    kitap1 = Kitap(ad="1984", yazar="George Orwell", yayın_yili="1949", sayfa_sayisi=328)
    kitap1.bilgileriYazdir()
    yazdir_güncel_mi(kitap1)
    yazdır_kalin_mi(kitap1)
    print()
    kitap2 = Kitap(ad="Dune", yazar="Frank Herbert", yayın_yili="1965", sayfa_sayisi=412)
    kitap2.bilgileriYazdir()
    yazdir_güncel_mi(kitap2)
    yazdır_kalin_mi(kitap2)
    print()
    kitap2.setAd(input("Kitabın yeni adını gıriniz: "))
    print(f"Kitabımızın yeni adı: {kitap2.getAd()}")
    print()
    kitap2.bilgileriYazdir()
    yazdir_güncel_mi(kitap2)
    yazdır_kalin_mi(kitap2)


from tekli_not import TekliNot
from coklu_not import CokluNot


def main():
    # TekliNot sınıfının kullanımı
    tekli_not = TekliNot()
    tekli_not.not_ekle("Alışveriş Listesi", "Elma, Muz, Süt")
    print("Tekli Not Başlık:", tekli_not.baslik)
    print("Tekli Not Metni:", tekli_not.not_metni)
    print("Oluşturulma Zamanı:", tekli_not.olusturma_zamani)
    print("Son Düzenleme Zamanı:", tekli_not.son_duzenleme_zamani)

    tekli_not.not_duzenle("Güncellenmiş Alışveriş Listesi", "Elma, Muz, Süt, Ekmek")
    print("\nTekli Not Güncellendi")
    print("Güncellenmiş Başlık:", tekli_not.baslik)
    print("Güncellenmiş Metin:", tekli_not.not_metni)
    print("Son Düzenleme Zamanı:", tekli_not.son_duzenleme_zamani)

    # ÇokluNot sınıfının kullanımı
    coklu_not = CokluNot()
    coklu_not.not_ekle("Toplantı Notları")
    coklu_not.not_ekle("Yemek Tarifi")
    print("\nÇoklu Not Listesi ve Zaman Damgaları:")
    for not_metni, zaman_damgasi in zip(coklu_not.notlar, coklu_not.zaman_damgalari):
        print(f"Not: {not_metni}, Zaman: {zaman_damgasi}")

    coklu_not.not_duzenle(1, "Güncellenmiş Yemek Tarifi")
    print("\nÇoklu Not Güncellendi")
    for not_metni, zaman_damgasi in zip(coklu_not.notlar, coklu_not.zaman_damgalari):
        print(f"Not: {not_metni}, Zaman: {zaman_damgasi}")

    coklu_not.not_sil(0)
    print("\nBir Not Silindi")
    for not_metni, zaman_damgasi in zip(coklu_not.notlar, coklu_not.zaman_damgalari):
        print(f"Not: {not_metni}, Zaman: {zaman_damgasi}")


if __name__ == "__main__":
    main()
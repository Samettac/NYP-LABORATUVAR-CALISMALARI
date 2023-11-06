

class Kitap():

    def __init__(self, ad, yazar, yayın_yili, sayfa_sayisi):
        self.ad = ad
        self.yazar = yazar
        self.yayin_yili = yayın_yili
        self.sayfa_sayisi = sayfa_sayisi


    def bilgileriYazdir(self):
        print(f"Ad: {self.ad}, Yazar: {self.yazar}, Yayım Yılı: {self.yayin_yili}, Sayfa Sayısı: {self.sayfa_sayisi}")


    def guncelMi(self):
        if self.yayin_yili == 2023:
            return True
        return False


    def kalinMi(self):
        if self.sayfa_sayisi >= 300:
            return True
        return False


    def setAd(self, yeni_deger):
        self.ad = yeni_deger

    def setYazar(self, yeni_deger):
        self.yazar = yeni_deger

    def setSayfaSayisi(self, yeni_deger):
        self.sayfa_sayisi = yeni_deger

    def getAd(self):
        return self.ad

    def getYazar(self):
        return self.ad
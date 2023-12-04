from arac import Arac

class Otomobil(Arac):
    def __init__(self, arac_markasi, model, uretim_yili, bakim_tarihi, yuz_kmde_yakit_tuketimi, depo, kapi_sayisi, bagaj_hacmi):
        super().__init__(arac_markasi, model, uretim_yili, bakim_tarihi, yuz_kmde_yakit_tuketimi, depo)
        self.kapi_sayisi = kapi_sayisi
        self.bagaj_hacmi = bagaj_hacmi

    def km_basina_maliyet_hesaplama(self, yakit_fiyati):
        return self.yuz_kmde_yakit_tuketimi*yakit_fiyati/100

    def hiz_sabitleyici_aktivasyonu(self, hiz):
        if hiz < 120:
            print(f"Hız sabitleyici {hiz} km/sa hızında aktive edildi")
            return True
        else:
            print(f"Hız sabitleyici 120 km/sa den daha hızlıbir hıza sabitlenemez.")
            return False

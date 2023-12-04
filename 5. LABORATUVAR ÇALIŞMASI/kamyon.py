from arac import Arac

class Kamyon(Arac):
    def __init__(self, arac_markasi, model, uretim_yili, bakim_tarihi, yuz_kmde_yakit_tuketimi, depo, yuk_kapasitesi, dingil_sayisi):
        super().__init__(arac_markasi, model, uretim_yili, bakim_tarihi, yuz_kmde_yakit_tuketimi, depo)
        self.yuk_kapasitesi = yuk_kapasitesi
        self.dingil_sayisi = dingil_sayisi

    def yuk_kapasitesi_kullanımi_hesaplama(self, yuk_agırlıgı):
        return yuk_agırlıgı / self.yuk_kapasitesi * 100

    def guclu_motor_modu_aktivasyonu(self):
        if True:
            return True
        return False
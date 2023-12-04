import datetime as dt

class Arac():
    def __init__(self, arac_markasi, model, uretim_yili, bakim_tarihi, yuz_kmde_yakit_tuketimi, depo):
        self.arac_markasi = arac_markasi
        self.model = model
        self.uretim_yili = uretim_yili
        self.bakim_tarihi = bakim_tarihi
        self.depo = depo
        self.yuz_kmde_yakit_tuketimi = yuz_kmde_yakit_tuketimi


    def yakit_tuketimi_hesapla(self, mesafe):
        return self.yuz_kmde_yakit_tuketimi*mesafe/100


    def bakım_zamanı_kontrolü(self):
        today_date = dt.datetime.now()
        if self.bakim_tarihi + dt.timedelta(days=180) <= today_date:
            return True
        return False
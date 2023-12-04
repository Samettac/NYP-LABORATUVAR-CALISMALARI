from otomobil import Otomobil
from kamyon import Kamyon
import datetime as dt

if __name__ == "__main__":
    araba = Otomobil("Toyota", "Corolla", 2020, dt.datetime(2021,9,15),
                     6, 50, 4, 400)
    print(araba.yakit_tuketimi_hesapla(36))
    print("Arabanın km başına maliyeti:", araba.km_basina_maliyet_hesaplama(10))
    print(araba.hiz_sabitleyici_aktivasyonu(60))
    print("Bakım zamanı gelmiş.") if araba.bakım_zamanı_kontrolü() else print("Bakım zamanı gelmemiş.")

    kamyon = Kamyon("Volvo", "FH16", 2019,  dt.datetime(2021,9,15),
                    15, 200, 20000, 6)
    print("Kamyonun yük kapasitesi kullanımı:", kamyon.yuk_kapasitesi_kullanımi_hesaplama(15000))
    print(kamyon.guclu_motor_modu_aktivasyonu())



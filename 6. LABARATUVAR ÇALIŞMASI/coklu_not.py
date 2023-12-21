from base_not import BaseNot
from typing import override
import datetime


class CokluNot(BaseNot):
    def __init__(self):
        super().__init__()
        self._notlar = []
        self._zaman_damgalari = []

    @property
    def notlar(self):
        return self._notlar

    @property
    def zaman_damgalari(self):
        return self._zaman_damgalari

    @override
    def not_ekle(self, yeni_not_metni):
        self.notlar.append(yeni_not_metni)
        self.zaman_damgalari.append(datetime.datetime.now())

    @override
    def not_duzenle(self, indeks, yeni_not_metni):
        self.notlar[indeks] = yeni_not_metni
        self.zaman_damgalari[indeks] = datetime.datetime.now()

    @override
    def not_sil(self, indeks):
        self.notlar.pop(indeks)
        self.zaman_damgalari.pop(indeks)


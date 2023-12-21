from base_not import BaseNot
from typing import override


class TekliNot(BaseNot):
    def __init__(self):
        super().__init__()
        self._baslik = None

    @property
    def baslik(self):
        return self._baslik

    @baslik.setter
    def baslik(self, yeni_deger):
        self._baslik = yeni_deger

    @override
    def not_ekle(self, baslik, not_metni):
        self.baslik = baslik
        self.not_metni = not_metni

    @override
    def not_duzenle(self, yeni_baslik, yeni_not_metni):
        self.baslik = yeni_baslik
        self.not_metni = yeni_not_metni

    @override
    def not_sil(self):
        self.baslik = None
        self.not_metni = None


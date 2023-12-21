import datetime


class BaseNot():
    def __init__(self):
        self._not_metni = None
        self._olusturma_zamani = datetime.datetime.now()
        self._son_duzenleme_zamani = datetime.datetime.now()

    @property
    def not_metni(self):
        return self._not_metni

    @not_metni.setter
    def not_metni(self, yeni_deger):
        self._not_metni = yeni_deger
        self._son_duzenleme_zamani = datetime.datetime.now()

    @property
    def olusturma_zamani(self):
        return self._olusturma_zamani

    @property
    def son_duzenleme_zamani(self):
        return self._son_duzenleme_zamani

    def not_ekle(self, baslik, not_metni):
        pass

    def not_duzenle(self):
        pass

    def not_sil(self):
        pass

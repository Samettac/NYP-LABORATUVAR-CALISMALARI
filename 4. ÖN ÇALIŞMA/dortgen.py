from ucgen import Ucgen
from math import sqrt


class Dortgen(Ucgen):
    def __init__(self, kose1, kose2, kose3, kose4):
        super().__init__(kose1, kose2, kose3)
        self.kose4 = kose4

    def cevre_hesapla(self):
        cevre = super().cevre_hesapla() + self.kose4
        return cevre
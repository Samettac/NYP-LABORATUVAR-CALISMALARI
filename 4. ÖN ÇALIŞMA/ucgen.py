from math import sqrt


class Ucgen():
    def __init__(self, kose1, kose2, kose3):
        self.kose1 = kose1
        self.kose2 = kose2
        self.kose3 = kose3

    def cevre_hesapla(self):
        cevre = self.kose1 + self.kose2 + self.kose3
        return cevre

    def alan_hesapla(self):
        s = self.cevre_hesapla() / 2
        alan = sqrt(s*(s-self.kose1)*(s-self.kose2)*(s-self.kose3))
        return alan
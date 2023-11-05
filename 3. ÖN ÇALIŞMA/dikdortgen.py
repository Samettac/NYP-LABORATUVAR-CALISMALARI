

class Dikdortgen():

    def __init__(self, uzunkenar, kısakenar):
        self.uzunkenar = uzunkenar
        self.kısakenar = kısakenar


    def dikdortgenCiz(self):
        kisaknr = self.kısakenar
        uzunknr = self.uzunkenar

        print("*" * kisaknr)
        for i in range(uzunknr-2):
            print("*", end="")
            print(" " * (kisaknr-2), end="")
            print("*")
        print("*" * kisaknr)


    def dikdortgenMi(self):
        if self.uzunkenar == self.kısakenar:
            return False
        return True


    def getUzunKenar(self):
        return self.uzunkenar


    def getKisaKenar(self):
        return self.kısakenar


    def setUzunKenar(self, yeni_deger):
        self.uzunkenar = yeni_deger


    def setKisaKenar(self, yeni_deger):
        self.kısakenar = yeni_deger
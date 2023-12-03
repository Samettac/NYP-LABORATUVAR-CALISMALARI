from ucgen import Ucgen
from dortgen import Dortgen

if __name__ == "__main__":
    ucgen = Ucgen(8,12,14.42222)
    print(ucgen.cevre_hesapla())
    print(ucgen.alan_hesapla())

    dikdortgen = Dortgen(2,2,4,4)
    print(dikdortgen.cevre_hesapla())
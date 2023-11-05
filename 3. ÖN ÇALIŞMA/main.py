from dikdortgen import Dikdortgen


if __name__ == "__main__":
    dik = Dikdortgen(10,5)
    dik.dikdortgenCiz()
    print("Dikdorgen mi?: "+ ("Evet" if dik.dikdortgenMi() else "Hayır"))
    dik2 = Dikdortgen(6,6)
    dik2.dikdortgenCiz()
    print("Dikdorgen mi?: "+ ("Evet" if dik2.dikdortgenMi() else "Hayır"))
    dik2.setKisaKenar(int(input("Dikdörtgenin kısa kenarını giriniz: ")))
    print(f"Dikdörtgenimizin yeni kısa kenar değeri: {dik2.getKisaKenar()}")
    dik2.dikdortgenCiz()
    print("Dikdorgen mi?: "+ ("Evet" if dik2.dikdortgenMi() else "Hayır"))
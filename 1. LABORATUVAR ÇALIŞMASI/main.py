import random

satir = int(input("Lütfen matrisin satırını giriniz: "))
sutun = int(input("Lütfen matrisin sütununu giriniz: "))


birinci_matris = [[0] * sutun for _ in range(satir)]
ikinci_matris = [[0] * sutun for _ in range(satir)]



def sayi_mevcudiyeti_kontrol(x, liste):
    for i in range(len(liste)):
        for j in range(len(liste[0])):
            if x == liste[i][j]:
                return True
    return False


def degerleri_al(satir, sutun):
    i = 0
    j = 0
    while i < satir:
        while j < sutun:
            deger = int(input(f"Lütfen matrisin {i}. satır {j}. sütununu giriniz: "))
            if sayi_mevcudiyeti_kontrol(deger, birinci_matris):
                print("************************************")
                print("UYARI: Aynı değer girilmiştir. Lütfen farklı bir değer giriniz.")
                print("************************************")
            else:
                birinci_matris[i][j] = deger
                j = j+1
        j = 0
        i = i + 1



def ikinci_matris_yerlestirme(satir, sutun):
    i = 0
    j = 0
    while i < satir:
        while j < sutun:
            deger = birinci_matris[random.randint(0, satir-1)][random.randint(0, sutun-1)]
            if sayi_mevcudiyeti_kontrol(deger, ikinci_matris):
                continue
            else:
                ikinci_matris[i][j] = deger
                j = j + 1
        j = 0
        i = i + 1


def degeri_bul(aranan_deger, liste:list):
    for i in range(len(liste)):
        try:
            degerin_sutunu = liste[i].index(aranan_deger)
        except ValueError: continue
        else: return (i, degerin_sutunu)


def en_uzak_eleman():
    max_uzaklık = 0
    uzaklık = 0
    birbirine_en_uzak_deger = None
    for i in range(satir):
        for j in range(sutun):
            deger = birinci_matris[i][j]
            ikincideki_konumu = degeri_bul(deger, ikinci_matris)
            # print(ikincideki_konumu)
            uzaklık = abs(i - ikincideki_konumu[0]) + abs(j - ikincideki_konumu[1])

            if max_uzaklık < uzaklık:
                max_uzaklık = uzaklık
                birbirine_en_uzak_deger = deger

    print(f"Birinci matris ile ikinci matris arasındaki birbirine en uzak eleman ve uzaklık miktarı:"
          f" {birbirine_en_uzak_deger}, {max_uzaklık}")


def matris_yazdır(matris, adi):
    print(f"{adi} matrisin çıktısı:")
    for i in range(len(matris)):
        for j in range(len(matris[0])):
            print(matris[i][j], end=" ")
        print()
    print()


degerleri_al(satir,sutun)
matris_yazdır(birinci_matris, "Birinci")

ikinci_matris_yerlestirme(satir,sutun)
matris_yazdır(ikinci_matris, "İkinci")

en_uzak_eleman()
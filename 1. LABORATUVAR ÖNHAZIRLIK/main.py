

def yazdir_k():
    harf_k = [[0] * 6 for _ in range(8)]
    for i in range(8):
        satir = list()
        if i < 4:
            satir.append(("*" * 2) + (" " * (4-(i+1))) + ("*" * 2) + (" " * i))
        else:
            satir.append(("*" * 2) + (" " * (i-4)) + ("*" * 2) + (" " * (7-i)))
        harf_k[i] = satir
    return harf_k


def yazdir_u():
    harf_u = [[0] * 6 for _ in range(8)]
    for i in range(8):
        satir = list()
        if i < 6:
            satir.append("*" * 2 + " " * 2 + "*" * 2)
        else:
            satir.append("*" * 6)
        harf_u[i] = satir
    return harf_u

def yazdir_s():
    harf_s = [[0] * 6 for _ in range(8)]
    for i in range(8):
        satir = list()
        if i == 2:
            satir.append(("*" * 2) + (" " * 4))
        elif i == 5:
            satir.append(" " * 4 + "*" * 2)
        else:
            satir.append("*" * 6)
        harf_s[i] = satir
    return harf_s


def kelime_gir():
    kelime = input("Lütfen kelime giriniz: ")
    return kelime


def sekilli_karakter_secimi(kelime:str, satir_sayisi:int):
    for i in range(satir_sayisi):
        for j in kelime.lower():
            if j == "k":
                print(yazdir_k()[i][0], end="")
            elif j == "u":
                print(yazdir_u()[i][0], end="")
            elif j == "s":
                print(yazdir_s()[i][0], end="")
            print("  ", end="")
        print()

def main():
    kelime = kelime_gir()
    satir_sayisi = 8
    sekilli_karakter_secimi(kelime, satir_sayisi)


if __name__ == "__main__":
    main()
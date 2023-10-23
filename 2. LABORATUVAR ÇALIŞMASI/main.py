def yazdir_b(i):
    satir = list()
    if i == 0:
        satir.append("****")
    elif 0 < i < 4:
        satir.append("**")
        if i == 3:
            satir.append(" " * i)
        else: satir.append(" " * i * 2)
        satir.append("**")
    elif 4 < i < 8:
        satir.append("**")
        if i == 7: satir.append("  ")
        else: satir.append(" " * (i - 2))
        satir.append("**")
    else:
        satir.append("*" * 5)
    return "".join(satir)


def yazdir_4(i):
    satir = list()
    if i < 6:
        satir.append(" " * (6-i))
        satir.append("**")
    elif i == 6:
        satir.append("**  **")
    elif i == 7:
        satir.append("*" * 8)
    elif i == 8:
        satir.append("    **")
    return "".join(satir)


def yazdir_3(i):
    satir = list()
    if i == 0 or i == 8:
        satir.append("*" * 5)
    elif i == 1 or i == 7:
        satir.append("   ****")
    elif 1 < i < 5:
        satir.append(" " * (6 - (i-2)*2))
        satir.append("***")
    elif 4 < i < 7:
        satir.append(" " * (4 + (i-5)*2))
        satir.append("***")
    return "".join(satir)


def kelime_gir():
    kelime = input("Lütfen kelime giriniz: ")
    return kelime


def sekilli_karakter_secimi(kelime:str, satir_sayisi:int):
    for x in range(len(kelime)):
        for i in range(satir_sayisi):
            if x == 0:
                for j in kelime.lower():
                    satir = list()
                    if j == "b":
                        satir = yazdir_b(i)
                    elif j == "4":
                        satir = yazdir_4(i)
                    elif j == "3":
                        satir = yazdir_3(i)
                    print(satir, end="")
                    print(" " * (9-len(satir)), end="  ")
                print()

            else:
                print(" " * ((9 * x) + (x * 2)), end="")
                satir = list()
                if kelime[x].lower() == "b":
                    satir = yazdir_b(i)
                elif kelime[x].lower() == "4":
                    satir = yazdir_4(i)
                elif kelime[x].lower() == "3":
                    satir = yazdir_3(i)
                print(satir, end="")
                print(" " * (9-len(satir)), end="  ")
                print(" " * ((9 * (len(kelime)-x-1)) + (x * 2)), end="")
                print()

        print()


def main():
    # for i in range(9):
    #     yazdir_3(i)

    kelime = kelime_gir()
    satir_sayisi = 9
    sekilli_karakter_secimi(kelime, satir_sayisi)


if __name__ == "__main__":
    main()
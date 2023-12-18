

while True:
    sayi = input("sayı: ")
    if sayi.isdigit() and int(sayi) > 0:
        sayi = int(sayi)
        break


collatz = [sayi]
while sayi !=1:
    if sayi % 2 != 0:
        sayi = int(sayi * 3 + 1)
    else:
        sayi = int(sayi / 2)
    collatz.append(sayi)

print(collatz)

en_buyuk = None
for sayi in collatz:
    if en_buyuk is None or sayi > en_buyuk:
        en_buyuk = sayi
print(en_buyuk)
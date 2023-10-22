# M x N ‘lik bir matris ile N x P ‘lik bir matris çarpımını hesaplayan programı kodlayınız.

boyut_1, boyut_2, boyut_3 = (4,3,2)
orijinal_matris = [[0] * boyut_1 for _ in range(boyut_1)]
filtre_matrisi = [[0] * boyut_2 for _ in range(boyut_2)]
sonuc_matrisi = [[0] * boyut_3 for _ in range(boyut_3)]
# orijinal_matris[i][j]

filtre_matrisi = [[1,2,1], [2,4,2], [1,2,1]]
filtre_matrisi_toplamı = 0
for row in range(len(filtre_matrisi)):
    filtre_matrisi_toplamı = filtre_matrisi_toplamı + sum(filtre_matrisi[row])
# print(filtre_matrisi_toplamı)
# print(orijinal_matris)
# print(filtre_matrisi)
# print(sonuc_matrisi)

# for x in range(len(orijinal_matris)):
#     for y in range(len(orijinal_matris)):
#         orijinal_matris[x][y] = int(input(f"Lütfen {x}. satır {y}. sütunun değerini giriniz: "))

orijinal_matris = [[7,8,2,6], [2,5,9,5], [2,3,9,5], [8,2,4,6]]

islem_matrisi = orijinal_matris


for i in range(len(sonuc_matrisi)):
    for j in range(len(sonuc_matrisi)):
        carpım = 0
        toplam = 0
        for k in range(len(filtre_matrisi)):
            for m in range(len(filtre_matrisi)):
                carpım = islem_matrisi[k + i][m + j] * filtre_matrisi[k][m]
                print(carpım)
                toplam = toplam + carpım
        islem_matrisi = orijinal_matris
        sonuc_matrisi[i][j] = round(toplam/filtre_matrisi_toplamı)

print(sonuc_matrisi)
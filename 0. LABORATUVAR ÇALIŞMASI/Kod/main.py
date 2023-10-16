# M x N ‘lik bir matris ile N x P ‘lik bir matris çarpımını hesaplayan programı kodlayınız.

a_row = int(input("Lütfen 1. dizinin satırını giriniz: "))
a_col = int(input("Lütfen 1. dizinin sütununu giriniz: "))

b_row = a_col
print(f"Matris çarpımının olması için 2. dizinin satırı {b_row} olarak belirlenmiştir.")
b_col = int(input("Lütfen 2. dizinin sütununu giriniz: "))

matrix_a = [[0]*a_col for _ in range(a_row)]
matrix_b = [[0]*b_col for _ in range(b_row)]
result_matrix = [[0] * b_col for _ in range(a_row)]
# print(matrix_a)
# print(matrix_b)
# print(result_matrix)

def take_numbers(row, col, matrix, name_of_matrix):
    for x in range(row):
        for y in range(col):
            matrix[x][y] = int(input(f"Lütfen {name_of_matrix}.dizinin {x}. satır {y}. sütununu giriniz: "))


take_numbers(row=a_row, col=a_col, matrix=matrix_a, name_of_matrix="1")
take_numbers(row=b_row, col=b_col, matrix=matrix_b, name_of_matrix="2")


print(matrix_a)
print(matrix_b)

for i in range(a_row):
    for j in range(b_col):
        sum = 0
        for k in range(a_col):
            sum += matrix_a[i][k] * matrix_b[k][j]
        result_matrix[i][j] = sum

print(result_matrix)
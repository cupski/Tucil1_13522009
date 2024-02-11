print("Welcome to Cyberpunk 2077 Breach Protocol")
#INPUT USER
jmlh_token = int(input("Masukkan jumlah token Unik: "))
token = input("Masukkan Token: ")
tokens = token.split()
while (len(tokens) != jmlh_token):
    print("Jumlah token unik harus sesuai")
    token = input("Masukkan Token: ")
    tokens = token.split()

buffer_size = int(input("Masukkan ukuran buffer: "))
matrix_size = input("Masukkan ukuran matriks (jumlah baris dan kolom dipisahkan oleh spasi): ")
jumlah_baris, jumlah_kolom = map(int, matrix_size.split())
sekuens_size = int(input("Masukkan jumlah sekuens: "))
max_sekuens = int(input("Masukkan ukuran maksimal sekuens: "))

#AUTOMATION MATRIX AND SEQUENS GENERAZATION


#SAMPLE
m = [
    ['7A', '55', 'E9', 'E9', '1C', '55'],
    ['55', '7A', '1C', '7A', 'E9', '55'],
    ['55', '1C', '1C', '55', 'E9', 'BD'],
    ['BD', '1C', '7A', '1C', '55', 'BD'],
    ['BD', '55', 'BD', '7A', '1C', '1C'],
    ['1C', '55', '55', '7A', '55', '7A']
]
sekuens_1 = ["BD", "E9", "1C"]
sekuens_2 = ["BD", "7A", "BD"]
sekuens_3 = ["BD", "1C", "BD", "55"]
all_sekuens = [sekuens_1, sekuens_2, sekuens_3]

#BRUTE FORCE SEARCHING
# for i in range(6):
#     if(m[i][0] == sekuens_2[0])
import random

def list_menu():
    print("Welcome to Cyberpunk 2077 Breach Protocol")
    print("----------Pilih Metode Input----------")
    print("1.Manual")
    print("2.file")

    menu = int(input("Pilihan Menu : "))
        
    while (menu < 1 or menu > 2):
        print("\nMasukan Tidak Valid")
        menu = int(input("Pilihan Menu : "))

    return menu

def generate_matrix(tokens, num_row, num_column):
    input_token = tokens*num_row
    # Mengacak urutan elemen
    random_elements = random.sample(input_token, num_row*num_column)
    
    # Membuat matrix n x n dengan elemen yang sudah diacak
    matrix = [random_elements[i*num_row:(i+1)*num_row] for i in range(num_row)]
    
    return matrix


def manual():
    jmlh_token = int(input("Masukkan jumlah token Unik: "))

    token = input("Masukkan Token: ")
    tokens = token.split()
    while (len(tokens) != jmlh_token):
        print("Masukan jumlah token unik harus sesuai")
        token = input("Masukkan Token: ")
        tokens = token.split()

    buffer_size = int(input("Masukkan ukuran buffer: "))
    matrix_size = input("Masukkan ukuran matriks (jumlah baris dan kolom dipisahkan oleh spasi): ")
    num_row, num_column = map(int, matrix_size.split())
    sekuens_size = int(input("Masukkan jumlah sekuens: "))
    max_sekuens = int(input("Masukkan ukuran maksimal sekuens: "))
    
    random_matrix = generate_matrix(tokens, num_row, num_column)

    return random_matrix


def run():
    user = list_menu()
    if user == 1:
        matrix = manual()
        for row in matrix:
            print(row)




run()


#AUTOMATION MATRIX AND SEQUENS GENERAZATION




#BRUTE FORCE SEARCHING
# for i in range(6):
#     if(m[i][0] == sekuens_2[0])
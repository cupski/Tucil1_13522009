import random

def generate_random_matrix(elements, n):
    # Mengacak urutan elemen
    random_elements = random.sample(elements, n*n)
    
    # Membuat matrix n x n dengan elemen yang sudah diacak
    matrix = [random_elements[i*n:(i+1)*n] for i in range(n)]
    
    return matrix

# Elemen yang akan diinput ke dalam matrix
input_elements = ['BD', '1C', '7A', '55', 'E9'] * 5  # Menambahkan elemen lebih banyak

# Ukuran matrix (n x n)
n = 5
input_elements = ['BD', '1C', '7A', '55', 'E9'] * n  # Menambahkan elemen lebih banyak

# Membuat matrix secara acak
random_matrix = generate_random_matrix(input_elements, n)

# Cetak matrix
for row in random_matrix:
    print(row)

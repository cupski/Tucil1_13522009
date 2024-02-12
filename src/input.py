import random
from bruteforce import BruteForceSolver

class InputHandler:

    def __init__(self):
        self.brute = BruteForceSolver([], 0, [], [])

    def list_menu(self):
        print("Welcome to Cyberpunk 2077 Breach Protocol")
        print("----------Pilih Metode Input----------")
        print("1.Manual")
        print("2.File")

        menu = int(input("Pilihan Menu : "))
            
        while (menu < 1 or menu > 2):
            print("\nMasukan Tidak Valid")
            menu = int(input("Pilihan Menu : "))

        return menu

    def generate_matrix(self, tokens, num_row, num_column):
        input_token = tokens*num_row
        # Mengacak urutan elemen
        random_elements = random.sample(input_token, num_row*num_column)
        matrix = [random_elements[i*num_row:(i+1)*num_row] for i in range(num_row)]
        
        return matrix

    def generate_sequences(self, tokens, sequence_size, max_length):
        sequences = []
        num_tokens = len(tokens)

        for length in range(2, max_length + 1):
            for i in range(num_tokens):
                for j in range(num_tokens - length + 1):
                    sequences.append(tokens[j:j+length])
        random.shuffle(sequences)
        
        sequences = sequences[:sequence_size]
        return sequences

    def generate_reward(self, sequence_size):
        matrix = []
        matrix.append(random.randint(-100, 0))
        for _ in range(sequence_size - 1):
            matrix.append(random.randint(matrix[-1], 100))
        
        return matrix

    def manual(self):
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
        sequence_size = int(input("Masukkan jumlah sekuens: "))
        max_sequence = int(input("Masukkan ukuran maksimal sekuens: "))
        
        random_matrix = self.generate_matrix(tokens, num_row, num_column)
        random_sequences = self.generate_sequences(tokens, sequence_size, max_sequence)
        random_reward = self.generate_reward(sequence_size)

        return random_matrix, random_sequences, random_reward, buffer_size

    def run(self):
        user = self.list_menu()
        if user == 1:
            matrix, sequences, reward, buffer = self.manual()
            print("Generated Matrix :")
            for row in matrix:
                print(row)
            
            print("Generated Sequence:")
            for i in range(len(sequences)):
                print(reward[i])
                print(sequences[i])

            self.brute.get_solution(matrix, buffer, sequences, reward)

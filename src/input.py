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

    def generate_matrix(self, tokens, num_column, num_row):
        input_token = tokens * (num_row*num_column)
        random_elements = random.sample(input_token, num_row * num_column)

        matrix = [random_elements[i * num_column : (i + 1) * num_column] for i in range(num_row)]
    
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
        while (len(tokens) != jmlh_token or (not all(len(token) == 2 for token in tokens)) or (not all(token.isalnum() for token in tokens)) or (len(set(tokens)) != len(tokens))):
            print("Masukan Token Tidak Valid")
            token = input("Masukkan Token: ")
            tokens = token.split()

        buffer_size = int(input("Masukkan ukuran buffer: "))
        matrix_size = input("Masukkan ukuran matriks (jumlah baris dan kolom dipisahkan oleh spasi): ")
        num_column, num_row = map(int, matrix_size.split())
        sequence_size = int(input("Masukkan jumlah sekuens: "))
        max_sequence = int(input("Masukkan ukuran maksimal sekuens: "))
        
        random_matrix = self.generate_matrix(tokens, num_column, num_row)
        random_sequences = self.generate_sequences(tokens, sequence_size, max_sequence)
        random_reward = self.generate_reward(sequence_size)

        return random_matrix, random_sequences, random_reward, buffer_size

    def input_file(self, filename):
        filepath = "input/" + filename + ".txt"
        with open(filepath, 'r') as file:
            buffer_size = int(file.readline().strip())
            num_column, num_row = map(int, file.readline().strip().split())
            matrix = []
            for _ in range(num_column):
                row = file.readline().strip().split()
                matrix.append(row)

            total_sequences = int(file.readline().strip())
            sequences = []
            rewards = []
            for _ in range(total_sequences):
                sequence = file.readline().strip().split()
                reward = int(file.readline().strip())
                sequences.append(sequence)
                rewards.append(reward)

        return buffer_size, matrix, sequences, rewards

    def save_to_file(self, matrix, buffer_size, sequences, rewards, best_path, max_reward, best_index, coords, execution):
        simpan = input("Apakah ingin menyimpan solusi? (y/n)")
        if((simpan == "Y") or (simpan == "y")):
            filename = input("Masukkan Nama File (berekstensi .txt): ")
            filepath = "output/" + filename + ".txt"
            with open(filepath , 'w') as file:
                file.write("Buffer Size: {}\n".format(buffer_size))
                file.write("Matrix:\n")
                for row in matrix:
                    file.write(" ".join(row) + "\n")
                
                file.write("Sequences:\n")
                for i, sequence in enumerate(sequences):
                    file.write("Sequence {}: {}\n".format(i + 1, " ".join(sequence)))
                    file.write("Reward: {}\n".format(rewards[i]))

                file.write("\nSolusi Teroptimal:\n")
                file.write("{}\n".format(max_reward))
                file.write("{}\n".format(" ".join(best_path)))
                for coord in coords[best_index]:
                    file.write("{} {}\n".format(coord[0], coord[1]))
                
                file.write("{} ms\n".format(execution))
        self.continue_menu()

    def continue_menu(self):
        print("\n----------Program----------")
        print("1.Kembali ke Menu")
        print("2.Keluar")

        menu = int(input("Pilihan : "))
        while (menu < 1 or menu > 2):
            print("\nMasukan Tidak Valid\n")
            menu = int(input("Pilihan : "))
        if (menu == 1):
            self.run()


    def run(self):
        user = self.list_menu()
        if user == 1:
            matrix, sequences, rewards, buffer_size = self.manual()
            print("Generated Matrix :")
            for row in matrix:
                print(" ".join(row))
            
            print("\nGenerated Sequences:")
            for i, sequence in enumerate(sequences):
                print("Sequence", i + 1, ":", " ".join(sequence))
                print("Reward:", rewards[i])

            best_path, max_reward, best_index, coords, execution =  self.brute.get_solution(matrix, buffer_size, sequences, rewards)
            self.save_to_file(matrix, buffer_size, sequences, rewards, best_path, max_reward, best_index, coords, execution)
        else:
            file = input("Masukkan Nama File (berekstensi .txt): ")
            buffer_size, matrix, sequences, rewards = self.input_file(file)
            print("Buffer Size:", buffer_size)
            print("Matrix:")
            for row in matrix:
                print(" ".join(row))
            print("\nSequences:")
            for i, sequence in enumerate(sequences):
                print("Sequence", i + 1, ":", " ".join(sequence))
                print("Reward:", rewards[i])

            best_path, max_reward, best_index, coords, execution =  self.brute.get_solution(matrix, buffer_size, sequences, rewards)
            self.save_to_file(matrix, buffer_size, sequences, rewards, best_path, max_reward, best_index, coords, execution)
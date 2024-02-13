import random
import time

class BruteForceSolver:
    def __init__(self, matrix, buffer_size, sequences, rewards):
        self.matrix = matrix
        self.buffer_size = buffer_size
        self.sequences = sequences
        self.rewards = rewards

    def get_routes(self, matrix, buffer_size):
            routes = []
            route = []
            coords = []
            coord = []
            num_rows = len(matrix)
            num_columns = len(matrix[0])
            curr_seq = -1

            # Loop melalui setiap kolom untuk memulai rute
            for col in range(num_columns):
                route.clear()
                coord.clear()
                # Memilih satu token pada posisi baris paling atas
                route.append(matrix[0][col])
                coord.append([0, col])
                # Inisialisasi rute baru
                first = True
                vertical = True  # True untuk gerakan horizontal, False untuk gerakan vertikal
                # Loop untuk membangun rute dengan pola horizontal, vertikal, horizontal, vertikal
                while len(route) < buffer_size + 1:
                    if not first:
                        route.clear()
                        coord.clear()
                    if vertical:
                        #elemen pertama
                        if first:
                            for curr_row in range(num_rows):
                                if curr_row != 0:
                                    route.append(matrix[curr_row][col])
                                    coord.append([curr_row,col])
                                    # Jika sudah mencapai panjang buffer atau panjang minimal rute
                                    if 2 <= len(route) <= buffer_size:
                                        routes.append(route[:])  
                                        coords.append(coord[:])
                                        route.pop()
                                        coord.pop()
                                    else:
                                        curr_seq = len(routes) - 2
                                        break
                            first = False
                            vertical = False
                        else:
                            route = routes[curr_seq].copy()
                            coord = coords[curr_seq].copy()
                            for curr_row in range(num_rows):
                                if ([curr_row, coord[-1][1]] not in coord):
                                    route.append(matrix[curr_row][coord[-1][1]])
                                    coord.append([curr_row,coord[-1][1]])
                                    if 2 <= len(route) <= buffer_size:
                                        routes.append(route[:])  
                                        coords.append(coord[:])
                                        route.pop()
                                        coord.pop()
                                    else:
                                        curr_seq = len(routes) - 2
                                        break
                            if (len(routes[curr_seq]) <= buffer_size):
                                if (len(routes[curr_seq]) < len(routes[curr_seq+1])):
                                    vertical = False

                    else:
                        route = routes[curr_seq].copy()
                        coord = coords[curr_seq].copy()
                        for curr_col in range(num_columns):
                            if ([coord[-1][0], curr_col] not in coord):
                                route.append(matrix[coord[-1][0]][curr_col])
                                coord.append([coord[-1][0], curr_col])
                                # Jika sudah mencapai panjang buffer atau panjang minimal rute
                                if 2 <= len(route) <= buffer_size:
                                    routes.append(route[:])  
                                    coords.append(coord[:])
                                    route.pop()
                                    coord.pop()
                                else:
                                    curr_seq = len(routes) - 2
                                    break
                        if (len(routes[curr_seq]) <= buffer_size):
                            if (len(routes[curr_seq]) < len(routes[curr_seq+1])):
                                vertical = True
                    curr_seq += 1
            return routes, coords
    
    def reward(self, path, sequences, rewards):
        total_reward = 0
        for idx, sequence in enumerate(sequences):
            sequence_length = len(sequence)
            for i in range(len(path) - sequence_length + 1):
                if path[i:i+sequence_length] == sequence:
                    total_reward += rewards[idx]
                    break  
        return total_reward


    def best_path(self, possible_paths, sequences, rewards):
        max_reward = 0
        best_path = []
        best_idx = None
        for idx, path in enumerate(possible_paths):
            reward = self.reward(path, sequences, rewards)
            if reward > max_reward:
                max_reward = reward
                best_path = path
                best_idx = idx
        return best_path, max_reward, best_idx


    def get_solution(self, matrix, buffer_size, sequences, rewards):
        start = time.time()
        routes, coords = self.get_routes(matrix, buffer_size)
        best_path, max_reward, best_index = self.best_path(routes, sequences, rewards)
        end = time.time()
        execution = round((end - start) * 1000, 3)
        print("\nSolusi Teroptimal:")
        print(max_reward)
        if(max_reward > 0):
            print(" ".join(best_path))
            for coord in coords[best_index]:
                final_coord = [coord[1] + 1, coord[0] + 1]
                print(" ".join(map(str, final_coord)))
            print("\n\n" + str(execution) + " ms") 
        else:
            print("Breach ini tidak memeiliki solusi")
            print("\n\n" + str(execution) + " ms")

        return best_path, max_reward, best_index, coords, execution

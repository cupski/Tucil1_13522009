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
        best_routes = []
        best_coords = []
        num_rows = len(matrix)
        num_columns = len(matrix[0])
        curr_seq = -1

        # Loop melalui setiap kolom untuk memulai rute
        for row in range(num_rows):
            route.clear()
            coord.clear()
            # Memilih satu token pada posisi baris paling atas
            route.append(matrix[0][row])
            coord.append([0, row])
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
                        for curr_col in range(num_columns):
                            if curr_col != 0:
                                route.append(matrix[curr_col][row])
                                coord.append([curr_col,row])
                                # Jika sudah mencapai panjang buffer atau panjang minimal rute
                                if len(route) < buffer_size:
                                    routes.append(route[:])  
                                    coords.append(coord[:])
                                    route.pop()
                                    coord.pop()
                                elif len(route) == buffer_size:
                                    best_routes.append(route[:])
                                    best_coords.append(coord[:])
                                    routes.append(route[:])  
                                    coords.append(coord[:])
                                    route.pop()
                                    coord.pop()
                                else:
                                    curr_seq = len(routes) - 1
                                    break
                        first = False
                        vertical = False
                    else:
                        route = routes[curr_seq].copy()
                        coord = coords[curr_seq].copy()
                        for curr_col in range(num_columns):
                            if ([curr_col, coord[-1][1]] not in coord):
                                route.append(matrix[curr_col][coord[-1][1]])
                                coord.append([curr_col,coord[-1][1]])
                                if len(route) < buffer_size:
                                    routes.append(route[:])  
                                    coords.append(coord[:])
                                    route.pop()
                                    coord.pop()
                                elif len(route) == buffer_size:
                                    best_routes.append(route[:])
                                    best_coords.append(coord[:])
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
                    for curr_row in range(num_rows):
                        if ([coord[-1][0], curr_row] not in coord):
                            route.append(matrix[coord[-1][0]][curr_row])
                            coord.append([coord[-1][0], curr_row])
                            # Jika sudah mencapai panjang buffer atau panjang minimal rute
                            if len(route) < buffer_size:
                                    routes.append(route[:])  
                                    coords.append(coord[:])
                                    route.pop()
                                    coord.pop()
                            elif len(route) == buffer_size:
                                best_routes.append(route[:])
                                best_coords.append(coord[:])
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
        return best_routes, best_coords
    
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
        print(" ".join(best_path))
        for coord in coords[best_index]:
            print(" ".join(map(str, coord)))
        print("\n\n" + str(execution) + " ms") 

        return best_path, max_reward, best_index, coords, execution

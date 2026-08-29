import numpy as np
import random

def check_row_column(matrix, value):
    rows = matrix.shape[0]
    for row in range(rows):
        if np.all(matrix[row, :] == value):
            return True
    cols = matrix.shape[1]
    for col in range(cols):
        if np.all(matrix[:, col] == value):
            return True

    # from top-left to bottom-right
    if (matrix.diagonal() == value).all():
        return True
    # from top-right to bottom-left
    if (np.fliplr(matrix).diagonal() == value).all():
        return True
    return False

def is_it_full(matrix):
    unique_values = np.unique(matrix)
    return len(unique_values) == 2 and 'X' in unique_values and 'O' in unique_values

def play_game():
    numbers = np.arange(1, 10)
    string_matrix = numbers.reshape(3, 3).astype(str)

    print(string_matrix)

    counter = 0
    game_mode = input("Choose game mode: [1] Player vs Player, [2] Player vs AI: ")

    if game_mode == '1':
        while np.any(string_matrix != 'X') and np.any(string_matrix != 'O'):
            number = input("Enter a number between 1 and 9: ")

            try:
                number = int(number)
                if 1 <= number <= 9:
                    search_value = str(number)
                    indices = np.where(string_matrix == search_value)
                    row_indices, col_indices = indices
                    if len(row_indices) > 0:
                        for row, col in zip(row_indices, col_indices):
                            if counter % 2 == 0:
                                string_matrix[row, col] = 'X'
                            else:
                                string_matrix[row, col] = 'O'
                        counter += 1
                        print(string_matrix)

                        if check_row_column(string_matrix, 'X'):
                            print("X wins!!")
                            break

                        if check_row_column(string_matrix, 'O'):
                            print("O wins!!")
                            break
                        if is_it_full(string_matrix):
                            print("No one wins :(")
                            break
                    else:
                        print("Number not found in the matrix. Try again.")
                else:
                    print("Number must be between 1 and 9. Try again.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
    elif game_mode == '2':
        while np.any(string_matrix != 'X') and np.any(string_matrix != 'O'):
            if counter % 2 == 0:
                number = input("Enter a number between 1 and 9: ")

                try:
                    number = int(number)
                    if 1 <= number <= 9:
                        search_value = str(number)
                        indices = np.where(string_matrix == search_value)
                        row_indices, col_indices = indices
                        if len(row_indices) > 0:
                            for row, col in zip(row_indices, col_indices):
                                string_matrix[row, col] = 'X'
                            counter += 1
                            print(string_matrix)

                            if check_row_column(string_matrix, 'X'):
                                print("X wins!!")
                                break

                            if is_it_full(string_matrix):
                                print("No one wins :(")
                                break
                        else:
                            print("Number not found in the matrix. Try again.")
                    else:
                        print("Number must be between 1 and 9. Try again.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")
            else:
                # AI's turn
                available_positions = np.where((string_matrix != 'X') & (string_matrix != 'O'))
                
                ai_position = random.choice(available_positions[0]), random.choice(available_positions[1])
                string_matrix[ai_position] = 'O'
                counter += 1
                print(string_matrix)

                if check_row_column(string_matrix, 'O'):
                    print("O wins!!")
                    break

                if is_it_full(string_matrix):
                    print("No one wins :(")
                    break
    else:
        print("Invalid game mode. Try again.")

play_game()
import random


def init_matrix(rows=11, cols=11):
    return [[random.randint(1, 4) for _ in range(cols)] for _ in range(rows)]


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print()


def detect_line_of_3_from_position(matrix, start_row, start_col):
    rows = len(matrix)
    cols = len(matrix[0])
    marked_for_removal = [[False for _ in range(cols)] for _ in range(rows)]
    points = 0
    detected = False

    # Verificare linie orizontala de 3
    if start_col <= cols - 3:
        if matrix[start_row][start_col] != 0 and matrix[start_row][start_col] == matrix[start_row][start_col + 1] == \
                matrix[start_row][start_col + 2]:
            marked_for_removal[start_row][start_col] = True
            marked_for_removal[start_row][start_col + 1] = True
            marked_for_removal[start_row][start_col + 2] = True
            points += 5
            detected = True

    # Verificare linie verticala de 3
    if start_row <= rows - 3:
        if matrix[start_row][start_col] != 0 and matrix[start_row][start_col] == matrix[start_row + 1][start_col] == \
                matrix[start_row + 2][start_col]:
            marked_for_removal[start_row][start_col] = True
            marked_for_removal[start_row + 1][start_col] = True
            marked_for_removal[start_row + 2][start_col] = True
            points += 5
            detected = True

    return marked_for_removal, points, detected


def detect_line_of_4_from_position(matrix, start_row, start_col):
    rows = len(matrix)
    cols = len(matrix[0])
    marked_for_removal = [[False for _ in range(cols)] for _ in range(rows)]
    points = 0
    detected = False

    # Verificare linie orizontala de 4
    if start_col <= cols - 4:
        if matrix[start_row][start_col] != 0 and matrix[start_row][start_col] == matrix[start_row][start_col + 1] == \
                matrix[start_row][start_col + 2] == matrix[start_row][start_col + 3]:
            marked_for_removal[start_row][start_col] = True
            marked_for_removal[start_row][start_col + 1] = True
            marked_for_removal[start_row][start_col + 2] = True
            marked_for_removal[start_row][start_col + 3] = True
            points += 10
            detected = True

    # Verificare linie verticala de 4
    if start_row <= rows - 4:
        if matrix[start_row][start_col] != 0 and matrix[start_row][start_col] == matrix[start_row + 1][start_col] == \
                matrix[start_row + 2][start_col] == matrix[start_row + 3][start_col]:
            marked_for_removal[start_row][start_col] = True
            marked_for_removal[start_row + 1][start_col] = True
            marked_for_removal[start_row + 2][start_col] = True
            marked_for_removal[start_row + 3][start_col] = True
            points += 10
            detected = True

    return marked_for_removal, points, detected


def detect_line_of_5_from_position(matrix, start_row, start_col):
    rows = len(matrix)
    cols = len(matrix[0])
    marked_for_removal = [[False for _ in range(cols)] for _ in range(rows)]
    points = 0
    detected = False

    # Verificare linie orizontala de 5
    if start_col <= cols - 5:
        if matrix[start_row][start_col] != 0 and matrix[start_row][start_col] == matrix[start_row][start_col + 1] == matrix[start_row][start_col + 2] == matrix[start_row][start_col + 3] == matrix[start_row][start_col + 4]:
            for k in range(5):
                marked_for_removal[start_row][start_col + k] = True
            points += 50
            detected = True

    # Verificare linie verticala de 5
    if start_row <= rows - 5:
        if matrix[start_row][start_col] != 0 and matrix[start_row][start_col] == matrix[start_row + 1][start_col] == matrix[start_row + 2][start_col] == matrix[start_row + 3][start_col] == matrix[start_row + 4][start_col]:
            for k in range(5):
                marked_for_removal[start_row + k][start_col] = True
            points += 50
            detected = True

    return marked_for_removal, points, detected


def detect_L_shape_from_position(matrix, start_row, start_col):
    marked_for_removal = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    points = 0
    detected = False
    candy_type = matrix[start_row][start_col]
    # Verificam daca exista un tip de bomboana în pozitia de start
    if candy_type == 0:
        return marked_for_removal, points, detected

    # Verificam cele patru rotatii posibile ale formei "L"
    # 1. L orientat în coltul stanga-jos
    if (start_row + 2 < len(matrix) and start_col + 1 < len(matrix[0]) and
        matrix[start_row + 1][start_col] == candy_type and
        matrix[start_row + 2][start_col] == candy_type and
        matrix[start_row + 2][start_col + 1] == candy_type and
        matrix[start_row][start_col + 1] == candy_type):
        detected = True
        points = 20
        marked_for_removal[start_row][start_col] = True
        marked_for_removal[start_row + 1][start_col] = True
        marked_for_removal[start_row + 2][start_col] = True
        marked_for_removal[start_row + 2][start_col + 1] = True
        marked_for_removal[start_row][start_col + 1] = True

    # 2. L orientat în coltul dreapta-jos
    elif (start_row + 2 < len(matrix) and start_col - 1 >= 0 and
          matrix[start_row + 1][start_col] == candy_type and
          matrix[start_row + 2][start_col] == candy_type and
          matrix[start_row + 2][start_col - 1] == candy_type and
          matrix[start_row][start_col - 1] == candy_type):
        detected = True
        points = 20
        marked_for_removal[start_row][start_col] = True
        marked_for_removal[start_row + 1][start_col] = True
        marked_for_removal[start_row + 2][start_col] = True
        marked_for_removal[start_row + 2][start_col - 1] = True
        marked_for_removal[start_row][start_col - 1] = True

    # 3. L orientat în coltul stanga-sus
    elif (start_row - 2 >= 0 and start_col + 1 < len(matrix[0]) and
          matrix[start_row - 1][start_col] == candy_type and
          matrix[start_row - 2][start_col] == candy_type and
          matrix[start_row - 2][start_col + 1] == candy_type and
          matrix[start_row][start_col + 1] == candy_type):
        detected = True
        points = 20
        marked_for_removal[start_row][start_col] = True
        marked_for_removal[start_row - 1][start_col] = True
        marked_for_removal[start_row - 2][start_col] = True
        marked_for_removal[start_row - 2][start_col + 1] = True
        marked_for_removal[start_row][start_col + 1] = True

    # 4. L orientat în coltul dreapta-sus
    elif (start_row - 2 >= 0 and start_col - 1 >= 0 and
          matrix[start_row - 1][start_col] == candy_type and
          matrix[start_row - 2][start_col] == candy_type and
          matrix[start_row - 2][start_col - 1] == candy_type and
          matrix[start_row][start_col - 1] == candy_type):
        detected = True
        points = 20
        marked_for_removal[start_row][start_col] = True
        marked_for_removal[start_row - 1][start_col] = True
        marked_for_removal[start_row - 2][start_col] = True
        marked_for_removal[start_row - 2][start_col - 1] = True
        marked_for_removal[start_row][start_col - 1] = True

    return marked_for_removal, points, detected


def detect_T_shape_from_position(matrix, start_row, start_col):
    marked_for_removal = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    points = 0
    detected = False
    candy_type = matrix[start_row][start_col]
    # Verificam daca exista un tip de bomboana în pozitia de start
    if candy_type == 0:
        return marked_for_removal, points, detected

    # Verificam cele patru rotatii posibile ale formei "T"
    # 1. T cu piciorul in jos
    if (start_row + 1 < len(matrix) and start_row - 1 >= 0 and start_col + 1 < len(matrix[0]) and
        matrix[start_row][start_col + 1] == candy_type and
        matrix[start_row + 1][start_col] == candy_type and
        matrix[start_row - 1][start_col] == candy_type):
        detected = True
        points = 30
        marked_for_removal[start_row][start_col] = True
        marked_for_removal[start_row][start_col + 1] = True
        marked_for_removal[start_row + 1][start_col] = True
        marked_for_removal[start_row - 1][start_col] = True

    # 2. T cu piciorul in sus
    elif (start_row + 2 < len(matrix) and start_col - 1 >= 0 and start_col + 1 < len(matrix[0]) and
          matrix[start_row + 1][start_col] == candy_type and
          matrix[start_row + 2][start_col] == candy_type and
          matrix[start_row + 1][start_col - 1] == candy_type and
          matrix[start_row + 1][start_col + 1] == candy_type):
        detected = True
        points = 30
        marked_for_removal[start_row][start_col] = True
        marked_for_removal[start_row + 1][start_col] = True
        marked_for_removal[start_row + 2][start_col] = True
        marked_for_removal[start_row + 1][start_col - 1] = True
        marked_for_removal[start_row + 1][start_col + 1] = True

    # 3. T cu piciorul la dreapta
    elif (start_row + 1 < len(matrix) and start_row - 1 >= 0 and start_col + 1 < len(matrix[0]) and
          matrix[start_row][start_col + 1] == candy_type and
          matrix[start_row + 1][start_col] == candy_type and
          matrix[start_row - 1][start_col] == candy_type):
        detected = True
        points = 30
        marked_for_removal[start_row][start_col] = True
        marked_for_removal[start_row][start_col + 1] = True
        marked_for_removal[start_row + 1][start_col] = True
        marked_for_removal[start_row - 1][start_col] = True

    # 4. T cu piciorul la stanga
    elif (start_row + 1 < len(matrix) and start_row - 1 >= 0 and start_col - 1 >= 0 and
          matrix[start_row][start_col - 1] == candy_type and
          matrix[start_row + 1][start_col] == candy_type and
          matrix[start_row - 1][start_col] == candy_type):
        detected = True
        points = 30
        marked_for_removal[start_row][start_col] = True
        marked_for_removal[start_row][start_col - 1] = True
        marked_for_removal[start_row + 1][start_col] = True
        marked_for_removal[start_row - 1][start_col] = True

    return marked_for_removal, points, detected



def candies_fall(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for j in range(cols):
        pointer = rows - 1
        for i in range(rows - 1, -1, -1):
            if matrix[i][j] != 0:
                matrix[pointer][j] = matrix[i][j]
                if pointer != i:
                    matrix[i][j] = 0
                pointer -= 1

        for i in range(pointer, -1, -1):
            matrix[i][j] = 0
    return matrix


def generate_new_candies(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for j in range(cols):
        for i in range(rows):
            if matrix[i][j] == 0:
                matrix[i][j] = random.randint(1, 4)
    return matrix

def update_matrix(matrix, marked_for_removal):
    # Eliminam bomboanele marcate
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if marked_for_removal[i][j]:
                matrix[i][j] = 0
    matrix = candies_fall(matrix)
    matrix = generate_new_candies(matrix)
    return matrix


def check_for_formations(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # 1. Verificam linie de 5
            if j <= len(matrix[0]) - 5:
                _, _, detected = detect_line_of_5_from_position(matrix, i, j)
                if detected:
                    return True

            # 2. Verificam formatiune de tip T
            if i <= len(matrix) - 3 and j <= len(matrix[0]) - 3:
                _, _, detected = detect_T_shape_from_position(matrix, i, j)
                if detected:
                    return True

            # 3. Verificam formatiune de tip L
            if i <= len(matrix) - 3 and j <= len(matrix[0]) - 2:
                _, _, detected = detect_L_shape_from_position(matrix, i, j)
                if detected:
                    return True

            # 4. Verificam linie de 4
            if j <= len(matrix[0]) - 4:
                _, _, detected = detect_line_of_4_from_position(matrix, i, j)
                if detected:
                    return True

            # 5. Verificam linie de 3
            if j <= len(matrix[0]) - 3:
                _, _, detected = detect_line_of_3_from_position(matrix, i, j)
                if detected:
                    return True

    # Daca nu am gasit nicio formatiune, returnam False
    return False

def candy_crush_game():
    matrix = init_matrix()
    total_points = 0
    max_points = 10000
    swap_attempts = 0

    def is_potential_swap(matrix, i1, j1, i2, j2):
        """
        Verifica daca interschimbarea intre doua pozitii are potential sa creeze o formatiune.
        """
        # Interschimbam temporar
        matrix[i1][j1], matrix[i2][j2] = matrix[i2][j2], matrix[i1][j1]
        # Verificam dacă exista vreo formatiune dupa interschimbare
        has_formation = check_for_formations(matrix)
        # Revenim la configuratia initiala
        matrix[i1][j1], matrix[i2][j2] = matrix[i2][j2], matrix[i1][j1]
        return has_formation

    while total_points < max_points:
        elimination_occurred = False

        # Verificam formatiunile in ordine descrescatoare de puncte
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # 1. Verificam linie de 5
                if j <= len(matrix[0]) - 5:
                    marked_for_removal, points, detected = detect_line_of_5_from_position(matrix, i, j)
                    if detected:
                        elimination_occurred = True
                        total_points += points
                        matrix = update_matrix(matrix, marked_for_removal)
                        break

                # 2. Verificam formatiune de tip T
                if i <= len(matrix) - 3 and j <= len(matrix[0]) - 3:
                    marked_for_removal, points, detected = detect_T_shape_from_position(matrix, i, j)
                    if detected:
                        elimination_occurred = True
                        total_points += points
                        matrix = update_matrix(matrix, marked_for_removal)
                        break

                # 3. Verificam formatiune de tip L
                if i <= len(matrix) - 3 and j <= len(matrix[0]) - 2:
                    marked_for_removal, points, detected = detect_L_shape_from_position(matrix, i, j)
                    if detected:
                        elimination_occurred = True
                        total_points += points
                        matrix = update_matrix(matrix, marked_for_removal)
                        break

                # 4. Verificam linie de 4
                if j <= len(matrix[0]) - 4:
                    marked_for_removal, points, detected = detect_line_of_4_from_position(matrix, i, j)
                    if detected:
                        elimination_occurred = True
                        total_points += points
                        matrix = update_matrix(matrix, marked_for_removal)
                        break

                # 5. Verificam linie de 3
                if j <= len(matrix[0]) - 3:
                    marked_for_removal, points, detected = detect_line_of_3_from_position(matrix, i, j)
                    if detected:
                        elimination_occurred = True
                        total_points += points
                        matrix = update_matrix(matrix, marked_for_removal)
                        break

        # Daca nu s-a gasit nicio formatiune, incercam sa facem interschimbari
        if not elimination_occurred:
            # Parcurgem matricea si încercam interschimbari intre elemente adiacente
            swap_successful = False
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    # Verificam cele patru directii pentru interschimbare
                    if j < len(matrix[0]) - 1 and is_potential_swap(matrix, i, j, i, j + 1):
                        # Interschimbare orizontala dreapta
                        matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
                        swap_attempts += 1
                        swap_successful = True
                        break
                    if j > 0 and is_potential_swap(matrix, i, j, i, j - 1):
                        # Interschimbare orizontala stanga
                        matrix[i][j], matrix[i][j - 1] = matrix[i][j - 1], matrix[i][j]
                        swap_attempts += 1
                        swap_successful = True
                        break
                    if i < len(matrix) - 1 and is_potential_swap(matrix, i, j, i + 1, j):
                        # Interschimbare verticala jos
                        matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
                        swap_attempts += 1
                        swap_successful = True
                        break
                    if i > 0 and is_potential_swap(matrix, i, j, i - 1, j):
                        # Interschimbare verticala sus
                        matrix[i][j], matrix[i - 1][j] = matrix[i - 1][j], matrix[i][j]
                        swap_attempts += 1
                        swap_successful = True
                        break
                if swap_successful:
                    break
            # Daca nu am gasit nicio formatiune prin interschimbari, jocul se incheie
            if not swap_successful:
                return swap_attempts
        matrix = candies_fall(matrix)
        matrix = generate_new_candies(matrix)
    return swap_attempts



if __name__ == "__main__":
    total_attempts = 0
    num_trials = 100
    for _ in range(num_trials):
        attempts = candy_crush_game()
        total_attempts += attempts
    average_attempts = total_attempts // num_trials
    print(f"Media numărului de interschimbări în {num_trials} jocuri este: {average_attempts}")

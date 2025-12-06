def solution():
    with open("input.txt", "r") as file:
        matrix = []
        for line in file:
            matrix.append(line.strip())
        accessible_roll_count = 0
        for row_index, row in enumerate(matrix):
            for col_index, col in enumerate(row):
                if col == ".":
                    continue
                neighbors = get_neighbors(matrix, row_index, col_index)
                rollcount = 0
                if neighbors.count("@") < 4:
                    accessible_roll_count += 1
                
        return accessible_roll_count


def get_neighbors(matrix, row_index, col_index):
    neighbors = []
    for i in range(row_index - 1, row_index + 2):
        for j in range(col_index - 1, col_index + 2):
            if i == row_index and j == col_index:
                continue
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[i]):
                neighbors.append(matrix[i][j])
    return neighbors


print(solution())


###
###
###
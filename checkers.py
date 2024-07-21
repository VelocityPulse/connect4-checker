import numpy


def check_horizontal_winner(player: chr, data: list[str]) -> bool:
    print("\tcheck_horizontal_winner - player " + player + ":")
    winner_pattern = player * 4

    for elem in data:
        if winner_pattern in elem:
            print("\t\tfound winner patter: " + elem)
            return True
    return False


def check_vertical_winner(player: chr, data: list[str]) -> bool:
    print("\tcheck_vertical_winner - player " + player + ":")
    winner_pattern = player * 4

    vertical_columns = []
    for h_idx in range(len(data[0])):
        column = ""
        for v_idx, datum in enumerate(data):
            column = column + data[v_idx][h_idx]
        vertical_columns = vertical_columns + [column]

    # print("\t\tvertical_columns = " + vertical_columns.__str__())

    for elem in vertical_columns:
        if winner_pattern in elem:
            print("\t\tfound winner patter: " + elem)
            return True
    return False


def check_diagonal_winner(player: chr, data: list[str]) -> bool:
    print("\tcheck_diagonal_winner - player " + player + ":")
    winner_pattern = player * 4

    max_col = len(data[0])
    max_row = len(data)
    cols = [[] for _ in range(max_col)]
    rows = [[] for _ in range(max_row)]
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -max_row + 1

    for x in range(max_col):
        for y in range(max_row):
            cols[x].append(data[y][x])
            rows[y].append(data[y][x])
            fdiag[x + y].append(data[y][x])
            bdiag[x - y - min_bdiag].append(data[y][x])

    for elem in fdiag:
        if winner_pattern in "".join(elem):
            print("\t\tfound winner patter: " + "".join(elem))
            return True

    for elem in bdiag:
        if winner_pattern in "".join(elem):
            print("\t\tfound winner patter: " + "".join(elem))
            return True
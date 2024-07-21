import string

from checkers import check_horizontal_winner, check_vertical_winner, check_diagonal_winner


def translate_brut_data(brut_data: str) -> list:
    print("\ttranslate_brut_data:")

    split_data = brut_data.split('\n')
    print("\t\tsplit_data =\t" + split_data.__str__())

    for idx, elem in enumerate(split_data):
        split_data[idx] = (elem
                           .replace("|   |", "| . |")
                           .replace("|   |", "| . |"))
    print("\t\texplicit_data =\t" + split_data.__str__())

    for idx, elem in enumerate(split_data):
        split_data[idx] = elem.replace(' ', '')
    print("\t\ttrimmed_data =\t" + split_data.__str__())

    for idx, elem in enumerate(split_data):
        split_data[idx] = elem.replace("|", '')
    print("\t\tpure_data = \t" + split_data.__str__())

    return split_data


def process(brut_data: string):
    print("\nprocess:")
    tab_game = translate_brut_data(brut_data)

    if check_horizontal_winner('X', tab_game):
        return print("winner is X !")
    elif check_horizontal_winner('O', tab_game):
        return print("winner is O !")

    elif check_vertical_winner('X', tab_game):
        return print("winner is X !")
    elif check_vertical_winner('O', tab_game):
        return print("winner is O !")

    elif check_diagonal_winner('X', tab_game):
        return print("winner is X !")
    elif check_diagonal_winner('O', tab_game):
        return print("winner is O !")

    print("No winner yet !")

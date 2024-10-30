import logos
STONE_1 = "O"
STONE_2 = "@"
board_full = False
current_player_index = 1
ROWS = 6
COLUMNS = 7
EMPTY_FIELD = " "
play_board = [[EMPTY_FIELD] * COLUMNS for i in range(ROWS)]


def print_board():
    print(logos.logo3)
    for r in play_board:
        print("|" + "|".join(r) + '|')


def place_stone(column_index, stone):
    for row in play_board[::-1]:
        if row[column_index] == EMPTY_FIELD:
            row[column_index] = stone
            break


def player_wins(stone, player_name):
    global we_have_a_winner
    for row in range(ROWS): # 4 x rows
        for column in range(COLUMNS):
def is_column_full(column_index):
    if play_board[0][column_index] == EMPTY_FIELD:
        return False
    else:
        return True


def player_wins():
    player_name = [player_name_1, player_name_2][current_player_index]
    stone = [STONE_1, STONE_2][current_player_index]
    for row in range(ROWS): # 4 in a row
        for column in range(COLUMNS - 3):
            if (play_board[row][column] == stone
                    and play_board[row][column + 1] == stone
                    and play_board[row][column + 2] == stone
                    and play_board[row][column + 3] == stone):
                print(f"\n  '{player_name}' wins!")
                return True

    for row in range(ROWS - 3): # 4 in a column
        for column in range(COLUMNS ):
            if (play_board[row][column] == stone
                    and play_board[row + 1][column] == stone
                    and play_board[row + 2][column] == stone
                    and play_board[row + 3][column] == stone):
                print(f"\n  '{player_name}' wins!")
                return True

    for row in range(ROWS): # 4 x diagonal ansteigend
        for column in range(COLUMNS - 3):
            if (play_board[row][column] == stone
                    and play_board[row - 1][column + 1] == stone        # column + 1 gibt fehler bei column 7 aus
                    and play_board[row - 2][column + 2] == stone
                    and play_board[row - 3][column + 3] == stone):
                print(f"\n  '{player_name}' wins!")
                return True

    for row in range(ROWS - 3): # 4 x diagonal absteigend
        for column in range(COLUMNS - 3):
            if (play_board[row][column] == stone
                    and play_board[row + 1][column + 1] == stone
                    and play_board[row + 2][column + 2] == stone
                    and play_board[row + 3][column + 3] == stone):
                print(f"\n  '{player_name}' wins!")
                return True
    return False

def ask_players_for_turn(player_name, stone):
    while True:
        column = int(input("\n" + player_name + " ist mit '" + stone + "' am Zug: "))            # if column != int erneute Spielerabfrage
        if 1 <= column <= 7:
            column_index = column - 1
            if is_column_full(column_index):
                print("Die Spalte ist voll.")
            else:
                place_stone(column_index, stone)
                print("\n" * 10)
                print_board()
                break
        else:
            print("Bitte die Eingabe korrigieren und nur Zahlen zwischen 1 und 7 wählen")
            # Schleife von vorne starten


# Willkommensbildschirm
print(logos.willkommen2)

# Spieler werden gebeten ihre Namen einzugeben
player_name_1 = input("Spieler 1: Bitte geben Sie ihren Namen ein: ")
print(player_name_1 + " spielt mit: " + STONE_1)
player_name_2 = input("Spieler 2:Bitte geben Sie ihren Namen ein: ")
print(player_name_2 + " spielt mit: " + STONE_2)

print("Bitte lege dinen Stein in eine der Spalten 1, 2, 3, 4, 5, 6 oder 7")

while not is_board_full() and not player_wins():
    current_player_index = (current_player_index + 1) % 2
    current_player_name = [player_name_1, player_name_2][current_player_index]
    current_player_stone = [STONE_1, STONE_2][current_player_index]
    ask_players_for_turn(current_player_name, current_player_stone)


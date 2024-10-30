import logos
STONE_1 = "O"
STONE_2 = "@"
board_full = False
we_have_a_winner = False
ROWS = 6
COLUMNS = 7
EMPTY_FIELD = " "
play_board = [[EMPTY_FIELD] * COLUMNS for i in range(ROWS)]


def print_board():
    print(logos.logo3)
    for r in play_board:
        print("|" + "|".join(r) + '|')


def place_stone(column, stone):
    column_index = column - 1
    for row in play_board[::-1]:
        if row[column_index] == EMPTY_FIELD:
            row[column_index] = stone
            break


def player_wins(stone, player_name):
    global we_have_a_winner
    for row in range(ROWS): # 4 x rows
        for column in range(COLUMNS):
            if (play_board[row][column] == stone
                    and play_board[row][column - 1] == stone        # gibt fehler bei column 7 aus
                    and play_board[row][column - 2] == stone
                    and play_board[row][column - 3] == stone):
                print(f"Player {player_name} wins")
                we_have_a_winner = True
                return we_have_a_winner

    for row in range(ROWS): # 4 x columns
        for column in range(COLUMNS):
            if (play_board[row][column] == stone
                    and play_board[row - 1][column] == stone
                    and play_board[row - 2][column] == stone
                    and play_board[row - 3][column] == stone):
                print(f"Player {player_name} wins")
                we_have_a_winner = True
                return we_have_a_winner

    for row in range(ROWS): # 4 x diagonal negativ
        for column in range(COLUMNS):
            if (play_board[row][column] == stone
                    and play_board[row - 1][column - 6] == stone        # column + 1 gibt fehler bei column 7 aus
                    and play_board[row - 2][column - 5] == stone
                    and play_board[row - 3][column - 4] == stone):
                print(f"Player {player_name} wins")
                we_have_a_winner = True
                return we_have_a_winner

    for row in range(ROWS): # 4 x diagonal positiv
        for column in range(COLUMNS):
            if (play_board[row][column] == stone
                    and play_board[row - 1][column - 1] == stone
                    and play_board[row - 2][column - 2] == stone
                    and play_board[row - 3][column - 3] == stone):
                print(f"Player {player_name} wins")
                we_have_a_winner = True
                return we_have_a_winner


def ask_players_for_turn(player_name, stone):
    while True:
        column = int(input("\n" + player_name + " ist mit '" + stone + "' am Zug: "))            # if column != int erneute Spielerabfrage
        if 1 <= column <= 7:
            place_stone(column, stone)
            print_board()
            break
        else:
            print("Bitte die Eingabe korrigieren und nur Zahlen zwischen 1 und 7 wählen")
            # Schleife von vorne starten
    print("\n" * 10)

# Willkommensbildschirm
print(logos.willkommen2)

# Spieler werden gebeten ihre Namen einzugeben
player_name_1 = input("Spieler 1: Bitte geben Sie ihren Namen ein: ")
print(player_name_1 + " spielt mit: " + STONE_1)
player_name_2 = input("Spieler 2:Bitte geben Sie ihren Namen ein: ")
print(player_name_2 + " spielt mit: " + STONE_2)

print("Bitte lege dinen Stein in eine der Spalten 1, 2, 3, 4, 5, 6 oder 7")

while not board_full and not we_have_a_winner:
    ask_players_for_turn(player_name_1, STONE_1)
    if player_wins(STONE_1, player_name_1):
        break
    ask_players_for_turn(player_name_2, STONE_2)
    if player_wins(STONE_2, player_name_2):
        break

STONE_1 = "O"
STONE_2 = "@"
board_full = False
we_have_a_winner = False
ROWS = 6
COLUMNS = 7
EMPTY_FIELD = " "
play_board = [[EMPTY_FIELD] * COLUMNS for i in range(ROWS)]


def print_board():
    for r in play_board:
        print("|" + "|".join(r) + '|')


def ask_players_for_turn(player_name, stone):
    while True:
        column = int(input(player_name + " ist am Zug"))
        if 1 <= column <= 7:
            play_board[row][column - 1] = stone  # Lege den Stein
            print_board()
            break
        else:
            print("Bitte die Eingabe korrigieren und nur Zahlen zwischen 1 und 7 wählen")
            # Schleife von vorne starten
        print("\n")


# Willkommensbildschirm
print("Herzlich Willkommen zu Vier Gewinnt")

# Spieler werden gebeten ihre Namen einzugeben
player_name_1 = input("Spieler 1: Bitte geben Sie ihren Namen ein: ")
print(player_name_1 + " spielt mit: " + STONE_1)
player_name_2 = input("Spieler 2:Bitte geben Sie ihren Namen ein: ")
print(player_name_2 + " spielt mit: " + STONE_2)

print("Bitte lege dinen Stein in eine der Spalten 1, 2, 3, 4, 5, 6 oder 7")

while not board_full and not we_have_a_winner:
    ask_players_for_turn(player_name_1, STONE_1)
    ask_players_for_turn(player_name_2, STONE_2)

STONE_1 = "0"
STONE_2 = "@"
board_full = False
we_have_a_winner = False


def print_board():
    print('''
     1 2 3 4 5 6 7
    | | | | | | | |
    | | | | | | | |
    | | | | | | | |
    | | | | | | | |
    | | | | | | | |
    | | | | | | | |
    ''')


def ask_players_for_turn(player_name, stone):
    while True:
        turn = int(input(player_name + " ist am Zug"))
        if 1 <= turn <= 7:
            print(stone + "legen")  # Lege den Stein
            break
        else:
            print("Bitte die Eingabe korrigieren und nur Zahlen zwischen 1 und 7 wählen")
            # Schleife von vorne starten


# Willkommensbildschirm
print("Herzlich Willkommen zu Vier Gewinnt")

# Spieler werden gebeten ihre Namen einzugeben
player_name_1 = input("Spieler 1: Bitte geben Sie ihren Namen ein: ")
print(player_name_1 + " spielt mit: " + STONE_1)
player_name_2 = input("Spieler 2:Bitte geben Sie ihren Namen ein: ")
print(player_name_2 + " spielt mit: " + STONE_2)

print("Bitte lege dinen Stein in eine der Spalten 1, 2, 3, 4, 5, 6 oder 7")
# Spieler wird aufgefordert den Stein in Spalte 1 - 7 zu legen

while not board_full and not we_have_a_winner:
    ask_players_for_turn(player_name_1, STONE_1)
    print_board()
    ask_players_for_turn(player_name_2, STONE_2)
    print_board()

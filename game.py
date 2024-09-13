
STONE_1 = "0"
STONE_2 = "@"

# Willkommensbildschirm
print("Herzlich Willkommen zu Vier Gewinnt")

# Spieler werden gebeten ihre Namen einzugeben
player_name_1 = input("Spieler 1: Bitte geben Sie ihren Namen ein: ")
print(player_name_1 + " spielt mit: " + STONE_1)
player_name_2 = input("Spieler 2:Bitte geben Sie ihren Namen ein: ")
print(player_name_2 + " spielt mit: " + STONE_2)

print("Bitte lege dinen Stein in eine der Spalten 1, 2, 3, 4, 5, 6 oder 7")
# Spieler wird aufgefordert den Stein in Spalte 1 - 7 zu legen


turn_1 = int(input(player_name_1 + " ist am Zug"))
if 1 <= turn_1 <= 7:
    print("Stein legen")  # Lege den Stein
else:
    print("Bitte die Eingabe korrigieren und nur Zahlen zwischen 1 und 7 wählen")
    # Schleife von vorne starten

turn_2 = int(input(player_name_2 + " ist am Zug"))
if 1 <= turn_2 <= 7:
    print("Stein legen")  # Lege den Stein
else:
    print("Bitte die Eingabe korrigieren und nur Zahlen zwischen 1 und 7 wählen")


play_board = print('''
 1 2 3 4 5 6 7
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
''')

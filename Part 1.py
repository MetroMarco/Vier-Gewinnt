# Willkommensbildschirm
print("Herzlich Willkommen zu Vier Gewinnt")

# Spieler werden gebeten ihre Namen einzugeben
Spielername1 = input("Spieler 1: Bitte geben Sie ihren Namen ein: ")
print(Spielername1 + " spielt mit O")
Spielername2 = input("Spieler 2:Bitte geben Sie ihren Namen ein: ")
print(Spielername2 + " spielt mit @")

print("Bitte lege dinen Stein in eine der Spalten 1, 2, 3, 4, 5, 6 oder 7")
# Spieler wird aufgefordert den Stein in Spalte 1 - 7 zu legen

zug_1 = int(input(Spielername1 + " ist am Zug"))
if 1 <= zug_1 <= 7:
    print("Stein legen") # Lege den Stein
else:
    print("Bitte die Eingabe korrigieren und nur Zahlen zwischen 1 und 7 wählen")
        # Schleife von vorne starten

zug_2 = int(input(Spielername2 + " ist am Zug"))
if 1 <= zug_2 <= 7:
    print("Stein legen")# Lege den Stein
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


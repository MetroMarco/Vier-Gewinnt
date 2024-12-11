import logos
import json
from game_values import *
from pathlib import Path
from threading import Thread


def current_player_name():
    return [player_name_1, player_name_2][current_player_index]


def print_board():
    print(logos.logo3)
    for r in play_board:
        print("|" + "|".join(r) + '|')


def place_stone(column_index, stone):
    for row in play_board[::-1]:
        if row[column_index] == EMPTY_FIELD:
            row[column_index] = stone
            break


def is_column_full(column_index):
    if play_board[0][column_index] == EMPTY_FIELD:
        return False
    else:
        return True


def is_board_full():
    for column in range(COLUMNS):
        if play_board[0][column] == EMPTY_FIELD:
            return False
    return True


def player_wins():
    player_name = current_player_name()
    stone = [STONE_1, STONE_2][current_player_index]
    for row in range(ROWS):  # 4 in a row
        for column in range(COLUMNS - 3):
            if (play_board[row][column] == stone
                    and play_board[row][column + 1] == stone
                    and play_board[row][column + 2] == stone
                    and play_board[row][column + 3] == stone):
                print(f"\n  '{player_name}' hat gewonnen!")
                return True

    for row in range(ROWS - 3):  # 4 in a column
        for column in range(COLUMNS):
            if (play_board[row][column] == stone
                    and play_board[row + 1][column] == stone
                    and play_board[row + 2][column] == stone
                    and play_board[row + 3][column] == stone):
                print(f"\n  '{player_name}' hat gewonnen!")
                return True

    for row in range(ROWS):  # 4 x diagonal ansteigend
        for column in range(COLUMNS - 3):
            if (play_board[row][column] == stone
                    and play_board[row - 1][column + 1] == stone
                    and play_board[row - 2][column + 2] == stone
                    and play_board[row - 3][column + 3] == stone):
                print(f"\n  '{player_name}' hat gewonnen!")
                return True

    for row in range(ROWS - 3):  # 4 x diagonal absteigend
        for column in range(COLUMNS - 3):
            if (play_board[row][column] == stone
                    and play_board[row + 1][column + 1] == stone
                    and play_board[row + 2][column + 2] == stone
                    and play_board[row + 3][column + 3] == stone):
                print(f"\n  '{player_name}' hat gewonnen!")
                return True
    return False


def ask_players_for_turn(stone):
    while True:
        column = input("\n" + current_player_name() + " ist mit '" + stone + "' am Zug: ")
        try:
            column = int(column)
        except ValueError:
            print("Bitte nur Zahlen eingeben!")
        else:
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
                print("Bitte die Eingabe korrigieren und nur Zahlen zwischen 1 und 7 wählen.")
                # Schleife von vorne starten

# Die aktuellen Werte in die JSON Datei schreiben
def get_game_data():
    return {
        "STONE_1": STONE_1,
        "STONE_2": STONE_2,
        "board_full": board_full,
        "current_player_index": current_player_index,
        "ROWS": ROWS,
        "COLUMNS": COLUMNS,
        "EMPTY_FIELD": EMPTY_FIELD,
        "play_board": play_board,
        "player_name_1": player_name_1,
        "player_name_2": player_name_2
    }


def dump_get_game_data():
    with open("game_data.json", "w") as json_file:
        json.dump(get_game_data(), json_file, indent=4)


#Werte in JSON Datei zurücksetzen, damit ein neues Spiel gestartet werden kann
def reset_game_data():
    return {
        "STONE_1": STONE_1,
        "STONE_2": STONE_2,
        "board_full": False,
        "current_player_index": current_player_index,
        "ROWS": ROWS,
        "COLUMNS": COLUMNS,
        "EMPTY_FIELD": EMPTY_FIELD,
        "play_board": [[EMPTY_FIELD] * COLUMNS for i in range(ROWS)],
        "player_name_1": "Spieler 1",
        "player_name_2": "Spieler 2"
    }


# Variablen aus den JSON-Daten setzen
def set_game_data(game_data):
    global STONE_1, STONE_2, current_player_index, ROWS, COLUMNS, EMPTY_FIELD, play_board, player_name_1, player_name_2, board_full
    STONE_1 = game_data["STONE_1"]
    STONE_2 = game_data["STONE_2"]
    board_full = game_data["board_full"]
    current_player_index = game_data["current_player_index"]
    ROWS = game_data["ROWS"]
    COLUMNS = game_data["COLUMNS"]
    EMPTY_FIELD = game_data["EMPTY_FIELD"]
    play_board = game_data["play_board"]
    player_name_1 = game_data["player_name_1"]
    player_name_2 = game_data["player_name_2"]



# Highscore JSON Datei erstellen, falls nicht vorhanden
HIGHSCORE_FILE_NAME = 'highscore.json'
HIGHSCORE_FILE = Path(HIGHSCORE_FILE_NAME)
if not HIGHSCORE_FILE.is_file():
    with open(HIGHSCORE_FILE_NAME, 'w') as json_file:
        json.dump(highscore, json_file, indent=4)

# game_data.JSON erstellen, falls noch nicht vorhanden
GAME_VALUES_NAME = 'game_data.json'
GAME_VALUES = Path(GAME_VALUES_NAME)
if not GAME_VALUES.is_file():
    with open(GAME_VALUES_NAME, 'w') as json_file:
        game_data = reset_game_data()
        json.dump(game_data, json_file, indent=4)

# Spiel in der Konsole
# def play_game_in_console():
# Willkommensbildschirm
print(logos.willkommen2)

load_last_game = input("Möchtest du das letzte Spiel laden? Y/N").lower()
while True:
    if load_last_game == "y":
        with open('game_data.json', 'r') as json_file:
            game_data = json.load(json_file)
            set_game_data(game_data)
    else:
        with open("game_data.json", "r") as json_file:
            json.load(json_file)
            set_game_data(reset_game_data())
        # Spieler werden gebeten ihre Namen einzugeben
        player_name_1 = input("Spieler 1: Bitte geben Sie ihren Namen ein: ")
        print(player_name_1 + " spielt mit: " + STONE_1)
        player_name_2 = input("Spieler 2:Bitte geben Sie ihren Namen ein: ")
        print(player_name_2 + " spielt mit: " + STONE_2)
        dump_get_game_data()


    print_board()
    print("Bitte lege deinen Stein in eine der Spalten 1, 2, 3, 4, 5, 6 oder 7")

    # Schleife vom Hauptspiel
    while not is_board_full() and not player_wins():
        with open('game_data.json', 'r') as json_file:
            json.load(json_file)
            current_player_index = (current_player_index + 1) % 2
            current_player_stone = [STONE_1, STONE_2][current_player_index]
            ask_players_for_turn(current_player_stone)
            dump_get_game_data()

    if is_board_full() and not player_wins():
        print("!!!WOW!!! Das Spiel endet unentschiden.")

    # Highscore Namen und Siege hinzufügen
    with open(HIGHSCORE_FILE_NAME, 'r') as json_file:
        highscore = json.load(json_file)
        if current_player_name() in highscore:
            highscore[current_player_name()]["won"] += 1
            with open(HIGHSCORE_FILE_NAME, 'w') as json_file:
                json.dump(highscore, json_file, indent=4)
        else:
            highscore.update({current_player_name(): {"won": 1}})
            with open(HIGHSCORE_FILE_NAME, 'w') as json_file:
                json.dump(highscore, json_file, indent=4)


    if input("\nMöchtest du ein neues Spiel starten? Y/N").lower() == "y":
        with open('game_data.json', 'w') as json_file:
            json.dump(reset_game_data(), json_file, indent=4)
        with open("game_data.json", "r") as json_file:
            game_data = json.load(json_file)
            set_game_data(reset_game_data())
        load_last_game = "n"
    else:
        print("\nDanke fürs spielen.")
        break

# def play_game_in_tkinter():



#
# thread_console = Thread(target=play_game_in_console)
# thread_console.start()

# Oberfläche anzeigen

# Variablen, Spielernamen und Spielfeld
STONE_1 = "O"
STONE_2 = "@"
board_full = False
current_player_index = 1
ROWS = 6
COLUMNS = 7
EMPTY_FIELD = " "
play_board = [[EMPTY_FIELD] * COLUMNS for i in range(ROWS)]

player_name_1 = "Spieler1"
player_name_2 = "Spieler2"
we_have_a_winner = False

highscore = {
    "Spieler": {
        "won": 0
    }
}
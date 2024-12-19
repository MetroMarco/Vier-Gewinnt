# Game designed and created by Marco Wolf
# Art from <a href="https://www.textstudio.com/">Font generator</a>

from tkinter import *
from tkinter import ttk
import json
from tkinter import messagebox
import os
import time
import game_values as gv

window = Tk()
window.title("4-Gewinnt")
window.geometry('660x730')
window.config(bg="yellow")
logo = PhotoImage(file='4-Gewinnt-art.png')
logo_big = logo.zoom(2)
logo_small = logo_big.subsample(3)
logo_highscore = PhotoImage(file='highscore-art.png')
logo_highscore_big = logo_highscore.zoom(2)
logo_highscore_small = logo_highscore_big.subsample(3)
currentPlayerColor = "pink"
players_name = "unknown"
seconds = 1
play_board = [[0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0]]


# Mehrere tabs anzeigen
notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)

notebook.add(tab1, text="Player-Names")
notebook.add(tab2, text="Game")
notebook.add(tab3, text="Highscore")

notebook.pack(fill=BOTH)


# Tab 1 Eingabe der Spielernamen
# Spieler Namen vom Input bekommen und in game_data ablegen
def get_player_1_name():
    player_name_1 = player1.get()  ## get und write player name function seperate
    with open('game_data.json', 'r') as file:
        game_data = json.load(file)
        game_data["player_name_1"] = player_name_1
        with open('game_data.json', 'w') as file:
            json.dump(game_data, file, indent=4)


def get_player_2_name():
    player_name_2 = player2.get()
    with open('game_data.json', 'r') as file:
        game_data = json.load(file)
        game_data["player_name_2"] = player_name_2
        with open('game_data.json', 'w') as file:
            json.dump(game_data, file, indent=4)


def clear_names():
    textfeld1.delete(0,END)
    textfeld2.delete(0,END)


def reset_game_data():
    for row in range(6):
        for column in range(7):
            play_board[row][column] = Button(frame, text="", width=7, height=3, bd=3, relief=SUNKEN, bg="blue")
            play_board[row][column].grid(row=row, column=column)
    with open('game_data.json', 'r') as file:
        game_data = json.load(file)
        gv.current_player_index = 1
        gv.play_board = [[gv.EMPTY_FIELD] * gv.COLUMNS for i in range(gv.ROWS)] # game_data wird nicht gelöscht????
        with open('game_data.json', 'w') as file:
            json.dump(game_data, file, indent=4)


def goto_game():
    notebook.select(tab2)

logo1 = Label(tab1, image=logo_small,bg="red").pack()

leeresfeld = Label(tab1, height=5,).pack()

name_frame = Frame(tab1)
name_frame.pack()
spielerNameLabel_1 = (Label(name_frame, text="Spieler 1: ", font=("Ink Free", 18, "bold"),
                            bg="yellow", width=12, relief="raised", pady=10))
spielerNameLabel_1.grid(row=1, column=1)
player1 = StringVar()
textfeld1 = (Entry(name_frame, font=("Ink Free", 30, "bold"), bg="yellow", width=11, textvariable=player1))
textfeld1.grid(row=1,column=2)
player_1_button = (Button(name_frame, text="Submit", font=("Ink Free", 18, "bold"),
                          width=8, fg="yellow", bg="black", cursor="hand2", relief="ridge", bd=3,
                          command=get_player_1_name))
player_1_button.grid(row=1,column=3)

spielerNameLabel_2 = (Label(name_frame, text="Spieler 2: ", font=("Ink Free", 18, "bold"),
                            bg="red", width=12, relief="raised", pady=10))
spielerNameLabel_2.grid(row=2, column=1)
player2 = StringVar()
textfeld2 = Entry(name_frame, font=("Ink Free", 30, "bold"), bg="red", width=11, textvariable=player2)
textfeld2.grid(row=2,column=2)
player_2_button = (Button(name_frame, text="Submit", font=("Ink Free", 18, "bold"),
                          width=8, fg="red", bg="black", cursor="hand2", relief="ridge", bd=3,
                          command=get_player_2_name))
player_2_button.grid(row=2,column=3)

clear_button = (Button(name_frame, text="Clear\nnames", font=("Ink Free", 18, "bold"), width=11, height=2,
                        fg="yellow", bg="black", cursor="hand2", relief="ridge", padx=5, bd=3, command=clear_names))
clear_button.grid(row=4,column=1)

reset_game_button = Button(name_frame, text="Reset Board\nto start a new Game", font=("Ink Free", 18, "bold"),
                           cursor="hand2", width=18, padx=2, fg="yellow", bg="black", relief="ridge", bd=3,
                           command= reset_game_data)
reset_game_button.grid(row=4,column=2)

goto_game_button = Button(name_frame, text="Go to\nthe Game", font=("Ink Free", 18, "bold"), cursor="hand2",
                           width=8, padx=1, fg="yellow", bg="black", relief="ridge", bd=3, command= goto_game)
goto_game_button.grid(row=4,column=3)

# Tab 2 the game
# Spiellogo Anzeigen
logolabel = Label(tab2, image=logo_small,bg="red").pack()

# Spielernamen anzeigen
simple_name_label = (Label(tab2,text="Name x,y",font=("Consolas",12),bg="blue",fg="white",width=97))
simple_name_label.pack()

def show_and_switch_current_player_names():
    global currentPlayerColor, players_name
    with open('game_data.json', 'r') as file:
        game_data = json.load(file)
        player_names = [game_data["player_name_1"], game_data["player_name_2"]]
        players_name = player_names[game_data["current_player_index"] - 1]
        simple_name_label.config(text=players_name)
        simple_name_label.after(1000, show_and_switch_current_player_names)
        if players_name == game_data["player_name_1"]:
            simple_name_label.config(fg="yellow")
            column_1_button.config(fg="yellow")
            column_2_button.config(fg="yellow")
            column_3_button.config(fg="yellow")
            column_4_button.config(fg="yellow")
            column_5_button.config(fg="yellow")
            column_6_button.config(fg="yellow")
            column_7_button.config(fg="yellow")
            return players_name
        elif players_name == game_data["player_name_2"]:
            simple_name_label.config(fg="red")
            column_1_button.config(fg="red")
            column_2_button.config(fg="red")
            column_3_button.config(fg="red")
            column_4_button.config(fg="red")
            column_5_button.config(fg="red")
            column_6_button.config(fg="red")
            column_7_button.config(fg="red")
            return players_name


def player_wins_popup():
    global players_name
    player_wins_window = Toplevel(window,bg="blue")
    player_wins_window.title("Player Wins")
    player_wins_window.geometry("500x300")
    wins_text = Label(player_wins_window, text=f"{players_name} Wins", font=("Ink Free", 50, "bold"), bg="blue")
    wins_text.pack()
    with open('game_data.json', 'r') as file:
        game_data = json.load(file)
        if players_name == game_data["player_name_1"]:
            wins_text.config(fg="yellow")
        else:
            wins_text.config(fg="red")


# Rahmen für das Spielfeld
frame = Frame(tab2,bg="blue",bd=5,relief=RIDGE)
# Buttons zum Legen der Steine anzeigen und Funktion zum Wiedergeben der Spalte
def click(num,frame):
    column = num
    with open('column_input.json', 'w') as f:
        json.dump(column, f)
    refresh_board(frame)


def refresh_board(frame):
    time.sleep(0.1)
    with open('game_data.json', 'r') as f:
        data = json.load(f)
        json_play_board = data['play_board']
        JSON_STONE_1 = data['STONE_1']
        JSON_STONE_2 = data['STONE_2']
        STONE_1_COLOR = "yellow"
        STONE_2_COLOR = "red"
        we_have_a_winner = data['we_have_a_winner']
        for row in range(6):
            for column in range(7):
                current_stone = json_play_board[row][column]
                if current_stone == JSON_STONE_1:
                    Button(frame, text="", width=7, height=3, bd=3, relief=SUNKEN, bg=STONE_1_COLOR
                           ).grid(row=row,column=column)
                elif current_stone == JSON_STONE_2:
                    Button(frame, text="", width=7, height=3, bd=3, relief=SUNKEN, bg=STONE_2_COLOR
                           ).grid(row=row, column=column)
        if we_have_a_winner:
            player_wins_popup()



column_buttons = Label(tab2)
column_1_button = Button(column_buttons, text=1, font=("Consolas",21),bg="darkblue",fg=currentPlayerColor,
       width=3,relief=RAISED,bd=5, cursor="circle",
       command=lambda: click(1,frame))
column_1_button.pack(side=LEFT)
column_2_button = Button(column_buttons, text=2, font=("Consolas",21),bg="darkblue",fg=currentPlayerColor,width=3,
       relief=RAISED,bd=5, cursor="circle",
       command=lambda: click(2,frame))
column_2_button.pack(side=LEFT)
column_3_button = Button(column_buttons, text=3, font=("Consolas",21),bg="darkblue",fg=currentPlayerColor,width=3,
       relief=RAISED,bd=5, cursor="circle",
       command=lambda: click(3,frame))
column_3_button.pack(side=LEFT)
column_4_button = Button(column_buttons, text=4, font=("Consolas",21),bg="darkblue",fg=currentPlayerColor,width=3,
       relief=RAISED,bd=5, cursor="circle",
       command=lambda: click(4,frame))
column_4_button.pack(side=LEFT)
column_5_button = Button(column_buttons, text=5, font=("Consolas",21),bg="darkblue",fg=currentPlayerColor,width=3,
       relief=RAISED,bd=5, cursor="circle",
       command=lambda: click(5,frame))
column_5_button.pack(side=LEFT)
column_6_button = Button(column_buttons, text=6, font=("Consolas",21),bg="darkblue",fg=currentPlayerColor,width=3,
       relief=RAISED,bd=5, cursor="circle",
       command=lambda: click(6,frame))
column_6_button.pack(side=LEFT)
column_7_button = Button(column_buttons, text=7, font=("Consolas",21),bg="darkblue",fg=currentPlayerColor,width=3,
       relief=RAISED,bd=5, cursor="circle",
       command=lambda: click(7,frame))
column_7_button.pack(side=LEFT)
column_buttons.pack()


# Spielfeld
for row in range(6):
    for column in range(7):
        play_board[row][column] = Button(frame, text="", width=7, height=3, bd=3, relief=SUNKEN, bg="blue")
        play_board[row][column].grid(row=row, column=column)
frame.pack()

show_and_switch_current_player_names()


# # tab3 the Highscore
# Highscore
highscore_label = Label(tab3, image=logo_highscore_small, bg="red")
highscore_label.pack()

with open('highscore.json', 'r') as file:
    highscore = json.load(file)


frame2 = Frame(tab3, bg="blue",bd=5,relief=RIDGE,)
nameLabel = Label(frame2, text="Name",font=("Consolas",18),width=15,bg="darkblue",fg="yellow",
                  bd=3,relief=RIDGE).grid(row=0,column=0)
winsLabel = Label(frame2, text="Wins",font=("Consolas",18),width=15,bg="darkblue",fg="yellow",
                  bd=3,relief=RIDGE).grid(row=0,column=1)

row = 1
for persons in highscore:
    Label(frame2, text=persons,font=("Consolas",12),
          width=20,bg="blue",fg="yellow").grid(row=row,column=0)
    row += 1

row = 1
for persons in highscore:
    Label(frame2, text=highscore[persons].get("won"),font=("Consolas",12),
          width=20,bg="blue",fg="yellow").grid(row=row,column=1)
    row +=1

frame2.pack()

# switch between tabs with the buttons and exit button
def playernametab():
    notebook.select(tab1)

def highscoretab():
    notebook.select(tab3)

def gametab():
    notebook.select(tab2)

def really_quit():
    if messagebox.askyesno("Quit", "Do you really want to quit?"):
        window.destroy()



# Buttons on the bottom
input_name_button = Button(window, text="Name Input", font=("Ink Free",20,"bold"),fg="yellow",bg="black",
                           padx=2,bd=5, relief=RIDGE, cursor="hand2", command= playernametab)
input_name_button.place(x=10, y=655)
button_game = Button(window, text="Game", font=("Ink Free",20,"bold"),fg="yellow", bg="black",
                     padx=20, bd=5, relief=RIDGE, cursor="hand2", command=gametab)
button_game.place(x=203, y=655)

button_highscore = Button(window, text="Highscore", font=("Ink Free",20,"bold"),fg="yellow", bg="black",
                          padx=5, bd=5, relief=RIDGE, cursor="hand2", command=highscoretab)
button_highscore.place(x=350, y=655)

button_quit = Button(window, text="Quit", font=("Ink Free",20,"bold"), fg="red", bg="black",
                     padx=26, bd=5, relief=RIDGE, cursor="hand2", command=really_quit)
button_quit.place(x=517, y=655)

window.mainloop()


# zur Namenseingabe zurück x
# erneut das spiel starten x Spielbrett neu laden x
# spiel Gewonnen anzeigen
# JSON wird noch nicht zurückgesetzt wenn das Spiel noch läuft
# update highscore label

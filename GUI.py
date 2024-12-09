# Game designed and created by Marco Wolf
# Art from <a href="https://www.textstudio.com/">Font generator</a>

from tkinter import *
from tkinter import ttk
import json
from tkinter.messagebox import askyesno

window = Tk()
window.title("4-Gewinnt")
window.geometry('660x700')
window.config(bg="yellow")
logo = PhotoImage(file='4-Gewinnt-art.png')
logo_big = logo.zoom(2)
logo_small = logo_big.subsample(3)
logo_highscore = PhotoImage(file='highscore-art.png')
logo_highscore_big = logo_highscore.zoom(2)
logo_highscore_small = logo_highscore_big.subsample(3)
player_color = ["yellow", "red"]
play_board = [[0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0]]


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


# Fenster bei Spielstart anzeigen zur Namneseingabe der Spieler
neues_fenster = Toplevel(window,bg="blue")
neues_fenster.geometry("600x200")
neues_fenster.title("Eingabe der Spielernamen.")

with open('game_data.json', 'r') as file:
    game_data = json.load(file)

leeresfeld = Label(neues_fenster,bg="blue",pady=10).grid(row=0,column=0)
spielereingabe_1 = (Label(neues_fenster, text="Spieler 1: ",font=("Ink Free",20,"bold"),bg="red",width=15,pady=10)
                    .grid(row=1,column=0))
player_1_button = (Button(neues_fenster,text="Submit",font=("Ink Free",20,"bold"),fg="red", bg="black",
                        cursor="hand2", command=get_player_1_name)
                 .grid(row=1,column=2))
player1 = StringVar()
textfeld1 = Entry(neues_fenster,font=("Ink Free",20,"bold"),bg="red",width=15,textvariable=player1).grid(row=1,column=1)
spielereingabe_2 = (Label(neues_fenster, text="Spieler 2: ",font=("Ink Free",20,"bold"),bg="yellow",width=15,pady=10)
                    .grid(row=2,column=0))
player_2_button = (Button(neues_fenster,text="Submit",font=("Ink Free",20,"bold"),fg="yellow", bg="black",
                        cursor="hand2", command=get_player_2_name)
                 .grid(row=2,column=2))
player2 = StringVar()
textfeld2 = Entry(neues_fenster, font=("Ink Free",20,"bold"),bg="yellow",width=15,textvariable=player2).grid(row=2,column=1)

neues_fenster.attributes('-topmost', True)


# Mehrere tabs anzeigen
notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="Game")
notebook.add(tab2, text="Highscore")
notebook.pack(fill=BOTH)


# Spiellogo Anzeigen
Label(tab1, image=logo_small,bg="red").pack()

# Spielernamen anzeigen
def show_and_switch_player_names():
    with open('game_data.json', 'r') as file:
        game_data = json.load(file)
        player_name_1 = game_data["player_name_1"]
        Label(tab1, text=player_name_1).pack()


# Rahmen für das Spielfeld
frame = Frame(tab1,bg="blue",bd=5,relief=RIDGE)
# Buttons zum Legen der Steine anzeigen und Funktion zum wiedergeben der Spalte
def click(num,frame):
    column = num
    with open('column_input.json', 'w') as f:
        json.dump(column, f)
    refresh_board(frame)
    return column

def refresh_board(frame):
    with open('game_data.json', 'r') as f:
        data = json.load(f)
        json_play_board = data['play_board']
        JSON_STONE_1 = data['STONE_1']
        JSON_STONE_2 = data['STONE_2']
        STONE_1_COLOR = "yellow"
        STONE_2_COLOR = "red"
        for row in range(6):
            for column in range(7):
                current_stone = json_play_board[row][column]
                if current_stone == JSON_STONE_1:
                    Button(frame, text="", width=7, height=3, bd=3, relief=SUNKEN, bg=STONE_1_COLOR
                           ).grid(row=row,column=column)
                elif current_stone == JSON_STONE_2:
                    Button(frame, text="", width=7, height=3, bd=3, relief=SUNKEN, bg=STONE_2_COLOR
                           ).grid(row=row, column=column)



column_buttons = Label(tab1)
column_1_button = Button(column_buttons, text=1, font=("Consolas",21),bg="darkblue",fg="yellow",
       width=3,relief=RAISED,bd=5, cursor="circle",
       command=lambda: click(1,frame)).pack(side=LEFT)
column_2_button = Button(column_buttons, text=2, font=("Consolas",21),bg="darkblue",fg="yellow",width=3,
       relief=RAISED,bd=5, cursor="circle",
       command=lambda: click(2,frame)).pack(side=LEFT)
column_3_button = Button(column_buttons, text=3, font=("Consolas",21),bg="darkblue",fg="yellow",width=3,
       relief=RAISED,bd=5, cursor="circle",
       command=lambda: click(3,frame)).pack(side=LEFT)
column_4_button = Button(column_buttons, text=4, font=("Consolas",21),bg="darkblue",fg="yellow",width=3,
       relief=RAISED,bd=5, cursor="circle",
       command=lambda: click(4,frame)).pack(side=LEFT)
column_5_button = Button(column_buttons, text=5, font=("Consolas",21),bg="darkblue",fg="yellow",width=3,
       relief=RAISED,bd=5, cursor="circle",
       command=lambda: click(5,frame)).pack(side=LEFT)
column_6_button = Button(column_buttons, text=6, font=("Consolas",21),bg="darkblue",fg="yellow",width=3,
       relief=RAISED,bd=5, cursor="circle",
       command=lambda: click(6,frame)).pack(side=LEFT)
column_7_button = Button(column_buttons, text=7, font=("Consolas",21),bg="darkblue",fg="yellow",width=3,
       relief=RAISED,bd=5, cursor="circle",
       command=lambda: click(7,frame)).pack(side=LEFT)
column_buttons.pack()


# Spielfeld
for row in range(6):
    for column in range(7):
        play_board[row][column] = Button(frame, text="", width=7, height=3, bd=3, relief=SUNKEN, bg="blue")
        play_board[row][column].grid(row=row, column=column)
frame.pack()

# Highscore
highscore_label = Label(tab2, image=logo_highscore_small, bg="red")
highscore_label.pack()

with open('highscore.json', 'r') as file:
    highscore = json.load(file)


frame2 = Frame(tab2, bg="blue",bd=5,relief=RIDGE,width=500,height=50)
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
    Label(frame2, text=highscore[persons].get("wins"),font=("Consolas",12),
          width=20,bg="blue",fg="yellow").grid(row=row,column=1)
    row +=1

frame2.pack()


# switch between tabs with the buttons and exit button
def highscoretab():
    notebook.select(tab2)

def gametab():
    notebook.select(tab1)

def really_quit():
    if askyesno("Quit", "Do you really want to quit?"):
        window.destroy()

# Buttons on the bottom
button_game = Button(window, text="Game", font=("Ink Free",20,"bold"),fg="blue", bg="black",
                     padx=20, bd=5, relief=RIDGE, cursor="hand2", command=gametab)
button_game.place(x=110, y=630)

button_highscore = Button(window, text="Highscore", font=("Ink Free",20,"bold"),fg="blue", bg="black",
                          padx=5, bd=5, relief=RIDGE, cursor="hand2", command=highscoretab)
button_highscore.place(x=251, y=630)

button_quit = Button(window, text="Quit", font=("Ink Free",20,"bold"), fg="red", bg="black",
                     padx=26, bd=5, relief=RIDGE, cursor="hand2", command=really_quit)
button_quit.place(x=412, y=630)

window.mainloop()
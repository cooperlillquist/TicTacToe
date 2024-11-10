import tkinter # GUI library

def set_tile(row, column):
    global curr_player

    if (gameover):
        return

    if board[row][column]["text"] !="":
        # Already taken spot
        return

    board[row][column]["text"] = curr_player #mark the board

    if curr_player == playerO:
        curr_player = playerX
    else: 
        curr_player = playerO

    label["text"] = curr_player+"'s turn"

    # check winner
    check_winner()

def check_winner():
    global turns, gameover
    turns += 1

    # Check horizontally
    for row in range(3):
        if (board[row][0]["text"]== board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+ " is the winner!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_grey)
            gameover = True
            return
        
    # Check Vertically
    for column in range(3):
        if(board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
           and board[0][column]["text"] != ""): 
            label.config(text=board[0][column]["text"]+ " is the winner!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_grey)
            gameover = True
            return
        
    # Check Diagonally
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"]+ " is the winner!", foreground=color_yellow)  
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_light_grey)
        gameover = True
        return
    
    # Anti Diagonal
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"]+ " is the winner!", foreground=color_yellow)
        board[0][2].config(foreground=color_yellow, background=color_light_grey)
        board[1][1].config(foreground=color_yellow, background=color_light_grey)
        board[2][0].config(foreground=color_yellow, background=color_light_grey)
        gameover = True
        return
    
    # Tie
    if (turns == 9):
        gameover = True
        label.config(text="Tie!", foreground=color_yellow)




def new_game():
    global turns, gameover

    turns = 0
    gameover = False

    label.config(text=curr_player+"'s turn", foreground="white") 

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_grey)


# game setup
playerX = "X"
playerO = "O"
curr_player = playerX

board = [[0,0,0], 
         [0,0,0], 
         [0,0,0]]

color_blue = '#4584B6'
color_yellow = '#ffde57'
color_grey = '#343434'
color_light_grey = '#646464'

turns = 0
gameover = False

# window setup
window =tkinter.Tk()
window.title("Tic Tac Tow")
window.resizable(False, False)


frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player+"'s turn", font=("Consolas", 20), background=color_grey,
                      foreground="white")

label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"), 
                                            background=color_grey, foreground=color_blue, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="Restart", font=("Consolas", 20), background=color_grey,
               foreground="white", command=new_game)

button.grid(row=4, column=0, columnspan=3, sticky="we")
frame.pack()

# center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()



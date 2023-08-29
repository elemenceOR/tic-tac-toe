import tkinter as tk
from tkinter import messagebox

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def handle_click(row, col):
    global current_player

    if board[row][col] == " ":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        if check_winner(board, current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins 😀!")
            reset_board()
        elif is_board_full(board):
            messagebox.showinfo("Game Over", "It's a tie🤝!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
    else:
        messagebox.showerror("Invalid Move", "That spot is already taken. Try again😥.")

def reset_board():
    global board, current_player

    for i in range(3):
        for j in range(3):
            board[i][j] = " "
            buttons[i][j].config(text=" ")
    
    current_player = "X"

# the board
root = tk.Tk()
root.title("Tic-Tac-Toe v1.0")
root.eval('tk::PlaceWindow . center')


board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"


buttons = []
for i in range(3):
    row_buttons = []
    for j in range(3):
        button = tk.Button(root, text=" ", font=("Poppins", 20), height=2, width=5, command=lambda row=i, col=j: handle_click(row, col), activebackground="lightblue")
        button.grid(row=i, column=j, padx=2, pady=2)
        row_buttons.append(button)
    buttons.append(row_buttons)


root.mainloop()

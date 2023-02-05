import tkinter as tk


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")

        self.buttons = []
        for i in range(9):
            button = tk.Button(master, text=" ", font=("Courier", 20), height=2, width=4,
                               command=lambda x=i: self.mark_square(x))
            button.grid(row=i//3, column=i % 3)
            self.buttons.append(button)

        self.player = "X"
        self.winner = None

    def mark_square(self, idx):
        button = self.buttons[idx]
        if button["text"] == " " and self.winner is None:
            button.config(text=self.player)
            self.check_for_winner()
            self.change_player()

    def change_player(self):
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"

    def check_for_winner(self):
        for i in [0, 3, 6]:
            if self.buttons[i]["text"] == self.buttons[i+1]["text"] == self.buttons[i+2]["text"] != " ":
                self.winner = self.buttons[i]["text"]
                break
        for i in [0, 1, 2]:
            if self.buttons[i]["text"] == self.buttons[i+3]["text"] == self.buttons[i+6]["text"] != " ":
                self.winner = self.buttons[i]["text"]
                break
        if self.buttons[0]["text"] == self.buttons[4]["text"] == self.buttons[8]["text"] != " ":
            self.winner = self.buttons[0]["text"]
        if self.buttons[2]["text"] == self.buttons[4]["text"] == self.buttons[6]["text"] != " ":
            self.winner = self.buttons[2]["text"]

        if self.winner is not None:
            for button in self.buttons:
                button.config(state="disabled")
            self.master.title(f"{self.winner} won the game!")


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()

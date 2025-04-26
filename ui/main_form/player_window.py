import tkinter as tk
from ui.add_form.add_player_window import AddPlayerWindow
from ui.show_form.show_player_window import ShowPlayerWindow

class PlayerWindow:
    def __init__(self, parent, player_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Управление игроками")
        self.window.geometry("400x200")
        self.player_model = player_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Управление игроками", font=("Arial", 14)).pack(pady=20)

        tk.Button(self.window, text="Добавить нового игрока", width=30, command=self.add_player).pack(pady=5)
        tk.Button(self.window, text="Показать всех игроков", width=30, command=self.show_players).pack(pady=5)

    def add_player(self):
        AddPlayerWindow(self.window, self.player_model)

    def show_players(self):
        ShowPlayerWindow(self.window, self.player_model)

import tkinter as tk
from ui.add_form.add_match_window import AddMatchWindow
from ui.show_form.show_match_window import ShowMatchWindow

class MatchWindow:
    def __init__(self, parent, match_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Управление матчами")
        self.window.geometry("400x200")
        self.match_model = match_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Управление матчами", font=("Arial", 14)).pack(pady=20)

        tk.Button(self.window, text="Добавить новый матч", width=30, command=self.add_match).pack(pady=5)
        tk.Button(self.window, text="Показать все матчи", width=30, command=self.show_matches).pack(pady=5)

    def add_match(self):
        AddMatchWindow(self.window, self.match_model)

    def show_matches(self):
        ShowMatchWindow(self.window, self.match_model)

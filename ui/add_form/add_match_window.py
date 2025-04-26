import tkinter as tk
from tkinter import messagebox

class AddMatchWindow:
    def __init__(self, parent, match_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Добавить матч")
        self.match_model = match_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Введите информацию о матче", font=("Arial", 14)).pack(pady=20)

        tk.Label(self.window, text="Дата").pack()
        self.date_entry = tk.Entry(self.window)
        self.date_entry.pack(pady=5)

        tk.Label(self.window, text="Место").pack()
        self.location_entry = tk.Entry(self.window)
        self.location_entry.pack(pady=5)

        tk.Label(self.window, text="Соперник").pack()
        self.opponent_entry = tk.Entry(self.window)
        self.opponent_entry.pack(pady=5)

        tk.Label(self.window, text="Счет").pack()
        self.score_entry = tk.Entry(self.window)
        self.score_entry.pack(pady=5)

        tk.Button(self.window, text="Добавить матч", width=30, command=self.add_match).pack(pady=10)

    def add_match(self):
        date = self.date_entry.get()
        location = self.location_entry.get()
        opponent = self.opponent_entry.get()
        score = self.score_entry.get()

        if not date or not location or not opponent or not score:
            messagebox.showerror("Ошибка", "Все поля обязательны для заполнения!")
            return

        self.match_model.create(date, location, opponent, score)
        messagebox.showinfo("Успех", "Матч добавлен успешно!")
        self.window.destroy()

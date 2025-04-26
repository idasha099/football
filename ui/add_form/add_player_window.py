import re
import tkinter as tk
from tkinter import messagebox

class AddPlayerWindow:
    def __init__(self, parent, player_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Добавить игрока")
        self.player_model = player_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Введите информацию об игроке", font=("Arial", 14)).pack(pady=20)

        tk.Label(self.window, text="Имя").pack()
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack(pady=5)

        tk.Label(self.window, text="Позиция").pack()
        self.position_entry = tk.Entry(self.window)
        self.position_entry.pack(pady=5)

        tk.Label(self.window, text="Возраст").pack()
        self.age_entry = tk.Entry(self.window)
        self.age_entry.pack(pady=5)

        tk.Label(self.window, text="Зарплата").pack()
        self.salary_entry = tk.Entry(self.window)
        self.salary_entry.pack(pady=5)

        tk.Button(self.window, text="Добавить игрока", width=30, command=self.add_player).pack(pady=10)

    def add_player(self):
        name = self.name_entry.get()
        position = self.position_entry.get()
        age = self.age_entry.get()
        salary = self.salary_entry.get()

        if not name or not position or not age or not salary:
            messagebox.showerror("Ошибка", "Все поля обязательны для заполнения!")
            return

        if not name.isalpha():
            messagebox.showerror("Ошибка", "Имя должно содержать только буквы!")
            return

        if not position.isalpha():
            messagebox.showerror("Ошибка", "Позиция должна содержать только буквы!")
            return

        if not age.isdigit() or int(age) < 16:
            messagebox.showerror("Ошибка", "Возраст должен быть числом и не менее 16!")
            return

        if not salary.isdigit() or int(salary) <= 0:
            messagebox.showerror("Ошибка", "Зарплата должна быть положительным числом!")
            return

        self.player_model.create(name, position, int(age), float(salary))
        messagebox.showinfo("Успех", "Игрок добавлен успешно!")
        self.window.destroy()

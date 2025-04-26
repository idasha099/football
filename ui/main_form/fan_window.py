import tkinter as tk
from ui.add_form.add_fan_window import AddFanWindow
from ui.show_form.show_fan_window import ShowFanWindow

class FanWindow:
    def __init__(self, parent, fan_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Управление болельщиками")
        self.window.geometry("400x200")
        self.fan_model = fan_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Управление болельщиками", font=("Arial", 14)).pack(pady=20)

        tk.Button(self.window, text="Добавить нового болельщика", width=30, command=self.add_fan).pack(pady=5)
        tk.Button(self.window, text="Показать всех болельщиков", width=30, command=self.show_fans).pack(pady=5)

    def add_fan(self):
        AddFanWindow(self.window, self.fan_model)

    def show_fans(self):
        ShowFanWindow(self.window, self.fan_model)

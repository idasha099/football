import tkinter as tk
from ui.add_form.add_coach_window import AddCoachWindow
from ui.show_form.show_coach_window import ShowCoachWindow

class CoachWindow:
    def __init__(self, parent, coach_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Управление тренерами")
        self.window.geometry("400x200")
        self.coach_model = coach_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Управление тренерами", font=("Arial", 14)).pack(pady=20)

        tk.Button(self.window, text="Добавить нового тренера", width=30, command=self.add_coach).pack(pady=5)
        tk.Button(self.window, text="Показать всех тренеров", width=30, command=self.show_coaches).pack(pady=5)

    def add_coach(self):
        AddCoachWindow(self.window, self.coach_model)

    def show_coaches(self):
        ShowCoachWindow(self.window, self.coach_model)

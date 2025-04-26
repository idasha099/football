import tkinter as tk
from tkinter import messagebox

class AddCoachWindow:
    def __init__(self, parent, coach_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Добавить тренера")
        self.coach_model = coach_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Введите информацию о тренере", font=("Arial", 14)).pack(pady=20)

        tk.Label(self.window, text="Имя").pack()
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack(pady=5)

        tk.Label(self.window, text="Специализация").pack()
        self.specialization_entry = tk.Entry(self.window)
        self.specialization_entry.pack(pady=5)

        tk.Label(self.window, text="Возраст").pack()
        self.age_entry = tk.Entry(self.window)
        self.age_entry.pack(pady=5)

        tk.Label(self.window, text="Зарплата").pack()
        self.salary_entry = tk.Entry(self.window)
        self.salary_entry.pack(pady=5)

        tk.Button(self.window, text="Добавить тренера", width=30, command=self.add_coach).pack(pady=10)

    def add_coach(self):
        name = self.name_entry.get()
        specialization = self.specialization_entry.get()
        age = self.age_entry.get()
        salary = self.salary_entry.get()

        if not name or not specialization or not age or not salary:
            messagebox.showerror("Ошибка", "Все поля обязательны для заполнения!")
            return

        if not name.isalpha():
            messagebox.showerror("Ошибка", "Имя должно содержать только буквы!")
            return

        if not specialization.isalpha():
            messagebox.showerror("Ошибка", "Специализация должна содержать только буквы!")
            return

        if not age.isdigit() or int(age) < 18:
            messagebox.showerror("Ошибка", "Возраст должен быть числом и не менее 18!")
            return

        if not salary.isdigit() or int(salary) <= 0:
            messagebox.showerror("Ошибка", "Зарплата должна быть положительным числом!")
            return

        self.coach_model.create(name, specialization, int(age), float(salary))
        messagebox.showinfo("Успех", "Тренер добавлен успешно!")
        self.window.destroy()

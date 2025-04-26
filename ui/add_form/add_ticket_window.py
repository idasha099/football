import tkinter as tk
from tkinter import messagebox

class AddTicketWindow:
    def __init__(self, parent, ticket_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Добавить билет")
        self.ticket_model = ticket_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Введите информацию о билете", font=("Arial", 14)).pack(pady=20)

        # Поле для выбора фаната
        tk.Label(self.window, text="Выберите фаната (ID)").pack()
        self.fan_id_entry = tk.Entry(self.window)
        self.fan_id_entry.pack(pady=5)

        # Поле для выбора матча
        tk.Label(self.window, text="Выберите матч (ID)").pack()
        self.match_id_entry = tk.Entry(self.window)
        self.match_id_entry.pack(pady=5)

        # Поле для ввода даты покупки билета
        tk.Label(self.window, text="Дата покупки билета (например, 2025-01-10)").pack()
        self.purchase_date_entry = tk.Entry(self.window)
        self.purchase_date_entry.pack(pady=5)

        # Кнопка для добавления билета
        tk.Button(self.window, text="Добавить билет", width=30, command=self.add_ticket).pack(pady=10)

    def add_ticket(self):
        # Получаем данные из полей
        fan_id = self.fan_id_entry.get()
        match_id = self.match_id_entry.get()
        purchase_date = self.purchase_date_entry.get()

        # Проверка на пустые поля
        if not fan_id or not match_id or not purchase_date:
            messagebox.showerror("Ошибка", "Все поля обязательны для заполнения!")
            return

        try:
            fan_id = int(fan_id)
            match_id = int(match_id)
        except ValueError:
            messagebox.showerror("Ошибка", "ID фаната и ID матча должны быть целыми числами!")
            return

        # Добавление билета без проверки на существование фаната и матча
        self.ticket_model.create(fan_id, match_id, purchase_date)
        messagebox.showinfo("Успех", "Билет добавлен успешно!")
        self.window.destroy()

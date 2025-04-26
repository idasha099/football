import tkinter as tk
from tkinter import messagebox, ttk

class AddFanWindow:
    def __init__(self, parent, fan_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Добавить фаната")
        self.fan_model = fan_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Введите информацию о фанате", font=("Arial", 14)).pack(pady=20)

        tk.Label(self.window, text="Имя фаната").pack()
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack(pady=5)

        tk.Label(self.window, text="Контактная информация (например, телефон)").pack()
        self.contact_entry = tk.Entry(self.window)
        self.contact_entry.pack(pady=5)

        tk.Label(self.window, text="Тип билета").pack()
        self.ticket_type_entry = tk.Frame(self.window)
        self.ticket_type_entry = ttk.Combobox(self.window, values=["Стандартный", "VIP"], state="readonly")
        self.ticket_type_entry.pack(pady=5)
        self.ticket_type_entry.set("Стандартный")


        tk.Button(self.window, text="Добавить фаната", width=30, command=self.add_fan).pack(pady=10)

    def add_fan(self):
        name = self.name_entry.get()
        contact_info = self.contact_entry.get()
        ticket_type = self.ticket_type_entry.get()

        if not name or not contact_info or not ticket_type:
            messagebox.showerror("Ошибка", "Все поля обязательны для заполнения!")
            return

        self.fan_model.create(name, contact_info, ticket_type)
        messagebox.showinfo("Успех", "Фанат добавлен успешно!")
        self.window.destroy()

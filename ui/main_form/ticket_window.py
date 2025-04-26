import tkinter as tk
from ui.add_form.add_ticket_window import AddTicketWindow
from ui.show_form.show_ticket_window import ShowTicketWindow

class TicketWindow:
    def __init__(self, parent, ticket_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Управление билетами")
        self.window.geometry("400x200")
        self.ticket_model = ticket_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Управление билетами", font=("Arial", 14)).pack(pady=20)

        tk.Button(self.window, text="Добавить новый билет", width=30, command=self.add_ticket).pack(pady=5)
        tk.Button(self.window, text="Показать все билеты", width=30, command=self.show_tickets).pack(pady=5)

    def add_ticket(self):
        AddTicketWindow(self.window, self.ticket_model)

    def show_tickets(self):
        ShowTicketWindow(self.window, self.ticket_model)

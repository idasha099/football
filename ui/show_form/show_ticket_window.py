import tkinter as tk
from tkinter import ttk

class ShowTicketWindow:
    def __init__(self, parent, ticket_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Список билетов")
        self.ticket_model = ticket_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Список билетов", font=("Arial", 14)).pack(pady=10)

        self.column_choices = {
            "ID": tk.BooleanVar(value=True),
            "ID болельщика": tk.BooleanVar(value=True),
            "ID матча": tk.BooleanVar(value=True),
            "Дата покупки": tk.BooleanVar(value=True),
        }

        tk.Label(self.window, text="Выберите отображаемые колонки:").pack(pady=5)

        columns_frame = tk.Frame(self.window)
        columns_frame.pack(pady=5)

        for col, var in self.column_choices.items():
            tk.Checkbutton(columns_frame, text=col, variable=var, command=self.update_columns).pack(side=tk.LEFT, padx=5)

        self.tree = ttk.Treeview(self.window, show="headings", height=10)
        self.tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(self.window, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        filter_frame = tk.Frame(self.window)
        filter_frame.pack(pady=5)

        tk.Label(filter_frame, text="Поиск по ID болельщика или ID матча:").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(filter_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)

        self.search_button = tk.Button(filter_frame, text="Поиск", command=self.search_tickets)
        self.search_button.pack(side=tk.LEFT, padx=5)

        self.sort_date_button = tk.Button(filter_frame, text="Сортировать по дате покупки", command=lambda: self.sort_tickets("purchase_date"))
        self.sort_date_button.pack(side=tk.LEFT, padx=5)

        self.load_data()

    def load_data(self, filter_text=None, tickets=None):
        if not tickets:
            tickets = self.ticket_model.get_all()

        if filter_text:
            tickets = [ticket for ticket in tickets if filter_text.lower() in str(ticket[1]).lower() or filter_text.lower() in str(ticket[2]).lower()]

        for row in self.tree.get_children():
            self.tree.delete(row)

        selected_columns = [col for col, var in self.column_choices.items() if var.get()]

        self.tree["columns"] = selected_columns
        for col in selected_columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        for ticket in tickets:
            values = []
            if "ID" in selected_columns:
                values.append(ticket[0])
            if "ID болельщика" in selected_columns:
                values.append(ticket[1])
            if "ID матча" in selected_columns:
                values.append(ticket[2])
            if "Дата покупки" in selected_columns:
                values.append(ticket[3])

            self.tree.insert("", "end", values=values)

    def search_tickets(self):
        search_text = self.search_entry.get()
        self.load_data(search_text)

    def sort_tickets(self, column):
        tickets = self.ticket_model.get_all()

        if column == "purchase_date":
            tickets.sort(key=lambda ticket: ticket[3])

        self.load_data(tickets=tickets)

    def update_columns(self):
        self.load_data()

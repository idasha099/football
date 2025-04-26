import tkinter as tk
from tkinter import ttk

class ShowMatchWindow:
    def __init__(self, parent, match_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Список матчей")
        self.match_model = match_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Список матчей", font=("Arial", 14)).pack(pady=10)

        self.column_choices = {
            "ID": tk.BooleanVar(value=True),
            "Дата": tk.BooleanVar(value=True),
            "Время": tk.BooleanVar(value=True),
            "Место": tk.BooleanVar(value=True),
            "Соперник": tk.BooleanVar(value=True),
            "Счет": tk.BooleanVar(value=True),
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

        tk.Label(filter_frame, text="Поиск по сопернику или месту:").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(filter_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)

        self.search_button = tk.Button(filter_frame, text="Поиск", command=self.search_matches)
        self.search_button.pack(side=tk.LEFT, padx=5)

        self.sort_date_button = tk.Button(filter_frame, text="Сортировать по дате", command=lambda: self.sort_matches("date"))
        self.sort_date_button.pack(side=tk.LEFT, padx=5)

        self.load_data()

    def load_data(self, filter_text=None, matches=None):
        if not matches:
            matches = self.match_model.get_all()

        if filter_text:
            matches = [match for match in matches if filter_text.lower() in match[4].lower() or filter_text.lower() in match[3].lower()]

        for row in self.tree.get_children():
            self.tree.delete(row)

        selected_columns = [col for col, var in self.column_choices.items() if var.get()]

        self.tree["columns"] = selected_columns
        for col in selected_columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        for match in matches:
            values = []
            if "ID" in selected_columns:
                values.append(match[0])
            if "Дата" in selected_columns:
                values.append(match[1])
            if "Время" in selected_columns:
                values.append(match[2])
            if "Место" in selected_columns:
                values.append(match[3])
            if "Соперник" in selected_columns:
                values.append(match[4])
            if "Счет" in selected_columns:
                values.append(match[5])

            self.tree.insert("", "end", values=values)

    def search_matches(self):
        search_text = self.search_entry.get()
        self.load_data(search_text)

    def sort_matches(self, column):
        matches = self.match_model.get_all()

        if column == "date":
            matches.sort(key=lambda match: match[1])

        self.load_data(matches=matches)

    def update_columns(self):
        self.load_data()

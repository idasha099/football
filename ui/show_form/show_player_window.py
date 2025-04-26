import tkinter as tk
from tkinter import ttk, messagebox

class ShowPlayerWindow:
    def __init__(self, parent, player_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Список игроков")
        self.player_model = player_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Список игроков", font=("Arial", 14)).pack(pady=10)

        self.column_choices = {
            "ID": tk.BooleanVar(value=True),
            "Имя": tk.BooleanVar(value=True),
            "Дата рождения": tk.BooleanVar(value=True),
            "Позиция": tk.BooleanVar(value=True),
            "Зарплата": tk.BooleanVar(value=True),
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

        tk.Label(filter_frame, text="Поиск по имени или позиции:").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(filter_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)

        self.search_button = tk.Button(filter_frame, text="Поиск", command=self.search_players)
        self.search_button.pack(side=tk.LEFT, padx=5)

        self.sort_name_button = tk.Button(filter_frame, text="Сортировать по имени", command=lambda: self.sort_players("name"))
        self.sort_name_button.pack(side=tk.LEFT, padx=5)

        # Кнопка для подсчета общей зарплаты
        self.salary_button = tk.Button(self.window, text="Подсчитать общую зарплату", command=self.calculate_total_salary)
        self.salary_button.pack(pady=10)

        self.load_data()

    def load_data(self, filter_text=None, players=None):
        if not players:
            players = self.player_model.get_all()

        if filter_text:
            players = [player for player in players if filter_text.lower() in player[1].lower() or filter_text.lower() in player[3].lower()]

        for row in self.tree.get_children():
            self.tree.delete(row)

        selected_columns = [col for col, var in self.column_choices.items() if var.get()]

        self.tree["columns"] = selected_columns
        for col in selected_columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        for player in players:
            values = []
            if "ID" in selected_columns:
                values.append(player[0])
            if "Имя" in selected_columns:
                values.append(player[1])
            if "Дата рождения" in selected_columns:
                values.append(player[2])
            if "Позиция" in selected_columns:
                values.append(player[3])
            if "Зарплата" in selected_columns:
                values.append(player[4])

            self.tree.insert("", "end", values=values)

    def search_players(self):
        search_text = self.search_entry.get()
        self.load_data(search_text)

    def sort_players(self, column):
        players = self.player_model.get_all()

        if column == "name":
            players.sort(key=lambda player: player[1].lower())

        self.load_data(players=players)

    def update_columns(self):
        self.load_data()

    def calculate_total_salary(self):
        total_salary = self.player_model.get_total_salary()
        messagebox.showinfo("Общая зарплата", f"Общая зарплата всех игроков: {total_salary} руб.")

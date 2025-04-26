import tkinter as tk
from tkinter import ttk

class ShowFanWindow:
    def __init__(self, parent, fan_model):
        self.window = tk.Toplevel(parent)
        self.window.title("Список болельщиков")
        self.fan_model = fan_model
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Список болельщиков", font=("Arial", 14)).pack(pady=10)

        self.column_choices = {
            "ID": tk.BooleanVar(value=True),
            "Имя": tk.BooleanVar(value=True),
            "Контактная информация": tk.BooleanVar(value=True),
            "Тип билета": tk.BooleanVar(value=True),
        }

        tk.Label(self.window, text="Выберите отображаемые колонки:").pack(pady=5)

        columns_frame = tk.Entry(self.window)
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

        tk.Label(filter_frame, text="Поиск по имени или типу билета:").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(filter_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)

        self.search_button = tk.Button(filter_frame, text="Поиск", command=self.search_fans)
        self.search_button.pack(side=tk.LEFT, padx=5)

        self.sort_name_button = tk.Button(filter_frame, text="Сортировать по имени", command=lambda: self.sort_fans("name"))
        self.sort_name_button.pack(side=tk.LEFT, padx=5)

        self.load_data()

    def load_data(self, filter_text=None, fans=None):
        if not fans:
            fans = self.fan_model.get_all()

        if filter_text:
            fans = [fan for fan in fans if filter_text.lower() in fan[1].lower() or filter_text.lower() in fan[3].lower()]

        for row in self.tree.get_children():
            self.tree.delete(row)

        selected_columns = [col for col, var in self.column_choices.items() if var.get()]

        self.tree["columns"] = selected_columns
        for col in selected_columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        for fan in fans:
            values = []
            if "ID" in selected_columns:
                values.append(fan[0])
            if "Имя" in selected_columns:
                values.append(fan[1])
            if "Контактная информация" in selected_columns:
                values.append(fan[2])
            if "Тип билета" in selected_columns:
                values.append(fan[3])

            self.tree.insert("", "end", values=values)

    def search_fans(self):
        search_text = self.search_entry.get()
        self.load_data(search_text)

    def sort_fans(self, column):
        fans = self.fan_model.get_all()

        if column == "name":
            fans.sort(key=lambda fan: fan[1].lower())

        self.load_data(fans=fans)

    def update_columns(self):
        self.load_data()

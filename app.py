import tkinter as tk

# Импортируем модели
from models.player import Player
from models.coach import Coach
from models.match import Match
from models.fan import Fan
from models.ticket import Ticket

# Импортируем интерфейс
from ui.main_form.player_window import PlayerWindow
from ui.main_form.coach_window import CoachWindow
from ui.main_form.match_window import MatchWindow
from ui.main_form.fan_window import FanWindow
from ui.main_form.ticket_window import TicketWindow


class FootballClubApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Управление футбольным клубом")
        self.root.geometry("400x300")

        self.player_model = Player()
        self.coach_model = Coach()
        self.match_model = Match()
        self.fan_model = Fan()
        self.ticket_model = Ticket()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Управление футбольным клубом", font=("Arial", 16)).pack(pady=20)

        tk.Button(self.root, text="Управление игроками", width=30, command=self.manage_players).pack(pady=5)
        tk.Button(self.root, text="Управление тренерами", width=30, command=self.manage_coaches).pack(pady=5)
        tk.Button(self.root, text="Управление матчами", width=30, command=self.manage_matches).pack(pady=5)
        tk.Button(self.root, text="Управление болельщиками", width=30, command=self.manage_fans).pack(pady=5)
        tk.Button(self.root, text="Управление билетами", width=30, command=self.manage_tickets).pack(pady=5)

    def manage_players(self):
        PlayerWindow(self.root, self.player_model)

    def manage_coaches(self):
        CoachWindow(self.root, self.coach_model)

    def manage_matches(self):
        MatchWindow(self.root, self.match_model)

    def manage_fans(self):
        FanWindow(self.root, self.fan_model)

    def manage_tickets(self):
        TicketWindow(self.root, self.ticket_model)


def run_app():
    root = tk.Tk()
    FootballClubApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_app()

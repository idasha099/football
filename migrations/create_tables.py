from db import connect_db


def create_tables():
    """Создает все таблицы в базе данных."""
    conn = connect_db()
    cursor = conn.cursor()

    # Создание таблицы игроков
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id_player INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birth_date TEXT NOT NULL,
            position TEXT NOT NULL,
            salary REAL NOT NULL
        )
    ''')

    # Создание таблицы тренеров
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS coaches (
            id_coach INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            specialization TEXT NOT NULL,
            experience INTEGER NOT NULL,
            salary REAL NOT NULL
        )
    ''')

    # Создание таблицы матчей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS matches (
            id_match INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            location TEXT NOT NULL,
            opponent TEXT NOT NULL,
            score TEXT
        )
    ''')

    # Создание таблицы составов матчей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS match_squads (
            id_squad INTEGER PRIMARY KEY AUTOINCREMENT,
            id_match INTEGER NOT NULL,
            id_player INTEGER NOT NULL,
            FOREIGN KEY (id_match) REFERENCES matches (id_match),
            FOREIGN KEY (id_player) REFERENCES players (id_player)
        )
    ''')

    # Создание таблицы болельщиков
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fans (
            id_fan INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact_info TEXT,
            ticket_type TEXT NOT NULL
        )
    ''')

    # Создание таблицы билетов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id_ticket INTEGER PRIMARY KEY AUTOINCREMENT,
            id_fan INTEGER NOT NULL,
            id_match INTEGER NOT NULL,
            purchase_date TEXT NOT NULL,
            FOREIGN KEY (id_fan) REFERENCES fans (id_fan),
            FOREIGN KEY (id_match) REFERENCES matches (id_match)
        )
    ''')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()

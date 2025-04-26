from db import connect_db

class Player:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor()

    def create(self, name, birth_date, position, salary):
        self.cursor.execute('''
            INSERT INTO players (name, birth_date, position, salary)
            VALUES (?, ?, ?, ?)
        ''', (name, birth_date, position, salary))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute('SELECT * FROM players')
        return self.cursor.fetchall()

    def get_total_salary(self):
        self.cursor.execute("SELECT SUM(salary) FROM players")
        result = self.cursor.fetchone()
        return result[0] if result[0] else 0

    def __del__(self):
        self.conn.close()

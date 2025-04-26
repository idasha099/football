from db import connect_db

class Match:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor()

    def create(self, date, time, location, opponent, score=None):
        self.cursor.execute('''
            INSERT INTO matches (date, location, opponent, score)
            VALUES (?, ?, ?, ?, ?)
        ''', (date, location, opponent, score))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute('SELECT * FROM matches')
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()

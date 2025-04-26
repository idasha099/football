from db import connect_db

class Ticket:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor()

    def create(self, id_fan, id_match, purchase_date):
        self.cursor.execute('''
            INSERT INTO tickets (id_fan, id_match, purchase_date)
            VALUES (?, ?, ?)
        ''', (id_fan, id_match, purchase_date))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute('SELECT * FROM tickets')
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()

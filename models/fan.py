from db import connect_db

class Fan:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor()

    def create(self, name, contact_info, ticket_type):
        self.cursor.execute('''
            INSERT INTO fans (name, contact_info, ticket_type)
            VALUES (?, ?, ?)
        ''', (name, contact_info, ticket_type))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute('SELECT * FROM fans')
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()

from db import connect_db

class Coach:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor()

    def create(self, name, specialization, experience, salary):
        self.cursor.execute('''
            INSERT INTO coaches (name, specialization, experience, salary)
            VALUES (?, ?, ?, ?)
        ''', (name, specialization, experience, salary))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute('SELECT * FROM coaches')
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()

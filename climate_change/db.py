import sqlite3

class DB:
    DB_NAME = 'forum.db'

    def __init__(self):
        self.init_db_done = False

    def create_user(self, email, salt, password_hash):
        conn = self.get_db_connection()
        conn.execute('INSERT INTO user (email, salt, password_hash) VALUES (?, ?, ?)',
                     (email, salt, password_hash))
        conn.commit()
        conn.close()

    def select_user(self, email):
        conn = self.get_db_connection()
        user = conn.execute('SELECT * FROM user WHERE email = ?', (email,)).fetchone()
        conn.close()
        return user

    def get_db_connection(self):
        if not self.init_db_done:
            self.init_db()
        
        conn = self.connect_to_db()
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_db(self):
        if not self.init_db_done:
            conn = self.connect_to_db()
            user_table = conn.execute("SELECT name FROM sqlite_master WHERE type = 'table' and name = 'user'").fetchone()
            if not user_table:
                self.create_table()
            self.init_db_done = True

    def create_table(self):
        conn = self.connect_to_db()
        with open('db/schema.sql') as f:
            conn.executescript(f.read())
            conn.commit()
            conn.close()

    def connect_to_db(self):
        try:
            conn = sqlite3.connect(DB.DB_NAME)
            return conn
        except sqlite3.Error:
            print(f'failed on connect to DB: {DB.DB_NAME}')

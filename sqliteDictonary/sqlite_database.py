import sqlite3
import os

class sqliteDictonary:
    def __init__(self, language):
        self.language = language
        db_folder = os.path.join(os.path.dirname(__file__), 'databases')        
        os.makedirs(db_folder, exist_ok=True)
        db_path = os.path.join(db_folder, f'{language}.db')
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS dictionary (
                            word TEXT, 
                            meaning TEXT,
                            example TEXT,
                            synonyms TEXT,
                            antonyms TEXT
                            )''')
        self.conn.commit()

    def add_word(self, word, meaning, example, synonyms, antonyms):
        self.cursor.execute('INSERT INTO dictionary VALUES (?, ?, ?, ?, ?)', (word, meaning, example, synonyms, antonyms))
        self.conn.commit()

    def add_batch_words(self, words):
        self.cursor.executemany('INSERT INTO dictionary VALUES (?, ?, ?, ?, ?)', words)
        self.conn.commit()

    def delete_word(self, word):
        self.cursor.execute('DELETE FROM dictionary WHERE word=?', (word,))
        self.conn.commit()

    def update_word(self, word, meaning, example, synonyms, antonyms):
        self.cursor.execute('UPDATE dictionary SET meaning=?, example=?, synonyms=?, antonyms=? WHERE word=?', (meaning, example, synonyms, antonyms, word))
        self.conn.commit()

    def update_batch_words(self, words):
        self.cursor.executemany('UPDATE dictionary SET meaning=?, example=?, synonyms=?, antonyms=? WHERE word=?', words)
        self.conn.commit()

    def get_word(self, word):
        self.cursor.execute('SELECT * FROM dictionary WHERE word=?', (word,))
        return self.cursor.fetchone()
    
    def set_version(self, version):
        self.cursor.execute('PRAGMA user_version = ?', (version,))
        self.conn.commit()

    def get_version(self):
        self.cursor.execute('PRAGMA user_version')
        return self.cursor.fetchone()[0]
    

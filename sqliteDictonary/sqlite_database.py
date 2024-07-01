import sqlite3
import os
import re

split_charachters = "{[(!,.:;?])]}"

class sqliteDictonary:
    def __init__(self, language, user_version=1):
        self.language = language
        db_folder = os.path.join(os.path.dirname(__file__), 'databases')        
        os.makedirs(db_folder, exist_ok=True)
        db_path = os.path.join(db_folder, f'{language}.db')
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS dictionary (
                            word TEXT, 
                            definition TEXT,
                            wordtype TEXT,
                            example TEXT,
                            synonyms TEXT,
                            antonyms TEXT,
                            UNIQUE(word, meaning)
                            )''')
        self.conn.commit()

    def add_word(self, word, definitions):
        for definition in definitions:
            wordtype = definition.get('wordtype', '')
            example = definition.get('example', '')
            synonyms = definition.get('synonyms', '')
            antonyms = definition.get('antonyms', '')

            try: 
                self.cursor.execute('INSERT INTO dictionary VALUES (?, ?, ?, ?, ?, ?)', 
                                (word, definition['definition'], wordtype, example, synonyms, antonyms))
            except sqlite3.IntegrityError: pass
        self.conn.commit()

    def delete_word(self, word):
        self.cursor.execute('DELETE FROM dictionary WHERE word=?', (word,))
        self.conn.commit()

    def update_word(self, word, definitions):
        for definition in definitions:
            wordtype = definition.get('wordtype', '')
            example = definition.get('example', '')
            synonyms = definition.get('synonyms', '')
            antonyms = definition.get('antonyms', '')

            try:
                self.cursor.execute('UPDATE dictionary SET definition=?, wordtype=?, example=?, synonyms=?, antonyms=? WHERE word=?', 
                                (definition['definition'], wordtype, example, synonyms, antonyms, word))
            except sqlite3.IntegrityError: pass
        self.conn.commit()

    def search_word(self, word):
        self.cursor.execute('SELECT * FROM dictionary WHERE word=?', (word,))
        return self.cursor.fetchall()
    
    def search_sentance(self, sentance):
        translated_sentance = []
        for section in sentance.split():
            for word in re.split(split_charachters, section):
                self.cursor.execute('SELECT * FROM dictionary WHERE word=?', (word,))
                translated_sentance.append(self.cursor.fetchall())
        return translated_sentance
    
    def set_version(self, version):
        self.cursor.execute('PRAGMA user_version = ?', (version,))
        self.conn.commit()

    def clear_duplicated_and_add_unique_constraint(self):
        self.cursor.execute('CREATE TABLE temp AS SELECT DISTINCT * FROM dictionary')
        self.cursor.execute('DROP TABLE dictionary')
        self.cursor.execute('ALTER TABLE temp RENAME TO dictionary')
        self.cursor.execute('CREATE UNIQUE INDEX idx_word_meaning ON dictionary (word, definition)')
        self.conn.commit()

    def get_version(self):
        self.cursor.execute('PRAGMA user_version')
        return self.cursor.fetchone()[0]
    
if __name__ == "__main__":
    db = sqliteDictonary("english")
    db.add_word("hello", [{'definition': 'used as a greeting or to begin a conversation', 'synonyms': 'hi', 'antonyms': 'goodbye'}])
    db.add_word("world", [{'definition': 'the earth, together with all of its countries and peoples', 'synonyms': 'earth', 'antonyms': 'universe'}])
    db.add_word("python", [{'definition': 'a high-level programming language', 'synonyms': 'programming language', 'antonyms': 'assembly language'}])
    print(db.search_word("hello"))
    print(db.search_word("world"))
    print(db.search_word("python"))
    print(db.get_version())
import os
import sqlite3
from typing import Optional

class ReviewsDB:
    DB_FOLDER = os.path.join(os.curdir, 'database')
    DB_NAME = 'reviews.db'
    TABLE_NAME = 'AmazonReviews'

    def __init__(self):
        self.connection: Optional[sqlite3.Connection] = None
        self.cursor: Optional[sqlite3.Cursor] = None

        if not os.path.isdir(self.DB_FOLDER):
            os.mkdir(self.DB_FOLDER)


    def connect(self) -> bool:
        try:
            self.connection = sqlite3.connect(os.path.join(self.DB_FOLDER, self.DB_NAME))
            self.cursor = self.connection.cursor()
            print('Successfully Connected to Database')
            self.__initialize_table()
            return True

        except sqlite3.Error as e:
            print(f'Error Connecting to Database - {e}')
            self.__close()
            return False


    def __initialize_table(self):
        try:
            self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
                ASIN PRIMARY KEY,
                scraped_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                reviews TEXT
            )
            ''')

            print('Initialized Table Successfully')
        except sqlite3.Error as e:
            print(f"Error Initializing Datable - {e}")
            self.__close()


    def __close(self):
        self.cursor.close()
        self.connection.close()

# debugging purpose only
if __name__ == '__main__':
    db = ReviewsDB()
    db.connect()
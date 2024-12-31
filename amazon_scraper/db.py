import os
import sqlite3
from typing import Optional

import json

class ReviewsDB:
    DB_FOLDER = os.path.join(os.curdir, 'database')
    DB_NAME = 'reviews.db'
    TABLE_NAME = 'AmazonReviews'

    def __init__(self) -> None:
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

    def __initialize_table(self) -> None:
        try:
            self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
                ASIN TEXT PRIMARY KEY,
                scraped_at DATETIME DEFAULT (strftime('%s', 'now')),
                reviews TEXT
            )
            ''')

            print('Initialized Table Successfully')
        except sqlite3.Error as e:
            print(f"Error Initializing Datable - {e}")
            self.__close()

    def insert_review(self, asin: str, reviews: list[str]) -> None:
        if self.connection and self.cursor:
            try:
                self.cursor.execute('''
                    INSERT INTO AmazonReviews (ASIN, reviews) VALUES (?, ?)
                ''', (asin, json.dumps(reviews)))

                self.connection.commit()

                print('Row inserted successfully')
            except sqlite3.Error as e:
                print(f'Error Inserting Review - {e}')
                self.__close()

        else:
            raise sqlite3.Error('Connect to the database first')

    def get_review(self, asin: str):
        if self.connection and self.cursor:
            try:
                result = self.cursor.execute('''
                    SELECT * FROM AmazonReviews WHERE ASIN = ?
                ''',
                (asin,),).fetchall()[0]

                return self.__prepare_review(result)
            except sqlite3.Error as e:
                print(f"Error in fetching row - {e}")
                # self.__close()

        else:
            raise sqlite3.Error('Connect to the database first')

    def check_asin(self, asin: str) -> bool:
        if self.connection and self.cursor:
            try:
                result = self.cursor.execute('''
                    SELECT EXISTS(SELECT 1 FROM AmazonReviews WHERE ASIN = ?)
                ''', (asin, ), ).fetchall()[0][0]

                return bool(result)
            except sqlite3.Error as e:
                print(f"Error in checking ASIN - {e}")

    @staticmethod
    def __prepare_review(result) -> dict[str: str]:
        asin, created_date, review_str = result

        reviews = json.loads(review_str)

        return {
            'ASIN': asin,
            'Scraped At': created_date,
            'Reviews': reviews
        }

    def __close(self) -> None:
        self.cursor.close()
        self.connection.close()

# debugging purpose only
if __name__ == '__main__':
    db = ReviewsDB()
    db.connect()
    asin = '1234abc'
    if db.check_asin(asin):
        results = db.get_review(asin)
        print(results)
    else:
        print('wrong asin')

import os
from typing import Optional

import pandas as pd

from utils import text_normalize, text_tokenize, text_lemmatize, remove_stopwords, create_embeddings

class DataLoader:
    FILE_NAME = 'fakeReviewData.csv'
    def __init__(self, file_name: Optional[str]=None) -> None:
        if file_name is not None:
            self.df: pd.DataFrame = pd.read_csv(file_name)

        else:
            self.df: pd.DataFrame = pd.read_csv(self.FILE_NAME)
            self.df['category'] = self.df['category'].map(lambda x: x.replace('_', ' ')[: -2])

    def remove_duplicates(self) -> None:
        if self.df.shape[0] > self.df.drop_duplicates().shape[0]:
            print('Dropping Duplicates!')
            self.df = self.df.drop_duplicates()

    def preprocess_data(self, preprocessing_steps: list[dict]):
        for step in preprocessing_steps:
            func = step['function']
            source_column = step['source_col']
            destination_column = step['destination_col']

            self.df[destination_column] = func(self.df[source_column])

    def preview_data(self, nrows: int = 5) -> None:
        print(self.df.sample(nrows))

    def save_processed_df(self, filename):
        self.df.to_json(filename, orient='records', lines=True)



# for debugging purpose only
if __name__ == '__main__':
    dl = DataLoader()
    dl.remove_duplicates()

    preprocessing_steps = [
        {'function': text_normalize, 'source_col': 'text_', 'destination_col': 'text_processed'},
        {'function': remove_stopwords, 'source_col': 'text_processed', 'destination_col': 'text_processed'},
        {'function': text_lemmatize, 'source_col': 'text_processed', 'destination_col': 'text_processed'},
        {'function': text_tokenize, 'source_col': 'text_processed', 'destination_col': 'text_tokenized'},
        {'function': create_embeddings, 'source_col': 'text_processed', 'destination_col': 'text_embeddings'}
    ]
    dl.preprocess_data(preprocessing_steps=preprocessing_steps)

    dl.save_processed_df('processed_data.json') # Using JSON here becasue CSV cannot handle nested lists which will be created when text is tokenized and embeddings will be created.
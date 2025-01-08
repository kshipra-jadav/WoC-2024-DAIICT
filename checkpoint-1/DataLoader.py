import os
from typing import Optional

import pandas as pd

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

    def preview_data(self, nrows: int = 5) -> None:
        print(self.df.sample(nrows))



# for debugging purpose only
if __name__ == '__main__':
    dl = DataLoader()
    dl.remove_duplicates()

    dl.preview_data(10)
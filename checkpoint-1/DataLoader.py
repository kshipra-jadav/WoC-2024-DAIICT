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


    def preview_data(self, nrows: int = 5) -> None:
        print(self.df.head(nrows))



# for debugging purpose only
if __name__ == '__main__':
    dl = DataLoader()

    dl.preview_data()
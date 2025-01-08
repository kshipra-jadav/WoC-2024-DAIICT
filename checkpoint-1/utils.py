import re
import time

import pandas as pd
from nltk.tokenize import ToktokTokenizer
from nltk.corpus import stopwords as stp
from nltk.stem import WordNetLemmatizer

def text_normalize(samples: pd.Series) -> pd.Series:
    samples = samples.apply(lambda x: x.lower()) # convert all samples to lower case

    samples = samples.apply(lambda x: re.sub(r'[^\w\s]', '', x)) # replace any character which is not string or space with blank

    return samples

def text_tokenize(samples: pd.Series) -> pd.Series:
    toktok = ToktokTokenizer() # Much better speed than word_tokenize
    samples = samples.apply(lambda x: toktok.tokenize(x))

    return samples

def remove_stopwords(samples: pd.Series) -> pd.Series:
    stopwords = set(stp.words('english'))

    samples = samples.apply(lambda x: [word for word in x if word not in stopwords])

    return samples

def text_lemmatize(samples: pd.Series) -> pd.Series:
    wnl = WordNetLemmatizer()

    samples = samples.apply(lambda x: [wnl.lemmatize(word) for word in x])

    return samples


def main():
    df = pd.read_csv('fakeReviewData.csv')

    df['text_'] = text_normalize(df['text_'])
    df['text_'] = text_tokenize(df['text_'])
    df['text_'] = remove_stopwords(df['text_'])

    start = time.perf_counter()
    df['text_'] = text_lemmatize(df['text_'])
    print(f"Took - {time.perf_counter() - start:.3f} secs")



if __name__ == '__main__':
    main()
import re
import time

import pandas as pd
from nltk.tokenize import ToktokTokenizer
from nltk.corpus import stopwords as stp
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer


def text_normalize(samples: pd.Series) -> pd.Series:
    samples = samples.apply(lambda x: x.lower()) # convert all samples to lower case

    samples = samples.apply(lambda x: re.sub(r'[^a-zA-Z\s]', '', x)) # replace any character which is not string or space with blank

    return samples

def text_tokenize(samples: pd.Series) -> pd.Series:
    toktok = ToktokTokenizer() # Much better speed than word_tokenize
    samples = samples.apply(lambda x: toktok.tokenize(x))

    return samples


def remove_stopwords(samples: pd.Series) -> pd.Series:
    stopwords = set(stp.words('english'))

    clean_samples = samples.apply(lambda x: ' '.join([word for word in x.split() if word not in stopwords]))

    return clean_samples

def text_lemmatize(samples: pd.Series) -> pd.Series:
    wnl = WordNetLemmatizer()

    samples = samples.apply(lambda x: wnl.lemmatize(x))

    return samples

def tfidf(samples: pd.Series) -> pd.Series:
    corpus = set()
    tfidf_vec = TfidfVectorizer()

    for sample in samples:
            for word in sample:
                corpus.add(word)
    tfidf_vec.fit(corpus)

    print(tfidf_vec.transform(samples[0]).toarray())

    # return tfidf_samples


def main():
    df = pd.read_csv('fakeReviewData.csv')

    df['text_'] = text_normalize(df['text_'])
    df['text_'] = remove_stopwords(df['text_'])
    df['text_'] = text_lemmatize(df['text_'])
    df['text_tokenized'] = text_tokenize(df['text_'])

    print(df['text_'].head(1))


if __name__ == '__main__':
    main()
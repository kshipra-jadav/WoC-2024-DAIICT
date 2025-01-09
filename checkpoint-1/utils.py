import re
import time

import pandas as pd
from nltk.tokenize import ToktokTokenizer
from nltk.corpus import stopwords as stp
from nltk.stem import WordNetLemmatizer
from sentence_transformers import SentenceTransformer

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

def create_embeddings(samples: pd.Series) -> pd.Series:
    model = SentenceTransformer('all-MiniLM-L6-v2')  # Had no choice. Sorry. TFIDF doesn't work on THIS big of a dataset.

    embeddings = model.encode(samples.tolist(), batch_size=32, show_progress_bar=True)

    return pd.Series(list(embeddings))



def main():
    df = pd.read_csv('fakeReviewData.csv')

    df['text_processed'] = text_normalize(df['text_'])
    df['text_processed'] = remove_stopwords(df['text_processed'])
    df['text_processed'] = text_lemmatize(df['text_processed'])
    df['text_tokenized'] = text_tokenize(df['text_processed'])

    df['text_embeddings'] = create_embeddings(df['text_processed'])

    print(df.head(2))


if __name__ == '__main__':
    main()
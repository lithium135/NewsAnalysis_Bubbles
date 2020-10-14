import pandas as pd
from pysentiment2.base import STATIC_PATH, BaseDict


class RN(BaseDict):
    """
    Dictionary class for
    Loughran and McDonald Financial Sentiment Dictionaries.
    
    See also https://www3.nd.edu/~mcdonald/Word_Lists.html
    
    The terms for the dictionary are stemmed by the default tokenizer.
    """

    def init_dict(self):
        renault_df = pd.read_csv("C://Users//jackl//OneDrive//Documents//Harvard//Research//Greenwood//l2_lexicon.csv", sep = ';')
        pos_ren = list(renault_df[renault_df['sentiment'] == 'positive']['keyword'])
        neg_ren = list(renault_df[renault_df['sentiment'] == 'negative']['keyword'])
        
        self._posset = pos_ren
        self._negset = neg_ren

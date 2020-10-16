import pandas as pd
from pysentiment2.base import STATIC_PATH, BaseDict


class RN(BaseDict):
    """
    Dictionary class for lexicon specified by Thomas Renault
    """

    def init_dict(self):
        PATH = "C://Users//jackl//OneDrive//Documents//Harvard//Research//Greenwood//l2_lexicon.csv"
        renault_df = pd.read_csv(PATH, sep = ';')
        pos_ren = list(renault_df[renault_df['sentiment'] == 'positive']['keyword'])
        neg_ren = list(renault_df[renault_df['sentiment'] == 'negative']['keyword'])
        
        self._posset = pos_ren
        self._negset = neg_ren

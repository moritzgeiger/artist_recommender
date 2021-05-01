# TABLES & VIS
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from ast import literal_eval
import numpy as np

# NLTK
import regex as re
import unicodedata

# ML
from sklearn.neighbors import KNeighborsRegressor
from joblib import dump, load

### not used. model is already trained.

top_50 = [
    'rock', 'pop', 'dance_pop', 'rap', 'hip_hop', 'pop_rap', 'pop_rock',
    'modern_rock', 'country_rock', 'urban_contemporary', 'folk_rock', 'latin',
    'soft_rock', 'trap', 'mellow_gold', 'funk', 'classic_rock',
    'adult_standards', 'pop_dance', 'indie_pop', 'alternative_rock',
    'southern_hip_hop', 'album_rock', 'indie_rock', 'gangster_rap',
    'alternative_metal', 'country', 'regional_mexican', 'new_wave_pop', 'soul',
    'r&b', 'post-teen_pop', 'tropical', 'quiet_storm', 'folk', 'hard_rock',
    'art_rock', 'dance_rock', 'classical_performance', 'roots_rock', 'edm',
    'brill_building_pop', 'indie_folk', 'electropop', 'contemporary_country',
    'hip_pop', 'blues_rock', 'underground_hip_hop', 'corrido',
    'stomp_and_holler'
]


class Preprocessor:
    def __init__(self):
        pass

    def OHE_genres(df=df_enc, top_50=top_50, fillna='rock'):
        """
        one hot encodes the given genres in the input list
        """
        df_cop = df.copy()
        df_cop[top_50] = 0
        for c, row in df_cop.iterrows():
            for i in top_50:
                if i in row['genres']:
                    df_cop.loc[c, i] = 1
            if all(row[top_50] == 0):
                df_cop.loc[c, fillna] = 1

        df_cop['target'] = 0

        return df_cop



    df_enc = OHE_genres()

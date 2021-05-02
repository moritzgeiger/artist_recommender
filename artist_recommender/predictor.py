# ML
from sklearn.neighbors import KNeighborsRegressor
from joblib import dump, load
import numpy as np

#TABLES
import pandas as pd
import pickle

# NLTK
import regex as re
import unicodedata


class Predictor:
    def __init__(self, artist):
        self.model = load('model.joblib')
        self.artist = artist
        self.df_enc = pd.read_csv('raw_data/preprocessed.csv', index_col=0)
        self.df = pd.read_csv('raw_data/data_by_artist_o.csv', index_col=0)

    def normalize(self, artist):
        """
        removing interpunction, trimming whitespaces and replacing spacial chars with their nearest relatives.
        inpt: a string you wish to normalize.
        returns: the normalized string.
        """
        reg = re.sub(r'[^\w\s]', ' ', artist.lower())
        white = re.sub(r'\s+', ' ', reg)
        uni = unicodedata.normalize('NFKD', white).encode('ascii','ignore').decode('utf8')
        return uni

    def finder(self):
        """
        will find your favourite artist in a given dataframe under the column name 'artist'.
        Pass the artist name (str) and the data frame (pd.DataFrame).
        returns: a pd.DataFrame containing the row of your searched artist
        """
        df_cop = self.df_enc.copy()
        df_cop['artists'] = df_cop.artists.apply(lambda x: self.normalize(x))
        artist = self.normalize(self.artist)
        print(f'looking for normalized term {artist}')
        try:
            # try to find the whole search term in artists via bool indexing
            ix = df_cop.artists[df_cop.artists == artist].index[0]
            print('found via bool indexing')
            return pd.DataFrame(df_cop.loc[ix,:]).T
        except:
            # tokenize search term
            search = artist.split(' ')
            # get index of searched term
            ixs = []
            for i, row in df_cop.iterrows():
                splt = row['artists'].lower().split(' ')
                found = [x in splt for x in search]
                if sum(found) >= len(found)/2:
                    ixs.append(i)
            if len(ixs) > 0:
                print('found alternatives via tokenized search')
                print(f'did you mean...')
                ## check if enc_df is needed
                return list(self.df.artists[ixs])
            else:
                print('could not find your artist. Please refine your search.')
                return 'Please refine your search'

    def recommend_artist(self, neighbors=3):
        """
        will find the nearest neighbors of the desired artist.
        pass the artists name, the fitted model and the pd.DataFrame suiting the model.
        returns a list of recommended artists similar to the imput artist.
        """
        inpt = self.finder()
        if isinstance(inpt, pd.DataFrame):
            print('got a valid dataframe')
            pred = inpt.drop(columns=['artists', 'genres', 'target'])
            print(f'df shape: {pred.shape}')
            dist, nearest = self.model.kneighbors(
                pred, n_neighbors=neighbors +
                1)  # Return the distances and index of the 2 closest points
            indexes = list(nearest[0])
            dist_new = dist[0][1:]  # the nearest is always the artist itself
            dist_fin = 1 - dist_new / (
                dist_new.max() + dist_new.max() / .2
            )  # the highest distance in the set => beautifying the range
            dist_fin = dist_fin.tolist() # streamlit doesnt seem to like same variable instanciations..
            print(f'distances: {dist_fin}')
            return {"success": self.df_enc.artists[indexes[1:]].tolist(),
                    "probas": dist_fin
                    }
        elif isinstance(inpt, list):
            print(inpt)
            return {'refine_search':inpt}
        else:
            return {'not_found':inpt}

# TABLES & VIS
import pandas as pd
from ast import literal_eval
import numpy as np

# ML
from sklearn.neighbors import KNeighborsRegressor
from joblib import dump, load


class Model:
    def __init__(self):
        self.df_enc = pd.read_csv('../raw_data/preprocessed.csv')

    def build_model(self):
        """
        builds the model from a given data set. dumps it to the root directory.
        """
        # Define X and y
        X = self.df_enc.drop(columns=['artists', 'genres',
                                'target'])  # Remove non numerical features
        y = self.df_enc['target']

        knn_model = KNeighborsRegressor().fit(X, y)  # Instanciate and train model
        dump(knn_model, '../model.joblib')
        return knn_model

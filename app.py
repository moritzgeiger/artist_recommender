# TABLES & VIS
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from ast import literal_eval
import numpy as np

# ML
from sklearn.neighbors import KNeighborsRegressor
from joblib import dump, load

# NLTK
import regex as re
import unicodedata

# PRODUCTION
import streamlit as st
import webbrowser
from urllib.parse import urljoin, quote

## PACKAGE CLASSES
from artist_recommender.predictor import Predictor

# for later redirection
spotify_const = 'https://open.spotify.com/search/'


########## PAGE CONFIG ##############
st.set_page_config(
    page_title="Spotify Artist Recommender",
    page_icon="🎸",
    layout="centered",
    initial_sidebar_state="collapsed")

####### INDEX PAGE ########
st.title('Welcome to the Spotify Artist Recommender App')
artist = st.text_input('Type in your favorite artist:')


#### FUNCTIONS #############
@st.cache(allow_output_mutation=True)
def recommender(artist):
    recommender = Predictor(artist)
    outpt = recommender.recommend_artist()
    return outpt

def show_results(lst_rec):
    for name in lst_rec:
        if st.button(name):
            name = quote(name)
            webbrowser.open_new_tab(urljoin(spotify_const, name))
        else:
            st.write('')

def result_handler(outpt):
    if 'success' in outpt:
        st.write(
            'I recommend you to check out the following three artists on Spotify:'
        )
        lst_rec = outpt['success']
        show_results(lst_rec)
        st.write('Click on one of the buttons to be redirected to Spotify.')

    elif 'refine_search' in outpt:
        st.write('Did you mean one of the following artists?')
        lst = outpt['refine_search']
        for alt in lst:
            with st.beta_expander(alt):
                outpt_new = recommender(alt)
                lst_rec = outpt_new['success']
                show_results(lst_rec)
                st.write(
                    'Click on one of the buttons to be redirected to Spotify.')

    elif 'not_found' in outpt:
        st.write('Couldn\'t find your artist')
        st.write(outpt['not_found'])

########## ACTIVATION FOR RECOMMENDER ###
if artist:
    outpt = recommender(artist.strip())

try:
    result_handler(outpt)
except:
    pass


############# SIDEBAR ################
st.sidebar.title("Credits")
st.sidebar.write("App made by Moritz Geiger. Visit my GitHub <a href='https://github.com/moritzgeiger/' target='blank'>here</a>.",
        unsafe_allow_html=True)

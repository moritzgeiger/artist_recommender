# Purpose 🎯
This is a very small project experimenting with the ```KNeighborsRegressor``` from the SkitLearn library.
The purpose is to showcase a clean workflow analyzing a data set of ~30,000 artists provided by this [kaggle source](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks?select=data_by_artist_o.csv).

# Contents 📒
This repo mainly focusses on a notebook analyzing the given data and building a small model to make find  similar musicians for a given input musician. The notebook can be found [here](https://github.com/moritzgeiger/artist_recommender/blob/main/notebooks/Artist_recommender.ipynb).

It is structured in the following way:

1. Introduction
2. Imports
3. The Dataset
4. Provided Features
5. Preprocessing
6. Model
7. Recommender

# The Recommender 🥁
The final recommender is also pushed to Heroku and available for everyone to try. Please follow this link to get there: [http://artist-recommender.herokuapp.com/](http://artist-recommender.herokuapp.com/).
The recommender is case, special-char and interpunction insensitive and therefore quite stable for a small project like this. Although it will only recognize fully written words and not auto-fill them (like 'Emine' or 'beatle'). Try it out yourself and have fun! 🥁

The app is run on a Streamlit Framework and hosted by heroku. Longer loading times might occur.


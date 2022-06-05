import streamlit as st
import pickle
import gzip
import pickletools
import pandas as pd




movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
filepath = "similarity.pkl"

with gzip.open(filepath, 'rb') as f:
    p = pickle.Unpickler(f)
    similarity = p.load()

#similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies



st.title('Movie Recommender System')

selected_movie = st.selectbox('Select a movie you love, and we will recommend you similar movies.',
             movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)

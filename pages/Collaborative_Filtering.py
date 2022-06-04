import streamlit as st
import pandas as pd
import pickle
import numpy as np
import sklearn


movieratings_pivot = pd.read_pickle('movieratings_pivot.pkl')
model_knn = pickle.load(open('model_knn.pkl', 'rb'))


st.title('Movie Recommender System')

st.markdown('### Using K-NN')
st.write("Pick your favourite movie, and we will recommend you similar movies that you might like.")

selected_movie = st.selectbox( '', movieratings_pivot.index)
distances, indices = model_knn.kneighbors(movieratings_pivot[movieratings_pivot.index == selected_movie].values.reshape(1, -1), n_neighbors = 11)


if st.button('Recommend'):
    for i in range(0, len(distances.flatten())):
        if i == 0:
            st.write(f'Recommended movies, similar to {selected_movie}:\n')
        else:
            st.write(f"{i}: {movieratings_pivot.index[indices.flatten()[i]]} with distance of {distances.flatten()[i]}:")

st.write("Note: The distance used in this algorithm is Cosine Distance. "
         "Thus, less the distance between the movies, more similarity between them.")

import streamlit as st
import pandas as pd


st.title(' Movie Recommendation Based on: -')

top10 = pd.read_pickle('top10.pkl')
popularity = top10.sort_values('popularity', ascending=False, ignore_index=True)
Weighted_Rating = top10.sort_values('Weighted_Rating', ascending=False, ignore_index=True)



col1, col2 = st.columns(2)

with col1:
    st.header("Popularity")
    st.dataframe(popularity.drop(columns=['id', 'vote_average', 'vote_count', 'Weighted_Rating', 'Norm_Weighted_Rating', 'Norm_popularity', 'score']).head(100))

with col2:
    st.header("Weighted Ratings")
    st.dataframe(Weighted_Rating.drop(columns=['id', 'vote_average', 'vote_count', 'popularity', 'Norm_Weighted_Rating', 'Norm_popularity', 'score']).head(100))


st.header("Score: Popularity and Weighted Ratings")
st.dataframe(top10.drop(columns=['id', 'vote_average', 'vote_count', 'Norm_Weighted_Rating', 'Norm_popularity']))

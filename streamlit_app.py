import streamlit as st

st.title('Movie Recommender Systems')

st.markdown('## Types of Movie Recommender System:-')
st.markdown('1. Popularity Based ')
st.markdown('2. Content Based filtering system ')
st.markdown('3. Collaborative filtering system')
st.write('In movie recommender systems we convert movies into vectors and then calculate the similarities between these vectors.')

st.markdown('### Similarity metrics that are mostly used:')

st.write('1. Cosine Similarity: The Cosine angle between the vectors.')
st.write('2. Dot Product: The cosine angle and magnitude of the vectors also matters.')
st.write('3. Euclidian Distance: The elementwise squared distance between two vectors.')
st.write('4. Pearson Similarity')

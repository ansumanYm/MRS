# Movie Recommender System

# Movie-Recommender-System
Web App:- 

Making a movie recommender system that can recommend movies in 3 different ways: Popularity based, Content based and Collaborative filtering.


![image](https://user-images.githubusercontent.com/96365389/171914506-09b4d2a0-011e-4fcc-a6f1-cc711c10ef11.png)

# Types of Movie Recommender System:-
  1. Popularity Based
  2. Content Based filtering system
  3. Collaborative filtering system


## Content-based filtering system: 
- Content-Based recommender system tries to guess the features or behavior of a user given the item’s features, he/she reacts positively to.
- It takes into account the genre, cast, crew and description of the movie a user liked, and then finds a similar kind of movie based on these metrices.
- Content-based filtering does not require other users' data during recommendations to one user.
- We converte all these features like genre, cast, crew, description, etc into vectors. Thus each movie is represented as a vector, and thus we can simply calculate the distance between thses vectors to find out similarities between them.

#### Similarity Metrics
They are mathematical measures which are used to determine how similar is a vector to a given vector.

Similarity metrics used mostly:

  1. Cosine Similarity: The Cosine angle between the vectors.
  2. Dot Product: The cosine angle and magnitude of the vectors also matters.
  3. Euclidian Distance: The elementwise squared distance between two vectors
  4. Pearson Similarity


## Collaborative filtering System: 
- Collaborative does not need the features of the items to be given. Every user and item is described by a feature vector or embedding.
- It creates embedding for both users and items on its own. It embeds both users and items in the same embedding space.
- It considers other users’ reactions while recommending a particular user. It notes which items a particular user likes and also the items that the users with behavior and likings like him/her likes, to recommend items to that user.

### Memory-based collaborative filtering: 
- Done mainly remembering the user-item interaction matrix, and how a user reacts to it, i.e, the rating that a user gives to an item. 
- There is no dimensionality reduction or model fitting as such.

### Model-based collaborative filtering: 
- Remembering the matrix, is not required here, thus it's not a memory-based recommender system. 
- From the matrix, we try to learn how a specific user or an item behaves. 
- We compress the large interaction matrix using dimensional Reduction or using clustering algorithms. 
- In this type, We fit machine learning models and try to predict how many ratings will a user give a product. There are several methods:

    1. Clustering algorithms
    2. Matrix Factorization based algorithm
    3. Deep Learning methods
    
#### 1. Clustering Algorithms: 
- They normally use simple clustering Algorithms like K-Nearest Neighbours to find the K closest neighbors or embeddings given a user or an item embedding based on the similarity metrics used.

#### 2. Matrix Factorization based algorithms:
- Idea: Like any big number can be factorized into smaller numbers, the user-item interaction table or matrix can also be factorized into two smaller matrices, and these two matrices can also be used to generate back the interaction matrix.


I have made a Web app that recommends movies by Popularity, Based on the content and by collaborative filtering.
Visit here: 


For further reading: 
- Types of Recommender systems: https://towardsdatascience.com/introduction-to-recommender-systems-1-971bd274f421
- Collaborative Filtering: https://towardsdatascience.com/various-implementations-of-collaborative-filtering-100385c6dfe0
- https://towardsdatascience.com/how-you-can-build-simple-recommender-systems-with-surprise-b0d32a8e4802
- Surprise Library: http://surpriselib.com For Matrix factorisation Method.
- Streamlit Documentation: https://docs.streamlit.io

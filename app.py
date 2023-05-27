import streamlit as st
import pickle
import pandas as pd     # to convert dictionary pickled file to dataframe
movies_dict = pickle.load(open('movie_dict.pkl','rb'))  # loading pickled file
movies =  pd.DataFrame(movies_dict)                     # dict to dataframe to access movie names
similarity = pickle.load(open('similarity_array.pkl','rb' ))  # to get vector array for each movie


def recommend(movie):
    index_of_movie =movies[movies['title'] == movie].index[0]   #will get index of input movie by user
    similarity_array = similarity[index_of_movie]        #will get array of similarity of given movie
    movies_req_list=sorted(list(enumerate(similarity_array)),reverse=True,key= lambda x: x[1])[1:6] #3.will fetch top 5 movies

    recommended_movies=[]
    for i in movies_req_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.title('Movies Recommender System')
selected_movie_name = st.selectbox('Select a movie',movies['title'].values)
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)    # will go back to recommend function and give us 5 movie names in list
    for i in recommendations:
        st.write(i)                        # will extract 5 items in list and display it one by one

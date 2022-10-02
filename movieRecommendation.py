import pickle
import streamlit as st
st.set_page_config(layout="wide")
import difflib
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    list_of_all_titles = movies_data['title'].tolist()
    find_close_match = difflib.get_close_matches(movie, list_of_all_titles)
    close_match = find_close_match[0]
    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 
    i = 1
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in sorted_similar_movies[1:10]:
        movie_id = movies_data.iloc[i[0]].id
        recommended_movie_names.append(movies_data.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movie_names,recommended_movie_posters

st.header('Movie Recommender System')
movies_data = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies_data['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3 = st.columns(3)
    i = 0
    while i<9:
        with col1:
            st.write(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])
        i=i+1
        with col2:
            st.write(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])
        i=i+1
        with col3:
            st.write(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])
        i=i+1

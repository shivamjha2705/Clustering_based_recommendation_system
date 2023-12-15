import streamlit as st
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=973f2675d48fd765d148f0e1d62f8e85&language=en-US'.format(
            movie_id))
    data = response.json()
    # Checking if 'poster_path' is present in the response
    if 'poster_path' in data:
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        return "No poster available"


def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]  # finding index
    distances = similarity[movie_index]

    # key will help in sorting based on similarities not on index
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies_df.iloc[i[0]].movie_id
        recommended_movies.append(movies_df.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


# Load the pickle file
movies_df = pd.read_pickle('movies.pkl')
similarity = pd.read_pickle('similarity.pkl')

# Applying CSS styles
st.markdown(
    """
    <style>
        
        .main{
            height: 100vh;
            width: 100vw;
            display: flex;
            align-items: center;
            justify-content: center;
            background-image: url("https://user-images.githubusercontent.com/33485020/108069438-5ee79d80-7089-11eb-8264-08fdda7e0d11.jpg"), linear-gradient(rgb(0 0 0 / 58%),rgb(0 0 0 / 78%));
            background-blend-mode: overlay;
            position: relative;
            }
        .main::after{
                position: relative;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-color: red;
            }
        header{
            background:transparent !important;
            }
        h1,.st-emotion-cache-16idsys p{color:white;}
        .st-bd {
            line-height: 2;
            }
        .st-ag {
            font-weight: 900;
            }
        .st-bx {
            background-color: rgb(250 250 250 / 59%);
            border: none;
            box-shadow: rgb(255 255 255 / 89%) 6px 2px 16px 0px, rgb(255 255 255 / 23%) -6px -2px 16px 0px;
        }
        .st-dc {
            background: linear-gradient(to bottom, #ffffff8c, #ffffff00);
            backdrop-filter: blur(42px);
            }
        .st-bd {
            line-height: 2;
        }
        .st-af {
            font-size: 1.8rem;
        }
        .st-emotion-cache-2n7b7j {
            background: #7ec1ff;
            }
        .st-emotion-cache-ocqkz7{align-items:center;}
        .st-emotion-cache-183lzff {color:white;}
        button{margin-top: 10px !important;}
        button p{font-weight:900;}
        .block-container{max-width:57rem;}
        .st-emotion-cache-mwz95r:hover{
            scale:1.2;
            z-index:11;
            cursor:pointer;
            transition: all 0.9s;
            box-shadow: rgb(255 255 255 / 89%) 0px 0px 16px 9px, rgb(255 255 255 / 23%) -6px -2px 16px 0px;
            }
        .st-emotion-cache-6awftf,.st-emotion-cache-eczf16{display:none;}
        # element-container{text-align:center;}
        
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():
    st.markdown('<div class="bg1">', unsafe_allow_html=True)
    st.title('Movie Recommendation System')
    selected_movie_name = st.selectbox('Search for a movie and get recommended 5 movies', movies_df['title'].values)

    # button
    if st.button('Recommend'):
        names, posters = recommend(selected_movie_name)

        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(names[0])
            st.image(posters[0])

        with col2:
            st.text(names[1])
            st.image(posters[1])
        with col3:
            st.text(names[2])
            st.image(posters[2])
        with col4:
            st.text(names[3])
            st.image(posters[3])
        with col5:
            st.text(names[4])
            st.image(posters[4])

    st.markdown('</div>', unsafe_allow_html=True)



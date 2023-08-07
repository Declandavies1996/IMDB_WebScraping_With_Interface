import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title('IMDB Web Scraper')

movie_Id = st.text_input('Enter IMDb Movie ID (e.g., tt0468569):')

if movie_Id:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    url = f'https://www.imdb.com/title/{movie_Id}/?ref_=chttp_t_3'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract movie title
    movie_title = soup.find("h1").text.strip()
    
    #Extract Rating
    rating = soup.find("sc-bde20123-1 iZlgcd")

    # Display movie title
    st.header(movie_title)
    
    # Extract movie rating
    rating_element = soup.find("span", class_="sc-bde20123-1 iZlgcd")
    if rating_element:
        rating = rating_element.text
        st.header("Movie Rating")
        st.write(rating)

    # Extract Description
    description_element = soup.find("span", class_="sc-466bb6c-2 eVLpWt")
    if description_element:
        description = description_element.text
        st.header("Movie Description")
        st.write(description)

else:
    st.warning("Please enter a valid IMDb Movie ID.")
    
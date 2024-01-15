import streamlit as st
import requests
from json import loads

st.image('/app/assets/logo.png')
st.title("My search engine :mag_right:")
option = st.sidebar.radio("Pick what you would like to search",["Demo","Summaries","Photos","Videos","Clear cache"])

if option == "Summaries":
    st.write("Fetched using Wikipedia's API")
    col1,col2,col3 = st.columns(3)
    with col1:
        word = st.text_input("Enter the word you would like to search")
    with col2:
        num = st.number_input("Enter the number if results you would like to get",step=1,min_value=1)
    with col3:
        but = st.button("Search!")
    if but:
        s = requests.get(f"http://almogf-back-end-1:8080/api/v1/search/{word}/times/{num}")
        if s.status_code == 200:
            st.success("Request succeeded")
            st.write(f"For the following word - '{word}' here are the top {num} results:")
            tmp = s.json()["data"]
            tmp.pop(0)
            for i in range (len(tmp)):
                st.write(f"{i+1}. {tmp[i]}")
        else:
            st.error(f"Sorry, no results were found for '{word}'")
if option == "Photos":
    st.write("Fetched using Pixabay's API")
    col1,col2,col3 = st.columns(3)
    with col1:
        photo = st.text_input("Enter the word you would like to search")
    with col2:
        num = st.number_input("Enter the number if photos you would like to get",step=1,min_value=1)
    with col3:
        but = st.button("Search!")
    if but:
        p = requests.get(f"http://almogf-back-end-1:8080/api/v1/photos/{photo}/times/{num}")
        if p.status_code == 200:
            st.success("Request succeeded")
            st.write(f"For the following word - '{photo}' here are the top {num} results:")
            tmp = p.json()["data"]
            tmp.pop(0)
            for i in range (len(tmp)):
                st.image(tmp[i])
        else:
            st.error(f"Sorry, no results were found for '{photo}'")
if option == "Clear cache":
    
    if st.button("Click here to clear cache"):
        clear_cache = requests.post("http://almogf-back-end-1:8080/api/v1/clearCache")
        if clear_cache.status_code == 200:
            st.success("Cache cleared")
        else:
            st.error("Sorry something went wrong, please try again")
if option == "Demo":
    col_a,col_b = st.columns(2)
    with col_a:
        get_button = st.button("Click me for the demo get request")
    with col_b:
        post_button = st.button("Click me for the demo post request")
    if get_button:
        g = requests.get("http://almogf-back-end-1:8080/api/v1/")
        if g.status_code == 200:
            st.success("Request suceeded")
            st.write(g.json()["data"])
        else:
            st.error("Request failed")
    if post_button:
        g = requests.post("http://almogf-back-end-1:8080/api/v1/")
        if g.status_code == 200:
            st.success("Request suceeded")
            st.write(g.json()["data"])
        else:
            st.error("Request failed")
            
if option == "Videos":
    st.write("Fetched using Youtube's API")
    col1,col2,col3 = st.columns(3)
    with col1:
        word = st.text_input("Enter the word you would like to search")
    with col2:
        num = st.number_input("Enter the number if results you would like to get",step=1,min_value=1)
    with col3:
        but = st.button("Search!")
    if but:
        s = requests.get(f"http://almogf-back-end-1:8080/api/v1/videos/{word}/times/{num}")
        if s.status_code == 200:
            st.success("Request succeeded")
            st.write(f"For the following word - '{word}' here are the top {num} results:")
            tmp = s.json()["data"]
            tmp.pop(0)
            for i in range (len(tmp)):
                st.video(f"{tmp[i]}",format='video/mp4',start_time=0)
        else:
            st.error(f"Sorry, no results were found for '{word}'")

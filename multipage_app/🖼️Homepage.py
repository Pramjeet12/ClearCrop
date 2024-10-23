import streamlit as st
from streamlit_lottie import st_lottie
import requests
st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)
st.title("Welcome to ClearCrop🌄.")
st.sidebar.success("Select a page above.")
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_factory = load_lottieurl("https://lottie.host/35cdb33c-76a6-4e10-b863-edf3706026cf/MGY1iI5H8S.json")
st_lottie(lottie_factory, key="factory")


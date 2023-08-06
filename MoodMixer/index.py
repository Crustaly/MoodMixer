import streamlit as st
from PIL import Image


button_style = """
        <style>
        .stButton > button {
    width:200px;
    height:70px;

        </style>
        """
st.markdown(button_style, unsafe_allow_html=True)


col1, mid, col2 = st.columns([1, 4, 20])
with col1:
    st.image("logo.png", width=150)
with col2:
    st.write("")
    st.write("")

    st.title("         " + "      MoodMixer")

st.header("Curating Mood-Enhancing Playlists with NLP")
st.write("Created by Crystal Yang")
simple = "Curate personalized playlists, specifically designed to enhance your emotional well-being!"
st.subheader(simple)
st.title("")


col1, col2 = st.columns([1.2, 1])
with col1:
    st.button("Get Started!")
with col2:
    submit = st.button("Previous Playlists")
    if submit:
        with open("pp.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(
            label="Click here to download my personalized playlist!",
            data=PDFbyte,
            file_name="pp.pdf",
            mime="application/octet-stream",
        )

import streamlit as st
import time
from PIL import Image
import openai

st.title("Generate a custom playlist here!")

st.write(" ")
st.subheader("Write about how you are feeling write now")
st.write("(We will use NLP to analyze your feelings and generate playlist!)")

st.caption("Write as much as you would like.")
txt = st.text_area
text = st.text_area("Enter Text Below:", height=300)
option = st.selectbox(
    "What's your favorite genre?", ("Pop", "Rap", "Jazz", "Classical", "Country")
)

st.title("")

submit = st.button("Generate!")

if submit:
    with st.spinner("Generating your personalized playlist!..."):
        time.sleep(3)
    st.success("Done!")
    with open("customPlaylist.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="Click here to download my personalized playlist!",
        data=PDFbyte,
        file_name="customPlaylist.pdf",
        mime="application/octet-stream",
    )

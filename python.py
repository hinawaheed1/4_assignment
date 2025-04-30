
import streamlit as st

st.title("My First Story Maker")
st.write("Answer the questions below to create your custom story!")

noun = st.text_input("Type a noun:")
verb = st.text_input("Type a verb:")
adjective = st.text_input("Type an adjective:")
place = st.text_input("Type a place:")

if st.button("Create Story"):
    story = f"One day in {place}, a {adjective} {noun} decided to {verb}. It changed everything!"
    st.subheader("Here's your story:")
    st.write(story)

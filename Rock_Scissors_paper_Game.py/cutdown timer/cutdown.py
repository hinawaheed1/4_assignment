
import streamlit as st
import time

st.title("Countdown Begins 🔔")
duration = st.number_input("Set timer (in seconds):", min_value=1, step=1)

if st.button("Begin Countdown"):
    placeholder = st.empty()
    for sec in range(duration, 0, -1):
        placeholder.markdown(f"⏱️ **{sec} seconds remaining...**")
        time.sleep(1)
    placeholder.markdown("🎉 **Boom! Time's up!**")

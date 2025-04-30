
import streamlit as st
import random

words = ['python', 'streamlit', 'project', 'hangman', 'developer']
word = random.choice(words).upper()
guessed = ['_' for _ in word]
tries = 6
used_letters = []

st.title("🎯 Hangman Game")
st.text(f"Word: {' '.join(guessed)}")
letter = st.text_input("Enter a letter:").upper()

if st.button("Guess"):
    if letter in used_letters:
        st.warning("Letter already used.")
    else:
        used_letters.append(letter)
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guessed[i] = letter
        else:
            tries -= 1

    st.write(f"Used Letters: {', '.join(used_letters)}")
    st.write(f"Remaining Tries: {tries}")
    st.text(f"Word: {' '.join(guessed)}")

    if '_' not in guessed:
        st.success("🎉 You won!")
    elif tries == 0:
        st.error(f"💀 Game Over! The word was: {word}")

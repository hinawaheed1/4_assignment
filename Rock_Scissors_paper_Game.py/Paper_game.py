
import streamlit as st
import random

def get_winner(player, computer):
    if player == computer:
        return "It's a tie"
    elif (player == 'Rock' and computer == 'Scissors') or \
         (player == 'Paper' and computer == 'Rock') or \
         (player == 'Scissors' and computer == 'Paper'):
        return "You win"
    else:
        return "Computer wins"

st.title("Rock Paper Scissors Game")

choices = ['Rock', 'Paper', 'Scissors']
player_choice = st.selectbox("Pick your move:", choices)
computer_choice = random.choice(choices)

if st.button("Play"):
    st.write(f"Your choice: {player_choice}")
    st.write(f"Computer's choice: {computer_choice}")
    result = get_winner(player_choice, computer_choice)
    st.subheader(result)

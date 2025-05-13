# 00_intro_python
# # 01_add_two_numbers.


# print("01_add_two_numbers.md")


# def add():
#     print("This application for add two numbers")
#     frist_number = int(input("Enter your frist number. "))
#     second_number = int(input("Enter your second number. "))
#     total = int(frist_number + second_number)
#     print(f'The total sum of {frist_number} and {second_number}is {total}')

# if __name__ == '__main__':
#     add()

# 02_agreement_bot.

# print("02_agreement_bot")

# def bot():

#     animal = str(input("What thair favorite animal is? "))
#     print(f"My favorite animal is also {animal}!")


# if __name__ == "__main__":
#     bot()
     
# 03_fahrenheit_to_celsius.

# print("03_convert_fahrenheit_to_celsius")
# def temp():
#   print("This for converting fahrenheit to celsius")
#   fahrenheit_degree = float(input("Enter your fahrenheit degree. "))
#   celsius_degree = (fahrenheit_degree - 32) * 5.0/9.0
#   print(f'Temperature {fahrenheit_degree} f = {celsius_degree} c')

# if __name__ == "__main__":

#     temp()

# 04_how_old_are_they.

# print("04_how_old_are_they")

# def add_ages():
#     anthon = 45
#     beth = anthon + 6
#     chen = beth + 20
#     derw = chen + anthon
#     ethan = chen + 0  # You can put any logic here

#     print("Anthon is " + str(anthon))
#     print("Beth is " + str(beth))
#     print("Chen is " + str(chen))
#     print("Derw is " + str(derw))
#     print("Ethan is " + str(ethan))

# if __name__ == "__main__":
#     add_ages(()

# 05_triangle_perimeter.
    
# print("05_triangle_perimeter.")

# def triangle():
#     print("This code is about sum of triangle sides")
#     side1 = float(input("Enter your first side of triangle: "))
#     side2 = float(input("Enter your second side of triangle: "))
#     side3 = float(input("Enter your third side of triangle: "))
#     total = side1 + side2 + side3
#     print(f"The sum of {side1}, {side2}, and {side3} is {total}")

# if __name__ == "__main__":
#     triangle()

# 06_square_number.

# print("06_square_number")
# def square():
#     print("This code is about square of given number")
#     num1 = int(input("Enter any number and i will give u a square value. "))
#     print(f'The square of {num1} is {num1 ** 2}')

# if __name__ == "__main__":
#     square()

# 01_expressions
# 01_dicesimulator.md

# import random
# print("01_dicesimulator")

# def roll_dice():
#     die1:int = random.randint(1,6)
#     die2:int = random.randint(1,6)
#     totall:int = die1 + die2
#     print(f'total of two dies: {totall}')

# def main():
#       die1:int = 10
#       print("die1 in main() start as: " + str(die1))
#       roll_dice()
#       roll_dice()
#       roll_dice()
#       print("die1 in main() is:" + str(die1))

# if  __name__ == "__main__":
#         main()

# 02_e=mc2.

# print("02_e=mc2")
# def energy():
#   c:float = 299792458
#   m:float = float(input("Enter kilos of mass:"))
#   print("e = m*c^2")
#   print("Mass =" + str(m) + " kg")
#   print("c =" + str(c) + " m/s")
#   print("e =" + str( m* c ** 2) + " jules")

# if  __name__ == "__main__":
#         energy()
     
# 03_feet_to_inches.md

# print("03_feet_to_inches.")
# inch: int = 12
# def foot():
#   feet:int = int(input("inter feet and i will convert into inches."))
#   print(f'There are {inch * feet}inches in {feet} feet.')
# if  __name__ == "__main__":
#   foot()

# 04_pythagorean_theorem.md

# import math
# print("04_pythagorean_theorem")
# def triangle():
#   ab:float = float(input("Enter the length of the side ab. "))
#   ac:float = float(input("Enter the length of the side ac. "))
#   bc:float = math.sqrt(ab**2 + ac**2)
#   print(f'The length of bc (the hypothenuse is : {bc})')
# if  __name__ == "__main__":
#   triangle()

# 05_remainder_division.md

# print("05_remainder_division")
# def remainder():
#   num1:int = int(input("Enter an integer to be divided: "))
#   num2:int = int(input("Enter an integer to divide by: "))
#   quoitlent:int = num1 // num2
#   remainder:int = num1 % num2
#   print(f'The result of following division is {quoitlent} with the remainder of {remainder}')
# if  __name__ == "__main__":
#   remainder()

# # 06_rolldice.md

# import random
# print("06_rolldice.")
# def dice():
#   die1:int= random.randint(1,6)
#   die2:int = random.randint(1,6)
#   total:int = int(die1 + die2)
#   print("First die:" + str(die1))
#   print("Second die:" + str(die2))
#   print(f'Total of two dies : {total}')

# if  __name__ == "__main__":
#   dice()

#  06_seconds_in_year.md    

# print("06_seconds_in_year")
# days_in_year:int=365
# hours_per_day:int=24
# minutes_per_hour:int=60
# seconds_per_minutes:int=60

# def seconds():
#   print(f"There are {days_in_year * hours_per_day * minutes_per_hour * seconds_per_minutes} seconds in a year!")

# if  __name__ == "__main__":
#   seconds()

# 07_tiny_mad_lib.md

# print("07_tiny_mad_lib")
# def mad_lib():
#   noun:str = str(input("Enter a noun: "))
#   adjective:str = str(input("Enter an adjective: "))
#   verb:str = str(input("Enter a verb: "))
#   print(f"Do you {verb} your {adjective} {noun} ?")

# if  __name__ == "__main__":
#     mad_lib()

# 02_lists
# 01_add_many_number.

# print("01_add_many_number")

# def add_number(numbers)->int:
#    num:int = 0
#    for i in numbers:
#     num += i
#    return num

# def main():
#       numbers:list[int] = [1,2,3,4,5,]
#       sum = add_number(numbers)
#       print(sum)
# if __name__ == "__main__":
#      main()
     

# print("02_double_list")

# def main():
#     numbers: list[int] = [1, 2, 3, 4, 5]
#     for i in range(len(numbers)):
#         index = numbers[i]
#         numbers[i] = index * 2
#     print(numbers)

# if __name__ == "__main__":
#     main()

# # 03_erase_canvas.


# import pygame
# import time

# pygame.init()

# CANVA_WIDTH = 400
# CANVA_HEIGHT = 400
# CELL_SIZE = 40
# ERASER_SIZE = 20

# BLUE = (0, 0, 225)
# WHITE = (255, 255, 255)
# PINK = (225, 182, 193)

# screen = pygame.display.set_mode((CANVA_WIDTH, CANVA_HEIGHT))
# pygame.display.set_caption("Enter effect in pygame")

# grid = []
# for row in range(0, CANVA_HEIGHT, CELL_SIZE):
#     for col in range(0, CANVA_WIDTH, CELL_SIZE):
#         rect = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE)
#         grid.append(rect)

# eraser = pygame.Rect(200, 200, ERASER_SIZE, ERASER_SIZE)

# running = True
# while running:
#     screen.fill(WHITE)

#     for rect in grid:
#         pygame.draw.rect(screen, BLUE, rect)

#     mouse_x, mouse_y = pygame.mouse.get_pos()
#     eraser.topleft = (mouse_x, mouse_y)

#     new_grid = []
#     for rect in grid:
#         if not eraser.colliderect(rect):
#             new_grid.append(rect)
#     grid = new_grid

#     pygame.draw.rect(screen, PINK, eraser)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     pygame.display.flip()
#     time.sleep(0.05)

# pygame.quit()


# 04_flowing_with_data_structures.

# print("04_flowing_with_data_structures")
# def add_three_coples(list,data):
#  for i in range(3):
#   list.append(data)

# def main():
#   message = input("Enter a message to copy.")
#   list = []
#   print("Before list:",)
#   add_three_coples(list,message)
#   print("After list:",list)

# if __name__ == "__main__":
#   main()


# 05_get_first_element.

# print("05_get_first_element")

# def get_first_element(lst):
#     print(lst[0])

# def get_lst():
#     lst = []
#     elem = input("Enter an element to add to the list: ")
#     while elem != "":
#         lst.append(elem)
#         elem = input("Enter an element to add to the list: ")
#     return lst

# def main():
#     lst = get_lst()
#     get_first_element(lst)

# if __name__ == "__main__":
#   main()
  
  
#   06_get_last_element.

# print("06_get_last_element")

# def get_last_element(lst):
#     print(lst[-1])

# def get_lst():
#     lst = []
#     elem = input("Enter an element to add to the list: ")
#     while elem != "":
#         lst.append(elem)
#         elem = input("Enter an element to add to the list: ")
#     return lst

# def main():
#     lst = get_lst()
#     get_last_element(lst)

# if __name__ == "__main__":
#     main()

# 07_get_list.

# print("07_get_list")

# def main():
#     lst = []
#     val = input("Enter a value to add to the list: ")
#     while val:
#         lst.append(val)
#         val = input("Enter a value to add to the list: ")
#     print("Here's the list:", lst)

# if __name__ == "__main__":
#     main()

# 08_shorten.

# print("08_shorten")

# MAX_LENGTH = 3

# def shorten(lst):
#     while len(lst) > MAX_LENGTH:
#         lst.pop()
#     return lst

# def get_lst():
#     lst = []
#     element = input("Enter an element to add to the list: ")
#     while element != "":
#         lst.append(element)
#         element = input("Enter an element to add to the list: ")
#     return lst

# def main():
#     lst = get_lst()
#     lst = shorten(lst)
#     print(".".join(lst) + ".")

# if __name__ == "__main__":
#     main()

# PROJECTS/homework_projects/03_if_statements
# print("01_print_events")
# def even():
#     for i in range(40):
#      print("Here is 20 even numbers are: ",i * 2)

# if __name__ == "__main__":
#     even()

# 02_international_voting_age.

# print("02_international_voting_age")

# peturksbouipo: int = 16
# Stanlau: int = 25
# Mayengua: int = 48

# def main():
#     age: int = int(input("How old are you? "))

#     if age >= peturksbouipo:
#         print(f"Your age is {age}, you are eligible to vote in Peturksbouipo")
#     else:
#         print(f"Your age is {age}, you are NOT eligible to vote in Peturksbouipo")

#     if age >= Stanlau:
#         print(f"Your age is {age}, you are eligible to vote in Stanlau")
#     else:
#         print(f"Your age is {age}, you are NOT eligible to vote in Stanlau")

#     if age >= Mayengua:
#         print(f"Your age is {age}, you are eligible to vote in Mayengua")
#     else:
#         print(f"Your age is {age}, you are NOT eligible to vote in Mayengua")

# if __name__ == "__main__":
#     main()

    # 03_if_statements/03_leap_year.

    # print("03_leap_year")

# def leap_year():
#     year: int = int(input("Enter a year: "))

#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print(f"{year} is a leap year")
#             else:
#                 print(f"{year} is not a leap year")
#         else:
#             print(f"{year} is a leap year")
#     else:
#         print(f"{year} is not a leap year")

# if __name__ == "__main__":
#     leap_year()

# 04_tall_enough_to_ride.

# print("04_tall_enough_to_ride")

# min_height: int = 50

# def main():
#     user: int = int(input("How tall are you? "))
#     if user >= min_height:
#         print("You are tall enough to ride")
#     else:
#         print("You are not tall enough to ride,My be next year.")

# if __name__ == "__main__":
#     main()

# 05_random_numbers.

# import random
# def main():
#   for i in range(10):
#     num:list[int] = random.randint(1,100)
#     print(num)

# if __name__ == "__main__":
#     main()

# PROJECTS/homework_projects/04_dictionaries

# # 00_count_nums.

# print("00_count_nums")

# def count_nums():
#     count_dict = {}

#     while True:
#         num = input("Enter a number (or 'Exit' to quit): ").strip()
#         if num == '' or num.lower() == 'exit':
#             break
#         elif num.isdigit():
#             num = int(num)
#             count_dict[num] = count_dict.get(num, 0) + 1
#             print(count_dict)
#         else:
#             print("Invalid input. Please enter a number or 'Exit'.")

#     return count_dict

# def display_counts(count_dict):
#     print("\nNumber Counts:")
#     for key, value in count_dict.items():
#         print(f"{key} appears {value} times")

# if __name__ == "__main__":
#     counts = count_nums()
#     display_counts(counts)

    # 04_dictionaries/01_phonebook.

    # print("01_phonebook")

# def add_contact(phonebook):
#     name = input("Enter contact name: ")
#     number = input("Enter contact number: ")
#     if name in phonebook:
#         print(f"{name} already exists in the phonebook.")
#     else:
#         phonebook[name] = number
#         print(f"{name} added to the phonebook.")

# def search_contact(phonebook):
#     name = input("Enter contact name to search: ")
#     if name in phonebook:
#         print(f"{name}: {phonebook[name]}")
#     else:
#         print(f"{name} not found in the phonebook.")

# def delete_contact(phonebook):
#     name = input("Enter contact name to delete: ")
#     if name in phonebook:
#         del phonebook[name]
#         print(f"{name} deleted from the phonebook.")
#     else:
#         print(f"{name} not found in the phonebook.")

# def display_contact(phonebook):
#     if phonebook:
#         print("\nPhonebook contacts list:")
#         for name, number in phonebook.items():
#             print(f"{name}: {number}")
#     else:
#         print("Phonebook is empty.")

# if __name__ == "__main__":
#     phonebook = {}
#     while True:
#         print("\nPhonebook Menu:")
#         print("1. Add Contact")
#         print("2. Search Contact")
#         print("3. Delete Contact")
#         print("4. Display Contacts")
#         print("5. Exit")

#         choice = input("Enter your choice (1-5): ")

#         if choice == '1':
#             add_contact(phonebook)
#         elif choice == '2':
#             search_contact(phonebook)
#         elif choice == '3':
#             delete_contact(phonebook)
#         elif choice == '4':
#             display_contact(phonebook)
#         elif choice == '5':
#             print("Exiting phonebook. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please enter a number between 1 and 5.")

    #  04_dictionaries/02_pop_up_shop.

    # print("02_pop_up_shop")

# def calculate_total_cost():
#     fruits_price = {
#         "apple": 5.0,
#         "mango": 15.0,
#         "kiwi": 8.0,
#         "pear": 12.0,
#         "banana": 16.0,
#         "orange": 10.0
#     }

#     total_cost = 0

#     for fruit, price in fruits_price.items():
#         while True:
#             try:
#                 quantity = int(input(f"How many {fruit} do you want?: "))
#                 if quantity < 0:
#                     print("Invalid input. Please enter a non-negative number.")
#                     continue
#                 total_cost += price * quantity
#                 print(f"Your total cost is: ${total_cost:.2f}\n")  # ✅ No "Final"
#                 break
#             except ValueError:
#                 print("Invalid input. Please enter a valid number.")

# if __name__ == "__main__":
#    calculate_total_cost()

# # 04_dictionaries/03_powerful_passwords.

# import hashlib

# print("03_powerful_passwords")

# def hash_password(password):
#     return hashlib.sha256(password.encode()).hexdigest()

# stored_logins = {
#     "user@example.com": hash_password("password123"),
#     "admin@example.com": hash_password("adminpass")
# }

# def login(email, password):
#     if email in stored_logins:
#         return stored_logins[email] == hash_password(password)
#     return False

# if __name__ == "__main__":
#     email = input("Enter your email: ")
#     password = input("Enter your password: ")

#     if login(email, password):
#         print("Login successful!")
#     else:
#         print("Invalid email or password.")

# PROJECTS/homework_projects/05_loops_control_flow

# 00_guess_my_number.

# import random

# def main():
#     secret_number = random.randint(1, 100)
#     print("I am thinking of a number between 1 and 100...")

#     guess = None
#     while guess != secret_number:
#         try:
#             guess = int(input("Enter a guess: "))
#         except ValueError:
#             print("Please enter a valid number.")
#             continue

#         if guess < secret_number:
#             print("Your guess is too low.")
#         elif guess > secret_number:
#             print("Your guess is too high.")
#         # when guess == secret_number, loop ends

#     print(f"Congratulations! The number was {secret_number}")

# if __name__ == "__main__":
#     main()

# 01_fibonacci.

# print("01_fibonacci")

# max_value = 10000

# def main():
#   a,b = 0,1
#   print(a,b,end=" ")

#   while True:
#     c = a+b
#     if c >= max_value:
#       break
#     print(c,end=" ")
#     a,b = b,c

# if __name__ == "__main__":
#   main()

# 02_print_events.

# print("02_print_events")

# def main():
#   for i in range(20):
#    print(i*2)

# if __name__ == "__main__":
#   main()

# 03_wholesome_machine.

# print("03_wholesome_machine")

# correct_affermation = "I am capable of doing anything.I put my mind too."

# def main():
#     print("Welcome to the Wholesome Machine")
#     while True:
#         user_input = input(
#             "please type the following affermation:" 
#             + correct_affermation 
#             + "\n"
#         )
#         if user_input == correct_affermation:
#             print("That's right!")
#             break
#         else:
#             print("That was not the affermation. try again")

# if __name__ == "__main__":
#     main()


# 04_liftoff.

# print("04_liftoff")

# def main():

#   for i in range(10, 0, -1):
#     print(i)
#   print("Liftoff!")

# if __name__ == "__main__":
#   main()

# 05_double_it.

# print("05_double_it")

# def main():
#     user_value = int(input("Enter a number: "))

#     while user_value < 100:
#         user_value = user_value * 2
#     print(user_value)

# if __name__ == "__main__":
#     main()


# PROJECTS/online_class_projects/01_basics

# print("00_joke_bot")

# PROMPT: str = "What do you want? "
# JOKE:str = "Why don't skeletons fight each other? \n Because they don't have the guts! 😂"
# SORRY:str = "sorry i only tell jokes."

# def main():
#     user_input = input(PROMPT)
#     user_input = user_input.lower()

#     if "joke" in user_input:
#         print(JOKE)
#     else:
#         print(SORRY)

# if __name__ == "__main__":
#     main()

# print("01_double_it")

# def main():
#   user_value = int(input("Enter a number:"))
#   while user_value < 100:

#    user_value = user_value * 2
#    print(user_value)

# if __name__ == "__main__":
#   main()

# print("02_liftoff")

# def main():

#   for i in range (10,0,-1):
#     print(i)
#   print("Liftoff!")

# if __name__ == "__main__":
#   main()

# import random
# print("00_guess_my_number.")

# def main():
#     secret_number = random.randint(1, 2)
#     print("I am thinking of a number between 1 and 100...")

#     guess = int(input("Enter a guess: "))

#     while guess != secret_number:
#         if guess < secret_number:
#             print("Your guess is too low.")
#         else:
#             print("Your guess is too high.")
#         guess = int(input("Enter a guess: "))

#     print(f"Congratulations! The number was {secret_number}")

# if __name__ == "__main__":
#     main()

# import random
# print("04_random_numbers")

# def main():
#     for _ in range(10):
#         print(random.randint(1, 100), end=" ")

# if __name__ == "__main__":
#     main()

# # mad_lib python project
# print("06_mad_libs")

# def main():
#     print("Let's create a fun Mad Libs story!")
    
#     noun = input("Enter a noun: ")
#     verb = input("Enter a verb: ")
#     adjective = input("Enter an adjective: ")
#     place = input("Enter a place: ")

#     print("\nHere's your story:")
#     print(f"Once upon a time in {place}, there was a {adjective} {noun} who loved to {verb} all day long.")

# if __name__ == "__main__":
#     main()

# Guess the Number Game Python Project (computer)

# import streamlit as st
# import random

# st.title("Number Guessing Game")

# random_number = random.randint(1, 3)
# user_input = st.number_input("Input Your Number", min_value=1, max_value=3, step=1)

# st.subheader("Let's check")

# if st.button("Check the number"):
#     if user_input < random_number:
#         st.warning("It's too low! Try something a bit higher. 🟡")
#     elif user_input > random_number:
#         st.warning("It's too high! Try something a bit lower. 🔴")
#     else:
#         st.success("🎉 Congratulations! You guessed the right number.")

# Guess the Number Game Python Project (user)

# import random

# def number_guessing_game():
#     print("🔢 Welcome! Think of a number between 1 and 100, and I'll try to guess it.")

#     minimum = 1
#     maximum = 100

#     while True:
#         computer_guess = random.randint(minimum, maximum)
#         print(f"🤔 Hmm... Is it {computer_guess}?")

#         response = input("Type 'too low', 'too high', or 'yes' if I got it right: ").lower().strip()

#         if response == 'too low':
#             minimum = computer_guess + 1
#         elif response == 'too high':
#             maximum = computer_guess - 1
#         elif response == 'yes':
#             print(f"🎉 Woohoo! I guessed it: {computer_guess} was your number!")
#             break
#         else:
#             print("⚠️ Please reply with 'too low', 'too high', or 'yes'.")

# number_guessing_game()


# Rock, paper, scissors Python Project

# import streamlit as st
# import random

# def get_winner(player, computer):
#     if player == computer:
#         return "It's a tie"
#     elif (player == 'Rock' and computer == 'Scissors') or \
#          (player == 'Paper' and computer == 'Rock') or \
#          (player == 'Scissors' and computer == 'Paper'):
#         return "You win"
#     else:
#         return "Computer wins"

# st.title("Rock Paper Scissors Game")

# choices = ['Rock', 'Paper', 'Scissors']
# player_choice = st.selectbox("Pick your move:", choices)
# computer_choice = random.choice(choices)

# if st.button("Play"):
#     st.write(f"Your choice: {player_choice}")
#     st.write(f"Computer's choice: {computer_choice}")
#     result = get_winner(player_choice, computer_choice)
#     st.subheader(result)

# Hangman Python Project

# import streamlit as st

# st.title("My First Story Maker")
# st.write("Answer the questions below to create your custom story!")

# noun = st.text_input("Type a noun:")
# verb = st.text_input("Type a verb:")
# adjective = st.text_input("Type an adjective:")
# place = st.text_input("Type a place:")

# if st.button("Create Story"):
#     story = f"One day in {place}, a {adjective} {noun} decided to {verb}. It changed everything!"
#     st.subheader("Here's your story:")
#     st.write(story)

# Countdown Timer Python Project

# import time

# def countdown(t):
#     while t:
#         mins, secs = divmod(t, 60)
#         timer = f"{mins:02d}:{secs:02d}"
#         print(timer, end="\r")
#         time.sleep(1)
#         t -= 1
#     print("Time's up!")

# seconds = int(input("Enter time in seconds: "))
# countdown(seconds)

# Password Generator Python Project

# import random
# import string

# characters = string.ascii_letters + string.digits + string.punctuation

# num_passwords = int(input("How many passwords do you want? "))
# length = int(input("Enter the length of each password: "))

# for _ in range(num_passwords):
#     password = ''.join(random.choice(characters) for _ in range(length))
#     print(password)

# BMI CALCULATOR


# import streamlit as st
# import pandas as pd 

# st.title("BMI calculator")

# height = st.slider("Enter your height (in cm):", 100, 250, 175)
# weight = st.slider("Enter your weight (in kg):", 40, 200, 70)

# bmi = weight / ((height / 100) ** 2)

# st.write(f"Your BMI is **{bmi:.2f}**")

# st.write("### BMI categories ###")
# st.write("- Underweight: BMI less than 18.5")
# st.write("- Normal weight: BMI between 18.5 and 24.9")
# st.write("- Overweight: BMI between 25 and 29.9")
# st.write("- Obesity: BMI 30 or greater")













     



















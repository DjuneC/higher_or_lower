import random
import os

from art import logo1, logo2
from game_data import instagram_data


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def get_follower_count(first, second):
    return first.get("follower_count"), second.get("follower_count")

def get_random_data():
    data = random.choice(instagram_data)

    return {"name": data["name"], "description": data["description"], "country": data["country"], "follower_count": data["follower_count"]}

def display_data(first, second, score=0):
    print(logo1)

    if score != 0:
        print("You got it right :> +1")

    print(f"Compare A: {first.get("name")}, a {first.get("description")}, from {first.get("country")}")
    print(logo2)
    print(f"Against B: {second.get("name")}, a {second.get("description")}, from {second.get("country")}")

def play(first_value, second_value, score):

    display_data(first=first_value, second=second_value)

    while True:

        answer = input("Who has more followers? Type 'A' or 'B': ").upper().strip()
        
        if answer not in ["A", "B"]:
            print("Can you read? look again. (Choose A or B)")
            continue

        f_follower_count, s_follower_count = get_follower_count(first=first_value, second=second_value)
        result = "A" if f_follower_count > s_follower_count else "B"


        if answer != result:
            clear_console()
            print(logo1)
            print(f"Sorry, that's wrong. Final score: {score}")
            break

        score += 1

        if result != "A":
            first_value = second_value

        second_value = get_random_data()
        
        clear_console()
        display_data(first=first_value, second=second_value, score=score)
import random
import os

from art import logo1, logo2
from game_data import instagram_data


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

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

def get_follower_count(first, second):
    return first.get("follower_count"), second.get("follower_count")
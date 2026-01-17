import random
import os

from game_data import instagram_data
from art import logo1, logo2

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def get_random_data():
    data = random.choice(instagram_data)

    return {"name": data["name"], "description": data["description"], "country": data["country"], "follower_count": data["follower_count"]}

def display_data(first, second):
    print(logo1)
    print(f"Compare A: {first.get("name")}, a {first.get("description")}, from {first.get("country")}")
    print(logo2)
    print(f"Against B: {second.get("name")}, a {second.get("description")}, from {second.get("country")}")

def play():
    pass

def main():
    first = get_random_data()
    second = get_random_data()
    f_follower_count = first.get("follower_count")
    s_follower_count = second.get("follower_count")
    score = 0

    display_data(first=first, second=second)

    while True:

        answer = input("Who has more followers? Type 'A' or 'B': ").upper()

        result = "A" if f_follower_count > s_follower_count else "B"

        if answer not in ["A", "B"]:
            print("Can you read? look again. (Choose A or B)")
            continue

        if answer != result:
            clear_console()
            print(logo1)
            print(f"Sorry, that's wrong. Final score: {score}")
            break
            

        print("You got it right :> +1")
        score += 1

        if result != "A":
            first = second

        second = get_random_data()
        
        clear_console()
        display_data(first=first, second=second)
        
    

    
if __name__ == "__main__":
    main()

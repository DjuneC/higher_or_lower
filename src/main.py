import random

from game_data import instagram_data


def get_random_data():
    data = random.choice(instagram_data)

    return {"name": data["name"], "description": data["description"], "country": data["country"], "follower_count": data["follower_count"]}

def display_data(first, second):
    print("Higher or lower")
    print(f"Compare A: {first.get("name")}, a {first.get("description")}, from {first.get("country")}")
    print("Vs.")
    print(f"Against B: {second.get("name")}, a {second.get("description")}, from {second.get("country")}")

def play():
    pass

def main():
    first = get_random_data()
    second = get_random_data()
    f_follower_count = first.get("follower_count")
    s_follower_count = second.get("follower_count")
    score = 0
    is_winning = True

    display_data(first=first, second=second)

    while is_winning:

        answer = input("Who has more followers? Type 'A' or 'B': ").upper()

        result = "A" if f_follower_count > s_follower_count else "B"

        if answer not in ["A", "B"]:
            print("Can you read? look again. (Choose A or B)")
            continue

        if answer != result:
            print("You bald head demon lookin' ass, you have lost...")
            is_winning = False
            break
            

        print("You got it right :> +1")
        score += 1

        if result != "A":
            first = second

        second = get_random_data()
        
        display_data(first=first, second=second)
        
    

    
if __name__ == "__main__":
    main()

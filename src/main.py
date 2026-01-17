import random

from game_data import instagram_data


def get_random_data():
    data = random.choice(instagram_data)

    return {"name": data["name"], "description": data["description"], "country": data["country"], "follower_count": data["follower_count"]}

def display_data(data_to_display):
    pass

def main():
    first = get_random_data()
    second = get_random_data()
    f_follower_count = first.get("follower_count")
    s_follower_count = second.get("follower_count")

    print("Higher or lower")

    print(f"Compare A: {first.get("name")}, a {first.get("description")}, from {first.get("country")}")
    print("Vs.")
    print(f"Against B: {second.get("name")}, a {second.get("description")}, from {second.get("country")}")

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    result = "A" if f_follower_count > s_follower_count else "B"

    print(result)

    
if __name__ == "__main__":
    main()

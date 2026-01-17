from art import logo1
from game_data import instagram_data
from game_operation import clear_console, get_random_data, display_data


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

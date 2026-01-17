from art import logo1
from game_operation import get_follower_count, get_random_data, clear_console, display_data


def main():
    first = get_random_data()
    second = get_random_data()

    score = 0

    display_data(first=first, second=second)

    while True:

        answer = input("Who has more followers? Type 'A' or 'B': ").upper().strip()

        f_follower_count, s_follower_count = get_follower_count(first=first, second=second)

        result = "A" if f_follower_count > s_follower_count else "B"
        print(result)

        if answer not in ["A", "B"]:
            print("Can you read? look again. (Choose A or B)")
            continue

        if answer != result:
            clear_console()
            print(logo1)
            print(f"Sorry, that's wrong. Final score: {score}")
            break

        score += 1

        if result != "A":
            first = second

        second = get_random_data()
        
        clear_console()
        display_data(first=first, second=second, score=score)
        
    

    
if __name__ == "__main__":
    main()

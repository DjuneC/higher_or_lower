from art import logo1
from game_operation import play, get_follower_count, get_random_data, clear_console, display_data


def main():
    first = get_random_data()
    second = get_random_data()

    score = 0

    play(first_value=first, second_value=second, score=score)        
   
    
if __name__ == "__main__":
    main()

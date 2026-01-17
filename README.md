# Instagram Follower Challenge - Higher or Lower Game

**A fun game to test your knowledge of Instagram celebrity and brand popularity!**

This Python project implements a Higher/Lower game where the user has to guess which of two names (celebrities or brands) has more followers on Instagram.  Each correct guess leads to a new comparison, and the game continues until the user loses.

## Table of Contents

*   [About](#about)
*   [Features](#features)
*   [How to Run](#how-to-run)
*   [Usage](#usage)
*   [Data Source](#data-source)
*   [Future Enhancements](#future-enhancements)
*   [Contributing](#contributing)
*   [License](#license)


## About

This project was created to be a simple, engaging game that combines trivia with a popular social media trend: Instagram follower counts. The core logic is based on the classic "Higher or Lower" game format.

## Features

*   **Interactive Game:** The user plays a turn-based Higher/Lower game.
*   **Instagram Focus:**  The game uses Instagram follower data.
*   **Celebrity & Brand Options:**  Names are drawn from a list of celebrities and popular brands.
*   **Scoring:**  The game tracks the user's score based on correct guesses.

## How to Run

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/DjuneC/higher_or_lower.git
    cd higher_or_lower
    ```

2.  **Run the Game:**
    ```bash
    python main.py
    ```
## Usage

1.  The game will start and display the first two names.
2.  The user is prompted to choose between "A" or "B", "A" or "B" can be a celebrity or a brand.
3.  The game will respond with whether their answer was correct.
4.  If correct, a new pair of names is presented.
5.  If incorrect, the game ends, and the user's score is displayed.

## Data Source

The names of celebrities and brands used in the game are obtained from a local data file. This data file is named `game_data.py`. This file is included with the repository. You could expand this later to pull data from an online source but 
for simplicity, it is local.

## Future Enhancements

*   **Expand the Data Source:** Use the Instagram API to fetch follower counts dynamically.
*   **Difficulty Levels:**  Implement different difficulty levels by varying the follower counts.
*   **Graphical User Interface (GUI):** Create a more visually appealing interface instead of the command-line version.
*   **Persistence:** Save high scores to a file.
*   **Error Handling:** Implement more robust error handling for API calls and data parsing.
*   **Data Validation:** Add checks to ensure the data being used is valid.

## Contributing

We welcome contributions to this project!  If you'd like to contribute, please:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them to your branch.
4.  Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

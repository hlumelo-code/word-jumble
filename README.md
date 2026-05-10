# WORD JUMBLE
<img width="580" height="386" alt="rmbg" src="https://github.com/user-attachments/assets/6d433b43-d545-4812-9b32-ef620626d7aa" />

## A CLI word-puzzle game inspired by Scrabble built to be *pythonic* and interactive.

The game provides the user with randomly sorted letters that do not make sense at first sight, but the player is tasked to rearrange them to form a word in order to complete each task. The game displays the set of characters to play with, and the user types them one-by-one to form the secret word hidden from the player.

## Project Details

#### Key Features

- Displays the the game title and the randomly sorted characters using the ASCII art through the "art" Python external library.
- Takes user input using "readchar", another Python external library that helps to record keyboard activity from user without having to press ENTER like the standard input() function built into the Python language. 
- Displays the progress of the player and the final result of the art using the same "art" library.
- The player can undo recent inputs if they made a mistake in rearranging characters.

#### Common Issues

The game currently only works for one round of JUMBLE, since the project is still in the developmental phase. This will be handled soon though, as I will work on building the game upwards. Do not be shocked when the game terminates after finishing the first word-puzzle you encounter.

#### Contacts & Links

- email -> hlumelowilliam@proton.me 
- X -> @hlumelo_code
- Facebook - @HlumeloWilliam 

## Installation & Usage Instructions

The project is currently not packaged as it is still developmental stage, so to use the code you have to manually `cd` to the `src/wordjumble` directory.

#### Creating a Virtual Environment

This project uses external libraries, so to make sure the code runs without raising the `ModuleNotFoundError`, make sure you first:
    - `cd/word-jumble`, which is the root directory of the project.
    - Create a Python Virtual Environment in the root directory of the project by typing the command -> `python -m venv .venv` in the terminal window. If you are suing a UNIX based OS like MAC OS or Linux, then the command will be similarly `python3 -m venv .venv`
    - Activate the Python Virtual Environment. On Windows -> `.venv\Scripts\activate` and on UNIX-like systems -> `source .venv/bin/activate`.

#### Installing Dependencies & Libraries 

To use install the dependencies, you must type the command `pip install -r requirements.txt`, which will automatically install all of the libraries needed to run the program successfully.

#### Using the Program 

You must `cd src/wordjumble`, then simply run the main.py file -> `python3 main.py`

## Usage Examples
#### Welcoming Window
<img width="1049" height="316" alt="Screenshot From 2026-05-07 12-18-19" src="https://github.com/user-attachments/assets/e9f2bd4b-b82a-449b-af75-8efc00783ac0" />

#### Playing Example for the word "DIMENSIONS"

<img width="1120" height="387" alt="Screencast From 2026-05-07 12-19-20" src="https://github.com/user-attachments/assets/d109a0f3-3e43-4165-8394-4d499b015725" />

#### Undoing Recent Inputs

<img width="853" height="371" alt="Screencast From 2026-05-07 12-35-27" src="https://github.com/user-attachments/assets/6dfde52c-07f5-41f6-bff9-75dc8eaa9bfa" />







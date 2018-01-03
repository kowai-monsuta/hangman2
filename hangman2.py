#Hangman
#Melissa V

import os
import random


def choose_language():
    global play_again_question, guess_win, guess_lose, guess_question, guess_play, guess_name, guess_hello, guess_cheater, guess_dumb, guess_win, huh_response, press_enter, bye_credit, name_credit, guess_enter
    
    print("")
    language = input("Whould you like to play in English or Spanish?")

    if language == 'English' or language == 'english' or language == 'e':
        guess_name = "What is your name?"
        guess_hello = "Hello! Welcome to..."
        guess_cheater = "Stop cheating! Enter one letter at time."
        guess_dumb = "Are you dumb? That's not a letter."
        play_again_question = "Wanna go again?"
        guess_enter = "Enter a letter:"
        huh_response = "I don't understand. Please enter 'y' or 'n'."
        guess_win = "You win!"
        guess_lose = "You lose!"
        press_enter = "Press Enter to continue..."
        guess_enter = "Enter a letter:"
        guess_play = "Save a life by guessing the word and spelling it correctly."
        bye_credit = "Thanks for playing!"
        name_credit = " This awesome game was created by "
    else:
        guess_name = "¿Cuál es su nombre?"
        guess_hello = "Hola! Bienvenido a..."
        guess_cheater = "Deja de hacer trampa! Ingrese una letra a la vez."
        guess_dumb = "¿Eres tonto? Esa no es una carta."
        play_again_question = "¿Quieres ir otra vez?"
        guess_enter = "Ingrese una letra:"
        huh_response = "No entiendo. Por favor ingrese 's' o 'n'."
        guess_win = "¡Tú ganas!"
        guess_lose = "Tú pierdes!"
        guess_play = "Salva una vida adivinando la palabra y deletreándola correctamente"
        press_enter = "Press Enter to continue..."
        bye_credit = "Gracias por jugar!"
        name_credit = " Este increíble juego fue creado por "



def show_start_screen():
    print("""
                                                                                            
                                                                              
   .                      _..._             __  __   ___                _..._    
 .'|                    .'     '.   .--./) |  |/  `.'   `.            .'     '.  
<  |                   .   .-.   . /.''\\  |   .-.  .-.   '          .   .-.   . 
 | |             __    |  '   '  || |  | | |  |  |  |  |  |    __    |  '   '  | 
 | | .'''-.   .:--.'.  |  |   |  | \`-' /  |  |  |  |  |  | .:--.'.  |  |   |  | 
 | |/.'''. \ / |   \ | |  |   |  | /("'`   |  |  |  |  |  |/ |   \ | |  |   |  | 
 |  /    | | `" __ | | |  |   |  | \ '---. |  |  |  |  |  |`" __ | | |  |   |  | 
 | |     | |  .'.''| | |  |   |  |  /'""'.\|__|  |__|  |__| .'.''| | |  |   |  | 
 | |     | | / /   | |_|  |   |  | ||     ||               / /   | |_|  |   |  | 
 | '.    | '.\ \._,\ '/|  |   |  | \'. __//                \ \._,\ '/|  |   |  | 
 '---'   '---'`--'  `" '--'   '--'  `'---'                  `--'  `" '--'   '--'

 """)
    print("")
    input("Press Enter to continue...")
    print("")

def get_name():
    print("")
    print(guess_name)
    name = input()
    print("")
    print(guess_play)
    print("")
    
def show_credits():
    print("")
    print(bye_credit)
    print("")
    print("")
    print("")
    print(name_credit)
    print("""
.----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | ____    ____ | || |  _________   | || |   _____      | || |     _____    | || |    _______   | || |    _______   | || |      __      | |
| ||_   \  /   _|| || | |_   ___  |  | || |  |_   _|     | || |    |_   _|   | || |   /  ___  |  | || |   /  ___  |  | || |     /  \     | |
| |  |   \/   |  | || |   | |_  \_|  | || |    | |       | || |      | |     | || |  |  (__ \_|  | || |  |  (__ \_|  | || |    / /\ \    | |
| |  | |\  /| |  | || |   |  _|  _   | || |    | |   _   | || |      | |     | || |   '.___`-.   | || |   '.___`-.   | || |   / ____ \   | |
| | _| |_\/_| |_ | || |  _| |___/ |  | || |   _| |__/ |  | || |     _| |_    | || |  |`\____) |  | || |  |`\____) |  | || | _/ /    \ \_ | |
| ||_____||_____|| || | |_________|  | || |  |________|  | || |    |_____|   | || |  |_______.'  | || |  |_______.'  | || ||____|  |____|| |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'
 """)

    
def play_again():
    print("")
    while True:
        decision = input(play_again_question)
        
        if decision == 'y' or decision == 'yes' or decision == 'si':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print(huh_response)


def get_puzzle():
    file_names = os.listdir("data")

    for i, f in enumerate(file_names):
        print(str(i) + ")" + f)

    choice = input("which one? ")
    choice = int(choice)

    file = "data/" + file_names[choice]

    with open(file, 'r') as f:
        lines = f.read().splitlines()

    category = lines[1]
    puzzle = random.choice(lines[1:])

    return puzzle

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses or not letter.isalpha():
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess():
    
    while True:
        print("")
        guess = input(guess_enter)
        print("")

        if len(guess) > 1:
            print(guess_cheater)
        
        elif not guess.isalpha():
            print(guess_dumb)
        
        else:
            return guess
    
def display_board(solved):
    print(solved)

def show_result(solved, puzzle):
    if solved == puzzle:
        print(guess_win)
    else:
        print(guess_lose)
        print(puzzle)
    
    
def play():
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)

    strikes = 0
    limit = len(puzzle)
    
    print(solved)
    
    while solved != puzzle and strikes < limit:
        letter = get_guess()

        if letter not in puzzle:
            pass
    
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)

        strikes += 1
        
    show_result(solved, puzzle)

show_start_screen()
choose_language()
name = get_name()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()

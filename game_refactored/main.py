'''
Main game file

imports game logic, UI

have play_round
'''

# Imports modules 
from game_logic import GuessGame
from ui import GameUI as GUI

def play_game():
    '''Single game round'''
    
    game = GuessGame()
    GUI.display_welcome()

    while not game.is_game_over():
        guess = GUI.get_guess()

        # Exit method handle
        if guess is None:
            GUI.display_goodbye()
            exit()
        
        # Invalid input handle
        if guess is False:
            continue

        # Process the passed guess
        result = game.make_guess(guess)

        # Handle out of range w/o counting attempts
        if result['result'] == 'invalid_range':
            GUI.display_error_out_of_range()
            continue
        # Handle if input is too low
        if result['result'] == 'too_low':
            GUI.display_hint_too_low(result['attempts_left'])
            continue

        # Handle if input is too high
        if result['result'] == 'too_high':
            GUI.display_hint_too_high(result['attempts_left'])
            continue

        # Handle if answer is correct
        if result['result'] == 'correct':
            GUI.display_win(result['secret_number'], result['attempts'])
            break
    
    # Handle loss - out of attempts
    if game.is_game_over() and game.attempts >= game.max_attempts:
        GUI.display_lose(game.secret_number)
    
    # Ask to play again
    ask_retry()

def ask_retry():
    '''Handles the retry function logic'''
    while True:
        choice = GUI.get_retry_choice()

        if choice is True:
            play_game()
            return
        elif choice is False:
            GUI.display_goodbye()
            exit()

def main():
    '''App entry point'''
    play_game()

if __name__ == "__main__":
    main()
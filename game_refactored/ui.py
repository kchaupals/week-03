'''
Game UI

Main functions - get_player_guess, show_hint, show_game_over and ask_play_again
'''
# Imports text output values from Config module
from config import (
    WELCOME_MSG, INSTRUCTIONS, EXIT_OPTION, GOODBYE_MSG,
    PROMPT_GUESS, PROMPT_RETRY, ERROR_INVALID_INPUT, ERROR_INVALID_RETRY,
    ERROR_OUT_OF_RANGE, HINT_TOO_HIGH, HINT_TOO_LOW, WIN_MSG, LOSE_MSG
)

class GameUI:
    '''Class that handles all user interface interactions'''

    @staticmethod
    def display_welcome():
        '''Displays welcome message and game instructions'''
        print(WELCOME_MSG)
        print(INSTRUCTIONS)
        print(EXIT_OPTION)

    @staticmethod
    def display_goodbye():
        '''Displays goodbye message'''
        print(GOODBYE_MSG)

    @staticmethod
    def get_guess():
        '''
        Method to get a guess from user input
        
        Returns:
            int or str: User guess (int) or 'q' to exit, or None if invalid input
        '''
        user_input = input(PROMPT_GUESS).strip()

        if user_input.lower() == 'q':
            return None
        try:    
            return int(user_input)
        except ValueError:
            print(ERROR_INVALID_INPUT)
            return False
    
    @staticmethod
    def display_error_out_of_range():
        '''Displays error message - Out of range'''
        print(ERROR_OUT_OF_RANGE)

    @staticmethod
    def display_hint_too_low(attempts_left):
        '''Displays message that provided guess is too low'''
        print(HINT_TOO_LOW.format(attempts_left=attempts_left))

    @staticmethod
    def display_hint_too_high(attempts_left):
        '''Displays message that provided guess is too high'''
        print(HINT_TOO_HIGH.format(attempts_left=attempts_left))

    @staticmethod 
    def display_win(number, attempts):
        '''Displays win message with dynamic values'''
        print(WIN_MSG.format(number=number, attempts=attempts))

    @staticmethod
    def display_lose(number):
        '''Displays lose message with secret number'''
        print(LOSE_MSG.format(number=number))

    @staticmethod
    def get_retry_choice():
        '''
        Questions user if they want to play again

        Returns:
            bool or None: True to play again, False to exit, None if invalid input is passed
        '''
        retry = input(PROMPT_RETRY).lower().strip()

        if retry in ['jā', 'ja']:
            return True
        elif retry in ['nē', 'ne']:
            return False
        else:
            print(ERROR_INVALID_RETRY)
            return None
        
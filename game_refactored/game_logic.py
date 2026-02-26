

'''
Game Logic for game - Guess the number

Requires:
    game_logic.py
    main.py
    ui.py
    scores.json (will be created if not present)

Functions - generate_secret, check_guess, is_game_over

'''
# Imports
import random 
from config import MIN_NUMBER, MAX_NUMBER, MAX_ATTEMPTS

class GuessGame:
    ''' This class handles the core game logic '''
    def __init__(self):
       ''' Function to initialize a new game '''
       self.secret_number = random.randint(MIN_NUMBER,MAX_NUMBER)
       self.attempts = 0
       self.max_attempts = MAX_ATTEMPTS

    def is_valid_guess(self, guess):
        '''
        Validate if the guess is within set range

        Parameters:
            guess (int): Users guess input
        
        Returns:
            bool: True if valid, False if otherwise
        
        '''
        return MIN_NUMBER <= guess <= MAX_NUMBER
    
    def make_guess(self, guess):
        '''
        Process a guess and return the result

        Parameters:
            guess (int): Users guess input
        
        Returns:
            dict: Containing 'result' (str), 'attempts_left' (int) and 'secret_number' (int)
        '''
        if not self.is_valid_guess(guess):
            return {
                'result': 'invalid_range',
                'attempts': self.attempts,
                'attempts_left': self.attempts_left,
                'secret_number': None
            }
        
        self.attempts += 1
        attempts_left = self.attempts_left

        if guess < self.secret_number:
            return {
                'result': 'too_low',
                'attempts': self.attempts,
                'attempts_left': attempts_left,
                'secret_number': None
            }
        elif guess > self.secret_number:
            return {
                'result': 'too_high',
                'attempts': self.attempts,
                'attempts_left': attempts_left,
                'secret_number': None
            }
        else:
            return {
                'result': 'correct',
                'attempts': self.attempts,
                'attempts_left': attempts_left,
                'secret_number': self.secret_number
            }
        
    @property
    def attempts_left(self):
        '''Get the number of attempts remaining'''
        return self.max_attempts - self.attempts
    
    def is_game_over(self):
        '''Check if the game has ended (reached max attempts)'''
        return self.attempts >= self.max_attempts
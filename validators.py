from datetime import datetime
'''
Uzdevums 3: Validācijas bibliotēka
Mērķis: nostiprināt funkciju rakstīšanu un virkņu apstrādi; praktizēt koda organizēšanu
atsevišķā modulī.
Izveido validators.py ar funkcijām:
is_email(text) # Vienkārša e-pasta validācija (satur @ un .)
is_phone_number(text) # Latvijas formāts: +371 XXXXXXXX (8 cipari)
is_valid_age(age) # 0–150, vesels skaitlis
is_strong_password(text) # Vismaz 8 simboli, satur burtus UN ciparus
is_valid_date(text) # YYYY-MM-DD formāts (pamata pārbaude)
Prasības:
• Katra funkcija atgriež bool (True/False)
• Katra funkcija — ar docstring
• validators.py ir atsevišķs modulis: to var importēt no citiem failiem
• if __name__ == "__main__": blokā — vismaz 3 testa gadījumi katrai funkcijai
(ieskaitot robežgadījumus)
# Piemērs: validators.py palaišana atsevišķi
python validators.py
# is_email('anna@inbox.lv') → True
# is_email('anna') → False
# is_email('anna@') → False
# is_phone_number('+371 26123456') → True
# is_phone_number('26123456') → False
# ...

'''

# define def's for validation 

def is_email(text):
    '''
    Function to validate passed e-mail, that should include [@] and [.]

    Args:
     text (str): Passed e-mail to be validated

    Returns:
        bool: True or False after e-mail has been validated
    '''
    if not isinstance(text, str) or not text:
        raise ValueError("To validate e-mail, the input must be not-empty string")
    return "@" in text and "." in text

def is_phone_number(text):
    '''
    Function to validate passed phone number, that should include [+371] and [8 numbers]

    Args:
     text (str): Passed phone number to be validated

    Returns:
        bool: True or False after phone number has been validated
    '''
    if not isinstance(text, str) or not text:
        raise ValueError("To validate number, the input must be not-empty string")
    
    text = text.replace(" ", "")

    if len(text) == 12 and text.startswith("+371") and text[4:].isdigit():
        return True
    return False
    

def is_valid_age(age):
    '''
    Function to validate passed age, that should be whole number and in range from 0-150

    Args:
     age (int): Passed age to be validated

    Returns:
        bool: True or False after age has been validated
    '''
    if not isinstance(age, (int, float)):
        return False
    if 0 <= age <= 150:
        return True
    return False


def is_strong_password(text):
    '''
    Function to validate and check if passed password is strong, that should include atleast 8 symbols, contain letters and numbers

    Args:
     text (str): Passed password to be validated

    Returns:
        bool: True or False after password has been validated
    '''
    if not isinstance(text, str):
        return False
    
    if len(text) < 8:
        return False
    
    # Setting flags for letter and number
    has_letter = False
    has_number = False

    for char in text:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_number = True
        
        if has_letter and has_number:
            return True
    return False

def is_valid_date(text):
    '''
    Function to validate passed date, that should be formated as follows: YYYY-MM-DD

    Args:
     text (str): Passed date to be validated

    Returns:
        bool: True or False after date has been validated
    '''
    if not isinstance(text, str):
        return False
    
    try:
        datetime.strptime(text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


    # validator.py main run demos 

if __name__ == "__main__":
    print(f'is_email("anna@yahoo.com") -> {is_email('anna@yahoo.com')}')
    print(f'is_email("anna.com") -> {is_email('anna.com')}')
    print(f'is_email("anna@") -> {is_email('anna@')}')
    print(f'is_phone_number("+371 2623456") -> {is_phone_number('+371 26123456')}')
    print(f'is_phone_number("26123456") -> {is_phone_number('26123456')}')
    print(f'is_phone_number("+371zoo") -> {is_phone_number('+371zoo')} ')
    print(f'is_valid_age(12) -> {is_valid_age(12)}')
    print(f'is_valid_age(245) -> {is_valid_age(245)}')
    print(f'is_valid_age(-25) -> {is_valid_age(-25)}')
    print(f'is_strong_password("MainuEiro") -> {is_strong_password('MainuEiro')}')
    print(f'is_strong_password("MainuEiro12") -> {is_strong_password('MainuEiro12')}')
    print(f'is_strong_password("12345678z") -> {is_strong_password('12345678z')}')
    print(f'is_valid_date("3045-85-75") -> {is_valid_date('3045-85-75')}')
    print(f'is_valid_date("2026-02-25") -> {is_valid_date('2026-02-25')}')
    print(f'is_valid_date("2.august") -> {is_valid_date('2.august')}')
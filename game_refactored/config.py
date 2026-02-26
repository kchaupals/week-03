'''
** Guess game configuration **

    Contains variables, that could be changed in future

    Also contains all text output to user, so this could be easily translated to serve game in different language
'''
# Import Game Logic for dynamic outputs


# Constants for game

MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 10

# UI Messages 

WELCOME_MSG = "★★★★ Sveicināti spēle 'Uzmini skaitli' ★★★★"
INSTRUCTIONS = f"★★★ Es esmu izvēlējies skaitli no {MIN_NUMBER} līdz {MAX_NUMBER}. Vai vari to uzminēt {MAX_ATTEMPTS} mēģinājumos? ★★★★"
EXIT_OPTION = '★★★★ Lai izietu no spēles, nospiest taustiņu "q" ★★★★' 
GOODBYE_MSG = "★★★★ Paldies par spēli, uz redzēšanos! ★★★★"

PROMPT_GUESS = "ℹ Ievadi savu minējumu (Vai 'q' lai izietu):"
PROMPT_RETRY = "ℹ Vai vēlies uzspēlēt vēlreiz? (Jā/Nē):"

ERROR_INVALID_INPUT = f"⚠ Nederīga ievade. Lūdzu, ievadi skaitli no {MIN_NUMBER} līdz {MAX_NUMBER}."
ERROR_OUT_OF_RANGE = f"⚠ Lūdzu, ievadīt skaitli no {MIN_NUMBER} līdz {MAX_NUMBER}"
ERROR_INVALID_RETRY = "⚠ Lūdzu, ievadi atbilid (Jā/Nē)"

# Messages with placeholders
HINT_TOO_LOW = "⚠ Par mazu! Mēģini vēlreiz. Tev ir atlikuši {attempts_left} mēģinājums(-i)!"
HINT_TOO_HIGH = "⚠ Par lielu! Mēģini vēlreiz. Tev ir atlikuši {attempts_left} mēģinājums(-i)!"
WIN_MSG = "✔ Super, spēle beigusies! Tu uzminēji skaitli {number} pēc {attempts} mēģinājumiem!"
LOSE_MSG = "✖ Tev neizdevās uzminēt. Atbilde bija {number}"

# Placeholders will be filled with dynamic values from Game Logic module
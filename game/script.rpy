# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:
    # Kutsutaan vuorotellen eri osat peliä call-funktiolla.
    # Peliosion loppuun laitetaan return niin kontrolli palaa tähän runkoon.
    call upgradetree
    return

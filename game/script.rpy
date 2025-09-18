# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:
<<<<<<< HEAD
    e "heippa :-D"
=======
    e "Hei maailma"
>>>>>>> 329b02491bce1fc5dd7274bd903f1e3fcd4bf412
    # Kutsutaan vuorotellen eri osat peliä call-funktiolla.
    # Peliosion loppuun laitetaan return niin kontrolli palaa tähän runkoon.
    call warehouse_gameplay
    call padTest
    call upgradeTree
    call upgradeCount
    return

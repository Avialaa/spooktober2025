# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#TODO: When we have better talking sounds, use this for character speech 
# init python:
#     def characterSpeak(event, interact = True, **kwargs):
#         if not interact:
#             return
#         if event == "show":
#             renpy.sound.play("audio/beeboob.mp3")
#         elif event == "slow_done" or event == "end":
#             renpy.sound.stop()

# define e = Character("Eileen", callback=characterSpeak)
# define A = Character("Agatha", callback=characterSpeak)
# define MC = Character("McName", callback=characterSpeak) # myöhemmin sit nimenvalinta
# define K = Character("Karkhos", callback=characterSpeak)
# define C = Character("Cee", callback=characterSpeak)
# define All = Character("All", callback=characterSpeak)

define e = Character("Eileen")
define A = Character("Agatha")
define MC = Character("McName") # myöhemmin sit nimenvalinta
define K = Character("Karkhos")
define C = Character("Cee")
define All = Character("All")

# The game starts here.

label start:
    # Kutsutaan vuorotellen eri osat peliä call-funktiolla.
    # Peliosion loppuun laitetaan return niin kontrolli palaa tähän runkoon.
    #call warehouse_gameplay
    #call roundEnd
    #call after_minigame

    #call day2_5A
    call day1_2
    
    
    #call padTest
    #call upgradeTree
    #call upgradeCount
    return

label after_minigame:
    e "minigame is over"

    return
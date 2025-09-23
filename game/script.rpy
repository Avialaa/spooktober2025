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

style karkhosNameStyle:
    color "#91A571"
    line_spacing -10
    xalign 0.5 yalign 0.3
    yoffset -10
    font "Raleway-Bold.ttf"
    size 45

default mcName = "Petri Dish"

define e = Character("Eileen")
define A = Character("Agatha", who_color="#CB985F")
define MC = Character("[mcName]", who_color="#84bdaf")
define K = Character("Karkhos\n{size=-17}{font=DMSans-Light.ttf}The Destroyer{/size}{/font}", who_style="karkhosNameStyle")
define C = Character("Cee", who_color="#877EA4")
define All = Character("All")

# The game starts here.

label start:
    # Kutsutaan vuorotellen eri osat peliä call-funktiolla.
    # Peliosion loppuun laitetaan return niin kontrolli palaa tähän runkoon.
    #call choose_name

    #call warehouse_gameplay
    #call roundEnd
    #call after_minigame

    call day2_3A
    #call day1_2
    
    
    #call padTest
    #call upgradeTree
    #call upgradeCount
    return

label after_minigame:
    $ quick_menu = True #show the quick menu
    e "minigame is over"

    return

label choose_name:
    #Example label for choosing main character name. 
    #TODO: Copy this into appropriate file when ready.
    python:
        mcName = renpy.input("You are a slime. What is your name?", allow=None, exclude='{}', length=15)
        mcName = mcName.strip()

        if not mcName:
            mcName = "Petri Dish"
    
    MC "test test test"
    MC "test test"
    return

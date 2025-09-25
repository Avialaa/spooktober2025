# The script of the game goes in this file.

init python:
    def karkhosSpeak(event, interact = True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/speakKarkhos.mp3")
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()
    def agathaSpeak(event, interact = True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/speakAgatha.mp3")
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()
    def ceeSpeak(event, interact = True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/speakCee.mp3")
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()
    def MCSpeak(event, interact = True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/speakMC.mp3")
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

define e = Character("Eileen")
define A = Character("Agatha", who_color="#CB985F", callback=agathaSpeak)
define MC = Character("[mcName]", who_color="#84bdaf", callback=MCSpeak) # myöhemmin sit nimenvalinta
define K = Character("Karkhos\n{size=-17}{font=DMSans-Light.ttf}The Destroyer{/size}{/font}", who_style="karkhosNameStyle", callback=karkhosSpeak)
define C = Character("Cee", who_color="#877EA4", callback=ceeSpeak)
define All = Character("All")

default mcName = "Petri Dish"

# The game starts here.

label start:
    # Kutsutaan vuorotellen eri osat peliä call-funktiolla.
    # Peliosion loppuun laitetaan return niin kontrolli palaa tähän runkoon.
    call upgradeTree
    call choose_name
    #call day1_1
    #eka minipelityövuoro
    call day1_2
    #call day1_3A jos $ agreewithagatha = True, sama day1_3B ja day1_3C
    # toinen minipelityövuoro
    if currentStoryRoute == "agatha":
        call day1_4A
    elif currentStoryRoute == "cee":
        call day1_4C
    # else:
    #     call day1_4B
    if currentStoryRoute == "agatha":
        call day1_6A
    elif currentStoryRoute == "karkhos":
        call day1_6B
    # elif currentStoryRoute == "cee":
    #     call day1_6C
    #call day2_1
    #kolmas minipelityövuoro
    #call day2_2
    if currentStoryRoute == "agatha":
        call day2_3A
    #elif currentStoryRoute == "karkhos":
    #   call day2_3B
    #elif currentStoryRoute == "cee":
    #   call day2_3C
    #neljäs minipelityövuoro
    if currentStoryRoute == "agatha":
        call day2_5A
    elif currentStoryRoute == "karkhos":
        call day2_5B
    elif currentStoryRoute == "cee":
        call day2_5C
    if currentStoryRoute == "agatha":
        call day3_1A
    if currentStoryRoute == "karkhos":
        call day3_1B
    if currentStoryRoute == "cee":
        call day3_1C
    
    call warehouse_gameplay
    call roundEnd
    call after_minigame
    call warehouse_gameplay
    call roundEnd
    call after_minigame
    call warehouse_gameplay
    call roundEnd
    call after_minigame

    call day2_3A
    #call day1_2
    
    #call padTest
    call upgradeTree
    #call upgradeCount
    return


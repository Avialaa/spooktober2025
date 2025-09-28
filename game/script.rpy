# The script of the game goes in this file.

init python:
    renpy.music.register_channel("beeps", mixer="voice") #custom channel for character voices

    def karkhosSpeak(event, interact = True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/speakKarkhos.mp3", channel='beeps')
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel='beeps')
    def agathaSpeak(event, interact = True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/speakAgatha.mp3", channel='beeps')
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel='beeps')
    def ceeSpeak(event, interact = True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/speakCee.mp3", channel='beeps')
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel='beeps')
    def MCSpeak(event, interact = True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/speakMC.mp3", channel='beeps')
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel='beeps')
    def allspeak(event, interact = True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/allspeak.mp3", channel='beeps')
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel='beeps', fadeout=1)
    def DeliverySpeak(event, interact = True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/speakDelivery.mp3", channel='beeps')
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel='beeps')
    
    

define e = Character("Eileen")
define A = Character("Agatha", who_color="#CB985F", callback=agathaSpeak)
define MC = Character("[mcName]", who_color="#84bdaf", callback=MCSpeak) # myöhemmin sit nimenvalinta
define K = Character("Karkhos\n{size=-17}{font=DMSans-Light.ttf}The Destroyer{/size}{/font}", who_style="karkhosNameStyle", callback=karkhosSpeak)
define C = Character("Cee", who_color="#877EA4", callback=ceeSpeak)
define All = Character("All", callback=allspeak)
define DeliveryAgent = Character("Delivery Agent", callback=DeliverySpeak)

default mcName = "Petri Dish"

# The game starts here.

label start:
    # Kutsutaan vuorotellen eri osat peliä call-funktiolla.
    # Peliosion loppuun laitetaan return niin kontrolli palaa tähän runkoon.
    #call upgradetreeTest
    call choose_test
    call choose_name
    call day1_1
    if minigameOn == True:
        #eka minipelityövuoro
        call tutorial
        call warehouse_gameplay
        call roundEnd
        call after_minigame
    else:
        call testing_choose_route

    call day1_2
    #call day1_3A jos $ agreewithagatha = True, sama day1_3B ja day1_3C
    if minigameOn == True:
        # toinen minipelityövuoro
        call tutorial_again
        call upgradeTree
        call warehouse_gameplay
        call roundEnd
        call after_minigame
    else:
        call testing_choose_route

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
    elif currentStoryRoute == "cee":
        call day1_6C
    call day_change #day changes!!
    call day2_1
    if minigameOn == True:
        #kolmas minipelityövuoro
        call upgradeTree
        call warehouse_gameplay
        call roundEnd
        call after_minigame
    else:
        call testing_choose_route

    call day2_2
    if currentStoryRoute == "agatha":
        call day2_3A
    elif currentStoryRoute == "karkhos":
        call day2_3B
    elif currentStoryRoute == "cee":
        call day2_3C

    if minigameOn == True:
        #neljäs minipelityövuoro
        call upgradeTree
        call warehouse_gameplay
        call roundEnd
        call after_minigame
    else:
        call testing_choose_route


    if currentStoryRoute == "agatha":
        call day2_5A
    elif currentStoryRoute == "karkhos":
        call day2_5B
    elif currentStoryRoute == "cee":
        call day2_5C
    call day_change #day changes!!
    call day3_1

    if minigameOn == True:
        #Viides työvuoro
        call upgradeTree
        call warehouse_gameplay
        call roundEnd
        call after_minigame
    else:
        call testing_choose_route
        
    if currentStoryRoute == "agatha":
        call day3_A1
    if currentStoryRoute == "karkhos":
        call day3_B1
    if currentStoryRoute == "cee":
        call day3_C1
    call finalcredits
    return


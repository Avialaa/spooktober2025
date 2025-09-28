default preferences.text_cps = 40

style karkhosNameStyle:
    color "#91A571"
    line_spacing -10
    xalign 0.5 yalign 0.3
    yoffset -10
    font "Raleway-Bold.ttf"
    size 45

style redPointsStyle:
    color "#eb3847"

style bluePointsStyle:
    color "#218ec4"

style yellowPointsStyle:
    color "#f0e767"

style greenPointsStyle:
    color "#4ec236"

style orangePointsStyle:
    color "#ffaa00"

style violetPointsStyle:
    color "#b272ed"

style pinkPointsStyle:
    color "#ee88cc"

style lightPointsStyle:
    color "#b1b1b1"

define audio.ilo = "audio/Vibing-Over-Venus.mp3"
define audio.riita = "audio/Chase-Pulse.mp3"
define audio.isoriita = "audio/Clash-Defiant.mp3"
define audio.bondaus = "audio/Heavy-Heart.mp3"
define audio.bondaus2 = "audio/Bittersweet.mp3"
define audio.suru = "audio/Wounded.mp3"
define audio.juoru = "audio/Vanes.mp3"
define audio.ending = "audio/Mana-Two-Part1.mp3"
define audio.metkut = "audio/Deadly-Roulette.mp3"



label after_minigame:
    $ quick_menu = True #show the quick menu
    $ chooseRoute() #must always be called BEFORE minigame reset
    $ resetMinigame()
    $ updateOrders()
    $ _skipping = True #allow skipping again
    $ renpy.block_rollback()
    $ config.rollback_enabled = True #allow rollback again

    if currentStoryRoute:
        e "Current route: [currentStoryRoute]"

    return

label choose_name:
    #Example label for choosing main character name. 
    #TODO: Copy this into appropriate file when ready.
    scene bg namingmc with fade
    python:
        mcName = renpy.input("You are a slime. What is your name?", allow=None, exclude='{}', length=15)
        mcName = mcName.strip()

        if not mcName:
            mcName = "Petri Dish"
    
    return

default minigameOn = True
label choose_test:
    menu:
        "Do you want to test minigame or both story and minigame or just story?"

        "Minigame only":
            $ minigameOn = True
            call test_minigame
        "Story and minigame":
            $ minigameOn = True
            return
        "Just story":
            $ minigameOn = False
            return

label testing_choose_route:
    menu:
        "Minigame skipped. Pick character route."

        "Karkhos":
            $ currentStoryRoute = "karkhos"
        "Agatha":
            $ currentStoryRoute = "agatha"
        "Cee":
            $ currentStoryRoute = "cee"
    
    if currentStoryRoute:
        e "Current route: [currentStoryRoute]"
    return


label test_minigame:
    call warehouse_gameplay
    call roundEnd
    call after_minigame
    call upgradeTree
    call warehouse_gameplay
    call roundEnd
    call after_minigame
    call upgradeTree
    call warehouse_gameplay
    call roundEnd
    call after_minigame
    call upgradeTree
    call warehouse_gameplay
    call roundEnd
    call after_minigame

    return

transform next_day:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

label day_change:
    if _skipping:
        hide screen skip_indicator
        $ _skipping = False
        $ renpy.config.skipping = False
    scene black with dissolve
    play sound nextday
    call screen day_change
    $ _skipping = True
    return
screen day_change:
    modal False

    add "black" at next_day
    
    text "The next day...":
        xcenter 0.5 ycenter 0.5
        at next_day
    timer 3.5 action [Hide(), Return()]

label tutorial:
    scene bg warehouse
    "Someone left sticky notes on the new work station... Looks like instructions on how to use the new system."
label sticky_notes_tutorial:
    window hide
    scene tutorial with fade
    pause
    scene bg warehouse with fade

label sticky_notes_menu:
    menu:
        "Take another look at the sticky notes.":
            jump sticky_notes_tutorial
        "Start your work shift.":
            pass
    
    return

label tutorial_again:
    scene bg warehouse
    "The sticky notes containing instructions are still on the work station."
    jump sticky_notes_menu

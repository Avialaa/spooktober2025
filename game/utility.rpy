
style karkhosNameStyle:
    color "#91A571"
    line_spacing -10
    xalign 0.5 yalign 0.3
    yoffset -10
    font "Raleway-Bold.ttf"
    size 45

label after_minigame:
    $ quick_menu = True #show the quick menu
    $ chooseRoute() #must always be called BEFORE minigame reset
    $ resetMinigame()
    $ updateOrders()

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

label choose_test:
    menu:
        "Do you want to test minigame or both story and minigame?"

        "Minigame only":
            call test_minigame
        "Story and minigame":
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

screen day_change:
    modal False
    add "black"
    text "The next day..." xcenter 0.5 ycenter 0.5
    timer 2.0 action Return()

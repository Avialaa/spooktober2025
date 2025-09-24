
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
    e "minigame is over"
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
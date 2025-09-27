label finalcredits:
    scene black
    show screen creditscreen
    pause 
    
    # or however long it takes to scroll through in a reasonable speed
    
    hide screen creditscreen
    return

screen creditscreen:
    modal True
    timer 50 action Hide()
    vbox:
        xsize 1080 # horizontal size of the credits
        ysize 4000 # how much vertical space your rolling credits take.
        xalign 0.5
        yalign 0.0
        at transform:
            subpixel True
            linear 40: # or however long it takes to scroll through in a reasonable speed
                yalign 1.0
                yoffset -500

        vbox:
            ysize 720 # enter vertical resolution, so that it starts with an empty screen
        text "Monstrocracy: Monster Workplace Democracy": #tähän logo kuvana? TO DO
            font "DMSans-Light.ttf"
            color "#6ea380"
            size 70
            xalign 0.5

        vbox:
            xalign 0.5
            spacing 10
            text "Lila Lukkarinen" :
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 50
                xalign 0.5
            text "Aimo Kurki":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 50
                xalign 0.5
            text "Alli \"Aviala\" Loikkanen":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 50
                xalign 0.5
            text "Lotta \"Otava\" Kokkonen":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 50
                xalign 0.5
            text "Nnancy":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 50
                xalign 0.5
            text "Noora \"Nuuri\" Nousiainen":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 50
                xalign 0.5
            text "Tuukka Mattila":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 50
                xalign 0.5   
            text "Julia": #TO DO julian nimi
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 50
                xalign 0.5
        vbox:
            xalign 0.5
            spacing 10
            text "Zoom Viewport":
                font "DMSans-Light.ttf"
                color "#9e6f94"
                size 50
                xalign 0.5
            text "Feniks @ feniksdev.com":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
        # text ""
        # text "Made with Ren'Py.":
        #     font "DMSans-Light.ttf"
        #     bold True
        #     xalign 0.5
        # vbox:
        #     ysize 100 # some empty space in between
        # add "a/a cg piano.png": # adding a picture in-between the text
        #     zoom 0.75
        #     xalign 0.5


        text "Thank you for playing!":
            font "DMSans-Light.ttf"
            color "#8580b1"
            bold True
            xalign 0.5
        vbox:
            ysize 500 # enter vertical resolution, so that it starts with an empty screen

        text "The End":
            font "DMSans-Light.ttf"
            bold True
            xalign 0.5
            yalign 0.5




label finalcredits:
    $ quick_menu = False
    scene black
    call screen creditscreen
    
    
    # or however long it takes to scroll through in a reasonable speed
    
    
   
    return

screen creditscreen:
    textbutton "Skip" action Return() xpos 0.95 ypos 0.95
    modal True
    timer 120 action Return()
    vbox:
        xsize 1080 # horizontal size of the credits
        ysize 9000 # how much vertical space your rolling credits take.
        xalign 0.5
        yalign 0.0
        
        at transform:
            subpixel True
            linear 110: # or however long it takes to scroll through in a reasonable speed
                yalign 1.0
                yoffset -500

        vbox:
            ysize 1100 # enter vertical resolution, so that it starts with an empty screen
        add 'gamelogo.png':
            xalign 0.5 # center horizontally
        text " ":
            size 50

        text "Made with Ren'Py for the Spooktober 2025 Jam":
            font "DMSans-Light.ttf"
            color "#91a197"
            xalign 0.5

        vbox:
            xalign 0.5
            spacing 10
            text "Developement team":
                font "DMSans-Light.ttf"
                color "#a37a9a"
                size 50
                xalign 0.5
                bold True
            text "Lila Lukkarinen" :
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "Aimo Kurki":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "Alli \"Aviala\" Loikkanen":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "Lotta \"Otava\" Kokkonen":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "Nnancy":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "Noora \"Nuuri\" Nousiainen":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "Tuukka Mattila":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5   
            text "Julia Limpet": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
        vbox:
            xalign 0.5
            spacing 20
            text "Project leader":
                font "DMSans-Light.ttf"
                color "#a37a9a"
                size 50
                xalign 0.5
                bold True
            text "Lila Lukkarinen":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5        
        vbox:
            xalign 0.5
            spacing 20
            text "Writing":
                font "DMSans-Light.ttf"
                color "#a37a9a"
                size 50
                xalign 0.5
                bold True
            vbox:
                xalign 0.5
                spacing 10
                text "Original concept, Karkhos, Agatha":
                    font "DMSans-Light.ttf"
                    color "#6a8885"
                    size 40
                    xalign 0.5
                    bold True
                text "Julia Limpet":
                    font "DMSans-Light.ttf"
                    color "#8580b1"
                    size 30
                    xalign 0.5
                text "Agatha":
                    font "DMSans-Light.ttf"
                    color "#6b8b89"
                    size 40
                    xalign 0.5
                    bold True
                text "Lotta \"Otava\" Kokkonen":
                    font "DMSans-Light.ttf"
                    color "#8580b1"
                    size 30
                    xalign 0.5
                text "Cee":
                    font "DMSans-Light.ttf"
                    color "#6b8b89"
                    size 40
                    xalign 0.5
                    bold True
                text "Nnancy":
                    font "DMSans-Light.ttf"
                    color "#8580b1"
                    size 30
                    xalign 0.5
        vbox:
            xalign 0.5
            spacing 20
            text "Game design and minigame":
                font "DMSans-Light.ttf"
                color "#a37a9a"
                size 50
                xalign 0.5
                bold True
            text "Alli \"Aviala\" Loikkanen":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5     
            text "Tuukka Mattila":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5     
        vbox:
            xalign 0.5
            spacing 20
            text "Lead programmer":
                font "DMSans-Light.ttf"
                color "#a37a9a"
                size 50
                xalign 0.5
                bold True
            text "Alli \"Aviala\" Loikkanen":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5   
        vbox:
            xalign 0.5
            spacing 20
            text "Programmers":
                font "DMSans-Light.ttf"
                color "#a37a9a"
                size 50
                xalign 0.5
                bold True
            text "Tuukka Mattila":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5   
            text "Lotta \"Otava\" Kokkonen":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5   
            text "Aimo Kurki":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5   
        vbox:
            xalign 0.5
            spacing 20
            text "Art":
                font "DMSans-Light.ttf"
                color "#a37a9a"
                size 50
                xalign 0.5
                bold True
            text "Art lead, UI design, Character art":
                font "DMSans-Light.ttf"
                color "#6b8b89"
                size 40
                xalign 0.5
                bold True
            text "Lila Lukkarinen":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5   
            text "Background art":
                font "DMSans-Light.ttf"
                color "#6b8b89"
                size 40
                xalign 0.5
                bold True
            text "Aimo Kurki":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5   
            text "Asset artist":
                font "DMSans-Light.ttf"
                color "#6b8b89"
                size 40
                xalign 0.5
                bold True
            text "Noora \"Nuuri\" Nousiainen":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5   

        vbox:
            xalign 0.5
            spacing 20
            text "Sound design":
                font "DMSans-Light.ttf"
                color "#a37a9a"
                size 50
                xalign 0.5
                bold True
            text "Lotta \"Otava\" Kokkonen":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5   
            text "Noora \"Nuuri\" Nousiainen":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5   
            text "Alli \"Aviala\" Loikkanen":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5   
            text "Julia Limpet":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5  

        vbox:
            xalign 0.5
            spacing 20
            text "Character sounds":
                font "DMSans-Light.ttf"
                color "#a37a9a"
                size 50
                xalign 0.5
                bold True
            text "Lotta \"Otava\" Kokkonen":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5  

        vbox:
            xalign 0.5
            spacing 10
            text "Music":
                font "DMSans-Light.ttf"
                color "#a37a9a"
                size 50
                xalign 0.5
                bold True

            text "\"Vibing Over Venus\" Kevin MacLeod (incompetech.com)": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "Licensed under Creative Commons: By Attribution 4.0 License": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 20
                xalign 0.5
            text "http://creativecommons.org/licenses/by/4.0/": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 20
                xalign 0.5
            text "   "
            text "\"Clash Defiant\" Kevin MacLeod (incompetech.com)": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "Licensed under Creative Commons: By Attribution 4.0 License": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 20
                xalign 0.5
            text "http://creativecommons.org/licenses/by/4.0/": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 20
                xalign 0.5
            text "   "
            text "\"Heavy Heart\" Kevin MacLeod (incompetech.com)": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "Licensed under Creative Commons: By Attribution 4.0 License": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 20
                xalign 0.5
            text "http://creativecommons.org/licenses/by/4.0/": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 20
                xalign 0.5
            text "   "
            text "\"Wounded\" Kevin MacLeod (incompetech.com)": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "Licensed under Creative Commons: By Attribution 4.0 License": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 20
                xalign 0.5
            text "http://creativecommons.org/licenses/by/4.0/": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 20
                xalign 0.5
            text "   "
            text "\"Vanes\" Kevin MacLeod (incompetech.com)": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "Licensed under Creative Commons: By Attribution 4.0 License": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 20
                xalign 0.5
            text "http://creativecommons.org/licenses/by/4.0/": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 20
                xalign 0.5
            text "   "
            text "\"Mana Two - Part 1\" Kevin MacLeod (incompetech.com)": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "Licensed under Creative Commons: By Attribution 4.0 License": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 20
                xalign 0.5
            text "http://creativecommons.org/licenses/by/4.0/": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 20
                xalign 0.5
            text "   "
            text "\"Bittersweet\" Kevin MacLeod (incompetech.com)": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "Licensed under Creative Commons: By Attribution 4.0 License": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 20
                xalign 0.5
            text "http://creativecommons.org/licenses/by/4.0/": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 20
                xalign 0.5
            text "   "
            text "\"Deadly Roulette\" Kevin MacLeod (incompetech.com)": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "Licensed under Creative Commons: By Attribution 4.0 License": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 20
                xalign 0.5
            text "http://creativecommons.org/licenses/by/4.0/": 
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 20
                xalign 0.5
            
        vbox:
            xalign 0.5  
            text "Sound effects":
                font "DMSans-Light.ttf"
                color "#a37a9a"
                size 50
                xalign 0.5
                bold True
            text "Thank you to the following users of freesound.org:":
                font "DMSans-Light.ttf"
                color "#6b8b89"
                size 40
                xalign 0.5
                bold True
            text "xkeril":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "qubodup":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "bruno.auzet":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "RutgerMuller":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "Godowan":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "Kneeling":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5

            text "LeonsFlashlight":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "CrownieYT":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "magnuswaker":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "TheBuilder15":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "CogFireStudios":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "kwahmah_02":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "PkBiggums":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
            text "Valenspire":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
        vbox:
            xalign 0.5
            spacing 10
            text "Zoom Viewport":
                font "DMSans-Light.ttf"
                color "#a37a9a"
                size 50
                xalign 0.5
                bold True
            text "Feniks @ feniksdev.com":
                font "DMSans-Light.ttf"
                color "#8580b1"
                size 30
                xalign 0.5
 


        text "Thank you for playing!":
            font "DMSans-Light.ttf"
            color "#8580b1"
            bold True
            xalign 0.5
        vbox:
            ysize 500 

        text "The End":
            font "DMSans-Light.ttf"
            bold True
            xalign 0.5
            yalign 0.5




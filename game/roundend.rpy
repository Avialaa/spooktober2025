
default roundEndrPoints = False
default roundEndbPoints = False
default roundEndyPoints = False
default roundEndgPoints = False
default roundEndoPoints = False
default roundEndvPoints = False
default roundEndpPoints = False
default roundEndlPoints = False

default roundEndTotalrPoints = False
default roundEndTotalbPoints = False
default roundEndTotalyPoints = False
default roundEndTotalgPoints = False
default roundEndTotaloPoints = False
default roundEndTotalvPoints = False
default roundEndTotalpPoints = False
default roundEndTotallPoints = False

default fishTotal = 0

init:
    image scoreBox = Frame("minigame scorebg.png", 40, 50)


label roundEnd:
    #Minigame is concluded by calling this label
    python:
        rPoints += roundrPoints+timerPoints
        bPoints += roundbPoints+timerPoints
        yPoints += roundyPoints+timerPoints
        gPoints += roundgPoints+timerPoints
        oPoints += roundoPoints+timerPoints
        vPoints += roundvPoints+timerPoints
        pPoints += roundpPoints+timerPoints
        lPoints += roundlPoints+timerPoints

        fishTotal += roundpPoints #kalapisteiden kokonaismäärä

        roundEndrPoints = False
        roundEndbPoints = False
        roundEndyPoints = False
        roundEndgPoints = False
        roundEndoPoints = False
        roundEndvPoints = False
        roundEndpPoints = False
        roundEndlPoints = False

        roundEndTotalrPoints = False
        roundEndTotalbPoints = False
        roundEndTotalyPoints = False
        roundEndTotalgPoints = False
        roundEndTotaloPoints = False
        roundEndTotalvPoints = False
        roundEndTotalpPoints = False
        roundEndTotallPoints = False
    call screen roundEndScreen
    python:
        roundrPoints = 0
        roundbPoints = 0
        roundyPoints = 0
        roundgPoints = 0
        roundoPoints = 0
        roundvPoints = 0
        roundpPoints = 0
        roundlPoints = 0
    return


screen roundEndScreen:

    on "show":
        action Play('audio', 'shiftOver_cogfirestudios__puzzle-game-victory-melody.mp3')
    
    #Timers to show point numbers
    timer 1.2 action SetVariable("roundEndrPoints", True)
    timer 1.4 action SetVariable("roundEndbPoints", True)
    timer 1.6 action SetVariable("roundEndyPoints", True)
    timer 1.8 action SetVariable("roundEndgPoints", True)
    timer 2.0 action SetVariable("roundEndoPoints", True)
    timer 2.2 action SetVariable("roundEndvPoints", True)
    timer 2.4 action SetVariable("roundEndpPoints", True)
    timer 2.6 action SetVariable("roundEndlPoints", True)

    timer 2.8 action SetVariable("roundEndTotalrPoints", True)
    timer 3.0 action SetVariable("roundEndTotalbPoints", True)
    timer 3.2 action SetVariable("roundEndTotalyPoints", True)
    timer 3.4 action SetVariable("roundEndTotalgPoints", True)
    timer 3.6 action SetVariable("roundEndTotaloPoints", True)
    timer 3.8 action SetVariable("roundEndTotalvPoints", True)
    timer 4.0 action SetVariable("roundEndTotalpPoints", True)
    timer 4.2 action SetVariable("roundEndTotallPoints", True)

    #Returns automatically TODO: quicken with action
    timer 6.0 action Return()

    hbox:
        align(0.5, 0.5)

        frame:
            padding(30, 20)
            background "scoreBox"
            vbox:
                xysize (250, 600)
                text "This round:"
                if roundEndrPoints:
                    text "{outlinecolor=#000}{color=#e82333}[f'{roundrPoints:.2f}']{/color}{/outlinecolor}" #f'{my_float:.6f}
                else: 
                    null height 39
                if roundEndbPoints:
                    text "{outlinecolor=#000}{color=#218ec4}[f'{roundbPoints:.2f}']{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndyPoints:
                    text "{outlinecolor=#000}{color=#f0e767}[f'{roundyPoints:.2f}']{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndgPoints:
                    text "{outlinecolor=#000}{color=#4ec236}[f'{roundgPoints:.2f}']{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndoPoints:
                    text "{outlinecolor=#000}{color=#ffaa00}[f'{roundoPoints:.2f}']{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndvPoints:
                    text "{outlinecolor=#000}{color=#8c47cc}[f'{roundvPoints:.2f}']{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndpPoints:
                    text "{outlinecolor=#000}{color=#ee88cc}[f'{roundpPoints:.2f}']{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndlPoints:
                    text "{outlinecolor=#000}{color=#999999}[f'{roundlPoints:.2f}']{/color}{/outlinecolor}"
                else: 
                    null height 39

        null width 50

        frame:
            padding(30, 20)
            background "scoreBox"
            vbox:
                xysize (250, 600)
                text "Total Points:"
                if roundEndTotalrPoints:
                    text "{outlinecolor=#000}{color=#e82333}[f'{rPoints:.2f}']{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndTotalbPoints:
                    text "{outlinecolor=#000}{color=#218ec4}[f'{bPoints:.2f}']{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndTotalyPoints:
                    text "{outlinecolor=#000}{color=#f0e767}[f'{yPoints:.2f}']{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndTotalgPoints:
                    text "{outlinecolor=#000}{color=#4ec236}[f'{gPoints:.2f}']{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndTotaloPoints:
                    text "{outlinecolor=#000}{color=#ffaa00}[f'{oPoints:.2f}']{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndTotalvPoints:
                    text "{outlinecolor=#000}{color=#8c47cc}[f'{vPoints:.2f}']{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndTotalpPoints:
                    text "{outlinecolor=#000}{color=#ee88cc}[f'{pPoints:.2f}']{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndTotallPoints:
                    text "{outlinecolor=#000}{color=#999999}[f'{lPoints:.2f}']{/color}{/outlinecolor}"
                else: 
                    null height 39


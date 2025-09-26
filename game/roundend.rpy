
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
                    text "[f'{roundrPoints:.2f}']" style "redPointsStyle"
                else: 
                    null height 39
                if roundEndbPoints:
                    text "[f'{roundbPoints:.2f}']" style "bluePointsStyle"
                else: 
                    null height 39
                if roundEndyPoints:
                    text "[f'{roundyPoints:.2f}']" style "yellowPointsStyle"
                else: 
                    null height 39
                if roundEndgPoints:
                    text "[f'{roundgPoints:.2f}']" style "greenPointsStyle"
                else: 
                    null height 39
                if roundEndoPoints:
                    text "[f'{roundoPoints:.2f}']" style "orangePointsStyle"
                else: 
                    null height 39
                if roundEndvPoints:
                    text "[f'{roundvPoints:.2f}']" style "violetPointsStyle"
                else: 
                    null height 39
                if roundEndpPoints:
                    text "[f'{roundpPoints:.2f}']" style "pinkPointsStyle"
                else: 
                    null height 39
                if roundEndlPoints:
                    text "[f'{roundlPoints:.2f}']" style "lightPointsStyle"
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
                    text "[f'{rPoints:.2f}']" style "redPointsStyle"
                else: 
                    null height 39
                if roundEndTotalbPoints:
                    text "[f'{bPoints:.2f}']" style "bluePointsStyle"
                else: 
                    null height 39
                if roundEndTotalyPoints:
                    text "[f'{yPoints:.2f}']" style "yellowPointsStyle"
                else: 
                    null height 39
                if roundEndTotalgPoints:
                    text "[f'{gPoints:.2f}']" style "greenPointsStyle"
                else: 
                    null height 39
                if roundEndTotaloPoints:
                    text "[f'{oPoints:.2f}']" style "orangePointsStyle"
                else: 
                    null height 39
                if roundEndTotalvPoints:
                    text "[f'{vPoints:.2f}']" style "violetPointsStyle"
                else: 
                    null height 39
                if roundEndTotalpPoints:
                    text "[f'{pPoints:.2f}']" style "pinkPointsStyle"
                else: 
                    null height 39
                if roundEndTotallPoints:
                    text "[f'{lPoints:.2f}']" style "lightPointsStyle"
                else: 
                    null height 39


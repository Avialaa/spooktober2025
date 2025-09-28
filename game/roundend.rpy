
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
default endSensitivity = False

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

    #screen can be skipped by click or space after 1 second, automatically skip after 30 s
    timer 1.0 action Setvariable("endSensitivity", True)
    if endSensitivity:
        key ["mousedown_1", "K_SPACE"] action [Return(), Setvariable("endSensitivity", False)]
    timer 30 action Return()

    hbox:
        align(0.5, 0.5)

        frame:
            padding(30, 20)
            background "scoreBox"
            vbox:
                xysize (250, 800)
                text "This round:"
                if roundEndrPoints:
                    hbox:
                        text "[f'{roundrPoints:.2f}']" style "redPointsStyle"
                        add "order meat.png":
                            fit "scale-down"
                            xysize (40,40)
                else: 
                    null height 36
                if roundEndbPoints:
                    hbox:
                        text "[f'{roundbPoints:.2f}']" style "bluePointsStyle"
                        add "order weapon.png":
                            fit "scale-down"
                            xysize (40,40)
                else: 
                    null height 36
                if roundEndyPoints:
                    hbox:
                        text "[f'{roundyPoints:.2f}']" style "yellowPointsStyle"
                        add "order treasure.png":
                            fit "scale-down"
                            xysize (40,40)
                else: 
                    null height 36
                if roundEndgPoints:
                    hbox:
                        text "[f'{roundgPoints:.2f}']" style "greenPointsStyle"
                        add "order sleep.png":
                            fit "scale-down"
                            xysize (40,40)
                else: 
                    null height 36
                if roundEndoPoints:
                    hbox:
                        text "[f'{roundoPoints:.2f}']" style "orangePointsStyle"
                        add "order light.png":
                            fit "scale-down"
                            xysize (40,40)
                else: 
                    null height 36
                if roundEndvPoints:
                    hbox:
                        text "[f'{roundvPoints:.2f}']" style "violetPointsStyle"
                        add "order fish.png":
                            fit "scale-down"
                            xysize (40,40)
                else: 
                    null height 36
                if roundEndpPoints:
                    hbox:
                        text "[f'{roundpPoints:.2f}']" style "pinkPointsStyle"
                        add "order keys.png":
                            fit "scale-down"
                            xysize (40,40)
                else: 
                    null height 36
                if roundEndlPoints:
                    hbox:
                        text "[f'{roundlPoints:.2f}']" style "lightPointsStyle"
                        add "order bone.png":
                            fit "scale-down"
                            xysize (40,40)
                else: 
                    null height 38

        null width 50

        frame:
            padding(30, 20)
            background "scoreBox"
            vbox:
                xysize (250, 800)
                text "Total Points:"
                if roundEndTotalrPoints:
                    hbox:
                        text "[f'{rPoints:.2f}']" style "redPointsStyle"
                        add "order meat.png":
                            fit "scale-down"
                            xysize (40,40)
                else: 
                    null height 36
                if roundEndTotalbPoints:
                    hbox:
                        text "[f'{bPoints:.2f}']" style "bluePointsStyle"
                        add "order weapon.png":
                            fit "scale-down"
                            xysize (40,40)
                else: 
                    null height 36
                if roundEndTotalyPoints:
                    hbox:
                        text "[f'{yPoints:.2f}']" style "yellowPointsStyle"
                        add "order treasure.png":
                            fit "scale-down"
                            xysize (40,40)
                else: 
                    null height 36
                if roundEndTotalgPoints:
                    hbox:
                        text "[f'{gPoints:.2f}']" style "greenPointsStyle"
                        add "order sleep.png":
                            fit "scale-down"
                            xysize (40,40)
                else: 
                    null height 36
                if roundEndTotaloPoints:
                    hbox:
                        text "[f'{oPoints:.2f}']" style "orangePointsStyle"
                        add "order light.png":
                            fit "scale-down"
                            xysize (40,40)
                else: 
                    null height 36
                if roundEndTotalvPoints:
                    hbox:
                        text "[f'{vPoints:.2f}']" style "violetPointsStyle"
                        add "order fish.png":
                            fit "scale-down"
                            xysize (40,40)
                else: 
                    null height 36
                if roundEndTotalpPoints:
                    hbox:
                        text "[f'{pPoints:.2f}']" style "pinkPointsStyle"
                        add "order keys.png":
                            fit "scale-down"
                            xysize (40,40)
                else: 
                    null height 36
                if roundEndTotallPoints:
                    hbox:
                        text "[f'{lPoints:.2f}']" style "lightPointsStyle"
                        add "order bone.png":
                            fit "scale-down"
                            xysize (40,40)
                else: 
                    null height 36


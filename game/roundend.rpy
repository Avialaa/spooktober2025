
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


label roundEnd:
    #Minigame is concluded by calling this label
    python:
        rPoints += roundrPoints
        bPoints += roundbPoints
        yPoints += roundyPoints
        gPoints += roundgPoints
        oPoints += roundoPoints
        vPoints += roundvPoints
        pPoints += roundpPoints
        lPoints += roundlPoints

        fishTotal += roundpPoints

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
            padding(10, 10)
            vbox:
                xysize (250, 600)
                text "This round:"
                if roundEndrPoints:
                    text "{space=30}{outlinecolor=#000}{color=#ff0000}[roundrPoints]{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndbPoints:
                    text "{space=30}{outlinecolor=#000}{color=#0000ff}[roundbPoints]{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndyPoints:
                    text "{space=30}{outlinecolor=#000}{color=#fbfb00}[roundyPoints]{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndgPoints:
                    text "{space=30}{outlinecolor=#000}{color=#00ff00}[roundgPoints]{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndoPoints:
                    text "{space=30}{outlinecolor=#000}{color=#ffaa00}[roundoPoints]{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndvPoints:
                    text "{space=30}{outlinecolor=#000}{color=#8800fb}[roundvPoints]{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndpPoints:
                    text "{space=30}{outlinecolor=#000}{color=#ee88cc}[roundpPoints]{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndlPoints:
                    text "{space=30}{outlinecolor=#000}{color=#999999}[roundlPoints]{/color}{/outlinecolor}"
                else: 
                    null height 39

        null width 50

        frame:
            padding(10, 10)
            vbox:
                xysize (250, 600)
                text "Total Points:"
                if roundEndTotalrPoints:
                    text "{space=30}{outlinecolor=#000}{color=#ff0000}[rPoints]{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndTotalbPoints:
                    text "{space=30}{outlinecolor=#000}{color=#0000ff}[bPoints]{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndTotalyPoints:
                    text "{space=30}{outlinecolor=#000}{color=#fbfb00}[yPoints]{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndTotalgPoints:
                    text "{space=30}{outlinecolor=#000}{color=#00ff00}[gPoints]{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndTotaloPoints:
                    text "{space=30}{outlinecolor=#000}{color=#ffaa00}[oPoints]{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndTotalvPoints:
                    text "{space=30}{outlinecolor=#000}{color=#8800fb}[vPoints]{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndTotalpPoints:
                    text "{space=30}{outlinecolor=#000}{color=#ee88cc}[pPoints]{/color}{/outlinecolor}"
                else: 
                    null height 39
                if roundEndTotallPoints:
                    text "{space=30}{outlinecolor=#000}{color=#999999}[lPoints]{/color}{/outlinecolor}"
                else: 
                    null height 39


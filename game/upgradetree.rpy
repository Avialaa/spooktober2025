init:
    image upgradeBox = Frame("minigame button score.png", 40, 30)
    image upgradeBox2 = Frame("minigame button basic.png", 40, 30)
    image upgradeBox3 = Frame("minigame button pressed.png", 40, 30)
    image upgradeBox4 = Frame("minigame button allbought.png", 40, 30)

    #image meatMini = 
    #image weaponMini
    #image treasureMini
    #image sleepMini
    #image lightMini
    #image fishMini
    #image keysMini
    #image boneMini

default firstDay = True

default rPoints = 0
default bPoints = 0
default yPoints = 0
default oPoints = 0
default gPoints = 0
default vPoints = 0
default pPoints = 0
default lPoints = 0

default orderrPoints = 0
default orderbPoints = 0
default orderyPoints = 0
default orderoPoints = 0
default ordergPoints = 0
default ordervPoints = 0
default orderpPoints = 0
default orderlPoints = 0

default roundrPoints = 0
default roundbPoints = 0
default roundyPoints = 0
default roundoPoints = 0
default roundgPoints = 0
default roundvPoints = 0
default roundpPoints = 0
default roundlPoints = 0

default rPointValue = 1
default bPointValue = 1
default yPointValue = 1
default oPointValue = 1
default gPointValue = 1
default vPointValue = 1
default pPointValue = 1
default lPointValue = 1

default upgradesBought = {}

default focusUpgradeName = "0"
default focusDescription = ""
default focusUpgradeID = ""
default focusupgradeLimit = 1
default frCost = 0
default fbCost = 0
default fyCost = 0
default fgCost = 0
default foCost = 0
default fvCost = 0
default fpCost = 0
default flCost = 0

default orderCounter = dict()
default itemCountDict = dict()
default itemCountList = []
default itemValueDict = {"light": 1, "sleep": 1, "fish": 1, "bone": 1, "meat": 1, "weapon": 1, "keys": 1, "treasure": 1}
default tier2ValueDict = {"light": 1, "sleep": 1, "fish": 1, "bone": 1, "meat": 1, "weapon": 1, "keys": 1, "treasure": 1}
default tier3ValueDict = {"light": 1, "sleep": 1, "fish": 1, "bone": 1, "meat": 1, "weapon": 1, "keys": 1, "treasure": 1}
default tier2ChanceDict = {"light": 0, "sleep": 0, "fish": 0, "bone": 0, "meat": 0, "weapon": 0, "keys": 0, "treasure": 0}
default tier3ChanceDict = {"light": 0, "sleep": 0, "fish": 0, "bone": 0, "meat": 0, "weapon": 0, "keys": 0, "treasure": 0}

default failPoints = 0
default validityFactor = 0
default timerPoints = 0

init python:

    def upgradePurchase():
        #is run when an upgrade is bought

        global focusUpgradeID
        global focusUpgradeLimit
        global upgradesBought
        global rPoints
        global bPoints
        global yPoints
        global gPoints
        global oPoints
        global vPoints
        global pPoints
        global lPoints
        global frCost
        global fbCost
        global fyCost
        global fgCost
        global foCost
        global fvCost
        global fpCost
        global flCost

        global itemValueDict
        global tier2ValueDict
        global tier3ValueDict
        global tier2ChanceDict
        global tier3ChanceDict
        global roundDuration
        global timerPoints
        global sleepTimerPoints
        global failPoints

        #subtracts upgrade cost from points
        rPoints += -frCost
        bPoints += -fbCost
        yPoints += -fyCost
        gPoints += -fgCost
        oPoints += -foCost
        vPoints += -fvCost
        pPoints += -fpCost
        lPoints += -flCost

        #adds bought upgrade into dict that tracks bought upgrades
        if focusUpgradeID not in upgradesBought:
            upgradesBought.update({focusUpgradeID: 1})
        else:
            upgradesBought[focusUpgradeID] +=1
        
        upgradeUpdate() #update variables
        
        #update buy screen prices after purchase
        frCost = frCost*2
        fbCost = fbCost*2
        fyCost = fyCost*2
        fgCost = fgCost*2
        foCost = foCost*2
        fvCost = fvCost*2
        fpCost = fpCost*2
        flCost = flCost*2

    def upgradeUpdate():
        #updates relevant variables after upgrade purchase

        global frCost
        global fbCost
        global fyCost
        global fgCost
        global foCost
        global fvCost
        global fpCost
        global flCost

        global roundDuration
        global timerPoints
        global sleepTimerPoints
        global failPoints
        global maxBoxItems
        global conveyerSpeed
        global conveyerInterval
        
        itemValueDict["light"] = (1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("lightMultiplier",0)))
        itemValueDict["sleep"] = (1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("sleepMultiplier",0)))
        itemValueDict["fish"] = (1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("fishMultiplier",0)))
        itemValueDict["bone"] = (1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("boneMultiplier",0)))
        itemValueDict["meat"] = (1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("meatMultiplier",0)))
        itemValueDict["weapon"] = (1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("weaponMultiplier",0)))
        itemValueDict["keys"] = (1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("keysMultiplier",0)))
        itemValueDict["treasure"] = (1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("treasureMultiplier",0)))
        
        tier2ValueDict["light"] = 10*(1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("light2Multiplier",0)))*(1.2**float(upgradesBought.get("lightMultiplier",0)))
        tier2ValueDict["sleep"] = 10*(1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("sleep2Multiplier",0)))*(1.2**float(upgradesBought.get("sleepMultiplier",0)))
        tier2ValueDict["fish"] = 10*(1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("fish2Multiplier",0)))*(1.2**float(upgradesBought.get("fishMultiplier",0)))
        tier2ValueDict["bone"] = 10*(1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("bone2Multiplier",0)))*(1.2**float(upgradesBought.get("boneMultiplier",0)))
        tier2ValueDict["meat"] = 10*(1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("meat2Multiplier",0)))*(1.2**float(upgradesBought.get("meatMultiplier",0)))
        tier2ValueDict["weapon"] = 10*(1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("weapon2Multiplier",0)))*(1.2**float(upgradesBought.get("weaponMultiplier",0)))
        tier2ValueDict["keys"] = 10*(1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("keys2Multiplier",0)))*(1.2**float(upgradesBought.get("keysMultiplier",0)))
        tier2ValueDict["treasure"] = 10*(1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("treasure2Multiplier",0)))*(1.2**float(upgradesBought.get("treasureMultiplier",0)))
        
        tier3ValueDict["light"] = 100*(1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("light3Multiplier",0)))*(1.2**float(upgradesBought.get("lightMultiplier",0)))
        tier3ValueDict["sleep"] = 100*(1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("sleep3Multiplier",0)))*(1.2**float(upgradesBought.get("sleepMultiplier",0)))
        tier3ValueDict["fish"] = 100*(1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("fish3Multiplier",0)))*(1.2**float(upgradesBought.get("fishMultiplier",0)))
        tier3ValueDict["bone"] = 100*(1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("bone3Multiplier",0)))*(1.2**float(upgradesBought.get("boneMultiplier",0)))
        tier3ValueDict["meat"] = 100*(1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("meat3Multiplier",0)))*(1.2**float(upgradesBought.get("meatMultiplier",0)))
        tier3ValueDict["weapon"] = 100*(1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("weapon3Multiplier",0)))*(1.2**float(upgradesBought.get("weaponMultiplier",0)))
        tier3ValueDict["keys"] = 100*(1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("keys3Multiplier",0)))*(1.2**float(upgradesBought.get("keysMultiplier",0)))
        tier3ValueDict["treasure"] = 100*(1.2**float(upgradesBought.get("pointMultiplier",0)))*(1.2**float(upgradesBought.get("treasure3Multiplier",0)))*(1.2**float(upgradesBought.get("treasureMultiplier",0)))
        
        tier2ChanceDict["light"] = upgradesBought.get("light2Chance",0)
        tier2ChanceDict["sleep"] = upgradesBought.get("sleep2Chance",0)
        tier2ChanceDict["fish"] = upgradesBought.get("fish2Chance",0)
        tier2ChanceDict["bone"] = upgradesBought.get("bone2Chance",0)
        tier2ChanceDict["meat"] = upgradesBought.get("meat2Chance",0)
        tier2ChanceDict["weapon"] = upgradesBought.get("weapon2Chance",0)
        tier2ChanceDict["keys"] = upgradesBought.get("keys2Chance",0)
        tier2ChanceDict["treasure"] = upgradesBought.get("treasure2Chance",0)
        
        tier3ChanceDict["light"] = upgradesBought.get("light3Chance",0)
        tier3ChanceDict["sleep"] = upgradesBought.get("sleep3Chance",0)
        tier3ChanceDict["fish"] = upgradesBought.get("fish3Chance",0)
        tier3ChanceDict["bone"] = upgradesBought.get("bone3Chance",0)
        tier3ChanceDict["meat"] = upgradesBought.get("meat3Chance",0)
        tier3ChanceDict["weapon"] = upgradesBought.get("weapon3Chance",0)
        tier3ChanceDict["keys"] = upgradesBought.get("keys3Chance",0)
        tier3ChanceDict["treasure"] = upgradesBought.get("treasure3Chance",0)

        roundDuration = 80+(10*upgradesBought.get("timeIncrease",0)) #increase round time by 10 seconds per round time upgrade
        timerPoints = (roundDuration/10)*upgradesBought.get("timePoints",0) #every second gives 0.1 of eachpoint per bought timer point upgrade
        sleepTimerPoints = roundDuration*upgradesBought.get("sleepTimePoints",0) #every second gives 1 green point per bought timer sleep point upgrade
        roundDuration = roundDuration/(2**upgradesBought.get("timePace",0)) #halves round duration without affecting timer points for each time pace upgrade bought
        if "noTime"  in upgradesBought:
            roundDuration = 0.1
        failPoints = upgradesBought.get("failPoint",0)*0.1
        maxBoxItems = 6+upgradesBought.get("box",0) 
        conveyerSpeed = 5.0*(0.9**upgradesBought.get("speed",0))
        conveyerInterval = 1.0*(0.9**upgradesBought.get("interval",0))*(conveyerSpeed/5)
        validityFactor = 1.1**upgradesBought.get("fault",0)-1

    def openShop(name, upgradeID, upgradeLimit, rCost, bCost, yCost, gCost, oCost, vCost, pCost, lCost, description):
        #function that is run when upgrade node is clicked

        global focusUpgradeID
        global focusUpgradeLimit
        global upgradesBought
        global frCost
        global fbCost
        global fyCost
        global fgCost
        global foCost
        global fvCost
        global fpCost
        global flCost
        global focusDescription

        focusUpgradeName = name
        focusUpgradeID = upgradeID
        focusUpgradeLimit = upgradeLimit
        frCost = rCost
        fbCost = bCost
        fyCost = yCost
        fgCost = gCost
        foCost = oCost
        fvCost = vCost
        fpCost = pCost
        flCost = lCost
        focusDescription = description

label upgradetreeTest:
    python:
        rPoints = 200
        bPoints = 200
        yPoints = 200
        gPoints = 200
        oPoints = 200
        vPoints = 200
        pPoints = 200
        lPoints = 200
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
    call upgradeTree
    call warehouse_gameplay
    call roundEnd
    call after_minigame
    call upgradeTree
    call warehouse_gameplay
    call roundEnd
    call after_minigame
    return

label upgradeTree:
    if workShift == 1 or workShift == 2:
        scene bg warehouse
    elif workShift == 3 or workShift == 4 or workShift == 5:
        scene bg warehouse posters
    else: 
        scene bg warehouse

    "Time for another shift!"
    if _skipping:
        hide screen skip_indicator
        $ renpy.choice_for_skipping()
        $ _skipping = False
    $ renpy.config.skipping = False
    $ config.rollback_enabled = False
    python:
        if firstDay:
            if rPoints == 0:
                rPoints +=1
            if bPoints == 0:
                bPoints +=1
            if yPoints == 0:
                yPoints +=1
            if gPoints == 0:
                gPoints +=1
            if oPoints == 0:
                oPoints +=1
            if vPoints == 0:
                vPoints +=1
            if pPoints == 0:
                pPoints +=1
            if lPoints == 0:
                lPoints +=1
            firstDay = False

        quick_menu = False
    play music ilo
    call screen upgradeTree

    return

screen upgradeNode(name, upgradeID, upgradeLimit, coord, rCost, bCost, yCost, gCost, oCost, vCost, pCost, lCost, description):
    #button type for upgrade nodes in upgrade tree
    button:
        align coord
        if upgradesBought.get(upgradeID) == upgradeLimit:
            background Frame("minigame button allbought.png", 40, 30)
        elif not (rPoints >= rCost and bPoints >= bCost and yPoints >= yCost and gPoints >= gCost and oPoints >= oCost and vPoints >= vCost and pPoints >= pCost and lPoints >= lCost):
            background Frame("minigame button nomoney.png", 40, 30)
        elif upgradeID in upgradesBought:
            background Frame("minigame button bought.png", 40, 30)
        elif focusUpgradeName == name:
            background Frame("minigame button pressed.png", 40, 30)
        else:
            background Frame("minigame button basic.png", 40, 30)
        if focusUpgradeName == name:
            padding (25, 12)
        else:
            padding (20,10)
        text name:
            font "Silkscreen-Regular.ttf"
            if upgradesBought.get(upgradeID) == upgradeLimit:
                color("#5A6056")
            if not (rPoints >= rCost and bPoints >= bCost and yPoints >= yCost and gPoints >= gCost and oPoints >= oCost and vPoints >= vCost and pPoints >= pCost and lPoints >= lCost):
                color("#654C4C")
            elif upgradeID in upgradesBought:
                color("#4C5942")
            elif focusUpgradeName == name:
                color("#2A3124")
            else:
                color("#4C5942")
        if focusUpgradeID == upgradeID and rPoints >= frCost and bPoints >= fbCost and yPoints >= fyCost and gPoints >= fgCost and oPoints >= foCost and vPoints >= fvCost and pPoints >= fpCost and lPoints >= flCost and upgradesBought.get(focusUpgradeID,0) < focusUpgradeLimit:
            action [Function(upgradePurchase), Play('sound', 'click_kwahmah_02__click.mp3')]
        else:
            action [Function(openShop, name, upgradeID, upgradeLimit, rCost, bCost, yCost, gCost, oCost, vCost, pCost, lCost, description, _update_screens=True), SetVariable("focusUpgradeName", name)]


screen pointView:
    vbox:
        xalign 0.01
        yalign 0.01
        spacing 10
        frame:
            background "upgradeBox"
            padding (20, 10)
            hbox:
                spacing 2
                text "[f'{rPoints:.2f}']" style "redPointsStyle":
                    yoffset 25
                add "order meat.png"
        frame:
            background "upgradeBox"
            padding (20, 10)
            hbox:
                spacing 2
                box_align 0.5
                text "[f'{bPoints:.2f}']" style "bluePointsStyle":
                    yoffset 25
                add "order weapon.png"
        frame:
            background "upgradeBox"
            padding (20, 10)
            hbox:
                spacing 2
                box_align 0.5
                text "[f'{yPoints:.2f}']" style "yellowPointsStyle":
                    yoffset 25
                add "order treasure.png"
        frame:
            background "upgradeBox"
            padding (20, 10)
            hbox:
                spacing 2
                box_align 0.5
                text "[f'{gPoints:.2f}']" style "greenPointsStyle":
                    yoffset 25
                add "order sleep.png"
        frame:
            background "upgradeBox"
            padding (20, 10)
            hbox:
                spacing 2
                box_align 0.5
                text "[f'{oPoints:.2f}']" style "orangePointsStyle":
                    yoffset 25
                add "order light.png"
        frame:
            background "upgradeBox"
            padding (20, 10)
            hbox:
                spacing 2
                box_align 0.5
                text "[f'{vPoints:.2f}']" style "violetPointsStyle":
                    yoffset 25
                add "order fish.png"
        frame:
            background "upgradeBox"
            padding (20, 10)
            has hbox:
                spacing 2
                text "[f'{pPoints:.2f}']" style "pinkPointsStyle":
                    yoffset 25
                add "order keys.png"
        frame:
            background "upgradeBox"
            padding (20, 10)
            hbox:
                spacing 2
                box_align 0.5
                text "[f'{lPoints:.2f}']" style "lightPointsStyle":
                    yoffset 25
                add "order bone.png"

screen upgradeTree:
    #add "bigspace_day.png"
    modal True

    text "{size=+7}{color=#ddd}Workshop Upgrades":
        align (0.5,0.001)
    
    #return button
    frame:
        background "upgradeBox"
        padding (20,10)
        xalign 0.5
        yalign 0.999
        textbutton "{color=#ddd}{size=+9}Done":
            action [SetVariable("focusUpgradeName", "0"), SetVariable("focusUpgradeID", "0"), Return()]

    #viewport for upgrade nodes

    side 'c b r':
        xysize (1200, 900)
        align (0.37, 0.38)
        frame:
            margin (0,0)
            viewport:
                xysize (1200, 900)
                child_size (4000,2000)
                draggable True
                xinitial 0.47
                yinitial 0.5
                arrowkeys True
                pagekeys True
                mousewheel True
                id "zoom_vp"

                #upgradenodes are here
                fixed:
                    xfit False
                    yfit False
                    use upgradeNode("Point +","pointMultiplier", 30, (0.5, 0.5), 1*(2**upgradesBought.get("pointMultiplier",0)), 1*(2**upgradesBought.get("pointMultiplier",0)), 1*(2**upgradesBought.get("pointMultiplier",0)), 1*(2**upgradesBought.get("pointMultiplier",0)), 1*(2**upgradesBought.get("pointMultiplier",0)), 1*(2**upgradesBought.get("pointMultiplier",0)), 1*(2**upgradesBought.get("pointMultiplier",0)), 1*(2**upgradesBought.get("pointMultiplier",0)), "Increases all point gain by 20%")
                    #regular point multipliers
                    if 'pointMultiplier' in upgradesBought:
                        use upgradeNode("Meat +","meatMultiplier", 30, (0.444, 0.465), 1*(2**upgradesBought.get("meatMultiplier",0)), 0, 0, 0, 0, 0, 0, 0, "Increases all points gained from meat items by 20%")
                    if 'pointMultiplier' in upgradesBought:
                        use upgradeNode("{size=-2}Lantern +","lightMultiplier", 30, (0.5, 0.465), 0, 0, 0, 0, 1*(2**upgradesBought.get("lightMultiplier",0)), 0, 0, 0, "Increases all points gained from lantern items by 20%") 
                    if 'pointMultiplier' in upgradesBought:
                        use upgradeNode("Coin +","treasureMultiplier", 30, (0.556, 0.465), 0, 0, 1*(2**upgradesBought.get("treasureMultiplier",0)), 0, 0, 0, 0, 0, "Increases all points gained from coin items by 20%")
                    if 'pointMultiplier' in upgradesBought:
                        use upgradeNode("Key +","keysMultiplier", 30, (0.444, 0.5), 0, 0, 0, 0, 0, 0, 1*(2**upgradesBought.get("keysMultiplier",0)), 0, "Increases all points gained from key items by 20%")
                    if 'pointMultiplier' in upgradesBought:
                        use upgradeNode("Bone +","boneMultiplier", 30, (0.556, 0.5), 0, 0, 0, 0, 0, 0, 0, 1*(2**upgradesBought.get("boneMultiplier",0)), "Increases all points gained from bone items by 20%")
                    if 'pointMultiplier' in upgradesBought:
                        use upgradeNode("Fish +","fishMultiplier", 30, (0.444, 0.535), 0, 0, 0, 0, 0, 1*(2**upgradesBought.get("fishMultiplier",0)), 0, 0, "Increases all points gained from fish items by 20%")
                    if 'pointMultiplier' in upgradesBought:
                        use upgradeNode("Blade +","weaponMultiplier", 30, (0.5, 0.535), 0, 1*(2**upgradesBought.get("weaponMultiplier",0)), 0, 0, 0, 0, 0, 0, "Increases all points gained from blade items by 20%")
                    if 'pointMultiplier' in upgradesBought:
                        use upgradeNode("Nap +","sleepMultiplier", 30, (0.556, 0.535), 0, 0, 0, 1*(2**upgradesBought.get("sleepMultiplier",0)), 0, 0, 0, 0, "Increases all points gained from nap items by 20%")
                    #tier2
                    if 'meatMultiplier' in upgradesBought:
                        use upgradeNode("Meat 2","meat2Chance", 5, (0.397, 0.43), 3*(2**upgradesBought.get("meat2Chance",0)), 0, 0, 0, 0, 0, 0, 0, "Meat has a +10% chance of appearing as Tier 2 meat with 10 times the point value.")
                    if 'lightMultiplier' in upgradesBought:
                        use upgradeNode("{size=-2}Lantern 2","light2Chance", 5, (0.5, 0.43), 0, 0, 0, 0, 3*(2**upgradesBought.get("light2Chance",0)), 0, 0, 0, "Lantern has a +10% chance of appearing as Tier 2 lantern with 10 times the point value.")
                    if 'treasureMultiplier' in upgradesBought:
                        use upgradeNode("Coin 2","treasure2Chance", 5, (0.611, 0.43), 0, 0, 3*(2**upgradesBought.get("treasure2Chance",0)), 0, 0, 0, 0, 0, "Coin has a +10% chance of appearing as tier 2 coin with 10 times the point value.")
                    if 'keysMultiplier' in upgradesBought:
                        use upgradeNode("Key 2","keys2Chance", 5, (0.397, 0.5), 0, 0, 0, 0, 0, 0, 3*(2**upgradesBought.get("keys2Chance",0)), 0, "Key has a +10% chance of appearing as tier 2 key with 10 times the point value.")
                    if 'boneMultiplier' in upgradesBought:
                        use upgradeNode("Bone 2","bone2Chance", 5, (0.605, 0.5), 0, 0, 0, 0, 0, 0, 0, 3*(2**upgradesBought.get("bone2Chance",0)), "Bone has a +10% chance of appearing as tier 2 bone with 10 times the point value.")
                    if 'fishMultiplier' in upgradesBought:
                        use upgradeNode("Fish 2","fish2Chance", 5, (0.397, 0.57), 0, 0, 0, 0, 0, 3*(2**upgradesBought.get("fish2Chance",0)), 0, 0, "Fish has a +10% chance of appearing as tier 2 fish with 10 times the point value.")
                    if 'weaponMultiplier' in upgradesBought:
                        use upgradeNode("Blade 2","weapon2Chance", 5, (0.5, 0.57), 0, 3*(2**upgradesBought.get("weapon2Chance",0)), 0, 0, 0, 0, 0, 0, "Blade has a +10% chance of appearing as tier 2 blade with 10 times the point value.")
                    if 'sleepMultiplier' in upgradesBought:
                        use upgradeNode("Nap 2","sleep2Chance", 5, (0.605, 0.57), 0, 0, 0, 3*(2**upgradesBought.get("sleep2Chance",0)), 0, 0, 0, 0, "Nap item has a +10% chance of appearing as Tier 2 nap item with 10 times the point value.")
                    #tier2+
                    if 'meat2Chance' in upgradesBought:
                        use upgradeNode("Meat 2+","meat2Multiplier", 15, (0.345, 0.395), 3*(2**upgradesBought.get("meat2Multiplier",0)), 0, 0, 0, 0, 0, 0, 0, "Tier 2 meat point value is increased by 20%.")
                    if 'light2Chance' in upgradesBought:
                        use upgradeNode("{size=-2}Lantern 2+","light2Multiplier", 15, (0.5, 0.395), 0, 0, 0, 0, 3*(2**upgradesBought.get("light2Multiplier",0)), 0, 0, 0, "Tier 2 lantern point value is increased by 20%.")
                    if 'treasure2Chance' in upgradesBought:
                        use upgradeNode("Coin 2+","treasure2Multiplier", 15, (0.658, 0.395), 0, 0, 3*(2**upgradesBought.get("treasure2Multiplier",0)), 0, 0, 0, 0, 0, "Tier 2 coin point value is increased by 20%.")
                    if 'keys2Chance' in upgradesBought:
                        use upgradeNode("Key 2+","keys2Multiplier", 15, (0.345, 0.5), 0, 0, 0, 0, 0, 0, 3*(2**upgradesBought.get("keys2Multiplier",0)), 0, "Tier 2 key point value is increased by 20%.")
                    if 'bone2Chance' in upgradesBought:
                        use upgradeNode("Bone 2+","bone2Multiplier", 15, (0.658, 0.5), 0, 0, 0, 0, 0, 0, 0, 3*(2**upgradesBought.get("bone2Multiplier",0)), "Tier 2 bone point value is increased by 20%.")
                    if 'fish2Chance' in upgradesBought:
                        use upgradeNode("Fish 2+","fish2Multiplier", 15, (0.345, 0.605), 0, 0, 0, 0, 0, 3*(2**upgradesBought.get("fish2Multiplier",0)), 0, 0, "Tier 2 fish point value is increased by 20%.")
                    if 'weapon2Chance' in upgradesBought:
                        use upgradeNode("Blade 2+","weapon2Multiplier", 15, (0.5, 0.605), 0, 3*(2**upgradesBought.get("weapon2Multiplier",0)), 0, 0, 0, 0, 0, 0, "Tier 2 blade point value is increased by 20%.")
                    if 'sleep2Chance' in upgradesBought:
                        use upgradeNode("Nap 2+","sleep2Multiplier", 15, (0.658, 0.605), 0, 0, 0, 3*(2**upgradesBought.get("sleep2Multiplier",0)), 0, 0, 0, 0, "Tier 2 nap item point value is increased by 20%.")
                    #tier3
                    if 'meat2Multiplier' in upgradesBought:
                        use upgradeNode("Meat 3","meat3Chance", 5, (0.295, 0.36), 15*(2**upgradesBought.get("meat3Chance",0)), 0, 0, 0, 0, 0, 0, 0, "Meat has a +10% chance of appearing as Tier 3 meat with 100 times the point value.")
                    if 'light2Multiplier' in upgradesBought:
                        use upgradeNode("{size=-2}Lantern 3","light3Chance", 5, (0.5, 0.36), 0, 0, 0, 0, 15*(2**upgradesBought.get("light3Chance",0)), 0, 0, 0, "Lantern has a +10% chance of appearing as Tier 3 lantern with 100 times the point value.")
                    if 'treasure2Multiplier' in upgradesBought:
                        use upgradeNode("Coin 3","treasure3Chance", 5, (0.71, 0.36), 0, 0, 15*(2**upgradesBought.get("treasure3Chance",0)), 0, 0, 0, 0, 0, "Coin has a +10% chance of appearing as Tier 3 coin with 100 times the point value.")
                    if 'keys2Multiplier' in upgradesBought:
                        use upgradeNode("Key 3","keys3Chance", 5, (0.295, 0.5), 0, 0, 0, 0, 0, 0, 15*(2**upgradesBought.get("keys3Chance",0)), 0, "Key has a +10% chance of appearing as Tier 3 key with 100 times the point value.")
                    if 'bone2Multiplier' in upgradesBought:
                        use upgradeNode("Bone 3","bone3Chance", 5, (0.71, 0.5), 0, 0, 0, 0, 0, 0, 0, 15*(2**upgradesBought.get("bone3Chance",0)), "Bone has a +10% chance of appearing as Tier 3 bone with 100 times the point value.")
                    if 'fish2Multiplier' in upgradesBought:
                        use upgradeNode("Fish 3","fish3Chance", 5, (0.295, 0.64), 0, 0, 0, 0, 0, 15*(2**upgradesBought.get("fish3Chance",0)), 0, 0, "Fish has a +10% chance of appearing as Tier 3 fish with 100 times the point value.")
                    if 'weapon2Multiplier' in upgradesBought:
                        use upgradeNode("Blade 3","weapon3Chance", 5, (0.5, 0.64), 0, 15*(2**upgradesBought.get("weapon3Chance",0)), 0, 0, 0, 0, 0, 0, "Blade has a +10% chance of appearing as Tier 3 blade with 100 times the point value.")
                    if 'sleep2Multiplier' in upgradesBought:
                        use upgradeNode("Nap 3","sleep3Chance", 5, (0.71, 0.64), 0, 0, 0, 15*(2**upgradesBought.get("sleep3Chance",0)), 0, 0, 0, 0, "Nap item has a +10% chance of appearing as Tier 3 nap item with 100 times the point value.")
                    #tier3+
                    if 'meat3Chance' in upgradesBought:
                        use upgradeNode("Meat 3+","meat3Multiplier", 15, (0.24, 0.325), 10*(2**upgradesBought.get("meat3Multiplier",0)), 0, 0, 0, 0, 0, 0, 0, "Tier 3 meat point value is increased by 20%.")
                    if 'light3Chance' in upgradesBought:
                        use upgradeNode("{size=-2}Lantern 3+","light3Multiplier", 15, (0.5, 0.325), 0, 0, 0, 0, 10*(2**upgradesBought.get("light3Multiplier",0)), 0, 0, 0, "Tier 3 lantern point value is increased by 20%.")
                    if 'treasure3Chance' in upgradesBought:
                        use upgradeNode("Coin 3+","treasure3Multiplier", 15, (0.765, 0.325), 0, 0, 10*(2**upgradesBought.get("treasure3Multiplier",0)), 0, 0, 0, 0, 0, "Tier 3 coin point value is increased by 20%.")
                    if 'keys3Chance' in upgradesBought:
                        use upgradeNode("Key 3+","keys3Multiplier", 15, (0.24, 0.5), 0, 0, 0, 0, 0, 0, 10*(2**upgradesBought.get("keys3Multiplier",0)), 0, "Tier 3 key point value is increased by 20%.")
                    if 'bone3Chance' in upgradesBought:
                        use upgradeNode("Bone 3+","bone3Multiplier", 15, (0.765, 0.5), 0, 0, 0, 0, 0, 0, 0, 10*(2**upgradesBought.get("bone3Multiplier",0)), "Tier 3 bone point value is increased by 20%.")
                    if 'fish3Chance' in upgradesBought:
                        use upgradeNode("Fish 3+","fish3Multiplier", 15, (0.24, 0.675), 0, 0, 0, 0, 0, 10*(2**upgradesBought.get("fish3Multiplier",0)), 0, 0, "Tier 3 fish point value is increased by 20%.")
                    if 'weapon3Chance' in upgradesBought:
                        use upgradeNode("Blade 3+","weapon3Multiplier", 15, (0.5, 0.675), 0, 10*(2**upgradesBought.get("weapon3Multiplier",0)), 0, 0, 0, 0, 0, 0, "Tier 3 blade point value is increased by 20%.")
                    if 'sleep3Chance' in upgradesBought:
                        use upgradeNode("Nap 3+","sleep3Multiplier", 15, (0.765, 0.675), 0, 0, 0, 10*(2**upgradesBought.get("sleep3Multiplier",0)), 0, 0, 0, 0, "Tier 3 nap item point value is increased by 20%.")
                    #capstone
                    if 'meat3Multiplier' in upgradesBought:
                        use upgradeNode("Supreme Meat","meatCap", 10, (0.16, 0.29), 80*(2**upgradesBought.get("meatCap",0)), 0, 0, 0, 0, 0, 0, 0, "Each point gained from meat gives 0.1 points of every other type.")
                    if 'light3Multiplier' in upgradesBought:
                        use upgradeNode("Supreme Lantern","lightCap", 10, (0.5, 0.29), 0, 0, 0, 0, 80*(2**upgradesBought.get("lightCap",0)), 0, 0, 0, "Each point gained from lanterns gives 0.1 points of every other type.")
                    if 'treasure3Multiplier' in upgradesBought:
                        use upgradeNode("Supreme Coin","treasureCap", 10, (0.845, 0.29), 0, 0, 80*(2**upgradesBought.get("treasureCap",0)), 0, 0, 0, 0, 0, "Each point gained from coin gives 0.1 points of every other type.")
                    if 'keys3Multiplier' in upgradesBought:
                        use upgradeNode("Supreme Key","keysCap", 10, (0.16, 0.5), 0, 0, 0, 0, 0, 0, 80*(2**upgradesBought.get("keysCap",0)), 0, "Each point gained from keys gives 0.1 points of every other type.")
                    if 'bone3Multiplier' in upgradesBought:
                        use upgradeNode("Supreme Bone","boneCap", 10, (0.845, 0.5), 0, 0, 0, 0, 0, 0, 0, 80*(2**upgradesBought.get("boneCap",0)), "Each point gained from bone gives 0.1 points of every other type.")
                    if 'fish3Multiplier' in upgradesBought:
                        use upgradeNode("Supreme Fish","fishCap", 10, (0.16, 0.71), 0, 0, 0, 0, 0, 80*(2**upgradesBought.get("fishCap",0)), 0, 0, "Each point gained from fish gives 0.1 points of every other type.")
                    if 'weapon3Multiplier' in upgradesBought:
                        use upgradeNode("Supreme Blade","weaponCap", 10, (0.5, 0.71), 0, 80*(2**upgradesBought.get("weaponCap",0)), 0, 0, 0, 0, 0, 0, "Each point gained from blades gives 0.1 points of every other type.")
                    if 'sleep3Multiplier' in upgradesBought:
                        use upgradeNode("Supreme Nap","sleepCap", 10, (0.845, 0.71), 0, 0, 0, 80*(2**upgradesBought.get("sleepCap",0)), 0, 0, 0, 0, "Each point gained from nap items gives 0.1 points of every other type.")
                    #combo
                    if 'sleepMultiplier' in upgradesBought and 'boneMultiplier' in upgradesBought:
                        use upgradeNode("{size=-9}Rot Combo","glCombo", 15, (0.605, 0.535), 0, 0, 0, 1*(2**upgradesBought.get("glCombo",0)), 0, 0, 0, 1*(2**upgradesBought.get("glCombo",0)), "Bones and nap items get a +10% bonus from each other.")
                    if 'sleepMultiplier' in upgradesBought and 'weaponMultiplier' in upgradesBought:
                        use upgradeNode("{size=-9}Death Combo","gbCombo", 15, (0.556, 0.57), 0, 1*(2**upgradesBought.get("gbCombo",0)), 0, 1*(2**upgradesBought.get("gbCombo",0)), 0, 0, 0, 0, "Blades and nap items get a +10% bonus from each other.")
                    if 'fishMultiplier' in upgradesBought and 'weaponMultiplier' in upgradesBought:
                        use upgradeNode("{size=-9}Sushi Combo","vbCombo", 15, (0.4455, 0.57), 0, 1*(2**upgradesBought.get("vbCombo",0)), 0, 0, 0, 1*(2**upgradesBought.get("vbCombo",0)), 0, 0, "Blades and fish get a +10% bonus from each other.")
                    if 'fishMultiplier' in upgradesBought and 'keysMultiplier' in upgradesBought:
                        use upgradeNode("{size=-9}Deep Combo","vpCombo", 15, (0.392, 0.535), 0, 0, 0, 0, 0, 1*(2**upgradesBought.get("vpCombo",0)), 1*(2**upgradesBought.get("vpCombo",0)), 0, "Keys and fish and nap items get a +10% bonus from each other.")
                    if 'meatMultiplier' in upgradesBought and 'keysMultiplier' in upgradesBought:
                        use upgradeNode("{size=-9}Taste Combo","rpCombo", 15, (0.39, 0.465), 1*(2**upgradesBought.get("rpCombo",0)), 0, 0, 0, 0, 0, 1*(2**upgradesBought.get("rpCombo",0)), 0, "Keys and meat get a +10% bonus from each other.")
                    if 'meatMultiplier' in upgradesBought and 'lightMultiplier' in upgradesBought:
                        use upgradeNode("{size=-9}Fry Combo","roCombo", 15, (0.444, 0.43), 1*(2**upgradesBought.get("roCombo",0)), 0, 0, 0, 1*(2**upgradesBought.get("roCombo",0)), 0, 0, 0, "Lanterns and meat get a +10% bonus from each other.")
                    if 'treasureMultiplier' in upgradesBought and 'lightMultiplier' in upgradesBought:
                        use upgradeNode("{size=-9}Shine Combo","yoCombo", 15, (0.561, 0.43), 0, 0, 1*(2**upgradesBought.get("yoCombo",0)), 0, 1*(2**upgradesBought.get("yoCombo",0)), 0, 0, 0, "Lanterns and coins get a +10% bonus from each other.")
                    if 'treasureMultiplier' in upgradesBought and 'boneMultiplier' in upgradesBought:
                        use upgradeNode("{size=-9}Greed Combo","ylCombo", 15, (0.61, 0.465), 0, 0, 1*(2**upgradesBought.get("ylCombo",0)), 0, 0, 0, 0, 1*(2**upgradesBought.get("ylCombo",0)), "Bones and coins get a +10% bonus from each other.")

                    #Karkhos upgrades
                    if 'sleep2Chance' in upgradesBought:
                        use upgradeNode("Slack","timePoints", 10, (0.657, 0.57), 0, 0, 0, 10*(2**upgradesBought.get("timePoints",0)), 0, 0, 0, 0, "Every second gain +0.1 of every point type during shift.")
                    if 'sleep2Chance' in upgradesBought:
                        use upgradeNode("Haphazard","fault", 10, (0.603, 0.605), 0, 0, 0, 10*(2**upgradesBought.get("fault",0)), 0, 0, 0, 0, "Gain +10% of the points from invalid orders.")
                    if 'sleep2Multiplier' in upgradesBought and 'timePoints' in upgradesBought:
                        use upgradeNode("Snore","sleepTimePoint", 10, (0.71, 0.605), 0, 0, 0, 10*(2**upgradesBought.get("sleepTimePoints",0)), 0, 0, 0, 0, "Every second gain +1 green point during shift.")
                    if 'sleep3Chance' in upgradesBought and 'timePoints' in upgradesBought:
                        use upgradeNode("Doze","timePace", 10, (0.71, 0.675), 0, 0, 0, 10*(2**upgradesBought.get("timePace",0)), 0, 0, 0, 0, "Makes every shift feel half as long.")
                    if 'sleepCap' in upgradesBought and 'timePace' in upgradesBought:
                        use upgradeNode("Slumber","noTime", 1, (0.91, 0.745), 0, 0, 0, 100, 0, 0, 0, 0, "No work, only points. Skips minigame.")
            
                    #Agatha upgrades
                    if 'light2Chance' in upgradesBought:
                        use upgradeNode("Speed","speed", 5, (0.554, 0.395), 0, 0, 0, 0, 2*(2**upgradesBought.get("speed",0)), 0, 0, 0, "Increase conveyer belt speed by 10%.")
                    if 'light2Multiplier' in upgradesBought and 'speed' in upgradesBought:
                        use upgradeNode("Efficiency","interval", 5, (0.566, 0.36), 0, 0, 0, 0, 3*(2**upgradesBought.get("interval",0)), 0, 0, 0, "Decrease the distance between the items on the conveyor belt by 10%.")
                    if 'light3Chance' in upgradesBought and 'interval' in upgradesBought:
                        use upgradeNode("Overtime","timeIncrease", 10, (0.564, 0.325), 0, 0, 0, 0, 10*(2**upgradesBought.get("timeIncrease",0)), 0, 0, 0, "Increase shift duration by 10 seconds.")
                        
                    #Cee upgrades
                    if 'fish2Chance' in upgradesBought:
                        use upgradeNode("Moist","fishy", 10, (0.345, 0.57), 0, 0, 0, 0, 0, 10*(2**upgradesBought.get("fishy",0)), 0, 0, "All other items also give some fish points.")
                    if 'fish2Multiplier' in upgradesBought and "fishy" in upgradesBought:
                        use upgradeNode("Big Box","box", 10, (0.292, 0.605), 0, 0, 0, 0, 0, 3*(2**upgradesBought.get("box",0)), 0, 0, "Increases box size by one.")
                    if 'fish2Multiplier' in upgradesBought and "box" in upgradesBought:
                        use upgradeNode("Smuggle","fishNumber", 10, (0.24, 0.64), 0, 0, 0, 0, 0, 5*(2**upgradesBought.get("fishNumber",0)), 0, 0, "Each fish is counted as +1 extra fish.")
                    if 'fish3Multiplier' in upgradesBought and "fishNumber" in upgradesBought:
                        use upgradeNode("Bounty of the Sea","bounty", 10, (0.135, 0.675), 0, 0, 0, 0, 0, 10*(2**upgradesBought.get("bounty",0)), 0, 0, "Gain +50 fish points at the end of shift.")

        #scrollbars of the viewport
        bar value XScrollValue("zoom_vp") xalign 0.5
        vbar value YScrollValue("zoom_vp") yalign 0.5

    #point status view
    use pointView

    #buy screen
    if focusUpgradeName != "0":
        frame:
            background "upgradeBox"
            padding (20, 10)
            xalign 0.99
            yalign 0.975
            xmaximum 400
            vbox:
                spacing 10
                text "[focusUpgradeName]":
                    font "fonts/Silkscreen-Regular.ttf"
                text "[focusDescription]":
                    font "fonts/DMSans-Light.ttf"
                hbox:
                    spacing 2
                    text "Cost:" 
                    hbox:
                        box_wrap True
                        spacing 2
                        box_wrap_spacing 2
                        if frCost > 0:
                            hbox:
                                text "[frCost]" style "redPointsStyle"
                                add "order meat.png":
                                    fit "scale-down"
                                    xysize (40,40)
                        if fbCost > 0:
                            hbox:
                                text "[fbCost]" style "bluePointsStyle"
                                add "order weapon.png":
                                    fit "scale-down"
                                    xysize (40,40)
                        if fyCost > 0:
                            hbox:
                                text "[fyCost]" style "yellowPointsStyle"
                                add "order treasure.png":
                                    fit "scale-down"
                                    xysize (40,40)
                        if fgCost > 0:
                            hbox:
                                text "[fgCost]" style "greenPointsStyle"
                                add "order sleep.png":
                                    fit "scale-down"
                                    xysize (40,40)
                        if foCost > 0:
                            hbox:
                                text "[foCost]" style "orangePointsStyle"
                                add "order light.png":
                                    fit "scale-down"
                                    xysize (40,40)
                        if fvCost > 0:
                            hbox:
                                text "[fvCost]" style "violetPointsStyle"
                                add "order fish.png":
                                    fit "scale-down"
                                    xysize (40,40)
                        if fpCost > 0:
                            hbox:
                                text "[fpCost]" style "pinkPointsStyle"
                                add "order keys.png":
                                    fit "scale-down"
                                    xysize (40,40)
                        if flCost > 0:
                            hbox:
                                text "[flCost]" style "lightPointsStyle"
                                add "order bone.png":
                                    fit "scale-down"
                                    xysize (40,40)
                side "r l":
                    xfill True
                    text "[upgradesBought.get(focusUpgradeID,0)]/[focusUpgradeLimit]"
                    frame:
                        if upgradesBought.get(focusUpgradeID) == focusUpgradeLimit:
                            background "upgradeBox4"
                        elif rPoints >= frCost and bPoints >= fbCost and yPoints >= fyCost and gPoints >= fgCost and pPoints >= foCost and vPoints >= fvCost and pPoints >= fpCost and lPoints >= flCost:
                            background "upgradeBox2"
                        else:
                            background "upgradeBox3"
                            
                        padding (20, 10)
                        button:
                            text "Buy":
                                if upgradesBought.get(focusUpgradeID) == focusUpgradeLimit:
                                    color("#5A6056")
                                elif rPoints >= frCost and bPoints >= fbCost and yPoints >= fyCost and gPoints >= fgCost and oPoints >= foCost and vPoints >= fvCost and pPoints >= fpCost and lPoints >= flCost:
                                    color("#2A3124")
                                else:
                                    color("#654C4C")
                                    
                                font "fonts/DMSans-Light.ttf"
                            if rPoints >= frCost and bPoints >= fbCost and yPoints >= fyCost and gPoints >= fgCost and oPoints >= foCost and vPoints >= fvCost and pPoints >= fpCost and lPoints >= flCost and upgradesBought.get(focusUpgradeID,0) < focusUpgradeLimit:
                                action [Function(upgradePurchase), Play('sound', 'click_kwahmah_02__click.mp3')]

screen unused:
    textbutton "upgrade1":
        xalign 0.5
        yalign 0.5
        tooltip "1 red, 1 blue, 1 yellow"
        if redpoints >=1 and bluepoints >=1 and yellowpoints >=1:
            action [IncrementVariable("upgrades"), IncrementVariable("rpoints", amount=-1), SetVariable("upgradevis1", 1)]
    if upgradevis1:
        textbutton "upgrade2":    
            xalign 0.4
            yalign 0.4
            tooltip "1 Redpoint"
            if redpoints >=1:
                action [IncrementVariable("upgrades"), IncrementVariable("rpoints", amount=-1)]    
    
    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]"
    
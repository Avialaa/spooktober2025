init:
    image upgradeBox = Frame("minigame button score.png", 40, 30)
    image upgradeBox2 = Frame("minigame button basic.png", 40, 30)
    image upgradeBox3 = Frame("minigame button pressed.png", 40, 30)
    image upgradeBox3 = Frame("minigame button allbought.png", 40, 30)

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
default tier2ChanceDict = {"light": 1, "sleep": 1, "fish": 1, "bone": 1, "meat": 1, "weapon": 1, "keys": 1, "treasure": 1}
default tier3ChanceDict = {"light": 1, "sleep": 1, "fish": 1, "bone": 1, "meat": 1, "weapon": 1, "keys": 1, "treasure": 1}

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
        
        itemValueDict["light"] = (1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("lightMultiplier",0)))
        itemValueDict["sleep"] = (1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("sleepMultiplier",0)))
        itemValueDict["fish"] = (1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("fishMultiplier",0)))
        itemValueDict["bone"] = (1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("boneMultiplier",0)))
        itemValueDict["meat"] = (1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("meatMultiplier",0)))
        itemValueDict["weapon"] = (1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("weaponMultiplier",0)))
        itemValueDict["keys"] = (1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("keysMultiplier",0)))
        itemValueDict["treasure"] = (1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("treasureMultiplier",0)))
        
        tier2ValueDict["light"] = 10*(1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("light2Multiplier",0)))
        tier2ValueDict["sleep"] = 10*(1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("sleep2Multiplier",0)))
        tier2ValueDict["fish"] = 10*(1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("fish2Multiplier",0)))
        tier2ValueDict["bone"] = 10*(1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("bone2Multiplier",0)))
        tier2ValueDict["meat"] = 10*(1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("meat2Multiplier",0)))
        tier2ValueDict["weapon"] = 10*(1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("weapon2Multiplier",0)))
        tier2ValueDict["keys"] = 10*(1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("keys2Multiplier",0)))
        tier2ValueDict["treasure"] = 10*(1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("treasure2Multiplier",0)))
        
        tier3ValueDict["light"] = 100*(1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("light3Multiplier",0)))
        tier3ValueDict["sleep"] = 100*(1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("sleep3Multiplier",0)))
        tier3ValueDict["fish"] = 100*(1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("fish3Multiplier",0)))
        tier3ValueDict["bone"] = 100*(1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("bone3Multiplier",0)))
        tier3ValueDict["meat"] = 100*(1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("meat3Multiplier",0)))
        tier3ValueDict["weapon"] = 100*(1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("weapon3Multiplier",0)))
        tier3ValueDict["keys"] = 100*(1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("keys3Multiplier",0)))
        tier3ValueDict["treasure"] = 100*(1.1**float(upgradesBought.get("pointMultiplier",0)))*(1.1**float(upgradesBought.get("treasure3Multiplier",0)))
        
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

        roundDuration = (40+5*upgradesBought.get("timeIncrease",0))/(1+upgradesBought.get("timeIncrease",0))
        timerPoints = (roundDuration/5)*upgradesBought.get("timePoints",0) #every 5 seconds gives 1 point
        roundDuration = roundDuration/(2**upgradesBought.get("timePace",0))
        failPoints = upgradesBought.get("pointMultiplier",0)*0,1




    def pointCount():
        #counts points when order is sent

        global orderrPoints
        global orderbPoints
        global orderyPoints
        global orderoPoints
        global ordergPoints
        global ordervPoints
        global orderpPoints
        global orderlPoints

        global roundrPoints
        global roundbPoints
        global roundyPoints
        global roundoPoints
        global roundgPoints
        global roundvPoints
        global roundpPoints
        global roundlPoints

        global itemValueDict
        global tier2ValueDict
        global tier3ValueDict

        global isOrderCorrect

        itemCountList = [] #list is used to count items one tier at a time
        #zeroing the initial point count of the order
        orderrPoints = 0
        orderbPoints = 0
        orderyPoints = 0
        orderoPoints = 0
        ordergPoints = 0
        ordervPoints = 0
        orderpPoints = 0
        orderlPoints = 0
        #adding tier 1 items into the counting list
        for item in itemsInBox:
            if item.tier == 1:
                itemCountList.append(item.name)
        #storing tier 1 item point values into order-specific variables
        orderrPoints = itemCountList.count("meat") * itemValueDict.get("meat")
        orderbPoints = itemCountList.count("weapon") * itemValueDict.get("weapon")
        orderyPoints = itemCountList.count("treasure") * itemValueDict.get("treasure")
        orderoPoints = itemCountList.count("light") * itemValueDict.get("light")
        ordergPoints = itemCountList.count("sleep") * itemValueDict.get("sleep")
        ordervPoints = itemCountList.count("fish") * itemValueDict.get("fish")
        orderpPoints = itemCountList.count("keys") * itemValueDict.get("keys")
        orderlPoints = itemCountList.count("bone") * itemValueDict.get("bone")
        itemCountList = [] #clearing counting list for tier 2 items
        #repeating process for tier 2 items
        for item in itemsInBox:
            if item.tier == 2:
                itemCountList.append(item.name)
        #this time tier 2 point multiplier is applied
        orderrPoints += itemCountList.count("meat") * itemValueDict.get("meat") * tier2ValueDict.get("meat")
        orderbPoints += itemCountList.count("weapon") * itemValueDict.get("weapon") * tier2ValueDict.get("weapon")
        orderyPoints += itemCountList.count("treasure") * itemValueDict.get("treasure") * tier2ValueDict.get("treasure")
        orderoPoints += itemCountList.count("light") * itemValueDict.get("light") * tier2ValueDict.get("light")
        ordergPoints += itemCountList.count("sleep") * itemValueDict.get("sleep") * tier2ValueDict.get("sleep")
        ordervPoints += itemCountList.count("fish") * itemValueDict.get("fish") * tier2ValueDict.get("fish")
        orderpPoints += itemCountList.count("keys") * itemValueDict.get("keys") * tier2ValueDict.get("keys")
        orderlPoints += itemCountList.count("bone") * itemValueDict.get("bone") * tier2ValueDict.get("bone")
        itemCountList = []
        #then the same for tier 3 items
        for item in itemsInBox:
            if item.tier == 3:
                itemCountList.append(item.name)

        orderrPoints += itemCountList.count("meat") * itemValueDict.get("meat") * tier3ValueDict.get("meat")
        orderbPoints += itemCountList.count("weapon") * itemValueDict.get("weapon") * tier3ValueDict.get("weapon")
        orderyPoints += itemCountList.count("treasure") * itemValueDict.get("treasure") * tier3ValueDict.get("treasure")
        orderoPoints += itemCountList.count("light") * itemValueDict.get("light") * tier3ValueDict.get("light")
        ordergPoints += itemCountList.count("sleep") * itemValueDict.get("sleep") * tier3ValueDict.get("sleep")
        ordervPoints += itemCountList.count("fish") * itemValueDict.get("fish") * tier3ValueDict.get("fish")
        orderpPoints += itemCountList.count("keys") * itemValueDict.get("keys") * tier3ValueDict.get("keys")
        orderlPoints += itemCountList.count("bone") * itemValueDict.get("bone") * tier3ValueDict.get("bone")
        
        #checking for order validity and applying point multiplier

        if isOrderCorrect:
            validityFactor = 1
        else:
            validityFactor = failPoints
        
        #adding order point totals into round point count       
        roundrPoints += orderrPoints*validityFactor
        roundbPoints += orderbPoints*validityFactor
        roundyPoints += orderyPoints*validityFactor
        roundoPoints += orderoPoints*validityFactor
        roundgPoints += ordergPoints*validityFactor
        roundvPoints += ordervPoints*validityFactor
        roundpPoints += orderpPoints*validityFactor
        roundlPoints += orderlPoints*validityFactor

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
        frCost = rCost*(2**upgradesBought.get(upgradeID,0))
        fbCost = bCost*(2**upgradesBought.get(upgradeID,0))
        fyCost = yCost*(2**upgradesBought.get(upgradeID,0))
        fgCost = gCost*(2**upgradesBought.get(upgradeID,0))
        foCost = oCost*(2**upgradesBought.get(upgradeID,0))
        fvCost = vCost*(2**upgradesBought.get(upgradeID,0))
        fpCost = pCost*(2**upgradesBought.get(upgradeID,0))
        flCost = lCost*(2**upgradesBought.get(upgradeID,0))
        focusDescription = description


label upgradeCount:
    #label that counts the amount of each type of upgrade bought
    python:
        upgrade1Count = upgradesBought.count('upgrade1')
        upgrade2Count = upgradesBought.count('upgrade2')
        upgrade3Count = upgradesBought.count('upgrade3')
        upgrade4Count = upgradesBought.count('upgrade4')
    "[upgrade1Count] [upgrade2Count] [upgrade3Count] [upgrade4Count]"
    return

label upgradeTreeTest:
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
    if _skipping:
        hide screen skip_indicator
        $ renpy.choice_for_skipping()
        $ _skipping = False
    $ renpy.config.skipping = False
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
    call screen upgradeTree
    return

screen upgradeNode(name, upgradeID, upgradeLimit, coord, rCost, bCost, yCost, gCost, oCost, vCost, pCost, lCost, description):
    #button type for upgrade nodes in upgrade tree
    button:
        align coord
        if not (rPoints >= rCost and bPoints >= bCost and yPoints >= yCost and gPoints >= gCost and oPoints >= oCost and vPoints >= vCost and pPoints >= pCost and lPoints >= lCost):
            background Frame("minigame button nomoney.png", 40, 30)
        elif focusUpgradeName == name:
            background Frame("minigame button pressed.png", 40, 30)
        elif upgradesBought.get(upgradeID) == upgradeLimit:
            background Frame("minigame button allbought.png", 40, 30)
        elif upgradeID in upgradesBought:
            background Frame("minigame button bought.png", 40, 30)
        else:
            background Frame("minigame button basic.png", 40, 30)
        padding (20,10)
        text name:
            font "Silkscreen-Regular.ttf"
            if not (rPoints >= rCost and bPoints >= bCost and yPoints >= yCost and gPoints >= gCost and oPoints >= oCost and vPoints >= vCost and pPoints >= pCost and lPoints >= lCost):
                color("#654C4C")
            elif focusUpgradeName == name:
                color("#2A3124")
            elif upgradesBought.get(upgradeID) == upgradeLimit:
                color("#5A6056")
            elif upgradeID in upgradesBought:
                color("#4C5942")
            else:
                color("#4C5942")

        action [Function(openShop, name, upgradeID, upgradeLimit, rCost, bCost, yCost, gCost, oCost, vCost, pCost, lCost, description, _update_screens=True), SetVariable("focusUpgradeName", name)]


screen pointView:
    vbox:
        xalign 0.01
        yalign 0.01
        spacing 10
        frame:
            background "upgradeBox"
            padding (20, 10)
            text "{outlinecolor=#000}{color=#ff0000}[rPoints]{/color}{/outlinecolor}"
        frame:
            background "upgradeBox"
            padding (20, 10)
            text "{outlinecolor=#000}{color=#0000ff}[bPoints]{/color}{/outlinecolor}"
        frame:
            background "upgradeBox"
            padding (20, 10)
            text "{outlinecolor=#000}{color=#fbfb00}[yPoints]{/color}{/outlinecolor}"
        frame:
            background "upgradeBox"
            padding (20, 10)
            text "{outlinecolor=#000}{color=#00ff00}[gPoints]{/color}{/outlinecolor}"
        frame:
            background "upgradeBox"
            padding (20, 10)
            text "{outlinecolor=#000}{color=#ffaa00}[oPoints]{/color}{/outlinecolor}"
        frame:
            background "upgradeBox"
            padding (20, 10)
            text "{outlinecolor=#000}{color=#8800fb}[vPoints]{/color}{/outlinecolor}"
        frame:
            background "upgradeBox"
            padding (20, 10)
            text "{outlinecolor=#000}{color=#ee88cc}[pPoints]{/color}{/outlinecolor}"
        frame:
            background "upgradeBox"
            padding (20, 10)
            text "{outlinecolor=#000}{color=#999999}[lPoints]{/color}{/outlinecolor}"

screen upgradeTree:
    add "bigspace_day.png"
    modal True

    #point status view
    use pointView
    
    #return button
    frame:
        background "upgradeBox"
        padding (20,10)
        xalign 0.99
        yalign 0.01
        textbutton "Return":
            action [SetVariable("focusUpgradeName", "0"), Return()]

    #upgrade nodes
    use upgradeNode("Point +","pointMultiplier", 5, (0.5, 0.5), 1, 1, 1, 1, 1, 1, 1, 1, "Increases all point gain by 10%")
    if 'pointMultiplier' in upgradesBought:
        use upgradeNode("Meat +","meatMultiplier", 5, (0.35, 0.4), 1, 0, 0, 0, 0, 0, 0, 0, "Increases all points gained from meat items by 10%")
    if 'pointMultiplier' in upgradesBought:
        use upgradeNode("Lantern +","lightMultiplier", 5, (0.5, 0.4), 0, 0, 0, 0, 1, 0, 0, 0, "Increases all points gained from lantern items by 10%") 
    if 'pointMultiplier' in upgradesBought:
        use upgradeNode("Coin +","treasureMultiplier", 5, (0.65, 0.4), 0, 0, 1, 0, 0, 0, 0, 0, "Increases all points gained from coin items by 10%")
    if 'pointMultiplier' in upgradesBought:
        use upgradeNode("Key +","keysMultiplier", 5, (0.35, 0.5), 0, 0, 0, 0, 0, 0, 1, 0, "Increases all points gained from key items by 10%")
    if 'pointMultiplier' in upgradesBought:
        use upgradeNode("Bone +","boneMultiplier", 5, (0.65, 0.5), 0, 0, 0, 0, 0, 0, 0, 1, "Increases all points gained from bone items by 10%")
    if 'pointMultiplier' in upgradesBought:
        use upgradeNode("Fish +","fishMultiplier", 5, (0.35, 0.6), 0, 0, 0, 0, 0, 1, 0, 0, "Increases all points gained from fish items by 10%")
    if 'pointMultiplier' in upgradesBought:
        use upgradeNode("Blade +","weaponMultiplier", 5, (0.5, 0.6), 0, 1, 0, 0, 0, 0, 0, 0, "Increases all points gained from blade items by 10%")
    if 'pointMultiplier' in upgradesBought:
        use upgradeNode("Nap +","sleepMultiplier", 5, (0.65, 0.6), 0, 0, 0, 1, 0, 0, 0, 0, "Increases all points gained from nap items by 10%")
    if 'meatMultiplier' in upgradesBought:
        use upgradeNode("Tier 2 Meat","meat2Chance", 5, (0.2, 0.3), 1, 0, 0, 0, 0, 0, 0, 0, "Meat has a +10%% chance of appearing as Tier 2 Meat with 10 times the point value.")
    if 'lightMultiplier' in upgradesBought:
        use upgradeNode("Tier 2 Lantern","light2Chance", 5, (0.5, 0.3), 0, 0, 0, 0, 1, 0, 0, 0, "Lantern has a +10%% chance of appearing as Tier 2 Lantern with 10 times the point value.")
    if 'goldMultiplier' in upgradesBought:
        use upgradeNode("Tier 2 Meat","treasure2Chance", 5, (0.2, 0.3), 1, 0, 0, 0, 0, 0, 0, 0, "Meat has a +10%% chance of appearing as tier 2 meat with 10 times the point value.")
    if 'meatMultiplier' in upgradesBought:
        use upgradeNode("Tier 2 Meat","keys2Chance", 5, (0.2, 0.3), 1, 0, 0, 0, 0, 0, 0, 0, "Meat has a +10%% chance of appearing as tier 2 meat with 10 times the point value.")
    if 'meatMultiplier' in upgradesBought:
        use upgradeNode("Tier 2 Meat","bone2Chance", 5, (0.2, 0.3), 1, 0, 0, 0, 0, 0, 0, 0, "Meat has a +10%% chance of appearing as tier 2 meat with 10 times the point value.")
    if 'meatMultiplier' in upgradesBought:
        use upgradeNode("Tier 2 Meat","fish2Chance", 5, (0.2, 0.3), 1, 0, 0, 0, 0, 0, 0, 0, "Meat has a +10%% chance of appearing as tier 2 meat with 10 times the point value.")
    if 'meatMultiplier' in upgradesBought:
        use upgradeNode("Tier 2 Meat","weapon2Chance", 5, (0.2, 0.3), 1, 0, 0, 0, 0, 0, 0, 0, "Meat has a +10%% chance of appearing as tier 2 meat with 10 times the point value.")
    if 'meatMultiplier' in upgradesBought:
        use upgradeNode("Tier 2 Meat","sleep2Chance", 5, (0.2, 0.3), 1, 0, 0, 0, 0, 0, 0, 0, "Meat has a +10%% chance of appearing as tier 2 meat with 10 times the point value.")
    if 'meat2Chance' in upgradesBought:
        use upgradeNode("Tier 2 Meat +","meat2Multiplier", 5, (0.1, 0.2), 1, 0, 0, 0, 0, 0, 0, 0, "Meat has a +10%% chance of appearing as tier 2 meat with 10 times the point value.")

    #buy screen
    if focusUpgradeName != "0":
        frame:
            background "upgradeBox"
            padding (20, 10)
            xalign 0.95
            yalign 0.95
            xmaximum 400
            vbox:
                spacing 10
                text "[focusUpgradeName]":
                    font "fonts/Silkscreen-Regular.ttf"
                text "[focusDescription]":
                    font "fonts/DMSans-Light.ttf"
                text "Cost: {outlinecolor=#000}{color=#ff0000}[frCost] {/color}{color=#0000ff}[fbCost] {/color}{color=#fbfb00}[fyCost] {/color}{color=#00ff00}[fgCost] {/color}{color=#ffaa00}[foCost] {/color}{color=#8800fb}[fvCost] {/color}{color=#ee88cc}[fpCost] {/color}{color=#999999}[flCost]{/color}{/outlinecolor}" 
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
                            elif rPoints >= frCost and bPoints >= fbCost and yPoints >= fyCost and gPoints >= fgCost and pPoints >= foCost and vPoints >= fvCost and pPoints >= fpCost and lPoints >= flCost:
                                color("#2A3124")
                            else:
                                color("#654C4C")
                                
                            font "fonts/DMSans-Light.ttf"
                        if rPoints >= frCost and bPoints >= fbCost and yPoints >= fyCost and gPoints >= fgCost and pPoints >= foCost and vPoints >= fvCost and pPoints >= fpCost and lPoints >= flCost and upgradesBought.get(focusUpgradeID,0) < focusUpgradeLimit:
                            action Function(upgradePurchase)

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
    
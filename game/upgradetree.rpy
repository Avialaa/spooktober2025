init:
    image bg upgradetree = "#000"

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

default upgradesBought = []

default focusUpgradeName = "0"
default focusDescription = ""
default focusUpgradeID = ""
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

default failPoints = 0
default validityFactor = 0

init python:

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


label upgradeCount:
    #label that counts the amount of each type of upgrade bought
    python:
        upgrade1Count = upgradesBought.count('upgrade1')
        upgrade2Count = upgradesBought.count('upgrade2')
        upgrade3Count = upgradesBought.count('upgrade3')
        upgrade4Count = upgradesBought.count('upgrade4')
    "[upgrade1Count] [upgrade2Count] [upgrade3Count] [upgrade4Count]"
    return


label upgradeTree:
    $ rPoints +=10
    $ bPoints +=10
    $ yPoints +=10
    $ gPoints +=10
    $ oPoints +=10
    $ vPoints +=10
    $ pPoints +=10
    $ lPoints +=10
    menu upgrade_phase:
        "Upgrade?"

        "Yes":
            $ quick_menu = False
            call screen upgradeTree

        "No":
            pass
    $ quick_menu = True
    "Done"
    return

screen upgradeNode(name, upgradeID, rCost, bCost, yCost, gCost, oCost, vCost, pCost, lCost, description):
    #button type for upgrade nodes in upgrade tree
    button:
        text name:
            if not (rPoints >= rCost and bPoints >= bCost and yPoints >= yCost and gPoints >= gCost and oPoints >= oCost and vPoints >= vCost and pPoints >= pCost and lPoints >= lCost):
                color("#888888")
        action [SetVariable("focusUpgradeName", name), SetVariable("focusUpgradeID", upgradeID), SetVariable("frCost", rCost), SetVariable("fbCost", bCost), SetVariable("fyCost", yCost), SetVariable("fgCost", gCost), SetVariable("foCost", oCost), SetVariable("fvCost", vCost), SetVariable("fpCost", pCost), SetVariable("flCost", lCost), SetVariable("focusDescription", description)]


screen pointView:
    vbox:
        xalign 0.01
        yalign 0.01
        spacing 10
        frame:
            padding (10, 10)
            text "{outlinecolor=#000}{color=#ff0000}[rPoints]{/color}{/outlinecolor}"
        frame:
            padding (10, 10)
            text "{outlinecolor=#000}{color=#0000ff}[bPoints]{/color}{/outlinecolor}"
        frame:
            padding (10, 10)
            text "{outlinecolor=#000}{color=#fbfb00}[yPoints]{/color}{/outlinecolor}"
        frame:
            padding (10, 10)
            text "{outlinecolor=#000}{color=#00ff00}[gPoints]{/color}{/outlinecolor}"
        frame:
            padding (10, 10)
            text "{outlinecolor=#000}{color=#ffaa00}[oPoints]{/color}{/outlinecolor}"
        frame:
            padding (10, 10)
            text "{outlinecolor=#000}{color=#8800fb}[vPoints]{/color}{/outlinecolor}"
        frame:
            padding (10, 10)
            text "{outlinecolor=#000}{color=#ee88cc}[pPoints]{/color}{/outlinecolor}"
        frame:
            padding (10, 10)
            text "{outlinecolor=#000}{color=#999999}[lPoints]{/color}{/outlinecolor}"

screen upgradeTree:
    add "bg upgradetree"
    tag menu
    modal True

    #point status view
    use pointView
    
    #return button
    frame:
        padding (10,10)
        xalign 0.99
        yalign 0.01
        textbutton "Return":
            action [SetVariable("focusUpgradeName", "0"), Return()]

    #upgrade nodes
    frame:
        padding (10,10)
        xalign 0.5
        yalign 0.5
        use upgradeNode("Point +","pointMultiplier", 1, 1, 1, 1, 1, 1, 1, 1, "Increases all point gain by 10%")
    if 'pointMultiplier' in upgradesBought:
        frame:
            padding (10,10)
            xalign 0.35
            yalign 0.4
            use upgradeNode("Meat +","meatMultiplier", 1, 0, 0, 0, 0, 0, 0, 0, "Increases all points gained from meat items by 10%")
    if 'pointMultiplier' in upgradesBought:
        frame:
            padding (10,10)
            xalign 0.5
            yalign 0.4
            use upgradeNode("Lantern +","lightMultiplier", 0, 0, 0, 0, 1, 0, 0, 0, "Increases all points gained from lantern items by 10%")
    if 'pointMultiplier' in upgradesBought:
        frame:
            padding (10,10)
            xalign 0.65
            yalign 0.4
            use upgradeNode("Coin +","goldMultiplier", 0, 0, 1, 0, 0, 0, 0, 0, "Increases all points gained from coin items by 10%")
    if 'pointMultiplier' in upgradesBought:
        frame:
            padding (10,10)
            xalign 0.35
            yalign 0.5
            use upgradeNode("Key +","keysMultiplier", 0, 0, 0, 0, 0, 0, 1, 0, "Increases all points gained from key items by 10%")
    if 'pointMultiplier' in upgradesBought:
        frame:
            padding (10,10)
            xalign 0.65
            yalign 0.5
            use upgradeNode("Bone +","bonesMultiplier", 0, 0, 0, 0, 0, 0, 0, 1, "Increases all points gained from bone items by 10%")
    if 'pointMultiplier' in upgradesBought:
        frame:
            padding (10,10)
            xalign 0.35
            yalign 0.6
            use upgradeNode("Fish +","fishMultiplier", 0, 0, 0, 0, 1, 0, 0, 0, "Increases all points gained from fish items by 10%")
    if 'pointMultiplier' in upgradesBought:
        frame:
            padding (10,10)
            xalign 0.5
            yalign 0.6
            use upgradeNode("Blade +","weaponMultiplier", 0, 1, 0, 0, 0, 0, 0, 0, "Increases all points gained from blade items by 10%")
    if 'pointMultiplier' in upgradesBought:
        frame:
            padding (10,10)
            xalign 0.65
            yalign 0.6
            use upgradeNode("Nap +","sleepMultiplier", 0, 0, 0, 1, 0, 0, 0, 0, "Increases all points gained from nap items by 10%")

    #buy screen
    if focusUpgradeName != "0":
        frame:
            padding (10, 10)
            xalign 0.95
            yalign 0.95
            vbox:
                spacing 10
                text "[focusUpgradeName]"
                text "[focusDescription]"
                text "Cost: {outlinecolor=#000}{color=#ff0000}[frCost] {/color}{color=#0000ff}[fbCost] {/color}{color=#fbfb00}[fyCost] {/color}{color=#00ff00}[fgCost] {/color}{color=#ffaa00}[foCost] {/color}{color=#8800fb}[fvCost] {/color}{color=#ee88cc}[fpCost] {/color}{color=#999999}[flCost]{/color}{/outlinecolor}" 
                frame:
                    padding (10, 10)
                    button:
                        text "Buy"
                        if rPoints >= frCost and bPoints >= fbCost and yPoints >= fyCost and gPoints >= fgCost and pPoints >= foCost and vPoints >= fvCost and pPoints >= fpCost and lPoints >= flCost:
                            action [AddToSet(upgradesBought, focusUpgradeID), IncrementVariable("rPoints", -frCost), IncrementVariable("bPoints", -fbCost), IncrementVariable("yPoints", -fyCost), IncrementVariable("gPoints", -fgCost), IncrementVariable("oPoints", -foCost), IncrementVariable("vPoints", -fvCost), IncrementVariable("pPoints", -fpCost), IncrementVariable("lPoints", -flCost)]

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
    
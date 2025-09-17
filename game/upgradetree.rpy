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
default upgrade1Count = 0
default upgrade2Count = 0
default upgrade3Count = 0
default upgrade4Count = 0

default focusUpgradeName = "0"
default focusDescription = ""
default focusUpgradeID = ""
default frCost = 0
default fbCost = 0
default fyCost = 0

default orderCounter = dict()
default itemCountDict = dict()
default itemCountList = []
default itemValueDict = {"light": 1, "sleep": 1, "fish": 1, "bone": 1, "meat": 1, "weapon": 1, "keys": 1, "treasure": 1}
default tier2ValueDict = {"light": 1, "sleep": 1, "fish": 1, "bone": 1, "meat": 1, "weapon": 1, "keys": 1, "treasure": 1}
default tier3ValueDict = {"light": 1, "sleep": 1, "fish": 1, "bone": 1, "meat": 1, "weapon": 1, "keys": 1, "treasure": 1}


init python:

    def pointCount():
        #counts points when order is sent
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
        itemCountDict= Counter(itemCountList) #tallies items in counting list into a dictionary
        #storing tier 1 item point values into order-specific variables
        orderrPoints = objectCountDict.get("meat") * itemValueDict.get("meat")
        orderbPoints = objectCountDict.get("weapon") * itemValueDict.get("weapon")
        orderyPoints = objectCountDict.get("treasure") * itemValueDict.get("treasure")
        orderoPoints = objectCountDict.get("light") * itemValueDict.get("light")
        ordergPoints = objectCountDict.get("sleep") * itemValueDict.get("sleep")
        ordervPoints = objectCountDict.get("fish") * itemValueDict.get("fish")
        orderpPoints = objectCountDict.get("keys") * itemValueDict.get("keys")
        orderlPoints = objectCountDict.get("bone") * itemValueDict.get("bone")
        itemCountList = [] #clearing counting list for tier 2 items
        #repeating process for tier 2 items
        for item in itemsInBox:
            if item.tier == 2:
                itemCountList.append(item.name)
        itemCountDict= Counter(itemCountList)
        #this time tier 2 point multiplier is applied
        orderrPoints += objectCountDict.get("meat") * itemValueDict.get("meat") * tier2ValueDict.get("meat")
        orderbPoints += objectCountDict.get("weapon") * itemValueDict.get("weapon") * tier2ValueDict.get("weapon")
        orderyPoints += objectCountDict.get("treasure") * itemValueDict.get("treasure") * tier2ValueDict.get("treasure")
        orderoPoints += objectCountDict.get("light") * itemValueDict.get("light") * tier2ValueDict.get("light")
        ordergPoints += objectCountDict.get("sleep") * itemValueDict.get("sleep") * tier2ValueDict.get("sleep")
        ordervPoints += objectCountDict.get("fish") * itemValueDict.get("fish") * tier2ValueDict.get("fish")
        orderpPoints += objectCountDict.get("keys") * itemValueDict.get("keys") * tier2ValueDict.get("keys")
        orderlPoints += objectCountDict.get("bone") * itemValueDict.get("bone") * tier2ValueDict.get("bone")
        itemCountList = []
        #then the same for tier 3 items
        for item in itemsInBox:
            if item.tier == 3:
                itemCountList.append(item.name)
        itemCountDict= Counter(itemCountList)
        orderrPoints += objectCountDict.get("meat") * itemValueDict.get("meat") * tier3ValueDict.get("meat")
        orderbPoints += objectCountDict.get("weapon") * itemValueDict.get("weapon") * tier3ValueDict.get("weapon")
        orderyPoints += objectCountDict.get("treasure") * itemValueDict.get("treasure") * tier3ValueDict.get("treasure")
        orderoPoints += objectCountDict.get("light") * itemValueDict.get("light") * tier3ValueDict.get("light")
        ordergPoints += objectCountDict.get("sleep") * itemValueDict.get("sleep") * tier3ValueDict.get("sleep")
        ordervPoints += objectCountDict.get("fish") * itemValueDict.get("fish") * tier3ValueDict.get("fish")
        orderpPoints += objectCountDict.get("keys") * itemValueDict.get("keys") * tier3ValueDict.get("keys")
        orderlPoints += objectCountDict.get("bone") * itemValueDict.get("bone") * tier3ValueDict.get("bone")
        #adding order point totals into round point count       
        roundrPoints += orderrPoints
        roundbPoints += orderbPoints
        roundyPoints += orderyPoints
        roundoPoints += orderoPoints
        roundgPoints += ordergPoints
        roundvPoints += ordervPoints
        roundpPoints += orderpPoints
        roundlPoints += orderlPoints


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
    $ rPoints +=2
    $ bPoints +=1
    $ yPoints +=1
    menu upgrade_phase:
        "Upgrade?"

        "Yes":
            hide quickmenu
            call screen upgradeTree

        "No":
            pass
    "Done"
    return

screen upgradeNode(name, upgradeID, rCost, bCost, yCost, description):
    #button type for upgrade nodes in upgrade tree
    button:
        text name:
            if not (rPoints >= rCost and bPoints >= bCost and yPoints >= yCost):
                color("#888888")
        action [SetVariable("focusUpgradeName", name), SetVariable("focusUpgradeID", upgradeID), SetVariable("frCost", rCost), SetVariable("fbCost", bCost), SetVariable("fyCost", yCost), SetVariable("focusDescription", description)]





screen upgradeTree:
    add "bg upgradetree"
    tag menu
    modal True


    #point status view
    hbox:
        xalign 0.5
        yalign 0.01
        spacing 10
        frame:
            padding (10, 10)
            text "{outlinecolor=#000}{color=#ff0000}Redpoints: [rPoints]{/color}{/outlinecolor}"
        frame:
            padding (10, 10)
            text "{outlinecolor=#000}{color=#0000ff}Bluepoints: [bPoints]{/color}{/outlinecolor}"
        frame:
            padding (10, 10)
            text "{outlinecolor=#000}{color=#fbfb00}Yellowpoints: [yPoints]{/color}{/outlinecolor}"
        frame:
            padding (10, 10)
            text "Upgrades: [upgradesBought]"
    
    #return button
    frame:
        padding (10,10)
        xalign 0.01
        yalign 0.01
        textbutton "Return":
            action [SetVariable("focusUpgradeName", "0"), Return()]

    #upgrade nodes
    frame:
        padding (10,10)
        xalign 0.5
        yalign 0.5
        use upgradeNode("Upgrade 1","upgrade1", 1, 1, 1, "Lorem ipsum")
    if 'upgrade1' in upgradesBought:
        frame:
            padding (10,10)
            xalign 0.4
            yalign 0.4
            use upgradeNode("Upgrade 2","upgrade2", 1, 0, 0, "Lorem ipsum")
    if 'upgrade1' in upgradesBought:
        frame:
            padding (10,10)
            xalign 0.6
            yalign 0.4
            use upgradeNode("Upgrade 3","upgrade3", 0, 1, 0, "Lorem ipsum")
    if 'upgrade1' in upgradesBought:
        frame:
            padding (10,10)
            xalign 0.6
            yalign 0.6
            use upgradeNode("Upgrade 4","upgrade4", 0, 0, 1, "Lorem ipsum")

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
                text "Cost: {outlinecolor=#000}{color=#ff0000}[frCost] red {/color}{color=#0000ff}[fbCost] blue {/color}{color=#fbfb00}[fyCost] yellow {/color}{/outlinecolor}" 
                frame:
                    padding (10, 10)
                    button:
                        text "Buy"
                        if rPoints >= frCost and bPoints >= fbCost and yPoints >= fyCost:
                            action [AddToSet(upgradesBought, focusUpgradeID), IncrementVariable("rPoints", -frCost), IncrementVariable("bPoints", -fbCost), IncrementVariable("yPoints", -fyCost)]

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
    
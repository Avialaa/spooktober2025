init:
    image bg upgradetree = "#000"

default rPoints = 0
default bPoints = 0
default yPoints = 0

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

label upgradeCount:
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
    
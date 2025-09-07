init:
    image bg upgradetree = "#000"

default rpoints = 0
default bpoints = 0
default ypoints = 0

default upgradesbought = []
default upgrade1 = 0
default upgrade2 = 0

default focusupgradename = "0"
default focusdescription = ""
default focusupgradeid = ""
default frcost = 0
default fbcost = 0
default fycost = 0

label upgradetree:
    $ rpoints +=2
    $ bpoints +=1
    $ ypoints +=1
    menu upgrade_phase:
        "Upgrade?"

        "Yes":
            hide quickmenu
            call screen upgradetree

        "No":
            pass
    "Done"
    return

screen upgradenode(name, upgradeid, rcost, bcost, ycost, description):
    button:
        text name:
            if not (rpoints >= rcost and bpoints >= bcost and ypoints >= ycost):
                color("#888888")
        action [SetVariable("focusupgradename", name), SetVariable("focusupgradeid", upgradeid), SetVariable("frcost", rcost), SetVariable("fbcost", bcost), SetVariable("fycost", ycost), SetVariable("focusdescription", description)]





screen upgradetree:
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
            text "{outlinecolor=#000}{color=#ff0000}Redpoints: [rpoints]{/color}{/outlinecolor}"
        frame:
            padding (10, 10)
            text "{outlinecolor=#000}{color=#0000ff}Bluepoints: [bpoints]{/color}{/outlinecolor}"
        frame:
            padding (10, 10)
            text "{outlinecolor=#000}{color=#fbfb00}Yellowpoints: [ypoints]{/color}{/outlinecolor}"
        frame:
            padding (10, 10)
            text "Upgrades: [upgradesbought]"
    
    #return button
    frame:
        padding (10,10)
        xalign 0.01
        yalign 0.01
        textbutton "Return":
            action [SetVariable("focusupgradename", 0), Return()]

    #upgrade nodes
    frame:
        padding (10,10)
        xalign 0.5
        yalign 0.5
        use upgradenode("Upgrade 1","upgrade1", 1, 1, 1, "Lorem ipsum")
    if 'upgrade1' in upgradesbought:
        frame:
            padding (10,10)
            xalign 0.4
            yalign 0.4
            use upgradenode("Upgrade 2","upgrade2", 1, 0, 0, "Lorem ipsum")
    if 'upgrade1' in upgradesbought:
        frame:
            padding (10,10)
            xalign 0.6
            yalign 0.4
            use upgradenode("Upgrade 3","upgrade3", 0, 1, 0, "Lorem ipsum")
    if 'upgrade1' in upgradesbought:
        frame:
            padding (10,10)
            xalign 0.6
            yalign 0.6
            use upgradenode("Upgrade 4","upgrade4", 0, 0, 1, "Lorem ipsum")

    #buy screen
    if focusupgradename != "0":
        frame:
            padding (10, 10)
            xalign 0.95
            yalign 0.95
            vbox:
                spacing 10
                text "[focusupgradename]"
                text "[focusdescription]"
                text "Cost: {outlinecolor=#000}{color=#ff0000}[frcost] red {/color}{color=#0000ff}[fbcost] blue {/color}{color=#fbfb00}[fycost] yellow {/color}{/outlinecolor}" 
                frame:
                    padding (10, 10)
                    button:
                        text "Buy"
                        if rpoints >= frcost and bpoints >= fbcost and ypoints >= fycost:
                            action [AddToSet(upgradesbought, focusupgradeid), IncrementVariable("rpoints", -frcost), IncrementVariable("bpoints", -fbcost), IncrementVariable("ypoints", -fycost)]

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
    
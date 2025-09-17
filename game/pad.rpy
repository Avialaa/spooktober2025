label padTest:
    call screen magicPad
    return

screen magicPad:
    zorder 100
    imagemap:
        auto "images/padPohja %s.png"
        align (0.05, 0.2)
        
        #buttons to call loot items to conveyor belt
        hotspot (326, 40, 162, 122) action Function(addMeat)
        hotspot (490, 43, 168, 119) action Function(addWeapon)
        hotspot (322, 163, 164, 147) action Function(addTreasure)
        hotspot (492, 163, 164, 149) action Function(addSleep)
        hotspot (324, 323, 159, 169) action Function(addLight)
        hotspot (491, 316, 164, 180) action Function(addFish)
        hotspot (323, 501, 160, 159) action Function(addKeys)
        hotspot (491, 498, 164, 167) action Function(addBone)
    
    vbox: #kaikki orderit
        #TODO: wrong item counts are displayed in game, fix!!!
        align (0.05, 0.2)
        vbox: #current order
            text "{color=#ff0000}Current order{/color}"
            $ uniqueItems = set(orders[0]) #orders[0] is the first nested order list in orders list. converting list to a set only leaves 1 of each duplicate string
            for item in uniqueItems:
                hbox:
                    text "{color=#ff0000}[item]  {/color}"
                    text "{color=#ff0000}x[orders[0].count(item)]{/color}" #returns number of items
            text " "
        vbox: #next order
            text "{color=#ff0000}Next order{/color}"
            $ uniqueItems = set(orders[1]) 
            for item in uniqueItems:
                hbox:
                    text "{color=#ff0000}[item]  {/color}"
                    text "{color=#ff0000}x[orders[1].count(item)]{/color}" #returns number of items
            text " "
        vbox: #next next order
            text "{color=#ff0000}Next next order{/color}"
            $ uniqueItems = set(orders[2])
            for item in uniqueItems:
                hbox:
                    text "{color=#ff0000}[item]  {/color}"
                    text "{color=#ff0000}x[orders[2].count(item)]{/color}" #returns number of items
            text " "


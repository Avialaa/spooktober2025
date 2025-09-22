style padStyle:
    font "Silkscreen-Regular.ttf"
    color "#a32453"

label padTest:
    call screen magicPad
    return

screen magicPad:
    zorder 100
    #show visual timer (actual timer is in warehouse_gameplay screen)
    

    imagemap:
        auto "images/padPohja %s.png"
        align (0.95, 0.25)
        
        #buttons to call loot items to conveyor belt
        hotspot (326, 40, 162, 122) action Function(addMeat)
        hotspot (490, 43, 168, 119) action Function(addWeapon)
        hotspot (322, 163, 164, 147) action Function(addTreasure)
        hotspot (492, 163, 164, 149) action Function(addSleep)
        hotspot (324, 323, 159, 169) action Function(addLight)
        hotspot (491, 316, 164, 180) action Function(addFish)
        hotspot (323, 501, 160, 159) action Function(addKeys)
        hotspot (491, 498, 164, 167) action Function(addBone)
    
    add "countdown" xalign 0.9 yalign 0.75 

    viewport:
        area (1170, 80, 300, 800) # area (xpos, ypos, xsize, ysize)
        add "black"
        vbox: #kaikki orderit
            #TODO: Fix potential bug here (indexList out of range kummallisissa kohdissa peliä)
            #align (0.72, 0.25)
            vbox: #current order
                text "Current order" style "padStyle"
                $ uniqueItems = set(orders[0]) #orders[0] is the first nested order list in orders list. converting list to a set only leaves 1 of each duplicate string
                for item in uniqueItems:
                    hbox:
                        add "[item]_1_idle" zoom 0.5 #current order has icons; next orders don't
                        text "[item]  " style "padStyle"
                        text "x[orders[0].count(item)]" style "padStyle"#returns number of items
                text " "
            vbox: #next order
                text "Next order" style "padStyle"
                $ uniqueItems = set(orders[1]) 
                for item in uniqueItems:
                    hbox:
                        text "[item]  "style "padStyle"
                        text "x[orders[1].count(item)]" style "padStyle" #returns number of items
                text " "
            vbox: #next next order
                text "Next next order" style "padStyle"
                $ uniqueItems = set(orders[2])
                for item in uniqueItems:
                    hbox:
                        text "[item]  " style "padStyle"
                        text "x[orders[2].count(item)]" style "padStyle" #returns number of items
                text " "

default orderItems1 = []
default orderItems2 = []
default orderItems3 = []

style padStyle:
    font "Silkscreen-Regular.ttf"
    color "#2c2326"
    line_spacing -10
    size 28

style padNextStyle:
    font "Silkscreen-Regular.ttf"
    color "#7d7d7d"
    line_spacing -10
    size 28

init python:
    def updateOrders():
        global orderItems1
        global orderItems2
        global orderItems3

        if len(orders) > 0:
            orderItems1 = set(orders[0]) #orders[0] is the first nested order list in orders list. converting list to a set only leaves 1 of each duplicate string
        if len(orders) > 1:
            orderItems2 = set(orders[1])
        if len(orders) > 2:
            orderItems3 = set(orders[2])

screen magicPad:
    zorder 100
    #show visual timer (actual timer is in warehouse_gameplay screen)
    

    imagemap:
        auto "images/padPohja %s.png"
        align (1.0, 0.25)
        
        #buttons to call loot items to conveyor belt
        hotspot (413, 189, 166, 165) action Function(addMeat)
        hotspot (583, 192, 166, 163) action Function(addWeapon)
        hotspot (586, 696, 161, 163) action Function(addTreasure)
        hotspot (587, 361, 163, 160) action Function(addSleep)
        hotspot (587, 530, 160, 162) action Function(addLight)
        hotspot (414, 529, 165, 161) action Function(addFish)
        hotspot (418, 695, 162, 163) action Function(addKeys)
        hotspot (418, 358, 163, 164) action Function(addBone)
    
    vbox:
        xpos 1570 yalign 0.9 
        text "Time left" style "padStyle"
        add "countdown"
    
    viewport:
        area (1520, 120, 290, 250) # area (xpos, ypos, xsize, ysize)
        text "Order items to conveyer belt" style "padStyle" xalign 0.5
    viewport:
        area (1185, 150, 290, 840) # area (xpos, ypos, xsize, ysize)
        #add "black"
        vbox: #kaikki orderit
            #TODO: Fix potential bug here (indexList out of range kummallisissa kohdissa peliä)
            #align (0.72, 0.25)
            vbox: #current order
                text "Current order" style "padStyle"
                for item in orderItems1:
                    hbox:
                        add "order [item]" #current order has icons; next orders don't
                        vbox:
                            text "[item]  " style "padStyle"
                            text "x[orders[0].count(item)]" style "padStyle"#returns number of items
                text " "
            vbox: #next order
                text "Next order" style "padNextStyle"
                for item in orderItems2:
                    hbox:
                        text "[item]  "style "padNextStyle"
                        text "x[orders[1].count(item)]" style "padNextStyle" #returns number of items
                text " "
            vbox: #next next order
                text "Next next order" style "padNextStyle"
                for item in orderItems3:
                    hbox:
                        text "[item]  " style "padNextStyle"
                        text "x[orders[2].count(item)]" style "padNextStyle" #returns number of items
                text " "

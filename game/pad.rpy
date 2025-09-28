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

default itemNameDict = {"light": "Lantern", "sleep": "Nap", "fish": "Fish", "bone": "Bone", "meat": "Meat", "weapon": "Blade", "keys": "Key", "treasure": "Coin"}

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
        hotspot (413, 189, 166, 165) action [Function(addMeat), Play('sound', 'click_kwahmah_02__click.mp3')]
        hotspot (583, 192, 166, 163) action [Function(addWeapon), Play('sound', 'click_kwahmah_02__click.mp3')]
        hotspot (586, 696, 161, 163) action [Function(addTreasure), Play('sound', 'click_kwahmah_02__click.mp3')]
        hotspot (587, 361, 163, 160) action [Function(addSleep), Play('sound', 'click_kwahmah_02__click.mp3')]
        hotspot (587, 530, 160, 162) action [Function(addLight), Play('sound', 'click_kwahmah_02__click.mp3')]
        hotspot (414, 529, 165, 161) action [Function(addFish), Play('sound', 'click_kwahmah_02__click.mp3')]
        hotspot (418, 695, 162, 163) action [Function(addKeys), Play('sound', 'click_kwahmah_02__click.mp3')]
        hotspot (418, 358, 163, 164) action [Function(addBone), Play('sound', 'click_kwahmah_02__click.mp3')]
    
    vbox:
        xpos 1570 yalign 0.9 
        text "Time left" style "padStyle"
        add "countdown"
    
    viewport:
        area (1520, 120, 290, 250) # area (xpos, ypos, xsize, ysize)
        text "Order items to conveyor belt" style "padStyle" xalign 0.5
    viewport:
        area (1185, 150, 290, 840) # area (xpos, ypos, xsize, ysize)
        #add "black"
        vbox: #kaikki orderit
            vbox: #current order
                text "Current order" style "padStyle"
                for item in orderItems1:
                    hbox:
                        add "order [item]" #current order has icons; next orders don't
                        vbox:
                            text "[itemNameDict.get(item)]  " style "padStyle"
                            if [item.name for item in itemsInBox].count(item) >= orders[0].count(item):
                                add "minigame checkmark.png" zoom 0.5
                            else:
                                text "x[orders[0].count(item)]" style "padStyle"#returns number of items
                text " "
            vbox: #next order
                text "Next order" style "padNextStyle"
                for item in orderItems2:
                    hbox:
                        text "[itemNameDict.get(item)]  "style "padNextStyle"
                        text "x[orders[1].count(item)]" style "padNextStyle" #returns number of items
                text " "
            vbox: #next next order
                text "Next next order" style "padNextStyle"
                for item in orderItems3:
                    hbox:
                        text "[itemNameDict.get(item)]  " style "padNextStyle"
                        text "x[orders[2].count(item)]" style "padNextStyle" #returns number of items
                text " "

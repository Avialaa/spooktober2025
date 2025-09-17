
default itemIndex = 0
default itemsInBox = []
default maxBoxItems = 6 #must be at least as big as max order size
default itemTypeList = ["light", "sleep", "fish", "bone", "meat", "weapon", "keys", "treasure"] #list of item names/item types. DO NOT CHANGE ORDER
default itemsOnConveyer = [] #items that will be spawned on conveyer; not currently visible items
default orderList = [] #list of items in last generated order
default orders = [] #list of orders (list of nested lists?)
default isOrderCorrect = True

init python:
  def hideItem(tag):
    renpy.hide_screen(tag)

  class Item:
    def __init__(self, name, tier):
      self.name = name
      self.tier = tier
      self.image = None
    def setImage(self):
      self.image = "{0}_{1}".format(self.name, self.tier)
    
  def showItemsOnConveyer():
    #Checks if anything to spawn on conveyer belt, and spawns first item from list
    global itemIndex #this tells Python that we want to use the global variable itemIndex
    if len(itemsOnConveyer) > 0:
      #pop returns the item and removes it from list
      item = itemsOnConveyer.pop(0)
    else:
      return
    #increment itemIndex so we get a different tag for each new spawned button
    itemIndex += 1
    item.setImage()
    renpy.show_screen("conveyer_item", item, 5, _tag=f"item_{itemIndex}")
  
  def sendOrder():
    #TODO: call points calculation function here etc
    global orders
    global isOrderCorrect
    isOrderCorrect = checkOrderValidity()
    #pointCount() TODO: Tuukka epäkommentoi tää kun haluat testata pointCount-funktion toimintaa (ajetaan kun painaa send order nappia)
    generateOrder()
    orders.pop(0) #remove finished order
    itemsInBox.clear()

  def generateOrder():
    #function that generates a list of item names
    global maxBoxItems
    global itemTypeList
    global orders
    global orderList

    #TODO: Test game and set order sizes that feel good; decide if box size affects order size
    #Or maybe order size could grow as days pass?
    if maxBoxItems < 8:
      orderSize =  renpy.random.randint(4,5)
    else:
      orderSize = renpy.random.randint(4,6)
    
    #orders can have 2 or 3 item types
    numberOfOrderTypes = renpy.random.randint(2,4)

    #make a copy of list of items so we can remove stuff without affecting the original list
    copiedItemTypeList = itemTypeList.copy()
    orderTypes = []

    #randomize as many item types as needed, add them to a list
    while numberOfOrderTypes > 0:
      orderType = renpy.random.choice(copiedItemTypeList)
      copiedItemTypeList.remove(orderType)
      orderTypes.append(orderType)
      numberOfOrderTypes -= 1
    
    orderList = []

    #make sure there is at least one of each chosen item in the order
    for order in orderTypes:
      orderList.append(order)

    #fill rest of the order with random items of chosen types
    while len(orderList) < orderSize:
      item = renpy.random.choice(orderTypes)
      orderList.append(item)
    
    orders.append(orderList) #add order to orders list for storage

  def checkOrderValidity():
    global orders
    global itemsInBox

    #make a copy of order so we can remove stuff without affecting the original list
    copiedOrder = orders[0].copy()

    isOrderCorrect = True

    for item in itemsInBox:
      if item.name in copiedOrder:
        #TODO: give points for correct item?
        copiedOrder.remove(item.name)
      else:
        #TODO: remove points for incorrect item?
        isOrderCorrect = False
    
    return isOrderCorrect

    
    
  

label warehouse_gameplay:
  #generate 3 orders at the start of the minigame
  $ generateOrder()
  $ generateOrder()
  $ generateOrder()
  call screen warehouse_gameplay

screen warehouse_gameplay:
  #warehouse gameplay screen, houses all sub-screens (tablet, box, conveyer belts, etc)
  use conveyer_belt(1)
  use warehouse_box
  use send_order_button
  #use tablet_item_buttons
  #use magicPad
  $ renpy.show_screen("magicPad", _zorder=100)
  
#TARVITAAN:
#-tilausten näyttäminen pädillä
#tilaus-backlogin generointi ja tallentaminen ja näyttäminen

screen conveyer_belt(conveyerInterval):
  zorder 20
  modal True 

  text "{outlinecolor=#000}{color=#ff0000}Ducks: [itemIndex] Order list: [orderList] Is latest order correct? [isOrderCorrect]{/color}{/outlinecolor}" #Items in box: [itemsInBox] Items on conveyer: [itemsOnConveyer]
  timer conveyerInterval:
    action [Function(showItemsOnConveyer)]
    repeat True


screen conveyer_item(item, timeOnConveyer):
  modal False
  zorder 50
  
  imagebutton:
    auto "{}_%s.png".format(item.image)
    #can't use Hide() because it uses screen names, not tags; must use renpy.hide_screen(tag) wrapped into a custom function
    #TODO: check if can use tags with Hide() after all
    #if box is full, button can't be clicked.
    if len(itemsInBox) +1 <= maxBoxItems:
      action [Function(hideItem, renpy.current_screen().tag), AddToSet(itemsInBox, item)] #TODO: If player tries to click item when box is full, box numbers shake
    at transform:
      xpos 0.1 ypos 0.3
      on show:
        linear timeOnConveyer xpos 0.7
  
  text "[renpy.current_screen().tag]":
    at transform:
      xpos 0.1 ypos 0.25
      on show:
        linear timeOnConveyer xpos 0.7
  #hide item and return it to conveyer spawn list
  timer timeOnConveyer action [Hide(), AddToSet(itemsOnConveyer, item)]

transform box_shake:
  xalign 0.7 yalign 1.1
  on show:
    linear 0.2 align (0.7, 1.0)
    linear 0.2 align (0.7, 1.1)

screen warehouse_box:

  frame style 'empty' xysize (600,450): 
    xalign 0.5 yalign 0.5
    background Frame("box.png",0,0)
    at box_shake
    text "{outlinecolor=#000}{color=#ff0000}Items: [len(itemsInBox)] / [maxBoxItems]{/color}{/outlinecolor}":
        xcenter 0.5 ycenter 0.5
  
screen send_order_button:
  textbutton "Send order":
    xalign 0.4 yalign 0.9
    action Function(sendOrder)


# screen tablet_item_buttons:

#   vbox:
#     xalign 0.0 yalign 0.5

#     textbutton "light" action Function(addLight)
#     textbutton "sleep" action Function(addSleep)
#     textbutton "fish" action Function(addFish)
#     textbutton "bone" action Function(addBone)
#     textbutton "meat" action Function(addMeat)
#     textbutton "weapon" action Function(addWeapon)
#     textbutton "keys" action Function(addKeys)
#     textbutton "treasure" action Function(addTreasure)

init python:
  #items are spawned using list indexes, so that if item names change, it won't break these functions. List order must always stay the same.
  #["light", "sleep", "fish", "bone", "meat", "weapon", "keys", "treasure"]
  def addLight():
    tier = 1 #TODO: make tier depend on percentages
    item = Item(itemTypeList[0], tier)
    itemsOnConveyer.append(item)

  def addSleep():
    tier = renpy.random.randint(1,3) #TODO: make tier depend on percentages
    item = Item(itemTypeList[1], tier)
    itemsOnConveyer.append(item)

  def addFish():
    tier = renpy.random.randint(1,3) #TODO: make tier depend on percentages
    item = Item(itemTypeList[2], tier)
    itemsOnConveyer.append(item)
  
  def addBone():
    tier = renpy.random.randint(1,3) #TODO: make tier depend on percentages
    item = Item(itemTypeList[3], tier)
    itemsOnConveyer.append(item)
  
  def addMeat():
    tier = renpy.random.randint(1,3) #TODO: make tier depend on percentages
    item = Item(itemTypeList[4], tier)
    itemsOnConveyer.append(item)
  
  def addWeapon():
    tier = renpy.random.randint(1,3) #TODO: make tier depend on percentages
    item = Item(itemTypeList[5], tier)
    itemsOnConveyer.append(item)
  
  def addKeys():
    tier = renpy.random.randint(1,3) #TODO: make tier depend on percentages
    item = Item(itemTypeList[6], tier)
    itemsOnConveyer.append(item)
  
  def addTreasure():
    tier = renpy.random.randint(1,3) #TODO: make tier depend on percentages
    item = Item(itemTypeList[7], tier)
    itemsOnConveyer.append(item)


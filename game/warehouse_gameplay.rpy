default itemIndex = 0
default itemsInBox = []
default maxBoxItems = 6 #must be at least as big as max order size
default itemTypeList = ["light", "sleep", "fish", "bone", "meat", "weapon", "keys", "treasure"] #list of item names/item types. DO NOT CHANGE ORDER
default itemsOnConveyer = [] #items that will be spawned on conveyer; not currently visible items
default orderList = [] #list of items in last generated order
default orders = [] #list of orders (list of nested lists?)
default isOrderCorrect = True
default boxReady = True
default boxAnimDuration = 0.5
default roundDuration = 50
default minigameOver = False
default conveyerInterval = 1 #miten tiuhaan tavarat on liukuhihnalla, sekunneissa spawnausväli (pienempi = tiheämpi)
default subsequentCorrectOrders = 0
default correctOrders = 0
default incorrectOrders = 0
default activeConveyerTags = [] #keep track of current conveyer tags so we can hide the screens when the minigame ends

default roundFish = 0
default agathaPoints = 0
default ceePoints = 0
default karkhosPoints = 0
default currentStoryRoute = None
default correctOrdersDemandedByAgatha = 3
default fishDemandedByCee = 5
default workShift = 0

default move_text = None #set transform to none

image countdown = DynamicDisplayable(show_countdown)

style boxTextStyle:
  font "Silkscreen-Regular.ttf"
  color "#a32453"
  size 45

image box = ConditionSwitch(
  "boxReady == True", "box_open.png",
  "boxReady == False", "box_closed.png",
  "True", "box_open.png"
)
init python:

  def show_countdown(st, at):
    global roundDuration
    if st > roundDuration:
      return Text("0.0", color ="#a32453", font = "Silkscreen-Regular.ttf", size = 60), None
    else:
      d = Text("{:.1f}".format(roundDuration - st), color ="#a32453", font = "Silkscreen-Regular.ttf", size = 60)
      return d, 0.1

init python:
  def resetMinigame():
    global correctOrders
    global incorrectOrders
    global subsequentCorrectOrders
    global orders
    global orderList
    global itemsOnConveyer
    global itemsInBox
    global roundFish
    global boxReady


    correctOrders = 0
    incorrectOrders = 0
    subsequentCorrectOrders = 0
    roundFish = 0
    boxReady = True
    orders.clear()
    orderList.clear()
    itemsOnConveyer.clear()
    itemsInBox.clear()
  
  def setMinigameGoals():
    global workShift
    global fishDemandedByCee
    global correctOrdersDemandedByAgatha

    if workShift == 1:
      correctOrdersDemandedByAgatha = 3
      fishDemandedByCee = 6
    elif workShift == 2:
      correctOrdersDemandedByAgatha = 3
      fishDemandedByCee = 8
    elif workShift == 3:
      correctOrdersDemandedByAgatha = 4
      fishDemandedByCee = 10
    elif workShift == 4:
      correctOrdersDemandedByAgatha = 4
      fishDemandedByCee = 14
    elif workShift == 5:
      correctOrdersDemandedByAgatha = 5
      fishDemandedByCee = 20


  def chooseRoute():
    global agathaPoints
    global ceePoints
    global karkhosPoints
    global currentStoryRoute
    global correctOrders
    global incorrectOrders
    global roundFish
    global workShift
    global correctOrdersDemandedByAgatha
    global fishDemandedByCee

    #First shift doesn't affect route
    if workShift == 1:
      return

    thisRoundWinner = None
    if (correctOrders - incorrectOrders) >= correctOrdersDemandedByAgatha:
      agathaPoints += 1
      thisRoundWinner = "agatha"
    else:
      karkhosPoints += 1
      thisRoundWinner = "karkhos"
    
    #Cee's route takes precedence over other routes; amount of correct order doesn't matter, only fish
    if roundFish >= fishDemandedByCee:
      ceePoints +=1
      thisRoundWinner = "cee"

    #if there's a clear point winner, select their route
    if ceePoints > agathaPoints and ceePoints > karkhosPoints:
      currentStoryRoute = "cee"
    elif agathaPoints > karkhosPoints and agathaPoints > ceePoints:
      currentStoryRoute = "agatha"
    elif karkhosPoints > agathaPoints and karkhosPoints > ceePoints:
      currentStoryRoute = "karkhos"
    
    #in case of a 3-way tie, use current round winner as the selected route
    elif ceePoints == agathaPoints and ceePoints == karkhosPoints and agathaPoints == karkhosPoints:
      currentStoryRoute = thisRoundWinner

    #if there's a tie between 2 characters, route is round winner, unless round winner has the least amount of points, in which case route is randomized between tie members
    elif ceePoints == agathaPoints or ceePoints == karkhosPoints or agathaPoints == karkhosPoints:
      if ceePoints == agathaPoints:
        if thisRoundWinner != "karkhos":
          currentStoryRoute = thisRoundWinner
        else:
          currentStoryRoute = renpy.random.choice(["cee", "agatha"])
      elif ceePoints == karkhosPoints:
        if thisRoundWinner != "agatha":
          currentStoryRoute = thisRoundWinner
        else:
          currentStoryRoute = renpy.random.choice(["cee", "karkhos"])
      elif agathaPoints == karkhosPoints:
        if thisRoundWinner != "cee":
          currentStoryRoute = thisRoundWinner
        else:
          currentStoryRoute = renpy.random.choice(["agatha", "karkhos"])
    
    else:
      #if all else fails, randomize route (this should never happen if logic is correct)
      currentStoryRoute = renpy.random.choice(["agatha", "karkhos", "cee"])


  def hideMinigame():
    renpy.hide_screen("warehouse_box")
    renpy.hide_screen("magicPad")
    hideAllConveyerItems()

  def hideItem(tag):
    renpy.hide_screen(tag)
    if tag in activeConveyerTags:
        activeConveyerTags.remove(tag)
  
  def hideAllConveyerItems():
    global activeConveyerTags
    for tag in activeConveyerTags:
        renpy.hide_screen(tag)
    activeConveyerTags.clear()
  
  def closeBox():
    global itemsInBox
    global boxReady

    if len(itemsInBox) == maxBoxItems:
      boxReady = False

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
    global activeConveyerTags
    if len(itemsOnConveyer) > 0:
      #pop returns the item and removes it from list
      item = itemsOnConveyer.pop(0)
    else:
      return
    #increment itemIndex so we get a different tag for each new spawned button
    itemIndex += 1
    item.setImage()
    tag = f"item_{itemIndex}"
    activeConveyerTags.append(tag)
    renpy.show_screen("conveyer_item", item, 5, _tag=tag)
  
  def sendOrder():
    global orders
    global isOrderCorrect
    isOrderCorrect = checkOrderValidity()
    pointCount() 
    generateOrder()
    countFish()
    orders.pop(0) #remove finished order
    itemsInBox.clear()
    updateOrders() #update orders for pad UI
    if isOrderCorrect == True:
      renpy.sound.play("correct_thebuilder15__notification-correct.mp3")
    else:
      renpy.sound.play("wrong_thebuilder15__wrong.mp3")
  
  def countFish():
    global roundFish
    global itemsInBox

    for item in itemsInBox:
      if item.name == "fish":
        roundFish += 1


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
    global subsequentCorrectOrders
    global correctOrders
    global incorrectOrders

    copiedOrder = orders[0].copy()
    isOrderCorrect = True

    # Create a list of item names from itemsInBox
    itemNamesInBox = [item.name for item in itemsInBox]

    for orderItem in copiedOrder:
        if orderItem in itemNamesInBox:
          #TODO: give points for correct item?
          itemNamesInBox.remove(orderItem)  # Remove to handle duplicates correctly
        else:
          #TODO: remove points for incorrect item?
          isOrderCorrect = False
    
    #track how many orders have been correct in a row
    if isOrderCorrect == True:
      subsequentCorrectOrders += 1
      correctOrders +=1
    else:
      subsequentCorrectOrders = 0
      incorrectOrders += 1

    return isOrderCorrect

label warehouse_gameplay:
  #this should disable skipping during minigame
  if _skipping:
    hide screen skip_indicator
    $ _skipping = False
  $ renpy.config.skipping = False

  #generate 3 orders at the start of the minigame
  $ generateOrder()
  $ generateOrder()
  $ generateOrder()
  $ updateOrders() #update orders for pad UI
  $ workShift += 1 #keep track of played work shifts
  $ setMinigameGoals() #set character story route goals for the day
  $ quick_menu = False #hide the quick menu during minigame
  $ minigameOver = False

  call screen warehouse_gameplay

screen warehouse_gameplay:
  add "bg warehouse.png"
  add "conveyer.png" xalign 0.0 yalign 0.45
  #warehouse gameplay screen, houses all sub-screens (tablet, box, conveyer belts, etc)
  use conveyer_belt(conveyerInterval)
  use send_order_button
  on "show":
    action [Show("warehouse_box"), Show("magicPad", _zorder=100)]
  
  timer roundDuration:
    action [Hide(transition = fade), Function(hideMinigame), SetVariable("minigameOver", True), Return()]
  #visual timer is shown in magicPad screen

screen conveyer_belt(conveyerInterval):
  zorder 20
  modal True 

  #developer debug text
  #text "{outlinecolor=#000}{color=#ff0000}BoxReady: [boxReady] Order list: [orderList] Is latest order correct? [isOrderCorrect]{/color}{/outlinecolor}" #Items in box: [itemsInBox] Items on conveyer: [itemsOnConveyer]
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
    #if len(itemsInBox) +1 <= maxBoxItems:
    action If(boxReady, true=[Function(hideItem, renpy.current_screen().tag), AddToSet(itemsInBox, item), Function(closeBox), Show("warehouse_box"), Play('audio', 'clickItem_leonsflashlight__box-open.mp3')], false=[SetVariable("move_text", box_text_shake), Show("box_text_shake_timer"), Play('audio', 'boxFull_pkbiggums__box_shatter2.mp3')])
    at transform:
      xpos -100 ypos 0.25
      on show:
        linear timeOnConveyer xpos 0.7
      on hide:
        linear 0.1 yoffset -50
        linear 0.2 yoffset 100 alpha 0.0
  
  #Uncomment for tag troubleshooting:
  # text "[renpy.current_screen().tag]":
  #   at transform:
  #     xpos -100 ypos 0.25
  #     on show:
  #       linear timeOnConveyer xpos 0.7
  #hide item and return it to conveyer spawn list
  timer timeOnConveyer action [Hide(), AddToSet(itemsOnConveyer, item)]

transform box_shake:
  xalign 0.3 yalign 1.2
  on replace:
    linear 0.15 xoffset -5
    linear 0.15 xoffset 5
    linear 0.1 xoffset 0
  on hide:
    linear (boxAnimDuration/3) yoffset -10
    linear (boxAnimDuration - boxAnimDuration/3) yoffset 100 alpha 0.0
  on show:
    alpha 0.0 xoffset 100
    linear (boxAnimDuration - boxAnimDuration/3) xoffset -10 alpha 1.0
    linear (boxAnimDuration/3) xoffset 0 

transform box_text_shake:
  xcenter 0.5 ycenter 0.6
  linear 0.15 yoffset -5
  linear 0.15 yoffset 5
  linear 0.1 yoffset 0

screen box_text_shake_timer:
  timer 0.5 action [SetVariable("move_text", None), Hide()]

screen warehouse_box:

  on "show":
    action Play('audio', 'boxWoosh2_magnuswaker__hard-swing-1.mp3')
  on "hide":
    action Play('audio', 'boxWoosh_qubodup__whoosh.mp3')
  on "replace":
    action Play('audio', 'itemToBox_crownieyt__open-package-box-parcel.mp3')

  frame style 'empty' xysize (773,600): 
    xalign 0.5 yalign 0.5
    background Frame("box", 0,0)
    at box_shake
    
    text "Items: [len(itemsInBox)] / [maxBoxItems]":
        xcenter 0.5 ycenter 0.6
        style "boxTextStyle"
        at move_text #empty transform; use action SetVariable("move_text", box_text_shake) to play animation
    
    
  
screen button_disable_timer:
  on "show":
    action SetVariable("boxReady", False)
  timer boxAnimDuration:
    if minigameOver == False:
      action [Show("warehouse_box")] #action [SetVariable("boxReady", True), Show("warehouse_box"), Hide()]
  timer (boxAnimDuration*2):
    action [SetVariable("boxReady", True), Hide()]



  
screen send_order_button:

  showif minigameOver == False:
    imagebutton:
      xalign 0.05 yalign 0.9
      auto "send_%s.png"
      #if len(itemsInBox) +1 <= maxBoxItems:
      if len(itemsInBox) > 0:
        action [Function(sendOrder), Hide("warehouse_box"), Show("button_disable_timer")]


#Item button spawn functions
init python:
  #items are spawned using list indexes, so that if item names change, it won't break these functions. List order must always stay the same.
  #["light", "sleep", "fish", "bone", "meat", "weapon", "keys", "treasure"]
  #tier is now randomized based on upgrades
  def addLight():
    if renpy.random.randint(1,10)<=tier3ChanceDict.get("light",0):
      tier = 3
    elif renpy.random.randint(1,10)<=tier2ChanceDict.get("light",0):
      tier = 2
    else:
      tier = 1
    item = Item(itemTypeList[0], tier)
    itemsOnConveyer.append(item)

  def addSleep():
    if renpy.random.randint(1,10)<=tier3ChanceDict.get("sleep",0):
      tier = 3
    elif renpy.random.randint(1,10)<=tier2ChanceDict.get("sleep",0):
      tier = 2
    else:
      tier = 1
    item = Item(itemTypeList[1], tier)
    itemsOnConveyer.append(item)

  def addFish():
    if renpy.random.randint(1,10)<=tier3ChanceDict.get("fish",0):
      tier = 3
    elif renpy.random.randint(1,10)<=tier2ChanceDict.get("fish",0):
      tier = 2
    else:
      tier = 1
    item = Item(itemTypeList[2], tier)
    itemsOnConveyer.append(item)
  
  def addBone():
    if renpy.random.randint(1,10)<=tier3ChanceDict.get("bone",0):
      tier = 3
    elif renpy.random.randint(1,10)<=tier2ChanceDict.get("bone",0):
      tier = 2
    else:
      tier = 1
    item = Item(itemTypeList[3], tier)
    itemsOnConveyer.append(item)
  
  def addMeat():
    if renpy.random.randint(1,10)<=tier3ChanceDict.get("meat",0):
      tier = 3
    elif renpy.random.randint(1,10)<=tier2ChanceDict.get("meat",0):
      tier = 2
    else:
      tier = 1
    item = Item(itemTypeList[4], tier)
    itemsOnConveyer.append(item)
  
  def addWeapon():
    if renpy.random.randint(1,10)<=tier3ChanceDict.get("weapon",0):
      tier = 3
    elif renpy.random.randint(1,10)<=tier2ChanceDict.get("weapon",0):
      tier = 2
    else:
      tier = 1
    item = Item(itemTypeList[5], tier)
    itemsOnConveyer.append(item)
  
  def addKeys():
    if renpy.random.randint(1,10)<=tier3ChanceDict.get("keys",0):
      tier = 3
    elif renpy.random.randint(1,10)<=tier2ChanceDict.get("keys",0):
      tier = 2
    else:
      tier = 1
    item = Item(itemTypeList[6], tier)
    itemsOnConveyer.append(item)
  
  def addTreasure():
    if renpy.random.randint(1,10)<=tier3ChanceDict.get("treasure",0):
      tier = 3
    elif renpy.random.randint(1,10)<=tier2ChanceDict.get("treasure",0):
      tier = 2
    else:
      tier = 1
    item = Item(itemTypeList[7], tier)
    itemsOnConveyer.append(item)


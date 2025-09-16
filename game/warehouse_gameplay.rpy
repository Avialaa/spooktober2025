
default itemIndex = 0
default itemsInBox = []
default maxBoxItems = 4
#items that will be spawned on conveyer; not currently visible items
default itemsOnConveyer = []

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
    global itemIndex #this tells Python that we want to use the global variable itemIndex
    if len(itemsOnConveyer) > 0:
      item = itemsOnConveyer.pop(0)
    else:
      return
    #item = Item("ankka", 1)
    itemIndex += 1
    item.setImage()
    renpy.show_screen("conveyer_item", item, 5, _tag=f"item_{itemIndex}")

  def addItemsToConveyerList(numberOfItems):
    while numberOfItems > 0:
      item = Item("ankka", 1)
      itemsOnConveyer.append(item)
      numberOfItems = numberOfItems -1
  

label warehouse_gameplay:
  #TODO: remove when items can be added via tablet
  $ addItemsToConveyerList(8)
  call screen warehouse_gameplay

screen warehouse_gameplay:
  #warehouse gameplay screen, houses all sub-screens (tablet, box, conveyer belts, etc)
  use conveyer_belt(1)
  use warehouse_box
  

#TARVITAAN
#funktio, joka määrittää mikä tavara tulee liukuhihnalle


#funktio, joka määrittää mikä tavara tulee liukuhihnalle:
#Lista, jolle voi lisätä tavaroita 
#tavaroita voi lisätä pädiltä, ja liukuhihnalla ohimenneet tavarat myös palaavat listan perälle (tehty)
#pädiltä lisätessä on takaraja, kuinka monta itemiä voi lisätä 
# --> tämä ominaisuus vain, jos saadaan implementoitua tavaroiden roskiin heittäminen

screen conveyer_belt(conveyerInterval):
  modal True 

  text "{outlinecolor=#000}{color=#ff0000}Ducks: [itemIndex]  Items in box: [itemsInBox] Items on conveyer: [itemsOnConveyer]{/color}{/outlinecolor}"
  timer conveyerInterval:
    action [Function(showItemsOnConveyer)]
    repeat True


screen conveyer_item(item, timeOnConveyer):
  modal False
  
  imagebutton:
    auto "{}_%s.png".format(item.image)
    #can't use Hide() because it uses screen names, not tags; must use renpy.hide_screen(tag) wrapped into a custom function
    #TODO: check if can use tags with Hide() after all
    #if box is full, button can't be clicked.
    if len(itemsInBox) +1 <= maxBoxItems:
      #TODO: AddToSet ei toimi, kun yrittää lisätä "ankka":aa monta kertaa; ongelmana että python ei lisää duplikaatteja samasta referenssistä listalle tai jotain?
      action [Function(hideItem, renpy.current_screen().tag), AddToSet(itemsInBox, item)] #TODO: If player tries to click item when box is full, box numbers shake
    at transform:
      xpos 0.1 ypos 0.5
      on show:
        linear timeOnConveyer xpos 0.7
  
  text "[renpy.current_screen().tag]":
    at transform:
      xpos 0.1 ypos 0.45
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

    add "box.png":
      at box_shake

    frame:
      at box_shake
      text "{outlinecolor=#000}{color=#ff0000}Items: [len(itemsInBox)] / [maxBoxItems]{/color}{/outlinecolor}" yoffset -400



#Funktio, joka ajetaan kun painetaan lähetä tilaus-nappia

#Verrataan laatikkolistaa tilaukseen
#Pisteytyssysteemi: jokaisesta oikeasta tavarasta pluspisteitä, puuttuvasta tavarasta miinuspisteitä 
#(ja ehkä joku virhemerkintä joka tulee sit sähköpostilla jos on puuttunut tavaroita)
#lisäksi tai sen sijaan hahmo/tavaratyyppikohtaiset pisteet

#kun pisteytys on tehty, laatikkolista tyhjennetään








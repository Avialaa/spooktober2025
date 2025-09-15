
default itemIndex = 0
default itemsInBox = []
default maxBoxItems = 4
default itemsOnConveyer = []

init python:
  def hideItem(tag):
    renpy.hide_screen(tag)

screen warehouse_gameplay:
  #warehouse gameplay screen, houses all sub-screens (tablet, box, conveyer belts, etc)
  use conveyer_belt(1)
  

#TARVITAAN
#item classi/objekti, jossa itemin nimi, kuva??, jne
#funktio, joka määrittää mikä tavara tulee liukuhihnalle

#item classi
#nimi
#kuva (tier määrittää kuvan)
#tier


#funktio, joka määrittää mikä tavara tulee liukuhihnalle:
#Lista, jolle voi lisätä tavaroita 
#tavaroita voi lisätä pädiltä, ja liukuhihnalla ohimenneet tavarat myös palaavat listan perälle
#pädiltä lisätessä on takaraja, kuinka monta itemiä voi lisätä 
# --> tämä ominaisuus vain, jos saadaan implementoitua tavaroiden roskiin heittäminen
#Pitää ehkä aina luoda uusi classi/objecti joka syötetään muille funktioille sitten? https://discuss.python.org/t/duplicated-objects-appended-into-list/14077

screen conveyer_belt(conveyerInterval):
  modal True 
  text "{outlinecolor=#000}{color=#ff0000}Ducks: [itemIndex]  Items in box: [itemsInBox]{/color}{/outlinecolor}"
  timer conveyerInterval:
    action [IncrementVariable("itemIndex"), Show("conveyer_item", None, "ankka", 5, _tag=f"item_{itemIndex}")]
    repeat True


screen conveyer_item(item, timeOnConveyer):
  modal False
  

  imagebutton:
    auto "{}_%s.png".format(item)
    #can't use Hide() because it uses screen names, not tags; must use renpy.hide_screen(tag) wrapped into a custom function
    #TODO: check if can use tags with Hide() after all
    #if box is full, button can't be clicked. TODO: check if this works (makes the button inactive?)
    if len(itemsInBox) <= maxBoxItems:
      #TODO: AddToSet ei toimi, kun yrittää lisätä "ankka":aa monta kertaa; ongelmana että python ei lisää duplikaatteja samasta referenssistä listalle tai jotain?
      action [Function(hideItem, renpy.current_screen().tag)] #, AddToSet(itemsInBox, item)]  #piilota nappi, aja funktio, joka lisää tavaran laatikkoon
    at transform:
      xpos 0.1 ypos 0.5
      on show:
        linear timeOnConveyer xpos 0.7
  
  text "[renpy.current_screen().tag]":
    at transform:
      xpos 0.1 ypos 0.45
      on show:
        linear timeOnConveyer xpos 0.7
  timer timeOnConveyer action Hide()



#Funktio, joka ajetaan kun painetaan lähetä tilaus-nappia

#Verrataan laatikkolistaa tilaukseen
#Pisteytyssysteemi: jokaisesta oikeasta tavarasta pluspisteitä, puuttuvasta tavarasta miinuspisteitä 
#(ja ehkä joku virhemerkintä joka tulee sit sähköpostilla jos on puuttunut tavaroita)
#lisäksi tai sen sijaan hahmo/tavaratyyppikohtaiset pisteet

#kun pisteytys on tehty, laatikkolista tyhjennetään








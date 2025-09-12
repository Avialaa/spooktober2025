
default itemIndex = 0

screen warehouse_gameplay:
  use conveyer_belt(2)
  #warehouse gameplay screen, houses all sub-screens (tablet, box, conveyer belts, etc)


#

# function spawnItem
# Takes the first item of itemsToSpawn list and spawns a corresponding textbutton on the conveyer belt. Removes the item from itemsToSpawn list

#we also need a list of items on the conveyer belt? 
#Or each button has an associated timer that destroys the button after a certain number of seconds (times conveyer speed modifier)

screen conveyer_belt(conveyerInterval):
  modal True 
  text "{outlinecolor=#000}{color=#ff0000}Ducks: [itemIndex]{/color}{/outlinecolor}"
  timer conveyerInterval:
    action [IncrementVariable("itemIndex"), Show("conveyer_item", None, "ankka", 5, _tag=f"item_{itemIndex}")]
    repeat True


screen conveyer_item(item, timeOnConveyer):
  modal False
  imagebutton:
    auto "{}_%s.png".format(item)
    action Hide() #piilota nappi, aja funktio, joka lisää tavaran laatikkoon
    at transform:
      xpos 0.1 ypos 0.5
      on show:
        linear timeOnConveyer xpos 0.7
  
  timer timeOnConveyer action Hide()







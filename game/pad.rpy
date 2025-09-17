label padTest:
    call screen magicPad
    return

screen magicPad:
    zorder 100
    imagemap:
        auto "images/padPohja %s.png"
        align (0.1, 0.1)
        
        hotspot (326, 40, 162, 122) action Function(addMeat)
        hotspot (490, 43, 168, 119) action Function(addWeapon)
        hotspot (322, 163, 164, 147) action Function(addTreasure)
        hotspot (492, 163, 164, 149) action Function(addSleep)
        hotspot (324, 323, 159, 169) action Function(addLight)
        hotspot (491, 316, 164, 180) action Function(addFish)
        hotspot (323, 501, 160, 159) action Function(addKeys)
        hotspot (491, 498, 164, 167) action Function(addBone)

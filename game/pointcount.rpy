
default feedbackList = []

init python:
    def pointCount():
    #counts points when order is sent

        global orderrPoints
        global orderbPoints
        global orderyPoints
        global orderoPoints
        global ordergPoints
        global ordervPoints
        global orderpPoints
        global orderlPoints

        global roundrPoints
        global roundbPoints
        global roundyPoints
        global roundoPoints
        global roundgPoints
        global roundvPoints
        global roundpPoints
        global roundlPoints

        global itemValueDict
        global tier2ValueDict
        global tier3ValueDict

        global isOrderCorrect
        global upgradesBought

        itemCountList = [] #list is used to count items one tier at a time
        #zeroing the initial point count of the order
        orderrPoints = 0
        orderbPoints = 0
        orderyPoints = 0
        orderoPoints = 0
        ordergPoints = 0
        ordervPoints = 0
        orderpPoints = 0
        orderlPoints = 0

        #adding tier 1 items into the counting list
        for item in itemsInBox:
            if item.tier == 1:
                itemCountList.append(item.name)
        #storing tier 1 item point values into order-specific variables
        orderrPoints = itemCountList.count("meat") * itemValueDict.get("meat")
        orderbPoints = itemCountList.count("weapon") * itemValueDict.get("weapon")
        orderyPoints = itemCountList.count("treasure") * itemValueDict.get("treasure")
        orderoPoints = itemCountList.count("light") * itemValueDict.get("light")
        ordergPoints = itemCountList.count("sleep") * itemValueDict.get("sleep")
        ordervPoints = itemCountList.count("fish") * itemValueDict.get("fish")
        orderpPoints = itemCountList.count("keys") * itemValueDict.get("keys")
        orderlPoints = itemCountList.count("bone") * itemValueDict.get("bone")
        itemCountList = [] #clearing counting list for tier 2 items

        #repeating process for tier 2 items
        for item in itemsInBox:
            if item.tier == 2:
                itemCountList.append(item.name)
        #this time tier 2 point multiplier is applied
        orderrPoints += itemCountList.count("meat") * itemValueDict.get("meat") * tier2ValueDict.get("meat")
        orderbPoints += itemCountList.count("weapon") * itemValueDict.get("weapon") * tier2ValueDict.get("weapon")
        orderyPoints += itemCountList.count("treasure") * itemValueDict.get("treasure") * tier2ValueDict.get("treasure")
        orderoPoints += itemCountList.count("light") * itemValueDict.get("light") * tier2ValueDict.get("light")
        ordergPoints += itemCountList.count("sleep") * itemValueDict.get("sleep") * tier2ValueDict.get("sleep")
        ordervPoints += itemCountList.count("fish") * itemValueDict.get("fish") * tier2ValueDict.get("fish")
        orderpPoints += itemCountList.count("keys") * itemValueDict.get("keys") * tier2ValueDict.get("keys")
        orderlPoints += itemCountList.count("bone") * itemValueDict.get("bone") * tier2ValueDict.get("bone")
        itemCountList = []

        #then the same for tier 3 items
        for item in itemsInBox:
            if item.tier == 3:
                itemCountList.append(item.name)

        orderrPoints += itemCountList.count("meat") * itemValueDict.get("meat") * tier3ValueDict.get("meat")
        orderbPoints += itemCountList.count("weapon") * itemValueDict.get("weapon") * tier3ValueDict.get("weapon")
        orderyPoints += itemCountList.count("treasure") * itemValueDict.get("treasure") * tier3ValueDict.get("treasure")
        orderoPoints += itemCountList.count("light") * itemValueDict.get("light") * tier3ValueDict.get("light")
        ordergPoints += itemCountList.count("sleep") * itemValueDict.get("sleep") * tier3ValueDict.get("sleep")
        ordervPoints += itemCountList.count("fish") * itemValueDict.get("fish") * tier3ValueDict.get("fish")
        orderpPoints += itemCountList.count("keys") * itemValueDict.get("keys") * tier3ValueDict.get("keys")
        orderlPoints += itemCountList.count("bone") * itemValueDict.get("bone") * tier3ValueDict.get("bone")

        #adding cee fish multiplier
        roundvPoints += roundvPoints*upgradesBought.get("fishNumber",0) 

        #adding combo points
        cOrderrPoints = orderpPoints*((1.1**upgradesBought.get("rpCombo",0))-1)
        cOrderrPoints = orderoPoints*((1.1**upgradesBought.get("roCombo",0))-1)
        cOrderoPoints = orderrPoints*((1.1**upgradesBought.get("roCombo",0))-1)
        cOrderoPoints = orderyPoints*((1.1**upgradesBought.get("yoCombo",0))-1)
        cOrderyPoints = orderoPoints*((1.1**upgradesBought.get("yoCombo",0))-1)
        cOrderyPoints = orderlPoints*((1.1**upgradesBought.get("ylCombo",0))-1)
        cOrderlPoints = orderyPoints*((1.1**upgradesBought.get("ylCombo",0))-1)
        cOrderlPoints = ordergPoints*((1.1**upgradesBought.get("glCombo",0))-1)
        cOrdergPoints = orderlPoints*((1.1**upgradesBought.get("glCombo",0))-1)
        cOrdergPoints = orderbPoints*((1.1**upgradesBought.get("gbCombo",0))-1)
        cOrderbPoints = ordergPoints*((1.1**upgradesBought.get("gbCombo",0))-1)
        cOrderbPoints = ordervPoints*((1.1**upgradesBought.get("vbCombo",0))-1)
        cOrdervPoints = orderbPoints*((1.1**upgradesBought.get("vbCombo",0))-1)
        cOrdervPoints = orderpPoints*((1.1**upgradesBought.get("vpCombo",0))-1)
        cOrderpPoints = ordervPoints*((1.1**upgradesBought.get("vpCombo",0))-1)
        cOrderpPoints = orderrPoints*((1.1**upgradesBought.get("rpCombo",0))-1)

        #adding cee upgrade bonus
        ordervPoints += (orderrPoints+orderbPoints+orderyPoints+ordergPoints+orderoPoints+orderpPoints+orderlPoints)*(1.1**upgradesBought.get("fishy",0))
        
        #adding combo points to order points
        orderrPoints += cOrderrPoints
        orderbPoints += cOrderbPoints
        orderyPoints += cOrderyPoints
        orderoPoints += cOrderoPoints
        ordergPoints += cOrdergPoints
        ordervPoints += cOrdervPoints
        orderpPoints += cOrderpPoints
        orderlPoints += cOrderlPoints

    #calculating capstone points
        capOrderrPoints = (orderbPoints*(1.1**upgradesBought.get("weaponCap",0)-1))+(orderyPoints*(1.1**upgradesBought.get("treasureCap",0)-1))+(ordergPoints*(1.1**upgradesBought.get("sleepCap",0)-1))+(orderoPoints*(1.1**upgradesBought.get("lightCap",0)-1))+(ordervPoints*(1.1**upgradesBought.get("fishCap",0)-1))+(orderpPoints*(1.1**upgradesBought.get("keysCap",0)-1))+(orderlPoints*(1.1**upgradesBought.get("boneCap",0)-1))
        capOrderbPoints = (orderrPoints*(1.1**upgradesBought.get("meatCap",0)-1))+(orderyPoints*(1.1**upgradesBought.get("treasureCap",0)-1))+(ordergPoints*(1.1**upgradesBought.get("sleepCap",0)-1))+(orderoPoints*(1.1**upgradesBought.get("lightCap",0)-1))+(ordervPoints*(1.1**upgradesBought.get("fishCap",0)-1))+(orderpPoints*(1.1**upgradesBought.get("keysCap",0)-1))+(orderlPoints*(1.1**upgradesBought.get("boneCap",0)-1))
        capOrderyPoints = (orderrPoints*(1.1**upgradesBought.get("meatCap",0)-1))+(orderbPoints*(1.1**upgradesBought.get("weaponCap",0)-1))+(ordergPoints*(1.1**upgradesBought.get("sleepCap",0)-1))+(orderoPoints*(1.1**upgradesBought.get("lightCap",0)-1))+(ordervPoints*(1.1**upgradesBought.get("fishCap",0)-1))+(orderpPoints*(1.1**upgradesBought.get("keysCap",0)-1))+(orderlPoints*(1.1**upgradesBought.get("boneCap",0)-1))
        capOrdergPoints = (orderrPoints*(1.1**upgradesBought.get("meatCap",0)-1))+(orderbPoints*(1.1**upgradesBought.get("weaponCap",0)-1))+(orderyPoints*(1.1**upgradesBought.get("treasureCap",0)-1))+(orderoPoints*(1.1**upgradesBought.get("lightCap",0)-1))+(ordervPoints*(1.1**upgradesBought.get("fishCap",0)-1))+(orderpPoints*(1.1**upgradesBought.get("keysCap",0)-1))+(orderlPoints*(1.1**upgradesBought.get("boneCap",0)-1))
        capOrderoPoints = (orderrPoints*(1.1**upgradesBought.get("meatCap",0)-1))+(orderbPoints*(1.1**upgradesBought.get("weaponCap",0)-1))+(orderyPoints*(1.1**upgradesBought.get("treasureCap",0)-1))+(ordergPoints*(1.1**upgradesBought.get("sleepCap",0)-1))+(ordervPoints*(1.1**upgradesBought.get("fishCap",0)-1))+(orderpPoints*(1.1**upgradesBought.get("keysCap",0)-1))+(orderlPoints*(1.1**upgradesBought.get("boneCap",0)-1))
        capOrdervPoints = (orderrPoints*(1.1**upgradesBought.get("meatCap",0)-1))+(orderbPoints*(1.1**upgradesBought.get("weaponCap",0)-1))+(orderyPoints*(1.1**upgradesBought.get("treasureCap",0)-1))+(ordergPoints*(1.1**upgradesBought.get("sleepCap",0)-1))+(orderoPoints*(1.1**upgradesBought.get("lightCap",0)-1))+(orderpPoints*(1.1**upgradesBought.get("keysCap",0)-1))+(orderlPoints*(1.1**upgradesBought.get("boneCap",0)-1))
        capOrderpPoints = (orderrPoints*(1.1**upgradesBought.get("meatCap",0)-1))+(orderbPoints*(1.1**upgradesBought.get("weaponCap",0)-1))+(orderyPoints*(1.1**upgradesBought.get("treasureCap",0)-1))+(ordergPoints*(1.1**upgradesBought.get("sleepCap",0)-1))+(orderoPoints*(1.1**upgradesBought.get("lightCap",0)-1))+(ordervPoints*(1.1**upgradesBought.get("fishCap",0)-1))+(orderlPoints*(1.1**upgradesBought.get("boneCap",0)-1))
        capOrderlPoints = (orderrPoints*(1.1**upgradesBought.get("meatCap",0)-1))+(orderbPoints*(1.1**upgradesBought.get("weaponCap",0)-1))+(orderyPoints*(1.1**upgradesBought.get("treasureCap",0)-1))+(ordergPoints*(1.1**upgradesBought.get("sleepCap",0)-1))+(orderoPoints*(1.1**upgradesBought.get("lightCap",0)-1))+(ordervPoints*(1.1**upgradesBought.get("fishCap",0)-1))+(orderpPoints*(1.1**upgradesBought.get("keysCap",0)-1))

        #adding capstone points to order points
        orderrPoints += capOrderrPoints
        orderbPoints += capOrderbPoints
        orderyPoints += capOrderyPoints
        orderoPoints += capOrderoPoints
        ordergPoints += capOrdergPoints
        ordervPoints += capOrdervPoints
        orderpPoints += capOrderpPoints
        orderlPoints += capOrderlPoints

        #checking for order validity and applying point multiplier
        if isOrderCorrect:
            validityFactor = 1
        else:
            validityFactor = failPoints

        #adjusting for order validity
        orderrPoints = orderrPoints*validityFactor
        orderbPoints = orderbPoints*validityFactor
        orderyPoints = orderyPoints*validityFactor
        orderoPoints = orderoPoints*validityFactor
        ordergPoints = ordergPoints*validityFactor
        ordervPoints = ordervPoints*validityFactor
        orderpPoints = orderpPoints*validityFactor
        orderlPoints = orderlPoints*validityFactor

        #adding order point totals into round point count
        roundrPoints += orderrPoints
        roundbPoints += orderbPoints
        roundyPoints += orderyPoints
        roundoPoints += orderoPoints
        roundgPoints += ordergPoints
        roundvPoints += ordervPoints
        roundpPoints += orderpPoints
        roundlPoints += orderlPoints

    def feedbackAmount():

        feedbackList = []

        if orderrpoints < 0:
            feedbackList.append("meat")

        if orderbpoints < 0:
            feedbackList.append("weapon")
            
        if orderypoints < 0:
            feedbackList.append("treasure")
            
        if ordergpoints < 0:
            feedbackList.append("sleep")
            
        if orderopoints < 0:
            feedbackList.append("light")
            
        if ordervpoints < 0:
            feedbackList.append("fish")
            
        if orderppoints < 0:
            feedbackList.append("keys")
            
        if orderlpoints < 0:
            feedbackList.append("bone")

transform point_feedback_transform_1:
    xalign 0.5
    yalign 1.1

    parallel:
        easein 0.3 yoffset -200
        easeout 0.3 yoffset 200

    parallel:
        alpha 0
        linear 0.1 alpha 1.0
        linear 0.5 alpha 0

transform point_feedback_transform_2:
    xalign 0.5
    yalign 1.1

    parallel:
        easein 0.3 yoffset -200
        easeout 0.3 yoffset 200

    parallel:
        alpha 0
        linear 0.1 alpha 1.0
        linear 0.5 alpha 0

    parallel:
        xoffset 0
        linear 0.6 xoffset 100

transform point_feedback_transform_3:
    xalign 0.5
    yalign 1.1

    parallel:
        easein 0.3 yoffset -200
        easeout 0.3 yoffset 200

    parallel:
        alpha 0
        linear 0.1 alpha 1.0
        linear 0.5 alpha 0

    parallel:
        xoffset 0
        linear 0.6 xoffset -100
        
transform point_feedback_transform_4:
    xalign 0.5
    yalign 1.1

    parallel:
        easein 0.3 yoffset -200
        easeout 0.3 yoffset 200

    parallel:
        alpha 0
        linear 0.1 alpha 1.0
        linear 0.5 alpha 0

    parallel:
        xoffset 0
        linear 0.6 xoffset 200

transform point_feedback_transform_5:
    xalign 0.5
    yalign 1.1

    parallel:
        easein 0.3 yoffset -200
        easeout 0.3 yoffset 200

    parallel:
        alpha 0
        linear 0.1 alpha 1.0
        linear 0.5 alpha 0

    parallel:
        xoffset 0
        linear 0.6 xoffset -200
        
transform point_feedback_transform_6:
    xalign 0.5
    yalign 1.1

    parallel:
        easein 0.3 yoffset -200
        easeout 0.3 yoffset 200

    parallel:
        alpha 0
        linear 0.1 alpha 1.0
        linear 0.5 alpha 0

    parallel:
        xoffset 0
        linear 0.6 xoffset 300

transform point_feedback_transform_7:
    xalign 0.5
    yalign 1.1

    parallel:
        easein 0.3 yoffset -200
        easeout 0.3 yoffset 200

    parallel:
        alpha 0
        linear 0.1 alpha 1.0
        linear 0.5 alpha 0

    parallel:
        xoffset 0
        linear 0.6 xoffset -300
        
transform point_feedback_transform_8:
    xalign 0.5
    yalign 1.1

    parallel:
        easein 0.3 yoffset -200
        easeout 0.3 yoffset 200

    parallel:
        alpha 0
        linear 0.1 alpha 1.0
        linear 0.5 alpha 0

    parallel:
        xoffset 0
        linear 0.6 xoffset 400

transform point_feedback_transform_9:
    xalign 0.5
    yalign 1.1

    parallel:
        easein 0.3 yoffset -200
        easeout 0.3 yoffset 200

    parallel:
        alpha 0
        linear 0.1 alpha 1.0
        linear 0.5 alpha 0

    parallel:
        xoffset 0
        linear 0.6 xoffset -400
'''
screen pointFeedback:
    if "meat" in feedbackList:
        if len(feedbackList) == 1:
            use meatFeedback:
                at point_feedback_transform_1
        elif len(feedbackList) < 4:
            use meatFeedback at point_feedback_transform_3
        elif len(feedbackList) < 6:
            use meatFeedback at point_feedback_transform_5
        elif len(feedbackList) < 8:
            use meatFeedback at point_feedback_transform_5
'''

screen meatFeedback:
    vbox:
        text "{size=+10}[orderrPoints]" style "redPointsStyle"
        add "order meat.png":
            fit "scale-down"
            xysize (50,50)
            
screen weaponFeedback:
    vbox:
        text "{size=+10}[orderbPoints]" style "bluePointsStyle"
        add "order weapon.png":
            fit "scale-down"
            xysize (50,50)
            
screen treasureFeedback:
    vbox:
        text "{size=+10}[orderyPoints]" style "yellowPointsStyle"
        add "order treasure.png":
            fit "scale-down"
            xysize (50,50)
            
screen sleepFeedback:
    vbox:
        text "{size=+10}[orderrPoints]" style "greenPointsStyle"
        add "order sleep.png":
            fit "scale-down"
            xysize (50,50)
            
screen lightFeedback:
    vbox:
        text "{size=+10}[orderrPoints]" style "orangePointsStyle"
        add "order light.png":
            fit "scale-down"
            xysize (50,50)
            
screen fishFeedback:
    vbox:
        text "{size=+10}[orderrPoints]" style "violetPointsStyle"
        add "order fish.png":
            fit "scale-down"
            xysize (50,50)
            
screen keysFeedback:
    vbox:
        text "{size=+10}[orderrPoints]" style "pinkPointsStyle"
        add "order keys.png":
            fit "scale-down"
            xysize (50,50)
            
screen boneFeedback:
    vbox:
        text "{size=+10}[orderrPoints]" style "lightPointsStyle"
        add "order bone.png":
            fit "scale-down"
            xysize (50,50)
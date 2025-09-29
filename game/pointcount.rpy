
default feedbackList = []
default rfeedbackPosition = 1
default bfeedbackPosition = 1
default yfeedbackPosition = 1
default gfeedbackPosition = 1
default ofeedbackPosition = 1
default vfeedbackPosition = 1
default pfeedbackPosition = 1
default lfeedbackPosition = 1

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
        ordervPoints += ordervPoints*upgradesBought.get("fishNumber",0) 

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

        #adding cee moist upgrade bonus
        ordervPoints += (orderrPoints+orderbPoints+orderyPoints+ordergPoints+orderoPoints+orderpPoints+orderlPoints)*(1.1**upgradesBought.get("fishy",0)-1)
        
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

        #setting point feedback
        feedbackAmount()

    def feedbackAmount():

        global feedbackList

        feedbackList = []

        if orderrPoints > 0:
            feedbackList.append("meat")

        if orderbPoints > 0:
            feedbackList.append("weapon")
            
        if orderyPoints > 0:
            feedbackList.append("treasure")
            
        if ordergPoints > 0:
            feedbackList.append("sleep")
            
        if orderoPoints > 0:
            feedbackList.append("light")
            
        if ordervPoints > 0:
            feedbackList.append("fish")
            
        if orderpPoints > 0:
            feedbackList.append("keys")
            
        if orderlPoints > 0:
            feedbackList.append("bone")

        

transform point_feedback_transform_1:
    xalign 0.05 
    yalign 0.9

    parallel:
        easein 1.0 yoffset -200
        ease 1.0 yoffset 100

    parallel:
        alpha 0
        linear 0.1 alpha 1.0
        pause 1.4
        linear 0.5 alpha 0

transform point_feedback_transform_2:
    xalign 0.05 
    yalign 0.9

    parallel:
        easein 1.0 yoffset -200
        ease 1.0 yoffset 100

    parallel:
        alpha 0
        linear 0.1 alpha 1.0
        pause 1.4
        linear 0.5 alpha 0

    parallel:
        xoffset 0
        easein 2.0 xoffset 100

transform point_feedback_transform_3:
    xalign 0.05 
    yalign 0.9

    parallel:
        easein 1.0 yoffset -200
        ease 1.0 yoffset 100

    parallel:
        alpha 0
        linear 0.1 alpha 1.0
        pause 1.4
        linear 0.5 alpha 0

    parallel:
        xoffset 0
        easein 2.0 xoffset -100
        
transform point_feedback_transform_4:
    xalign 0.05 
    yalign 0.9

    parallel:
        easein 1.0 yoffset -200
        ease 1.0 yoffset 100

    parallel:
        alpha 0
        linear 0.1 alpha 1.0
        pause 1.4
        linear 0.5 alpha 0

    parallel:
        xoffset 0
        easein 2.0 xoffset 200

transform point_feedback_transform_5:
    xalign 0.05 
    yalign 0.9

    parallel:
        easein 1.0 yoffset -200
        ease 1.0 yoffset 100

    parallel:
        alpha 0
        linear 0.1 alpha 1.0
        pause 1.4
        linear 0.5 alpha 0

    parallel:
        xoffset 0
        easein 2.0 xoffset -200
        
transform point_feedback_transform_6:
    xalign 0.05 
    yalign 0.9

    parallel:
        easein 1.0 yoffset -200
        ease 1.0 yoffset 100

    parallel:
        alpha 0
        linear 0.1 alpha 1.0
        pause 1.4
        linear 0.5 alpha 0

    parallel:
        xoffset 0
        easein 2.0 xoffset 300

transform point_feedback_transform_7:
    xalign 0.05 
    yalign 0.9

    parallel:
        easein 1.0 yoffset -200
        ease 1.0 yoffset 100

    parallel:
        alpha 0
        linear 0.1 alpha 1.0
        pause 1.4
        linear 0.5 alpha 0

    parallel:
        xoffset 0
        easein 2.0 xoffset -300
        
transform point_feedback_transform_8:
    xalign 0.05 
    yalign 0.9

    parallel:
        easein 1.0 yoffset -200
        ease 1.0 yoffset 100

    parallel:
        alpha 0
        linear 0.1 alpha 1.0
        pause 1.4
        linear 0.5 alpha 0

    parallel:
        xoffset 0
        easein 2.0 xoffset 400

transform point_feedback_transform_9:
    xalign 0.05 
    yalign 0.9

    parallel:
        easein 1.0 yoffset -200
        ease 1.0 yoffset 100

    parallel:
        alpha 0
        linear 0.1 alpha 1.0
        pause 1.4
        linear 0.5 alpha 0

    parallel:
        xoffset 0
        easein 2.0 xoffset -400

screen pointFeedback:
    zorder 200
    timer 2.1 action Hide("pointFeedback")
    if len(feedbackList) == 1:
        if "meat" in feedbackList:
            timer 0.1 action [SetVariable("rfeedbackPosition", 1), Show("meatFeedback")]
        elif "weapon" in feedbackList:
            timer 0.1 action [SetVariable("bfeedbackPosition", 1), Show("weaponFeedback")]
        elif "treasure" in feedbackList:
            timer 0.1 action [SetVariable("yfeedbackPosition", 1), Show("treasureFeedback")]
        elif "sleep" in feedbackList:
            timer 0.1 action [SetVariable("gfeedbackPosition", 1), Show("sleepFeedback")]
        elif "light" in feedbackList:
            timer 0.1 action [SetVariable("ofeedbackPosition", 1), Show("lightFeedback")]
        elif "fish" in feedbackList:
            timer 0.1 action [SetVariable("vfeedbackPosition", 1), Show("fishFeedback")]
        elif "keys" in feedbackList:
            timer 0.1 action [SetVariable("pfeedbackPosition", 1), Show("keysFeedback")]
        elif "bone" in feedbackList:
            timer 0.1 action [SetVariable("lfeedbackPosition", 1), Show("boneFeedback")]
    elif len(feedbackList) == 2:
        if "meat" in feedbackList:
            if feedbackList[0] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 2), Show("meatFeedback")]
            else:
                timer 0.1 action [SetVariable("rfeedbackPosition", 3), Show("meatFeedback")]
        if "weapon" in feedbackList:
            if feedbackList[0] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 2), Show("weaponFeedback")]
            else:
                timer 0.1 action [SetVariable("bfeedbackPosition", 3), Show("weaponFeedback")]
        if "treasure" in feedbackList:
            if feedbackList[0] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 2), Show("treasureFeedback")]
            else:
                timer 0.1 action [SetVariable("yfeedbackPosition", 3), Show("treasureFeedback")]
        if "sleep" in feedbackList:
            if feedbackList[0] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 2), Show("sleepFeedback")]
            else:
                timer 0.1 action [SetVariable("gfeedbackPosition", 3), Show("treasureFeedback")]
        if "light" in feedbackList:
            if feedbackList[0] == "light":
                timer 0.1 action [SetVariable("lfeedbackPosition", 2), Show("lightFeedback")]
            else:
                timer 0.1 action [SetVariable("lfeedbackPosition", 3), Show("treasureFeedback")]
        if "fish" in feedbackList:
            if feedbackList[0] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 2), Show("fishFeedback")]
            else:
                timer 0.1 action [SetVariable("vfeedbackPosition", 3), Show("fishFeedback")]
        if "keys" in feedbackList:
            if feedbackList[0] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 2), Show("keysFeedback")]
            else:
                timer 0.1 action [SetVariable("pfeedbackPosition", 3), Show("keysFeedback")]
        if "bone" in feedbackList:
            if feedbackList[0] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 2), Show("boneFeedback")]
            else:
                timer 0.1 action [SetVariable("lfeedbackPosition", 3), Show("boneFeedback")]
        
    elif len(feedbackList) == 3:
        if "meat" in feedbackList:
            if feedbackList[0] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 2), Show("meatFeedback")]
            elif feedbackList[1] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 1), Show("meatFeedback")]
            else:
                timer 0.1 action [SetVariable("rfeedbackPosition", 3), Show("meatFeedback")]
        if "weapon" in feedbackList:
            if feedbackList[0] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 2), Show("weaponFeedback")]
            elif feedbackList[1] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 1), Show("weaponFeedback")]
            else:
                timer 0.1 action [SetVariable("bfeedbackPosition", 3), Show("weaponFeedback")]
        if "treasure" in feedbackList:
            if feedbackList[0] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 2), Show("treasureFeedback")]
            elif feedbackList[1] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 1), Show("treasureFeedback")]
            else:
                timer 0.1 action [SetVariable("yfeedbackPosition", 3), Show("treasureFeedback")]
        if "sleep" in feedbackList:
            if feedbackList[0] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 2), Show("sleepFeedback")]
            elif feedbackList[1] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 1), Show("sleepFeedback")]
            else:
                timer 0.1 action [SetVariable("gfeedbackPosition", 3), Show("treasureFeedback")]
        if "light" in feedbackList:
            if feedbackList[0] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 2), Show("lightFeedback")]
            elif feedbackList[1] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 1), Show("lightFeedback")]
            else:
                timer 0.1 action [SetVariable("ofeedbackPosition", 3), Show("treasureFeedback")]
        if "fish" in feedbackList:
            if feedbackList[0] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 2), Show("fishFeedback")]
            elif feedbackList[1] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 1), Show("fishFeedback")]
            else:
                timer 0.1 action [SetVariable("vfeedbackPosition", 3), Show("fishFeedback")]
        if "keys" in feedbackList:
            if feedbackList[0] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 2), Show("keysFeedback")]
            elif feedbackList[1] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 1), Show("keysFeedback")]
            else:
                timer 0.1 action [SetVariable("pfeedbackPosition", 3), Show("keysFeedback")]
        if "bone" in feedbackList:
            if feedbackList[0] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 2), Show("boneFeedback")]
            elif feedbackList[1] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 1), Show("boneFeedback")]
            else:
                timer 0.1 action [SetVariable("lfeedbackPosition", 3), Show("boneFeedback")]

    elif len(feedbackList) == 4:
        if "meat" in feedbackList:
            if feedbackList[0] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 4), Show("meatFeedback")]
            elif feedbackList[1] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 2), Show("meatFeedback")]
            elif feedbackList[2] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 3), Show("meatFeedback")]
            else:
                timer 0.1 action [SetVariable("rfeedbackPosition", 5), Show("meatFeedback")]
        if "weapon" in feedbackList:
            if feedbackList[0] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 4), Show("weaponFeedback")]
            elif feedbackList[1] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 2), Show("weaponFeedback")]
            elif feedbackList[2] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 3), Show("weaponFeedback")]
            else:
                timer 0.1 action [SetVariable("bfeedbackPosition", 5), Show("weaponFeedback")]
        if "treasure" in feedbackList:
            if feedbackList[0] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 4), Show("treasureFeedback")]
            elif feedbackList[1] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 2), Show("treasureFeedback")]
            elif feedbackList[2] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 3), Show("treasureFeedback")]
            else:
                timer 0.1 action [SetVariable("yfeedbackPosition", 5), Show("treasureFeedback")]
        if "sleep" in feedbackList:
            if feedbackList[0] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 4), Show("sleepFeedback")]
            elif feedbackList[1] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 2), Show("sleepFeedback")]
            elif feedbackList[2] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 3), Show("sleepFeedback")]
            else:
                timer 0.1 action [SetVariable("gfeedbackPosition", 5), Show("treasureFeedback")]
        if "light" in feedbackList:
            if feedbackList[0] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 4), Show("lightFeedback")]
            elif feedbackList[1] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 2), Show("lightFeedback")]
            elif feedbackList[2] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 3), Show("lightFeedback")]
            else:
                timer 0.1 action [SetVariable("ofeedbackPosition", 5), Show("treasureFeedback")]
        if "fish" in feedbackList:
            if feedbackList[0] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 4), Show("fishFeedback")]
            elif feedbackList[1] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 2), Show("fishFeedback")]
            elif feedbackList[2] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 3), Show("fishFeedback")]
            else:
                timer 0.1 action [SetVariable("vfeedbackPosition", 5), Show("fishFeedback")]
        if "keys" in feedbackList:
            if feedbackList[0] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 4), Show("keysFeedback")]
            elif feedbackList[1] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 2), Show("keysFeedback")]
            elif feedbackList[2] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 3), Show("keysFeedback")]
            else:
                timer 0.1 action [SetVariable("pfeedbackPosition", 5), Show("keysFeedback")]
        if "bone" in feedbackList:
            if feedbackList[0] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 4), Show("boneFeedback")]
            elif feedbackList[1] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 2), Show("boneFeedback")]
            elif feedbackList[2] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 3), Show("boneFeedback")]
            else:
                timer 0.1 action [SetVariable("lfeedbackPosition", 5), Show("boneFeedback")]

    elif len(feedbackList) == 5:
        if "meat" in feedbackList:
            if feedbackList[0] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 4), Show("meatFeedback")]
            elif feedbackList[1] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 2), Show("meatFeedback")]
            elif feedbackList[2] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 1), Show("meatFeedback")]
            elif feedbackList[3] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 3), Show("meatFeedback")]
            else:
                timer 0.1 action [SetVariable("rfeedbackPosition", 5), Show("meatFeedback")]
        if "weapon" in feedbackList:
            if feedbackList[0] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 4), Show("weaponFeedback")]
            elif feedbackList[1] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 2), Show("weaponFeedback")]
            elif feedbackList[2] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 1), Show("weaponFeedback")]
            elif feedbackList[3] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 3), Show("weaponFeedback")]
            else:
                timer 0.1 action [SetVariable("bfeedbackPosition", 5), Show("weaponFeedback")]
        if "treasure" in feedbackList:
            if feedbackList[0] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 4), Show("treasureFeedback")]
            elif feedbackList[1] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 2), Show("treasureFeedback")]
            elif feedbackList[2] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 1), Show("treasureFeedback")]
            elif feedbackList[3] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 3), Show("treasureFeedback")]
            else:
                timer 0.1 action [SetVariable("yfeedbackPosition", 5), Show("treasureFeedback")]
        if "sleep" in feedbackList:
            if feedbackList[0] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 4), Show("sleepFeedback")]
            elif feedbackList[1] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 2), Show("sleepFeedback")]
            elif feedbackList[2] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 1), Show("sleepFeedback")]
            elif feedbackList[3] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 3), Show("sleepFeedback")]
            else:
                timer 0.1 action [SetVariable("gfeedbackPosition", 5), Show("treasureFeedback")]
        if "light" in feedbackList:
            if feedbackList[0] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 4), Show("lightFeedback")]
            elif feedbackList[1] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 2), Show("lightFeedback")]
            elif feedbackList[2] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 1), Show("lightFeedback")]
            elif feedbackList[3] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 3), Show("lightFeedback")]
            else:
                timer 0.1 action [SetVariable("ofeedbackPosition", 5), Show("treasureFeedback")]
        if "fish" in feedbackList:
            if feedbackList[0] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 4), Show("fishFeedback")]
            elif feedbackList[1] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 2), Show("fishFeedback")]
            elif feedbackList[2] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 1), Show("fishFeedback")]
            elif feedbackList[3] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 3), Show("fishFeedback")]
            else:
                timer 0.1 action [SetVariable("vfeedbackPosition", 5), Show("fishFeedback")]
        if "keys" in feedbackList:
            if feedbackList[0] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 4), Show("keysFeedback")]
            elif feedbackList[1] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 2), Show("keysFeedback")]
            elif feedbackList[2] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 1), Show("keysFeedback")]
            elif feedbackList[3] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 3), Show("keysFeedback")]
            else:
                timer 0.1 action [SetVariable("pfeedbackPosition", 5), Show("keysFeedback")]
        if "bone" in feedbackList:
            if feedbackList[0] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 4), Show("boneFeedback")]
            elif feedbackList[1] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 2), Show("boneFeedback")]
            elif feedbackList[2] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 1), Show("boneFeedback")]
            elif feedbackList[3] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 3), Show("boneFeedback")]
            else:
                timer 0.1 action [SetVariable("lfeedbackPosition", 5), Show("boneFeedback")]
        
    elif len(feedbackList) == 6:
        if "meat" in feedbackList:
            if feedbackList[0] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 6), Show("meatFeedback")]
            elif feedbackList[1] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 4), Show("meatFeedback")]
            elif feedbackList[2] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 2), Show("meatFeedback")]
            elif feedbackList[3] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 3), Show("meatFeedback")]
            elif feedbackList[4] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 5), Show("meatFeedback")]
            else:
                timer 0.1 action [SetVariable("rfeedbackPosition", 7), Show("meatFeedback")]
        if "weapon" in feedbackList:
            if feedbackList[0] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 6), Show("weaponFeedback")]
            elif feedbackList[1] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 4), Show("weaponFeedback")]
            elif feedbackList[2] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 2), Show("weaponFeedback")]
            elif feedbackList[3] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 3), Show("weaponFeedback")]
            elif feedbackList[4] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 5), Show("weaponFeedback")]
            else:
                timer 0.1 action [SetVariable("bfeedbackPosition", 7), Show("weaponFeedback")]
        if "treasure" in feedbackList:
            if feedbackList[0] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 6), Show("treasureFeedback")]
            elif feedbackList[1] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 4), Show("treasureFeedback")]
            elif feedbackList[2] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 2), Show("treasureFeedback")]
            elif feedbackList[3] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 3), Show("treasureFeedback")]
            elif feedbackList[4] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 5), Show("treasureFeedback")]
            else:
                timer 0.1 action [SetVariable("yfeedbackPosition", 7), Show("treasureFeedback")]
        if "sleep" in feedbackList:
            if feedbackList[0] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 6), Show("sleepFeedback")]
            elif feedbackList[1] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 4), Show("sleepFeedback")]
            elif feedbackList[2] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 2), Show("sleepFeedback")]
            elif feedbackList[3] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 3), Show("sleepFeedback")]
            elif feedbackList[4] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 5), Show("sleepFeedback")]
            else:
                timer 0.1 action [SetVariable("gfeedbackPosition", 7), Show("treasureFeedback")]
        if "light" in feedbackList:
            if feedbackList[0] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 6), Show("lightFeedback")]
            elif feedbackList[1] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 4), Show("lightFeedback")]
            elif feedbackList[2] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 2), Show("lightFeedback")]
            elif feedbackList[3] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 3), Show("lightFeedback")]
            elif feedbackList[4] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 5), Show("lightFeedback")]
            else:
                timer 0.1 action [SetVariable("ofeedbackPosition", 7), Show("treasureFeedback")]
        if "fish" in feedbackList:
            if feedbackList[0] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 6), Show("fishFeedback")]
            elif feedbackList[1] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 4), Show("fishFeedback")]
            elif feedbackList[2] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 2), Show("fishFeedback")]
            elif feedbackList[3] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 3), Show("fishFeedback")]
            elif feedbackList[4] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 5), Show("fishFeedback")]
            else:
                timer 0.1 action [SetVariable("vfeedbackPosition", 7), Show("fishFeedback")]
        if "keys" in feedbackList:
            if feedbackList[0] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 6), Show("keysFeedback")]
            elif feedbackList[1] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 4), Show("keysFeedback")]
            elif feedbackList[2] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 2), Show("keysFeedback")]
            elif feedbackList[3] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 3), Show("keysFeedback")]
            elif feedbackList[4] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 5), Show("keysFeedback")]
            else:
                timer 0.1 action [SetVariable("pfeedbackPosition", 7), Show("keysFeedback")]
        if "bone" in feedbackList:
            if feedbackList[0] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 6), Show("boneFeedback")]
            elif feedbackList[1] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 4), Show("boneFeedback")]
            elif feedbackList[2] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 2), Show("boneFeedback")]
            elif feedbackList[3] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 3), Show("boneFeedback")]
            elif feedbackList[4] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 5), Show("boneFeedback")]
            else:
                timer 0.1 action [SetVariable("lfeedbackPosition", 7), Show("boneFeedback")]

    elif len(feedbackList) == 7:
        if "meat" in feedbackList:
            if feedbackList[0] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 6), Show("meatFeedback")]
            elif feedbackList[1] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 4), Show("meatFeedback")]
            elif feedbackList[2] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 2), Show("meatFeedback")]
            elif feedbackList[3] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 1), Show("meatFeedback")]
            elif feedbackList[4] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 3), Show("meatFeedback")]
            elif feedbackList[5] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 5), Show("meatFeedback")]
            else:
                timer 0.1 action [SetVariable("rfeedbackPosition", 7), Show("meatFeedback")]
        if "weapon" in feedbackList:
            if feedbackList[0] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 6), Show("weaponFeedback")]
            elif feedbackList[1] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 4), Show("weaponFeedback")]
            elif feedbackList[2] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 2), Show("weaponFeedback")]
            elif feedbackList[3] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 1), Show("weaponFeedback")]
            elif feedbackList[4] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 3), Show("weaponFeedback")]
            elif feedbackList[5] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 5), Show("weaponFeedback")]
            else:
                timer 0.1 action [SetVariable("bfeedbackPosition", 7), Show("weaponFeedback")]
        if "treasure" in feedbackList:
            if feedbackList[0] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 6), Show("treasureFeedback")]
            elif feedbackList[1] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 4), Show("treasureFeedback")]
            elif feedbackList[2] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 2), Show("treasureFeedback")]
            elif feedbackList[3] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 1), Show("treasureFeedback")]
            elif feedbackList[4] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 3), Show("treasureFeedback")]
            elif feedbackList[5] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 5), Show("treasureFeedback")]
            else:
                timer 0.1 action [SetVariable("yfeedbackPosition", 7), Show("treasureFeedback")]
        if "sleep" in feedbackList:
            if feedbackList[0] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 6), Show("sleepFeedback")]
            elif feedbackList[1] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 4), Show("sleepFeedback")]
            elif feedbackList[2] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 2), Show("sleepFeedback")]
            elif feedbackList[3] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 1), Show("sleepFeedback")]
            elif feedbackList[4] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 3), Show("sleepFeedback")]
            elif feedbackList[5] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 5), Show("sleepFeedback")]
            else:
                timer 0.1 action [SetVariable("gfeedbackPosition", 7), Show("treasureFeedback")]
        if "light" in feedbackList:
            if feedbackList[0] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 6), Show("lightFeedback")]
            elif feedbackList[1] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 4), Show("lightFeedback")]
            elif feedbackList[2] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 2), Show("lightFeedback")]
            elif feedbackList[3] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 1), Show("lightFeedback")]
            elif feedbackList[4] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 3), Show("lightFeedback")]
            elif feedbackList[5] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 5), Show("lightFeedback")]
            else:
                timer 0.1 action [SetVariable("ofeedbackPosition", 7), Show("treasureFeedback")]
        if "fish" in feedbackList:
            if feedbackList[0] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 6), Show("fishFeedback")]
            elif feedbackList[1] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 4), Show("fishFeedback")]
            elif feedbackList[2] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 2), Show("fishFeedback")]
            elif feedbackList[3] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 1), Show("fishFeedback")]
            elif feedbackList[4] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 3), Show("fishFeedback")]
            elif feedbackList[5] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 5), Show("fishFeedback")]
            else:
                timer 0.1 action [SetVariable("vfeedbackPosition", 7), Show("fishFeedback")]
        if "keys" in feedbackList:
            if feedbackList[0] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 6), Show("keysFeedback")]
            elif feedbackList[1] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 4), Show("keysFeedback")]
            elif feedbackList[2] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 2), Show("keysFeedback")]
            elif feedbackList[3] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 1), Show("keysFeedback")]
            elif feedbackList[4] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 3), Show("keysFeedback")]
            elif feedbackList[5] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 5), Show("keysFeedback")]
            else:
                timer 0.1 action [SetVariable("pfeedbackPosition", 7), Show("keysFeedback")]
        if "bone" in feedbackList:
            if feedbackList[0] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 6), Show("boneFeedback")]
            elif feedbackList[1] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 4), Show("boneFeedback")]
            elif feedbackList[2] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 2), Show("boneFeedback")]
            elif feedbackList[3] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 1), Show("boneFeedback")]
            elif feedbackList[4] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 3), Show("boneFeedback")]
            elif feedbackList[5] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 5), Show("boneFeedback")]
            else:
                timer 0.1 action [SetVariable("lfeedbackPosition", 7), Show("boneFeedback")]

    else:
        if "meat" in feedbackList:
            if feedbackList[0] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 8), Show("meatFeedback")]
            elif feedbackList[1] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 6), Show("meatFeedback")]
            elif feedbackList[2] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 4), Show("meatFeedback")]
            elif feedbackList[3] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 2), Show("meatFeedback")]
            elif feedbackList[4] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 3), Show("meatFeedback")]
            elif feedbackList[5] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 5), Show("meatFeedback")]
            elif feedbackList[6] == "meat":
                timer 0.1 action [SetVariable("rfeedbackPosition", 7), Show("meatFeedback")]
            else:
                timer 0.1 action [SetVariable("rfeedbackPosition", 9), Show("meatFeedback")]
        if "weapon" in feedbackList:
            if feedbackList[0] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 8), Show("weaponFeedback")]
            elif feedbackList[1] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 6), Show("weaponFeedback")]
            elif feedbackList[2] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 4), Show("weaponFeedback")]
            elif feedbackList[3] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 2), Show("weaponFeedback")]
            elif feedbackList[4] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 3), Show("weaponFeedback")]
            elif feedbackList[5] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 5), Show("weaponFeedback")]
            elif feedbackList[6] == "weapon":
                timer 0.1 action [SetVariable("bfeedbackPosition", 7), Show("weaponFeedback")]
            else:
                timer 0.1 action [SetVariable("bfeedbackPosition", 9), Show("weaponFeedback")]
        if "treasure" in feedbackList:
            if feedbackList[0] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 8), Show("treasureFeedback")]
            elif feedbackList[1] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 6), Show("treasureFeedback")]
            elif feedbackList[2] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 4), Show("treasureFeedback")]
            elif feedbackList[3] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 2), Show("treasureFeedback")]
            elif feedbackList[4] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 3), Show("treasureFeedback")]
            elif feedbackList[5] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 5), Show("treasureFeedback")]
            elif feedbackList[6] == "treasure":
                timer 0.1 action [SetVariable("yfeedbackPosition", 7), Show("treasureFeedback")]
            else:
                timer 0.1 action [SetVariable("yfeedbackPosition", 9), Show("treasureFeedback")]
        if "sleep" in feedbackList:
            if feedbackList[0] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 8), Show("sleepFeedback")]
            elif feedbackList[1] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 6), Show("sleepFeedback")]
            elif feedbackList[2] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 4), Show("sleepFeedback")]
            elif feedbackList[3] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 2), Show("sleepFeedback")]
            elif feedbackList[4] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 3), Show("sleepFeedback")]
            elif feedbackList[5] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 5), Show("sleepFeedback")]
            elif feedbackList[6] == "sleep":
                timer 0.1 action [SetVariable("gfeedbackPosition", 7), Show("sleepFeedback")]
            else:
                timer 0.1 action [SetVariable("gfeedbackPosition", 9), Show("treasureFeedback")]
        if "light" in feedbackList:
            if feedbackList[0] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 8), Show("lightFeedback")]
            elif feedbackList[1] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 6), Show("lightFeedback")]
            elif feedbackList[2] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 4), Show("lightFeedback")]
            elif feedbackList[3] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 2), Show("lightFeedback")]
            elif feedbackList[4] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 3), Show("lightFeedback")]
            elif feedbackList[5] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 5), Show("lightFeedback")]
            elif feedbackList[6] == "light":
                timer 0.1 action [SetVariable("ofeedbackPosition", 7), Show("lightFeedback")]
            else:
                timer 0.1 action [SetVariable("ofeedbackPosition", 9), Show("treasureFeedback")]
        if "fish" in feedbackList:
            if feedbackList[0] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 8), Show("fishFeedback")]
            elif feedbackList[1] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 6), Show("fishFeedback")]
            elif feedbackList[2] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 4), Show("fishFeedback")]
            elif feedbackList[3] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 2), Show("fishFeedback")]
            elif feedbackList[4] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 3), Show("fishFeedback")]
            elif feedbackList[5] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 5), Show("fishFeedback")]
            elif feedbackList[6] == "fish":
                timer 0.1 action [SetVariable("vfeedbackPosition", 7), Show("fishFeedback")]
            else:
                timer 0.1 action [SetVariable("vfeedbackPosition", 9), Show("fishFeedback")]
        if "keys" in feedbackList:
            if feedbackList[0] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 8), Show("keysFeedback")]
            elif feedbackList[1] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 6), Show("keysFeedback")]
            elif feedbackList[2] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 4), Show("keysFeedback")]
            elif feedbackList[3] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 2), Show("keysFeedback")]
            elif feedbackList[4] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 3), Show("keysFeedback")]
            elif feedbackList[5] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 5), Show("keysFeedback")]
            elif feedbackList[6] == "keys":
                timer 0.1 action [SetVariable("pfeedbackPosition", 7), Show("keysFeedback")]
            else:
                timer 0.1 action [SetVariable("pfeedbackPosition", 9), Show("keysFeedback")]
        if "bone" in feedbackList:
            if feedbackList[0] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 8), Show("boneFeedback")]
            elif feedbackList[1] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 6), Show("boneFeedback")]
            elif feedbackList[2] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 4), Show("boneFeedback")]
            elif feedbackList[3] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 2), Show("boneFeedback")]
            elif feedbackList[4] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 3), Show("boneFeedback")]
            elif feedbackList[5] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 5), Show("boneFeedback")]
            elif feedbackList[6] == "bone":
                timer 0.1 action [SetVariable("lfeedbackPosition", 7), Show("boneFeedback")]
            else:
                timer 0.1 action [SetVariable("lfeedbackPosition", 9), Show("boneFeedback")]

screen meatFeedback:
    timer 2.0 action Hide("meatFeedback")
    hbox:
        if rfeedbackPosition == 1:
            at point_feedback_transform_1
        elif rfeedbackPosition == 2:
            at point_feedback_transform_2
        elif rfeedbackPosition == 3:
            at point_feedback_transform_3
        elif rfeedbackPosition == 4:
            at point_feedback_transform_4
        elif rfeedbackPosition == 5:
            at point_feedback_transform_5
        elif rfeedbackPosition == 6:
            at point_feedback_transform_6
        elif rfeedbackPosition == 7:
            at point_feedback_transform_7
        elif rfeedbackPosition == 8:
            at point_feedback_transform_8
        elif rfeedbackPosition == 9:
            at point_feedback_transform_9
        text "{size=+30}+[orderrPoints]" style "redPointsStyle"
        add "order meat.png":
            fit "scale-down"
            xysize (70,70)
            
screen weaponFeedback:
    timer 2.0 action Hide("weaponFeedback")
    hbox:
        if bfeedbackPosition == 1:
            at point_feedback_transform_1
        elif bfeedbackPosition == 2:
            at point_feedback_transform_2
        elif bfeedbackPosition == 3:
            at point_feedback_transform_3
        elif bfeedbackPosition == 4:
            at point_feedback_transform_4
        elif bfeedbackPosition == 5:
            at point_feedback_transform_5
        elif bfeedbackPosition == 6:
            at point_feedback_transform_6
        elif bfeedbackPosition == 7:
            at point_feedback_transform_7
        elif bfeedbackPosition == 8:
            at point_feedback_transform_8
        elif bfeedbackPosition == 9:
            at point_feedback_transform_9
        text "{size=+30}+[orderbPoints]" style "bluePointsStyle"
        add "order weapon.png":
            fit "scale-down"
            xysize (70,70)
            
screen treasureFeedback:
    timer 2.0 action Hide("treasureFeedback")
    hbox:
        if yfeedbackPosition == 1:
            at point_feedback_transform_1
        elif yfeedbackPosition == 2:
            at point_feedback_transform_2
        elif yfeedbackPosition == 3:
            at point_feedback_transform_3
        elif yfeedbackPosition == 4:
            at point_feedback_transform_4
        elif yfeedbackPosition == 5:
            at point_feedback_transform_5
        elif yfeedbackPosition == 6:
            at point_feedback_transform_6
        elif yfeedbackPosition == 7:
            at point_feedback_transform_7
        elif yfeedbackPosition == 8:
            at point_feedback_transform_8
        elif yfeedbackPosition == 9:
            at point_feedback_transform_9
        text "{size=+30}+[orderyPoints]" style "yellowPointsStyle"
        add "order treasure.png":
            fit "scale-down"
            xysize (70,70)
            
screen sleepFeedback:
    timer 2.0 action Hide("sleepFeedback")
    hbox:
        if gfeedbackPosition == 1:
            at point_feedback_transform_1
        elif gfeedbackPosition == 2:
            at point_feedback_transform_2
        elif gfeedbackPosition == 3:
            at point_feedback_transform_3
        elif gfeedbackPosition == 4:
            at point_feedback_transform_4
        elif gfeedbackPosition == 5:
            at point_feedback_transform_5
        elif gfeedbackPosition == 6:
            at point_feedback_transform_6
        elif gfeedbackPosition == 7:
            at point_feedback_transform_7
        elif gfeedbackPosition == 8:
            at point_feedback_transform_8
        elif gfeedbackPosition == 9:
            at point_feedback_transform_9
        text "{size=+30}+[ordergPoints]" style "greenPointsStyle"
        add "order sleep.png":
            fit "scale-down"
            xysize (70,70)
            
screen lightFeedback:
    timer 2.0 action Hide("lightFeedback")
    hbox:
        if ofeedbackPosition == 1:
            at point_feedback_transform_1
        elif ofeedbackPosition == 2:
            at point_feedback_transform_2
        elif ofeedbackPosition == 3:
            at point_feedback_transform_3
        elif ofeedbackPosition == 4:
            at point_feedback_transform_4
        elif ofeedbackPosition == 5:
            at point_feedback_transform_5
        elif ofeedbackPosition == 6:
            at point_feedback_transform_6
        elif ofeedbackPosition == 7:
            at point_feedback_transform_7
        elif ofeedbackPosition == 8:
            at point_feedback_transform_8
        elif ofeedbackPosition == 9:
            at point_feedback_transform_9
        text "{size=+30}+[orderoPoints]" style "orangePointsStyle"
        add "order light.png":
            fit "scale-down"
            xysize (70,70)
            
screen fishFeedback:
    timer 2.0 action Hide("fishFeedback")
    hbox:
        if vfeedbackPosition == 1:
            at point_feedback_transform_1
        elif vfeedbackPosition == 2:
            at point_feedback_transform_2
        elif vfeedbackPosition == 3:
            at point_feedback_transform_3
        elif vfeedbackPosition == 4:
            at point_feedback_transform_4
        elif vfeedbackPosition == 5:
            at point_feedback_transform_5
        elif vfeedbackPosition == 6:
            at point_feedback_transform_6
        elif vfeedbackPosition == 7:
            at point_feedback_transform_7
        elif vfeedbackPosition == 8:
            at point_feedback_transform_8
        elif vfeedbackPosition == 9:
            at point_feedback_transform_9
        text "{size=+30}+[ordervPoints]" style "violetPointsStyle"
        add "order fish.png":
            fit "scale-down"
            xysize (70,70)
            
screen keysFeedback:
    timer 2.0 action Hide("keysFeedback")
    hbox:
        if pfeedbackPosition == 1:
            at point_feedback_transform_1
        elif pfeedbackPosition == 2:
            at point_feedback_transform_2
        elif pfeedbackPosition == 3:
            at point_feedback_transform_3
        elif pfeedbackPosition == 4:
            at point_feedback_transform_4
        elif pfeedbackPosition == 5:
            at point_feedback_transform_5
        elif pfeedbackPosition == 6:
            at point_feedback_transform_6
        elif pfeedbackPosition == 7:
            at point_feedback_transform_7
        elif pfeedbackPosition == 8:
            at point_feedback_transform_8
        elif pfeedbackPosition == 9:
            at point_feedback_transform_9
        text "{size=+30}+[orderpPoints]" style "pinkPointsStyle"
        add "order keys.png":
            fit "scale-down"
            xysize (70,70)
            
screen boneFeedback:
    timer 2.0 action Hide("boneFeedback")
    hbox:
        if lfeedbackPosition == 1:
            at point_feedback_transform_1
        elif lfeedbackPosition == 2:
            at point_feedback_transform_2
        elif lfeedbackPosition == 3:
            at point_feedback_transform_3
        elif lfeedbackPosition == 4:
            at point_feedback_transform_4
        elif lfeedbackPosition == 5:
            at point_feedback_transform_5
        elif lfeedbackPosition == 6:
            at point_feedback_transform_6
        elif lfeedbackPosition == 7:
            at point_feedback_transform_7
        elif lfeedbackPosition == 8:
            at point_feedback_transform_8
        elif lfeedbackPosition == 9:
            at point_feedback_transform_9
        text "{size=+30}+[orderlPoints]" style "lightPointsStyle"
        add "order bone.png":
            fit "scale-down"
            xysize (70,70)
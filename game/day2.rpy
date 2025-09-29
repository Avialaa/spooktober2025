define visited = set()

label day2_1:
    play music ilo
    scene black
    #(Conditional: reittiin sopiva kommentti skenen alussa)
    # A
    if currentStoryRoute == "agatha":
        "Another morning, another workday. Usually I walk fast to reach the warehouse in time, but today I left early."
    # B
    if currentStoryRoute == "karkhos":
        "My slime body is heavy as I drag myself to the warehouse."
    # C
    if currentStoryRoute == "cee":
        "I slept poorly. My dreams were populated with conveyor belts and boxes bursting at the seams. But the long walk through the dungeon pushes the dreams out of my mind."

    # kaikkien yhteinen täst eteenpäin kaikki
    "It was only yesterday that going to work felt like a holiday. My hopes for a peaceful week remain shattered on the floor."
    "The three of them could have cooled down during the night, but even I have trouble being optimistic about this."
    "Being the middleman in such a big fight is like a second job."
    "And as if dealing with the fight wasn't enough, the Loot never stops pouring in. If we don't keep up, we'll be buried in it."
    "Can't believe I'm about to say this…"
    MC "Boss, please come back sooner!"

    # warehouse BG, vaalimainosversio
    scene bg hallway posters with dissolve
    "Decorations…? Is today a festival?"
    "On closer inspection, these are probably related to the fight. It seems they hope to sway me with slogans and art. Seems kinda cheap." 
    #TODO: arttien näyttäminen
    play sound paper
    show julisteet2 at middle with dissolve:
        zoom 1.5
        yoffset -400
    "Agatha promises streamlined efficiency for the safety of all monsterkind."
    pause 0.5
    play sound paper
    hide julisteet2 with dissolve
    show julisteet3 at middle with dissolve:
        zoom 1.5
        yoffset -400
    "Karkhos… seems to be advocating for workplace wellness?"
    pause 0.5
    play sound paper
    hide julisteet3 with dissolve
    show julisteet1 at middle with dissolve:
        zoom 1.5
        yoffset -400
    "Cee vows revolution on our corrupt and unjust system. Their words, not mine."
    pause 0.5
    hide julisteet1 with dissolve
    "When did they even have the time to hang all this? To make all of this? They're all really dedicated…"
    "In a way, it's amazing how much effort they're putting into this. They all have ideas for how to improve the warehouse."
    "Though it's a pain, I'd feel bad just ignoring them."
    play sound footsteps
    scene bg warehouse posters with dissolve
    pause 1
    stop sound fadeout 1
    "Well, I'll deal with the posters later. The guys promised to not mess things up for the warehouse. On this at least, I trust them."
    "As I get ready to start packing, I notice several pieces of paper on my workstation."
    MC "What is it this time? Let's see."

    # jos nä sais mahtuu kaikki samal kerral textboxiin se ois hyvä. Omil riveil kaikki -TO DO
    # "\"Please pack as many perfect orders as you can. Best, AGATHA.\"
    # \"Hey. Take it easy. The orders are just suggestions. -KARKHOS\"
    # \"Prithee, pack many a fish into every order. Yours truly, CEE.\""
    window hide
    play sound paper
    show notes_from_characters with dissolve
    pause
    MC "...Huh."

    stop music fadeout 5
    return

label day2_2: 
# (After morning minigame, at warehouse)
    scene black
    if thisRoundWinner == "agatha":
        "As we work, Agatha and I gossip about the other departments. We also exchange plans for tomorrow's snacks."
        "She seems happy with my performance."
    # B
    if thisRoundWinner == "karkhos":
        "While working, Karkhos and I exchange complaints. It makes the minutes go a little faster."
        "He seems pleased with my pace."
    # C
    if thisRoundWinner == "cee":
        "While working, I listen to Cee rant about their big plans. It makes the hours go by a bit faster."
        "Cee seems happy with how many fish I'm adding."
    
    scene bg warehouse posters with dissolve
    "Phew!"
    "I'm getting the hang of this new system."
    "After I turn off my conveyor belt, the warehouse falls quiet. Everyone's already left for lunch. Could get used to a silence like this."

    # At breakroom, show all sprites
    play sound footsteps
    play music riita fadein 3
    scene bg breakroom posters with dissolve
    show agatha perus zorder 1 at middle with dissolve
    show cee perus zorder 3 at cright with dissolve
    show karkhos perus mato zorder 2 at cleft with dissolve
    stop sound fadeout 1
    "All three of them are already in the break room. They're all holding posters, hammers and nails. The empty wallspace in the break room must have enticed them."
    show agatha vihainen at hop
    A "Unbelivable. I expected better from you two."
    show karkhos pikkuviha mato
    K "As if you are one to talk."
    show cee vihainen at hop
    C "This is mutiny!"
    pause 0.5
    "Briefly, I entertain the fantasy of abandoning lunch, turning around and returning to work. But all four of Agatha's eyes turn to me."
    show agatha vakava
    A "[MC]! Will you talk sense into these two?"
    show karkhos at hop
    K "Why're you dragging [MC] into this? Don't try to misdirect. What you did isn't cool."
    show cee vihainen
    C "Mister Destroyer, I dare argue your actions have proven just as despicable."
    show karkhos kauhistus mato
    K "What actions?"
    show cee at hop
    C "Précis!"
    show karkhos pikkuviha mato
    show cee perus
    MC "One at a time? I'm sure nobody did it on purpose, whatever it is."
    show cee vihainen
    C "Miss Agatha here has conspired to make wretches of us all."
    show karkhos pikkuviha mato at hop
    K "Cee has done that too!"
    show agatha vakava at hop
    A "Don't forget Karkhos has compromised monsterkind's safety, the warehouse's very purpose."
    show agatha vihainen at hop
    A "We agreed on not going against Boss' orders until [MC] has decided. And here we are."
    show cee vihainen at hop
    C "What fungus has infested thine brain for you to think you're exempt?"
    show agatha
    A "Working hard is EXACTLY what Boss wants. I have not gone against him. Yet you, Cee, have put fish into every order?"
    show cee hullu hymy
    C "I'm simply practicing some much needed service development. As per Boss' orders."
    show agatha at hop
    A "You're practically begging to get fired!"
    show cee vihainen at hop
    C "Isn't there someone here asking for it rather more insistently?"
    show karkhos vihainen mato
    K "...What, me?! No! All I ask for are better conditions."
    show agatha vakava
    show cee perus
    show karkhos perus mato
    stop music fadeout 3
    MC "Wait wait wait… One at a time."
    play music ilo
    # (!!!!! Valinta jossa pitää valita kaikki 3 vaihtoehtoa että pääsee eteenpäin)
    #


label qqquestions:  
    menu:
        set visited
        "Agatha, what did you actually do?":
            $ visited.add("Agatha, what did you actually do?")
            # A neutral
            show agatha vihainen at hop
            show karkhos perus mato
            show cee perus
            A "Don't act like I'm some villain. I've worked harder than anyone here."
            MC "Just, sounded like something serious has happened."
            show agatha vakava
            A "Fine, for the sake of transparency."
            A "I might have ordered a triple of everything."
            show agatha at hop
            A "Wisely! So that we can better show our capabilities."
            A "Would be difficult to work hard without anything to pack. I'm sure you see where I'm coming from."
            MC "But even at normal capacity, the cavern is pretty stuffed. Where did you plan to store all this triple loot?"
            # A smile
            show agatha iloinen suukiinni
            A "..."
            show agatha iloinen at hop
            A "Look around. Vacant floor space everywhere. And we won't be needing the break room once all the Loot arrives."
            "Oh, Agatha."
            jump qqquestions
        "Karkhos, how many boxes today?":
            $ visited.add("Karkhos, how many boxes today?")
            show karkhos pikkuviha mato
            show agatha vakava
            show cee perus
            K "Why's that important? I have done what's within my capabilities."
            MC "Which is…?"
            show karkhos nukkuva mato
            K "Hey, it's not my fault the Loot I got sent today was especially tricky to pack. Couldn't have done it any faster."
            show karkhos pikkuviha mato
            K "I had to do a thorough quality inspection, sort everything, and the conveyor belt was misbehaving so I had to fix it, and…"
            K "I've completed a full and whole- A whopping total of a—"
            # K sad
            show karkhos alakuloinen mato
            K "...a…"
            # K angry
            show karkhos vihainen mato
            K "I have prioritized quality over quantity."
            "I can see why the others are upset."
            jump qqquestions
        "Cee, what's this development stuff?":
            $ visited.add("Cee, what's this development stuff?")
            show cee hullu hymy
            show agatha vakava
            show karkhos perus mato
            C "There festers a livid darkness within these cavernous halls. To develop our machinations faster than it can grow, such is my design."
            MC "Sorry, my lowly slime brain has lost the thread. Could you rephrase that?"
            show cee perus
            C "Very well, my sluggish companion. I put fish into all the orders."
            MC "Yeah, that's… yeah."
            show cee karmiva hymy
            C "...AND drilled down to groundwater, installed a pump, and harnessed the conveyor belt for power."
            "WHAT."
            show agatha vakava at hop
            show karkhos pikkuviha mato at hop
            "Agatha and Karkhos give me knowing looks."
            show cee tosi iloinen at hop
            C "Rejoice: we shall soon have fresh water aplenty."
            MC "That's insane!"
            show cee kauhistus
            C "It is what anyone in my situation ought to have done."
            MC "I don't think ANYONE but you would have done that."
            # C smiles
            show cee tosi iloinen
            C "Oh, you do flatter me."
            jump qqquestions

label after_questions:
    $ visited.clear()
    show karkhos perus mato
    show cee perus
    show agatha vakava
    "Whoa. They've rewritten the rules and don't seem to regret a thing. They promised to not disturb the warehouse's purpose until this dispute is settled, and yet."
    "So much for democracy."
    "Honestly though, I kind of understand. I haven't always gone strictly by Boss' orders either. Following all these orders and agreements is really hard, okay!"
    stop music fadeout 3
    MC "Listen. We all do stupid things sometimes. Accidentally or deliberately. What matters is what we do from now on."
    show agatha vihainen at hop
    A "Yeah, get it together, guys!"
    show karkhos pikkuviha mato
    K "You too."
    play music riita
    show karkhos vihainen mato
    K "This isn't fair. I have done what I can."
    K "If what I've accomplished is not enough, then from now on, I will not pack a single box."
    show cee vihainen
    C "I also refuse to waste time. These superfluous meetings are gobbling up the most productive hours of the day."
    show cee at hop
    C "What I must do cannot wait. Farewell!!!"
    play sound footsteps
    hide cee with easeoutleft
    # C pois, footsteps
    show agatha at hop
    stop sound fadeout 1
    A "ARGH!!!"
    play sound wingflap
    hide agatha with moveouttop
    # A pois, wing flaps
    show karkhos pikkuviha mato
    K "...too pissed to nap…"
    play sound footsteps
    hide karkhos with easeoutright
    # K pois, footsteps
    stop sound fadeout 3
    "Our fragile social harmony is falling apart. Agatha and I are the only ones still properly working."
    "All my life, I've only practiced avoiding fights. Now that I need to stop one, I don't know how."
    "I'm exactly the wrong monster for this second job I didn't even apply for."
    "It's almost time to return to work."
    "…I'll eat later…"
    stop music fadeout 5
    return

default day2_3A_done = False
label day2_3A:
    $ day2_3A_done = True
    scene black with fade
    pause 1
    play music juoru
    scene bg hallway posters with dissolve
    #footsteps
    play sound footsteps
    "My lunch break evaporated once again. I'll just eat the emergency snack bar I keep at my workstation."
    # Cee appears
    show cee karmiva hymy at middle with moveinright
    C "[MC]!"
    show bg hallway posters at hpunch:
        zoom 1.02
        xoffset -20
    #TÄTÄ EI VARMAAN VOI PITÄÄ
    MC "Eeek!"
    show bg hallway posters:
        zoom 1
        xoffset 0
    show cee perus
    C "Fret not. You must come with me."
    MC "But the break's almost over."
    show cee perus at hop
    C "The tidings I bring concern Miss Agatha."
    show cee hullu hymy
    C "I'm certain you would be interested. It shall not take long."
    show cee perus
    #haluun zoomata kuvan nurkkaan täs jos on aikaa tutkii miten
    play sound footsteps
    show bg hallway posters with dissolve:
        zoom 2
        xoffset -1650
        yoffset -400
    stop sound fadeout 2
    "Cee ushers me into a crevice in the corridor. I follow, initially reluctant, except…"
    "What's so important that they waited for me, after storming off like that? I'm a bit curious."
    "Cee speaks in a lower voice than usual. Which, granted, is still pretty loud."
    show cee alakuloinen
    C "Pardon the precautions. I had to make sure that the tiny control freak wasn't following us."
    show cee perus
    C "I've heard some rather concerning rumours about you and Miss Agatha. The hallways are whispering that you have taken a liking to her rigorous ways."
    show cee kauhistus at hop
    C "[MC], you must not fall under her spell!"
    show cee vihainen
    C "I have seen her true colors. Once, she interrupted my work just to tell me I wasn't projecting enough enthusiasm."
    show cee vihainen at hop
    C "Such insolence!"
    # Cee looks angry
    C "Why should we show enthusiasm while performing these repetitive, mundane tasks? Can't she fathom that my passions lie elsewhere entirely?"
    MC "She isn't that bad once you get to know her. She's working hard to protect her fellow monsters."
    show cee alakuloinen
    C "That, my foolish comrade, is what she WANTS you to think."
    show cee hullu hymy
    C "Do not be fooled by her big eyes and paper thin wings. Underneath that disguise you'll find a ferocious predator, poised to bite those standing in her way." 
    MC "Hey, that's going too far."
    show cee perus at hop
    C "Hardly! What shall a mere worker do, when told to triple their efforts?"
    show cee kauhistus
    C "To try is to perish, whilst to not try is to be bitten."
    show cee perus
    C "Were we to work harder, would it not in actuality decrease our output? Eat the marlin's roe, and be bereft of the fish."
    show cee perus
    C "She is thinking short term, when what matters is the long term."
    show cee kauhistus
    C "Unwittingly, she may yet be furthering my goals."
    show cee karmiva hymy at hop
    C "She will wring dry this den of Loot, and whilst we wither, she will flutter away to greener pastures."
    C "Rather than a moth, she is a locust. Nay, a disease!"
    MC "Stop."
    show cee kauhistus at hop
    C "...!"
    MC "I appreciate the sentiment, but I won't let you badmouth Agatha."
    MC "She cares about the warehouse and wants us to succeed."
    show cee vihainen at hop
    C "Bah! I did not think you simple-minded enough to fall for her ruse. Consider me disappointed."
    show cee perus
    C "I have given my augury. Since you wish to remain ignorant, do not cry for help once the predator attacks."
    # Cee leaves
    play sound footsteps
    hide cee with moveoutleft
    stop sound fadeout 3
    scene bg hallway posters with dissolve
    "I'm speechless. It's not okay to speak about coworkers like that."
    "I can't tell if this was just Cee's personal dislike, or an actual worry about our wellbeing. Maybe it was both."
    "Does sound like Agatha should have been nicer to Cee."
    "Once, even I used to think she was an inconsiderate nitpicker. But I understand her better now."
    "All Agatha is trying to do is make the land safer for monsters."
    "Nothing predator-like about that."
    pause 0.5
    stop music fadeout 5
    "...Right?"
    scene black with fade
    return

default day2_3B_done = False
label day2_3B:
    # (agatha tulee puhuu paskaa karkhoksesta)
    $ day2_3B_done = True
    # käytävä, walking
    play sound footsteps
    play music juoru
    scene bg hallway posters with dissolve
    pause 1
    play sound wingflap
    show agatha perus at middle with easeinleft
    A "[MC]!"
    "The break is almost over, yet Agatha has waited for me. Extremely abnormal."
    "I detect no trace of her earlier anger. My curiosity is piqued."
    MC "I thought you went back already."
    show agatha at hop
    A "In a minute. I have something important to tell you. It concerns Karkhos."
    show agatha vakava
    A "Say. How much has Karkhos told you about his reasons for being here?"
    MC "For being here in the warehouse? Not much."
    show agatha at hop
    A "You know how undead are usually tireless, obedient servants, that kind of thing?"
    A "Necromancers usually supply magical energy to the undead they raise, taking away the need for food and rest."
    show agatha perus at hop
    A "Doesn't match a certain Mister Destroyer, does it?"
    MC "...What are you getting at?"
    show agatha iloinen
    A "I think I cracked what's going on with him."
    show agatha perus at hop
    A "A few years back, the whole undead servant thing ruffled some feathers. Do you remember?"
    MC "Not really. News travels slow to the dungeon."
    show agatha vakava
    A "The Monsters' Rights Union started advocating for undeads' rights. They were outraged that our dead were being raised as servants."
    show agatha vakava at hop
    A "The huge protests were the talk of the land."
    A "The necromancers' guild eventually yielded. In response to the protests, they signed an agreement to preserve the corpse's personality as they raised it."
    show agatha at hop
    A "A huge victory, right?"
    show agatha alakuloinen
    A "Turns out an undead with a personality intact might have a thing or two to say about being forced into service."
    A "The necromancers have since discontinued the agreement, returning to the old ways, but the undead raised under the agreement remain."
    MC "You're saying Karkhos was a …test dummy?"
    MC "I had no idea he had gone through something like this. Though he has always been pretty opinionated for an undead."
    show agatha vakava
    A "I don't know the details, but I suspect Karkhos was resurrected to be an employee for the Chain of Loot."
    A "He probably needs to work here, per the necromantic contract, or something bad happens. Here, or somewhere else in the chain."
    MC "Maybe Karkhos will tell us himself when he's ready. This is enough gossip for one day."
    A "Ask him yourself, then."
    show agatha at hop
    A "But you see? Someone forced into working isn't the best judge of what's good for the warehouse. His opinions are tinted by his horrible and inescapable circumstances."
    show agatha vihainen
    A "Let's be real. This is a pretty cushy job. He's the only one who can't muster the willpower to try harder."
    A "It's wrong for the whole system to run to pace with the weakest link."
    show agatha at hop
    A "I don't know what's wrong with him, and I don't care. He's handling it about as poorly as one can."
    show agatha at hop
    A "I won't let him drag us down with him."
    MC "That's for Boss to decide. Karkhos isn't harming any of us."
    show agatha vakava
    A "Isn't he? Karkhos never participates in the holiday gift exchanges, eats the communal foods even though he doesn't need to, doesn't clean up after himself, is always late..."
    show agatha vihainen at hop
    A "And I need to work harder to make up for it."
    show agatha at hop
    A "He's such a bad employee! Some days I wish he would just…"

    menu:
        "Karkhos isn't a bad employee.":
            show agatha pelokas at hop
            "Agatha flinches, but doesn't stop talking."
            show agatha vakava
            A "A good employee doesn't suddenly stop doing what he is asked."
            MC "Is it really so wrong for the workload to match those who tire the fastest?"
        "Makes a brutal sort of sense.":
            show agatha vakava at hop
            A "Life is brutal. It's why monsters need Loot in the first place."

    A "If Karkhos wins this argument about workplace improvements, you know what'll happen?"
    show agatha vakava at hop
    A "Karkhos will present his crazy demands for 500\% more breaks, or whatever he haphazardly decides on, and Boss will laugh us out of his office."
    show agatha pelokas at shake2
    A "Then Boss will hire a lobotomy wizard to make US into thoughtless, wantless servants."
    show agatha pelokas at middle
    MC "Now you're just exaggerating."
    MC "Let's just go back to work? Badmouthing coworkers behind their backs isn't part of the job."
    show agatha vakava at hop
    A "Fine. Suit yourself."
    A "But once Boss returns, I won't let this behavior continue."
    play sound wingflap
    hide agatha with easeoutright
    # agatha läpsyttelee pois
    "If what Agatha told me is true…"
    "How would I feel about doing forced labor?"
    #TODO: conditional skenessä 2.5B jos pelaaja saanu tän skenen
    stop music fadeout 5
    
    return

label day2_3C:
    # bg käytävä
    scene black with fade
    pause 1
    play sound footsteps
    scene bg hallway posters with dissolve
    play music juoru fadein 1
    stop sound fadeout 3

    "My lunch break evaporated once again. I'll just eat the emergency snack bar I keep at my workstation."
    show karkhos pikkuviha mato at middle with dissolve
    K "[MC], I gotta speak to you."
    MC "Huh? You waited for me?"
    K "It's about Cee."
    "What's so important that he waited for me, after storming off like that? I'm a bit curious."
    MC "Has Cee done something?"
    show karkhos nukkuva mato
    K "Besides what they've confessed to? For sure."
    show karkhos perus mato
    K "But that's not what I'm here for."
    K "You know, Cee was already employed here when I started. I was just a newbie, in need of guidance in the ways of the warehouse."
    show karkhos pikkuviha mato
    K "On that first day, you know what Cee said to me?"
    show karkhos vihainen mato
    K "NOTHING."
    K "I tried to be nice, but I got treated like there was nothing going on between my ears. Cee just gave me murderous side-eyes and a mean cold shoulder."
    MC "Cee ignored me in the beginning too. It probably wasn't personal."
    K "Cuz Cee looks down on everyone."
    show karkhos pikkuviha mato
    K "Be honest: do you even know what Cee's advocating for?"
    MC "Uh… Equality and better benefits?"
    K "But what's Cee gonna DO about it?"
    "I only pause to think for a second, but Karkhos reads my silence as an admission."
    show karkhos at hop
    K "See, you don't even know."
    K "Be real. Cee has no plans to let you in on the jig. They're a solo monster."
    MC "That's not true. Cee wants to increase efficiency by building better recreational facilities."
    K "So more boxes packed, but less tired workers? How's that gonna math out?"
    K "If it was possible to do more without doing more, don't you think I'd be campaigning for it? How's messing with the conveyor belt gonna \"revolutionize the system\"? Miracle cures don't exist."
    K "[MC], sorry to break it to you, but Cee's using you."
    show karkhos vihainen mato
    K "All day long Cee calls us fools, idiots, and so on. Clear as day what their opinion of us is."
    K "They've used big words to confuse you. But all that fancy talk is like a small pufferfish inhaling water to look bigger."
    MC "If Cee's just a pufferfish, then you have no reason to be provoked by them."
    show karkhos at hop
    K "I'm not getting provoked! It's annoying, is all."

    menu:
        "I get to side with whoever I want.":
            MC "I choose. That's the spirit of the game."
        "It's not okay to badmouth coworkers.":
            MC "Karkhos, you've gone too far."
            show karkhos pikkuviha mato
            K "Tit for tat. I haven't done anything Cee hasn't."
            MC "Then be the bigger monster and stop."

    show karkhos nukkuva mato at hop
    "Karkhos sighs and shrugs."
    K "Welp. I tried. Guess that's that."
    show karkhos perus mato
    K "So long, [MC], and take it easy with the fish."
    # karkhos menee pois
    play sound footsteps
    hide karkhos with easeoutright
    stop sound fadeout 3
    "Without any further convincing, Karkhos stomps back into the break room. He gave up shockingly fast."
    "Though he had a point, he has also misunderstood Cee's intentions."
    "Cee's the only one looking far into the future. That's admirable."
    "And Karkhos was wrong. I know exactly what Cee's planning."
    stop music fadeout 5
    pause 1
    "...Right?"
    return

label day2_5:
    scene black
    if thisRoundWinner == "agatha":
        "At one point, I almost drop a heavy box, but Agatha catches me. She's surprisingly strong."
    # B
    if thisRoundWinner == "karkhos":
        "Mid-shift, I knock over a large pallet of packed boxes. Karkhos rushes to help me clean up."
    # C
    if thisRoundWinner == "cee":
        "Mid-shift, Cee brings me some water. The kind gesture gives me strength."

    return

label day2_5A:
    
    scene bg breakroom posters night with dissolve
    play music bondaus
    "As I start heading home, I see something shocking out of the corner of my eye."
    show agatha alakuloinen at agathabreakroom
    "Is that… Agatha? Sitting in the break room and not working?"
    "I mean, she shouldn't be, strictly speaking, but usually she can never be pried away until well after everyone else has left."
    "I catch myself looking around for threats. Something must be fundamentally wrong with the world."
    show agatha alakuloinen at hop
    A "UuUugGHhh…"
    "I'm almost too spooked to speak up."
    show agatha alakuloinen at zoomToNormalSize
    MC "Agatha…?"
    show agatha alakuloinen at middle with move
    A "Oh, [MC]. Sorry. Don't worry about me…"
    MC "I thought you'd still be working. It's not- don't tell me someone has died?"
    A "No, nothing like that."
    show agatha alakuloinen at hop
    "She sighs."
    A "I'm just feeling a bit… lonely."
    A "I don't understand why the others don't see the value in doing our best for the Loot Chain."
    MC "Yeah… It was a bit sad to work without Karkhos and Cee today."
    show agatha vakava
    A "I just feel like… They work here, right? So why won't they {i}work{/i}?"
    #work itallics
    show agatha vihainen at hop
    A "If they don't want to do it, they could just- just…"
    show agatha alakuloinen at hop
    "She bites her lip."
    #: conditional jos lukenut 2.3A:n:
    if day2_3A_done == True:
        "I think back to Cee's story of Agatha demanding they show more enthusiasm. Was there more to it than Cee told, or could she really be plotting death by overwork?"
    menu:
        "\"Well, everyone's different.\"":
            show agatha at hop
            A "But we're all supposed to be working together!"
        "\"I get it. I wish they'd do more.\"":
            show agatha vakava at hop
            A "Right??"
    show agatha vakava
    A "I just… When I looked around, I saw Karkhos napping in a box and Cee jamming the conveyor belt with fish!"
    show agatha pelokas at hop
    A "And- and- and what are we going to tell Boss when he comes back?!"
    A "Our output is {i}half{/i} of what it should be!"
    #half itallics
    show agatha pelokas at shake2
    A "[MC], I can't make up for this much slacking off!"
    show agatha pelokas at hop, shake2
    A "I mean, I would if I could, but I can't!"
    show agatha alakuloinen at middle
    "She puts her head in her hands."
    MC "There, there…"
    MC "Look on the bright side. Our output's still good compared to before the new system."
    show agatha alakuloinen at hop
    A "I know. But I- I was…"
    "Nooo! I wanted to improve her mood, but she looks like she might cry!"
    show agatha alakuloinen kyynel
    A "I was really looking forward to the higher productivity."
    "That's actually a tear on her face."
    MC "..."
    MC "I'm not the brightest, but is this really about productivity?"
    A "..."
    show agatha alakuloinen at hop
    A "Yes?"
    A "I know it sounds phoney, but each piece of Loot really matters to someone out there."
    MC "I mean, you're not wrong, but…"
    show agatha alakuloinen
    A "..."
    MC "...?"
    show agatha vakava 
    A "...Fine. Okay. [MC], how much do you know about the Human Wilds?"
    MC "I mean, I've seen pictures?"
    show agatha vakava at hop
    A "Right."
    "Her eyes are distant for a moment, before drilling back into me with their usual uncanny brightness."
    A "I … grew up in the Human Wilds. There was no Loot system back then."
    A "Most of my kind are nectar farmers, and it's dangerous work. When a human stumbles on you in the flower field…"
    show agatha pelokas at shake2
    "She shudders."
    MC "What? What?"
    show agatha vihainen at hop
    A "They {i}swat{/i} at you!"
    #swat itallics
    show agatha pelokas at hop
    A "They're enormous and they scream and flail and they look at you like you're some kind of nasty- nasty… human."
    show agatha alakuloinen
    A "One day when I was just a larva, my father returned home late in the evening, limping back because a human broke his wing."
    A "Since then, he's always had trouble flying long distances. But I'm glad nothing worse happened."
    MC "I'm so sorry. I can't imagine… I never had to worry about my moms and pops that way."
    show agatha vakava at hop
    A "I'm glad you haven't had to fear humans."
    show agatha alakuloinen
    A "You know, Karkhos likes to go on and on about how nice it was to be out in the sunlight, but I like it here."
    show agatha vakava
    A "It's like we're under a protective dome, day in and day out."
    A "When we moved here, I had my first restful sleep since emerging from my cocoon."
    MC "I'm glad you're here now."
    #A smile
    show agatha perus
    A "Yeah. Me too."
    show agatha vakava
    A "After I started working here, I got a letter from my cousin."
    A "She told me that Loot had saved her mate's life."
    show agatha alakuloinen
    A "It means the world to me that we can make life better for everyone I left behind."
    MC "I… hadn't really thought about it, but I'm happy that our work means so much."
    show agatha vakava at hop
    A "It means {i}everything{/i}."
    #everything itallics
    "There's that intense look again."
    show agatha vakava at hop
    A "[MC], if your vote comes out in my favor tomorrow, we can double- no, triple- no, {b}QUADRUPLE{/i} the amount of lives saved each day!"
    #quadruble boldattu
    show agatha iloinen
    A "We'll all work hard together, knowing that each box we pack helps countless monsters."
    show agatha iloinen suukiinni
    "I'm pretty sure we could count them, but… Sure."
    MC "Yeah, sounds good!"
    show agatha tosi iloinen
    A "Yes! I look forward to a bright and productive future with you. As soon as we tally the results tomorrow."
    show agatha perus at hop
    "She jumps up from the table."
    A "Thank you for lending an ear, [MC]. I feel better. I think I'm ready to go back to work."
    "The workday is over, though…?"
    MC "Uh, okay. Happy to help."
    show agatha perus at hop
    A "See you tomorrow!"
    MC "Yeah. See you!"
    play sound wingflap
    hide agatha with moveoutright
    "She flutters back towards the packing area, humming a cheerful tune."
    "I worry a bit about how long she's going to keep working, but at least she cheered up."
    "I also feel energized, looking at her. Maybe I'll go for an evening waddle before returning home."
    scene black with dissolve
    stop music fadeout 5
    pause 2
    return

label day2_5B:

    play music bondaus
    scene bg hallway posters with dissolve
    pause 1
    scene bg hallway posters night with dissolve
    "Second day done. Can't wait to go home and melt in my bathtub shaped hole. Keeping a good posture without any bones takes effort."
    "Still, work was a lot easier when I didn't push myself so hard."
    "I can still hear conveyor belt sounds coming from the warehouse. Some of the guys are still working."
    "As for who isn't, I have a guess."

    # corridor BG
    # karkhos sprite
    play sound footsteps
    scene bg hallway posters night
    show karkhos perus at middle
    "Knew it."
    stop sound fadeout 1
    K "Out the door, right on the dot."
    MC "Old habits die hard."
    show karkhos iloinen at hop
    K "Die is right! You're crawling along like YOU are the token zombie."
    show karkhos perus
    K "But I had a reason for waiting. Tomorrow's the day of truth. Wanted to check in on you."
    K "Thought we could walk to the big intersection together?"
    MC "Oh. Sure."
    show karkhos tosi iloinen
    K "Awesome!"
    show karkhos iloinen
    "He's really spirited. Usually, he leaves work dragging his feet, groaning like a zombie. The regular kind—the kind that gurgle, drool and are real culinarians when it comes to internal organs."

    #(Conditional: jos 2.3B (edellinen skene) saatu)
    if day2_3B_done == True:
        "When he first started working at the warehouse, I did note he's more animated than other animated corpses. To think that all this time, he was working under a necromantic contract."
        "Being forced to work… The rest of us chose this job, but Karkhos didn't get to choose. It's possible he doesn't enjoy a single thing about working here."

    # footsteps, they are both walking
    show karkhos perus
    K "You look to be thinking real hard."
    show karkhos iloinen
    K "Maybe it's cuz you still have questions about my great workplace improvement plan?"
    K "Well, the walk to the big intersection is a long one. If you wanna ask, now's the time. Q and A. Karkhos the Destroyer: an open book."
    "I do have a lot of questions. Whether he likes working here, for one."
    "But all these years, I've never asked my coworkers anything personal. Monsters usually tell it straight if they want to. Unless they're a sphinx."
    "Suddenly, I'm all nerves. Even though I don't have any."

    menu:
        "Talk about the weather":
            MC "The dungeon air today sure is on the moist side."
            show karkhos iloinen at hop
            K "Huh? Sure is. Moisture good for ya?"
            MC "For slimekind, hydration is very important. Mom used to spray me with sugar water during dry seasons."
            show karkhos alakuloinen
            K "For me, moisture's trouble. I gotta be careful my brain doesn't become a residence for some mold."
            K "I've already got a tenant, and Wormy even pays rent. And eats the mold."
            show karkhos alakuloinen mato at hop
            "Wormy wriggles up to nod vehemently."
            "...! This is it, the perfect lead in."
        "Discuss current affairs":
            show karkhos perus
            MC "I heard humans attacked the dire-frog village. Thankfully nobody died. They all had Loot. But their homes got trampled."
            show karkhos pikkuviha at hop
            K "I didn't hear about this! News reaches the dungeon so slow."
            # angry sprite
            show karkhos vihainen
            K "Those villainous humans always take advantage of the vulnerable. They are despicable."
            show karkhos alakuloinen
            K "Well. At least we won't be seeing undead frogfolk just yet."
            "...! This is it, the perfect lead in."
        "Ask how he died":
            "Tact's for wimps!"
    show karkhos perus
    MC "I've always just been a slime. But I've gathered you were a different type of monster before? If it's not too weird to ask, how'd you become undead?"
    show karkhos alakuloinen
    K "Uh. When I said it's a Q and A, I sorta hoped you'd ask about workers' right to more breaks."
    MC "Sorry. Your death is probably a difficult memory."
    show karkhos perus
    K "Nah, man. I used to be an orc. The way I died was stupid."
    K "Didn't have Loot on me, while my clan mates did. The last thing I saw was their retreating feet."
    show karkhos alakuloinen at hop
    K "That should've been it for me, but I woke up in the chain's restoration facility. Guess I looked strong enough to be turned into an undead?"
    show karkhos perus
    K "But no hard feelings to the necromancer who patched me up."
    K "Though I think she took my kidney. And something else over in my mid abdomen. The cavity sometimes gathers liquid."
    # K happy sprite
    show karkhos iloinen
    K "Oh well! I've still got lots of organs to spare. Not like they do much now. They've probably spoiled anyway."
    show karkhos perus
    MC "You were… happy to be turned into an undead?"
    K "Getting a new chance at life doesn't happen to everyone."
    show karkhos iloinen at hop
    K "There was still a lot I wanted to experience, and I was happy to give back."
    show karkhos nukkuva
    K "The Loot saved my clan mates, and the chain gave me a second life. Didn't matter I was destined to work until my body fell apart."
    # sad sprite
    show karkhos alakuloinen
    K "But this job… When I was alive, daily chores were never this taxing."
    K "As days have trickled by, not even the good cause keeps my feet moving."
    K "I've worked all my life, but even after death, the grind goes on." 
    # angry sprite
    show karkhos pikkuviha
    K "If monsters must work, then I demand it be something we don't tire from doing! What's wrong with that?"
    K "To make monsters contort themselves into rigid time slots, it's just unnatural. We should be allowed some flexibility in the hours we work."
    MC "To your credit, no other zombie would have lasted a day in the warehouse."
    "His angry eyebrows lift in minor triumph."
    show karkhos vihainen at hop
    K "Yeah! No zombie can beat me."
    show karkhos pikkuviha
    MC "Maybe you just need a holiday? When's the last time you had time off?"
    show karkhos alakuloinen
    K "When I was alive. Back in the orc village, we had a thing called \"rest day\". No such things here. If only Boss would give us a few days off."
    show karkhos vihainen at shake
    K "I'd go lava surfing, cave diving, ride a wyrm and kiss the moon."
    show karkhos vihainen at hop
    K "Just because I'm dead doesn't mean I can't LIVE A LITTLE."
    "The shout echoes down every branching cavern. Anyone creeping around the dungeon probably turned to run."
    show karkhos perus
    K "That being so, we need to reach a resolution with this fight. Cee and Agatha need to learn that enough's enough."
    K "Tomorrow at lunch, we'll check your dispatch records. The winner will have their way with the warehouse."
    show karkhos pikkuviha
    K "If we all refuse to work these unreasonable hours, Boss will have no choice but to grant our demands."
    K "I'll win by any means necessary, because I'm right."
    MC "Yeah! It's not fair you're being forced into manual labor, even though you're tired."
    show karkhos kauhistus at hop
    K "What? No! [MC], it's not fair to ANY of us!"
    show karkhos pikkuviha
    K "Everyone else has just gone numb and capitulated to the horrible conditions. Like they were, I dunno, a bunch of zombies?"
    show karkhos alakuloinen at hop
    K "...Not you, of course! But everyone else."

    menu:
        "Yeah! They're all zombies!!!":
            show karkhos vihainen at shake
            show bg hallway posters night at shake:
                zoom 1.05
                yoffset 50
            K "YEEEEAHHH!!!!"
            "The roar echoes. The sound is like a warband of orcs rushing toward us. It's exhilarating."
        "That was a bit mean.":
            show karkhos kauhistus at hop
            "Karkhos clears his throat."
            show karkhos alakuloinen
            K "My bad. Got carried away. I'm sure the other two THINK they can handle the workload."

    show karkhos pikkuviha at hop
    show bg hallway posters night:
        zoom 1.0
        yoffset 0
    pause 1
    play sound footsteps
    "The great intersection is busy this time of evening. Dungeon guards are on their patrol. Tinkerers are running to reset traps, and the cleaning crew is marching to mop up dead humans."
    show karkhos perus
    stop sound fadeout 2
    K "Well, my cave's that way. Was nice chatting."
    # karkhos tosi iloinen
    show karkhos tosi iloinen at hop
    K "I have no idea what's going to happen tomorrow. Pretty exciting."
    MC "See you tomorrow."
    K "See ya."
    play sound footsteps
    hide karkhos with moveoutright
    stop sound fadeout 4
    "I wave. Karkhos enters the stream of monsters, and disappears behind a bend in a cavern."
    "Tomorrow, huh. I have a feeling that after tomorrow, nothing will be the same."
    scene black with dissolve
    stop music fadeout 5
    pause 2
    return

label day2_5C: #Cee emotional evening

    play music ilo
    scene bg hallway posters with dissolve
    pause 1
    scene bg hallway posters night with dissolve
    "As I get ready to leave work, I realize I've forgotten something."
    MC "Darn it. I left my lunch box in the break room."
    "I glide through the empty hallways. Everyone else must either be super busy or have already left for the day."
    "I have a hunch which option Agatha and Karkhos have picked, but..."
    "As I open the break room door, I notice I'm not alone."
    play sound footsteps
    scene bg breakroom posters night with dissolve

    show cee alakuloinen at ceebreakroom with dissolve
    #onks tää liian goofyn näkönen
    stop sound fadeout 3
    "Why is Cee sulking at the table?"
    show cee alakuloinen at middle with move:
        zoom 1.0
    # Cee appears
    # Cee alakuloinen
    MC "What's wrong, Cee? I don't think I've ever seen you like this before. You're usually so… Confident. Verbose. Did something happen?"
    show cee alakuloinen at hop  
    C "The ocean is dark and full of terrors..."
    # C karmiva hymy
    show cee karmiva hymy
    C "...but dry land is even more dangerous. They say the seas are treacherous but they're nothing compared to the dry, twisted hell of the land." 
    "Leave it to Cee to ponder something like this all by themselves in the break room."
    "However, it seems like something is bothering them for real. I can't just leave them be."
    show cee perus
    MC "Uh-huh. Correct me if I'm wrong but it seems like you hate working on dry land. Is this what this is about? Feeling like a fish out of water?"
    show cee alakuloinen
    C "'tis not the land itself that bothers me, although I must admit I am not fond of it either. I'm more of a Mariana Trench type of monster, if you catch my drift."
    "Again with the sea puns, I see, Cee."

    MC "So, if dry land isn't the problem, what is?"
    play music metkut
    show cee iloinen at hop
    C "Ah, I'm glad you asked. The targets of my undying wrath are the beasts that INHABIT the dry land and oppress us sea creatures."
    MC "Ah."
    # Cee vihainen
    show cee vihainen at hop
    C "Nobody in this blasted corporation ever listens to me. Those obnoxious landlubbers seem to think my head is filled with brine instead of a brain. Fools, all of them!"
    C "I am a maelstrom amongst ordinary whirlpools. Why can't they see that my abilities and ideas are well beyond inimitable?"
    MC "I'm glad you value yourself, Cee."
    "What on Earth do they eat for breakfast? Self-esteem cereal? Maybe I should ask them where to buy some…"

    show cee at hop
    C "Those impudent land-dwellers look down on our loot. They consider it mere trumpery."
    C "Such insolence! Just because our loot has tiny, insignificant traces of rust or seaweed on it, it's suddenly inferior. Leave it to the surface-dwellers to be that superficial!" 
    "Ouch. Cee does have a point. The others can be kind of mean when it comes to sea monster loot."
    "I wonder why, though. Isn't it kind of exciting to get to open a treasure chest covered in barnacles?"
    "No? It's just me?"
    MC "I understand. It'd bother me as well if my input was never appreciated."
    # Cee iloinen
    show cee iloinen at hop
    C "However, change is coming, and I am its herald."
    C "We cannot overthrow the fur-covered kraken for good, but what we CAN do is make some changes that cannot be reversed so easily. Everyone will benefit!"

    MC "There's something I've been meaning to ask you, Cee. Has Boss done something to you, or is there some other reason for your, uh, resentment?"
    show cee iloinen at hop
    "I can see Cee twitching."
    # Cee perus
    show cee perus
    C "'twas my very first day at this blasted corporation. There I was, innocent like a newly hatched man-eating sea serpent, ready to take on the day and all the responsibilities."
    C "Little did I know that a ferocious beast was lurking in the shadows, claws and fangs ready to tear into fresh meat."
    "Our boss? Really?"
    C "I spotted him near the warehouse. Alone. Unguarded. It was the perfect moment to strike."
    C "I approached him and gave him the biggest smile my face was capable of forming. Then it happened."
    MC "What happened?"
    # Cee vihainen
    show cee vihainen at hop
    C "He called me sweet."
    MC "Sweet? That doesn't sound too bad to me."
    show cee vihainen at shake
    C "I was trying to intimidate him! He was supposed to petrify and then run with his tail between his legs! That way, it would've been clear as day that I am not one to be toyed with."
    MC "Um, Cee, do you realize that smiling is usually considered a nice gesture? Not intimidating?"
    show cee at hop
    C "I wanted to secure my position from day one so that no one would ever dare question my capability. If the kraken was afraid of me, so would be everyone else!"
    stop music fadeout 4
    MC "Why on Earth did you want your colleagues to be afraid of you? Wouldn't that make working together difficult?"
    show cee alakuloinen at hop
    play music bondaus2 fadein 1
    C "My fellow prisoner, do you have any idea how bad it feels when nobody takes you seriously?"
    C "I try my best to act serious and foreboding, and yet those land-dwellers laugh at me and call me cute. It's mortifying."  
    MC "Ah. I'm sorry, Cee. I had no idea you were feeling that way."
    "I feel bad for Cee. They are trying so hard and everyone just keeps brushing them off."
    "Even I remember not taking them seriously when I first met them. Something along the lines of 'wow, that person should probably go touch some dungeon moss'."
    "Ouch. It doesn't feel good to realize you're part of the problem."
    C "Ever since that day, I have not forgiven the fur-covered kraken or his flagrant minions. The wound in my heart runs deep."
    MC "Thanks for helping me understand, Cee."

    # Cee perus
    show cee perus
    C "Tomorrow, after the midday feast…"
    "Lunch, Cee. Lunch."
    C "We shall check the state of the warehouse and decide who our next leader is."
    MC "Feeling nervous?"
    # Cee iloinen
    show cee iloinen at hop
    C "Nay! Do not be ridiculous. Someone of my calibre doesn't even know the meaning of such trivial words."
    MC "Glad to see you being your old self again, Cee."
    "Tomorrow, change is coming. One way or another."
    "Maybe I'M the one feeling nervous."
    scene black with dissolve
    stop music fadeout 5
    pause 2
    return
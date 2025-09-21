

label day1_2: 

# Post-minigame

    scene bg warehouse
    "Done!"
    "The new system will take some getting used to. Until now, I've had to carry everything by hand. The boss always knew which boxes were mine because of the slime stains. I can say goodbye to that."
    # siipien läpsytys
    # Agatha fades in, smiling
    show agatha iloinen suukiinni at middle, hop
    A "…"
    MC "Hi, Agatha."
    A "Good afternoon, MC! Did you sleep well?"
    MC "Same as always?"
    A "Excellent!"
    A "I was hoping to hear your thoughts on the new dispatch ecosystem. After testing the fruits of the wizard's innovation all morning, I'm sure you have some solid constructive feedback."

    menu:
        "“It's more work than before.”":
            A "…While I'm sure the boss appreciates all feedback… Maybe that's a bit… But of course, I don't want to put words in your mouth! But…"
            "She looks conflicted."
        "“It's easy.”":
            A "Great! As expected of the second best employee of the year!"
            "If I recall, she came in first. I don't think she meant ill with that."

    A "I'm sure you're aware, but the boss is relying on us. That he has left us unsupervised signifies great trust."
    A "GREAT trust."
    A "Let's show up properly this week, and be the best versions of ourselves!"
    "She flutters back into the warehouse."
    "Well, the lunch hour's wasting. Not that it's ever an hour, but 30 minutes. Presently, only 28 remain."



    scene bg hallway
    "Huh? That's…"

    # Show K sprite. Silmät kiinni?
    show karkhos nukkuva at middle
    "He's sitting down. I can feel his snoring through the rock floor."
    # K neutral sprite
    show karkhos perus at hop
    K "…mornin', MC."
    MC "Hey Karkhos. Have you been sleeping here the entire shift?"
    show karkhos pikkuviha
    K "...'course not. Stuffed them boxes real hard 'n proper. Just like you."
    show karkhos perus
    K "Man, the new system's really got me down. Learning new stuff sucks, doesn't it?"

    menu:
        "“I wouldn't go that far.”":
            show karkhos iloinen at hop
            K "Hah! You're so easygoing."
        "“It is what it is.”":
            show karkhos iloinen at hop  
            "He perks up."
            K "So you hate it too, huh?"
    show karkhos perus
    K "How come the boss isn't here to test the new system with us? I heard he went to mountaintown. They're having a festival."
    MC "He's getting us a loot deal with the mountain giants. It'll be good for the warehouse."
    show karkhos pikkuviha
    K "Yeah yeah, we'll send better loot to the monsters, the monsters toss the Loot at attacking humans, and get to keep their sorry lives. The cycle of Loot that powers itself. Except in truth it's us powering it."
    K "If I work any harder than this, my stitches are gonna rip. You know how it is for zombies."
    K "Wormy has also had enough."
    #worm sprite
    show karkhos perus mato
    "I nod as a greeting to Wormy, who returns the gesture."
    MC "I'm headed to lunch. You want to come?"
    K "Nah. Cool seeing you."
    K "…"
    "He gives me a weird look. His gaze follows me out."
    "Does he usually speak this much?"

    scene bg breakroom
    "Because of the delays, when I reach the breakroom, I'm not the first one."
    show cee iloinen zorder 3 at hop, middle
    # C happy sprite
    C "Top of the morning, fellow prisoner."
    MC "Good morning to you too, Cee."
    show cee vihainen 
    "Cee grimaces. It makes their face squish like putty. Goo oozes from the folds."
    C "Have you managed to feast your eyeballs on the devastation in the warehouse? The infernal machinery has been wound up, and no longer is there any stopping it."
    MC "Everyone seems to have a strong opinion on the new system."
    show cee perus
    C "Are we, the four heralds of this abysmal lair, content with only trimming the moss, whilst the rock remains unmoved? It's about the rock, MC, the rock."
    MC "Um… The wall moss does need a trim, doesn't it?"
    # Fluttering sound
    # Agatha appears
    show agatha vihainen zorder 1 at cleft with moveinleft
    show cee vihainen at hop
    # C and A angry

    C "I arrived first. Begone."
    show agatha vihainen at hop
    A "This is EVERYONE'S break room, as you know and have known since: forever."
    # Footsteps
    # K neutral sprite
    show karkhos perus zorder 2 at cright with moveinright
    K "Whoa! What's good, slackers."
    "Agatha looks ready to pop a wing muscle."
    show cee vihainen at hop
    C "This is the sacredly ordained lunch break. Was it not you who slacked off? Perhaps your sacred right ought to be revoked."
    A "You can't revoke the policy mandated lunch break!"
    "They're really getting fired up. Maybe all this time, they just pretended to like each other because Boss was here. Doesn't feel like much of a break when the noise level is this high."
    "Well, not gonna ruin my day. As long as they're leaving me out of it."
    # A smile
    show agatha iloinen
    A "What's your stance, MC?"
    # C smile
    show cee iloinen
    C "Yes, do join and settle this petty dispute of Fools."
    # K neutral
    K "..did you just call yourself…"
    MC "No, no. I'm okay with whatever you decide."
    # C neutral
    show cee perus
    C "Nay! You must not remain impartial."
    MC "I really don't mind. I'm not even involved."
    K "Wow. I wouldn't have thought you'd stoop so low."
    MC "...wait, what?"
    C "Oh MC, you must know…"
    A "...that the only thing separating us from lowly humans is…"
    # all angry
    All "...DEMOCRACY!"
    "The declaration echoes in the room."
    # all neutral
    K "It's just the four of us working here. No hierarchies, just equals. Makes only sense we all participate in decision making."
    A "It's not a democratic decision if one of us abstains from voting."
    MC "Can't abstinence also be a type of choice?"
    # all angry
    All "No!"
    "Suddenly they all agree an awful lot."
    # A smiles
    A "I'm afraid that's three against one."
    A "I've always said we need to work harder. This is our chance to earn the Boss' unwavering trust. Our efforts will guarantee monsters across the land safety."
    K "Nah, we should take it easy while the Boss isn't looking. Rested workers are harder workers."
    C "Why stop at puny course changes such as those? I propose we invest this time on R&D, on futureproofing this nigh obsolete lair."
    MC "Did I get this right: you need me to say who I agree with, as a tiebreaker?"
    # all smile
    "Oh dear. When I heard Boss is leaving on a business trip, I expected a more relaxed workweek. This is the opposite of that! Without asking, they roped me into their conflict, and even outvoted my attempt to get out."
    "I let out a heavy sigh. Let them see my inconvenience and suffering. I hope they feel at least a little bad."
    # all sprites smiling
    All "..."
    "I sigh deeply."
    "The quickest way out would be to give an answer."

# tää valinta märää, onks seuraava kohtaus 1.3 A, B vai C. Mut se kohtaus tulee vast kun tää nykyinen on loppunu.
    menu:
        "“Working hard is important” (agree with Agatha)":
            $ agreewithagatha = True
            "Before I speak, I lock eyes with Agatha. Her smile widens."

        "“Enough rest is important” (agree with Karkhos)":
            $ agreewithkarkhos = True
            "Before I speak, I glance at Karkhos. Our eyes meet. Awkward."

        "“Seeking new ways to improve is important” (agree with Cee)":
            $ agreewithcee = True
            "Before I speak, my eyes meet Cee's. He looks surprised."
    MC "I guess since I have to say, I would…"
    A "Stop!"
    MC "Why???"
    C "We cannot be appeased with mere words."
    K "Words are cheap. We need actions."
    A "What we propose goes like this: just test the system, work like you would normally. Though you claim you don't mind who wins, I wonder, is that really true?"
    K "When you work long enough at a place, it's inevitable to start forming opinions."
    A "Exactly. Just test the system, and your true feelings on this issue will surely shine through."
    "What can I even say? The fight has been beaten out of me. I'm starting to question everything I held true. Maybe being noncommittal IS unforgivable. The power of being outvoted sure is frightening."
    MC "Okay. I promise to give it some thought. If that's everything, I still need to eat."
    "They scatter, but keep giving me secretive glances."

    if agreewithagatha:
        jump day1_3A
    # if agreewithkarkhos: 
    #     jump day1_3B
    # if agreewithcee: 
    #     jump day1_3C

label day1_3A:
    scene bg breakroom
    "I feel like if I don't put my metaphorical foot down now, I won't have time to {i}eat{/i} on this \"sacredly\"-whatever lunch break."
    #eat itallics
    #wing flaps sound
    show agatha perus with moveinleft
    "Ah. As usual, it's a race to the ice box between me and Agatha. I don't often win, but then, she has wings."
    "But this time, even though she gets there well ahead of me…"
    #A smile
    show agatha iloinen zorder 2
    A "Go ahead, MC."
    MC "Uh, thanks? That's gentlemonsterly of you."
    A "Why, of course. There's no rush. There are still…"
    "She glances at the clock on the wall."
    A "... 7 minutes and 23 seconds left of lunch. I'm not worried about my spotless attendance record. Even a little. Not at all."
    MC "Your… Sure."
    "I grab my lunchbox, and she rushes to grab her thermos after me."
    A "Now, I saw it in your eyes. No - don't say anything! I wouldn't want to cheat, but I can tell you sympathize with my views." 
    A "As expected of our second best employee!"
    MC "..."
    "She's sitting down on the table next to me."
    "I hoped the rest of my lunch break would be peaceful, but I guess it was too good to be true."
    "She pops open her homemade nectar. Its strong, fruity aroma gives my NutriMold a weird undertaste."
    A "You know, the Loot Chain has given us so much. Stable employment, safe and cozy caves, a purpose."
    A "I think it's the least we can do to give our best in return."
    MC "I do agree about the benefits. Life's hard outside of the dungeon, what with all the humans."
    A "Right? And by doing our part, we get to make life better {i}outside{/i} of the dungeon as well. Good loot saves lives!"
    #outside itallics
    A "And, although this is a bit more crass to bring up…"
    "She lowers her voice conspiratorially."
    A "Who do you think Boss will consider for a promotion when our business inevitably booms?"
    A "With how things are going, it's not going to be {i}him{/i}."
    #him itallics
    #Show Karkhos
    show agatha perus at cleft zorder 2 with moveinleft
    show karkhos perus at cright zorder 1
    "She gives Karkhos the side-eye of the century."
    menu:
        "I don't really want a promotion.":
        #A smile
            A "Well, I would also be happy to help you improve your productivity from a managerial position." 
        "You're probably not wrong.":
        #A frown?
            A "Right? I don't want to foster a hostile atmosphere in the workplace, but…"
            A "Sometimes I feel like he's not motivated to work."
    hide karkhos with moveoutright
    show agatha perus at middle
    "Agatha sips the last of her nectar and stands up."
    MC "Going already? There's still two minutes left."
    A "Can't neglect my record! Which, by the way, you should mind as well!"
    A "Of course, I'm just doing my work as usual. Normally. Until you cast your vote."
    A "Since we all agreed not to meddle until you pick m- a side."
    "Feeling confident, I see."
    A "{i}If{/i} you want to support me for the good of all, I'd ask you to just work as hard as you can!"
    #if itallics
    A "Ship as many orders as you can muster!"
    A "But remember how Boss gets about mistakes."
    #Shake A
    show agatha pelokas at shake #shake pitää lopettaa, muuten jää päälle
    "She shudders."
    show agatha perus at middle
    MC "Yeah. I never want to have another… What did he call it? 'Chit-chat' with him."
    A "Yes. We should strive for that."
    A "Anyway, I'm counting on you to ship as many flawless orders as possible!"
    A "Have a productive afternoon, [MC]!"
    hide agatha with moveoutleft
    #A bounces off
    MC "Thanks, you too?"
    "...Was that a well-wish or a threat?"
    


label day1_4A:

    scene bg warehouse
    show agatha iloinen at middle, hop
    A "Good work, MC! You shipped a lot of good orders today."
    A "I knew I could count on you!"
    MC "Uh, thanks?"
    "How on earth has she kept track of my performance? I never see her eyes leave the…"
    #ehkä zoom in A? yks siipi wink
    show agatha vinkkaus 
    "My gaze is drawn down. One of her wing eyes winks at me."

label day1_6A:

    scene bg breakroom
    
    "Okay, I made it through my first day with the new system pretty respectably."
    "Can't wait to get home and snack on the rest of that rare moss I've been saving."
    "My body starts to salivate just thinking about it."
    show agatha perus at middle
    A "MC!"
    MC "Moss! I mean Agatha!" 
    #A pikku hyppy
    show agatha iloinen at hop
    A "?"
    A "I just wanted to reiterate, great work today! Your numbers were off the charts… The old charts, anyway."
    "She's been really nice to me ever since I was pressured into voting. It's getting pretty transparent, but oh well."
    MC "Thanks. Maybe I'll catch up to you if I keep it up, haha!"
    #A twitch
    show agatha pelokas
    A "Haha! Maybe you will!"
    "..."
    MC "Anyway, I should get…"
    show agatha perus 
    A "If you don't mind, [MC], could I have a moment of your time?"
    "Moss…"
    MC "Sure. What's up?"
    A "I think I can tell you're… a kindred spirit, [MC]. I hope you don't mind me being so bold."
    A "You're such a reliable presence at the warehouse."
    A "I can't always rely on the others to do their part, but I can trust that you will."
    MC "It's nothing? I just do my job?"
    #Make A bigger
    show agatha perus at zoom_in
    A "EXACTLY!"
    show agatha perus at zoom_normal
    #Make A normal size
    A "Don't sell yourself short, [MC]! What you do means a lot. Really."
    "Yeah, she's being REALLY nice. I know she just wants to butter me up… But it's kind of nice to be appreciated."
    A "And not just to me. Every piece of loot we ship could save a monster's life, you know." 
    A "But despite that, Cee has no appreciation for what Boss has created here. And Karkhos…"
    "I can see her going to great trouble, trying to find a diplomatic way to put this."
    MC "...Yeah. Karkhos."
    #A smile
    show agatha iloinen
    A "Well put."
    show agatha perus
    A "You know, the two of them may think they \"just work here\", but their slacking off affects a lot of others: us here, because we have to make up for it, and all of the monsters out there in the world who depend on Loot to protect them!"
    "That's a bit lofty, but I guess her passion for work must come from somewhere. The bit about just working here I feel in my gel."
    MC "I do wish Karkhos and Cee would help a bit more, sometimes."
    A "That's putting it mildly."
    A "But if you support me and we get everyone on board, I know we can take Loot to new heights."
    A "I have so many ideas to improve our productivity for the good of all monsterkind."
    A "More incentives for hard work! Less distractions!"
    "I can't help being enticed by the idea of incentives. It would be nice to get some thanks when I do a good job."
    A "Not to mention expansion!"
    A "There's still room to spread more awareness, and as demand grows, I think the Warehouse will eventually spawn branches."
    A "When that happens, I want to be there to lead the charge."
    #neutraali ilme, shake
    A "Uh. If they'll have me."
    "Boss's shoes are pretty big for her to fill, literally, but she seems really motivated."
    menu:
        "Sure. Maybe you'll get lucky.":
            A "Right. I'll do my best."
        "Go for it! I believe in you.":
            A "Oh!"
            #A smile
            A "Thank you, [MC]."
    A "Our work is important, and I want to give all I can to it."
    A "You know, life is hard for monsters living out in the Human Wilds, and it was even harder before the Loot system."
    #Shake A
    A "When you'd come across a human, it was fight, run or die."
    MC "Yikes!"
    A "Yes. It was even harder for the smaller monsters who don't stand a chance in terms of size."
    A "I mean, some have venom or spikes, but not all."
    A "Without a natural weapon or magic, your only options would be running or dying."
    A "Never leave the dungeon without carrying Loot, MC. Trust me on this."
    A "Humans are scary…"
    menu:
        "Are you speaking from experience?":
            "Her eyes snap to mine and then turn away again."
            A "...Some."
            "She picks at the hair on her arm absentmindedly. I guess she doesn't want to elaborate."
        "You got it.":
            A "Good. Don't forget it."
    A "How about you, [MC]? Have you had any human encounters?"
    MC "No, thank goo. I coalesced in a dungeon like most slimes, so I haven't been out much."
    A "I'm glad. That's how it should be for everyone."
    "When did the mood get this heavy?"
    #Shake A
    A "In any case, I've kept you long enough, [MC]. I should also get going."
    A "Thank you for taking the time for me…"
    "She seems way gloomy. It was surprisingly nice chatting to her, so it'd be a shame to send her off like this."
    "I want to cheer her up, and I know just the thing."
    MC "No proble-moth!"
    "I garnish my pun with a wink."
    "I've been practicing, but my face still looks a bit weird when I focus on closing one eye. Hopefully she doesn't notice."
    #A smile
    A "Pff."
    "Was that a genuine chuckle?"
    A "Nice one, [MC]. Problemoth…"
    "She chuckles again. Yes!!"
    A "Get a good rest, so you can bring your best tomorrow as well!"
    MC "You too, Agatha!"
    "She turns back towards the workroom."
    MC "Wait, you're not going home?"
    A "I just want to pack a few more boxes. I'll be right behind you, promise."
    MC "Okay…"
    #A fade out
    "Oh well, to each their own, and she did seem to cheer up from my pun. Now, I've got a date waiting."
    "Moss, sweet moss…"

return
default agreewithagatha = False
default agreewithkarkhos = False
default agreewithcee = False


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
    A "Good afternoon, [MC]! Did you sleep well?"
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
    K "…mornin', [MC]."
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
    C "Are we, the four heralds of this abysmal lair, content with only trimming the moss, whilst the rock remains unmoved? It's about the rock, [MC], the rock."
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
    A "What's your stance, [MC]?"
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
    C "Oh [MC], you must know…"
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
    if agreewithkarkhos: 
        jump day1_3B
    if agreewithcee: 
        jump day1_3C

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
    A "Go ahead, [MC]."
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
    

#(kohtauksessa 1.2 valitun coworkkerin scene)

label day1_3B:

    # Corridor BG
    scene bg hallway
    "To finish eating in time, I had to forgo pre-digestion. The food chunks floating in my body ludge around unpleasantly."
    # footsteps, K neutral appears
    show karkhos perus at middle with moveinright
    K "Hey, [MC]. Already back to the grind, yeah?"
    MC "Didn't you start your break before me?"
    K "I'll just make up the minutes later. The break's way too short to begin with."
    K "Just because our job's important, shouldn't mean we'll have to work until even our bones are ground to dust."
    K "Though you haven't got any bones, do you?"
    MC "Neither does Agatha. Cee has some, I think."
    K "Bones or not, everyone gets tired. Been wanting to tell this to Boss for ages. But I know he won't listen, not unless all four of us stand behind a single demand. Power in numbers. Like with the uniforms!"
    MC "Oh, true. I still can't imagine what Boss was thinking, putting us in evil cultist getups. It was inconvenient."
    K "Putting it mildly. The robes were a huge pain. Mine always got soggy with gut juice, and the hem made me trip more times than I can remember. The ones we have now are much better. And I don't gotta wear a shirt."
    MC "It was nice that Boss listened, even though he really liked the evil cult look. He's reasonable when it really counts. Must've been because all four of us insisted on it."
    K "This time's no different. We need a unified front. What could be more important than the longevity of the very monsters doing all the heavy lifting?"
    # warehouse BG
    scene bg warehouse with fade
    show karkhos perus at middle
    K "I've been thinking—crazy I know."
    K "As long as we send out enough boxes, doesn't really matter what's inside. Leave some empty space in those boxes, will you? Easier to carry. That would show you agree with me."
    K "We'll show that the warehouse is plenty efficient if we work reasonable hours. Maybe we'll even be MORE efficient with enough breaks. When the Boss returns, he'll have no choice but to agree."
    MC "How much more free time were you thinking?"
    K "Wasn't. Those details will come naturally later. Flexibility, and so on. As I've gotten older, I've understood it's important to not set plans in stone too early."
    "I feel he might have misunderstood some sound advice there. No way am I correcting him, though."
    MC "Uh, speaking of working."
    K "Maybe I've kept you \"too long\"?"
    "He makes air quotes."
    MC "Are you going to continue your …break?"
    K "Nah, I'll get to packing shortly. Promised to work normally until you decide. We even shook on it, me and the two hurrywarts."
    K "None of us want the other two to start doing whatever. It's the one thing we agreed on. Agatha's the most vocal, but Cee's also unbelievably stubborn. So until this thing's settled, I'll go on as usual."
    # K angry
    show karkhos vihainen
    K "They just don't know what's good for them. But they'll run out of fuel soon."

    # (loppujuttu PLACEHOLDER julialle)

label day1_3C:

    scene bg warehouse
    # Cee appears
    # Cee perus
    show cee iloinen at middle with moveinleft
    C "Greetings, my fellow prisoner. Sorry about the brusquerie, but do you have a minute? A fleeting moment to spare?"
    MC "Um, sure thing, Cee. What's up?"
    C "Nay, [MC], nay. What I have to say is FAR more important so please heed my words."
    MC "Alright, Cee, I'm all ears. Um. If I HAD ears, I mean."
    C "Wonderful."
    show cee perus
    C "Do you have any idea what we're up against? Or rather, what kind of a monster is standing in our way, sitting at the top of our corporation?"
    "Cee is talking about Boss, right?"

    menu: 
        "\"Um… dragon?\"":
            MC "Don't dragons like, I don't know, sitting on piles of gold?"
            # Cee iloinen
            show cee iloinen at hop
            C "Ha! Good guess, but nothing quite so fiery."
            "I was already imagining Boss breathing fire. Haha." 

        "\"Boss is a werewolf, isn\'t he?\"":
            MC "I thought you knew that. You've MET Boss, right?"
            C "You poor creature and your lack of imagination. Do you always take everything so literally?"
            "Hey! It's not my fault you're asking strange questions."
        
        "\"I have no idea what you're trying to imply.\"":
            #Cee iloinen
            show cee iloinen at hop
            C "Then allow me to explain, my obtuse comrade."
            "Obtuse?"
            "I have no idea what that word means, but I have a hunch it's nothing flattering…"
    # Cee perus
    show cee perus
    C "Small fish like us have a ghost of a chance against a ferocious KRAKEN unless we join forces. We simply must turn this ghastly ship around while we still can, and steer it towards a brighter future."

    C "Now that the beast is gone, we have the perfect moment to strike. It’s going to be too late when the kraken is back, my fellow prisoner. It's going to be far too late…"
    "Cee stares into the distance and shudders."
    MC "Wait, kraken?"
    C "Aye."
    MC "Boss? Our boss?"
    C "Précis. That imposing fur is hiding dozens, nay, HUNDREDS of grisly tentacles ready to grab any poor fish trying to escape the frigid currents of oppression."
    MC "Wow. Um, okay, you certainly have some strong opinions on this topic."

    C "Why yes, my benighted friend. If not me, who else? The others do not see what I see."
    "Hehe. See and Cee. They are a SEA monster after all."
    C "They lack the ability to comprehend such complicated matters - bless their piteous little brains. I, on the other hand, am well beyond capable of creating a new, better world for us all."
    MC "You sure have been thinking about this a lot, haven't you, Cee?"
    C "Indeed I have. Heed my words, for I shall not be abased any longer."
    C "We must strike NOW, before the tentacles grab us and drag us back into the abyss. We have suffered long enough and 'tis finally time for justice!"
    # Cee looks determined
    MC "Huh. I guess, when you put it like that…"

    # Cee iloinen
    C "I shall wait patiently until our temporary leader is decided, and the others shall too. However, IF either of those fools tries to intervene in the process…"
    # Cee karmiva hymy
    "Yikes!"
    MC "I'm pretty sure they won't. They want it fair and square, just like you and me."
    C "They better."
    MC "Don't worry, Cee. I'm feeling optimistic about this."
    # Cee perus
    C "Very well then. Thank you for this colloquy."

    "They sure use a lot of fancy words. I wish there was a fancy word for someone using too many fancy words."

    C "Now then, I suppose you have some work to do. The infernal machine awaits."
    MC "Oh, right."
    C "Before you start, I have a suggestion. You know what makes any shipment better?"
    MC "Uh…"
    # Cee tosi iloinen
    C "Fish, of course! I suggest you use your slimy little appendages and slip in as many fish as you can."
    "Fish? They want me to pack fish with the orders?"
    C "It would please me immensely."
    MC "Um, I'll think about it, I guess."
    C "Marvelous. I'll be observing you, [MC]."
    "Oh no. I can already feel the performance anxiety hitting." 



label day1_4A:

    scene bg warehouse
    show agatha iloinen at middle, hop
    A "Good work, [MC]! You shipped a lot of good orders today."
    A "I knew I could count on you!"
    MC "Uh, thanks?"
    "How on earth has she kept track of my performance? I never see her eyes leave the…"
    #ehkä zoom in A? yks siipi wink
    show agatha vinkkaus 
    "My gaze is drawn down. One of her wing eyes winks at me."

label day1_4C: #Cee congratulates MC

    scene bg warehouse
    "Thank goo I didn't mess anything up."
    # Cee appears
    # Cee iloinen
    show cee iloinen at middle with moveinleft
    show cee iloinen at hop
    C "Well done, [MC]. I'm happy to inform you that I'm pleased with your performance."
    MC "Glad to hear that, Cee."
    "Now this is a surprise. I haven't seen Cee this peppy before."
    # Cee tosi iloinen 
    show cee tosi iloinen
    C "You are well beyond capable. Perhaps we should host a soiree to celebrate your prowess."
    MC "Now now, Cee, you're exaggerating. I was simply doing my job."
    C "No need to be so modest, my dear sluggish companion. You were MARVELOUS." 

    C "A raging tempest destroying everything in its way. Nay, a ferocious SHARK gnashing its teeth and tearing through innocent flesh!"
    "All I did was slip in some fish, and they're this pleased with me? Wow."
    C "Ahhh, I just might shed a tear if I could."
    # Cee iloinen
    show cee iloinen
    MC "Um, sure. If you say so."
    "I'm pretty sure I haven't done anything extraordinary, but here Cee is, singing my praises."
    C "Small fish like us could use a shark like you. Even the bravest landlubbers go pale at the sight of a shark baring its teeth."
    MC "I'm still pondering my options here, but thanks, Cee. I'll let you know when I've made my decision."
    "I start to take my leave, nodding at Cee before I go."     
    C "Even if you remain vacillating, I shall wait patiently."


label day1_6A:

    scene bg breakroom night
    
    "Okay, I made it through my first day with the new system pretty respectably."
    "Can't wait to get home and snack on the rest of that rare moss I've been saving."
    "My body starts to salivate just thinking about it."
    show agatha perus at middle
    A "[MC]!"
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
    A "Never leave the dungeon without carrying Loot, [MC]. Trust me on this."
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

label day1_6B:

    "Done with the day! I'm so tired! When I stretched earlier, so many air bubbles in me popped that it was mildly alarming."
    "Agatha is still working, but the other two seem to have already gone home. I worked hard, and have earned a good night's rest."

    # Käytävä bg
    scene bg hallway night
    show karkhos perus at middle
    "Hm? Karkhos is idling in the corridor. Why hasn't he gone home yet?"
    K "Hey. Good work out there."
    "I should return the compliment, but in light of today's events…"
    MC "Thanks. You look tired as well."
    K "For sure. Could say I'm …DEAD tired."
    MC "..."
    K "Anyway."
    K "The new system's more thinking and less hauling than I'm used to. Agatha said it's just the learning curve, but I dunno. Sounds like a trick. A real fact is that my brain's overheating."
    # sad sprite
    K "And where will Wormy go if my skull's a sauna?"
    show karkhos perus mato
    "The top of Karkhos' brain writhes. \"Wormy\" pokes out and nods empathically."
    MC "I get it. My body temperature also goes up when I move around."
    MC "One summer, when Agatha was sick and we had to work overtime, it was so hot I turned into a puddle. I had to be scraped off the floor and put into the ice box. Took hours before I could move again."
    K "Cee told me about that! Goes to show how important getting to regulate our own breaks is. My previous job in the chain also had unreasonable demands, but at least I got to take a five whenever I wanted."
    "Uh oh. I think he's told me what his previous job was, but I've forgotten."

    menu: 
        "(pretend you remember)":
            MC "Right, it was the job with the, the thing with the…"
            # happy sprite
            show karkhos iloinen
            K "Loot deliveries, yeah. You remembered."
            "I'm sorry."
        "(admit you don't)":
            MC "I feel you might have told me, but I can't seem to remember what your previous job was."
            # sad sprite
            "Karkhos looks disappointed, but he bravely pushes the disappointment away."
            K "It's cool. We've all got our hands full."
            # normal sprite
            K "I used to do Loot deliveries."

    K "I kinda miss it. Took the Loot to \"the monster that needs it\". Nobody was looking over my shoulder, so when I was tired, it was okay to sit down and take a well-timed power nap."
    K "Day after day was a huge deal of running, so much that I wondered if I would die a second time. But the naps under the trees made up for it."
    # K happy silmät kiinni
    show karkhos tosi iloinen
    K "I woke up to birds singing and the sun shining, the wind in my hair and blades of grass brushing against my bones."
    "He seems to get lost in the good memory."
    MC "Why'd you leave then?"
    show karkhos perus
    K "Didn't. Got the boot. Must've been cuz they hate zombies or something."
    MC "..."
    K "Over here, it's all different. I haven't seen the sun in years."
    MC "That IS a downside of working in a dungeon."
    "Karkhos looks at the wall contemplatively. If he's so tired, how come he doesn't find a less taxing job? But there's no way I'm asking that."
    MC "So… See you tomorrow?"
    show karkhos perus at hop
    K "Oh, I've kept you, haven't I?"
    K "Gotta be honest here. I feel like you get where I'm coming from. The other two are stubborn, and the Boss thinks he's always right. But you're not like that. It's like you adapt to what's around you."
    MC "Thanks, I get that alot."
    K "Just be careful, 'kay? Being too malleable might mean someone can use that. Against you."
    MC "That is actually exactly what all slime babies get taught in slime school."
    K "Really?! Damn. Guess I was insensitive."

    menu:
        "I appreciate the sentiment.":
            K "Sorry, I said something stupid again. There's a reason they never called me Karkhos the Poet."
        "I still haven't made up my mind.":
            K "For sure. Better be certain, so you can stand behind your choice."
    show karkhos iloinen
    K "Was nice having a proper heart to hear with you. Can't believe how little we've chatted up till now."
    K "Let's go for drinks sometime? If we ever get a day off, that is."

    # (???? joku loppu-juttu viel, PLACEHOLDER julialle)

return
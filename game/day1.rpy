default agreewithagatha = False
default agreewithkarkhos = False
default agreewithcee = False

label day1_1:
    play music ilo
    pause 1 
    scene black with dissolve
    pause 1
    #(scene alkaa heti nimen valinnan jälkeen.)
    # Musta ruutu taustalla
    "Another morning, another day at the Loot warehouse."
    "The work's hard, but not as hard as life outside the dungeon."
    "As long as I work here, I get three meals a day. What more could a slime ask for, right?"
    "But this week, Boss is away on a business trip."
    "Though he isn't a bad guy, nothing beats the freedom of no superiors breathing down your neck. Well, proverbial neck."
    "This fluffy feeling of freedom… It's like I'm on a holiday!"


    #kävelyn ääniä
    #Käytävä BG
    play sound footsteps 
    scene bg hallway with dissolve
    play sound distantspeak fadein 1
    "Hm? I can hear my coworkers. Sounds like they've gathered behind that bend in the corridor. If they wanted to have a meeting, how come they haven't told me?"
    # ilman spritejä!!!
    stop sound
    A "I'm only offering a suggestion."
    K "And I suggest you …uh… don't?"
    C "I do relish it when the fools fight."
    play sound distantspeak
    "Doesn't seem like they're about to stop."
    "Rather than get involved, I just want to get started with the day. Means I get home sooner."
    "If I just sneak by, maybe they won't notice…"
    stop sound fadeout 4
    # musta ruutu
    scene black with dissolve
    # warehouse
    scene bg warehouse with dissolve
    "Phew! Whatever they were fighting about, I'm sure they'll sort it out. Let's see here…"
    "Before leaving on the business trip, Boss got a wizard to install a new loot dispatch system. He told us to test it while he's gone."
    "It's unexpectedly complicated… Still, I won't let this dampen my easygoing week! The sooner I start, the more boxes I'll pack before lunch."
    #stop music
    return

label day1_2: 

# Post-minigame

    play music ilo
    scene bg warehouse with dissolve
    "Done!"
    "The new system will take some getting used to."
    "Until now, I've had to carry everything by hand. Boss always knew which boxes were mine because of the slime stains. I can say goodbye to that."
    # siipien läpsytys
    # Agatha fades in, smiling
    play sound wingflap
    show agatha perus at middle, hop with dissolve
    A "…"
    MC "Hi, Agatha."
    A "Good afternoon, [MC]! Did you sleep well?"
    MC "Same as always?"
    show agatha iloinen at hop
    A "Excellent!"
    show agatha perus
    A "I was hoping to hear your thoughts on the new dispatch ecosystem. After testing the fruits of the wizard's innovation all morning, I'm sure you have some solid constructive feedback."

    menu:
        "\"It's more work than before.\"":
            show agatha pelokas at hop
            A "…While I'm sure Boss appreciates all feedback… Maybe that's a bit… But of course, I don't want to put words in your mouth! But…"
            show agatha alakuloinen
            "She looks conflicted."
        "\"It's easy.\"":
            show agatha tosi iloinen
            A "Great! As expected of the second best employee of the year!"
            "If I recall, she came in first. I don't think she meant ill with that."

    show agatha perus
    A "I'm sure you're aware, but Boss is relying on us. That he has left us unsupervised signifies great trust."
    show agatha iloinen at zoom_in:
        yoffset 150
    A "GREAT trust."
    show agatha iloinen at zoomToNormalSize:
        yoffset 0
    A "Let's show up properly this week, and be the best versions of ourselves!"
    hide agatha with moveoutleft
    "She flutters back into the warehouse."
    "Well, the lunch hour's wasting. Not that it's ever an hour, but 30 minutes. Presently, only 28 remain."
    show bg hallway with dissolve
    
    "Huh? That's…"

    # Show K sprite. Silmät kiinni?
    show karkhos nukkuva at middle, shake2 with dissolve
    "He's sitting down. I can feel his snoring through the rock floor."
    # K neutral sprite
    show karkhos perus at hop
    K "…mornin', [MC]."
    MC "Hey Karkhos. Have you been sleeping here the entire shift?"
    show karkhos pikkuviha
    K "...'course not. Stuffed them boxes real hard 'n proper. Just like you."
    show karkhos alakuloinen
    K "Man, the new system's really got me down. Learning new stuff sucks, doesn't it?"

    menu:
        "\"I wouldn't go that far.\"":
            show karkhos iloinen at hop
            K "Hah! You're so easygoing."
        "\"It is what it is.\"":
            show karkhos iloinen at hop  
            "He perks up."
            K "So you hate it too, huh?"
    show karkhos perus
    K "How come Boss isn't here to test the new system with us? He just up and left for Mount Big, right when they're having a festival."
    MC "He's getting us a loot deal with the mountain giants. It'll be good for the warehouse."
    show karkhos pikkuviha
    K "Yeah yeah. Send better Loot to monsters, the monsters toss the Loot at attacking humans, and get to keep their sorry lives."
    K "The cycle of Loot that powers itself. Except, in truth, it's us powering it."
    show karkhos nukkuva
    K "If I work any harder than this, my stitches are gonna rip. You know how it is for zombies."
    show karkhos perus
    K "Wormy has also had enough."
    #worm sprite
    show karkhos pikkuviha mato at hop
    "The top of Karkhos' head writhes. I nod a greeting to Wormy, who returns the gesture."
    show karkhos perus mato
    MC "I'm headed to lunch. You want to come?"
    K "Nah. Cool seeing you."
    K "…"
    "He gives me a weird look. His gaze follows me out."
    "Does he usually speak this much?"

    scene bg breakroom with dissolve
    "Because of the delays, when I reach the break room, I'm not the first one."
    show cee perus zorder 3 at hop, middle
    # C happy sprite
    C "Top of the morning, fellow prisoner."
    MC "Good morning to you too, Cee."
    show cee vihainen
    "Cee grimaces. It makes their face squish like putty. Goo oozes from the folds."
    C "Have you managed to feast your eyeballs on the devastation in the warehouse? The infernal machinery has been wound up, and no longer is there any stopping it."
    MC "Everyone seems to have a strong opinion on the new system."
    show cee perus
    C "Are we, the four heralds of this abysmal lair, content with only trimming the moss, whilst the rock remains unmoved?"
    show cee vihainen
    C "It's about the rock, [MC], the rock."
    show cee perus
    MC "Um… The wall moss does need a trim, doesn't it?"
    stop music
    # Fluttering sound
    play sound wingflap
    # Agatha appears
    show agatha vihainen zorder 1 at cright with moveinright
    show cee vihainen at hop
    # C and A angry
    "As we are speaking, Agatha flies in."
    play music riita
    C "I arrived first. Begone."
    show agatha vihainen at hop
    A "This is EVERYONE'S break room, as you know and have known since: forever."
    # Footsteps
    play sound footsteps
    # K neutral sprite
    show karkhos perus zorder 2 at cleft with moveinleft
    stop sound fadeout 2
    K "Whoa! What's good, slackers."
    "Agatha looks ready to pop a wing muscle."
    show cee vihainen at shake
    C "This is the sacredly ordained lunch break."
    show karkhos pikkuviha
    C "Was it not you, Karkhos, who slacked off? Perhaps your sacred right ought to be revoked."
    show agatha vihainen at shake
    A "You can't revoke the policy mandated lunch break!"
    show karkhos at shake
    "They're really getting fired up."
    "Maybe all this time, they just pretended to like each other because Boss was here."
    "Doesn't feel like much of a break when the noise level is this high."
    "Well, not gonna ruin my day. As long as they're leaving me out of it."
    show agatha iloinen at hop
    A "What's your stance, [MC]?"
    # C smile
    show cee iloinen at hop
    C "Yes, do join and settle this petty dispute of fools."
    # K neutral
    show karkhos kauhistus at hop
    K "…did you just call yourself…"
    show karkhos pikkuviha
    MC "No, no. I'm okay with whatever you decide."
    # C neutral
    show cee kauhistus at hop
    C "Nay! You must not remain impartial."
    MC "I really don't mind. I'm not even involved."
    show karkhos at hop
    K "Wow. I wouldn't have thought you'd stoop so low."
    MC "...wait, what?"
    show cee perus at hop
    C "Oh [MC], you must know…"
    show agatha perus at hop
    A "...that the only thing separating us from lowly humans is…"
    # all angry
    show karkhos pikkuviha at hop
    show cee vihainen at hop
    show agatha vihainen at hop
    stop music
    All "...DEMOCRACY!"
    "The declaration echoes in the room."
    play music ilo
    # all neutral
    show karkhos perus at hop
    show cee perus
    show agatha perus
    K "It's just the four of us packing boxes here at the warehouse."
    K "No hierarchies, just equals. Makes only sense we all participate in decision making."
    show agatha perus at hop
    A "It's not a democratic decision if one of us abstains from voting."
    MC "Can't abstinence also be a type of choice?"
    # all angry
    show karkhos vihainen at hop
    show cee vihainen at hop
    show agatha vihainen at hop
    All "No!"
    "Suddenly they all agree an awful lot."
    # A smiles
    show karkhos perus
    show cee perus
    show agatha tosi iloinen at hop
    A "I'm afraid that's three against one."
    show agatha perus
    A "I've always said we need to work harder. This is our chance to earn Boss' unwavering trust. Our efforts will guarantee monsters across the land safety."
    show karkhos nukkuva at hop
    K "Nah, we should take it easy while Boss isn't looking. Rested workers are harder workers."
    show karkhos perus
    show cee karmiva hymy at hop
    C "Why stop at puny course changes such as those? I propose we invest this time on R&D, on futureproofing this nigh obsolete lair."
    show cee perus
    MC "Did I get this right: you need me to say who I agree with, as a tiebreaker?"
    # all smile
    show agatha iloinen suukiinni at hop
    show cee iloinen at hop
    show karkhos iloinen at hop
    pause 1
    "Oh dear. When I heard Boss was leaving on a business trip, I expected a more relaxed workweek. This is the opposite of that!"
    "Without asking, they roped me into their conflict, and even outvoted my attempt to get out."
    "I let out a heavy sigh. Let them see my inconvenience and suffering. I hope they feel at least a little bad."
    # all sprites smiling
    show agatha iloinen suukiinni at hop
    show cee iloinen at hop
    show karkhos iloinen at hop
    "All" "..."
    "I sigh deeply."
    "The quickest way out would be to give an answer."

# tää valinta märää, onks seuraava kohtaus 1.3 A, B vai C. Mut se kohtaus tulee vast kun tää nykyinen on loppunu.
    menu:
        "\"Working hard is important\" (agree with Agatha)":
            $ agreewithagatha = True
            show agatha tosi iloinen at hop
            "Before I speak, I lock eyes with Agatha. Her smile widens."

        "\"Enough rest is important\" (agree with Karkhos)":
            $ agreewithkarkhos = True
            show karkhos perus at hop
            "Before I speak, I glance at Karkhos. Our eyes meet. Awkward."

        "\"Seeking new ways to improve is important\" (agree with Cee)":
            $ agreewithcee = True
            show cee kauhistus at hop
            "Before I speak, my eyes meet Cee's. They look surprised."
    MC "I guess since I have to say, I would…"
    show agatha vakava at hop
    show karkhos perus
    A "Stop!"
    MC "Why???"
    show cee hullu hymy at hop
    C "We cannot be appeased with mere words."
    show cee perus
    show karkhos pikkuviha at hop
    K "Words are cheap. We need actions."
    show agatha perus
    A "What we propose goes like this: just test the system, work like you would normally."
    A "Though you claim you don't mind who wins, I wonder, is that really true?"
    show karkhos perus
    K "When you work at a place long enough, you can't help forming opinions."
    show agatha perus at hop
    A "Exactly. Just test the system, and your true feelings on this issue will surely shine through."
    "What can I even say? The fight has been beaten out of me."
    "I'm starting to question everything I held true. Maybe being noncommittal IS unforgivable. The power of being outvoted sure is frightening."
    MC "Okay. I promise to give it some thought."
    MC "If that's everything, I still need to eat."
    "They scatter, but keep giving me secretive glances."
    play sound wingflap
    hide agatha with moveoutright
    play sound footsteps
    hide cee with moveoutleft
    hide karkhos with moveoutleft
    pause 1
    stop sound

    if agreewithagatha:
        jump day1_3A
    if agreewithkarkhos: 
        jump day1_3B
    if agreewithcee: 
        jump day1_3C

label day1_3A:
    scene bg breakroom
    "If I don't put my metaphorical foot down now, I definitely won't have time to {i}eat{/i} on this \"sacredly\"-whatever lunch break."
    #eat itallics
    #wing flaps sound
    play sound wingflap
    show agatha perus at middle with moveinleft
    "Ah. As usual, it's a race to the ice box between me and Agatha. I don't often win, but then, she has wings."
    "But this time, even though she gets there well ahead of me…"
    #A smile
    show agatha iloinen zorder 2 at hop
    A "Go ahead, [MC]."
    MC "Uh, thanks? That's gentlemonsterly of you."
    A "Why, of course. There's no rush. There are still…"
    show agatha perus
    "She glances at the clock on the wall."
    A "... 7 minutes and 23 seconds left of lunch. I'm not worried about my spotless attendance record. Even a little. Not at all."
    MC "Your… Sure."
    show agatha perus at hop
    "I grab my lunchbox, and she rushes to grab her thermos after me."
    A "Now, I saw it in your eyes. No - don't say anything! I wouldn't want to cheat, but I can tell you sympathize with my views." 
    show agatha at hop
    A "As expected of our second best employee!"
    MC "..."
    "She's sitting down on the table next to me."
    "I hoped the rest of my lunch break would be peaceful, but I guess it was too good to be true."
    show agatha at hop
    "She pops open her homemade nectar. Its strong, fruity aroma gives my NutriMold a weird undertaste."
    A "You know, the Loot Chain has given us so much. Stable employment, safe and cozy caves, a purpose."
    show agatha iloinen
    A "I think it's the least we can do to give our best in return."
    show agatha perus
    MC "I do agree about the benefits. Life's hard outside of the dungeon, what with all the humans."
    show agatha tosi iloinen at hop
    A "Right? And by doing our part, we get to make life better {i}outside{/i} of the dungeon as well. Good loot saves lives!"
    #outside itallics
    show agatha vakava
    A "And, although this is a bit more crass to bring up…"
    "She lowers her voice conspiratorially."
    A "Who do you think Boss will consider for a promotion when our business inevitably booms?"
    show agatha vihainen
    A "With how things are going, it's not going to be {i}him{/i}."
    #him itallics
    #Show Karkhos
    show agatha vihainen at cright zorder 2 with moveinleft
    show karkhos perus at cleft zorder 1 with dissolve
    "She gives Karkhos the side-eye of the century."
    hide karkhos with moveoutleft
    show agatha vihainen at middle with move
    menu:
        "\"I don't really want a promotion.\"":
            show agatha iloinen
        #A smile
            A "Well, I would also be happy to help you improve your productivity from a managerial position." 
        "\"You're probably not wrong.\"":
            show agatha alakuloinen
        #A frown?
            A "Right? I don't want to foster a hostile atmosphere in the workplace, but…"
            show agatha vakava
            A "Sometimes I feel like he's not motivated to work."
    #hide karkhos with moveoutright
    #show agatha perus at middle
    pause 0.5
    show agatha perus at hop
    "Agatha sips the last of her nectar and stands up."
    MC "Going already? There's still two minutes left."
    A "Can't neglect my record! Which, by the way, you should mind as well!"
    show agatha perus at hop
    A "Of course, I'm just doing my work as usual. Normally. Until you cast your vote."
    A "Since we all agreed not to meddle until you pick m- a side."
    "Feeling confident, I see."
    show agatha tosi iloinen
    A "{i}If{/i} you want to support me for the good of all, I'd ask you to just work as hard as you can!"
    #if itallics
    show agatha perus
    A "Ship as many orders as you can muster, and remember that everyone appreciates a freebie. You can slip in a few extras when there's room in the box!"
    show agatha vinkkaus at hop
    A "My recommendation: I think you simply cannot have too many lanterns."
    pause 0.5
    show agatha pelokas
    A "But remember how Boss gets about mistakes."
    #Shake A
    show agatha pelokas at shake2 #shake pitää lopettaa, muuten jää päälle
    "She shudders."
    show agatha pelokas at middle
    MC "Yeah. I never want to have another… What did he call it? 'Chit-chat' with him."
    show agatha vakava
    A "Yes. We should strive for that."
    show agatha perus
    A "Anyway, I'm counting on you to ship as many flawless orders as possible!"
    show agatha iloinen
    A "Have a productive afternoon, [MC]!"
    play sound wingflap
    hide agatha with moveoutleft
    #A bounces off
    MC "Thanks, you too?"
    "...Was that a well-wish or a threat?"
    #stop music
    return
    

#(kohtauksessa 1.2 valitun coworkkerin scene)

label day1_3B:

    # Corridor BG
    scene bg hallway with dissolve
    "To finish eating in time, I had to forgo pre-digestion. The food chunks floating in my body ludge around unpleasantly."
    # footsteps, K neutral appears
    play sound footsteps
    show karkhos perus at middle with moveinright
    stop sound fadeout 3
    K "Hey, [MC]. Already back to the grind, yeah?"
    MC "Didn't you start your break before me?"
    show karkhos pikkuviha
    K "I'll just make up the minutes later. The break's way too short to begin with."
    show karkhos pikkuviha at hop
    K "Just because our job's important, shouldn't mean we'll have to work until even our bones are ground to dust."
    show karkhos kauhistus
    K "Though you haven't got any bones, do you?"
    show karkhos perus
    MC "Neither does Agatha. Cee has some, I think."
    show karkhos nukkuva
    K "Bones or not, everyone gets tired."
    show karkhos perus
    K "Been wanting to tell this to Boss for ages. But I know he won't listen, not unless all four of us stand behind a single demand. Power in numbers."
    show karkhos iloinen at hop
    K "Like with the uniforms!"
    MC "Oh, true. I still can't imagine what Boss was thinking, putting us in evil cultist getups. It was inconvenient."
    show karkhos pikkuviha
    K "Putting it mildly. The robes were a huge pain."
    K "Mine always got soggy with gut juice, and the hem made me trip more times than I can remember."
    show karkhos iloinen
    K "The ones we have now are much better. And I don't gotta wear a shirt."
    MC "It was nice that Boss listened, even though he really liked the evil cult look. He's reasonable when it really counts."
    MC "Must've been because all four of us insisted on it."
    show karkhos nukkuva
    K "This time's no different. We need a unified front."
    show karkhos pikkuviha
    K "What could be more important than the longevity of the very monsters doing all the heavy lifting?"
    # warehouse BG
    play sound footsteps
    show bg warehouse with dissolve
    pause 1
    show karkhos perus at hop
    stop sound fadeout 2
    K "I've been thinking—crazy, I know."

    # MINIPELI OHJEET
    show karkhos pikkuviha
    K "Agatha's always on my case about mistakes, but mistakes are as natural as bowel movements."
    K "We can't exactly go on full strike, but I say we set some boundaries."
    show karkhos nukkuva
    K "Pressure to be perfect gets in our head. Let's embrace it."
    show karkhos vihainen
    K "Let's show them what rushing can cause. Lots and lots of mistakes."
    show karkhos kauhistus at hop
    K "Although… The new workstation's still missing many quality of life improvements."
    show karkhos perus
    K "I wanna earn the ones that make life easier. The green ones."
    show karkhos nukkuva at hop
    K "Guess I need to prioritize shipping out the nap items."
    MC "A good pillow is important."
    show karkhos tosi iloinen
    K "A basic necessity, for sure."

    #Allin lisäys
    # K "Or if you really want to do more, at least get some of orders wrong. To show that pressure causes us to make more mistakes, you know?"
    # K "You might want to get some orders right to earn some workstation upgrades... Just don't overdo it, okay? Mess up orders every now and then."

    show karkhos iloinen
    K "We'll show that the warehouse is plenty efficient if we work within reasonable expectations."
    show karkhos tosi iloinen at hop
    K "Maybe we'll be MORE efficient with less pressure."
    show karkhos perus
    K "When Boss returns, he'll have no choice but to agree."
    MC "What were you thinking of pitching Boss?"
    show karkhos pikkuviha
    K "Wasn't. Those details will come naturally later. Flexibility, and so on."
    K "As I've gotten older, I've understood it's important to not set plans in stone too early."
    "I feel he might have misunderstood some sound advice there. No way am I correcting him, though."
    MC "Uh, speaking of working."
    show karkhos kauhistus
    K "Oh."
    show karkhos pikkuviha
    K "Maybe I've kept you \"too long\"?"
    "He makes air quotes."
    MC "Are you going to continue your …break?"
    show karkhos perus at hop
    K "Nah, I'll get to packing shortly. Promised to work normally until you decide."
    K "We even shook on it, me and the two hurrywarts."
    show karkhos nukkuva
    K "None of us want the other two to go rogue. It's the one thing we agreed on."
    show karkhos perus
    K "Agatha's the most vocal, but Cee's also unbelievably stubborn. So until this thing's settled, I'll go on as usual."
    # K angry
    show karkhos pikkuviha at hop
    K "They just don't know what's good for them. But they'll run out of fuel soon."
    play sound footsteps
    hide karkhos with dissolve
    stop sound fadeout 2
    "On that note, we get back to packing."
    "As I get ready to boot up the new system, the food chunks churn in my slime."
    "If the breaks were a bit longer, I certainly wouldn't complain…"
    # MINIPELI OHJE

    #Allin muutos
    #"…Only three boxes per shift, huh?"
    # "Slack off, and don't be afraid to make some mistakes, huh?"
    "Embrace the mistakes, huh?"
    #stop music

    return

label day1_3C:

    #TÄHÄN VOIS LAITTAA PAREMMAN TRANSITION JOTENKI
    window hide
    show black with dissolve
    pause 1
    "After lunch, it's back to work again."
    stop music fadeout 3
    scene bg warehouse with dissolve
    pause 0.5
    # Cee appears
    # Cee perus
    play sound footsteps
    play music metkut
    show cee iloinen at middle with moveinright
    stop sound fadeout 3
    C "Greetings, my fellow prisoner. Sorry about the brusquerie, but do you have a minute? A fleeting moment to spare?"
    MC "Sure thing, Cee. I'm all ears. Um. If I HAD ears, I mean."
    show cee tosi iloinen
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
            show cee at hop
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
    C "Small fish like us have a ghost of a chance against a ferocious KRAKEN unless we join forces."
    C "We simply must turn this ghastly ship around while we still can, and steer it towards a brighter future."
    show cee hullu hymy
    C "Now that the beast is gone, we have the perfect moment to strike." 
    show cee alakuloinen
    C "It's going to be too late when the kraken is back, my fellow prisoner. It's going to be far too late…"
    show cee alakuloinen at hop
    "Cee stares into the distance and shudders."
    MC "Wait, kraken?"
    show cee perus
    C "Aye."
    MC "Boss? Our boss?"
    show cee vihainen
    C "Précis. That imposing fur is hiding dozens, nay, HUNDREDS of grisly tentacles ready to grab any poor fish trying to escape the frigid currents of oppression."
    MC "Wow. Um, okay, you certainly have some strong opinions on this topic."
    show cee iloinen
    C "Why yes, my benighted friend. If not me, who else? The others do not see what I see."
    "Hehe. See and Cee. They are a SEA monster after all."
    show cee vihainen
    C "They lack the ability to comprehend such complicated matters - bless their piteous little brains."
    show cee iloinen
    C "I, on the other hand, am well beyond capable of creating a new, better world for us all."
    MC "You sure have been thinking about this a lot, haven't you, Cee?"
    show cee perus
    C "Indeed I have. Heed my words, for I shall not be abased any longer."
    show cee hullu hymy
    C "We must strike NOW, before the tentacles grab us and drag us back into the abyss. We have suffered long enough and 'tis finally time for justice!"
    # Cee looks determined
    MC "Huh. I guess, when you put it like that…"

    # Cee iloinen
    show cee iloinen
    C "I shall wait patiently until our temporary leader is decided, and the others shall too."
    show cee perus
    C "However, IF either of those fools tries to intervene in the process…"
    stop music
    show cee karmiva hymy at hop:
        zoom 1.2
        yoffset 100
    show bg warehouse at hpunch:
        zoom 1.02
        xoffset -20
    pause 1.0
    # Cee karmiva hymy
    play music metkut
    "Yikes!"
    pause 0.5
    show bg warehouse:
        zoom 1
        xoffset 0
    show cee at middle:
        zoom 1
        yoffset 0
    MC "I'm pretty sure they won't. They want it fair and square, just like you and me."
    show cee iloinen
    C "They better."
    MC "Don't worry, Cee. I'm feeling optimistic about this."
    # Cee perus
    show cee perus
    C "Very well then. Thank you for this colloquy."

    "They sure use a lot of fancy words. I wish there was a fancy word for someone using too many fancy words."
    show cee at hop
    C "Now then, I suppose you have some work to do. The infernal machine awaits."
    MC "Oh, right."
    C "Before you start, I have a suggestion. You know what makes any shipment better?"
    MC "Uh…"
    # Cee tosi iloinen
    show cee tosi iloinen
    C "Fish, of course! I suggest you use your slimy little appendages and slip in as many fish as you can."
    "Fish? They want me to pack fish with the orders?"
    C "It would please me immensely."
    MC "Um, I'll think about it, I guess."
    show cee iloinen
    C "Marvelous. I'll be observing you, [MC]."
    C "Apropos; the new system doesn't penalize you for slipping in extra items with correct orders."
    play sound footsteps
    hide cee with moveoutleft
    stop sound fadeout 4
    "Oh no. I can already feel the performance anxiety hitting."
    #stop music
    return



label day1_6A:

    play music ilo
    scene bg warehouse with dissolve
    pause 1
    scene bg warehouse night with dissolve
    
    "Okay, I made it through my first day with the new system pretty respectably."
    "Can't wait to get home and snack on the rest of that rare moss I've been saving."
    "My body starts to salivate just thinking about it."
    play sound wingflap
    show agatha perus at middle with easeinleft
    A "[MC]!"
    MC "Moss! I mean Agatha!" 
    #A pikku hyppy
    show agatha iloinen at hop
    A "?"
    A "Good work! You shipped a lot of good orders today."
    show agatha iloinen suukiinni
    MC "Uh, thanks?"
    "How on earth has she kept track of my performance?"
    "I never see her eyes leave the…"
    #ehkä zoom in A? yks siipi wink
    show agatha vinkkaus at hop
    "My gaze is drawn to the side. One of her wing eyes winks at me."
    play sound wingflap
    play sound footsteps
    show bg hallway night with dissolve
    pause 1
    stop sound fadeout 3
    show agatha perus at hop
    A "Indeed, your numbers were off the charts… The old charts, anyway."
    "She's been really nice to me ever since I was pressured into voting. It's getting pretty transparent, but oh well."
    MC "Thanks. Maybe I'll catch up to you if I keep it up, haha!"
    #A twitch
    show agatha perus at shake2
    A "Haha! Maybe you will!"
    "..."
    MC "Anyway, I should get…"
    show agatha vakava at hop 
    A "If you don't mind, [MC], could I have a moment more of your time?"
    "Moss…"
    MC "Sure. What's up?"
    show agatha perus
    A "I think I can tell you're… a kindred spirit, [MC]. I hope you don't mind me being so bold."
    A "You're such a reliable presence at the warehouse."
    A "I can't always rely on the others to do their part, but I can trust that you will."
    MC "It's nothing? I just do my job?"
    #Make A bigger
    stop music fadeout 3
    show agatha iloinen at zoom_in:
        yoffset 150
    A "EXACTLY!"
    pause 1
    show agatha perus at zoomToNormalSize:
        yoffset 0
    #Make A normal size
    play music bondaus2
    A "Don't sell yourself short, [MC]! What you do means a lot. Really."
    "Yeah, she's being REALLY nice. I know she just wants to butter me up… But it's kind of nice to be appreciated."
    show agatha vakava
    A "And not just to me. Every piece of loot we ship could save a monster's life, you know." 
    show agatha vihainen
    A "But despite that, Cee has no appreciation for what Boss has created here. And Karkhos…"
    show agatha at shake2
    "I can see her going to great trouble, trying to find a diplomatic way to put this."
    show agatha at middle
    MC "...Yeah. Karkhos."
    #A smile
    show agatha iloinen at hop
    A "Well put."
    show agatha vakava
    A "The two of them may think they \"just work here\", but their slacking off affects a lot of others."
    A "Us here, because we have to make up for it, and all of the monsters out there in the world who depend on Loot to protect them!"
    "That's a bit lofty, but I guess her passion for work must come from somewhere. The bit about just working here I feel in my gel."
    MC "I do wish Karkhos and Cee would help a bit more, sometimes."
    show agatha vihainen
    A "That's putting it mildly."
    show agatha perus at hop
    A "But if you support me and we get everyone on board, I know we can take Loot to new heights."
    show agatha iloinen
    A "I have so many ideas to improve our productivity for the good of all monsterkind."
    show agatha at hop
    A "More incentives for hard work! Less distractions!"
    "I can't help being enticed by the idea of incentives. It would be nice to get some thanks when I do a good job."
    show agatha at hop
    A "Not to mention expansion!"
    A "There's still room to spread more awareness, and as demand grows, I think the Warehouse will eventually spawn branches."
    A "When that happens, I want to be there to lead the charge."
    #neutraali ilme, shake
    show agatha alakuloinen at hop
    A "Uh. If they'll have me."
    "Boss's shoes are pretty big for her to fill, literally, but she seems really motivated."
    menu:
        "\"Sure. Maybe you'll get lucky.\"":
            show agatha vakava at hop
            A "Right. I'll do my best."
        "\"Go for it! I believe in you.\"":
            show agatha perus
            A "Oh!"
            show agatha tosi iloinen at hop
            #A smile
            A "Thank you, [MC]."
    A "Our work is important, and I want to give all I can to it."
    show agatha vakava
    A "You know, life is hard for monsters living out in the Human Wilds, and it was even harder before the Loot system."
    #Shake A
    show agatha at shake2
    A "When you'd come across a human, it was fight, run or die."
    show agatha at middle
    MC "Yikes!"
    A "Yes. It was even harder for the smaller monsters who don't stand a chance in terms of size."
    show agatha alakuloinen at hop
    A "I mean, some have venom or spikes, but not all."
    A "Without a natural weapon or magic, your only options would be running or dying."
    show agatha vakava
    A "Never leave the dungeon without carrying Loot, [MC]. Trust me on this."
    show agatha pelokas at hop
    A "Humans are scary…"
    menu:
        "\"Are you speaking from experience?\"":
            show agatha vakava
            "Her eyes snap to mine and then turn away again."
            show agatha alakuloinen
            A "...Some."
            "She picks at the hair on her arm absentmindedly. I guess she doesn't want to elaborate."
        "\"You got it.\"":
            show agatha vakava
            A "Good. Don't forget it."
    show agatha vakava at hop
    A "How about you, [MC]? Have you had any human encounters?"
    MC "No, thank goo. I coalesced in a dungeon like most slimes, so I haven't been out much."
    A "I'm glad. That's how it should be for everyone."
    pause 1
    "When did the mood get this heavy?"
    pause 1
    #Shake A
    show agatha alakuloinen at hop
    A "In any case, I've kept you long enough, [MC]. I should also get going."
    A "Thank you for taking the time for me…"
    "She seems way gloomy. It was surprisingly nice chatting to her, so it'd be a shame to send her off like this."
    "I want to cheer her up, and I know just the thing."
    play music ilo
    show bg hallway night at hpunch:
        zoom 1.02
        xoffset -20
    show agatha vakava
    MC "{size=+10}{b}No proble-moth!{/b}{/size}"
    show bg hallway night:
        zoom 1.0
        xoffset 0
    "I garnish my pun with a wink."
    "I've been practicing, but my face still looks a bit weird when I focus on closing one eye. Hopefully she doesn't notice."
    pause 1
    #A smile
    show agatha iloinen suukiinni at hop
    A "Pff."
    "Was that a genuine chuckle?"
    show agatha iloinen
    A "Nice one, [MC]. Problemoth…"
    show agatha iloinen suukiinni at hop
    play sound agathachuckle volume 2
    "She chuckles again. Yes!!"
    show agatha vinkkaus
    A "Get a good rest, so you can bring your best tomorrow as well!"
    MC "You too, Agatha!"
    show agatha perus at agathabreakroom with move
    "She turns back towards the workroom."
    MC "Wait, you're not going home?"
    show agatha at hop
    A "I just want to pack a few more boxes. I'll be right behind you, promise."
    MC "Okay…"
    #A fade out, wingflap
    play sound wingflap
    hide agatha with easeoutleft
    "Oh well. To each their own, and she did seem to cheer up from my pun. Now, I've got a date waiting."
    "Moss, sweet moss…"
    scene black with dissolve
    stop music fadeout 5
    pause 2
    return

label day1_6B:
    scene black
    "As we work, Karkhos and I commiserate over a particularly large order of swords."
    
    play music ilo
    scene bg warehouse with dissolve
    pause 1
    scene bg warehouse night with dissolve
    "Done with the day! I'm so tired!"
    "When I stretched earlier, so many air bubbles popped that it was moderately alarming."
    "Agatha is still working, but the other two seem to have left."
    "I worked hard, and have earned a good night's rest."

    # Käytävä bg
    scene bg hallway night with dissolve
    show karkhos perus at middle with dissolve
    "Hm? Karkhos is idling in the corridor. Why hasn't he gone home yet?"
    show karkhos at hop
    K "Hey. Good work out there."
    "I should return the compliment, but in light of today's events…"
    MC "Thanks. You look tired as well."
    show karkhos iloinen
    K "For sure. Could say I'm …DEAD tired."
    stop music fadeout 5
    MC "..."
    show karkhos perus at hop
    play music bondaus
    K "Anyway."
    show karkhos nukkuva
    K "The new system's more thinking and less hauling than I'm used to."
    show karkhos perus
    K "Agatha said it's just the learning curve, but I dunno. Sounds like a trick."
    show karkhos pikkuviha
    K "A real fact is that my brain's overheating."
    show karkhos alakuloinen
    # sad sprite
    K "And where will Wormy go if my skull's a sauna?"
    show karkhos alakuloinen mato at hop
    "The top of Karkhos' brain writhes. Wormy pokes out and nods empathically."
    MC "I get it. My body temperature also goes up when I move around."
    show karkhos perus mato
    MC "One summer, when Agatha was sick and we had to work overtime, it was so hot I turned into a puddle."
    show karkhos kauhistus mato
    MC "I had to be scraped off the floor and put into the ice box. Took hours before I could move again."
    show karkhos pikkuviha mato
    K "Cee told me about that! Goes to show how important getting to regulate our own breaks is."
    K "My previous job in the chain also had unreasonable demands, but at least I got to take a five whenever I wanted."
    "Uh oh. I think he's told me what his previous job was, but I've forgotten."

    menu: 
        "(pretend you remember)":
            MC "Right, it was the job with the, the thing with the…"
            # happy sprite
            show karkhos tosi iloinen mato at hop
            K "Loot deliveries, yeah. You remembered."
            "I'm sorry."
        "(admit you don't)":
            MC "I feel you might have told me, but I can't seem to remember what your previous job was."
            # sad sprite
            show karkhos alakuloinen mato
            "Oh no. He's disappointed, but trying to hide it."
            K "It's cool. We've all got our hands full."
            show karkhos perus mato
            # normal sprite
            K "I used to do Loot deliveries."
    show karkhos perus mato
    K "I kinda miss it. Took the Loot to the monster that needs it."
    K "Nobody was looking over my shoulder. So when I was tired, it was okay to sit down and take a well-timed power nap."
    show karkhos nukkuva mato at hop
    K "Day after day was a huge deal of running, so much that I wondered if I would die a second time."
    show karkhos perus mato
    K "But the naps under the trees made up for it."
    # K happy silmät kiinni
    show karkhos tosi iloinen mato
    K "I woke up to birds singing and the sun shining, the wind in my hair and blades of grass brushing against my bones."
    "He seems to get lost in the good memory."
    MC "Why'd you leave then?"
    show karkhos perus mato
    K "Didn't. Got the boot."
    K "Must've been cuz they hate zombies or something."
    MC "..."
    show karkhos alakuloinen mato
    K "Over here, it's all different. I haven't seen the sun in months."
    MC "That IS a downside of working in a dungeon."
    "If he's so tired, how come he doesn't find a less taxing job? But there's no way I'm asking that."
    MC "So… See you tomorrow?"
    show karkhos perus mato at hop
    K "Sorry. I ended up yammering again."
    K "Gotta be honest here. I feel like you get where I'm coming from."
    show karkhos pikkuviha mato
    K "The other two are stubborn, and Boss thinks he's always right. But you're not like that."
    show karkhos perus mato
    K "It's like you adapt to what's around you."
    MC "Thanks, I get that alot."
    show karkhos pikkuviha mato at hop
    K "Just be careful, 'kay? Being too malleable might mean someone can use that. Against you."
    MC "That is actually exactly what all slime babies get taught in slime school."
    show karkhos kauhistus mato at hop
    K "Really?!"
    show karkhos alakuloinen mato
    K "Damn. Guess that was insensitive of me."
    menu:
        "I appreciate the sentiment.":
            show karkhos alakuloinen mato
            K "Sorry, I said something stupid again."
            K "There's a reason they never called me Karkhos the Poet."
            pause 1
        "I still haven't made up my mind.":
            show karkhos perus mato
            K "For sure. Better be certain, so you can stand behind your choice."
    show karkhos iloinen mato
    K "Was nice having a proper heart to hear with you. Can't believe how little we've chatted up till now."
    K "Let's go for drinks sometime? If we ever get a day off, that is."
    MC "Sure!"
    play sound footsteps
    hide karkhos with easeoutright
    stop sound fadeout 4
    "Hmm. Agatha and Cee seem to think he's a lazy, selfish oaf, but the more I talk to him…"
    "He truly just cares about our wellbeing."
    "Though chatting was nice, now I'm tired enough to pass out."
    "I wonder… With more rest, what would I be capable of?"
    scene black with dissolve
    stop music fadeout 5
    pause 2
    return

label day1_6C:
    scene bg warehouse with dissolve
    pause 1
    scene bg warehouse night with dissolve
    "Thank goo I didn't mess anything up."
    # Cee appears
    # Cee iloinen
    show cee iloinen at middle with moveinleft
    show cee iloinen at hop
    play music metkut
    C "Well done, [MC]. I'm happy to inform you that I'm pleased with your performance."
    MC "Glad to hear that, Cee."
    "Now this is a surprise. I haven't seen Cee this peppy before."
    # Cee tosi iloinen 
    show cee tosi iloinen
    C "You are well beyond capable. Perhaps we should host a soiree to celebrate your prowess."
    MC "Now now, Cee, you're exaggerating. I was simply doing my job."
    C "No need to be so modest, my dear sluggish companion. You were MARVELOUS." 
    show cee tosi iloinen at hop
    C "A raging tempest destroying everything in its way. Nay, a ferocious SHARK gnashing its teeth and tearing through innocent flesh!"
    "All I did was slip in some fish, and they're this pleased with me? Wow."
    show cee iloinen
    C "Ahhh, I just might shed a tear if I could."
    # Cee iloinen
    show cee iloinen
    MC "Um, sure. If you say so."
    "I'm pretty sure I haven't done anything extraordinary, but here Cee is, singing my praises."
    show cee perus
    C "Small fish like us could use a shark like you. Even the bravest landlubbers go pale at the sight of a shark baring its teeth."
    MC "Me? A shark? Um, wow. Thanks, I guess?"
    C "You're very welcome."
    C "Before you retreat into your slimy cave…"
    C "Have you remembered to take enough time for yourself today? What's that trendy piece of corporate jargon everyone is using these days…"
    # Cee tosi iloinen
    show cee tosi iloinen
    C "Oh, right. MICRO BREAKS. Have you taken any micro breaks amidst the dangers of working life?"
    "Why is Cee interested in me all of a sudden?"
    menu:
        "How should I react?"
        "\"No, but I guess I could give it a try.\"":
            show cee iloinen
            C "Oh, definitely!"
            C  "Do you wish to hear how I spend MY micro breaks?"
            MC "Sure thing."
            # Cee hullu hymy
            show cee tosi iloinen
            C "Five minutes in the break room freezer."
            MC "Freezer?!"
            show cee hullu hymy at hop
            stop music fadeout 3
            C "It reminds me of the deepest, coldest parts of the ocean."
            pause 0.5
            # Cee iloinen
            show cee iloinen
            C "It reminds me of home."
            play music metkut
        "\"Nah. Not so keen on that corporate jargon.\"":
            # Cee perus
            show cee perus
            C "Truly?"
            MC "Yeah. Our superiors always come up with new, trendy words that actually mean nothing."
            MC "Micro break is a fancy word for closing your eyes for a minute or grabbing a cup of coffee when you can."
            show cee at hop
            C "Hmm. Perhaps you are right, my fellow prisoner."
        "\"Since when were you this interested in my well-being, Cee?\"":
            show cee iloinen at hop
            C "There is no reason to be suspicious, [MC]."
            show cee karmiva hymy
            C "Ever since this friendly little race to power started, I have been observing you. Monitoring you. Watching you."
            MC "That's three reasons to be suspicious, Cee!"
            show cee iloinen
            C "I only have your best interests in mind, my dear sluggish companion." 
    label after_menu:
    show cee perus at hop
    C "Anyhow. We should stick together, you and I. We must free ourselves and rise above these obtuse plebeians."
    show cee iloinen
    # Cee iloinen
    C "No longer shall we remain oppressed by the uncouth masses. We shall rise from the waves and build a new world where us sea creatures are treated with proper respect!"
    "Proper respect, huh? That… doesn't sound too bad, actually. Everyone deserves to be treated respectfully!" 
    MC "Tell me more about this new world of yours."
    # Cee tosi iloinen
    show cee tosi iloinen at hop
    C "Oh, it's going to be WONDERFUL. First of all, everyone from sirens to sea serpents is treated equally."
    show cee perus
    MC "That's nice, but what about those of us who don't have, um, gills and all that?"
    # Cee smiles
    show cee iloinen
    C "Don't worry your slimy little head about it."
    show cee tosi iloinen
    C "We are partners in crime, you and I! I shall not allow the tides of change to whisk you away and drown you."
    MC "Thanks, I guess?"
    # Cee iloinen
    show cee iloinen
    C "You're welcome, [MC], you're very welcome."
    pause 0.5
    MC "So, anything else?"
    show cee iloinen at hop
    C "Oh my dear comrade, I'm just getting started. Imagine PARADISE. What's the first image that pops into your mind?"
    MC "Hmm… Paradise island perhaps? Palm trees, sand?"
    MC "Cute little coconut drinks with umbrellas?"
    MC "The sea?"
    # Cee tosi iloinen
    show cee tosi iloinen at hop
    C "Précis!"
    MC "I'm not sure I follow. Aren't we talking about making this company a better place for us all?"
    # Cee iloinen
    show cee iloinen
    C "Indeed we are."
    MC "So..?"
    # Cee tosi iloinen
    show cee tosi iloinen at hop
    pause 1.5
    "Huh. The warehouse IS quite large. I suppose it could fit a couple of palm trees."
    show cee iloinen
    C "No more dusty corridors or ghastly warehouses - only glittering waves and endless peace of mind."
    show cee perus
    C "And sand, I suppose. For you land-dwellers."
    show cee iloinen
    MC "How kind of you, Cee."
    # Cee perus
    show cee perus
    C "I see no reason to work ourselves to death in lackluster conditions. Us monsters require stimuli in order to remain productive."
    MC "I actually agree with you on this one. None of us are machines… unless you count Galahad the golem from the collecting department as one. Maybe not."
    show cee iloinen
    C "I think we can all agree that glittering waves and silly little drinks make working much more pleasant and therefore more efficient."
    # Cee tosi iloinen
    show cee tosi iloinen at hop
    C "I can already see the sick leave statistics dropping!"
    MC "Wow, Cee, I'm actually starting to feel enthusiastic about this idea of yours. Well done."
    "Could this warehouse really be turned into a paradise island? Could Cee really achieve that if we let them?"
    "I hope so. I can practically already taste the pina colada and feel the sun on my non-existent skin."
    show cee perus
    # Cee perus
    C "That being said, I do hope you aren't considering siding with Karkhos. Using your talents for the benefit of him and his tomfoolery would be an utter waste."
    show cee vihainen at hop
    C "Ugh, we cannot choose that simple-minded brute as our leader."
    MC "Brute?"
    show cee perus
    C "Aye. Were Karkhos in charge, he might turn a simple business meeting into a rencontre. Imagine the destruction. The horrors. The screams!"
    "That doesn't sound like Karkhos. The guy IS an orc, but…"
    MC "Hold on for a second, Cee. Aren't you being a bit too harsh on him?"
    MC "Karkhos may look like a bloodthirsty fellow, but he hasn't been dabbling in destruction after his death, has he? He's probably the chillest monster I know." 
    show cee vihainen
    C "Bah, fine. But if it's not his fists that are going to destroy this corporation, his lack of enthusiasm is."
    show cee perus
    C "All Karkhos wants to do is, well, NOTHING. He lacks the passion a proper leader should have."
    show cee vihainen at hop
    C "If Karkhos becomes our leader, I bet the first thing he'll do is go on a six-week vacation. He'd practically leave us drowning! I will not stand for such foolishness!"
    "Hmm. That does sound something like Karkhos might do."
    "I'm not one to dedicate myself entirely to work, but I AM feeling a bit concerned about Karkhos' leading capabilities."
    MC "Yeah, I guess you do have a point. Karkhos isn't exactly the ambitious type."
    show cee perus at hop
    C "Indeed. But our dear Agatha is. Do we truly need another power-hungry autocrat now that the first one is finally gone?"
    "As if you aren't trying to take over as well, Cee…"
    MC "Agatha is just a hard-working monster who wants everybody else to work hard as well. Nothing wrong with that."
    show cee kauhistus at hop
    C "Nay, my fellow prisoner. Can't you see all she cares about is making us work to the bone?"
    show cee perus
    C "Do you have any idea what would happen if that winged monomaniac was in charge of the infernal machine?"
    MC "No, but I suppose you do."
    # Cee karmiva hymy
    show cee karmiva hymy at hop
    C "Carnage, [MC]. Utter carnage."
    MC "You can't be serious, right?"
    C "On the contrary."
    show cee perus
    # Cee perus
    C "If we let Agatha get in charge, we'll be nothing more than easily disposable machine parts. And do machine parts have any other meaning than serve until they break? Nay." 
    show cee alakuloinen
    C "If Agatha takes over, you can kiss your precious work life balance goodbye. We'll be working from dusk to dawn, until we can barely stand."
    C "The warehouse will be her altar and we'll be the sacrifice. Only to impress this imposing lump of fur we call Boss." 
    "Yikes! Maybe Cee does have a point after all."
    "I don't think Agatha knows the meaning of work life balance. Thank goo Cee and I seem to be on the same page when it comes to leisure time."
    MC "Hmm. It's not like I want to dedicate myself entirely to our work. I have other interests as well, and I value my free time."
    # Cee smiles
    show cee iloinen
    C "I'm pleased we see eye to eye."
    pause 1
    show cee tosi iloinen at hop
    C "I'm afraid I must retreat now. The new world I'm planning needs all of MY free time."
    MC "See you later then, Cee. I'll let you guys know when I've made up my mind."
    show cee perus
    C "Until you make your decision, I remain pendulous, swinging above the swirling sea. My fate lies in your slimy appendages, [MC]."
    # Cee leavesR
    play sound footsteps
    hide cee with easeoutleft
    stop sound fadeout 3
    "Cee hurries off. They can be really convincing when they want to, huh?"
    "Hmm."
    "Choosing between doing nothing, doing too much, and paradise island, seems quite simple, when you put it that way. But is it really that simple?"
    "Ugh, I need to get home and de-stress before thinking about any big decisions."
    scene black with dissolve
    stop music fadeout 5
    pause 2
    return
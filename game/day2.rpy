
label day2_3A:

    scene bg hallway posters
    #footsteps
    "My lunch break evaporated once again. I'll just eat the emergency snack bar I keep at my workstation."
    # Cee appears
    show cee perus with moveinright
    C "MC!"
    MC "Eeek!"
    C "Fret not. You must come with me."
    MC "But the break's almost over."
    C "The tidings I bring concern Miss Agatha. I'm certain you would be interested. It shall not take long."
    "Cee ushers me into a crevice in the corridor. I follow, initially reluctant, except…"
    "Ever since Boss left, I haven't really talked with Cee. What's so important that they waited for me, after storming off like that? I'm a bit curious."
    "Cee speaks in a lower voice than usual. Which, granted, is still pretty loud."
    C "Pardon the precautions. I had to make sure that the tiny control freak wasn't following us."
    C "I've heard some rather concerning rumours about you and Miss Agatha. The hallways are whispering that you have taken a liking to her rigorous ways."
    C "MC, you must not fall under her spell!"
    C "I have seen her true colors. Once, she interrupted my work just to tell me I wasn't projecting enough enthusiasm. Such insolence!"
    # Cee looks angry
    C "Why should we show enthusiasm while performing these repetitive, mundane tasks? Can't she fathom that my passions lie elsewhere entirely?"
    MC "She isn't that bad once you get to know her. She's working hard to protect her fellow monsters."
    C "That, my foolish comrade, is what she WANTS you to think."
    C "Do not be fooled by her big eyes and paper thin wings. Underneath that disguise you'll find a ferocious predator, poised to bite those standing in her way." 
    MC "Hey, that's going too far."
    C "Hardly! What shall a mere worker do, when told to triple their efforts? To try is to perish, whilst to not try is to be bitten."
    C "Were we to work harder, would it not in actuality decrease our output? Eat the marlin's roe, and be bereft of the fish. She is thinking short term, when what matters is the long term."
    C "Unwittingly, she may yet be furthering my goals. She will wring dry this den of Loot, and whilst we wither, she will flutter away to greener pastures. Rather than a moth, she is a locust. Nay, a disease!"
    MC "Stop."
    C "...!"
    MC "I appreciate the sentiment, but I won't let you badmouth Agatha."
    MC "She cares about the warehouse and wants us to succeed."
    C "Bah! I did not think you simple-minded enough to fall for her ruse. Consider me disappointed."
    C "I have given my augury. Since you wish to remain ignorant, do not cry for help once the predator attacks."
    # Cee leaves
    hide cee with moveoutleft
    "I'm speechless. It's not okay to speak about coworkers like that."
    "I can't tell if this was just Cee's personal dislike, or an actual worry about our wellbeing. Maybe it was both. Does sound like Agatha should have been nicer to Cee."
    "Once, even I used to think she was an inconsiderate nitpicker. But I understand her better now. All Agatha is trying to do is make the land safer for monsters. Nothing predator-like about that."
    "...Right?"


label day2_5A:
    scene bg breakroom posters posters night 
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
    A "I just feel like… They work here, right? So why won't they {i}work{/i}?"
    #work itallics
    show agatha vihainen at hop
    A "If they don't want to do it, they could just- just…"
    show agatha alakuloinen at hop
    "She bites her lip."
    #conditional jos lukenut 2.3A:n: LISÄÄ MYÖHEMMIN KONDITIO KUN TEKSTI OLEMASSA!!!!
    # if read2_3A = True:
    #     "I think back to Cee's story of Agatha demanding they show more enthusiasm. Was there more to it than Cee told, or could she really be plotting death by overwork?"
    #     menu:
    #         "Well, everyone's different."
    #             A "But we're all supposed to be working together!"
    #         "I get it. I wish they'd do more."
    #             A "Right??"
    show agatha vakava
    A "I just… When I looked around, I saw Karkhos napping in a box and Cee jamming the conveyor belt with fish!"
    show agatha pelokas
    A "And- and- and what are we going to tell Boss when he comes back?!"
    A "Our output is {i}half{/i} of what it should be!"
    #half itallics
    A "[MC], I can't make up for this much slacking off!"
    show agatha pelokas at hop
    A "I mean, I would if I could, but I can't!"
    show agatha alakuloinen
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
    A "Yes?"
    show agatha alakuloinen at hop
    A "I know it sounds phoney, but each piece of Loot really matters to someone out there."
    MC "I mean, you're not wrong, but…"
    show agatha alakuloinen
    A "..."
    MC "...?"
    show agatha vakava at hop
    A "...Fine. Okay. [MC], how much do you know about the Human Wilds?"
    MC "I mean, I've seen pictures?"
    show agatha vakava at hop
    A "Right."
    "Her eyes are distant for a moment, before drilling back into me with their usual uncanny brightness."
    A "I … grew up in the Human Wilds. There was no Loot system back then."
    A "Most of my kind are nectar farmers, and it's dangerous work. When a human stumbles on you in the flower field…"
    show agatha pelokas at shake
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
    A "[MC], if your vote comes out in my favor tomorrow, we can double- no, triple- no, {b}QUADRUPLE{/i} the amount of lives each day!"
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
    hide agatha with moveoutright
    "She flutters back towards the packing area, humming a cheerful tune."
    "I worry a bit about how long she's going to keep working, but at least she cheered up."
    "I also feel energized, looking at her. Maybe I'll go for an evening waddle before returning home."

label day2_5B:

    scene bg hallway posters night
    "Second day done. Can't wait to go home and melt in my bathtub shaped hole. Keeping my professionally cubistic shape together is tiring."
    "I can still hear conveyor belt sounds coming from the warehouse. Some of the guys are still working."
    "As for who isn't, I have a guess."

    # corridor BG
    # karkhos sprite
    scene bg hallway posters night
    show karkhos perus
    "Knew it."
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

    # (Conditional: jos 2.3B (edellinen skene) saatu) LISÄÄ MYÖHEMMIN KONDITIO KUN TEKSTI OLEMASSA!!!!
    # "When he first started working at the warehouse, I did note he's more animated than other animated corpses. To think that all this time, he was working under a necromantic contract."
    # "Being forced to work… The rest of us chose this job, but Karkhos didn't get to choose. It's possible he doesn't enjoy a single thing about working here."

    # footsteps, they are both walking
    show karkhos perus
    K "You look to be thinking real hard."
    show karkhos iloinen
    K "Maybe it's cuz you still have questions about my great workplace improvement plan?"
    K "Well, the walk to the big intersection is a long one. If you wanna ask, now's the time. Q and A. Karkhos the Destroyer: an open book."
    "I do have a lot of questions. Whether he likes working here, for one. But all these years, I've never asked my coworkers anything personal. Monsters usually tell it straight if they want to. Unless they're a sphinx."
    "Suddenly, I'm all nerves. Even though I don't have any."

    menu:
        "Talk about the weather":
            MC "The dungeon air today sure is on the moist side."
            show karkhos iloinen at hop
            K "Huh? Sure is. Moisture good for ya?"
            MC "For slimekind, hydration is very important. Mom used to spray me with sugar water during dry seasons."
            show karkhos alakuloinen
            K "For me, moisture's trouble. I gotta be careful my brain doesn't become a residence for some mold. I've already got a tenant, and Wormy even pays rent. And eats the mold."
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
    K "Nah, man. I used to be an orc. The way I died was stupid. Didn't have Loot on me, while my clan mates did. The last thing I saw was their retreating feet. That should've been it for me, but I woke up in the chain's restoration facility."
    K "No hard feelings to the necromancer who patched me up. Though I think she took my kidney. And something else over in my mid abdomen. The cavity sometimes gathers liquid."
    # K happy sprite
    show karkhos iloinen
    K "Oh well! I've still got lots of organs to spare. Not like they do much now. They've probably spoiled anyway."
    MC "You were… happy to be turned into an undead?"
    # K neutral sprite
    K "Getting a new chance at life doesn't happen to everyone. There was still a lot I wanted to experience, and I was happy to give back. The Loot saved my clan mates, and the chain gave me a second life."#
    show karkhos perus
    K "In the beginning, didn't matter I was destined to work until my body fell apart."
    # sad sprite
    show karkhos alakuloinen
    K "But this job… Seems I was happy too soon, huh?"
    K "I've worked all my life, but even after death, the grind goes on." 
    # angry sprite
    show karkhos pikkuviha
    K "If monsters must work, then I demand it be something we don't tire from doing! What's wrong with that?"
    K "To make monsters contort themselves into rigid time slots, it's just unnatural. We should be allowed some flexibility in the hours we work."
    MC "To your credit, no other zombie would have lasted a day in the warehouse."
    "His angry eyebrows lift in minor triumph."
    show karkhos pikkuviha at hop
    K "Yeah! No zombie can beat me."
    MC "Maybe you just need a holiday? When's the last time you had time off?"
    show karkhos alakuloinen
    K "When I was alive. Back in the orc village, we had a thing called \"rest day\". No such things here."
    show karkhos vihainen at shake
    K "If I had a few days off, I'd go lava surfing, cave diving, ride a wyrm and kiss the moon. Just because I'm dead doesn't mean I can't LIVE A LITTLE."
    "The shout echoes down every branching cavern. Anyone creeping around the dungeon probably turned to run."
    show karkhos perus at hop
    K "That being so, we need to reach a resolution with this fight. Cee and Agatha need to learn that enough's enough. Tomorrow at lunch, we'll check your dispatch records. The winner will have their way with the warehouse."
    show karkhos pikkuviha
    K "If we all refuse to work these unreasonable hours, the Boss will have no choice but to grant our demands."
    K "I'll win by any means necessary, because I'm right."
    MC "Yeah! It's not fair you're being forced into manual labor, even though you're tired."
    show karkhos perus at hop
    K "What? No! MC, it's not fair to ANY of us!"
    K "Everyone else has just gone numb and capitulated to the horrible conditions. Like they were, I dunno, a bunch of zombies?"
    show karkhos alakuloinen at hop
    K "...Not you, of course! But everyone else."

    menu:
        "Yeah! They're all zombies!!!":
            show karkhos vihainen at shake
            K "YEEEEAHHH!!!!"
            "The roar echoes. The sound is like a warband of orcs rushing toward us. It's exhilarating."
        "That was a bit mean.":
            show karkhos kauhistus at hop
            "Karkhos clears his throat."
            show karkhos alakuloinen
            K "My bad. Got carried away. I'm sure the other two think they can handle the workload."

    "The great intersection is busy this time of evening. Dungeon guards are on their patrol. Tinkerers are running to reset traps, and the cleaning crew is marching to mop up dead humans."
    show karkhos perus at hop
    K "Well, my cave's that way. Was nice chatting."
    # karkhos tosi iloinen
    show karkhos tosi iloinen at hop
    K "I have no idea what's going to happen tomorrow. Pretty exciting."
    hide karkhos with moveoutright
    "I wave. Karkhos enters the stream of monsters, and disappears behind a bend in a cavern."
    "Tomorrow, huh. I have a feeling that after tomorrow, nothing will be the same."

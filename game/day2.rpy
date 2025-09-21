


label day2_5A:
    scene bg breakroom night
    "As I start heading home, I see something shocking out of the corner of my eye."
    show agatha alakuloinen
    "Is that… Agatha? Sitting in the break room and not working?"
    "I mean, she shouldn't be, strictly speaking, but usually she can never be pried away until well after everyone else has left."
    "I catch myself looking around for threats. Something must be fundamentally wrong with the world."
    A "UuUugGHhh…"
    "I'm almost too spooked to speak up."
    MC "Agatha…?"
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
    A "If they don't want to do it, they could just- just…"
    "She bites her lip."
    #conditional jos lukenut 2.3A:n: LISÄÄ MYÖHEMMIN KONDITIO KUN TEKSTI OLEMASSA!!!!
    # if read2_3A = True:
    #     "I think back to Cee's story of Agatha demanding they show more enthusiasm. Was there more to it than Cee told, or could she really be plotting death by overwork?"
    #     menu:
    #         "Well, everyone's different."
    #             A "But we're all supposed to be working together!"
    #         "I get it. I wish they'd do more."
    #             A "Right??"
    A "I just… When I looked around, I saw Karkhos napping in a box and Cee jamming the conveyor belt with fish!"
    A "And- and- and what are we going to tell Boss when he comes back?!"
    A "Our output is {i}half{/i} of what it should be!"
    #half itallics
    A "[MC], I can't make up for this much slacking off!"
    A "I mean, I would if I could, but I can't!"
    "She puts her head in her hands."
    MC "There, there…"
    MC "Look on the bright side. Our output's still good compared to before the new system."
    A "I know. But I- I was…"
    "Nooo! I wanted to improve her mood, but she looks like she might cry!"
    A "I was really looking forward to the higher productivity."
    "That's actually a tear on her face."
    MC "..."
    MC "I'm not the brightest, but is this really about productivity?"
    A "..."
    A "Yes?"
    A "I know it sounds phoney, but each piece of Loot really matters to someone out there."
    MC "I mean, you're not wrong, but…"
    A "..."
    MC "...?"
    A "...Fine. Okay. [MC], how much do you know about the Human Wilds?"
    MC "I mean, I've seen pictures?"
    A "Right."
    "Her eyes are distant for a moment, before drilling back into me with their usual uncanny brightness."
    A "I … grew up in the Human Wilds. There was no Loot system back then."
    A "Most of my kind are nectar farmers, and it's dangerous work. When a human stumbles on you in the flower field…"
    "She shudders."
    MC "What? What?"
    A "They {i}swat{/i} at you!"
    #swat itallics
    A "They're enormous and they scream and flail and they look at you like you're some kind of nasty- nasty… human."
    A "One day when I was just a larva, my father returned home late in the evening, limping back because a human broke his wing."
    A "Since then, he's always had trouble flying long distances. But I'm glad nothing worse happened."
    MC "I'm so sorry. I can't imagine… I never had to worry about my moms and pops that way."
    A "I'm glad you haven't had to fear humans."
    A "You know, Karkhos likes to go on and on about how nice it was to be out in the sunlight, but I like it here."
    A "It's like we're under a protective dome, day in and day out."
    A "When we moved here, I had my first restful sleep since emerging from my cocoon."
    MC "I'm glad you're here now."
    #A smile
    A "Yeah. Me too."
    A "After I started working here, I got a letter from my cousin."
    A "She told me that Loot had saved her mate's life."
    A "It means the world to me that we can make life better for everyone I left behind."
    MC "I… hadn't really thought about it, but I'm happy that our work means so much."
    A "It means {i}everything{/i}."
    #everything itallics
    "There's that intense look again."
    A "[MC], if your vote comes out in my favor tomorrow, we can double- no, triple- no, {b}QUADRUPLE{/i} the amount of lives each day!"
    #quadruble boldattu
    A "We'll all work hard together, knowing that each box we pack helps countless monsters."
    "I'm pretty sure we could count them, but… Sure."
    MC "Yeah, sounds good!"
    A "Yes! I look forward to a bright and productive future with you. As soon as we tally the results tomorrow."
    "She jumps up from the table."
    A "Thank you for lending an ear, [MC]. I feel better. I think I'm ready to go back to work."
    "The workday is over, though…?"
    MC "Uh, okay. Happy to help."
    A "See you tomorrow!"
    MC "Yeah. See you!"
    hide agatha with moveoutleft
    "She flutters back towards the packing area, humming a cheerful tune."
    "I worry a bit about how long she's going to keep working, but at least she cheered up."
    "I also feel energized, looking at her. Maybe I'll go for an evening waddle before returning home."

label day2_5B:

    "Second day done. Can't wait to go home and melt in my bathtub shaped hole. Keeping my professionally cubistic shape together is tiring."
    "I can still hear conveyor belt sounds coming from the warehouse. Some of the guys are still working."
    "As for who isn't, I have a guess."

    # corridor BG
    # karkhos sprite
    scene bg hallway night
    show karkhos perus
    "Knew it."
    K "Out the door, right on the dot."
    MC "Old habits die hard."
    K "Die is right! You're crawling along like YOU are the token zombie."
    K "But I had a reason for waiting. Tomorrow's the day of truth. Wanted to check in on you."
    K "Thought we could walk to the big intersection together?"
    MC "Oh. Sure."
    K "Awesome!"
    "He's really spirited. Usually, he leaves work dragging his feet, groaning like a zombie. The regular kind—the kind that gurgle, drool and are real culinarians when it comes to internal organs."

    # (Conditional: jos 2.3B (edellinen skene) saatu) LISÄÄ MYÖHEMMIN KONDITIO KUN TEKSTI OLEMASSA!!!!
    # "When he first started working at the warehouse, I did note he's more animated than other animated corpses. To think that all this time, he was working under a necromantic contract."
    # "Being forced to work… The rest of us chose this job, but Karkhos didn't get to choose. It's possible he doesn't enjoy a single thing about working here."

    # footsteps, they are both walking
    K "You look to be thinking real hard."
    K "Maybe it's cuz you still have questions about my great workplace improvement plan?"
    K "Well, the walk to the big intersection is a long one. If you wanna ask, now's the time. Q and A. Karkhos the Destroyer: an open book."
    "I do have a lot of questions. Whether he likes working here, for one. But all these years, I've never asked my coworkers anything personal. Monsters usually tell it straight if they want to. Unless they're a sphinx."
    "Suddenly, I'm all nerves. Even though I don't have any."

    menu:
        "Talk about the weather":
            MC "The dungeon air today sure is on the moist side."
            K "Huh? Sure is. Moisture good for ya?"
            MC "For slimekind, hydration is very important. Mom used to spray me with sugar water during dry seasons."
            K "For me, moisture's trouble. I gotta be careful my brain doesn't become a residence for some mold. I've already got a tenant, and Wormy even pays rent. And eats the mold."
            "Wormy wriggles up to nod vehemently."
            "...! This is it, the perfect lead in."
        "Discuss current affairs":
            MC "I heard humans attacked the dire-frog village. Thankfully nobody died. They all had Loot. But their homes got trampled."
            K "I didn't hear about this! News reaches the dungeon so slow."
            # angry sprite
            K "Those villainous humans always take advantage of the vulnerable. They are despicable."
            K "Well. At least we won't be seeing undead frogfolk just yet."
            "...! This is it, the perfect lead in."
        "Ask how he died":
            "Tact's for wimps!"

    MC "I've always just been a slime. But I've gathered you were a different type of monster before? If it's not too weird to ask, how'd you become undead?"
    K "Uh. When I said it's a Q and A, I sorta hoped you'd ask about workers' right to more breaks."
    MC "Sorry. Your death is probably a difficult memory."
    K "Nah, man. I used to be an orc. The way I died was stupid. Didn't have Loot on me, while my clan mates did. The last thing I saw was their retreating feet. That should've been it for me, but I woke up in the chain's restoration facility."
    K "No hard feelings to the necromancer who patched me up. Though I think she took my kidney. And something else over in my mid abdomen. The cavity sometimes gathers liquid."
    # K happy sprite
    K "Oh well! I've still got lots of organs to spare. Not like they do much now. They've probably spoiled anyway."
    MC "You were… happy to be turned into an undead?"
    # K neutral sprite
    K "Getting a new chance at life doesn't happen to everyone. There was still a lot I wanted to experience, and I was happy to give back. The Loot saved my clan mates, and the chain gave me a second life. In the beginning, didn't matter I was destined to work until my body fell apart."
    # sad sprite
    K "But this job… Seems I was happy too soon, huh?"
    K "I've worked all my life, but even after death, the grind goes on." 
    # angry sprite
    K "If monsters must work, then I demand it be something we don't tire from doing! What's wrong with that?"
    K "To make monsters contort themselves into rigid time slots, it's just unnatural. We should be allowed some flexibility in the hours we work."
    MC "To your credit, no other zombie would have lasted a day in the warehouse."
    "His angry eyebrows lift in minor triumph."
    K "Yeah! No zombie can beat me."
    MC "Maybe you just need a holiday? When's the last time you had time off?"
    K "When I was alive. Back in the orc village, we had a thing called \"rest day\". No such things here. If I had a few days off, I'd go lava surfing, cave diving, ride a wyrm and kiss the moon. Just because I'm dead doesn't mean I can't LIVE A LITTLE."
    "The shout echoes down every branching cavern. Anyone creeping around the dungeon probably turned to run."
    K "That being so, we need to reach a resolution with this fight. Cee and Agatha need to learn that enough's enough. Tomorrow at lunch, we'll check your dispatch records. The winner will have their way with the warehouse."
    K "If we all refuse to work these unreasonable hours, the Boss will have no choice but to grant our demands."
    K "I'll win by any means necessary, because I'm right."
    MC "Yeah! It's not fair you're being forced into manual labor, even though you're tired."
    K "What? No! MC, it's not fair to ANY of us!"
    K "Everyone else has just gone numb and capitulated to the horrible conditions. Like they were, I dunno, a bunch of zombies?"
    K "...Not you, of course! But everyone else."

    menu:
        "Yeah! They're all zombies!!!":
            K "YEEEEAHHH!!!!"
            "The roar echoes. The sound is like a warband of orcs rushing toward us. It's exhilarating."
        "That was a bit mean.":
            "Karkhos clears his throat."
            K "My bad. Got carried away. I'm sure the other two think they can handle the workload."

    "The great intersection is busy this time of evening. Dungeon guards are on their patrol. Tinkerers are running to reset traps, and the cleaning crew is marching to mop up dead humans."
    K "Well, my cave's that way. Was nice chatting."
    # karkhos tosi iloinen
    show karkhos tosi iloinen at hop
    K "I have no idea what's going to happen tomorrow. Pretty exciting."
    "I wave. Karkhos enters the stream of monsters, and disappears behind a bend in a cavern."
    "Tomorrow, huh. I have a feeling that after tomorrow, nothing will be the same."

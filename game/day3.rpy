label day3_1C:  #Cee wins
    scene bg hallway
    "They went inside my dispatch platform some time ago. This is it."
    "!! They're coming out!!"
    "Oh… The suspense is making my digestive region sick."
    # Cee, Karkhos & Agatha sprites
    # Cee tosi iloinen, Karkhos alakuloinen, Agatha vihainen
    show agatha vihainen zorder 1 at cleft with moveinleft
    show karkhos alakuloinen zorder 2 at cright with moveinright
    show cee tosi iloinen zorder 3 at hop, middle with moveinright
    C "Justice! Finally!"
    # Cee grins
    show cee hullu hymy
    show agatha alakuloinen kyynel at shake2
    A "How could this be? Our beloved company will be driven into chaos!"
    show karkhos at hop
    K "I have a bad feeling about this as well…" 
    show cee vihainen at hop
    show agatha alakuloinen kyynel at cleft
    C "Heed my words. My triumph was unequivocal and I will not allow its legitimacy to be questioned. From this day onward, I shall be the harbinger of change."
    C "And you two shall obey my commands without question. Have I made myself clear?"
    # Agatha alakuloinen
    show agatha alakuloinen at hop
    A "Hmph. Yes."
    # Karkhos perus
    show karkhos perus at hop
    K "Sure thing."
    show cee iloinen at hop
    C "Marvelous."

    "I can practically taste the coconut drinks already. Coming to work every morning will become so much easier with proper motivation!"
    C "I shall start orchestrating the necessary changes immediately. This dull, disconsolate den has seen the last of its miserable days."
    menu:
        "\"What are you going to do first, now that you're in charge?\"":
            # Cee tosi iloinen
            show cee iloinen at hop
            C "Well. I did promise you land-dwellers some sand, didn't I?"
            MC "You sure did. Good to know you haven't forgotten us little monsters now that you're in charge, haha."
            show cee tosi iloinen
            C "As if I could ever forget my dear benevolent benefactor."
            show cee iloinen
            C "I shall send my minions to find the softest of sands and create the paradise we all deserve!"
            "Minions? It seems that Cee has already adapted to their new position."

        "\"If you need a list of silly little drinks that'll boost our motivation, you know who to call.\"":
            show cee tosi iloinen
            C "Splendid! I knew I could always count on you. So what are you suggesting?"
            MC "First of all, no matter what we're going to drink, it has to be served in a coconut shell. Don't forget to add the little umbrella decorations either."
            show cee iloinen
            C "Duly noted. What else?"
            MC "Tropical fruit and colors are always good. However, the drinks can't be too sweet - the aftermath of sugar rush will only wreck our productivity. You've gotta be careful!"
            show cee perus
            C "Thank you for your input, [MC]. I'll see what I can do."  
            
    
    show cee tosi iloinen at hop
    C "Ahh, I am practically brimming with energy. My great master plan shall finally come into fruition!"

    MC "I'm looking forward to all the changes you've planned. Soon we'll have a fairer workplace for everyone."
    show cee karmiva hymy
    C "Précis. I've got it all planned out. My effulgence will guide us all towards a wetter tomorrow!"
    MC "Um, you mean BETTER tomorrow?"
    show cee iloinen
    C "Ah, yes. That, too, of course."
    MC "C'mon, Karkhos, Agatha, let's go take a break and leave Cee to their own devices."
    #Agatha and Karhkos leave with the MC
    hide agatha with moveoutleft
    hide karkhos with moveoutright
    "Karkhos and Agatha follow me, not even looking back at the warehouse."
    "Everything seems fine, so why am I feeling a bit uneasy right now?"
    show cee hullu hymy at shake
    # Cee hullu hymy
    C "Hehehe. Hehehehehehehehehehe."
    scene black with fade
    pause 1.0


#TODO lisää joku ääniefekti ehkä? 
    #label C2 Cee has messed up big time

    scene bg warehouse with dissolve # TODO: cee ending versio tähän 
    # Käytävät tulvivat. Märkää loottia lilluu vedessä.
    "Paradise island? That's what we were promised, but…"
    # Karkhos appears.
    # Karkhos alakuloinen
    show karkhos alakuloinen at middle with moveinleft
    #TODO hitaampi moveinleft
    K "Ugh, it's so hard to move through these waters. Guess I'm not the only one who's not gonna make it to the next shift on time."
    #Karkhos disappears
    hide karkhos with moveoutright
    "Our workplace has become a water dungeon."
    "No sun, no palm trees, no silly little drinks - even the water is murky and dirty."
    "Well. I suppose we DO have sand like Cee promised, but it's mostly underwater. I can kiss the dream of getting to make sand castles during breaks goodbye."
    A "Hey, watch where you're going!"
    # Agatha appears
    # Agatha vihainen
    show agatha vihainen at middle, shake2 with moveinright
    A "Oohh, I dropped my file! I can't dive after it. Someone help me!"
    hide agatha with moveoutright
    #Agatha disappears

    "Most of the place is flooded. Every room is like a secluded island and getting from one island to another is far from easy."
    "Most of our work equipment isn't fit to be used in underwater conditions, either."  
    "What's more, some of us can't come to work anymore."
    "There's a vampire from the collecting department who can no longer do her job because of the running water. She seems pretty stressed about it, and rightfully so."

    "Our sea creature colleagues seem happy, though. They're faster and more productive than the rest of us."
    "In fact, I think their production levels have skyrocketed, and so has their satisfaction with work life. They all sing Cee's praises."
    "Yeah, the sea creatures are thriving, but the rest of us are struggling."
    "Sea creature loot obviously doesn't suffer from these circumstances. We're able to produce and distribute more of it than ever. Regular loot, however…"
    "Agatha mentioned that people are already complaining about destroyed spell scrolls and mouldy magic boots."
    "Several land-dwelling monsters are upset that their loot is now considered faulty when it doesn't do well in water."
    "It's the same as before, just with the roles reversed. Cee and the other sea monsters are now the norm, and the rest of us feel inadequate."
    "I don't think this is what Cee had in mind when they were planning on changing things."

    # Cee appears.
    # Cee tosi iloinen.
    show cee tosi iloinen at middle, shake2 with moveinright
    "Cee looks cheerful, but it's obvious they're stressed about something."
    show cee at hop
    C "Greetings, [MC]! How is life in paradise? I've been so busy with all the logistics and renovations that I haven't had the time to chat with my dear benefactor."
    MC "This is hardly the paradise island I had in mind, Cee."
    show cee perus
    C "Truly? Is this about the drinks with the little umbrellas? Not to worry - I can assure you they are the very next thing on my list of priorities."
    show cee iloinen at shake2
    "Cee smiles nervously at me."
    C "The life of an autocrat is far from easy. I cannot please everyone."
    C "The sea creatures demanded liberation, respect, and better working conditions - of course I made those things my priority."
    show cee at hop
    C "Besides, you got your precious sand, did you not? I kept my promise!"
    MC "Yeah, but it's all underwater. This is not a paradise island, Cee, this is a water dungeon!"
    MC "Everything is falling apart. The sea creatures are happy, but everyone else is miserable."
    # Cee perus
    MC "People are complaining about wet loot, and it's already causing us trouble with the humans. It's become difficult to move between rooms and do our jobs. Some of us can't even get to work anymore."
    show cee kauhistus
    MC "I believed in you, Cee - this can't be what you had in mind when you said you wanted to improve things!"
    # Cee vihainen
    show cee vihainen at hop
    C "How dare you! I am the very picture of omnipotence! My work has made me popular amongst our peers!"
    "That's what you say, but I can see beneath the surface, Cee. Where has your confidence gone?"
    MC "Yes, the sea creatures adore you, but how about the rest of the company?"
    C "Bah. If someone complains, I'll just… contain them in an underwater cell or something."
    show cee karmiva hymy at hop
    C "Ha! Problem solved."
    MC "You can't be serious. The Cee I picked to improve our working conditions wasn't a power-hungry dictator. You're better than this!"
    # Cee perus. Gurgling noises.

    # Agatha & Karkhos appear
    # Agatha vihainen, Karkhos pikkuviha
    show cee perus zorder 3
    show agatha vihainen zorder 1 at cright with moveinright
    show karkhos pikkuviha zorder 2 at cleft with moveinleft
    show agatha at hop
    A "There you are! I've had enough of this wet, murky madness!"
    show karkhos at hop
    show cee perus at shake2
    K "My legs weigh a ton. Got sand between my toes."
    # Cee Cee alakuloinen. Louder gurgling noises.
    show cee alakuloinen
    A "Our productivity is dropping!"
    K "Our loot is wet."
    show cee alakuloinen at shake
    A "I heard the vampires are going to riot. They're gonna miss this month's Bloody Friday because they can't come to work thanks to running water."
    K "A nasty gnoll yelled at me on the phone. She said she's gonna leave a negative review."
    MC "Cee, please listen to us. This isn't working and we have to do something until something terrible happens."
    show cee vihainen at shake, hop:
        zoom 1.3
        yoffset 140
    # Cee vihainen. Even louder gurgling noises.
    show karkhos kauhistus
    show agatha vakava
    show bg warehouse with hpunch:
        zoom 1.016
    C "Siiiiiiiiiiiiileeeeeeeeeeeenceeeeeeeeeeee!"
    pause 0.5
    show bg warehouse:
        zoom 1
    hide cee with moveoutleft
    pause 1
    # C storms off. TODO: Swimming sounds.

    MC "Oh no. I'll go after them."
    #Karkhos alakuloinen
    show karkhos alakuloinen
    K "Watch out for the whirlpool between the toilets and the exit. Nearly got stuck in it on my way home yesterday."
    #Agatha and Karkhos disappear
    hide karkhos with moveoutright
    hide agatha with moveoutright
    show bg warehouse with fade:
        zoom 2.0
        yoffset 550
    "Ah, there's Cee! They sure swim fast."
    "Luckily there's a dead-end at the end of this hallway. There's no way Cee can escape me."

    # Cee appears, Cee vihainen
    show cee vihainen at middle with moveinright
    MC "There you are, Cee."
    C "Have you come to mock me? Have you come to laugh at my hubris, at my pathetic state?"
    MC "Of course not. I can see that you're not happy with how things turned out, either."
    # Cee looks frustrated
    show cee at hop
    C "How utterly disappointing!"
    show cee alakuloinen
    C "How could I, the maelstrom amongst ordinary whirlpools, be such a fool? I honestly thought I was making this corporation a better place for us sea creatures!"
    MC "You WERE, Cee. It's just that not everyone here is a sea creature. In fact, most of us aren't. We need something that works for EVERYONE."
    show cee vihainen
    C "That's not what was happening before I took over, mind you. Did you forget how utterly humiliated us sea creatures were? How utterly humiliated I was?"
    C "If I am abased, we'll simply go back to how things were, and I assure you, I am NOT ready for that." 
    MC "I'm not saying we should just go back and pretend nothing happened, Cee. Instead, how about we try something new altogether? And, well, together?"
    # Cee doesn't look convinced
    show cee perus
    MC "Everyone deserves to be treated with proper respect. Sea creatures, land-dwellers, slimes… EVERYONE."
    show cee alakuloinen
    MC "Things were far from perfect before and you tried your best to change them. However, I don't think this is what you wanted, was it?"
    # Cee alakuloinen

    MC "I'm not saying this corporation is just like a big, loving family or anything that cheesy."
    MC "Most of us just want to go to work, make this world just a tiny bit safer of a place for us monsters, and relax after work."
    MC "Big changes are rarely successful without proper planning or time. It's impressive that you managed to do all of this in just a couple of days, but you have to admit that your plan just… backfired."
    "I haven't seen Cee this miserable, well, ever. I guess they've already realized that this isn't what they wanted after all."
    MC "I'm sure we can turn this around if we make the decision and the changes together. How's that sound?"
    show cee at hop
    C "Hmph."
    show cee perus
    C "My fellow prisoner. Before I accede, I need you to convince me that such conduct does not result in yet another disaster."
    C "What makes you think that the land-dwelling masses - who, in fact, are currently rather cross with me - would not create a solution that hurts us sea creatures even more?"
    show cee at hop
    C "What if they thirst for vengeance?"
    MC "I get your point and I'm pretty sure most folks aren't exactly pleased with you right now."
    MC "However, TOGETHER includes EVERYONE - all the sea creatures who work here, and you as well. We can't afford getting things this messed up again. I'm sure the others will understand." 
    show cee alakuloinen at hop
    # Cee alakuloinen
    C "Very well then. It seems that I was right to make you my partner in crime, [MC]. You clearly possess something even I do not."
    C "I take back what I said - you are not a shark sinking its teeth into flesh, you are a gentle whale gliding through the depths."
    MC "Aww, thank you, Cee."
    show bg with hpunch
    show cee perus
    "As I start to head back, Cee grabs me."
    C "I was not being completely honest with you before. I mentioned wanting to be feared by everyone - even Boss."
    MC "Yeah?"
    show cee alakuloinen
    C "The truth is… I wanted to be accepted, not feared."
    C "Boss is immensely popular, so I thought improving this corporation would make the uncouth masses follow me instead of him. Then no one would look down on me ever again."
    MC "Cee…"
    show cee perus
    C "I wanted to be a herald of change, a shining paragon for all the sea creatures that doubt themselves in this system that deems us lacking just because we are different."
    MC "A noble cause."
    show cee alakuloinen
    C "But look where it got me. Now I've made a complete fool out of myself in front of both the landlubbers and my kin."
    C "Perhaps I should just find the deepest, coldest spot in the nearest ocean and disappear for a century. Nay, a millennium."
    MC "Now now, Cee, there's no need for that."
    MC "It's like ripping off a bandage. Yeah, it's gonna sting, but it IS necessary and you'll feel better afterwards. Isolation and rumination are only going to make you feel worse."
    # Cee vihainen
    show cee vihainen at hop
    C "Ugh. Must you truly act like such a voice of reason?"
    MC "Kind of."  
    show cee perus
    # Cee perus
    C "Fine, I'll remain here and face the consequences. If the land-dwelling masses end up demanding punishment as compensation for my actions, I suppose I shall not plead for impunity."
    MC "That's very mature of you, Cee. However, I'm sure we can talk this out with everyone, no punishment required."
    MC "It's not like we can't fix this place, and I bet most folks understand that you were only trying to make things better."
    MC "Besides, you don't have to do this alone. I'm the one who decided to side with you. Like you said, I'm your partner in crime."
    # Cee smiles
    show cee iloinen
    C "I consider myself quite verbose. However, I'm feeling something rather ineffable right now. I'll leave it up to you to imagine and translate the depths of my soul."
    MC "Don't worry, Cee, I think I have a pretty good idea of how you're feeling." 
    scene bg warehouse with fade:
        zoom 1.0
        yoffset 0
        pause 1
    show cee alakuloinen zorder 3 at middle
    show karkhos perus zorder 2 at cleft with moveinleft
    show agatha vakava zorder 1 at cright with moveinright
    # MC and Cee return to Karkhos and Agatha. Karkhos and Agatha appear
    # Cee alakuloinen
    MC "Our friend Cee here has seen the error in their ways. We'll dry the hallways and get rid of the sand… somehow."
    show karkhos pikkuviha
    K "Um. I'm actually kinda busy right now, so you should probably ask someone else to clean up. Maybe one of the vampires can help, after the water has been drained?"
    show agatha vihainen at hop
    A "Ugh, I'LL do it. Right now, I've got plenty of pent up frustration that needs to be released." 
    MC "After we've cleaned up this place, we have to call for a meeting and discuss how we'll do things from now on. Cee's solution was far from perfect…"
    show agatha vakava at hop
    A "Obviously."
    MC "...but at least they tried to improve this corporation and our working conditions. That's something we all want, right?"
    MC "I'm sure there's something we can do, and we must do it together. No monster left behind."
    show cee perus
    C "I hope we can leave this silly little dispute behind us. It would be foolish to not do so."
    show agatha vihainen at hop
    A "Silly little dispute? You practically tried to drown us all, you-"
    show cee alakuloinen
    MC "Yes, and Cee here is very sorry for their actions. Aren't you, Cee?"
    "Cee looks like they're actually sorry. Good."
    C "Yes, well. I got a little carried away. I'm sorry."
    show karkhos perus at hop
    K "Don't mention it. No hard feelings." 
    show agatha vakava at hop
    A "Apology accepted. Just don't do it again!"
    show cee vihainen at hop
    C "Yes yes, no need to rub it in my face." 
    show bg warehouse with fade
    show cee perus
    "We discuss the clean-up operation."
    "Agatha is full of energy but we agree that she can't take care of everything all by herself."
    "In the end, Cee and Karkhos are willing to help. It feels good to see the three of them getting along again."
    show karkhos iloinen
    K "Y'know, I kinda like how the warehouse looks like a big pool. Should've brought my trusty old swim ring."
    show agatha perus at hop
    A "I suppose I can't ignore the fact that you were trying to make our work environment more pleasant, either. Statistics do show that thriving workers are more productive, after all."
    show cee iloinen
    MC "See, Cee? The others value your input. I'm sure your ideas will be useful when we discuss how to run things here from now on."
    "I look at Cee, Agatha and Karkhos."
    "No more distrust. No more fighting. Landlubbers and sea creatures, trying their best together."
    "As it should be."
    return

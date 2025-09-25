label day3_1A:
    scene bg hallway posters
    "They went to check my records some time ago. This is it."
    "They're coming out!"
    "The suspense is making my digestive region sick."
    # sprites, A happy ja kaks muuta sad
    show karkhos alakuloinen mato zorder 2 at cleft with easeinleft:
        xalign 0.01 xoffset -100
    show cee alakuloinen zorder 1 at cright with easeinright:
        xalign 0.99 xoffset 100
    show agatha iloinen zorder 3 at middle, hop with easeinleft
    A "Well well well. Let's keep this meeting brief. Precious productive hours are wasting."
    A "The warehouse was in tip top shape. Looks like [MC] has shipped an impressive quantity of Loot. That means it's my victory."
    A "That being so, we're going to enact some changes around here."
    show agatha at shake2
    A "From now on, the three of you must do as I say. Per our agreement."
    "She trembles with excitement."
    show karkhos alakuloinen with dissolve
    K "...I'm gonna die."
    show cee alakuloinen at hop
    C "How doth a sailor jump the ship, when the captain has tied him to the mast?"
    # A tosi iloinen
    show agatha tosi iloinen at middle
    A "What's that? Complaining is poison to a positive working environment. So turn that frown upside down."
    show agatha vakava at hop
    A "NOW."
    # cee karmiva hymy ja karkhos vihainen
    show cee karmiva hymy at hop
    show karkhos vihainen at hop
    "Both of them give it a go, but their smiles end up grotesque fakes."
    show agatha at hop
    A "Ever since Boss left on the business trip, we have fallen behind schedule. As if that wasn't enough, we have a large shipment coming in tomorrow."
    show agatha perus
    A "To remedy the situation, I propose overtime. Fairly compensated, of course."
    show karkhos perus
    show cee perus
    K "Compensated how?"
    show agatha iloinen at hop
    A "Great question! Though in the future, please please raise your hand before speaking."
    show agatha tosi iloinen
    A "The compensation will naturally be your own feeling of satisfaction."
    show karkhos pikkuviha at hop
    K "...I refuse."
    show agatha vakava
    A "Ah, more rule breaking. Checks out with your prior record."
    A "Though it's unfortunate, good leadership sometimes requires compromises. Karkhos, if you refuse to pack, go run to the delivery agents. Fresh air and exercise will energize you for our all-nighter."
    show agatha iloinen at hop
    A "Inform the delivery department that we'll be working until morning, so they better do the same."
    K "And if they say no?"
    show agatha tosi iloinen at hop
    A "Tell them it's an emergency."
    show agatha perus
    A "Cee. Fix that leaking hole at your workstation. Your unauthorized equipment modifications end here."
    # cee alakuloinen
    show cee alakuloinen at hop
    C "As you command, oh fearsome overlord."
    show agatha iloinen at hop
    A "After you're done with these personal tasks, return to receive further instructions. Any questions?"
    "And all-nighter? I haven't pulled one of those since school. Maybe it'll be fun, like a sleepover."
    hide karkhos with dissolve
    hide cee with dissolve
    hide agatha with dissolve
    "But as we get back to work, worry gnaws at my gelatin."
    "Was this really the correct choice?"
    scene black with dissolve
    pause 1.5
    #musta ruutu täs välis

label day4_2A:
    #day 4 grafiikka

    #varasto BG
    scene bg warehouse night with dissolve
    pause 1
    "The glowing mushrooms are changing colors from a sleeping state to awake."
    show bg warehouse with dissolve
    "The sounds of hurried footsteps and of boxes filling have not stopped echoing down the dungeon's corridors."
    "My movements have slowed each hour of the all-nighter. I keep dropping Loot, stumbling and scraping, and even mistook a sword for a sausage. Is this what it's like to be undead?"
    "When I saw Cee working, their arms were moving, but there was no light in their eyes. As if the soul had been sucked out."
    "The last I saw Karkhos, he had crawled under the breakroom's table. When I checked if he was asleep, he was staring at a crack in the wall."
    "But the warehouse is nearly empty, and astonishingly well organized. We've accomplished a lot. Though it's been hard."
    #agatha iloinen suukiinni appears
    show agatha iloinen suukiinni at shake2, middle with easeinleft #TODO: jos aikaa, slow ease in?
    "Agatha has trouble flying straight as she approaches."
    show agatha iloinen
    A "Great work out there, MC. Here, some nectar to get the day started."
    show agatha iloinen suukiinni at hop
    "She flings me a bag of nectar. It's the kind she is always sipping. It's very small."
    MC "Thanks. Tastes like the sun."
    show agatha iloinen
    A "Tastes like work well done."
    show agatha perus
    #TODO: footsteps tosi hiljasella
    pause 1
    show agatha iloinen
    A "Oh, that must be the delivery agents with the triple Loot. Be a dear and go tell them where to put everything. Come fetch me when they're done."
    MC "Aye aye, ma'am…"
    scene black with dissolve
    pause 1.0
    scene bg hallway with dissolve
    #musta ruutu, sit käytävä bg
    "Delivery agent" "Huff… A… delivery… for the warehouse."
    "The monster doubles over and pants heavily."
    "Behind, a dozen more delivery monsters slump down and fumble for their waterskins. The carts they were pulling take up the whole corridor, and are overflowing with unsorted Loot."
    "Delivery agent" "Could you finally tell us what the emergency is? Unrest is spreading. We've heard the rumors."
    MC "Wait, what rumors?"
    "Delivery agent"  "That a warband of thousand humans intends to raid the dungeon! Everyone's scared. The fear was the only thing keeping us moving all night."
    "Like a stone pushed downhill, everything's suddenly happening too fast for my tired mind."
    MC "Uh… Leave the unsorted Loot here. We've packed more boxes for delivery."
    "Delivery agent" "Delivery to where? Last I checked, all monsters already had Loot."
    pause 0.5
    MC "...Could you wait a minute? I have to check with someone."
    scene black with dissolve
    pause 1.0
    scene bg warehouse with dissolve
    #musta ruutu, sit varasto
    "What's going on? Agatha said we are behind schedule, but apparently everyone already has Loot?"
    #cee perus
    show cee perus zorder 1 at cright with easeinright:
        xalign 0.99 xoffset 100
    C "You appear dismayed. No wonder."
    MC "Did you know that all monsters already have Loot? Isn't that really amazing?"
    show cee at hop
    C "Ah. Suspect it, I did. It appears our efforts have borne fruit."
    C "And yet, I hear no cheers nor praise, but angry muttering from the entryway."
    show karkhos perus mato zorder 2 at cleft with easeinleft:
        xalign 0.01 xoffset -100
    # Karkhos appears
    "Karkhos comes in from the corridor. He must've been in the breakroom."
    K "Had a chat with the delivery guys. They were pissed. Figures."
    #agatha ilmestyy, vakava
    show agatha vakava zorder 3 at middle with easeinleft
    A "What are you all standing around for? No extra breaks until the warehouse is empty."
    show karkhos at hop
    K "About that. The delivery agents are real cross we lied about that emergency."
    MC "You told them?!"
    show karkhos pikkuviha mato
    K "They asked."
    # agatha vihainen
    show agatha vihainen at hop
    A "No lies were spoken. When monster lives are on the line, every day is an emergency."
    MC "They said all monsters already have Loot."
    #agatha vakava
    show agatha vakava
    A "And we'll send every monster a round of extra. When they use their Loot, they'll have spares immediately at hand. Safety doubled."
    # cee alakuloinen
    show cee alakuloinen
    C "Ah, furnish the nests of little monsters akin to a dragon's hoard. Surely the humans won't…"
    # cee hullu hymy
    show cee hullu hymy at hop
    C "How shall I say this? Won't simply loot the unguarded nests?"
    show agatha vihainen
    A "Nobody asked your opinion."
    # karkhos vihainen
    show karkhos vihainen mato at hop
    K "You won't even let us speak? Here's the facts. Our pace has plummeted. Even yours, Agatha. It's the exhaustion. We should just go home at this point."
    show karkhos pikkuviha mato
    K "In fact, if we go on working, our lives might be in danger."
    show agatha at hop
    A "My pace has NOT plummeted. And little fatigue never killed anyone."
    show karkhos perus mato
    K "Dunno about that. But when I told the delivery guys who's in charge, they started digging through the unsorted Loot for weapons."
    #a pelokas, ja c kauhistus
    show agatha pelokas
    show cee kauhistus
    MC "Weapons?"
    A "You're joking, right?"
    show karkhos pikkuviha mato
    show cee perus
    K "Nah, dead serious. Seems they wanna take revenge on the sorry monster who lied about the emergency. Can't say I blame them."
    # agatha alakuloinen
    show agatha alakuloinen at shake2
    A "R-r-revenge?"
    MC "What's wrong Agatha? Did you drink spoiled nectar?"
    "The faint color on Agatha's face has drained even whiter."
    A "N-n-n-n-"
    MC "No?"
    # Agatha pelokas
    show agatha pelokas at shake
    show karkhos kauhistus mato
    show cee kauhistus
    A "NOOOOOOOOOOOOOO!"
    # agatha pois vauhdikkaasti
    hide agatha with moveouttop
    "A single flap of wings, and she has shot into the depths of the warehouse. I didn't know she could fly that fast."
    show karkhos at hop
    K "Huh? I thought she'd throw a fit, but that didn't seem like anger?"
    MC "Of course not! She's scared."
    show cee at hop
    C "Truly? Of our delivering colleagues? Whatever for?"
    show karkhos perus mato
    show cee perus
    MC "Scared that an angry mob will swat at her with swords, what else? We need to find her."
    MC "Cee and I will start searching. Karkhos, can you go and apologize to the angry mob?"
    show karkhos pikkuviha mato
    K "Ask for a gem from a dragon's hoard while you're at it? Heck. I'll try."
    scene black with dissolve
    pause 1
    #musta ruutu
    "None of us saw where she flew, so we start peeking behind boxes and calling for her. Cee sloshes around a bag of nectar and flashes Agatha's favorite lantern."
    "The shelving wobbles as I climb to the top. It's high enough to make me queasy. In the topmost corner of the warehouse, quiet sniffling betrays Agatha's hiding place."
    show bg warehouse with dissolve
    #    zoom 1.7 xoffset -1300
    # warehouse bg, no sprite
    A "They're going to swat at me…"
    "The sobs are coming from a partially rusted suit of armor. The crying echoes off the metal. I peek inside. "

    #TODO: PLACEHOLDER Tähän valinta lähestyyks varovasti vai ei tms?

    # agatha alakuloinen kyynel
    show agatha alakuloinen kyynel at middle with dissolve
    A "Go away…"
    "Her thick fur has started shedding from stress. Static is making the sheddings stick to the metal armor. Not even her antennae have been spared the patchy balding."
    "Without the thick fur, she looks even smaller."
    MC "Karkhos apologized to the delivery monsters. They've left. It's safe to come out."
    show agatha at shake2
    A "Sword this, axe that, monsters aren't any better than humans."
    show agatha at middle
    A "I'm just doing my best, so how come they want to take revenge on me? The dungeon was supposed to be safe."

    # täs menus ei alt tekstii, pelkät valinnat
    menu:
        "\"Yeah. That wasn't very positive-working-environment of them.\"":
            pass
        "\"Exhaustion makes us do stupid things sometimes.\"":
            pass

    "Agatha peeks at me through the helmet's visor."
    A "It's so unfair. I'm small, so I need to work harder to keep up with the big monsters. If I don't keep up, I'll be thrown back into the Human Wilds."
    MC "Nobody's throwing you out. You're important to the warehouse."
    A "Doesn't feel like it. The moment Boss left, Cee and Karkhos just started lazing around. Nothing I said had any effect."
    A "I had to step up to cover for their negligence, and they haven't even apologized."
    # PLACEHOLDER
    A "They say I'm an unreasonable workaholic. Their words hurt. Hurt as much as being swatted at."
    MC "Let's climb down? I think they should hear this."
    show agatha alakuloinen at hop
    "She wipes her tears and nods."

    #musta ruutu
    scene black with dissolve
    pause 1.0
    scene bg warehouse with dissolve
    "Though the shelves sway as I climb down, I manage to reach the floor without falling."
    # käytävä bg? tai varasto. K ja C spritet
    show cee perus zorder 3 at cleft, hop with dissolve
    C "Pspspspspspsps."
    show karkhos perus mato zorder 2 at cright, hop with dissolve
    # show karkhos at hop
    K "Agatha, please come out!"
    show agatha alakuloinen zorder 1 at middle with dissolve
    show cee at cright with ease:
        xalign 0.99 xoffset 100
    show karkhos at cleft with ease:
        xalign 0.01 xoffset -100
    # A slow fade in
    All "..."
    MC "Krhm. Agatha would like to speak."
    K "Wait. I'll go first."
    show karkhos pikkuviha mato
    K "Look. I can't work any harder than this. It might be easy for you, but not for us."
    show agatha at hop
    A "...It's not easy for me…"
    show cee at hop
    C "?"
    A "I also get tired. And even though I'm small and you're big, I do the exact same work."
    show cee iloinen at hop
    C "Hah, you jest!"
    show cee perus
    C "What you do is on par with a giant. We are unable to emulate that."
    show karkhos alakuloinen mato
    K "Look, I shouldn't have just stopped working. Must've been stressful to you. But you're just too fast. I had …trouble keeping up. Being compared to you made me feel small."
    A "Small?"
    show cee alakuloinen
    C "For a fish on dry land, far from home as I am, your standards were difficult to understand. You were scary."
    # agatha pelokas
    show agatha pelokas
    A "I was SCARY?" 
    show agatha at hop
    A "..."
    show agatha alakuloinen
    A "All this time, I thought I was the only one having problems, since I was the smallest. I guess I never stopped to consider what you two must feel."
    # agatha vakava
    show agatha vakava
    A "To feel small and afraid is an awful thing. I don't wish it on anyone."
    # PLACEHOLDER
    show cee perus
    show karkhos perus mato
    A "Maybe I was unreasonable. It's not good for the Chain to expand too quickly, either. Maybe Boss had our pace all figured out."
    MC "And despite everything, we worked really hard, and sent Loot to every monster. That's worth celebrating."
    show agatha vakava at hop
    show karkhos kauhistus mato at hop
    show cee kauhistus at hop
    MC "You know, if the four of us can't keep up with orders, maybe Boss should hire a fifth monster?"
    # kaikki yllättyny
    show agatha at hop
    A "I hadn't even considered that."
    show agatha perus
    A "Truth be told, it'd be nice to relax once in a while."
    # K ja C tosi iloinen
    show cee tosi iloinen at cright with ease:
        xoffset 0
    show karkhos tosi iloinen mato
    C "Rejoice! The winter has passed!"
    show karkhos tosi iloinen mato at cleft with ease: #TODO: onks tää positio väärä
        xoffset 0
    K "This new Agatha ain't half bad."
    # A vakava
    show agatha vakava at hop
    "The whites of her cheeks are turning redder."
    A "Maybe it's alright to take the afternoon easy. Just this once."
    scene black with dissolve

    # PLACEHOLDER Sit viel suunnilleen samat loppuhöpinät kun muilla reiteillä? (Puuttuu viel niistäkin))



label day3_1B:
    scene bg hallway
    "They went to check my dispatch records some time ago. This is it."
    "They're coming out! The suspense is making my digestive region sick."
    # sprites, karkhos happy ja kaks muuta sad
    show agatha alakuloinen zorder 1 at cleft with moveinleft
    show cee alakuloinen zorder 2 at cright with moveinright
    show karkhos tosi iloinen zorder 3 at middle with moveinleft
    show agatha at hop
    A "We have …a winner…"
    show cee at hop
    C "Fair and square…"
    show karkhos iloinen at hop
    K "Heh. Cheer up, guys. This is only the beginning."
    K "MC. Looks like you have shipped less items than usual. That means I win."
    K "You're living proof that the work's just too hard. Now that you all finally see reason, let's start living like we'll be dead tomorrow."
    MC "What will our demands to Boss be?"
    K "Dunno yet. Those details will sort themselves out."
    show karkhos at hop
    K "Oh, got it! We need something to get the brain juices flowing."
    K "I hear the gargoyles down the river invented a new cocktail. It's got dryad liquor and distilled dire-ant venom. You'll need a stomach of stone for it. I've wanted to try it ever since I died."
    show karkhos tosi iloinen
    K "After that, we can go lava surfing, and…"
    "An image of a cat at a fish market is conjured into my mind's eye."
    "Not so for the other two. It's like everything they believed in has crumbled."
    #A sad sprite
    show agatha pelokas at hop
    A "We haven't even made room for the... Oh, at this rate, we'll all be dead before Boss returns."
    #K happy
    show karkhos iloinen at hop
    K "See, even Agatha is already relaxed enough to be cracking jokes."
    show agatha alakuloinen
    K "I reckon lunch is as good a time to go on a little excursion as any. The Loot orders will start piling up, but that's a positive."
    K "Monsters these days are way too demanding. A few days of delivery delay should be the new normal. It's good to set healthy boundaries in these things."
    show cee perus at hop
    C "Uh. Before we depart, I must-"
    show karkhos perus
    K "No. We're off the clock. Not a single brainwave goes to anything related to the warehouse."
    show cee at hop
    C "None? At all? Are you certain?"
    K "It's called work-life balance."
    show cee hullu hymy
    C "As you demand, oh Karkhos the Great. Your meager servants shall obey and ignore the cries of the innocent, pleading for their life-saving Loot."
    show karkhos vihainen at hop
    show cee kauhistus
    #K angry
    K "Hey, watch out."
    #K happy
    show karkhos tosi iloinen at hop
    show cee alakuloinen
    K "The jokey mood's contagious."
    "Though it's only lunch, we march for the doors. Agatha and Cee give the warehouse one final, longing look."
    hide karkhos with moveoutright
    hide cee with moveoutright
    hide agatha with moveoutright
    "This result… Was it really alright?"
    scene black with fade
    pause 1


label day4_2B:
    #(päivä 4 grafiikka)

    scene black
    #musta ruutu
    "Bleary. Dizzy. I open my eyes after a dreamless black."
    "The only reason I believe it's an hour to noon is because my clock says so. It's like I haven't slept a wink."
    "Ouch… Even my aches have aches. My body's toxin percentage must be very high."
    "We left work after lunch. Though Karkhos is always tired at work, he was practically hopping out the dungeon."
    "He took us to village after village. We drank and tried local dares not even the residents themselves would do."
    "Losing the whole \"who's right and who's wrong\" thing did a number on Cee and Agatha. They went along with Karkhos' whims, though unenthusiastically. I suppose I did, too."
    "Agatha was the first one to wash out. In the goblin village, she bathed in Karkhos' ale mug. After that, she tried to explain flower crossbreeding to us."
    "She started crying uncontrollably, said horticulture is so beautiful, and curled up to sleep on the table."
    "All evening, Cee kept looking at the clock and fidgeting."
    "When we were visiting the salamanders, Cee wanted to try inventing a new drink. They kept the ingredients a secret, but everyone who drank the concoction blacked out. Cee included."
    "Karkhos was in a great mood though. Effortlessly made friends with the gargoyles, goblins and salamanders…"
    "After he'd had enough, Karkhos and I carried the other two back to the caves."
    "A night to remember. I had fun, but can't say I feel more rested. Our demands to the Boss aren't any clearer, either."

    #TODO: walking sound
    #käytävä BG
    scene bg hallway with fade
    "Karkhos told us to not come to the warehouse until noon, and to bring a pillow."
    "Though we had fun, I don't see how a bender like that will help. My idea of \"living like no tomorrow\" would probably be a tasty meal and a vivid sunset."
    "Maybe Karkhos knows what he's doing. Maybe our productivity will be off the charts today. Hopefully not on the low end."
    #TODO: kävely äänii
    "As I approach the warehouse, I hear the commotion of a crowd."
    "A group of delivery agents has gathered in front of the main entrance."
    "Delivery agent" "Hey! Why's the warehouse not giving Loot to deliver?"
    "Delivery agent" "We've got a huge number of deliveries to make. Humans attacked this morning, and many monsters used their Loot."
    "Uh oh." 
    "I apologize and squeeze past. If there's one thing the slimekind are good at, it's this."
    "They grumble, but when I say I only work here, they let me in."

    #TODO: warehouse. Vettä ja roinaa versio.
    scene bg warehouse with dissolve
    "The humidity is so high I could start melting. Waterlogged Loot litters the entryway. There's a smell of rust, and of something rotting."
    #Agatha sprite
    show agatha alakuloinen kyynel zorder 1 at middle with easeinbottom
    "Agatha flutters above the water. I've never seen her this rundown."
    show agatha at hop
    A "I can't do this anymore. Just because this was the majority decision…"
    #TODO: kävely vedessä ääni
    "Cee is crawling through the water that's not deep enough for swimming. They gurgle something in the water. I shake my head."
    # C sprite
    show cee perus zorder 2 at cright with easeinbottom
    show agatha alakuloinen
    "Cee sits up and looks contemplative."
    C "It appears the downsides of a \"work-life balance\" have become apparent."
    MC "You left your weird pump running, didn't you."
    C "Leave it I did, for yesterday, I was ordered to drop everything. Mayhaps I ought to have opposed our new overlord. Alas, I did not."
    C "Absent overlord, I might add."
    show agatha at hop
    A "Where is Karkhos? It's past noon."
    #TODO: footsteps in water approaching. They stop.
    "We all turn. Karkhos has stopped at the entrance. He seems horrified."
    #neutraali ilme, tai sit joku kauhistus?
    show karkhos kauhistus mato zorder 3 at cleft with easeinleft
    K "What's going on…"
    K "There were delivery agents outside. I told them to take the day off, but it just made them angrier."
    K "But this mess… We were only away from one noon to the next!"
    #K angry
    show karkhos vihainen mato at hop
    show cee alakuloinen
    show agatha alakuloinen at shake2 with ease:
        yoffset 30
    K "Cee, what were you thinking? And Agatha, you should have known better!"
    show karkhos at shake
    K "None of this is my fault, right?! It's not my fault Agatha ordered triples, or that Cee wanted to turn this place into an aquarium?! It's not my fault!"
    show karkhos at hop
    "He's getting winded from yelling. He looks at each of us for support. Agatha is so miserable she barely stays in the air. Cee is staring at their hands through the wavering water."
    show karkhos alakuloinen mato
    K "If we'd been here in the evening, we would have noticed the flooding earlier. None of this loot would be ruined."
    show karkhos vihainen mato
    K "Damn it… I should have seen this coming— Gh!"
    show karkhos vihainen mato with ease:
        yoffset 200
    #TODO: onks tää liian goofy
    show agatha pelokas at middle
    show cee kauhistus
    "Karkhos grips his gut and slumps into the water. Brownish blood is oozing through his fingers. The large suture in his abdomen has ripped."
    MC "?!?!"
    show agatha pelokas at hop
    A "Eek!"
    show cee at hop
    C "Fuck!"
    show karkhos pikkuviha mato
    K "Chill, it's cool. Happens all the time. I've got a sewing needle and sinew at my workstation."
    MC "Agatha, go get it!"
    show agatha pelokas at shake
    A "B-b-b-b-blood!"
    hide agatha with easeouttop
    "She flies up to the ceiling and hides behind a stalactite."
    show cee perus at hop
    C "I'll go."
    #TODO: walking (running?) in water sound
    hide cee with easeoutbottom
    pause 1
    show karkhos at hop:
        yoffset 200
    K "My gut always rips when I get too agitated. I've gotten pretty good at sewing thanks to it. Hurts, though."
    MC "Amazing it didn't rip last night."
    show karkhos perus mato
    K "Oh. Now that you say it, that's probably it. All that carousing and drinking must've weakened the stitches."
    #TODO: water footsteps
    show cee perus zorder 2 at cright with moveinbottom
    "Cee has managed to find the sewing supplies. We watch silently, as Karkhos sews his abdomen back shut."
    show cee at middle with ease
    "While he sews, part of the intestine slips out, like a tongue lolling out of a second mouth. Cee helps by shoving it back in."
    "When he's done, Karkhos glances at me wearily."
    show karkhos alakuloinen mato zorder 3 at cleft with ease:
        yoffset 0
    show cee at cright with ease
    K "Should've seen this coming. Some of this mess, at least."
    MC "That makes four of us."
    #Agatha fades in
    show cee perus zorder 2
    show agatha alakuloinen zorder 1 at middle with dissolve
    pause 0.5
    show agatha at hop
    A "...I'm sorry…"
    show karkhos perus mato at hop
    K "Hey, what for?"
    show agatha vakava
    A "...When I lost the vote to you, I started doubting everything I believed in. Is what I have been advocating for really alright? So I stopped thinking and went along with your stupid plan blindly."
    C "I also thought, that though my aims had been clear to me, perhaps I had been looking at the world through dyed water."
    show cee alakuloinen at hop
    show agatha alakuloinen
    C "How could I ever again be certain of anything? So when our new overlord ejected us from labor, I neglected to exercise due caution."
    show karkhos at hop
    show cee perus
    K "Guys…"
    show karkhos alakuloinen mato
    K "Oh man. Yet another thing I've Karkhos the Destroyer'd… It just keeps happening."
    K "Truth is, I didn't get the name because I'm a menace on the battlefield. Got it cuz I always mess things up."
    show agatha vakava at hop
    A "That's awful!"
    show cee kauhistus at hop
    C "You ought not have taken the name if it was slanderous."
    show karkhos pikkuviha mato
    K "If it fits, it sits."
    show agatha alakuloinen
    A "..."
    A "I'm sorry, Karkhos. I was so focused on myself, that I didn't see how much you were struggling. I didn't want to believe you were doing your best."
    show cee perus
    C "It is much the same for me. I apologize."
    show karkhos alakuloinen mato
    K "Nah. I've been the biggest idiot of all."
    K "When I noticed I couldn't keep up with the rest of you, it made me feel weak and useless. Agatha is so small, yet she did double what I did."
    K "I was too afraid to ask for reduced hours without everyone backing me up. Hell, I'd rather have disintegrated than admitted my weakness. So I blamed the work."
    MC "You were so intimidating, that I thought you knew how to stand up for yourself. I never thought..."
    show agatha vakava
    MC "But now that we see what has gone wrong, it's an opportunity to fix things. Nothing irreversible has happened, right?"
    show agatha iloinen suukiinni
    A "Right! Though I might not be ready to work less myself, I will stand behind Karkhos on this."
    show agatha iloinen at hop
    show karkhos perus mato
    A "I will write a persuasive speech to Boss, demanding your hours be reduced, without touching your employment contract. I bet the necromantic contract doesn't care how many hours you work."
    show cee at hop
    show karkhos iloinen mato
    C "Perhaps there is yet more to be done. I shall consult the necromancer. More magical energy might invigorate thine mal maintained cadaver. The kidney and liver had mayhaps a purpose as well."
    show karkhos tosi iloinen mato
    MC "And I'm going to start cleaning up. Lots to be done before Boss returns."

    # PLACEHOLDER tästäki puuttuu viel loppujäähdyttelyt
    return


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

label part_1:

    scene bg black with fade
    show bg_1 at up_pan

    Lars "{i}Discere, cogitare, agere— {/i}the triad of wisdom."

    Lars "\'Learning enriches the mind, and thinking sharpens it, but it is through action that we truly manifest our knowledge and shape our reality.\'"

    Lars narration "You'd think that a merchant guild wouldn't bother creating such a philosophical motto and instead advertise {i}'buy one, get one'{/i} dragon ship seats every holiday season."

    Lars narration "We could even offer complementary earthling-made meals by the human chefs who were transported to our realm upon their death."
    
    show bg_1 at end_pan

    Lars narration "But then again, embarking on artifact hunts and historical expeditions wouldn't make sense if the sole purpose of our guild, {i}'Custodes Sylvae'{/i}, was commerce."
    
    pause 1.0

    show claude serious at right with dissolve
    
    show claude serious at jp

    show lars
    $ claude_name = "Unknown"
    Claude "Who on Divonia is mumbling this loud to themselves early in the morning?"

    show lars
    Claude "I'm losing my beauty sleep over here."
    $ claude_name = "Claude"

    Lars narration "I steal a glance from my perch atop the dragon ship and it looks like one, or should I say, the {i}only{/i} passenger, has woken up in quite a grumpy manner."

    menu:
        " " " "
        "Playfully surprise him":
            $ options["C1"]=1
            jump playfully_surprise_him

        "Resist the urge to surprise him":
            $ options["C1"]=2
            jump resist_the_urge_to_surprise_him


label playfully_surprise_him:

    Lars narration "Something tells me I should surprise him, just to cheer up the mood."

    voice "audio/voice/lars/lars_003_take02.ogg"
    Lars "It's me, Sir Claude. Did you already forget about your comrade after a few hours of sleep?"

    show claude shocked at center:
        linear 0.5 xalign 0.5

    show lars
    Claude "Ah, my dearest Captain [Lars]!"

    show lars
    Claude "How could I ever get that nightingale-like voice of yours out of my head? It's almost like my personal alarm clock!"

    Lars narration "Up for a challenge this early? Typical."

    voice "audio/voice/lars/lars_004_take02.ogg"
    Lars "I'm glad you appreciate my vocal talents. But you know, I can't take all the credit."

    voice "audio/voice/lars/lars_005_take02.ogg"
    Lars "You're the one who inspires me to mumble so loudly during our journeys."

    voice "audio/voice/lars/lars_006_take02.ogg"
    Lars "It's the only way I can drown out your attention-seeking snores."

    show claude smile at center 
    with dissolve
    show lars
    Claude "You always find a way to turn the tables, don't you?"

    show lars
    Claude "Although..."

    show lars
    Claude "I can unfailingly capture your attention through {i}other{/i} means, if I choose to."

    jump C_1_End

label resist_the_urge_to_surprise_him:

    Lars narration "It's best that I focus on piloting our dragon first. Otherwise, I'll never hear the end of it."

    voice "audio/voice/lars/lars_007_take02.ogg"
    show lars
    Lars "Good morning to you too, Sir Claude."

    show claude shocked at center 
    with dissolve
    show lars
    Claude "What a boring reaction. I expected more spunk from you..."
   
    voice "audio/voice/lars/lars_008_take02.ogg"
    show lars serious
    Lars "Nevermind then. Hmph!"

label C_1_End:

    show claude at center
    with dissolve
    Lars narration "It's truly a wonder how he managed to stay asleep throughout our entire journey, considering the lack of proper seat arrangements or resting areas on our new dragon ship."

    Lars narration "However, Sir Claude has always been notorious for his resourcefulness in such moments, owing to his history of travels and adventurous ordeals, despite his {i}comfortable{/i} upbringings."

    voice "audio/voice/lars/lars_009_take01.ogg"
    show lars
    Lars "I will return to my duties, then, Sir—"

    show lars
    show claude shocked at center
    with dissolve
    Claude "Didn't I already tell you to drop the {i}'Sir'{/i} for the umpteenth time, Captain?"
    
    voice "audio/voice/lars/lars_010_take01.ogg"
    show lars serious
    Lars "Do we have to go over this cliche back and forth as well?"

    voice "audio/voice/lars/lars_011_take02.ogg"
    show lars serious
    Lars "I promised I'd do it if you stopped insisting on {i}Captain{/i} this and {i}Captain{/i} that."

    show claude blush at center
    with dissolve
    show lars serious
    Claude "It makes us seem more of an adventurous pair, though, don't you think so?"

    Lars narration "Indeed, my knack in piloting and his remarkable merchant acumen just clicked, though I wouldn't admit that outloud."

    Lars narration "Whether it was going on expeditions, dealing in trades, or connecting with the quirky passengers we often had..."

    Lars narration "We always made an efficient team. Maybe even the best among all the guild members."

    show lars
    show claude smile with dissolve
    show claude smile at jp
    Claude "Now that I think about it, what were you talking to yourself about?"

    show lars
    Claude "Confiding trade-secrets to our dragon, Spotsy? Or maybe secretly practicing a secret confession for {i}me—{/i}"

    voice "audio/voice/lars/lars_012_take01.ogg"
    show lars serious
    Lars "She doesn't even have any spots. You're bad at naming as always, Sir-"

    show claude serious with dissolve
    Lars narration "He lets out an intrusive cough."

    voice "audio/voice/lars/lars_013_take02.ogg"
    show lars
    show claude smile with dissolve
    Lars "-Claude. Not to mention, the confession jokes won't work if you keep repeating them over and over again."

    show claude shocked at center 
    with dissolve
    show lars
    Claude "Who knows, maybe one day, I'll surprise you with a confession that will leave you speechless."

    Lars narration "Once he begins, there's no stopping his relentless flirting. Might as well shift my focus to something else...like our very new dragon!"

    hide claude
    show spotsy
    with dissolve
    Lars narration "I reach out, my hand confidently caressing the head of our newest guild member who I hope I'm taking good care of."

    Lars narration "Her eyes meet mine in and in a show of trust, her scale's part open, revealing mesmerizing roseate flames simmering underneath."

    show lars
    Claude "Don't let your attention wander off too much, Captain."

    Lars narration "Sir Claude's voice carries a subtle touch of displeasure as he observes me caressing Spotsy's head."

    Lars narration "Maybe the uncomfortable seating arrangement is getting to him."

    show smoke
    show lars
    Claude "You can spare the royal treatment. She's just a glorified lizard that could use a few mint leaves."

    Lars narration "As if to express her annoyance, Spotsy lets out a flushed, puffy plume of smoke from her nostrils. A low rumbling note resonates from her throat, a clear indication of her irritation."

    hide smoke
    hide spotsy
    show claude at center 
    with dissolve

    voice "audio/voice/lars/lars_014_take01.ogg"
    show lars serious
    Lars "You're starting to irritate her, Sir-"
    
    show claude serious with dissolve
    Lars narration "Another intrusive cough."

    voice "audio/voice/lars/lars_015_take02.ogg"
    show claude smile with dissolve
    show lars serious
    Lars "-Claude, I think you should stop."

    show lars serious
    Claude "She doesn't like it, hmm...that just makes me want to do it even more though."
    
    show lars serious
    show claude serious with dissolve
    show claude serious at jp
    Claude "Stealing Captain's attention away from me and not facing any consequences? Not on my watch."
    
    show claude shocked with dissolve
    show lars serious
    Claude "I could also argue that I don't want to end up as some unfortunate passenger who prematurely expires and transports to the Earthly realm just because you were adoring our newest dragon ship."
    
    show lars serious
    Claude "There have been one too many incidents like that lately."

    Lars narration "His sudden change of topic leaves me slightly bewildered. I withdraw my hand from Spotsy's head, and she shakes her head as if still searching for my comforting touch."

    show claude smile with dissolve
    Lars narration "In contrast, a mischievous grin adorns Sir Claude's face."

    Lars narration "Maybe the problem wasn't the seats after all..."

    voice "audio/voice/lars/lars_016_take02.ogg"
    show claude with dissolve
    show lars sad
    Lars "The numbers of transported humans have certainly increased quite a bit these days."

    voice "audio/voice/lars/lars_017_take02.ogg"
    show lars sad
    Lars "Even still, they are a precious rarity. In all my years of flying travelers across the lands of Divonia, I have only ever met a handful of them."

    show lars sad
    Claude "Not many would want to undertake the journey of transitioning to a new realm they know nothing about, after all."

    voice "audio/voice/lars/lars_018_take01.ogg"
    show claude smile with dissolve
    show lars 
    Lars "I understand that, but they always fascinate me with the tales of their past life."
    
    voice "audio/voice/lars/lars_019_take01.ogg"
    Lars "All our guild members were born and raised here, so I don't have the chance to closely work with one of those travelers either."

    show claude shocked with dissolve
    show lars
    Claude "Tsk, tsk, already thinking of replacing me with someone else, are you, Captain?"

    voice "audio/voice/lars/lars_020_take01.ogg"
    Lars "You said it yourself, one has to admire their bravery. Since descending into Divonia is a grand leap of faith into the unknown."

    show claude smile with dissolve
    Lars narration "A muffled chuckle escapes him."

    Lars narration "Sir Claude has always been the most spirited member in our guild when faced with adversity."

    Lars narration "Must feel great to not have any worries and be nonchalant about everything."

    show claude sad with dissolve 
    show lars
    Claude "Ah, how gladly I would take their place if I could..."

    show lars 
    Claude "Life can get pretty boring when you have everything you need in the palm of your hand."

    show claude smile with dissolve
    Lars narration "Always trying to satisfy his thirst for adventure...but that's part of his charm, I suppose."

    Lars narration "I could hardly recall a day when Sir Claude didn't turn a simple task into a grand quest. He always was, and still is, on the lookout for opportunities to embark on new escapades."

    show claude smile at center
    with dissolve
    show lars
    Claude "I'd advise you to concentrate on steering our ship for now, Captain, before you get even more distracted. Your gaze is practically burning my scales."

    voice "audio/voice/lars/lars_022_take.ogg"
    hide claude with dissolve
    show claude_lars_banter with dissolve
    show lars narration
    Lars "Oh, don't flatter yourself, your scales are nothing compared to Spotsy's."

    show lars narration
    Claude "Well, I suppose it's my mistake for trying to catch the attention of a certain dragon-obsessed pilot. What will become of my grandiose confession now?"

    voice "audio/voice/lars/lars_023_take02.ogg"
    show lars narration
    Lars "Don't be so hard on yourself, Sir Claude!"

    voice "audio/voice/lars/lars_024_take01.ogg"
    show lars narration
    Lars "You know I appreciate you for more than your appearance, even if I rank you below Spotsy. Stopping the confession jokes could help though—"
    
    hide claude_lars_banter with dissolve
    show claude serious with dissolve

    show lars
    Claude "No need for the empty flattery."
    
    show lars
    Claude "I've had my fill of it thanks to a {i}certain{/i} family name."
    
    show claude smile with dissolve
    show lars
    Claude "However, you need to make sure to take care of her well since I did make quite the effort for her exchange."

    Lars narration "As is his custom, Sir Claude deftly redirects the conversation whenever his family is brought up."

    Lars narration "I used to wonder if he was doing so to maintain his privacy as a renowned heir with a diamond spoon, but despite the many years we spent together as partners, the sentiment never changed."

    Lars narration "What effort could he be talking about? The person we negotiated with today eagerly handed over all his prized possessions the moment he heard the {i}'Dupont'{/i} surname."

    show claude
    Lars "It was hardly a fair exchange."
    
    show lars
    show claude sad
    Claude "Well, that's the con of having an outrageously high-class family name like mine, I suppose. Makes one's trade prone to being {i}disgustingly{/i} easy."

    voice "audio/voice/lars/lars_027_take02.ogg"
    show lars serious
    Lars "And let's not forget about that one specific artifact. They were so adamant to wash their hands of it."

    show claude shocked at center
    show lars
    Claude "I'm not one to accept gifts without scrutiny. But there was something about it that piqued my interest. You'll have a better idea once you take a look at it yourself."

    hide claude with dissolve
    show lars_stuck with dissolve

    Lars narration "Question is, what if it turns out to be hazardous or a curse?"
    
    voice "audio/voice/lars/lars_028_take.ogg"
    show lars narration
    Lars "Scrutiny would have been welcomed."
    
    show lars narration
    Claude "I was planning to spice things up a bit, so why not embrace the opportunity of a possible adventure?"

    Lars narration "Right...because who wouldn't jump at the chance to receive an artifact with no known origins, suddenly materializing out of thin air, and with no apparent acquisition date?"

    hide lars_stuck with dissolve
    
    show claude serious at center
    with dissolve
    show lars
    Claude "Captain, your facial expression is practically giving a masterclass in sarcasm. Might want to hide it under a thin layer of worry or, Divs forbid, {i}concern{/i} for your partner."

    menu:
        " " " "
        "Apologize for teasing him":
            $ options["C2"]=1
            jump apologize_for_teasing_him

        "Continue teasing him even more":
            $ options["C2"]=2
            jump continue_teasing_him_even_more


label apologize_for_teasing_him:

    voice "audio/voice/lars/lars_030_take01.ogg"
    show claude shocked with dissolve 
    Lars "I apologize, Sir Claude. You know I have no ill intentions."

    show lars 
    Claude "Oh, how it pains me to witness my most faithful, loyal, and devoted companion trying to replace me with some unknown human whilst {i}MOCKING{/i} my skills..."

    show lars 
    Claude "My scales are going to shed off from the misery of it all."

    voice "audio/voice/lars/lars_030_take02.ogg"
    Lars "Come on, Sir Claude. Don't be so dramatic. You know I'm only teasing you as payback."

    show lars
    Claude "I am baffled, dumbfounded, bamboozled, shocked, bewildered, and confuzzled to the highest degree."

    show lars
    Claude "Well, witnessing your adorable desperation has sparked a generous mood in me. Go ahead, demonstrate just how indispensable I am to you."
    
    voice "audio/voice/lars/lars_032_take01.ogg"
    Lars "Then...how should I show it to you?"

    show claude smile with dissolve 
    show lars
    Claude "There's something that I {i}really{/i} want but with our relationship as is, you won't be able to give it to me, it's a very precious gift so to speak"

    show claude
    Lars narration "My fur prickles with anticipation. I can sense my ears perking up, betraying my keen interest in his next words and what he could possibly want from me."

    voice "audio/voice/lars/lars_033_take02.ogg"
    show lars
    Lars "A gift? For you? But you already have everything you need."

    Lars narration "His family has his pockets lined with all the gold and treasures imaginable too, so I can't see what he'd want from someone of my caliber. The best I can offer him is a handful of dragon treats."

    show claude with dissolve 
    show lars
    Claude "Haha, I'll tell you more about it in due time."

    jump C_2_End
    return

label continue_teasing_him_even_more:

    show lars
    Lars "The infamous Claude {i}Dupont{/i}, not checking the items he negotiates for?"

    show claude shocked with dissolve
    show lars
    Claude "Please, [Lars], you should know better than blabbering {i}Dupont{/i} recklessly."

    voice "audio/voice/lars/lars_036_take01.ogg"
    show lars serious
    Lars "Weren't you going to stop calling me {i}Captain{/i} as well? Or are you going to change the topic again?"

    show bg_1:
        subpixel True
        linear 2.0 blur 10
    show claude smile at center:
        parallel:
            linear 1.0 yalign -0.1
        parallel:
            linear 3.0 zoom 1.50

    Lars narration "Leaning close, his fingertips gently brush against my cheek, leaving a trail of warmth. Golden eyes lock onto mine with unwavering intensity."

    Lars narration "As his lips draw near my ear, his voice deepens, resonating with a seductive allure that sends shivers down my spine."
    
    show claude smile with dissolve
    show lars blush
    Claude "See? I used your name, so you have to call me by mine too...{i}without{/i} the tiring title."

    show claude blush with dissolve
    show lars blush
    Claude "I prefer it when you say my name after all. It's one of the tiny joys of my life."

    show bg_1:
        linear 2.0 blur 0
    show claude smile at center:
        parallel:
            linear 2.0 zoom 1.0
        parallel:
            linear 1.0 yalign 0.5
            linear 1.0 ypos 0.5
    
    Lars narration "The sudden remark takes me by surprise, even though it's not the first time I've heard Sir Claude make such a comment. After all, he possesses a captivatingly flirtatious nature, effortlessly weaving his charm into every interaction."

    voice "audio/voice/lars/lars_037_take01.ogg"
    show lars blush
    Lars "W-w-what are you saying all of a sudden?! Did you lose your mind?"
    
    show claude smile at jp
    show lars blush
    Claude "Awe, is our Captain getting shy all of a sudden? Did you know your ears get red when you're embarrassed?"
    
    Lars narration "With little time to question his truthfulness, I instinctively place my hands on my ears, hoping to shield any trace of vulnerability that might betray my reaction to his words."

    show claude blush with dissolve
    show lars blush
    Lars "I am a dragon pilot, an unwavering force soaring through the skies."

    show lars blush
    Claude "Yes, indeed. That much is observable."

    Lars "My years of experience have honed my resilience and steeled my resolve. I cannot allow myself to be easily affected by the whimsical words of Sir Claude, no matter how charismatic he may be!"

    show lars blush
    Claude "Awe, did I get under your skin, Captain? So much that you had to switch to third-person commentary?"

    Lars narration "Sir Claude remains unfazed by my momentary embarrassment except for a triumphant smile."

    show lars blush
    Lars "He's only joking to gauge my reaction—"

    show claude blush at jp
    show lars blush
    Claude "Haha, look at you. Navigating the skies like a pro with those sharp fox eyes, yet somehow missing the obvious right in front of you."

    show lars
    Lars "Pardon?"

label C_2_End:

    show claude smile
    show lars
    Claude "Let's save this conversation for later, shall we?"

    show claude
    show lars
    Claude "Our {i}dearest{/i} Guild Master is signaling our landing spot."

    hide claude with dissolve

    Lars narration "I glance downward, and our destination near the sea comes into view."

    $ renpy.choice_for_skipping()

    play music "track_2_field_of_flowers.ogg" fadeout 2.0 fadein 2.0
    
    scene bg black with fade
    show bg_2 at pan

    Lars narration "Like an artist painting delicate strokes on a canvas, Master Sylvian has already lined up the location with an array of enchanting flowers."

    Lars narration "Each bloom carefully chosen to mark our path with a vibrant array of sunflowers and roses. Their vivid colors stand out, captivating the eye and creating a striking contrast against the backdrop of the serene oceanic landscape."

    Lars narration "The gentle breeze carries the sweet fragrance of the flowers, adding to the enchanting ambiance"
    
    show bg_2 at end_pan

    show lars
    Lars "Ah, we arrived so early. I have to reward Spotsy well when we get back."

    show claude smile at center
    with dissolve
    show lars
    Claude "I'd be inclined to say that you didn't manage to tap into our dragon's full potential Captain. Owning up to how I stole your attention for more than half, {i}or better yet{/i}, the entire ride."

    show lars
    Claude "However, since you managed to get us here without any dangerous maneuvers, I'll let you to be the first person to touch our newest artifact."

    show lars
    Claude "I tend to appreciate and reward my companions well, especially if they're my {i}lover—{/i}"

    show lars serious
    Lars "Being the first person to touch a suspicious artifact is the last thing I'd prefer to do."

    show lars serious
    Claude "It's the first time it's made its way to our side of the realm, hence the occasion is quite momentous."

    show lars serious
    Claude "You could say the thrill is {i}irresistible.{/i}"

    Lars narration "He locks eyes with me, and I can't help feeling a tad self-conscious under the weight of his declaration, whether it was actually meant for me or not."

    show claude at jp
    show lars
    Claude "Let's not forget, the true essence of a discovery is experienced by the first person who ascertains it and not those who come later. Be it the second or the last to follow."

    show lars
    Claude "If you don't seize this moment now, who knows when you'll get another chance like this? It will certainly be a captivating story to delight your future passengers."

    show lars
    Lars "Fine! Now let me focus before any of us plummet to their death."

    Lars narration "As the sole passengers aboard the dragon ship, guiding Spotsy in her safe descent was a seamless task."

    Lars narration "The proximity to the water offers a perfect opportunity for her to release some pent-up energy too."

    Lars narration "Hopefully, she's not too tired from the journey. I'd hate to burn her out from the get-go. First impressions matter for dragons as well, especially when it concerns their pilots"

    Lars narration "However, once we disembark, our attention turns to the tall and slender magician making his way towards us."

    show claude at center_2left with move
    show sylvian at center_3right with move:
        xpos 1.2
        linear 2.0 xalign 0.85
    
    Lars narration "A warm smile graces his lips, accompanied by the graceful flutter of his obsidian wings."

    Lars narration "With a hushed incantation, the brim of his hat blossoms into a vibrant tapestry of roses and sunflowers, their delicate petals unfurling in a mesmerizing display. The air is instantly infused with their soft fragrance, which mingles with a refreshment spell."

    voice "audio/voice/sylvian/sylvian_001_take02.ogg"
    $ sylvian_name = "Unknown"
    show lars
    Sylvian "Welcome back, dear members of {i}Custodes Sylvae{/i}. I'm happy to see that you both landed safely."

    voice "audio/voice/sylvian/sylvian_002_take03.ogg"
    show sylvian blush
    show lars
    Sylvian "[Lars], your piloting was truly magnificent as always. It's a sight that I'm honored to witness every time."
    $ sylvian_name = "Sylvian"

    show claude serious
    show sylvian serious funny
    with dissolve
    show lars
    Claude "Feel free to skip the cliché warm welcome, Boss Sylvian."

    voice "audio/voice/lars/lars_042_take01.ogg"
    show lars serious
    Lars "Sir Claude!"
    
    show lars serious
    Claude "I know you're probably itching to have [Lars] by your side, but—"

    voice "audio/voice/lars/lars_043_take01.ogg"
    show lars serious
    Lars "That's enough! You can't talk to our mentor that way."
    
    show lars serious
    Claude "Tsk, butter him up more, will you?"

    voice "audio/voice/sylvian/sylvian_003_take01.ogg"
    show sylvian with dissolve
    show lars
    Sylvian "Nevermind him [Lars]. It's best to let the spotlight find its own stage rather than chasing after it."

    voice "audio/voice/lars/lars_044_take02.ogg"
    Lars "Thank you, Master. I wish you could have joined us on the ride too. Sir Claude here almost caused us to plummet to our doom...multiple times I must say."

    show claude shocked with dissolve
    show lars
    Claude "Eh, I did promise to reward you later, didn't I? Drum roll please ~"

    play sound sfx_drum_roll loop fadein 2.0
    Lars narration "Tension fills the air as the anticipation builds up, drawing everyone's attention. Then, in a dramatic display, he spreads his arms wide, showcasing a grand reveal which is..."

    stop sound fadeout 2.0
    Lars narration "...nothing?"

    show claude shocked at jp
    show lars
    Claude "Haha, I seem to have left it on the ship."

    voice "audio/voice/lars/lars_045_take01.ogg"
    show lars
    Lars "Should I go get it, then?"

    show claude smile with dissolve
    show lars
    Claude "No need, my dear Captain. Boss Sylvian can handle it just fine. You and I have been quite busy, and the artifact box is heavy enough to demand a touch of fresh energy."

    voice "audio/voice/lars/lars_046_take01.ogg"
    show lars serious
    Lars serious "We can't ask that from our senior, Sir Claude! Especially when I'm perfectly capable—"

    voice "audio/voice/sylvian/sylvian_004_take01.ogg"
    show lars serious
    show sylvian sad
    Sylvian "Aren't you tired from guiding our new dragon, [Lars]? I could easily fly and grab it for you. It's no trouble at all."

    menu:
        " " " "
        "Ask Master Sylvian to grab the cargo for you":
            $ options["CS1"]=1
            jump ask_Sylvian_grab_cargo

        "Tell Sir Claude to grab the cargo himself":
            $ options["CS1"]=2
            jump tell_Claude_grab_cargo


label ask_Sylvian_grab_cargo:

    voice "audio/voice/lars/lars_047_take01.ogg"
    show lars
    Lars "Would that be alright with you Master? I'd like to spend some time with Sir Claude."

    voice "audio/voice/sylvian/005_take03.ogg"
    show lars
    Sylvian "I respect your choice [Lars], even though—"

    voice "audio/voice/sylvian/sylvian_006_take02.ogg"
    show lars
    Sylvian "{size=*0.75}I also wanted to spend some time with you..."

    voice "audio/voice/sylvian/sylvian_007_take02.ogg"
    show lars
    Sylvian "But uhm, never mind, I suggested it in the first place after all."

    show lars
    show claude smile with dissolve
    show claude smile at jp
    Claude "Awe, you chose to stay with me instead of Boss Sylvian. I'm touched, Captain."

    show lars
    Claude "I'll have to give you a special reward later {i}in private{/i}."

    hide lars
    hide sylvian with dissolve
    
    show bg_2:
        linear 3.0 blur 10
    show claude smile at center with move:
        linear 1.0
        parallel:
            linear 1.0 yalign -0.1
        parallel:
            linear 3.0 zoom 1.50

    Lars narration "His hands gently encircle my waist, drawing me closer to him as he whispers the last part of his sentence."

    Lars narration "His eyes, akin to pools of molten sunlight, meet mine and a mischievous spark dances within them."

    Lars narration "While I usually dismiss this as him being more touchy-feely than usual, his last comment makes me think otherwise."

    Lars narration "Not to mention, beneath his playfulness, there lurked a subtle undertone of his usual competitive spirit. As if he and Master shared a friendly rivalry, each vying to outdo the other in their unique way."

    voice "audio/voice/sylvian/sylvian_008_take01.ogg"
    show lars blush
    Sylvian "Ahem!"
    
    show bg_2:
        parallel:
            linear 1.0 blur 0
        parallel:
            linear 1.0 zoom 1.0
    
    show claude serious at center:
        parallel:
            linear 1.0 yalign -0.1
        parallel:
            linear 1.0 zoom 1.0
    
    show lars
    Claude "Really appreciate you cutting in {i}Boss{/i}."
    
    show claude serious at center_2left with move
    show sylvian mad at center_3right with dissolve
    
    voice "audio/voice/sylvian/sylvian_009_take03.ogg"
    show lars
    Sylvian "Not to interrupt but I'm sure Rory will arrive soon, so it's best to prepare yourself, [Lars]."

    voice "audio/voice/sylvian/sylvian_010_take01.ogg"
    show lars
    show sylvian serious funny with dissolve
    Sylvian "As for you, Claude, remember what I said about teasing him too much?"

    show lars
    Claude "Before worrying about Captain over here, you should head on to where our new dragon is resting, Boss."

    show lars
    Claude "We wouldn't want her to accidentally drop our cargo to the depths of the sea."

    show lars
    show sylvian sad with dissolve
    Sylvian "..."

    hide sylvian sad with dissolve
    
    Lars narration "Master Sylvian, without uttering another word, gracefully takes flight, his wings resembling those of a majestic black swan. Each feather ruffles in the breeze, catching and refracting slivers of sunlight, creating a mesmerizing shimmer which I didn't know was possible."
    
    show rory at center_2right with moveinright
    
    Lars narration "However, a familiar voice rings in the air before I can observe any further."

    $ rory_name = "Unknown"
    voice "audio/voice/rory/rory_001_take02.ogg"
    show lars
    Rory "{bt}Clauuuuuuuuuuuuudy~{/bt}"
    $ rory_name = "Rory"
    
    show claude smile at center_3left with move

    show lars
    Claude "{bt}Roryyyyyyyyyyyyy~{/bt}"

    Lars narration "A figure emerges from where Master Sylvian stood just a few seconds ago, and to my pleasant surprise, it is none other than my childhood best friend. "

    voice "audio/voice/rory/rory_002_take01.ogg"
    show rory angry with dissolve
    show lars 
    Rory "I believe I mentioned that if I ever catch you bossing [Lars] around, I'd pluck out your lizard eyes to adorn my newest puppet, Agatha."

    show rory angry at jp
    voice "audio/voice/rory/rory_003_take01.ogg"
    show lars 
    Rory "You should know that my threats work quite effectively, especially with how Brittina's dress is bedazzled with the scales you've kindly donated...in your sleep, of course."

    Lars narration "True to her lineage as a bull descendent, Rory possesses a fiery temperament and is quick to charge at those who annoy her."

    Lars narration "Her family, the Kyoko blacksmiths, and the Dupont merchants have been locked in a spirited rivalry for generations. Both families have passed down their competitive natures to their heirs, adding fuel to the fire."

    Lars narration "However, Rory was an exception to the traditional path of the Kyoko family. While blacksmithing was the cornerstone of their legacy, Rory's talents lay elsewhere. She found her passion in puppet shows and other forms of artistic expression."

    show rory with dissolve
    show rory at jp
    voice "audio/voice/rory/rory_004_take01.ogg"
    show lars happy
    Rory "[Lars], you're here too. Awe, I missed you so much!"

    voice "audio/voice/lars/lars_049_take01.ogg"
    show lars happy
    Lars "Rory, it's so nice to see you again. I missed you too. "

    show lars happy
    show claude shocked with dissolve
    Claude "Look at our hot-tempered bull, breathing fire as soon as she lays eyes on me."

    show lars happy
    Claude "It's a pleasure to see you again, little Rory. Or should I say, {i}a curse to behold?{/i}"

    voice "audio/voice/lars/lars_050_take01.ogg"
    show lars serious
    Lars "Guys, stop bickering like two little 'little Rory' in the first place— whether it was the height difference or the perpetual little sibling energy between them." 

    Lars narration "Fortunately, Rory never failed to deliver in comebacks, though hers always carried a more imaginative flair."

    show rory angry with dissolve
    voice "audio/voice/rory/rory_005_take03.ogg"
    show lars serious
    Rory "It's just RORY! Call me 'little' one more time, and you'll find more of your receding hairline gracing puppet Alex..."

    show lars serious
    Claude "Now, now, I would have to say these finely braided silver strands that I've so {i}kindly donated{/i} to you are what's bringing half the revenue for your puppet shows, aren't they little Rory?"

    show rory angry at jp
    voice "audio/voice/rory/rory_006_take02.ogg"
    show lars serious
    Rory "You really have the gall to talk to me like that, when all of your travel funds are conveniently collected from my shows?!"

    voice "audio/voice/rory/rory_007_take02.ogg"
    show claude smile with dissolve
    show lars serious
    Rory "Such audacity doesn't appear out of nowhere unless the heat has really gotten to your head."

    voice "audio/voice/rory/rory_008_take02.ogg"
    show lars serious
    Rory "How about a calming dip in the sea to cool off a bit? I could  help you out with a gentle push~"

    voice "audio/voice/lars/lars_051_take02.ogg"
    show lars sad
    Lars "How about we all cool down for a sec—"

    show rory with dissolve
    show lars sad
    Claude "I'm sure the hydro dragons would be delighted to have me amongst them."

    voice "audio/voice/rory/rory_009_take01.ogg"
    show lars sad
    Rory "Hmph, you could put your merchant skills to use there, too. Ten more seconds to live for a platter of rotten lizard meat."

    voice "audio/voice/sylvian/sylvian_021_take02.ogg"
    show claude
    show lars sad
    Sylvian "{size=*1.25}I'm back with the cargo!" with vpunch

    show claude at center_1left
    show rory at center_left
    with move
    show sylvian at right with moveinright

    Lars narration "Thankfully, Master Sylvian swiftly intervenes, diffusing the tension with his timely return. It's always a relief when he steps in; the two never listen to me when they start arguing, but his authority commands attention."

    hide sylvian
    hide claude
    hide rory
    with dissolve
    show box with dissolve
    Lars narration "The weight of anticipation fills the air, drawing all eyes toward the mysterious object, and momentarily, the conflict is forgotten."

    jump CS_1_End

label tell_Claude_grab_cargo:

    voice "audio/voice/lars/lars_048_take01.ogg"
    show sylvian with dissolve
    show lars
    Lars "Sir Claude, can you bring the artifact yourself? I'd like to spend some time with Master Sylvian."

    show claude shocked with dissolve
    show claude shocked at jp
    show lars
    Claude "I'm shocked, Captain. Choosing Boss Sylvian over me?! I wouldn't have imagined."
    
    show lars
    Claude "You even ignored my request about dropping the {i}Sir{/i} part."

    voice "audio/voice/sylvian/sylvian_011_take01.ogg"
    show sylvian blush with dissolve
    show lars
    Sylvian "I am grateful that you wish to share your time with me, [Lars], even if you're tired from your journey."

    voice "audio/voice/sylvian/sylvian_012_take02.ogg"
    show sylvian with dissolve
    show lars
    Sylvian "Rory will arrive soon as well, so we all can spend some time together."

    Lars narration "Master Sylvian gently touches the brim of his hat and a magnificent bouquet blooms forth."

    hide sylvian
    hide claude
    with dissolve

    show sylvian_bouquet
    with dissolve
    Lars narration "Sunflowers rise proudly, while lavender blossoms intertwine. Brilliant clusters of marigolds sprout forth as well."

    Lars narration "I remember that his hat was one of his personal crafts, a magical creation that bloomed flowers according to his mood."

    Lars narration "It's unfortunate that I'm not well-versed in flower languages; otherwise, I would be able to decipher the heartfelt messages he wishes to convey through these enchanting floral gifts."

    Lars narration "Nonetheless, I can't help but feel treasured whenever he gives me gifts. After all, I've noticed that he hasn't given this kind of gift to anyone else, and the thought warms my heart for some reason..."

    hide sylvian_bouquet
    show claude serious at center_2left
    show sylvian at center_3right
    with dissolve
    
    show lars
    Claude "Quite the showmanship, Boss."

    show lars
    Claude "Though I wonder if Captain over here got the message in your {i}subtle{/i} gesture."

    show sylvian blush
    Lars narration "Without regarding his comment, Master Sylvian comes closer and presents me with the bouquet, throwing a smile at Sir Claude who promptly leaves with his back towards us."

    hide claude with dissolve
    show bg_2:
        xalign 0.5
        yalign 0.5
        parallel:
            linear 2.0 blur 15
        parallel:
            linear 2.0 zoom 1.2
    
    show sylvian blush at center with move
    show sylvian blush:
        parallel:
            linear 1.0 yalign 0.2
        parallel:
            linear 3.0 zoom 1.50
    
    voice "audio/voice/sylvian/sylvian_013_take04.ogg"
    show lars blush
    Sylvian "These are for you [Lars], I hope you like them. They may not resemble your brilliance the way they should."

    voice "audio/voice/sylvian/sylvian_014_take01.ogg"
    show lars blush
    Sylvian "Even still, flowers are the silent poets of our emotions, conveying in colors and scents what words...often struggle to express."

    voice "audio/voice/lars/lars_052_take02.ogg"
    show lars blush
    Lars "Thank you, Master. Though I'm a bit uncertain about the sudden gesture, I appreciate it nonetheless."

    voice "audio/voice/sylvian/sylvian_015_take01.ogg"
    show lars blush
    Sylvian "That's more than enough for me."

    show bg_2:
        parallel:
            linear 2.0 blur 0
        parallel:
            linear 2.0 zoom 1.0
    show sylvian:
        parallel:
            linear 1.0 yalign -0.1
        parallel:
            linear 1.0 zoom 1.0

    voice "audio/voice/sylvian/sylvian_016_take04.ogg"
    show lars
    Sylvian "Moving on, it might be best for you to take care of your task, Claude."

    show sylvian:
        zoom 1.0
    show sylvian at center_2right with move
    show claude serious at center_2left with dissolve

    show lars serious
    Claude "So glad that nauseating scene was over."

    voice "audio/voice/sylvian/sylvian_017_take02.ogg"
    show sylvian serious funny with dissolve
    show lars serious
    Sylvian "Be careful with your words Claude."

    show lars serious
    Claude "Mhm, sure sure."

    voice "audio/voice/sylvian/sylvian_018_take02.ogg"
    show lars serious
    Sylvian "Better yet, I believe it's best for you to leave for the moment. We're still not sure of the origins of the artifact you brought and there needs to be a level of caution involved as well."

    voice "audio/voice/lars/lars_053_take01.ogg"
    show lars
    Lars "That's exactly what I said!"

    show lars
    Claude "Hmph..."
   
    hide lars
    hide claude serious with dissolve

    show sylvian at center_3right with move
    Lars narration "As Sir Claude takes his leave, his silver lizard tail gracefully sways behind him, reminiscent of the rhythmic movements of the sea. His scales, resembling those of the majestic dragons I often encounter in my journeys, captivate my gaze with their intricate detailing, despite their diminutive size."

    show rory at center_2left with moveinleft
    Lars narration "However, a familiar voice rings in the air before I can observe any further."

    voice "audio/voice/rory/rory_004_take01.ogg"
    show lars happy
    Rory "[Lars]! Awe, I missed you so much."

    voice "audio/voice/lars/lars_049_take01.ogg"
    show lars happy
    Lars "Rory, it's so nice to see you again! I missed you too."

    voice "audio/voice/rory/rory_010_take01.ogg"
    show lars happy
    Rory "You too! And good to see that slithering, slimy tail going away."

    Lars narration "The figure that emerges from where Sir Claude stood just a few seconds ago, is none other than Rory, my childhood best friend. True to her lineage as a bull descendent, Rory possesses a fiery temperament and is quick to charge at those who annoy her."

    Lars narration "Under Master Sylvian's guidance, she apprenticed as the guild's head of finance, helping us gather funds for every mission through her puppet shows."

    voice "audio/voice/rory/rory_011_take01.ogg"
    show lars 
    Rory "Mentor, I was preparing my puppets for the afternoon show at the market square."

    show rory angry with dissolve
    show rory angry at jp
    voice "audio/voice/rory/rory_012_take03.ogg"
    show lars 
    Rory "I feel like something is missing but I don't know what exactly..."

    voice "audio/voice/sylvian/sylvian_019_take02.ogg"
    show sylvian serious funny with dissolve
    show lars 
    Sylvian "Let's work together to find something to inspire you before the show, shall we?"

    voice "audio/voice/rory/rory_013_take02.ogg"
    show rory with dissolve
    show lars 
    Rory "Thank you, Mentor. I don't know if my family will be there but I don't want to disappoint them in case I miss the mark with the show later today."

    Lars narration "Rory's family, the Kyoko blacksmiths, and the Dupont merchants have been locked in a spirited rivalry for generations. Both families have passed down their competitive natures to their heirs, adding fuel to the fire."

    Lars narration "However, Rory was an exception to the traditional path of the Kyoko family. While blacksmithing was the cornerstone of their legacy, Rory's talents lay elsewhere. She found her passion in puppet shows and other forms of artistic expression."

    voice "audio/voice/rory/rory_014_take01.ogg"
    show rory angry with dissolve
    show lars
    Rory "They're already giving me side glances for not working with them in the blacksmiths."

    voice "audio/voice/sylvian/sylvian_020_take03.ogg"
    show sylvian sad with dissolve
    show lars 
    Sylvian "Do you need me to talk with them, Rory?"

    Lars narration "Rory offers a faint smile, her thumbs anxiously twiddling together."

    voice "audio/voice/rory/rory_015_take01.ogg"
    show rory with dissolve
    show lars 
    Rory "There's no need. They're the type to be appeased with actions rather than words. The best I can do is prove that I was made for the puppeteer business."

    voice "audio/voice/rory/rory_046_take02.ogg"
    show sylvian with dissolve
    show lars 
    Rory "When life gets tough, I just have to remember to stay strong and keep charging!"

    voice "audio/voice/lars/lars_054_take02.ogg"
    show lars
    Lars "Haha! That's right, Rory, it's not about the size of the bull, it's about the size of its determination!"

    voice "audio/voice/rory/rory_016_take03.ogg"
    show rory angry with dissolve
    show lars 
    Rory "Come on, [Lars]. No shorty jokes. A certain {i}someone{/i} spews enough of them already."

    voice "audio/voice/lars/lars_055_take01.ogg"
    show lars 
    Lars "Alright, alright. I'll make it up to you by helping you out for the show."

    show rory with dissolve
    show rory at jp
    voice "audio/voice/rory/rory_017_take01.ogg"
    show lars 
    Rory "Yay~ Thank you!"

    show lars 
    Claude "{size=*1.25}I have arrived with our mystery artifact." with vpunch

    show rory at center_left
    show sylvian at right
    with move
    
    show claude smile at center_1left
    with moveinleft
    Lars narration "Speak of the devil, Sir Claude makes his entrance with the grande and ornate box held tightly by his tail. His eyes glimmer with a mixture of anticipation and excitement."

    hide sylvian
    hide claude
    hide rory
    with dissolve

    show box with dissolve
    Lars narration "However, rather than keeping it for himself, he extends the box towards me."

label CS_1_End:

    hide box with dissolve

    show claude smile at center_1left
    show rory at center_left
    show sylvian at right
    with dissolve

    Lars narration "As the heavy weight of the artifact transfers to my hands, I feel a sense of responsibility settle in."

    if options["CS1"]==1:
        show lars
        Lars "I think I can take it from here, Master."

        show lars
        show sylvian sad with dissolve
        Sylvian "Carrying such things after your tiring journey might affect your health, [Lars]."

        show lars
        show sylvian blush with dissolve
        Sylvian "But thank you for worrying about me...I really appreciate it coming from you."


    else:
        show lars
        Lars "I think I can take it from here, Sir Claude."

        show lars
        show claude smile with dissolve
        show claude smile at jp
        Claude "Anxious for the reveal. Aren't you?"

        show lars
        Claude "Don't worry, I'm not a fan of breaking promises. Especially, for one I made with you."

    show sylvian sad with dissolve
    show lars
    Sylvian "Let me cast an energizing spell for you just in case, [Lars]. I wouldn't want you to hurt yourself carrying something heavy like that."

    show lars
    Sylvian "If there's one thing my academic days have taught me, it is to not overwork when there's an easier alternative available."
    
    show lars
    Sylvian "No one will truly appreciate your effort if you're the sole person assigning value to it..."

    menu:
        " " " "
        "Accept his offer":
            $ options["S1"]=1
            jump accept_his_offer

        "Reject his offer":
            $ options["S1"]=2
            jump reject_his_offer


label accept_his_offer:

    Lars narration "Something is telling me I should accept his offer."

    show lars
    Lars "Yes, please. This box isn't doing me any favors either."

    show rory at jp
    voice "audio/voice/rory/rory_018_take02.ogg"
    show lars
    Rory "Oh Claudyyy, how about you tell me what the trip was like?"

    show claude shocked with dissolve
    show lars
    Claude "Hold on, little Rory, where do you think you're taking me all of a sudden—"

    hide claude
    hide rory
    with moveoutleft

    show sylvian with dissolve
    show sylvian at center with move
    pause 1.0

    show bg_2:
        pause 0.5
        parallel:
            easein 0.25 zoom 1.1
            easeout 0.5 zoom 1.0
            easein 0.25 zoom 1.05
            easeout 0.5 zoom 1.0
        parallel:
            easein 0.25 blur 20
            easeout 0.5 blur 0
            easein 0.25 blur 10
            easeout 0.5 blur 0
    show sylvian:
        linear 0.5 xalign 0.5
        parallel:
            easein 0.25 zoom 1.1
            easeout 0.5 zoom 1.0
            easein 0.25 zoom 1.05
            easeout 0.5 zoom 1.0
        parallel:
            easein 0.25 blur 5
            easeout 0.5 blur 0
            easein 0.25 blur 5
            easeout 0.5 blur 0

    Lars narration "Instantly, Master Sylvian utters an incantation and a sense of liveliness washes over me, like the exhilaration that follows after completing a marathon."

    show sylvian blush with dissolve
    show lars
    Sylvian "Are you feeling better now? I could conjure up some stalks to help with the box as well—"

    hide sylvian with dissolve

    show lars_energy with dissolve

    show lars narration
    Lars "It's okay Master, I need to get in my daily dose of exercise too. I don't want you to think that I'm too weak for one box! More than that, what would our passengers think if their pilot wasn't able to pick up their luggage or equipment?"
    
    show lars narration
    Lars "My parents wouldn't let me live this down if they ever heard such rumors since they raised me to give my all to take care of those around me considering—"
    
    Sylvian "Oh my, such an interesting result..."

    show lars narration
    Lars "Haha, nothing to worry about! But did you know, Master Sylvian? I was researching Spotsy and as part of the {i}Roseate Flame{/i} species, the intense temperature generated through their breathing process can cause the air pockets under their scales to bubble and expand."
    
    show lars narration
    Lars "Their flushed distortions aren't for mere show either, Rory mentioned that certain blacksmiths hire them for their forging practices since the heat produced is exceptionally hotter than regular flames, making it a valuable resource for crafting extraordinary weapons and armor—"

    hide lars_energy with dissolve

    voice "audio/voice/sylvian/sylvian_024_take03.ogg"
    show sylvian blush at center
    with dissolve
    show lars
    Sylvian "As much as I enjoy hearing you talk about the dragons which you treasure, we need to calm you down a little. Let's use that breathing technique that I taught you last time. You remember, [Lars]?"

    show bg_2:
        xalign 0.5
        yalign 0.5
        parallel:
            linear 2.0 blur 15
        parallel:
            linear 2.0 zoom 1.2
    
    show sylvian blush at center with move
    show sylvian blush:
        parallel:
            linear 1.0 yalign 0.2
        parallel:
            linear 3.0 zoom 1.50

    Lars narration "He takes my hand into his own, slowly tracing circles on my palm. His touch feels warm, and there's a slight hint of perspiration, as if he's nervous about holding it."

    voice "audio/voice/sylvian/sylvian_025_take01.ogg"
    show lars
    Sylvian "Breathe for 3 seconds...hold it for 6...now release it for 9 seconds..."

    Lars narration "Obediently, I follow Master's instructions, allowing my breath to gradually slow down. Despite my heart still thumping in my chest, each measured inhale and exhale brings a sense of calm that envelops me, grounding me in the present moment."

    voice "audio/voice/sylvian/sylvian_026_take03.ogg"
    show lars
    Sylvian "No one is going to think those things of you, [Lars]."

    voice "audio/voice/sylvian/sylvian_027_take02.ogg"
    show lars
    Sylvian "If I were a dragon, I wouldn't want any other pilot than you to take care of me. I've seen how you praise their efforts and spoil them relentlessly."

    voice "audio/voice/sylvian/sylvian_028_take01.ogg"
    show lars
    Sylvian "I mean, who wouldn't want to be praised by someone they admire...I mean, not that I admire you in {i}that{/i} way, but ughhh...nevermind!"

    Lars narration "Suddenly, he takes hold of the tips of my fingers, as if he's shying away from holding my hand fully. I'm sure my ears are flushed all the way from the sweetness of his shy gesture."

    Claude "So, what I gather is that Master Sylvian wants to have [Lars] ride him—"

    show bg_2:
        parallel:
            linear 2.0 blur 0
        parallel:
            linear 2.0 zoom 1.0
    show sylvian:
        parallel:
            linear 1.0 yalign -0.1
        parallel:
            linear 1.0 zoom 1.0

    show lars
    Lars "Since when were you two here?"

    show sylvian blush at right with move

    show claude at center_1left
    show rory at center_left
    with moveinleft

    voice "audio/voice/rory/rory_019_take01.ogg"
    show lars
    Rory "Sorry Master, I couldn't keep him occupied any longer."

    show sylvian blush
    Lars narration "In the blink of an eye, Master Sylvian's demeanor shifts. He turns his head away, almost as if he's trying to conceal his reaction to Claude's statement. Yet, even from behind, I catch a glimpse of his ears slightly reddening."

    show lars blush
    Claude "My, my, my, are you feeling hot all of a sudden, Boss? Maybe it's because of all the cloaks and layers you're wearing."

    voice "audio/voice/lars/lars_058_take02.ogg"
    show lars blush
    Lars "He's joking, Master Sylvian. Just forget about him. I appreciate the energizing spell, even if it didn't work out like we thought."

    voice "audio/voice/sylvian/sylvian_029_take04.ogg"
    show sylvian serious funny with dissolve
    show lars blush
    Sylvian "Definitely not. I'll have to look into ways to tweak it for better results in the future."

    voice "audio/voice/lars/lars_059_take01.ogg"
    show lars blush
    Lars "And not just that...I, um, wanted to thank you for helping me stay calm and for the motivational words. It's not often that someone praises my dragon skills. I thought no one really cared."

    show sylvian blush with dissolve
    show sylvian blush at jp
    voice "audio/voice/sylvian/sylvian_030_take04.ogg"
    show lars blush
    Sylvian "{size=*1.25}OF COURSE I DO!" with vpunch

    show sylvian:
        zoom 1.0

    Lars narration "Wow, it's not often that he raises his voice like that."

    voice "audio/voice/sylvian/sylvian_031_take04.ogg"
    show lars
    Sylvian "I don't think it's the right place to talk about this, but know that I always keep you in mind, Lars. You're really precious to me- ah, I meant, to our guild. Not- not only to me, of course. But I mean you- well you are but ugh-"

    voice "audio/voice/lars/lars_060_take01.ogg"
    show lars
    Lars "Haha, I know, Master. You're not just a Boss to me; you're a friend as well."

    voice "audio/voice/sylvian/sylvian_032_take02.ogg"
    show sylvian sad with dissolve
    show claude smile with dissolve
    show lars
    Sylvian "Ah, what a joy to be  just a {i}friend{/i} to you..."

    voice "audio/voice/sylvian/sylvian_033_take04.ogg"
    show lars
    Sylvian "{size=*0.75}Maybe my own lack of directness caused this in the first place."

    voice "audio/voice/lars/lars_061_take01.ogg"
    Lars "Pardon me?"

    voice "audio/voice/sylvian/sylvian_034_take02.ogg"
    show lars
    Sylvian "Uhm, ah, n-nothing nothing, uhm, yes, nothing to concern yourself with. Let's analyze the artifact now, shall we?"

    jump S_1_End

label reject_his_offer:

    voice "audio/voice/lars/lars_062_take01.ogg"
    show lars
    Lars "Thank you for the offer, Master. But it's nothing I can't shake off."

    show sylvian sad with dissolve
    Lars narration "He looks dejected, and now I feel guilty about declining his kind proposal."

label S_1_End:

    show claude serious at jp
    show lars
    Claude "{i}AHEM!{/i} I think we're better off witnessing the artifact before the evening sets in and little Rory decides to pull something off for her puppets again."

    show rory angry with dissolve
    show claude smile with dissolve
    show lars
    Claude "I can see fumes coming out of her head as we speak. Oh look! I think they got even bigger."

    show lars
    Rory "Ugh, I can't deal with this again."

    show lars
    Lars "What should we do now, Master?"

    hide lars
    hide sylvian
    hide claude
    hide rory
    with dissolve
    show box with dissolve
    Sylvian "Let me cast a safety spell over the box first, you can never be sure if there are any hidden traps inside."

    Lars narration "After a few seconds of inspection without any notable reactions, Master Sylvian breaks the silence."

    hide box with dissolve
    
    show rory at center_left
    show claude at center_1left
    show sylvian at right
    with dissolve
    
    show lars
    Sylvian "No traps or enchantments detected. It seems we're in the clear."

    show claude smile with dissolve
    show lars
    Claude "Time to witness the treasure within, Captain."

    hide rory
    hide claude
    hide sylvian
    show normal_necklace 
    with dissolve

    Lars "As I carefully open the ornate box, I discover a beautiful necklace inside. It features a simple leather band and a captivating centerpiece-a stunning red gem with a mesmerizing ruby hue."

    Lars "An unsettling feeling creeps in the longer I gaze at it, as if it could ensnare my focus. Shivers run down my spine, and my fur stands on end, reacting to some unseen energy."

    show lars
    Claude "Before anyone starts their inspection, I promised our dear Captain he'd be the first person to hold it."

    hide normal_necklace
    
    show rory at center_left
    show claude at center_1left
    show sylvian at right
    with dissolve

    show lars serious
    Lars "Thanks, but no thanks, Sir Claude. My instincts are warning me about this artifact, something seems off about it."

    show lars serious
    Claude "It wouldn't hurt to at least hold it in your hand, would it?"

    Lars narration "I direct my gaze towards the opened box, feeling the weight of everyone's anticipation upon me. Carefully lifting the necklace from its resting place, I note its light size despite the box's heftiness."

    show rory at jp
    show lars
    Rory "Wow! It's truly a work of art."

    show sylvian serious funny with dissolve
    show lars
    Sylvian "Indeed, it's a testament to the skill and craftsmanship of the civilization that created it. {i}But who and when exactly?{/i}"

    show claude smile with dissolve
    show lars
    Claude "We have no idea about its origins yet, but that's the fun part of it all."

    show lars
    Claude "Not to mention, I could never let go of such a mysterious prize, I need to uncover its secrets all for myself..."

    Lars narration "Sir Claude's expression undergoes a striking transformation, shifting from one of casual curiosity and playful mirth to that of intense obsession. His eyes fixate unwaveringly on the artifact, a glimmer of determination and fervor dancing within them."

    Lars "It is no secret that he possesses a deep-seated fascination with challenges and trials. Though he seldom shares the reasons behind his unwavering obsession, his eyes betray his inner excitement whenever faced with such an opportunity."

    show claude at jp
    show lars
    Claude "...Ahem, with the help of our prestigious scholar as well of course!"

    show lars
    Claude "Boss Sylvian, you have quite the reputation in the academic world for your discoveries and inventions. If someone were to understand the potential behind this artifact, it would be none other than you."

    show rory angry with dissolve
    show lars serious
    Rory "Ugh, quit trying to suck up and get close to my Mentor with your scale-rotten face."

    show lars serious
    Claude "Weren't these the very same scales you took for that one specific doll of yours? Admit it, you just don't measure up to scale. Specifically, {i}my scales!{/i}"

    show lars serious
    Claude "Hmm, what was it called again? Boring-ina? Boorish-ina? Banal-ina?"

    show lars serious
    Rory "It was BRITTINA, you dagger-mouthed, bark-bellied, algae-breathing gullet on legs—" with vpunch

    show sylvian serious funny with dissolve
    show lars serious
    Sylvian "Oh dear...things are starting to get out of hand."

    show lars serious
    Lars "Come on guys, it's time to stop. We're losing daylight over here."

    Lars narration "As always, neither side showed any signs of stopping their retort. After all, the first to stop would be the first to lose and their competitive nature wouldn't allow them this leeway."

    show claude at jp
    show lars serious
    Claude "It's no wonder that your family legacy is going to die with you. I wouldn't put myself in the low position of insulting you, though it's a huge plus if I do."

    show lars serious
    Lars "Sir Claude, that's not like you to—"

    show lars serious
    Rory "Look, I think we all have something to bring to this conversation, but you don't. Especially when all you ever have to add is self-inserted praise and narcissism."

    show lars serious
    Lars "Come on Rory, you don't really mean that—"

    show sylvian serious funny at jp
    show lars serious
    Sylvian "{size=*1.25}Both of you, it's time to stop." with vpunch

    show sylvian:
        zoom 1.0

    show claude shocked with dissolve
    show rory with dissolve

    Lars narration "Master Sylvian's voice echoes through the air, instantly commanding everyone's attention and calming the conflict-ridden atmosphere."

    Lars narration "While he typically exudes a collected composure, there are occasions when he utilizes his authoritative voice to instill a sense of order among those around him."

    Lars narration "It's a captivating contrast, witnessing the guild leader within him command respect and bring about a calm atmosphere."

    show sylvian with dissolve
    show lars
    Sylvian "Let us embrace empathy's grace and refrain from jesting, for each soul carries its own unique beauty. Whether it be descendents of lizards, foxes, swans, or bulls."

    voice "audio/voice/rory/rory_021_take02.ogg"
    show lars
    Rory "Sorry, Mentor. Looks like I've overstepped a bit."

    show claude with dissolve
    show lars
    Claude "It's never a good move to annoy your benefactor. Apologies, Boss."

    Lars narration "As Sir Claude and Rory move away to not bump heads again, I quietly make my way towards Master Sylvian."

    hide claude 
    hide rory
    with moveoutleft

    show sylvian at center
    with move

    show lars
    Lars "Thanks for easing off the tension, Master. It gets out of hand when they start bickering."

    Lars narration "A shy smile graces Master Sylvian's lips as he gently rests his hands on my shoulders. The feathers of his swan-like wings delicately brush against my back, imbuing me with a sense of tranquility and ease."

    show lars
    Sylvian "No problem at all, [Lars]. I might not understand your relationship with Rory well, as you have been best friends from a young age...but I would hate to see a rift between us as guild members."

    show lars
    Sylvian "Your bond with Rory holds a treasure untold. A childhood's embrace worth more than gold."

    show sylvian sad with dissolve
    show lars sad
    Sylvian "I wish I could have that kind of equal friendship too."

    Lars narration "He's acting a bit strange, what should I do now?"

    menu:
        " " " "
        "{size=*0.97}Poke further and ask why he's feeling that way":
            $ options["S2"]=1
            jump poke_further_and_ask

        "{size=*0.97}Joke about his statement and steer the conversation":
            $ options["S2"]=2
            jump joke_about_his_statement


label poke_further_and_ask:

    Lars narration "It's not like Master Sylvian to act like this, and seeing him slightly melancholic leaves me with a sense of concern."

    voice "audio/voice/lars/lars_063_take02.ogg"
    show lars sad
    Lars "What do you mean, Master. Are you saying we aren't friends? Did our departure make you lonely?"

    Lars narration "He shakes his head a bit, as if trying to clear his thoughts."

    voice "audio/voice/sylvian/sylvian_035_take03.ogg"
    show lars sad
    Sylvian "It's just that as your superior, I don't have the equal relationship that you have with Rory or Claude—"

    voice "audio/voice/lars/lars_064_take01.ogg"
    show lars
    Lars "You know, even though I'm just your junior, you're a cherished friend to me. Of course, I value you first and foremost as our Boss, but I also appreciate how you're always kind to everyone."

    Lars narration "Summoning all my courage, I move closer and grasp Master Sylvian's hands, locking my gaze with his."

    show bg_2:
        xalign 0.5
        yalign 0.5
        parallel:
            linear 2.0 blur 15
        parallel:
            linear 2.0 zoom 1.2
    
    show sylvian blush at center with move
    show sylvian blush:
        parallel:
            linear 1.0 yalign 0.2
        parallel:
            linear 3.0 zoom 1.50

    Lars narration "The initial shock on his face gives way to a warm and genuine smile, a flicker of happiness illuminating his eyes."

    voice "audio/voice/lars/lars_065_take01.ogg"
    Lars "I'm sorry if it sounds like I'm trying to, you know, suck up to you or ask for something. That's really not my intention at all. It's just— Well, I tend to be pretty straightforward, especially when dealing with stray dragons. I mean, not that I'm saying you're anything like a stray dragon! I guess what I'm trying to say is, ugh..."

    voice "audio/voice/sylvian/sylvian_036_take03.ogg"
    show lars
    Sylvian "Heh! Frogive me, I just- haha..." with vpunch

    voice "audio/voice/sylvian/sylvian_037_take03.ogg"
    show lars
    Sylvian "Ah, what a delight you are [Lars], what would I do without you to brighten up my day? A stray dragon, you say?"

    voice "audio/voice/lars/lars_067_take01.ogg"
    show lars blush
    Lars "Come on, Master, I have a reputation to keep as a dragon pilot. You can't go around telling everyone that I compared my guild master to a stray dragon. I'll never hear the end of it from Rory and Sir Claude."

    Lars narration "I shake my head in mock frustration, burying my face in my hands. Master Sylvian always falls for these antics, especially when someone asks for his help or a favor."

    show bg_2:
        parallel:
            linear 2.0 blur 0
        parallel:
            linear 2.0 zoom 1.0
    show sylvian:
        parallel:
            linear 1.0 yalign -0.1
        parallel:
            linear 1.0 zoom 1.0

    voice "audio/voice/sylvian/sylvian_038_take03.ogg"
    show lars blush
    Sylvian "It's alright, [Lars], just lift your head and look at me. I'll keep our little secret safe, just between us, alright?"

    show sylvian:
        zoom 1.0

    Lars narration "As if understanding my need for reassurance, he gently pets me on the head, softly rubbing my ears in the process."

    voice "audio/voice/sylvian/sylvian_039_take03.ogg"
    show lars blush
    Sylvian "Don't worry about me too much, [Lars]. It's just that...it's hard to bring out the words that build up in your throat sometimes."

    voice "audio/voice/sylvian/sylvian_040_take02.ogg"
    show lars blush
    Sylvian "But I do appreciate your efforts, I just hope that I can be the recipient of your more {i}endearing{/i} efforts as well."

    show lars blush
    Lars "Did I hear him right? I can't believe he'd say something like that..."

    jump S_2_End

label joke_about_his_statement:

    voice "audio/voice/lars/lars_068_take02.ogg"
    show lars
    Lars "Don't worry about it, Master! I have never seen a person more talented than you in casting flower magic. I'm sure that if you whip up a quick spell, you'll have everyone fighting to be your companion in no time."

    hide sylvian with dissolve
    show sylvian_upset with dissolve

    voice "audio/voice/sylvian/sylvian_041_take03.ogg"
    Sylvian "Well, it's no use tricking people into becoming your companions, [Lars]."

    voice "audio/voice/sylvian/sylvian_042_take01.ogg"
    Sylvian "We used to have a lot of rivalry back in the Tower of Magicians. Your comment reminds me of those days where we would try and use every trick up our sleeves to get ahead."
    
    voice "audio/voice/sylvian/sylvian_043_take02.ogg"
    Sylvian "I wish to never go back to those days if possible. After all, {i}Custodes Sylvae{/i} is my current solace."

    hide sylvian_upset with dissolve
    show sylvian sad at center with dissolve

    Lars narration "In an instant, the atmosphere shifts, and a wave of melancholy washes over Master Sylian. His hands, once tranquil, now tremble slightly, and the furrow on his brow deepens as if he's grappling with memories etched on his face."

    Lars narration "His jaw tightens, a silent struggle playing out in the subtle lines that trace his expression. It's as if he's transported himself back to moments he'd rather keep buried, and the weight of untold stories lingers in the air."

    voice "audio/voice/lars/lars_070_take01.ogg"
    show lars sad
    Lars "Uhm, Master, you might have misunderstood something, I meant that we enjoy your company as fellow guild members, not that we—"

    voice "audio/voice/sylvian/sylvian_044_take03.ogg"
    show lars sad
    Sylvian "It's okay [Lars], I'm just getting upset on my own, that's all."

    Lars narration "My words don't seem to reach him anymore, it seems."

label S_2_End:

    show sylvian serious funny at center
    with dissolve
    pause 1.0

    show lars
    Sylvian "EVERYONE! Steadfast now."

    Lars narration "Nevermind, he was probably feeling sentimental."

    show sylvian serious funny at right
    with move
    show claude at center_1left
    show rory at center_left
    with moveinleft

    Lars narration "As everyone settles under Master Sylvian's gentle yet authoritative command, he takes hold of the artifact, brimming with curiosity."

    show lars
    Sylvian "It's time to get back to business. I'd like to observe this a bit more in my lab as well."

    hide sylvian
    hide claude
    hide rory
    with dissolve
    
    show normal_necklace with dissolve

    show lars
    Sylvian "It eerily resembles an artifact that I had previously seen in the Archmage's tower. A one-of-a-kind necklace with a similar gemstone belonging to a family of dragons with our very own half-human, half-animal traits as descendants."
    
    show lars
    Sylvian "I haven't heard of them in quite some time, and though the color of its gem contrasts the descriptions I've heard and read, the artistry is quite similar."

    hide normal_necklace with dissolve
    
    show sylvian serious funny at right
    show claude at center_1left
    show rory at center_left
    with dissolve

    show lars
    Sylvian "Speaking of which, how much did you exchange for it, Claude? We need to see if the funds from Rory's recent puppet show will be able to cover the costs."

    show claude smile with dissolve
    show lars
    Claude "A merchant only parts with what they're willing to share. Fortunately, the notorious Claude can conquer any challenge he wishes for at his own behest."

    show lars
    Claude "I received this curious box free of charge. The seller was practically begging me to take it."

    show lars
    Claude "Ah, the misery of knowing the world will fit into the palm of my hand as long as I aim for it."

    Lars narration "Rory's eyes widen to an almost comical extent, as if they're on the verge of rolling out of their sockets. As for Master Sylvian, he merely closes his eyes, whether he's focusing on what Sir Claude is saying or mentally preparing himself for any upcoming conflicts...I can't tell."

    show lars
    Rory "Narcissus left a voicemail, saying he's issuing the world a mental refund for the surplus of self-absorption you're currently exuding."

    show lars
    Claude "Getting real creative with the insults, aren't you?"

    show rory angry with dissolve
    show lars
    Rory "I have never meant anything more in all my bull years."

    show lars
    Claude "That explains why you're such a bullshitting—"

    show lars
    show sylvian at jp
    Sylvian "Ahem! Let's move on, shall we?"

    Lars narration "Nice save as always."

    show lars
    show rory
    Rory "By the way Mentor, can I take this artifact for a spin before you put it in your lab?"

    show lars
    Rory "I could whip up a show-stopping puppet in no time with it."

    show claude shocked with dissolve
    show lars
    Claude "But that's absurd, who knows when your puppet project is going to finish?"

    show lars
    Lars "That's a great idea. We could come and visit your puppet show stall this way too. It's been quite a while since I last played with the kids."

    show lars
    Sylvian "If you feel inspired by this artifact, then by all means, go ahead."

    show lars
    Claude "Not you too, Boss..."

    show claude smile with dissolve
    show lars
    Claude "Captain, how about you wear the necklace for now instead of little Rory? It's color suits your fur, after all."

    show rory angry with dissolve
    show lars
    Rory "Not with the little Rory comment again—"

    show lars
    Claude "It reminds of the red string of fate...though, placing your faith in such notions is for those incapable of steering their own lives."

    show lars serious
    Lars "These confession jokes are getting really out of hand."

    hide lars
    hide rory 
    hide claude 
    hide sylvian
    with dissolve 
    
    show normal_necklace 
    with dissolve

    show blink_necklace
    with dissolve
    Lars narration "Alas, disregarding Sir Claude's comment, I take the moment to put on the necklace, the gemstone's ruby color captures my attention and I marvel at the curious glow that emits from it."
    
    Lars narration "It's strange though, I don't recall the color being so vibrant. It's almost as if it's shining or signaling something."

    hide blink_necklace
    hide normal_necklace with dissolve
    
    show rory at center
    with dissolve
    Rory "Let's go [Lars], or you'll get left behind~ The others already went ahead."

    Lars "I'm coming, wait for me!"
    
    hide rory with moveoutright

    play sound sfx_grassy_walk loop
    Lars narration "Shaking off my trance, I hasten toward the others who have gathered ahead."

    Lars narration "Master Sylvian deliberately slows his steps and I pass him. Looks like he'll be keeping a watchful eye over the rest of us as we go ahead."

    Lars narration "Meanwhile, Sir Claude and Rory pick up their pace, engaging in a competition to see who can reach the puppet stall first. Their banter fills the air as they exchange witty remarks, not holding back on their rivalry."

    Lars narration "Hopefully, it'll be another day without any troubles here in Divonia and {i}Custodes Sylvae{/i}."

    stop sound fadeout 2.0

    $ renpy.choice_for_skipping()

    play music "track_3_the_town.ogg" fadeout 2.0 fadein 2.0
    scene bg black with fade
    show bg_3 at pan with fade

    play sound sfx_people_talking loop

    Lars narration "The town square pulsates with vibrant energy with the captivating tapestry of stalls embellishing the grassy pathway."
    
    Lars narration "As I walk through this bustling scene, my attention is drawn to the medley of merchants enticing passersby with their wares, creating an atmosphere of enchantment and wonder."

    Lars narration "The tantalizing scents of delectable dishes waft through the air, drawing in hungry travelers, including myself, with promises of culinary delights."

    show bg_3 at end_pan

    Lars narration "As I stroll along, my mind wanders to my guildmates, and I can't help but imagine them donning different attire from the clothing boutiques."

    Lars narration "My imagination runs wild with visions of my guildmates donning different attire from the stalls."

    stop sound fadeout 1.0

    show bg_3 at bg_blur:
        parallel:
            linear 0.5 xalign 0.5
        parallel:
            linear 1.0 zoom 1.5
    show rory at center:
        parallel:
            linear 1.0 zoom 2.0
        parallel:
            linear 2.0 yoffset 200
            linear 9.0 yoffset 760
    
    Lars narration "Rory comes to mind first as my best friend. A practical and independent soul, whose artistic flair and unique personality are effortlessly mirrored in her attire."

    Lars narration "Her outfits are accessorized with charming trinkets. Practical short sleeves allow her to move with ease, while thoughtfully designed pockets serve as clever storage for her beloved tools and equipment for her puppet shows."

    show bg_3:
        linear 1.0 zoom 1.0
    show rory:
        parallel:
            linear 1.0 yoffset 0
        parallel:
            linear 1.0 zoom 1.0
        parallel:
            linear 1.0 xalign 0.5

    Lars narration "Particularly her emergency puppets, which always seem to come to the rescue in unexpected situations."

    hide rory with dissolve

    Lars narration "Hmm...who else comes to mind?"

    menu:
        " " " "
        "Master Sylvian's academic outfit":
            $ options["CS2"]=1
            jump master_Sylvian

        "Sir Claude's merchant outfit":
            $ options["CS2"]=2
            jump sir_Claude

label master_Sylvian:
    show bg_3 at bg_blur:
        linear 2.0 zoom 1.5
    show sylvian at center with dissolve:
        parallel:
            linear 2.0 zoom 2.0
        parallel:
            linear 2.0 yoffset 200
            linear 10.0 yoffset 830

    Lars narration "As a flower magician, Master Sylvian weaves his clothing with delicate floral spells, each stitch carrying the soft whisper of his incantations."

    Lars narration "His fondness for deep, shadowy hues consistently manifests in his attire—a seamless blend of midnight-hued blossoms that effortlessly complement the color palette of his elegant, swan-like wings."

    Lars narration "There's also his signature personally-crafted magician's hat. He once mentioned that this unique accessory serves to stabilize the emotional energy he channels, transforming it into an array of different blooms."

    Lars narration "I wish I had the ability to decipher the meaning behind the flowers that draw from his emotions."

    Lars narration "Yet, my knowledge in this area primarily revolves around memorizing names of plants and herbs safe for dragons - avoiding accidental poisonings, preventing ailments, and ensuring respectful offerings, among other practical considerations."

    Lars narration "Nevertheless, next to Master Sylvian, my understanding barely scratches the surface. He may downplay it, but getting to his level of expertise seems like it would take a century, if not more."

    Lars narration "That's one of the many things I admire about him— being so knowledgeable yet never shying away from wanting to discover more about the world and the people around him."

    show bg_3:
        linear 1.0 zoom 1.0
        
    hide sylvian with dissolve

    show sylvian at right
    show rory at center_left 
    show claude smile at center_1left
    with dissolve 

    jump CS_2_End

label sir_Claude:
    show bg_3 at bg_blur:
        linear 2.0 zoom 1.5
    show claude smile at center with dissolve:
        parallel:
            linear 1.0 zoom 2.0
        parallel:
            linear 2.0 yoffset 200
            linear 10.0 yoffset 900
   
    Lars narration "Sir Claude always holds his appearance with unparalleled pride. I can envision him draped in a new style of opulent faux fur and leather clothing curated from exotic lands courtesy of his family, and even his own, well-established connections."

    Lars narration "Surrounded by a retinue of devoted servants, he could easily present with a garment thoughtfully designed to accentuate and showcase his glistening scales, and maybe even leave an opening for his enormous tail."

    Lars narration "But, given his independent streak, I wouldn't be surprised if he goes with whatever catches his eye, not caring much about what's in vogue among the nobles or even paying attention to the advice of his fashionista advisors."

    Lars narration "Just looking at him now, with those silver braids cascading down his back, I'm served a gentle reminder to do something about my own unruly fox fur and maybe tidy up my ponytail."
    
    Lars narration "That's one of the many things I admire about him— being his own source of inspiration without having to make a conscious effort to appeal to others or impress them."
    
    show bg_3:
        linear 1.0 zoom 1.0
    show claude smile:
        parallel:
            linear 1.0 yoffset 0
        parallel:
            linear 1.0 zoom 1.0
        parallel:
            linear 1.0 xalign 0.5

    hide claude smile with dissolve

    show claude smile at center_1left
    show rory at center_left 
    show sylvian at right
    with dissolve

label CS_2_End:

    show claude smile at center_1left:
        zoom 1.0
    show sylvian at right:
        zoom 1.0

    show lars
    Rory "I don't think I need to mention this, but if any of you happen to spot my parents, could you...convince them to attend the show?"

    show lars
    Rory "I've tried inviting them countless times, but they always manage to find an excuse. Maybe...if someone else were to extend the invitation, they might feel too embarrassed to decline."

    Lars narration "Rory's family always took pride in showcasing their meticulously crafted armors and weapons, forged over the years. Whenever I pass by their stall, I can't help but be awestruck by the gleaming steel and the intricate designs that speak of their unwavering dedication to their art."

    Lars narration "It's no surprise that if anyone were to harness the shimmering blazes of the {i}Roseate Flame{/i}, it would be them, for they embody the spirit of the forge and the indomitable strength of their bull lineage."

    show lars
    Claude "Let it be known that I'm only helping out because I want to spend some more time with Captain [Lars] over here. Otherwise, I'd be indulging in a cool shade at my family's own tradepost. After all, who knows what new trinkets await to be blessed by my presence when I'm there."

    Lars narration "The Dupont family are notorious for their array of foreign novelties; enticing visitors with a fascination for distant lands and cultures. Their stalls are always filled with rare and luxurious items, each one carefully curated to capture the attention of potential buyers seeking something unique for an exorbitant price."

    show sylvian sad with dissolve
    show lars
    Claude "Who knows, my dear Captain, some of them might just complement your new necklace perfectly. I'd love to see them on you during our adventures. I can already picture a fantastic matching set—"

    show lars
    Lars "Thanks for the offer, Sir—"

    show claude serious with dissolve
    show claude serious at jp
    Claude "{size=*1.25}{i}Ahem!{/i}" with vpunch

    Lars "—Claude, but what use would I have for them? They'll only get lost during dragon riding."

    show claude shocked with dissolve
    Lars narration "Ever the showman, he raises his eyebrows in mock shock, pausing with a light gasp."

    show lars
    Claude "So, you're open to accepting an accessory that's on you without you needing to pocket it, right?"

    show lars
    Lars "I guess so, but I don't want to force—"

    show claude smile with dissolve
    show lars
    Claude "Perfect! Now, what would be the ultimate gift to match Captain's splendor?"

    show lars
    Claude "Any thoughts, Rory {i}dearest{/i}?"

    Lars "What do you mean—"

    show rory angry with dissolve
    show lars
    Rory "Why should {i}I{/i} help {i}you{/i}?"

    show lars
    Claude "How about a friendly competition, then? May the best one, {i}which couldn't be anyone other than me{/i}, win and the prize will be—"

    show lars
    Rory "I couldn't care any less about prizes. I just want to savor your defeat!"

    show rory with dissolve
    show lars
    Rory "Now! Let me think this through..."

    show lars
    Rory "Earrings? Nah, not good. They'd be gone with the wind before you know it!"

    show lars
    Rory "[Lars] already has that artifact on, so no need for any necklaces."

    show lars
    Rory "Bracelets or anklets would be a disaster around the dragons too. They've got those sharp spikes and claws that could easily get tangled up. We either need to go bigger, like a full-on dragon armor or go smaller like a—"

    show lars
    Claude "How about a ring then? It could be the perfect accessory to keep on without it getting in the way."

    show claude blush with dissolve
    show lars
    Claude "What about it, Captain? Are you up for it?"

    show lars blush
    Lars "What are you talking about? That's basically a proposal, isn't it?"

    show lars blush
    Claude "Not so much a proposal, but more of a heartfelt promise that you'll keep me in mind whenever you look at it. After all, you always accept Boss's bouquets and poems. Don't they count as gifts too?"

    show lars
    Lars "Well, sure, they do...but I can't picture him having flirtatious intentions like yours, right Master? And weren't you the one cracking confession jokes all the time anyway, Sir Claude? I'm sure it's no different this time."

    Lars narration "As seconds stretch into an uncomfortable silence, I scan the room, hoping for any signs of acknowledgment. Yet, the absence of a single uttered word leaves me with an awkward feeling."

    Lars narration "Sir Claude seems to already be lost in a daydream as he softly whispers to himself. It looks as if he's planning something important and couldn't care less about the current situation."

    Lars narration "Meanwhile, Master Sylvian, who lingering inconspicuously in the background -to the point of escaping my notice- now stands quietly. His eyes fixed upon me, silently pleading for acknowledgment."

    Lars narration "Who should I question about the intentions behind their gifts?"

    stop music fadeout 1.0
    menu:
        " " " "
        "Ask Master Sylvian about his poems and flowers":
            $ options["CS3"]=1
            jump ask_Master_Sylvian_about

        "Ask Sir Claude about his keepsake ring":
            $ options["CS3"]=2
            jump ask_Sir_Claude_about

label ask_Master_Sylvian_about:

    play music "track_6_romance_scene.ogg" fadeout 2.0 fadein 2.0
    
    hide claude 
    hide rory
    with dissolve

    show sylvian sad at center with move
    with move
    Lars narration "It's best to approach Master Sylvian first, as he tends to take my words more seriously than Sir Claude does."

    voice "audio/voice/lars/lars_071_take01.ogg"
    show lars
    Lars "Master, why didn't you answer my question earlier?"

    voice "audio/voice/lars/lars_072_take01.ogg"
    Lars "Did you...have a different intention behind all the gifts you've given me so far?"

    voice "audio/voice/sylvian/sylvian_045_take03.ogg"
    show lars
    Sylvian "Uhm...how do I put it...it's j-just that—"

    voice "audio/voice/sylvian/sylvian_046_take03.ogg"
    show lars
    Sylvian "W-well, I...I don't think this is the best time to, you know...uhm...explain my reasoning, but—"

    voice "audio/voice/lars/lars_073_take02.ogg"
    Lars "So, you do have a reason beyond just our friendship, right? Or is it a secret that you can't tell me?"

    Lars narration "As if drawn in by the gravity of my serious question, he takes a deep breath and looks me directly in the eyes."

    voice "audio/voice/sylvian/sylvian_047_take03.ogg"
    show sylvian with dissolve
    show lars
    Sylvian "I...I don't want to lie to you, [Lars]. Concealing my true feelings would only bring harm upon myself, akin to breaking my own neck under the weight of deception. However, this isn't the right time for me."

    voice "audio/voice/sylvian/sylvian_048_take03.ogg"
    show lars
    Sylvian "You hold a unique place in my heart, [Lars], and I truly admire you. Yet, confessing my secrets now fills me with apprehension, I fear that it might jeopardize the bond we share."

    voice "audio/voice/sylvian/sylvian_049_take03.ogg"
    show lars
    Sylvian "Moreover, the delicate balance of our guild relationship as Boss and member makes my feelings for you...well, somewhat unethical. I'd feel like I'm abusing my power as the leader."

    show lars blush
    Lars "..."

    hide sylvian with dissolve

    show sylvian_flirt with dissolve

    voice "audio/voice/lars/lars_074_take01.ogg"
    show lars narration
    Lars "Understood, Master. I'm not sure I get it entirely, but whenever you feel ready to share, I'll be here to listen."

    voice "audio/voice/lars/lars_075_take01.ogg"
    show lars narration
    Lars "But no more gifts for now, I don't want there to be another misunderstanding between us."

    voice "audio/voice/sylvian/sylvian_050_take03.ogg"
    Sylvian "I'll hold back on the bouquets as you requested, but I confess that abstaining from the poems might prove to be a more difficult task, haha."

    voice "audio/voice/sylvian/sylvian_051_take03.ogg"
    Sylvian "\"If metal can be polished to a mirror-like finish, what polishing might the mirror of the heart require?\""

    voice "audio/voice/sylvian/sylvian_052_take02.ogg"
    Sylvian "\"Between the mirror and the heart is this single difference: The heart conceals secrets, while the mirror does not.\""

    voice "audio/voice/sylvian/sylvian_054_take01.ogg"
    Sylvian "Moving forward, I promise to be transparent with you, to let my honesty shine through, if you'll allow me to."

    hide sylvian_flirt with dissolve

    voice "audio/voice/sylvian/sylvian_054_take02.ogg"
    show sylvian blush at center with dissolve
    show lars blush
    Sylvian "You have my thanks, [Lars]."

    voice "audio/voice/lars/lars_076_take01.ogg"
    Rory "Let's keep on moving, shall we?"

    show sylvian blush at right with move
    show sylvian with dissolve

    show rory at center_left
    show claude at center_1left
    with dissolve
    
    jump CS_3_End

label ask_Sir_Claude_about:
    play music "track_6_romance_scene.ogg" fadeout 2.0 fadein 2.0
    
    hide rory
    hide sylvian
    with dissolve

    show claude blush at center with move
    Lars narration "It's best to approach Sir Claude first, since he tends to be more straightforward with his answers."

    show lars
    Lars "Why did you mention a ring, Sir Claude? I feel like you might be taking the teasing a bit too far today."

    show claude shocked with dissolve
    show lars
    Claude "Captain, why would you ever think that? Especially after promising that you'd wear my gift...so you were toying with my feelings all this time—"

    voice "audio/voice/lars/lars_078_take01.ogg"
    Lars "I didn't promise anything in the first place Sir—"

    show lars
    Claude "{i}Cough, Hack, Wheeze, Gasp, and Splutter.{/i}" with vpunch

    voice "audio/voice/lars/lars_079_take01.ogg"
    show lars serious
    Lars "—Claude. You're not even trying to pretend to cough!"

    show lars serious
    Claude "Obviously, since the previous strategy didn't work with you so I have to take it up a notch."

    show lars serious
    Claude "Anyways, I have no qualms about covering the cost for the ring either."

    voice "audio/voice/lars/lars_080_take01.ogg"
    show lars serious
    Lars "But I said—"

    show claude blush
    show lars blush
    Claude "You could ask for all the gold in this realm, and it would be yours to possess. I'd love to spoil you senseless, you know?"

    show lars blush
    Claude "Or could it be that you want more? Something that can't be bought with gold and jewels?"

    voice "audio/voice/lars/lars_081_take02.ogg"
    Lars "I'm not exactly talking about that, because there's honestly no need—"

    show claude serious
    Claude "Need I remind you about Boss Sylvian's so-called {i}gifts?{/i}"

    Lars narrration "Master's presents are purely gestures of appreciation, but rings usually mean a lot more..."
    
    show lars
    voice "audio/voice/lars/lars_084_take01.ogg"
    show claude sad with dissolve
    Lars "Perhaps...some of my human passengers did mention gifting rings as accessories, is that what you meant?"

    show lars
    Claude "..."
    
    show lars
    Claude "Maybe it's too soon for you to understand what I mean, Captain."

    show lars
    Claude "But you could say the reason I'm suddenly giving you these rings is because of Boss Sylvian over there. I've noticed that he's been getting {i}too close{/i} to you recently, and it's making me—"

    Lars narration "He runs his fingers through his hair, disturbing its meticulously arranged strands. The strong and distinctive scent of his leather cologne wafts through the air as his gaze, like a magnetic force, fixates on me. A playful smile slowly adorns his face."

    show claude smile with dissolve
    show lars
    Claude "I'm not keen on the idea of losing what I've set my sights on to someone else, especially after being so straightforward about my intentions toward you all this time."

    voice "audio/voice/lars/085_take01.ogg"
    show lars serious
    Lars serious "So, it's just a competition to you? A rivalry to see who can get closest to me and then revel in the feeling of winning?"

    show claude shocked with dissolve
    show lars serious
    Claude "That's not what I meant..."

    Lars narration "He takes a deep breath, preparing himself as if he's about to reveal a significant secret."

    show claude sad with dissolve
    show lars serious
    Claude "I do have {i}special{/i} feelings for you, Captain, and I admit they're not ones as simple as friendship. But you know how I've always been hesitant about settling down."

    show lars serious
    Claude "It's a personal struggle that I'm trying to come to terms with, but I can't openly share all of it here right now."

    voice "audio/voice/lars/lars_086_take02.ogg"
    show claude blush with dissolve
    show lars blush
    Lars "{i}Special{/i} feelings?"

    show lars blush
    Claude "Why don't we continue this conversation somewhere private, just the two of us? I'll truly open up and explain my intentions. Please believe me when I say I have no plans to play with your feelings. I promise you."

    show lars blush
    Claude "My interest in you is genuine, but it's difficult for me to keep my emotions anchored when my heart always yearns for new adventures and distant horizons. Not to mention, Boss Sylvian..."

    Lars narration "Hearing Claude's earnest plea, I realize that this situation is more complex than I initially thought. His vulnerability and honesty tug at my heart. I nod, silently agreeing to have this crucial conversation in a more intimate setting."

    show lars blush
    Lars "..."

    hide claude blush with dissolve
    
    show claude_flirt with dissolve

    voice "audio/voice/lars/lars_087_take01.ogg"
    show lars narration
    Lars "Understood, while I can't say I'm entirely satisfied, I won't press you further. Whenever you feel ready to share, I'll be here to listen."

    Claude "Thank you, Captain. You can count on me to keep that promise. I might even add it to the keepsake I'll give you later on."

    voice "audio/voice/lars/lars_089_take02.ogg"
    show lars narration
    Lars "No rings! It would only distract me once people start asking questions about it and I need to keep my mind sharp for our passengers."

    hide claude_flirt with dissolve
    
    show claude blush with dissolve
    show lars 
    Claude "What about your necklace? Why don't I promise on that instead?"

    show bg_3 at bg_blur:
        subpixel True
        linear 2.0 blur 10
    show claude blush at center:
        parallel:
            linear 1.0 yalign -0.1
        parallel:
            linear 3.0 zoom 1.50

    Lars narration "Before I have a chance to respond, Sir Claude closes in, wrapping me in a swift yet firm embrace. I catch a glimpse of a rare and momentary blush on his cheeks as he draws me closer."

    show lars
    Claude "You mean a lot to me, Captain, and I don't want to rush my secret. When the time is right, I'll share everything with you."
    
    show bg_3:
        linear 2.0 blur 0
    show claude blush at center:
        parallel:
            linear 2.0 zoom 1.0
        parallel:
            linear 1.0 yalign 0.5
            linear 1.0 ypos 0.5

    Rory "Let's keep on moving, shall we?"

    show claude blush at center_1left with move
    show claude with dissolve

    show rory at center_left
    show sylvian at right
    with dissolve

label CS_3_End:
    play music "track_3_the_town.ogg" fadeout 2.0 fadein 2.0
    play sound sfx_grassy_walk loop

    scene bg black with fade
    pause 1.0
    show bg_3 at pan with fade
    
    Lars narration "We effortlessly blended into the diverse crowd of people, a mix of descendants with their distinct tails, wings, and horns representing various species."

    Lars narration "Navigating a bustling town square like this would indeed be a challenge for regular descendants, particularly the scarce humans. Yet, after riding countless dragons and becoming accustomed to their scales, a few feathers or fur become manageable obstacles."

    Lars narration "Now that I'm thinking about it..."

    show bg_3 at end_pan

    show lars
    Lars "Hey Rory, since I promised I'd help you out, what's our plan for today going to look like?"

    show claude at center_1left
    show rory at center_left
    show sylvian at right
    with dissolve

    Lars narration "It was no secret that Rory's performances provided the main source of funding for our expeditions and negotiations, making it a collective mission for all of us to occasionally advertise her shows."

    Lars narration "The well-being of our guild's dragons heavily relied on those funds, and I cannot bear the thought of them going hungry or enduring any discomfort. I would willingly starve myself before allowing such a situation to come up."

    show lars
    Rory "I was thinking that we could focus on a children's show for today [Lars], you guys can start gathering the kids up a little further ahead."

    Lars narration "Before long, the collective footsteps of our group come to a halt, a unanimous signal that we had arrived at our destination."

    stop sound fadeout 1.0

    show lars
    Rory "Here we go! A one-of-a-kind stall for one-of-a-kind puppets who actually have a purpose in life, unlike a certain someone."

    show lars
    Rory "Not to mention, Brittina and Alex were very excited to enhance their looks with the help of Claudyyy over here."

    show claude shocked with dissolve
    show lars
    Rory "I did want to pluck out the lizard's eyes for Agatha, but it's very hard to do that in his sleep especially since he's such a light sleeper."

    show lars serious
    Lars "He's the heaviest sleeper I know, what're you talking about?"

    show rory at jp
    show lars serious
    Rory "I wouldn't put it past him to fake it or something. He's quite the attention-seeking piece of work—"

    show lars serious
    Claude "Ehhh, you've been watching over me in my sleep, little Rory?"

    show claude smile with dissolve
    show lars serious
    Claude "I could excuse the scale stealing incident and the hair cutting fiasco because I'm so benevolent."

    show lars serious
    Claude "However, night peeking is a no-no."

    show sylvian sad with dissolve
    show lars serious
    Claude "Unless...it's my lovely Captain who does it."

    Sylvian "That's enough Claude, you're making [Lars] uncomfortable."

    Lars narration "Sir Claude's comment certainly came out of the blue, now they're both looking at me. What should I do now?"

    menu:
        " " " "
        "Look back at Master Sylvian":
            $ options["CS4"]=1
            jump look_back_at_Master_Sylvian

        "Look back at Sir Claude":
            $ options["CS4"]=2
            jump look_back_at_Sir_Claude

label look_back_at_Master_Sylvian:

    show lars serious
    Lars narration "I glance at Master Sylvian, silently seeking his assistance."

    show claude shocked with dissolve
    show sylvian mad with dissolve
    show lars
    Sylvian "Let's give [Lars] some space and respect his feelings, Claude."

    Lars narration "I can see Sir Claude making quite a stupefied face due to the sudden interference. He probably didn't expect to be scolded like that."

    hide claude shocked
    hide rory
    with dissolve
    show sylvian mad at center with move
    show sylvian blush with dissolve

    show bg_3:
        xalign 0.5
        yalign 0.5
        parallel:
            linear 2.0 zoom 1.25
        parallel:
            linear 2.0 blur 15

    show sylvian blush:
        parallel:
            linear 1.0 yalign 0.2
        parallel:
            linear 3.0 zoom 1.50

    
    Lars narration "Meanwhile, Master Sylvian regards me with a kind look as he reaches out and gently rubs my ears, soothing my embarrassment. He's become the sole focus in my line of sight right now..."

    show bg_3:
        xalign 0.5
        yalign 0.5
        parallel:
            linear 1.0 zoom 1.0
        parallel:
            linear 1.0 blur 0

    show sylvian blush:
        parallel:
            linear 1.0 yalign -0.1
        parallel:
            linear 1.0 zoom 1.0


    Claude "Mhm, quite the focused look you've got there Captain."

    show sylvian blush at right with move

    show claude sad at center_1left
    show rory at center_left
    with dissolve

    voice "audio/voice/lars/lars_092_take02.ogg"
    Lars "That's right, listen to Master Sylvian. He's practically a mind reader when it comes to picking up on my cues and emotions—way ahead of you!"

    Lars narration "He lets out a light sigh, seemingly contemplating his actions."

    show lars
    Claude "...I suppose. Can't go against our esteemed Captain's wishes."

    show lars
    Claude "But you can't be serious about Master Sylvian reading you better than I do."

    voice "audio/voice/lars/lars_093_take01.ogg"
    show lars blush
    Lars "I am, Master Sylvian has shown genuine care and consideration for my feelings. However, with you, it feels like everything is either taken as a joke or a competition!"

    voice "audio/voice/sylvian/sylvian_055_take03.ogg"
    show sylvian with dissolve
    show lars
    Sylvian "Claude, it's time to stop with the teasing. As the leader of {i}Custodes Sylvae{/i}, I don't want you to do anything that jeopardizes our bond as fellow guild members."

    show claude sad with dissolve
    show lars
    Claude "Hmph, suit yourself {i}Boss{/i}. I'll back off for now."

    show lars
    Claude "But I'll have you know that I'm not giving up anytime soon."

    voice "audio/voice/sylvian/sylvian_056_take03.ogg"
    show sylvian mad with dissolve
    show lars
    Sylvian "Never use someone's weaknesses as a weapon against them, for it reflects your own character more than theirs, Claude."

    show lars serious
    Claude "As much as I {i}adore{/i} your poetry and philosophical quotes, I'll stand my ground when it comes to teasing Captain over here."

    show claude smile with dissolve
    show lars serious
    Claude "You see, it's fun for me to see which of his buttons I can push."

    show lars serious
    Claude "Anyone attempting to be a goody two shoes all the time, like you, is destined for downfall unless they find a way to unleash their deepest desires, {i}Boss{/i}. Maybe even share a secret or two!"

    show sylvian sad with dissolve
    Lars narration "A shadow crosses Master Sylvian's face at Sir Claude's comment, as if a nerve was struck deep within him. The situation seems to be on the verge of getting out of hand, but my curiosity urges me to see how things will unfold."

    show lars serious
    Claude "I would even dare say that you're the one who is harboring the most dangerous inner feelings among all of us. At least, {i}I{/i} can release some steam by having fun with my Captain over here."

    Lars narration "...{i}my{/i} Captain?"

    show lars serious
    Claude "Yet, it seems like flowers are the only companions you can trust your secrets with."

    show lars serious
    Claude "Not to mention, isn't it time for you to admit to [Lars] that you've loved—"

    show sylvian sad at jp
    voice "audio/voice/sylvian/sylvian_057_take02.ogg"
    show lars serious
    Sylvian "{size=*1.25}THAT IS QUITE ENOUGH, CLAUDE!" with vpunch

    voice "audio/voice/sylvian/sylvian_058_take01.ogg"
    show lars serious
    Sylvian "I treasure you as a member of {i}'Custodes Sylvae'{/i}, but your snapdragon of a mouth is intolerable."

    voice "audio/voice/sylvian/sylvian_059_take02.ogg"
    show lars serious
    Sylvian "Gracefully deceptive petals that press together to bloom in deceit. You certainly have a lot to say, but when it comes to revealing things about yourself, you remain as enigmatic as ever."

    voice "audio/voice/sylvian/sylvian_060_take04.ogg"
    show claude shocked with dissolve
    show sylvian serious funny with dissolve 
    show lars serious
    Sylvian "How about revealing the reason behind why you adopted that {i}ambitious{/i} persona of yours? You certainly try to show it off at every occasion, now don't you?"

    show claude shocked at jp
    show lars serious
    Claude "Tsk tsk, outing me like this just because you couldn't handle what I said?"

    show lars serious
    Rory "Uhm, Mentor, I don't understand what's going on here. But can we stop bickering for a second?"

    voice "audio/voice/lars/lars_094_take02.ogg"
    show lars serious
    Lars "Rory's right, it's not like you two to argue like this..."

    show lars serious
    Claude "It seems that some things—"

    voice "audio/voice/sylvian/sylvian_061_take04.ogg"
    show lars serious
    Sylvian "—are overdue for the both of us."

    show sylvian at right
    show claude at center_1left
    show rory at center_left
    with dissolve

    show rory at jp
    Rory "Ahem, we have more important things to do right now."

    jump CS_4_End

label look_back_at_Sir_Claude:

    show lars serious
    Lars narration "I glance at Sir Claude, silently seeking his assistance."

    hide sylvian sad
    hide rory
    with dissolve

    show claude smile at center with move
    show claude blush with dissolve

    Lars narration "He playfully winks, a certain charm in his eyes that's hard to ignore. I'm pretty sure my tail is all ruffled up by the gesture, and who knows what state my cheeks are in right now—they always seem to be in a world of their own."

    show bg_3:
        subpixel True
        linear 2.0 blur 10
    show claude smile at center:
        parallel:
            linear 1.0 yalign -0.1
        parallel:
            linear 3.0 zoom 1.50

    Lars narration "He stretches his hand in my direction, entwining our fingers and pulling me closer until we're touching shoulder to shoulder."

    Claude "Who knows what stage our relationship will reach in the very near future? Am I right, Captain?"

    show bg_3:
        linear 2.0 blur 0
    show claude smile at center:
        parallel:
            linear 1.0 zoom 1.0
        parallel:
            linear 2.0 yalign 0.5
            linear 2.0 ypos 0.5

    Lars narration "As Sir Claude pulls away, releasing my hand, my attention shifts to the impending storm gathering above Master Sylvian's silhouette. His furrowed brows and crossed arms betray a sense of bitterness."

    show claude smile at center_2left
    with move
    show sylvian sad at center_2right
    with dissolve

    Lars narration "To emphasize the point further, delicate hyacinth blossoms, donned in their regal purple hues, frame the brim of his hat. Each subtle shake of his head becomes a silent decree, causing the once-graceful petals to wilt and wither, perfectly reflecting the disappointment etched on his face."

    Lars narration "But why is he looking at me like that?"

    Lars narration "I'm not always on board with Sir Claude's shenanigans, yet, it's often easier to go along with his wishes. He enjoys the challenge, and the excitement of competition makes resisting him seem pointless."

    Lars narration "Master Sylvian knows that as well, so why would he show such an expression?"

    hide sylvian sad with dissolve

    show claude smile at center
    with move
    show lars blush
    Claude "Whether it's the way your cute tail wags around when you start rambling or how your ears perk up while listening to human's tales, I can tell each and every one of them apart."

    Lars narration "His scaly hand traces the contours of my ears. I could feel myself slowly heating up even more; my ears and tail are too sensitive for this."

    show lars blush
    Claude "I don't need magical gimmicks to understand you, Captain. Though, I still enjoy teasing and playfully tugging on the line between us."

    show lars blush
    Claude "But rest assured, I'll turn this line into a strong thread of destiny that will bind us in ways you can never imagine. Nothing is impossible if I put my mind to it, {i}exclusively{/i} for you."

    show claude smile at center_1left 
    with move

    show rory at center_left
    show sylvian sad at right
    with dissolve

    show rory at jp
    Rory "Ahem, we have more important things to do right now."

label CS_4_End:

    Rory "Try to gather the kids while I set everything up at the stall."

    hide rory
    hide claude
    hide sylvian
    with dissolve

    Lars narration "I make my way through the bustling groups of children, intent on grabbing their attention. The excitement in the air is palpable as their laughter and chatter fills the space."

    Lars narration "It's best that I tuck the artifact beneath my equipment for now. Children are easily captivated by shiny objects, and I wouldn't want them accidentally pulling and damaging the necklace."

    Lars narration "I take a deep breath and shout an announcement that echoes through the crowd."

    Lars "{size=*1.25}HEY EVERYONE, I'M BACK!" with vpunch

    Lars "{size=*1.25}THE PUPPET SHOW IS GOING TO START SOON!" with vpunch

    play sound sfx_children_playing loop
    Lars narration "The moment I finish my announcement, I am bombarded by a swarm of children running towards me, their voices rising in a crescendo of excitement. Little hands tug at my sleeves, pulling me in different directions, each child eager to share their thoughts or be part of the upcoming event."

    Lars narration "Amidst the joyful chaos, I can see Sir Claude and Master Sylvian observing from afar, their watchful eyes filled with amusement and a glint of...something else that I can't quite put my finger on."

    scene bg black with fade
    show bg_3 at pan with fade

    "Random Kid 1" "Yay! [Lars] is back from his trip."


    "Random Kid 2" "I missed you, [Lars]; my dragon has been messing with my toys recently. You definitely have to help!"


    "Random Kid 3" "[Lars]! Don't forget we still have our race for the afternoon. You have to help me win, please!"

    Lars "Heh. This takes me back to when I was a kid."

    show bg_3 at end_pan

    stop sound fadeout 1.0

    show sylvian at center
    with moveinright
    
    show lars
    Sylvian "I hope I'm not bothering you in the middle of your task, [Lars]."

    Lars "Of course not Master, this would be the perfect time to show off my skills to you in person. I'm the fastest amongst everyone here after all."

    show claude smile at center_2left
    show sylvian at center_2right
    with move
    
    show lars 
    Claude "Hmm, how typical of our dear Captain to compare himself with mere children."

    Lars "Just a friendly reminder – I can outrun you anytime. It might be a tad embarrassing for someone who sees themselves as the pioneer of all the competitions and challenges in Divonia, wouldn't you say?"

    show claude smile
    show lars
    Claude "You reckon you're fast? Blink, and you'll miss it, Captain. I could have you speechless with my speed, if I so desired."

    Lars "Well, Sir–"

    show claude with dissolve
    show lars
    Claude "And so he coughs again until his lungs give out, {i}wheeze{/i}, and {i}gag{/i}."

    Lars "–Claude, with all that coughing, who's to say if you'll have enough time to catch your breath or not? It's not a race if you're just jogging to the finish line."

    show claude smile with dissolve
    show lars
    Claude "Haha, my dear Captain [Lars], it's more of a dramatic pause for suspense. You know, giving others a chance to catch up and revel in the anticipation of my victory. It's a race with flair!"

    show sylvian at jp
    show lars
    Sylvian "Let's continue on with our work, shall we?"

    Lars narration "Both guild members stand by my side. Sir Claude, with his innate charisma, effortlessly charms the children surrounding us. Meanwhile, Master Sylvian, mesmerizes them with his expertly performed flower magic."

    show claude with dissolve
    show lars
    Claude "Awe, I'll pretend to be hurt, but while we're on the topic, I believe that you have to challenge yourself more."

    show lars
    Claude "You won't be able to show off your talents to anyone when you spend your time with these childish competitions. How will you be able to prove yourself to the elite if you only ever rival with kids?"

    show lars serious
    Lars "Not everything is a contest to prove oneself, Sir Claude."

    show lars
    Lars "Sometimes, I can be content with just playing around and enjoying the moment as is. Isn't that right, Master?"

    show lars
    Sylvian "Success without heart can be empty and hollow, Claude. While I understand you want to distinguish yourself from your family legacy for the sake of your {i}ambitions{/i}, I can't help but worry about the path you're choosing."

    Lars narration "Family legacy..."

    Lars narration "It was certainly true that Sir Claude had the tendency to act out against his family's wishes from time to time but according to the rumor mills, he didn't have a reason to."

    Lars narration "The Dupont family, a lovely couple of lizard descendants, never strived Claude of love and affection. Yet, from time to time, he seemed to entertain the notion of separating himself from them, as if he were born from a nameless hermaphrodite, and all he ever was is 'Claude,' not a 'Dupont.'"

    show lars
    Sylvian "Pursuing rivalry solely to prove your self-worth to unfamiliar faces is a fleeting pursuit. In time, the present will slip away from your grasp."

    show claude serious with dissolve
    show sylvian sad with dissolve
    
    show lars
    Claude "With all due respect {i}Boss{/i}, but, isn't that lack of ambition precisely why you're here with us today instead of boasting around the academia halls?"

    show lars
    Claude "While I appreciate your presence in our guild and your support for my endeavors, it seems you've relinquished all your desires, merely allowing yourself to be carried along by the whims of your flowery path."

    show claude smile with dissolve
    Claude "But, you see, if you're not determined about your dreams, someone else could come and snatch it right out of your hands."

    Lars narration "I catch Sir Claude throwing a peek at me but he quickly switches his focus back to Master Sylvian."

    Lars narration "When it came to dreams, Master Sylvian had garnered quite the reputation as the {i}Genius of the Century{/i} during his tenure at the Tower of Magicians in Divonia."

    Lars narration "Although he rarely spoke about his past experiences, a glimpse into his emotions could be seen in the way his feathers drooped and his shoulders slumped with a sense of dejection whenever the topic came up."

    Lars narration "Even his perpetual hunched posture served as a constant reminder of his time as a prestigious state magician. A time where he would work himself to the bone day and night with no rest in between."

    Lars narration "Despite his current focus on flower magic, it was evident that Master Sylvian had a different area of expertise in the past. The secrets and stories behind his prior magic remained locked away, untold."

    Lars narration "Not to mention, the formation of our guild seemed to be a deliberate decision he made in response to his experiences as an academician, though he seldom delves into the specifics."

    show lars serious
    Claude "It's in the very motto of {i}Custodes Sylvae{/i} after all."

    show lars serious
    Claude "{i}Discere, cogitare, agere—{/i} the triad of wisdom. Learning enriches the mind, and thinking sharpens it, but it is through action that we truly manifest our knowledge and shape our reality."

    show lars serious
    Claude "Looks like you're stumbling on that third step."

    show lars serious
    Claude "Isn't that right, Captain?"

    show lars serious
    Lars "..."

    show lars serious
    Sylvian "Your statements hold grains of truth, Claude."

    show lars serious
    Sylvian "Without love or ambition, our lives languish in the shadows of mediocrity."

    show lars serious
    Sylvian "They ignite the fire within, propelling us to venture beyond our limits, to dream and to create, shaping a life of purpose and fulfillment."

    show lars serious
    Claude "So, you do agree—"

    hide claude smile
    hide sylvian sad
    with dissolve

    show claude_sylvian_fight with dissolve

    Sylvian "However..."

    Sylvian "Amidst our pursuit of them, let us not overlook the tranquility of mediocrity."

    Sylvian "For not every path must lead to grand creations or extraordinary feats."

    Sylvian "In embracing simplicity, we find contentment, and in cherishing the ordinary, we discover the beauty of a life unburdened by the pressures of relentless ambition."

    Claude "Aren't you only saying that because you were burnt out and having nothing else to pursue?"

    Claude "If you always treasured this so-called {i}contentment{/i} why did you decide to spread your name onto society as the top academic of Divonia?"

    Claude "You could have simply stuck to the bottom ranks and let your life aimlessly pass by without ever achieving something or dare I say - {i}fall in love{/i}."

    hide claude_sylvian_fight with dissolve

    show claude serious at center_2left
    show sylvian sad at center_2right
    with dissolve

    if options["CS3"]==1:

        show lars sad
        Lars "What's he talking about, Master?"

        show lars sad
        Lars "Is that part of the secret you wanted to tell me? That you were in love with someone else? Then, what about the mixed signals that I've been receiving from you so far?"

        show sylvian blush with dissolve
        Sylvian "N-no, you're misunderstanding something here— I-I mean, not you. It's probably my fault here, but—"

        show lars sad
        Lars "I don't want to sound conceited, but if I were the person you're in love with, I'd like to think that you would have told me about it by now."

        show lars sad
        Lars "But then again, you're secretive about your history as well..."

        show sylvian sad with dissolve
        Sylvian "I'm sorry but I can't tell you any more about it with Claude here."



    if options["CS3"]==2:

        Lars "I've been so busy with Sir Claude that I didn't even notice. You've fallen for someone, Master?"

        Lars "That's exciting! When are you going to introduce us?"



    show claude serious
    show sylvian 
    with dissolve
    Claude "Focus here Captain, we can talk about that later. Unless you've already taken someone's side in this discussion?"

    show lars
    Lars "Uhm, you're both people that I deeply admire and I don't really want to—"

    show claude shocked with dissolve
    show lars
    Claude "Don't want to? I expect you to at least share your personal opinion if you share the sentiment of {i}taking no sides{/i}."

    show lars
    Sylvian "Pay him no mind, [Lars], he's just upset for himself."

    Lars narration "What do I do now?"

    menu:
        " " " "
        "{size=*0.80}Agree with Master Sylvian about valuing our current contentment{/size}":
            $ options["CS5"]=1
            jump agree_with_Master_Sylvian

        "{size=*0.80}Agree with Sir Claude about the positive value of ambition{/size}":
            $ options["CS5"]=2
            jump agree_with_Sir_Claude


label agree_with_Master_Sylvian:

    show sylvian
    show claude serious
    with dissolve

    voice "audio/voice/lars/lars_096_take01.ogg"
    Lars "I agree with Master Sylvian."

    Lars "I think what he says is true about enjoying what we want instead of simply going after something for the challenge."

    Lars "I like hanging out with my dragons even if we aren't in the middle of an expedition or mission and I wouldn't change my relationship with them for the world."

    Lars "Going after artifact hunts and transporting passengers without an ounce of love seems depressing to me."

    voice "audio/voice/sylvian/sylvian_062_take03.ogg"
    show lars
    Sylvian "Phew, thankfully, Claude's influence hasn't rubbed off on you too much."

    voice "audio/voice/sylvian/sylvian_063_take02.ogg"
    show sylvian blush with dissolve
    show lars
    Sylvian "I'm always impressed by how well you articulate your words, my dear junior. Perhaps we can delve into these philosophies and {i}other matters{/i} when we find some time to ourselves later."

    voice "audio/voice/lars/lars_099_take01.ogg"
    show sylvian sad with dissolve
    show lars blush
    Lars "I would love to spend time with you but Spotsy needs me more after we're done with this, don't you think so?"

    voice "audio/voice/lars/lars_100_take02.ogg"
    Lars "She's had a long flight after all and I'm the only person who can take care of her."

    voice "audio/voice/sylvian/sylvian_064_take02.ogg"
    show lars
    Sylvian "I can't deny that I am a bit disappointed..."

    voice "audio/voice/sylvian/sylvian_065_take03.ogg"
    show sylvian with dissolve
    show lars blush
    Sylvian "However, it's one of the things that I like seeing you do, [Lars]."

    voice "audio/voice/sylvian/sylvian_066_take03.ogg"
    show lars blush
    Sylvian "It's amongst my wishes to someday be a recipient of the same adoration you hold for your dragons."

    voice "audio/voice/lars/lars_101_take01.ogg"
    show lars blush
    Lars "What do you—"

    show claude with dissolve
    show sylvian with dissolve

    jump CS_5_End

label agree_with_Sir_Claude:

    show claude smile
    show sylvian sad
    with dissolve

    voice "audio/voice/lars/lars_102_take01.ogg"
    Lars "I agree with what Sir Claude says."

    Lars "It's not fair to avoid fighting for what you love and letting it slip out of your reach."

    Lars "I could admire my dragons all day and night but if I never take that leap of fate to touch them and show them my feelings directly, then I'll only ever be walking in a circle."

    Lars "I also can't imagine going a day without learning about the new dragon species out there."

    show claude blush with dissolve
    show lars blush
    Claude "Glad to see that you've learnt a few things about my motto of life, Captain. It's not complete, but I'll teach more later, {i}in private{/i}."

    voice "audio/voice/lars/lars_099_take01.ogg"
    show lars blush
    Lars "I would love to spend time with you but Spotsy needs me more after we're done with this, don't you think so?"

    voice "audio/voice/lars/lars_100_take02.ogg"
    show lars blush
    Lars "She's had a long flight after all and I'm the only person who can take care of her."

    show lars blush
    Claude "At this rate, I don't think I'll ever be able to compete with your love for dragons, Captain. But I'll do my best to win you over, and spoil you rotten the same way you do for your dragons."

    show lars blush
    Lars "What do you—"

    show claude with dissolve
    show sylvian with dissolve

label CS_5_End:

    show claude at center_1left 
    show sylvian at right
    with move

    show rory at center_left 
    with dissolve


    show rory at jp
    show lars
    Rory "Guys, why isn't anyone coming? Where are the kids?"

    Lars narration "Rory suddenly approaches with a faint trace of concern etched on her face."

    show lars
    Lars "Ah, I gathered them all here!"

    show lars serious
    Lars "...see?"

    play music "track_4_time_stop.ogg" fadeout 2.0 fadein 2.0

    Lars narration "It's such an eerie scene...the children, once animated, have now come to an abrupt standstill, their vibrant expressions frozen in unnatural stillness."

    Lars narration "A surreal silence blankets not just them but everyone around us; it appears as though the world beyond our group has been caught in the grips of time."

    Lars narration "The once-bustling atmosphere has dissipated, replaced by an unsettling quietude."

    show sylvian serious funny
    show rory angry
    show claude shocked
    with dissolve

    show lars serious
    Rory "Is this a joke? Was there a surprise flash mob that I wasn't aware of?"

    show rory angry with dissolve
    show lars serious
    Rory "{bt}{size=*2.0}Claudyyyyyy.{/bt}" with vpunch

    show lars serious
    Rory "Bribing children to pull pranks on me again, eh?"

    show lars serious
    Claude "As much as I would love to take credit for such an event, I have no clue what's happening either."

    show lars serious
    Sylvian "A strange phenomenon is happening, it seems."

    show lars serious
    Lars "What do you think is going on, Master?"

    Lars narration "Acting on instinct, my hand reaches out, grasping at the figures frozen in time, attempting to break the eerie stillness that envelops them. I shake them gently, yet with a growing sense of urgency, hoping to shatter the rigid spell that holds them captive."

    Lars narration "Alas, my efforts yield no response, and the unnatural stillness persists,"

    show lars sad
    Lars "Kids, come on. We're getting really worried over here. Why're you standing frozen like this?"

    show claude serious with dissolve
    show lars sad
    Claude "What could have suddenly happened? Everything was fine up until a few minutes ago."

    Lars narration "In the midst of my attempts to shake off the statues, a peculiar sensation courses through me."

    hide rory
    hide sylvian
    hide claude
    with dissolve

    show normal_necklace 
    with dissolve

    show blink_necklace
    with dissolve

    Lars "The necklace I'm wearing grows warmer, its temperature gradually rising. Intrigued and compelled, I shift my attention towards it. It appears Rory has noticed it too."

    show lars
    Rory "Hold up! What's happening to the artifact right now? Take a look."

    Lars "Instantly, everyone's gaze fixates on me."

    show lars
    Rory "It's blinking and shining like crazy! Do you think it has something to do with what's going on? Maybe a weird spell that suddenly got activated?"

    show lars
    Rory "It's as if we're the only people moving and everyone else is frozen in time. Don't you find it weird?"

    show lars
    Rory "What's going on, Mentor? Can't you do something about this?"

    show lars
    Claude "Calm down little Rory—"

    show lars
    Rory "Claude, what the heck did you bring with yourself?! If anything goes wrong, I'm holding you responsible!"

    show lars
    Claude "..."

    hide blink_necklace
    hide normal_necklace 
    with dissolve

    show sylvian serious funny at right 
    show rory angry at center_left 
    show claude serious at center_1left  
    with dissolve
    
    show lars serious
    Sylvian "I have only ever heard of one artifact having the ability to do such a thing. Remember the one we talked about when we first opened the box?"

    show lars serious
    Sylvian "However, the color of the gem in our necklace is different from that I remember."

    show lars serious
    Sylvian "Even then, why would such a thing happen so suddenly?"

    show lars serious
    Claude "I didn't hear about an effect like this from the merchant either, there was no mention of it when they handed over the artifact to me. I couldn't have been duped like this, that's simply impossible—"

    show lars sad
    Lars "What do we do now? What's going to happen to them?"

    show sylvian
    show lars sad
    Sylvian "Steadfast everyone, calm yourselves down." with vpunch

    show rory
    show claude
    with dissolve

    show lars
    Sylvian "The brave person is not the one who feels no fear, but the one who conquers that fear. Let's do our best to figure this out."

    show lars
    Lars "Me too! I'm the strongest one among us, I'll try to protect us in case something goes south."

    show claude shocked with dissolve
    show lars serious
    Claude "Wait! Can anyone else see that shadow over there?"

    Lars narration "It appears Sir Claude spotted an approaching figure before any of us did, courtesy of his lizard-sharp eyesight."

    show sylvian serious funny with dissolve
    show lars serious
    Claude "I think that it's watching us. Stay on guard."

    Lars narration "As the tension in the air grows, I sense the presence of an unknown observer. It sends a chill down my spine, and I can feel my ears perk up."

    Lars narration "A bead of sweat rolls down my forehead, and my ginger fur seems to prickle, almost as if it senses the imminent danger and excitement that lay ahead."

    show claude serious with dissolve
    voice "audio/voice/zephyr/zephyr_001_take01.ogg"
    show lars serious
    $ zephyr_name = "Unknown"
    Zephyr "Looks like some interesting Divs have entered my domain while I was occupied."

    $ renpy.choice_for_skipping()
    show rory:
        linear 1.5 xalign 1.05
    show claude serious as clonclaude:
        yalign 1.0
        linear 0.25 alpha 0.0
    show claude serious:
        yalign 1.0
        xalign 0.0 
        xzoom -1.0
        alpha 0.0
        linear 0.25 alpha 1.0
        pause 0.25
        linear 1.0 xalign 0.5
    show sylvian serious funny:
        linear 1.5 xalign 0.7
    
    show zephyr happy:
        xalign -1.0
        linear 1.5 xalign 0.0

    voice "audio/voice/zephyr/zephyr_002_take01.ogg"
    show lars serious
    $ zephyr_name = "Unknown"
    Zephyr "I was frozen in anticipation for what would come next, but I have work to do after this. My castle isn't going to clean up after itself!"

    show zephyr happy at jp
    voice "audio/voice/zephyr/zephyr_003_take02.ogg"
    $ zephyr_name = "Unknown"
    Zephyr "Get it? {i}frozen in anticipation{/i}. {bt}Hehehehehe~{/bt}"

    show sylvian serious funny at center_left
    show claude serious at center_2right:
        xzoom -1
    with move

    show zephyr happy:
        linear 0.5 xalign -0.2
        linear 1.75 xalign 0.0

    Lars narration "In an instant, Master Sylvian's incantation casts a protective shield of varying blooms and plants around us, shimmering with the combined energies of crystalline dews."

    show zephyr happy:
        xalign 0
        yalign 0
    
    Lars narration "Even with the shield in place, my predator instincts stay sharp. The tension in the air is palpable, and I'm acutely aware of the figure's every move. Time seems to slow down as I focus intently on its enigmatic presence, poised to react if any threat arises."

    show rory angry with dissolve
    Lars narration "With Rory by my side, her cutting tools poised for self-defense, we form a united front against the unknown creature."

    show sylvian serious funny at center_right
    show claude serious at center_left
    show rory angry at right
    with move

    Lars narration "Sir Claude, ever bold and quick-witted, leaps forward to question the puzzling figure."
    
    show lars serious
    Claude "Who's there? Are you the person behind this? What's—"

    voice "audio/voice/zephyr/zephyr_004_take01.ogg"
    show lars serious
    $ zephyr_name = "Unknown"
    Zephyr "Slow doooown there."
    
    voice "audio/voice/zephyr/zephyr_005_take02.ogg"
    show lars serious
    $ zephyr_name = "Unknown"
    Zephyr "Times not running away after all. You know?"

    show lars serious
    Sylvian "..."

    show lars serious
    Lars "..."

    show lars serious
    Claude "..."

    voice "audio/voice/rory/rory_022_take03.ogg"
    show rory with dissolve
    show lars serious
    Rory "Heh—"

    show zephyr sad with dissolve
    show zephyr sad at jp
    voice "audio/voice/zephyr/zephyr_006_take02.ogg"
    show lars serious
    $ zephyr_name = "Unknown"
    Zephyr "{size=*2.0} DON'T JUDGE ME!" with vpunch

    voice "audio/voice/rory/rory_023_take01.ogg"
    show lars serious
    Rory "Too late for that now."

    show zephyr with dissolve:
        xalign 0
        yalign 0
    
    voice "audio/voice/zephyr/zephyr_007_take02.ogg"
    $ zephyr_name = "Unknown"
    Zephyr "After all, it's been some time since I could speak with someone without them being brainwashed or stuck in time."

    voice "audio/voice/lars/lars_110_take02.ogg"
    Lars "Huh? What're you talking about?"

    show zephyr happy at shake
    voice "audio/voice/zephyr/zephyr_008_take02.ogg"
    show lars serious
    $ zephyr_name = "Unknown"
    Zephyr "Ah, the inquisitive one speaks. Hmm, I'll call you Scouty from now on since you look the part as well."

    voice "audio/voice/lars/lars_111_take01.ogg"
    Lars "My name is [Lars], not Scouty!"

    voice "audio/voice/zephyr/zephyr_009_take01.ogg"
    show lars serious
    $ zephyr_name = "Unknown"
    Zephyr "My brain cells will only acknowledge you as Scouty from here on out."

    voice "audio/voice/zephyr/zephyr_010_take02.ogg"
    show lars serious
    $ zephyr_name = "Unknown"
    Zephyr "You're all destined to be new additions to my castle renovation army, so sparing the effort of using two names at once seems reasonable."

    Lars narration "But you only have to remember one, which is {i}[Lars]{/i}! But who knows what may happen if I say that outloud."

    voice "audio/voice/zephyr/zephyr_011_take02.ogg"
    show lars serious
    $ zephyr_name = "Unknown"
    Zephyr "Well, let's see who else we have in this riveting cohort. I'm sure your names are all yawn-inducing, but let's make this roll call fun, shall we?"

    show zephyr at jp
    voice "audio/voice/zephyr/zephyr_012_take01.ogg"
    show lars serious
    $ zephyr_name = "Unknown"
    Zephyr "You, the one with the flowery hat, must be the smart one in the group since you haven't interrupted me so far. I'll call you Smarty from now on."

    show zephyr:
        zoom 1.0

    voice "audio/voice/zephyr/zephyr_013_take02.ogg"
    show lars serious
    $ zephyr_name = "Unknown"
    Zephyr "But be careful not to interject too much like Scouty."

    voice "audio/voice/lars/lars_113_take02.ogg"
    show lars serious
    Lars "But how is that even related to what I asked—"

    show claude shocked with dissolve
    show lars serious
    Claude "Hey now, when did I—"

    show rory angry with dissolve
    show rory angry at jp
    show claude shocked at jp

    show rory angry:
        zoom 1.0

    show claude shocked:
        zoom 1.0

    voice "audio/voice/rory/rory_024_take02.ogg"
    show lars serious
    Rory "—ever interrupt you?" with vpunch

    show zephyr sad with dissolve
    show zephyr sad at shake
    voice "audio/voice/zephyr/zephyr_014_take02.ogg"
    show lars serious
    $ zephyr_name = "Unknown"
    Zephyr "Scouty, and the other two, I need my main character moment over here, stop blabbering so much."

    Lars narration "I take a deep breath, frustration bubbling up within me as I watch the scene unfold. The figure's words are becoming increasingly difficult to make sense of."

    Lars narration "I glance at my companions, hoping someone will step up and challenge their nonsensical monologue. We can't afford to let them dominate the conversation."

    Lars narration "Come on, someone has to say something."

    show zephyr with dissolve
    voice "audio/voice/zephyr/zephyr_015_take01.ogg"
    show lars serious
    $ zephyr_name = "Unknown"
    Zephyr "As I was saying—"

    show sylvian serious funny at jp
    voice "audio/voice/sylvian/sylvian_067_take01.ogg"
    show lars serious
    Sylvian "Enough banter, who exactly are you?"

    show sylvian serious funny:
        zoom 1.0

    Lars narration "Relief washes over me as Master Sylvian speaks up."

    voice "audio/voice/sylvian/sylvian_068_take03.ogg"
    show sylvian serious funny at center_right
    show lars serious
    Sylvian "State the truth, or you'll face the consequences. I prefer not to harm others, but I'll do what needs to be done as the leader."

    play sound sfx_clap
    Lars narration "Suddenly, the sound of a single clap pierces through the stillness. It's a sharp and commanding sound, one that demands our attention."

    voice "audio/voice/zephyr/zephyr_016_take01.ogg"
    show lars serious
    $ zephyr_name = "Unknown"
    Zephyr "Impressive words, especially considering your current disadvantage but I'll humor you this time."

    voice "audio/voice/zephyr/zephyr_017_take01.ogg"
    show lars serious
    $ zephyr_name = "Unknown"
    Zephyr "Since Smarty asked, it's time for the cliché introduction séance, the kind they do for video games and TV shows."

    voice "audio/voice/zephyr/zephyr_018_take01.ogg"
    show lars serious
    $ zephyr_name = "Unknown"
    Zephyr "Hopefully, they spared no expense in making me the fairest of them all. A little extra villainous charm never hurt anyone~"

    voice "audio/voice/zephyr/zephyr_019_take02.ogg"
    show lars serious
    $ zephyr_name = "Unknown"
    Zephyr "But before that, you'd better cease all your magical theatrics and weapon brandishing if you don't want me to lose interest in this little charade."

    Lars narration "Gradually, Master Sylvian begins to dismantle the defensive walls he had erected, and Rory and I, in sync, follow suit. Hopefully, that's the right choice to make for now."

    show rory at right
    show sylvian at center_right
    show claude at center_left
    with dissolve

    voice "audio/voice/zephyr/zephyr_020_take02.ogg"
    show lars 
    $ zephyr_name = "Unknown"
    Zephyr "Anyway, you can address me as the {i}“Omniscient Lord of Bankruptcy”{/i} or if it's easier on the tongue, the {i}“Malevolent Architect of Debt”{/i}. Personally, I'm partial to the latter title—it aligns better with my aspirations."

    $ zephyr_name = "Zephyr"
    show lars 
    Lars "Uhm, does that mean that you cause bankruptcy or that you're the literal embodiment of bankruptcy?"

    voice "audio/voice/rory/rory_025_take02.ogg"
    show lars 
    Rory "Do you design debt plans to bankrupt others or are you so bankrupt that you're already knee-deep in the debt plan already?"

    voice "audio/voice/rory/rory_026_take02.ogg"
    show lars 
    Rory "But then again, I can't see if you have knees or not."

    voice "audio/voice/sylvian/sylvian_069_take03.ogg"
    show lars 
    Sylvian "I don't think that's an issue we need to be discussing right now, my dear juniors."

    show zephyr sad with dissolve
    show zephyr sad at shake
    voice "audio/voice/zephyr/zephyr_021_take02.ogg"
    show lars 
    "{size=36}{color=#CD4EDD}Malevolent Architect of Debt{/size}" "Ahhh, keep quiet for a second! I'm not used to talking this much. If it weren't for you meddling Divs, I would have gotten away with my grandiose plan already."

    voice "audio/voice/rory/rory_027_take03.ogg"
    show lars 
    Rory "Somehow, I really doubt that you'd be capable of doing something like that."

    voice "audio/voice/zephyr/zephyr_022_take02.ogg"
    show lars 
    "{size=36}{color=#CD4EDD}Malevolent Architect of Debt{/size}" "Hmph, don't underestimate me. I could wipe your minds clean right now since you've already heard my voice, and even learnt of my grandiose plan —though not completely— and what else..."

    voice "audio/voice/zephyr/zephyr_023_take01.ogg"
    show lars 
    "{size=36}{color=#CD4EDD}Malevolent Architect of Debt{/size}" "You're probably going to learn of my real name which is Zephyr, but anyway—"

    voice "audio/voice/rory/rory_028_take02.ogg"
    show lars 
    Rory "Isn't this the same case of yelling out your attack name before it's your turn to fight?"

    Lars narration "We're spending too much time here; I need to take a proactive approach and ask him some questions myself before anything bad happens to everyone else who's been frozen."

    play music "track_5_zephyr_theme.ogg" fadeout 2.0 fadein 2.0

    $ choice_g1[0] = 0
label menu_g1:
    if (choice_g1[0] and choice_g1[1]):
        jump G_1_End
    
    menu:
        " " " "
        "{size=*0.88}Are you the person responsible for freezing everyone?{/size}" if choice_g1[0]==0:
            $ options["G1"]=1
            $ choice_g1[0] = 1
            jump are_you_the_person

        "{size=*0.88}How come you're freezing everyone for a castle renovation?{/size}" if choice_g1[1]==0:
            $ options["G1"]=2
            $ choice_g1[1] = 1
            jump how_come_you


label are_you_the_person:

    show sylvian
    show claude
    show zephyr 
    with dissolve

    voice "audio/voice/lars/lars_114_take02.ogg"
    show lars serious
    Lars "Are you the person responsible for this?"

    show rory at jp
    voice "audio/voice/rory/rory_029_take01.ogg"
    show lars serious
    Rory "Come on, [Lars]! He can't actually lack that many brain cells to spell out his plan like that—"

    show zephyr at shake
    voice "audio/voice/zephyr/zephyr_024_take02.ogg"
    show lars serious
    Zephyr "Exactly what do I get in exchange for all this talking and sharing my top-secret agenda? Huh?"

    show claude smile with dissolve
    show lars serious
    Claude "I'm sure we can reach a compromise if we settle this down like proper negotiators. Threatening someone won't get you on their side, after all. It will only provoke them to attack."

    voice "audio/voice/zephyr/zephyr_025_take01.ogg"
    show lars serious
    Zephyr "Hmph, you're quite the silver-tongue, aren't you?"

    voice "audio/voice/zephyr/zephyr_026_take02.ogg"
    show lars serious
    Zephyr "I'll call you Slicky from now on to match those lizard descendent traits of yours since you think you're so—"

    show lars serious
    Claude "Shadowy figure, calls himself weird titles for attention, keeps talking about freezing time and brainwashing everyone. I think it's fairly obvious we have a deal-breaking villain on our hands. Unless you're not actually the person behind this."

    show zephyr at shake
    voice "audio/voice/zephyr/zephyr_027_take01.ogg"
    show lars serious
    Zephyr "Of course, I am! I wouldn't brandish my family name with such buffoonery if I didn't have a grandiose endgame in mind."

    show lars serious
    Claude "Are you sure about that? Maybe you're just a random kid messing with some kind of weird spell?"

    show zephyr sad with dissolve

    show zephyr sad at jp
    voice "audio/voice/zephyr/zephyr_028_take01.ogg"
    show lars serious
    Zephyr "K-K-Kid?! I'm older than all of you combined! I mean, I've been sleeping for a few centuries but ugh that's not the point! Let me start from the beginning since you're so quick to make me out to be a low-class villain, Slicky." with vpunch

    show lars serious
    Claude "So you're not a villain?"

    show zephyr with dissolve
    voice "audio/voice/zephyr/zephyr_029_take02.ogg"
    show lars serious
    Zephyr "Of course, I'm not; I'm the maestro of mischief, the virtuoso of vexation, the puppeteer of pandemonium, the curator of calamity, pulling strings to unveil the grand tapestry of turmoil—"

    show lars serious
    show claude serious with dissolve
    Claude "Okay, okay, we get it! Now on to answering the question."

    voice "audio/voice/zephyr/zephyr_030_take02.ogg"
    show lars serious
    Zephyr "Quite the impatient one, aren't you Slicky?"

    voice "audio/voice/zephyr/zephyr_031_take01.ogg"
    show lars serious
    Zephyr "You see, my family has had this unique time freezing artifact for quite a few generations now. We'd have the responsibility of using it to maintain order and peace in the land as noble dragon descendants of the house of— well, never mind that for now."

    show zephyr at jp
    voice "audio/voice/zephyr/zephyr_032_take02.ogg"
    show lars serious
    Zephyr "You don't need to know the details."

    show zephyr:
        zoom 1.0

    show rory at shake
    voice "audio/voice/rory/rory_030_take02.ogg"
    show lars serious
    Rory "Seems like we have a delusional con-artist here."

    voice "audio/voice/zephyr/zephyr_033_take02.ogg"
    show zephyr sad with dissolve
    show lars serious
    Zephyr "I'm not lying!"

    voice "audio/voice/rory/rory_031_take03.ogg"
    show rory angry with dissolve
    show lars serious
    Rory "You're clearly not using it responsibly, now, are you?"

    voice "audio/voice/zephyr/zephyr_034_take01.ogg"
    show zephyr happy with dissolve
    show lars serious
    Zephyr "Hold on there, bull woman, unless you want to be called Speedy or—"

    show claude smile with dissolve
    show lars serious
    Claude "I insist you call her Smally, since she fits the size standard."

    show rory angry at jp
    voice "audio/voice/rory/rory_032_take01.ogg"
    show lars serious
    Rory "Ernest Jones called from Earth and said he wants his god complex back."

    voice "audio/voice/zephyr/zephyr_035_take02.ogg"
    show zephyr sad with dissolve
    show lars serious
    Zephyr "Quit trying to shadow my lore explanation, you two." with vpunch

    voice "audio/voice/rory/rory_033_take03.ogg"
    show rory with dissolve
    show lars serious
    Rory "Hehe, {i}shadow...{/i}"

    voice "audio/voice/zephyr/zephyr_036_take01.ogg"
    show zephyr happy with dissolve
    show lars serious
    Zephyr "I've decided to use the artifact for my personal gain since my present situation calls for it. But it'll all be worth it when my castle is renovated."

    voice "audio/voice/sylvian/sylvian_070_take04.ogg'"
    show sylvian serious funny with dissolve
    show lars serious
    Sylvian "Were there never any countermeasures set up in the case of someone misusing the artifact?"

    voice "audio/voice/rory/rory_034_take01.ogg"
    show lars serious
    Rory "Mentor, shouldn't we use some discretion here?"

    voice "audio/voice/zephyr/zephyr_037_take01.ogg"
    show lars serious
    Zephyr "Should we ever deviate from our path and misuse it, the paired artifact would counteract the spell. Anyone who touches it would be immune to the artifact's magic."

    voice "audio/voice/zephyr/zephyr_038_take02.ogg"
    show lars serious
    Zephyr "Basically, the same necklace but with a different colored gemstone and the opposite ability—"

    show claude shocked with dissolve

    show sylvian serious funny at jp
    show claude shocked at jp
    show rory at jp

    voice "audio/voice/sylvian/sylvian_071_take02.ogg"
    show lars serious
    Sylvian "...Did you say, it was a necklace with a gemstone?"

    voice "audio/voice/zephyr/zephyr_039_take02.ogg"
    show zephyr at shake
    show lars serious
    Zephyr "Hmm, yeah, what about it?"

    show zephyr:
        zoom 1.0

    voice "audio/voice/sylvian/sylvian_072_take02.ogg"
    show lars serious
    Sylvian "Out of curiosity, where is that artifact now?"

    voice "audio/voice/zephyr/zephyr_040_take02.ogg"
    show lars serious
    Zephyr "I'm not an all-knowing encyclopedia, now am I? I have no clue about its current whereabouts. It might have been pilfered while I was in my centuries-long slumber; it wasn't there when I woke up."

    voice "audio/voice/zephyr/zephyr_041_take01.ogg"
    show zephyr sad with dissolve
    show lars serious
    Zephyr "Hmph, it's not like you'll believe me anyways."

    voice "audio/voice/lars/lars_115_take02.ogg"
    show lars
    Lars "Come on, we're listening to your story right now, aren't we?"

    voice "audio/voice/zephyr/zephyr_042_take02.ogg"
    show lars
    Zephyr "I've tried to convince so many people till now, human and descendent alike."

    voice "audio/voice/zephyr/zephyr_043_take02.ogg"
    show lars
    Zephyr "What makes your group so special?"

    voice "audio/voice/zephyr/zephyr_044_take02.ogg"
    show lars
    Zephyr "You know what? Forget it."

    jump menu_g1

label how_come_you:

    show claude
    show sylvian
    show zephyr sad 
    with dissolve

    voice "audio/voice/zephyr/zephyr_045_take02.ogg"
    show lars serious
    Zephyr "Well, I've been sleeping for a few centuries now. When I finally woke up, there was no one around, and I found myself in the form of a ghost-like creature."

    voice "audio/voice/zephyr/zephyr_046_take02.ogg"
    show lars serious
    Zephyr "My castle, once grand, had turned into a complete wreck. To make matters worse, not a trace of gold was left!"

    voice "audio/voice/zephyr/zephyr_047_take02.ogg"
    show lars serious
    Zephyr "Countless generations of descendants faithfully served us during my decades of wakefulness. However, upon reopening my eyes, not a single soul lingered."

    show rory at jp
    voice "audio/voice/rory/rory_035_take02.ogg"
    show lars serious
    Rory "Is that why you settled on the title of “Omniscient Lord of Bankruptcy”? Then why would you need two titles like “Malevolent Architect of Debt”?"

    voice "audio/voice/zephyr/zephyr_048_take02.ogg"
    show zephyr happy with dissolve
    show lars serious
    Zephyr "Shush, you can't cut in while I'm laying down my sob story." with vpunch

    voice "audio/voice/zephyr/zephyr_049_take02.ogg"
    show zephyr sad with dissolve
    show lars serious
    Zephyr "Like I said, I couldn't find anyone and the castle was completely empty."

    voice "audio/voice/zephyr/zephyr_050_take01.ogg"
    show lars serious
    Zephyr "I searched for so many days but to no avail, I thought that instead of searching, I should start waiting instead. But who could even recognize our family castle with its broken-down state?"

    voice "audio/voice/zephyr/zephyr_051_take02.ogg"
    show lars serious
    Zephyr "Eventually, I decided to hire some descendants to work on restoring my castle to a somewhat presentable state. Yet, to my disbelief, after just a few days, they had the audacity to demand compensation."

    voice "audio/voice/zephyr/zephyr_052_take01.ogg"
    show lars serious
    Zephyr "Can you fathom such impertinence?"

    show claude shocked with dissolve
    show lars serious
    Claude "But how could you? No money, no family, not even a proper place to sleep in, you'd be knee-deep in debt by this point if you decided to hire people."

    voice "audio/voice/zephyr/zephyr_053_take02.ogg"
    show lars serious
    Zephyr "T-That's ugh...totally—not what happened. Hahaha..."

    show lars serious
    "Everyone" "So, that's what happened, isn't it?"

    voice "audio/voice/zephyr/zephyr_054_take02.ogg"
    show lars serious
    Zephyr "They didn't believe me when I said I was a noble dragon descendent so it was no use appealing to their loyalty."

    voice "audio/voice/rory/rory_036_take02.ogg"
    show lars serious
    Rory "I mean, I hardly blame them at this point."

    show lars serious
    Claude "Long story short, you just wanted free labor."

    show lars serious
    Claude "We're past the stage of paying others with exposure and influencer points, you know?"

    show claude smile with dissolve
    show lars serious
    Claude "Unless it's me that does it, because they're getting their gold's worth and so much more."

    voice "audio/voice/zephyr/zephyr_055_take01.ogg"
    show lars serious
    Zephyr "Stop cutting in, you two! Take a cue from Smarty over there and learn to be a bit more silent."

    voice "audio/voice/rory/rory_037_take02.ogg"
    show lars serious
    Rory "How much longer is this going to take? Can we skip this?"

    show zephyr at jp
    voice "audio/voice/zephyr/zephyr_056_take01.ogg"
    show lars serious
    Zephyr "{size=*1.25}DON'T! PLEASE!{size=*1.0} I'm reaching the good part of the story after all." with vpunch

    voice "audio/voice/zephyr/zephyr_057_take02.ogg"
    show lars serious
    Zephyr "Ahem! So, instead of finding descendants looking for compensation, I decided to hire newly transported humans!"

    Lars narration "HE DID WHAT???"
    
    show sylvian serious funny
    show claude shocked
    with dissolve

    show sylvian serious funny at jp
    show rory at jp
    show claude shocked at jp

    show zephyr at shake
    voice "audio/voice/zephyr/zephyr_058_take01.ogg"
    show lars serious
    Zephyr "Genius idea, I know. They wouldn't have any qualms for gold either since they don't understand the mechanics of this realm yet."

    voice "audio/voice/zephyr/zephyr_059_take02.ogg"
    show lars serious
    Zephyr "Bonus points, they also easily accepted how I'm a noble and that I could give them positions in my castle as soon as it was renovated."

    voice "audio/voice/zephyr/zephyr_060_take02.ogg"
    show lars serious
    Zephyr "I need a proper place to rest after all and a castle of that size needs regular maintenance."

    voice "audio/voice/sylvian/sylvian_073_take01.ogg"
    show lars serious
    Sylvian "You keep mentioning your castle and innocently slaving away unknowing humans. But where is this castle of yours? None of my maps, scrolls, or academic documents have ever pointed to the existence of a secret and perished household like the one you're describing."

    voice "audio/voice/sylvian/sylvian_074_take01.ogg"
    show lars serious
    Sylvian "Not to mention, how does that even result in your usage of an artifact to freeze time?"

    show claude serious with dissolve
    show lars serious
    Claude "That's right! We've been walking around this issue for some time now and we haven't learnt one single coherent thing from you. Just bits and pieces that aren't helping us get out of this mess. Maybe you're just a minion for someone else's plan—"

    voice "audio/voice/zephyr/zephyr_061_take02.ogg"
    show zephyr sad with dissolve
    show lars serious
    Zephyr "I think you're undermining my generosity here; I gave you so much information for nothing. I could even wipe your brains clean."
    
    voice "audio/voice/zephyr/zephyr_062_take02.ogg"
    show lars serious
    Zephyr "After all, I'm only mentioning these because I haven't had the chance to properly speak with someone for a long time now so you mustn't think that I enjoy talking to people, okay? OKAY?"

    show lars serious
    "Everyone" "He definitely enjoys talking with people."

    voice "audio/voice/lars/lars_116_take02.ogg"
    show lars serious
    Lars "So you're a noble dragon descendent who's been sleeping for centuries."

    voice "audio/voice/lars/lars_117_take01.ogg"
    show lars serious
    Lars "You woke up, broke and homeless. You decided to use free labor from the descendants to clean up the mess in your castle. However, you couldn't pay their wages properly. You then decided to slave away unsuspecting humans since they were ignorant about the rules of the realm."

    voice "audio/voice/lars/lars_118_take01.ogg"
    show lars serious
    Lars "But why did you use the time freeze artifact in the first place?"

    show zephyr at shake
    voice "audio/voice/zephyr/zephyr_063_take01.ogg"
    show lars serious
    Zephyr "How could I bring them back to my castle without explaining the situation to them? They would get suspicious and run away from now. You know how hard I've worked to manually capture the humans and brainwash them to fix up my home? Or do you want me to be homeless?"

    voice "audio/voice/zephyr/zephyr_064_take02.ogg"
    show lars serious
    Zephyr "You heartless people, you're making me fake sob over here."
   
    show lars serious
    Claude "You're obviously lacking a certain moral regard to be paying your employees so poorly, not to mention—"

    voice "audio/voice/zephyr/zephyr_065_take02.ogg"
    show lars serious
    Zephyr "I didn't want to, okay? But what other choice did I have?"

    voice "audio/voice/rory/rory_038_take01.ogg"
    show rory angry with dissolve
    show lars serious
    Rory "Literally, anything besides making a house-renovating army of human zombie servants."

    voice "audio/voice/zephyr/zephyr_066_take01.ogg"
    show lars serious
    Zephyr "I couldn't win them over with my title and I couldn't make them work without compensation either."

    voice "audio/voice/zephyr/zephyr_067_take01.ogg"
    show lars serious
    Zephyr "The time freeze did help me in relocating them and ensuring I was the first one I spoke to, making my situation clear. It was the easiest solution for me. I'd pay them back if I got a flow of gold going on."

    voice "audio/voice/zephyr/zephyr_068_take01.ogg"
    show lars serious
    Zephyr "Rumor has it that news and gossip about transported humans fetch quite the price these days, rivaling even celebrities and renowned descendants. If I could secure some scandalous scoops, I'd amass enough wealth to renovate my abode without the hassle of this extra business."

    jump menu_g1

label G_1_End:

    play music "track_1_intro.ogg" fadeout 2.0 fadein 2.0

    show claude 
    show sylvian
    show rory
    show zephyr
    with dissolve

    show zephyr sad with dissolve
    show zephyr sad at shake
    voice "audio/voice/zephyr/zephyr_071_take02.ogg"
    show lars
    Zephyr "Ugh, I'm getting tired of this interview session."

    show claude smile with dissolve
    show claude smile at jp
    show lars
    Claude "Where's the proof that you haven't been speaking gibberish so far?"

    show lars
    Claude "Merchants always need to showcase their credibility, same goes for someone who's exchanging our time with childish bluffs."

    voice "audio/voice/zephyr/zephyr_072_take02.ogg"
    show lars
    Zephyr "This group is going to be the death of me, I swear."

    voice "audio/voice/sylvian/sylvian_075_take03.ogg"
    show sylvian serious funny with dissolve
    show lars
    Sylvian "This is going to take us even longer if we continue at this pace. Rory, could you come here for a second?"

    show rory:
        linear 0.5 xalign 0.85
    
    Lars narration "Master Sylvian beckons Rory over to his side and starts whispering something in her ear. I can't make out what they're saying, but it seems important enough that he even brings up his wings to cover his mouth."

    show rory at right with move

    Lars narration "However, before I have more time to analyze what was going on, Rory chirps back to our side."

    show sylvian with dissolve
    show rory at right
    show rory at jp

    voice "audio/voice/rory/rory_039_take02.ogg"
    show lars
    Rory "You can't die on us yet {bt}Ghostyyyy{/bt}; I'm planning to give you a timeless puppet show after all!"

    show zephyr with dissolve
    show zephyr at shake
    voice "audio/voice/zephyr/zephyr_073_take02.ogg"
    show lars
    Zephyr "What are you talking about, Speedy?"

    voice "audio/voice/rory/rory_040_take01.ogg"
    show lars
    Rory "You mentioned that you wanted to be entertained, right? So why don't I keep you occupied— I mean, uh— keep you \"strung along\" for a private show."

    show rory at shake
    show claude smile with dissolve
    voice "audio/voice/rory/rory_041_take02.ogg"
    show lars
    Rory "I'm sure a person of your caliber is also familiar with these kinds of VIP events, aren't you? Because it would be totally embarrassing if you didn't."

    show zephyr at jp
    voice "audio/voice/zephyr/zephyr_074_take02.ogg"
    show lars
    Zephyr "Wha- of course I have! What kind of noble descendant would I be if I didn't? Come on, then. Entertain me if you can."

    voice "audio/voice/rory/rory_042_take02.ogg"
    show lars
    Rory "As expected. It's a good thing I always have my handy puppets for extreme situations like this."

    voice "audio/voice/rory/rory_043_take01.ogg"
    show lars
    Rory "Get ready to be amazed by Brittina and Alex. Unfortunately, Agatha hasn't undergone a complete makeover yet, thanks to a certain someone who keeps stalling."

    show lars
    Claude "{i}I wonder who that could be...{/i}"

    voice "audio/voice/rory/rory_044_take01.ogg"
    show lars
    Rory "So, why don't we go around the corner where I have my stall set up?"

    voice "audio/voice/zephyr/zephyr_075_take01.ogg"
    show zephyr sad with dissolve
    show lars
    Zephyr "Huh, what about my new army additions here?"

    Lars narration "Good to know that we're demoted past the nicknames as well."

    voice "audio/voice/rory/rory_045_take02.ogg"
    show lars
    Rory "They can't do anything when the time is frozen like this, so why don't we have some fun without any worries?"

    show lars
    Zephyr "..."

    Lars narration "Is he going to accept?"

    show lars
    "Everyone" "..."

    voice "audio/voice/zephyr/zephyr_076_take01.ogg"
    show lars
    Zephyr "Ugh, fine. Might as well enjoy my time with someone who is also interested in the art of puppets."

    voice "audio/voice/rory/rory_047_take01.ogg"
    show lars
    Rory "Exactly—"

    Lars narration "However, before Rory has the time to finish her sentence, Zephyr's shadow encloses around her, and they both disperse without a trace, leaving a momentary respite from his presence."

    hide zephyr
    hide rory
    with dissolve

    show claude at center_2left:
        xzoom 1
    
    show sylvian at center_2right with move
    show sylvian at jp
    show lars
    Sylvian "It's good to see my junior using her wit to buy us some extra time for discussing certain matters."

    show lars
    Lars "That was part of your plan all along?"

    show claude serious with dissolve
    show lars
    Claude "Look, Captain, we don't have much time to lavish praise on our precious {i}Boss{/i} and little Rory right now."

    show lars sad
    Lars "I'm a bit worried about Rory, though. Maybe I should have convinced Zephyr to let me go with her—"

    show claude smile with dissolve
    show lars sad
    Claude "Pfft, she's perfectly fine taking care of her own, and that's coming from me."

    show lars sad
    Claude "Let's move on, though. The only sensible option here is to graciously accept everything our so-called \"villain\" is saying."

    show lars serious
    Lars "How so? Isn't there even a tiny bit of doubt in your mind?"

    show claude shocked with dissolve
    show claude shocked at jp
    show lars
    Claude "I do believe what he's saying, or more so, I want his story to be true. I've been waiting for a thrilling adventure like this for quite a long time now, and the opportunity is now within my grasp."

    show lars
    Sylvian "I also think we have to believe what he says. Most notably what he mentioned about the necklace."

    show lars
    Claude "But he didn't even know that we have his so-called counter-artifact with us. Especially with how [Lars] has been hiding the necklace under his clothing all this time."

    show claude smile with dissolve
    Claude "I'd probably miss it too without these handy lizard eyes."

    show sylvian sad with dissolve
    Claude "Speaking of eyes, if I happen to overlook something crucial, I might just have to attribute it to being too captivated by your presence, Captain. Gotta take responsibility, you know?"

    hide claude smile
    hide sylvian sad
    with dissolve

    show sylvian_cranky with dissolve

    Lars narration "A low murmur reaches me and I turn my gaze towards Master Sylvian. His expression has shifted into a stern, disapproving look. It's evident that Sir Claude's nonchalant attitude is grating on his nerves."

    Lars narration "But then again, this has been Sir Claude's personality for a long time; there's no helping it."

    show lars
    Lars "For now, why don't we listen to what Master Sylvian has to say? He's certainly smarter than the both of us."

    hide sylvian_cranky with dissolve
    show claude_cranky with dissolve

    show lars
    Claude "I'm sure he can speak for himself—"

    show lars
    Sylvian "Exactly, and I'd like to take a moment to discuss what's really important here if you could set aside your flirtatious act for a second."

    Lars narration "His eyes lock onto mine, and a serene smile graces his lips."

    show lars
    Sylvian "Thank you for what you just did, [Lars]."

    Lars "It's no problem, Master. Now, let's get back to what you were saying."

    hide claude_cranky with dissolve

    show claude at center_2left
    show sylvian at center_2right 
    with dissolve

    show lars
    Sylvian "From what I understood, that shadowy figure is a noble dragon descendent from the previous dynasty of Divonia."

    show lars
    Sylvian "Supposedly, he's been sleeping for centuries, using his family's time freeze artifact on himself for some unbeknownst reason."

    show lars
    Sylvian "After all, a man is not what he thinks he is, he is what he hides."

    show lars
    Sylvian "This mysterious person can easily be related to us as well when you consider how the artifact fell into our hands in the first place."

    show claude shocked with dissolve
    show lars
    Claude "I did think it was suspicious how the merchant was trying to get rid of the box so quickly. No one would try to sell something to the Dupont family at a loss in profits."

    show sylvian sad with dissolve
    show lars sad
    Lars "I'm sorry too. I messed up big time. I shouldn't have put any of you in this situation. What kind of dragon pilot am I if I can't ensure the safety of those around me?"

    Sylvian "Don't be too hard on yourself, [Lars]. We were all caught up in the excitement of a mysterious artifact. It's easy to overlook the finer details in such situations."

    show sylvian 
    show claude 
    with dissolve

    show lars
    Sylvian "Now that we're aware, let's approach this with caution to avoid falling for any more tricks. Before our young Lord arrives, we should gather all the information we can for now."

    Lars "To summarize, he's using the legacy necklace to suspend time for everyone, and it's supposedly structurally identical to the artifact we have albeit with a different gemstone and contrasting ability."

    Lars "I also believe that the reason we escaped from his spells' effects was because of this necklace right here."

    Lars narration "I glance down at the accessory that I've carefully concealed beneath my dragon pilot equipment, and my heart skips a beat when I see that it's still shining brightly with a vivid red glow."

    hide sylvian 
    hide claude
    with dissolve

    show shining_necklace 
    with dissolve

    Lars "The heat it emitted during our earlier encounter with Zephyr may have subsided, but its enchanting radiance remains."

    Lars "Now that I think about it, he mentioned not knowing the whereabouts of the artifact, despite being in charge of the two couple necklaces all this time. My question is, why did this variable suddenly exempt us from the time freeze effect? Could it be related to the artifact?"

    show lars
    Sylvian "If it was related to the presence of the artifact in a known area, then why wasn't anyone else near the seashore also affected by its counteracting abilities? The weird shadow also said something similar."

    show lars
    Claude "Perhaps...it's related to touching the artifact."

    show lars
    Claude "Think about it, we all experienced this phenomenon after holding the necklace."

    show lars
    Claude "Not to mention, we were the only people who touched the artifact after opening the box."

    hide shining_necklace
    show claude smile at center_2left 
    show sylvian serious funny at center_2right 
    with dissolve

    show lars
    Lars "Quite the detective, aren't you? I didn't realize I had a master of deduction by my side."

    show lars
    Claude "Oh, Captain, you'll uncover even more intriguing talents if you choose to stick around with me."

    show sylvian sad with dissolve
    show lars 
    Sylvian "Enough flirting, Claude."

    show claude smile at shake
    show lars
    Claude "Yeah yeah, whatever you say, big Boss."

    show lars serious
    Lars serious "His plan to renovate his castle seems utterly absurd to me, though."

    show sylvian serious funny with dissolve
    show lars
    Claude "Mhm, hiring descendants only to realize he can't pay his way through. Going for humans and not even offering to inform them of the rules around here. It's both malicious and strangely naive at the same time."

    Lars "What about the people who are currently captured by him? How do we convince him to let them go?"

    show sylvian with dissolve
    show lars
    Sylvian "“To lose patience is to lose the battle.”"

    show lars
    Sylvian "Let's take this one step at a time."

    show lars
    Sylvian "After our deck is complete, we can use our hidden ace and free the people under his spell. It may be late for those who fell victim to his scheme, but we need to put a stop to this time suspension phenomenon."

    Lars "But how are we supposed to do that? He already wants to stop us by adding us to his zombie human army since he believes we'll spoil his plans."

    Lars "Also, I can't figure out why he's giving all this info to us, knowing it's going to work against him. Does he have another plan in mind?"

    show claude smile at jp
    show lars
    Claude "Like I said, he's probably just a naive kid. But we can use that to our advantage."

    show lars
    Sylvian "Fortunately for us, a threatening tongue reveals a wayward start."

    show lars
    Sylvian "For in loose words, a tale unfolds, of inner battles and stories untold."

    show lars
    Claude "I'd like to think that one of his screws is missing."

    Lars "So I'm assuming we're going to act unaware of why we're not affected by the time suspension?"

    show lars
    Sylvian "I think it's best that we do. Otherwise, we'll be divulging the reason why we're not influenced by his artifact and how the countermeasure necklace has fallen into the palm of our hands."

    Lars "What if he notices though?"

    show lars
    Claude "He's more preoccupied with being entertained than trying to figure out why we're moving around freely. Do you recall him even questioning us about it?"

    Lars "Now that you mention it..."

    Lars narration "Speak of the devil, Zephyr's black particles coalesce once more and he and Rory appear side-by-side. My initial worry dissipates as they emerge with grins plastered across their faces."

    $ renpy.choice_for_skipping()
    show sylvian zorder 1 with dissolve:
        linear 0.5 xalign 0.6
    show claude zorder 2 with dissolve:
        pause 0.25
        xzoom -1.0
        pause 0.25
        linear 0.5 xalign 0.4
    
    show zephyr happy at left with dissolve:
        yalign 0
        yoffset 0
    show rory at right with dissolve
    
    show lars
    Zephyr "Finished with the banter and jokes? Speedy here kept me quite occupied, I must say."
    
    show lars
    Rory "Petition to designate this guy as our story antagonist. We'll have a 99.9\% chance of success in distracting him, and he won't even make a fuss about it."

    show zephyr at shake
    show lars
    Zephyr "I'd say it's worth it because of that fabulous puppet show earlier."

    show lars
    Zephyr "I look forward to seeing you bring in new dolls to the scene as well. This could be my new hobby after reading my daily gossip columns."

    show rory at jp
    show lars
    Rory "Yay, another fan acquired!~"

    show lars
    Sylvian "I'm glad to see you back safely, my dear junior."

    show claude smile with dissolve
    show lars
    Claude "Can't say I share the sentiment."

    show rory angry with dissolve
    show lars
    Rory "Well, you're a few degrees short of cold-blooded, so I don't blame you."

    show zephyr zorder 3
    show lars
    Sylvian "That's enough for now, there's something more important we need to address."

    show sylvian at center_3left
    show claude at center_2right
    with move
    
    Lars narration "Master Sylvian's steady voice resonates with unwavering conviction as he faces Zephyr."

    show sylvian serious funny with dissolve
    show lars serious
    Sylvian "Noble descendent, it's clear that you're manipulating a fundamental fabric of time for your personal gain. However, we cannot remain in this state too long."

    Lars narration "It seems like Master Sylvian will not be mentioning our displeasure about the brainwashed army at his castle. It's probably best to keep a secret for now."

    show lars serious
    Zephyr "Here's the fact, Smarty. I don't understand the mechanics of it either and I don't really have to."

    show lars serious
    Zephyr "What I do know is that you guys can escape the effects of my family heirloom either because you're special in some way or there's a variable that I'm not aware of, like the counter artifact."

    Lars narration "Oh no, is he catching on to us?"

    Lars narration "I grasp the gemstone beneath my piloting gear, my fingers wrapping around it tightly. It's as if I'm seeking reassurance that our hidden card remains securely in our possession"

    Lars narration "Looking over my shoulder, I notice my tail wagging at full speed. The rhythmic swaying is almost involuntary, a physical manifestation of the heightened anxiety stirred by Zephyr's comments."

    show sylvian with dissolve
    show lars serious
    Zephyr "{i}But{/i}...enough of that imaginary scenario because I don't really care why you're not affected."

    show claude smile with dissolve
    show lars serious
    Claude "Told you so, Captain."

    show lars serious
    Zephyr "When I take you back to my castle. You'll join my army and I'll be able to continue my renovation plans without any worries of someone trying to ruin it."

    show lars serious
    Zephyr "Keyword being {i}“try”{/i}."

    show lars serious
    Zephyr "After all, you guys cannot escape from me while my artifact is still working."

    Lars narration "That's literally what we're trying to do here though!"

    show zephyr sad with dissolve
    show lars serious
    Zephyr "However, I can't keep time frozen forever. I need to teach my new minions what they need to do."

    show lars serious
    Claude "Before that, I possess a proposition that might pique your interest."

    show zephyr happy with dissolve
    show lars serious
    Zephyr "Hmm? What is it Slicky?"

    show lars serious
    Claude "It appears you're seeking some amusement, considering your remarks about the lackluster nature of your current {i}companions{/i}. We could be the very diversion you yearn for."

    show lars serious
    Zephyr "That won't do. I can't leave you guys alone; you might spoil my plans or decide to play around with the artifact when I'm not looking, especially since I gave you the description for it. Got it, Scouty? Slicky? Smarty?"

    show lars serious
    Lars "Why do I feel like we've become Earthling pets of some sort with all these weird nicknames?"

    show lars serious
    Zephyr "I've been surrounded by so many brainwashed humans during the castle renovations that my brain cells are rotting by the lack of creativity and putrid repeated phrases. You could say their antics are rubbing off on me."

    show lars serious
    Zephyr "Anywho, how can you convince me that you won't be an obstacle to my plan until my castle is restored?"

    show rory with dissolve
    show lars serious
    Rory "We'll pinky promise."

    show lars serious
    Rory "That's the most you can get from us."

    show lars serious
    Zephyr "See? Then there's no reason for me to let you leave—"

    Lars narration "This won't do! We must uncover the truth behind all of this."

    Lars narration "I can't give up right now, not when I have a responsibility to protect my comrades."

    show lars 
    Lars "We'll earn your trust."

    show lars serious
    Zephyr "Somehow, I really doubt—"

    show sylvian sad with dissolve
    show lars serious
    Sylvian "[Lars]! What're you trying to do?"

    show claude shocked with dissolve
    show lars serious
    Claude "I'm not a fan of what you're trying to pull here, Captain. Especially since it's without me."

    show lars serious
    Lars "You can't pull that on us, you know? We also gave you a chance when you shared your story."

    show zephyr at shake
    show lars serious
    Zephyr "..."

    show lars serious
    Lars "You just need to give us a few minutes and listen to our case."

    show zephyr at shake
    show lars serious
    Zephyr "..."

    show lars
    Zephyr "Ugh fine! But just for a little. It's not like I wanted to repay you back for listening to me, okay? OKAY?"

    show lars
    "Everyone" "He's definitely repaying us for listening to him."

    Lars "Master Sylvian, you're the smartest person amongst us—"

    show claude shocked at jp
    show lars
    Claude "I'm hurt that you're not even considering me Captain..."

    show lars
    Claude "You should have at least hesitated a bit..."

    Lars "We need you to come up with a plan!"

    show sylvian sad at shake
    show lars
    Sylvian "[Lars], why did you suggest such a thing to him?"

    show lars
    Sylvian "He's a dangerous person! Time-freezing? Brainwashing? How can you trust him so quickly after only a few conversations?"

    show lars
    Sylvian "Now, his attention is directed toward you, or whatever you intend to discuss with him."

    Lars "I don't trust him; I just think that it's best if we decide on a plan so I don't get tongue tied like the last time he asked me a question."

    Lars "At least, I got us a little time so we can discuss our options."

    show claude serious with dissolve
    show lars
    Claude "Sorry, Captain. But I'm siding with Boss on this one."

    show lars
    Claude "Just to clarify, my reasons are a bit different."

    show claude smile with dissolve
    show lars
    Claude "Boss Sylvian might want to divert his attention from us and discreetly find a solution to maintain his current peace and order. But I'm more inclined to jump right into the heart of the matter."

    show lars
    Claude "He could be a secret royal heir for all I care, but I'm driven by curiosity. I can't resist this challenge and let someone else take the credit for solving the mystery."

    show lars
    Claude "I mean, a missing noble heir, a potentially unexplored castle, and an artifact that freezes time? When was the last time we faced a challenge like this?"

    Lars narration "Staying true to their personalities, both Master Sylvian and Sir Claude have their distinct motivations for wanting to unravel this mystery."

    Lars narration "As for me, I'm still uncertain about my own stance. Who should I confide in to discuss my decision?"

    menu:
        " " " "
        "Speak with Master Sylvian":
            $ options["CS6"]=1
            jump speak_with_Master_Sylvian

        "Speak with Sir Claude":
            $ options["CS6"]=2
            jump speak_with_Sir_Claude


label speak_with_Master_Sylvian:

    play music "track_6_romance_scene.ogg" fadeout 2.0 fadein 2.0

    hide claude smile
    hide rory 
    hide zephyr 
    with dissolve

    show sylvian sad at center
    with move

    voice "audio/voice/lars/lars_121_take02.ogg"
    Lars "How do we present our case?"

    voice "audio/voice/sylvian/sylvian_076_take03.ogg"
    show lars
    Sylvian "You have to understand, [Lars]. We need to show how weak we are in front of him so he loses interest."

    voice "audio/voice/sylvian/sylvian_077_take03.ogg"
    show lars
    Sylvian "If he gets curious about the origins of our artifact, things could take a dangerous turn."

    voice "audio/voice/sylvian/sylvian_078_take01.ogg"
    show lars
    Sylvian "He basically admitted to slaving away humans and descendants alike just for some castle renovations."

    voice "audio/voice/sylvian/sylvian_079_take03.ogg"
    show sylvian serious funny with dissolve
    show lars
    Sylvian "Does any of that sound rational to you?"

    voice "audio/voice/lars/lars_122_take02.ogg"
    show lars serious
    Lars "No, but shouldn't we aim to ruin his plan for the same reason? He's robbing unsuspecting humans of their freedom. As members of {i}'Custodes Sylvae',{/i} our duty is to rescue them—"

    voice "audio/voice/sylvian/sylvian_080_take03.ogg"
    show sylvian sad with dissolve
    show lars serious
    Sylvian "We're just a merchant guild, [Lars]. I understand your sentiments, but we can't rush into things like this."

    voice "audio/voice/sylvian/sylvian_082_take02.ogg"
    show sylvian with dissolve
    show lars sad
    Sylvian "An opportunity will arise if we give it time. Once we have more information about the artifact, we can start devising a plan, whatever it may be."

    voice "audio/voice/sylvian/sylvian_083_take03.ogg"
    show sylvian blush with dissolve
    show lars sad
    Sylvian "I can't let him get his hands on any of my valuable guild members, {i}especially{/i} not you."

    Lars narration "Master Sylvian? What's with the sudden declaration? It almost sounded like..."

    voice "audio/voice/sylvian/sylvian_084_take03.ogg"
    show lars blush
    Sylvian "[Lars], my world became quite distorted during my days in academia, like a scrambled puzzle. I was in a state where I couldn't progress until each piece fell into place."

    voice "audio/voice/sylvian/sylvian_085_take03.ogg"
    show lars blush
    Sylvian "To my surprise, a piece did fall into my grasp, owing to an incredible chance, miracle, or even mere luck, and that piece is my precious guild. I don't want you to do anything irrational and risk losing anyone."

    voice "audio/voice/lars/lars_126_take01.ogg"
    show lars blush
    Lars "I understand Master. Don't worry, I have your back as well. I'm not going to let anyone touch my precious comrades!"

    voice "audio/voice/lars/lars_128_take02.ogg"
    show lars 
    Lars "Let's just talk it out with the others for now. Alright?"

    voice "audio/voice/sylvian/sylvian_086_take02.ogg"
    show sylvian sad with dissolve
    Sylvian "I suppose this conversation can wait for another time."

    show sylvian sad at right
    with move
    Lars narration "As I move away to speak with the other members, a faint whisper reaches me, though I can't discern its exact words."

    voice "audio/voice/sylvian/sylvian_087_take02.ogg"
    show lars
    Sylvian "{size=*0.75}It's been so long that I've reached out for a piece of my own accord that I've forgotten how to clench what's already in the palm of my hand."

    Lars narration "I hope he didn't say anything too serious."

    jump CS_6_End

label speak_with_Sir_Claude:

    play music "track_6_romance_scene.ogg" fadeout 2.0 fadein 2.0

    hide rory
    hide sylvian sad
    hide zephyr
    with dissolve

    show claude smile at center
    with move

    voice "audio/voice/lars/lars_121_take02.ogg"
    Lars "How do we present our case?"

    show lars
    Claude "My dearest Captain [Lars], I adore your stubbornness at times like this, so it's only right that I offer my support."

    show lars
    Claude "I believe it's wiser to pique our new Lord's interest in us rather than dismiss it."

    show claude at shake
    show lars
    Claude "Picture this— he realizes we're ordinary individuals and decides to incorporate us into his team of {i}renovators{/i}."

    show lars
    Claude "However, that would likely cut off our access to any information from the other members of his so-called army."

    show lars
    Claude "That's why taking direct action is imperative."

    show lars
    Claude "I could take a more subtle approach and talk to the merchant again, inquire about possible tools or learn the story behind our artifact."

    show lars
    Claude "But I can't risk losing my seat in this interesting show."

    Lars narration "Sir Claude..."

    show claude blush with dissolve
    show lars blush
    Claude "I would go on ahead on my own but I don't want to leave my duo behind either."

    show lars blush
    Claude "It would be no fun without you by my side, [Lars]."

    Lars narration "He called me [Lars]. I never thought I would hear him say my name in such a way."

    Lars narration "I suppose it's only fitting that I match his level of enthusiasm."

    voice "audio/voice/lars/lars_131_take01.ogg"
    Lars "I understand!"

    voice "audio/voice/lars/lars_132_take01.ogg"
    show lars blush
    Lars "I can't leave you all by yourself and I'm not letting you hog all the fun either."

    Lars narration "Perhaps it was the surge of my newfound conviction or the palpable anticipation of an impending challenge that sent my adrenaline levels soaring."

    show claude smile with dissolve
    show claude smile at jp
    show lars blush
    Claude "That's what I wanted to hear."

    show lars blush
    Claude "Adventures favor the bold and fortunate."

    show lars blush
    Claude "We'll end up misusing our lifetime of luck if we don't take up this chance."

    show lars blush
    Lars narration "Alright, Alright, I get it. Time to get a move on now."

    show claude smile at shake
    show lars
    Claude "I already used up a great portion of my luck so I can have this opportunity with you and I won't give up on any chances!"

    show lars blush
    Lars narration "What a riot, everyone else can hear you making such a loud declaration!"
    
    show lars blush
    Lars narration "Not even a lick of embarrassment either, that's just how self-assured he is..."

label CS_6_End:

    scene bg black with fade
    show bg_3 with fade

    play music "track_1_intro.ogg" fadeout 2.0 fadein 2.0
    
    show sylvian zorder 1 at center_right
    show claude zorder 2 at center_left:
        xzoom -1.0
    with dissolve
    
    show zephyr happy at left with dissolve:
        yalign 0
        yoffset 0
    show rory at right with dissolve:
        xalign 1.05

    show lars serious
    Zephyr "Ah enough talking. Come here Scouty!"

    Lars narration "I stride purposefully towards him and hold my tail straight as a sign of readiness."

    show claude smile with dissolve
    show lars serious
    Claude "You can't stop now, Captain."

    show lars serious
    Sylvian "You have to make him listen well, [Lars]."

    show lars serious
    Rory "I'm rooting for you [Lars], show him what you're made of!"

    Lars narration "If he truly is as dangerous as we all think, then I should try to get to the root of this issue and make sure he doesn't use the time freeze artifact again."

    show lars serious
    Zephyr "Hurry up now, I don't have all day."

    show lars serious
    Lars "{size=*1.25}Young Lord Zephyr!" with vpunch

    show zephyr sad with dissolve
    show zephyr sad at jp
    show lars serious
    Zephyr "Yikes, are you attempting to blast a hole through my non-existent eardrums or something?"

    show zephyr:
        zoom 1.0

    Lars "We'll be your private entertainers and provide the scoop you need for your renovation funds."

    Lars narration "I share a meaningful look with my fellow guild members, and it's clear that they are all equally puzzled. The silence that follows my suggestion serves as confirmation."

    show claude serious with dissolve
    show sylvian serious funny with dissolve
    show rory at shake
    show lars serious
    Rory "I don't think it's too late to come back just as confidently, [Lars]..."

    show zephyr happy with dissolve
    show lars serious
    Zephyr "What're you trying to scheme Slicky? Are you trying to trick me with this sudden suggestion?"

    Lars "It's simple, we can't stay suspended for too long."

    Lars "You won't let us leave either because we could prove to be an obstacle for you. Not to mention, it seems you're more interested in keeping tabs on us than your army of humans."

    Lars "Hence, the best we can do is reach a compromise that suits both our interests."

    show claude blush with dissolve
    show lars blush
    Claude "That's the kind of negotiation skill I'd like to see."

    show claude smile with dissolve
    show lars
    Zephyr "...and your idea of a compromise is for me to have you all entertain me and give me a scoop?"

    show sylvian with dissolve
    Lars "You like to be entertained, don't you? At your disposal, there is a famous merchant, puppet-master, magician, and a dragon pilot."

    Lars "You can earn a column's worth of gossip material and earn your funds without hurting anyone. Didn't you say that you dislike brainwashing and kidnapping people as well?"

    show lars
    Zephyr "Hmm, such insolence!" with vpunch

    show zephyr at shake
    show lars
    Zephyr "However, I like to have fun as well. How will you tip the odds in our favor?"

    Lars "I don't need to. We're the only ones aware of your situation and still willing to listen. That's why we're the best suited to cater to your interests."

    show sylvian blush with dissolve
    show lars blush
    Sylvian "Great work, my dear junior. I knew I could trust you."

    show lars blush
    Zephyr "That does make sense, so what will everyone be doing? I'm assuming Speedy will do some kind of puppet show again—"

    Lars "You'll only take me as your entertainer and you need to promise to let the others go."

    show lars
    Zephyr "Huh—"

    show sylvian 
    show claude shocked
    show rory
    with dissolve

    show rory at jp
    show claude shocked at jp
    show sylvian at jp
    "Everyone" "{size=*1.5}WHAAAAT????" with vpunch

    Lars "After all, I'm a dragon pilot, so we already share quite a few common interests, especially considering that you're a supposed dragon descendent."

    Lars narration "Please, take the bait!"

    show zephyr sad with dissolve
    show zephyr sad with shake
    show lars serious
    Zephyr "..."

    show zephyr sad with shake
    show lars serious
    Zephyr "...two."

    show lars serious
    Lars "Hmm, what?"

    show lars serious
    Zephyr "I'd like two of you to take on the role of my personal  entertainers."

    show sylvian sad
    show claude serious
    show rory angry
    with dissolve

    show lars serious
    Zephyr "I'll take you to my castle and the rest of you can prance around as it."

    show lars serious
    Zephyr "It's a win-win situation for me since I can ensure your friends won't attempt anything while you're kept as hostages—uh, entertainers, I mean!"

    show lars serious
    Zephyr "You have to keep me well entertained though considering I'm a huge fan of confessions and duo comedy routines."
    
    show lars serious
    Rory "So you're trying to {i}ice-olate{/i} us."

    show zephyr at shake
    Zephyr "Finally! Somehow who understands my sense of humor."

    show lars serious
    Lars "But that's not what I told you, it's only supposed to be me. Here's the deal: no touching their hair, no messing with furs, feathers, scales, anything!"

    show lars serious
    Lars "Also, you can't take us to your castle. Who knows how risky it could be when it's not fully renovated yet?"

    Lars narration "If he does go after the other guild members, he'll notice that we don't have any special powers to counteract the artifacts' time suspension effect. We could all get caught without any counter measures! I don't want to risk going to an unknown location either."

    show claude at jp
    show lars serious
    Claude "Don't get too excited now, Captain. I'm not going to let you go down this route by yourself—"

    show claude:
        zoom 1.0

    show sylvian sad with dissolve
    show lars serious
    Sylvian "Forget the plan, we didn't discuss this self-sacrificing scenario, [Lars]! You mustn't risk—"

    show lars serious
    Zephyr "Hey, Scouty, you didn't listen to me, it seems. Single confessions are for the holy folk, not for entertainment."

    show lars serious
    Zephyr "How are you going to do a duo comedy with only yourself?"

    show lars serious
    Zephyr "Are you going to have a heart-to-heart with your reflection in the mirror, or perhaps consult your spineless shadow for therapist advice?"

    show lars serious
    Zephyr "You're lucky I'm a benevolent enough person because I'll at least give you the option to choose."

    show lars serious
    Zephyr "Pick between Smarty and Slicky over there, since I already had Speedy entertain me."

    Lars "..."

    show sylvian sad at shake
    Sylvian "[Lars], I can't leave you alone like this, otherwise..."

    show lars sad
    Lars "Master—"

    show sylvian serious funny with dissolve
    show claude shocked with dissolve
    show lars sad
    Sylvian "Let us go to his castle together."

    show lars sad
    Sylvian "Even though I disagree with this hasty approach, I'll do my best to assist you with my knowledge and magical prowess."


    if options["CS6"]==1:

        show sylvian blush with dissolve
        show lars blush
        Sylvian "You're a cherished member of my guild, one of the few things I've gotten right—a rare and perfectly fitted puzzle piece that I won't jeopardize or let slip away, even if it means disrupting my current state of peace."

        Lars narration "The intensity of Master Sylvian's gaze pins me, and my heart skips a beat in response. The heat in his stare seems to sear through me, and I can't help but feel the weight of his words hanging in the air."

        Lars narration "I can't believe that I was this important to him."

        Lars narration "Perhaps there's a chance to uncover more about him in the future."

        Lars narration "Why he departed academia and how it caused him to abandon his past and establish the guild for us, alongside the rationale behind his motto of life to keep things uncomplicated and go with the flow."

        Lars narration "Most importantly, I wonder why he wants me to be safe within his sight..."



    show claude smile with dissolve
    show lars
    Claude "Captain, didn't we talk about our future plans together? What kind of a duo would we be if one left the other behind?"

    show lars
    Claude "In a world of limitless horizons and uncharted trails, I am a wanderer at heart, forever seeking new thrills and adventures."

    show lars
    Claude "Yet, amidst the uncertainty that lies ahead, I want you to choose me to walk by your side."

    show lars
    Claude "I'll make the journey worthwhile for you with my charm and experience."


    if options["CS6"]==2:

        show claude blush with dissolve
        show claude blush at shake
        show lars blush
        Claude "Plus, we'll make quite the successful team if we tackle this mystery together."

        show lars blush
        Claude "An adventurous duo isn't complete without its counterpart, and if it's not you walking that path with me, then I won't have anyone else to share it with."

        Lars narration "The intensity of Sir Claude's gaze pins me, and my heart skips a beat in response. The heat in his stare seems to sear through me, and I can't help but feel the weight of his words hanging in the air."

        Lars narration "I can't believe that I was this important to him as his guild member."

        Lars narration "Perhaps there's a chance to uncover more about him in the future—"

        Lars narration "His relationship with his family and his motivations for distancing himself from them, alongside the reason behind his affinity for challenges and ambition."

        Lars narration "Most importantly, I wonder why he wants me as his partner in this venture..."

    
    Lars narration "It looks like I'm stuck in a dilemma. Who will I choose as my partner?"

    jump select_route
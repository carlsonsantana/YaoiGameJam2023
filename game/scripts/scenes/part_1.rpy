label part_1:

    play music "track_1_intro.ogg"
    scene bg_1 with fade:
        zoom 1.5
        xalign 0.0
        yalign 0.5
    
    #show lars #onlayer overall
    #panning effect - sample in drive
    Lars "‘Discere, cogitare, agere— the triad of wisdom.’"
    show bg_1 at pan
    Lars "‘Learning enriches the mind, and thinking sharpens it, but it is through action that we truly manifest our knowledge and shape our reality.’"

    #panning ends
    hide lars

    Lars narration "One would think that a merchant guild wouldn’t bother creating such a philosophical motto and instead advertise ‘buy one, get one’ dragon ship seats every holiday season."

    Lars narration "We could even offer complementary earthling-made meals by the human chefs who were transported to our realm upon their death."
    
    show bg_1 at end_pan

    Lars narration "But then again, embarking on artifact hunts and historical expeditions wouldn’t make sense if the sole purpose of our guild, ‘Custodes Sylvae’, was commerce."
   
    show claude serious at right
    #"Unknown" "Who on Divonia is mumbling this loud to themselves early in the morning?"
    Claude "Who on Divonia is mumbling this loud to themselves early in the morning?"

    #"Unknown" "I’m losing my beauty sleep over here."
    Claude "I’m losing my beauty sleep over here."

    Lars narration "I steal a glance from my perch atop the dragon ship and it looks like one, or should I say, the only passenger, has woken up in quite a grumpy manner."

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

    show lars
    Lars "It’s me, Sir Claude. Did you already forget about  your comrade after a few hours of sleep?"

    show claude smile at center:
        linear 0.5 xalign 0.5
    show lars
    Claude "Ah, my dearest Captain [Lars]!"

    show lars
    Claude "How could I ever get that nightingale-like voice of yours out of my head? It’s almost like my personal alarm clock!"

    hide lars
    Lars narration "Up for a challenge this early? Typical."

    show lars
    Lars "I’m glad you appreciate my vocal talents. But you know, I can’t take all the credit."

    Lars "You’re the one who inspires me to mumble so loudly during our journeys."

    Lars "It’s the only way I can drown out your attention-seeking snores."

    show claude at center
    Claude "You always find a way to turn the tables, don't you?"

    Claude "Although…"

    Claude "I can unfailingly capture your attention through other means, if I choose to."

    jump C_1_End

label resist_the_urge_to_surprise_him:

    hide lars
    Lars narration "It’s best that I focus on piloting our dragon first. Otherwise, I’ll never hear the end of it."

    show lars
    Lars "Good morning to you too, Sir Claude."

    show claude shocked at center:
        linear 0.5 xalign 0.5
    Claude "What a boring reaction. I expected more spunk from you…"

    Lars "Nevermind then. Hmph!"

label C_1_End:

    hide lars
    show claude at center
    Lars narration "It’s truly a wonder how he managed to stay asleep throughout our entire journey, considering the lack of proper seat arrangements or resting areas on our new dragon ship."

    Lars narration "However, Sir Claude has always been notorious for his resourcefulness in such moments, owing to his history of travels and adventurous ordeals, despite his comfortable upbringings."

    show lars
    Lars "I will return to my duties, then, Sir—"

    Claude "Didn’t I already tell you to drop the ‘Sir’ for the umpteenth time, Captain?"

    Lars "Do we have to go over this cliche back and forth as well?"

    Lars "I promised I’d do it if you stopped insisting on “Captain” this and “Captain” that."

    show claude smile at center
    Claude "It makes us seem more of an adventurous pair, though, don’t you think so?"

    hide lars
    Lars narration "Indeed, and there is a good reason for that."

    Lars narration "My knack in piloting and his remarkable merchant abilities just clicked. Whether it was going on expeditions, dealing in trades, or connecting with the quirky passengers we often had..."

    Lars narration "We always made an efficient team. Maybe even the best among all the guild members."

    Lars narration "Well…at least, if you ignore that there are only four of us."

    Claude "Now that I think about it, what were you talking to yourself about?"

    Claude "Confiding trade-secrets to our dragon, Spotsy? Or even a secret confession for me—"

    show lars
    Lars "She doesn’t even have any spots. You’re bad at naming as always, Sir-"

    hide lars
    Lars narration "He lets out an intrusive cough."

    show lars
    Lars "-Claude. Not to mention, the confession jokes won’t work if you keep repeating them over and over again."

    show claude at center
    show lars
    Claude "Who knows, maybe one day, I'll surprise you with a confession that will leave you speechless."

    hide lars
    hide claude
    show spotsy
    Lars narration "I reach out, my hand confidently caressing the head of our newest guild member who I hope I’m taking good care of."

    Lars narration "Her eyes meet mine in and in a show of trust, her scale’s part open, revealing mesmerizing roseate flames simmering underneath."

    Claude "Don’t let your attention wander off too much, Captain."

    Lars narration "Sir Claude's voice carries a subtle touch of displeasure as he observes me caressing Spotsy's head."

    Lars narration "Maybe the uncomfortable seating arrangement is getting to him."

    show smoke
    Claude "Spare the royal treatment. She’s just a glorified lizard that could use a few mint leaves."

    Lars narration "As if to express her annoyance, Spotsy lets out a flushed, puffy plume of smoke from her nostrils. A low rumbling note resonates from her throat, a clear indication of her irritation."

    hide smoke
    hide spotsy
    show claude at center
    show lars
    Lars "You're starting to irritate her, Sir-"
    Lars narration "Another intrusive cough."

    Lars "-Claude, I think you should stop."

    show lars serious
    Claude "She doesn’t like it, hmm…that just makes me want to do it even more though."
    show lars serious
    Claude "Stealing Captain’s attention away from me and not facing any consequences? Not on my watch."
    show lars serious
    Claude "I could also argue that I don't want to end up as some unfortunate passenger who prematurely expires and transports to the Earthly realm just because you were adoring our newest ship."
    show lars serious
    Claude "There have been one too many incidents like that lately."

    hide lars
    Lars narration "His sudden change of topic leaves me slightly bewildered. I withdraw my hand from Spotsy's head, and she shakes her head as if still searching for my comforting touch."

    Lars narration "In contrast, a mischievous grin adorns Sir Claude's face."

    Lars narration "Maybe the problem wasn’t the seats after all…"

    show claude shocked at center
    show lars
    Lars "The numbers of transported humans have certainly increased quite a bit these days."

    Lars "Even still, they are a precious rarity. In all my years of flying travelers across the lands of Divonia, I have only ever met a handful of them."

    show claude at center
    show lars
    Claude "Not many would want to undertake the journey of transitioning to a new realm they know nothing about, after all."

    Lars "I understand that, but they always fascinate me with the tales of their past life."

    Lars "All our guild members were born and raised here, so I don’t have the chance to closely work with one of those travelers either."

    show claude smile
    show lars
    Claude "Tsk, tsk, already thinking of replacing me with someone else, are you, Captain?"

    Lars "You said it yourself, one has to admire their bravery. Since descending into Divonia is a grand leap of faith into the unknown."

    hide lars
    Lars narration "A muffled chuckle escapes him."

    Lars narration "Claude is always the most spirited one when faced with adversity and adventure."

    Lars narration "Must feel great to not have any worries and be nonchalant about everything."

    Claude "Ah, how gladly I would take their place if I could…"

    Claude "Life can get pretty boring when you have everything you need in the palm of your hand."

    show lars blush
    Lars "Always trying to satisfy your thirst for adventure, eh?"

    hide lars
    Lars narration "I could hardly recall a day when Sir Claude didn’t turn a simple task into a grand quest. He always was, and still is, on the lookout for opportunities to embark on new escapades."

    show claude at center
    Claude "I’d advise you to concentrate on steering our ship for now, Captain, before you get even more distracted. Your gaze is practically burning my scales."

    show lars
    Lars "Oh, don’t flatter yourself, your scales are nothing compared to Spotsy’s."

    hide lars
    show claude serious at center
    Lars narration "My playful grin is met with a sulky stare."

    Claude "Well, I suppose it's my mistake for attempting to catch the attention of a certain dragon-obsessed pilot. What will become of my grandiose confession now?"

    show lars
    Lars "Don’t be so hard on yourself, Sir Claude."

    Lars "You know I appreciate you for more than your appearance, even if I rank you below Spotsy. Stopping the confession jokes could help though—"
    show lars
    Claude "No need for the empty flattery."
    show lars
    Claude "I've had my fill of it thanks to a certain family name."
    show lars
    Claude "However, you need to make sure to take care of her well since I did make quite the effort for her exchange."

    hide lars
    Lars narration "As is his custom, Sir Claude deftly redirects the conversation whenever his family is brought up."

    Lars narration "I used to wonder if he was doing so to maintain his privacy as a renowned heir with a diamond spoon, but despite the many years we spent together as partners, the sentiment never changed."

    show lars
    Lars "What effort are you talking about? Hmm?"

    Lars "The person we negotiated with today eagerly handed over all his prized possessions the moment he heard the 'Dupont' surname. It was hardly a fair \"exchange\" at that point."
    show lars
    Claude "Well, that's the con of having an outrageously high-class family name like mine, I suppose. Makes one’s trade prone to being disgustingly easy."

    Lars "And let's not forget about that one specific artifact. They were so adamant to wash their hands of it."

    show claude shocked at center
    show lars
    Claude "I’m not one to accept gifts without scrutiny. But there was something about it that piqued my interest. You’ll have a better idea once you take a look at it yourself."

    Lars "What if it turns out to be hazardous or a curse? Scrutiny would have been welcomed."
    show lars
    Claude "I was planning to spice things up a bit, so why not embrace the opportunity of a possible adventure?"

    Lars "Right…because who wouldn’t jump at the chance to receive an artifact with no known origins, suddenly materializing out of thin air, and with no apparent acquisition date?"

    show claude serious at center
    show lars
    Claude "Your sarcasm is showing Captain, might want to hide it under a thin layer of worry or, Divs forbid, concern for your partner."

    menu:
        " " " "
        "Apologize for teasing him":
            $ options["C2"]=1
            jump apologize_for_teasing_him

        "Continue teasing him even more":
            $ options["C2"]=2
            jump continue_teasing_him_even_more


label apologize_for_teasing_him:

    show lars
    Lars "I apologize, Sir Claude. You know I have no ill intentions."

    Claude "Oh, how it pains me to witness my most faithful, loyal, and devoted companion trying to replace me with some unknown human whilst MOCKING my skills…"

    Claude "My scales are going to shed off from the misery of it all."

    Lars "Come on, Sir Claude. Don’t be so dramatic. You know I’m only teasing you as payback."

    show claude shocked at center
    Claude "I am baffled, dumbfounded, bamboozled, shocked, bewildered, and confuzzled to the highest degree."

    Lars "You’re irreplaceable to me, and your merchant skills are unmatched—"

    Claude "Hmph, why should I trust your word? You should know that actions speak louder after all."

    Lars "Then…how should I show it to you?"

    show claude smile at center
    Claude "There’s something that I really want but with our relationship as is, you won’t be able to give it to me."

    show claude
    hide lars
    Lars narration "My fur prickles with anticipation. I can sense my ears perking up, betraying my keen interest in his next words and what he could possibly want from me."

    show lars
    Lars "A gift? For you? But you already have everything you need."

    Lars "Your family has your pockets lined with all the gold and treasures imaginable too, so I can’t see what you’d want from someone like me."

    show claude at center
    Claude "I’ll tell you more about it in due time."

    jump C_2_End
    return

label continue_teasing_him_even_more:

    show lars
    Lars "The infamous Claude Dupont, not checking the items he negotiates for?"

    show claude serious at center
    Claude "Please, [Lars], you should know better than blabbering ‘Dupont’ recklessly."

    Lars "Weren’t you going to stop calling me ‘Captain’ as well? Or are you going to change the topic again?"

    show bg_1:
        linear 2.0 blur 15
    show claude smile at center:
        linear 2.0 zoom 1.1
    #zoom in a little on Claude and blur the background
    Lars narration "Leaning close, his fingertips gently brush against my cheek, leaving a trail of warmth. Golden eyes lock onto mine with unwavering intensity. As his lips draw near my ear, his voice deepens, resonating with a seductive allure that sends shivers down my spine."

    show claude smile
    Claude "See? I used your name, so you have to call me by mine too...without the titles."

    Claude "I prefer it when you say my name after all. It’s one of the tiny joys of my life."

    #slowly zoom to normal and unblur background
    show bg_1:
        linear 1.0 blur 0
    show claude smile at center:
        linear 1.0 zoom 1.0
    Lars narration "The sudden remark takes me by surprise, even though it’s not the first time I’ve heard Sir Claude make such a comment. After all, he possesses a captivatingly flirtatious nature, effortlessly weaving his charm into every interaction."

    Lars narration "However, a part of me hesitates, fearing that surrendering to his banter may lead to my own demise."

    show lars blush
    Lars "W-w-what are you saying all of a sudden?! Did you lose your mind?"

    show claude blush
    Claude "Awe, is our Captain getting shy all of a sudden? Did you know your ears get red when you're embarrassed?"

    hide lars
    Lars narration "With little time to question his truthfulness, I instinctively place my hands on my ears, hoping to shield any trace of vulnerability that might betray my reaction to his words."

    show lars blush
    Lars "I am a dragon pilot, an unwavering force soaring through the skies."

    Claude "Yes, indeed. That much is observable."

    Lars "My years of experience have honed my resilience and steeled my resolve. I cannot allow myself to be easily affected by the whimsical words of Sir Claude, no matter how charismatic he may be!"

    show claude smile at center
    Claude "Awe, did I get under your skin, Captain? So much that you had to switch to third-person commentary?"

    hide lars
    Lars narration "Sir Claude remains unfazed by my momentary embarrassment except for a triumphant smile."

    show lars blush
    Lars "He’s only joking to gauge my reaction—"

    Claude "Haha, look at you. Navigating the skies like a pro with those sharp fox eyes, yet somehow missing the obvious right in front of you."

    show lars
    Lars "Pardon?"

label C_2_End:

    show claude at center
    Claude "Let’s continue this conversation later, shall we?"

    Claude "Our dearest Guild Master is signaling our landing spot."

    #hide all
    hide claude
    hide sylvian
    hide rory

    Lars narration "I glance downward, and our destination near the sea comes into view."

    $ renpy.choice_for_skipping()
    play music "track_2_field_of_flowers.ogg"
    scene bg black with fade
    show bg_2 at pan with fade
    #panning effect - sample in drive
    
    Lars narration "Like an artist painting delicate strokes on a canvas, Master Sylvian has already lined up the location with an array of enchanting flowers."
    
    #show bg_2 at pan

    Lars narration "Each bloom carefully chosen to mark our path with a vibrant array of sunflowers and roses. Their vivid colors stand out, captivating the eye and creating a striking contrast against the backdrop of the serene oceanic landscape."

    Lars narration "The gentle breeze carries the sweet fragrance of the flowers, adding to the enchanting ambiance"
    
    show bg_2 at end_pan

    #panning ends
    show lars
    Lars "Ah, we arrived so early. I have to reward Spotsy well when we get back."

    show claude smile at center
    Claude "I’d be inclined to say that you didn’t manage to tap into our dragon’s full potential Captain. Owning up to how I stole your attention for more than half, or better yet, the entire ride."

    Claude "However, since you managed to get us here without any dangerous maneuvers, I’ll allow you to be the first person to touch our newest artifact."

    Claude "I tend to appreciate and reward my companions well, especially if they’re my lover—"

    show lars serious
    Lars "Being the first person to touch a suspicious artifact is the last thing I’d prefer to do."

    Claude "It’s the first time it’s made its way to our side of the realm, hence the occasion is quite momentous."

    show claude blush at center
    Claude "You could say the thrill is irresistible."

    hide lars
    Lars narration "He locks eyes with me, and I can’t help feeling a tad self-conscious under the weight of his declaration, whether it was actually meant for me or not."

    Claude "Let's not forget, the true essence of a discovery is experienced by the first person who ascertains it and not those who come later. Be it the second or the last to follow."

    Claude "If you don’t seize this moment now, who knows when you’ll get another chance like this? It will certainly be a captivating story to delight your future passengers."

    show lars
    Lars "Fine! Now let me focus before any of us plummet to their death."

    hide lars
    Lars narration "As the sole passengers aboard the dragon ship, guiding Spotsy in her safe descent was a seamless task."

    Lars narration "The proximity to the water offers a perfect opportunity for her to release some pent-up energy too. Hopefully, she’s not too tired from the journey. I’d hate to burn her out from the get-go. First impressions matter for dragons as well, especially when it concerns their pilots."

    Lars narration "However, once we disembark, our attention turns to the tall and slender magician making his way towards us."

    show sylvian at right with move:
        xpos 1.2
        linear 0.5 xalign 1.0
    show claude at left with move
    Lars narration "A warm smile graces his lips, accompanied by the graceful flutter of his obsidian wings."

    Lars narration "With a hushed incantation, the brim of his hat blossoms into a vibrant tapestry of roses and sunflowers, their delicate petals unfurling in a mesmerizing display. The air is instantly infused with their soft fragrance, which mingles with a refreshment spell."

    #"Unknown" "Welcome back, dear members of ‘Custodes Sylvae’. I’m happy to see that you both landed safely."
    Sylvian "Welcome back, dear members of ‘Custodes Sylvae’. I’m happy to see that you both landed safely."

    #"Unknown" "[Lars], your piloting was truly magnificent as always. It’s a sight that I’m honored to witness every time."
    Sylvian "[Lars], your piloting was truly magnificent as always. It’s a sight that I’m honored to witness every time."

    
    #move sylvian to the right
    Claude "Feel free to skip the cliché warm welcome, Boss Sylvian."

    show lars serious
    Lars "Sir Claude!"

    show sylvian mad at right
    show lars serious
    Claude "I know you're probably itching to have [Lars] by your side, but—"

    Lars "That’s enough! You can’t talk to our mentor that way."
    
    show lars
    Claude "Tsk, butter him up more, will you?"

    show lars
    show sylvian at right
    Sylvian "Nevermind him [Lars]. It's best to let the spotlight find its own stage rather than chasing after it."

    Lars "Thank you, Master. I wish you could have joined us on the ride too. Sir Claude here almost caused us to plummet to our doom...multiple times I must say."

    show claude shocked at left
    show lars
    Claude "Eh, I did promise to reward you later, didn’t I? Drum roll please ~"

    play sound sfx_drum_roll
    hide lars
    Lars narration "Tension fills the air as the anticipation builds up, drawing everyone’s attention. Then, in a dramatic display, he spreads his arms wide, showcasing a grand reveal which is…"

    stop sound
    Lars narration "…nothing?"

    Claude "Haha, I seem to have left it on the ship."

    show lars
    Lars "Should I go get it, then?"

    show claude smile at left
    show lars
    Claude "No need, my dear Captain. Boss Sylvian can handle it just fine. You and I have been quite busy, and the artifact box is heavy enough to demand a touch of fresh energy."

    show lars serious
    Lars serious "We can’t ask that from our senior, Sir Claude! Especially when I'm perfectly capable—"

    show lars serious
    Sylvian "Aren’t you tired from guiding our new dragon, [Lars]? I could easily fly and grab it for you. It’s no trouble at all."

    menu:
        " " " "
        "Ask Master Sylvian to grab the cargo for you":
            $ options["CS1"]=1
            jump ask_Sylvian_grab_cargo

        "Tell Sir Claude to grab the cargo himself":
            $ options["CS1"]=2
            jump tell_Claude_grab_cargo


label ask_Sylvian_grab_cargo:

    show lars happy
    Lars "Would that be alright with you Master? I’d like to spend some time with Sir Claude."

    Sylvian "I respect your choice [Lars], even though—"

    show sylvian blush at right
    Sylvian "I also wanted to spend some time with you…"

    Sylvian "But uhm, never mind, I suggested it in the first place after all."

    show claude serious at left
    Claude "Awe, you chose to stay with me instead of Boss Sylvian. I’m touched, Captain."

    Claude "I’ll have to give you a special reward later in private."

    hide lars
    show sylvian:
        linear 1.0 xalign 2.5
    show bg_2:
        parallel:
            linear 1.0 blur 15
        parallel:
            linear 1.0 zoom 1.2
    show claude smile:
        parallel:
            linear 1.0 xalign 0.5
        parallel:
            linear 1.0 zoom 1.1
    #move claude to the center
    #zoom on claude and blur background
    Lars narration "His hands gently encircle my waist, drawing me closer to him as he whispers the last part of his sentence."

    Lars narration "His eyes, akin to pools of molten sunlight, meet mine and a mischievous spark dances within them."

    Lars narration "While I might usually dismiss this as him being more touchy-feely than usual, his last comment makes me think otherwise."

    Lars narration "Yet, beneath that playfulness, there lurked a subtle undertone of competition, evident in the way he regarded Master Sylvian. It was as if they shared a friendly rivalry, each vying to outdo the other in their unique way."

    #slowly zoom to normal and unblur background
    show bg_2:
        parallel:
            linear 1.0 blur 0
        parallel:
            linear 1.0 zoom 1.0
    show claude smile:
        parallel:
            linear 0.5 xalign 0.0
        parallel:
            linear 0.5 zoom 1.0
    show sylvian mad:
        linear 0.5 xalign 1.0
    #move claude to left
    show lars blush
    Sylvian "Ahem!"

    show sylvian at right
    show lars
    Sylvian "Not to interrupt but I’m sure Rory will arrive soon, so it’s best to prepare yourself, [Lars]."

    Sylvian "As for you, Claude, remember what I said about teasing him too much?"

    show claude at left
    Claude "Before worrying about Captain over here, you should head on to where our new dragon is resting, Boss."

    Claude "We wouldn’t want her to accidentally drop our cargo to the depths of the sea."

    Sylvian "…"

    #In this section, since sylvian is taking flight, it would make more sense to have him transition out of the left side of the scene instead of simply hiding him. His sprite does a turn to the opposite side and after he exits, claude will move to the center
    show sylvian:
        linear 1.0 xalign -1.2
    Lars narration "Master Sylvian, without uttering another word, gracefully takes flight, his wings resembling those of a majestic black swan. Each feather ruffles in the breeze, catching and refracting slivers of sunlight, creating a mesmerizing shimmer which I didn’t know was possible."
    hide sylvian
    show rory:
        xalign -1.5
    Lars narration "However, a familiar voice rings in the air before I can observe any further."

    #claude moves to the right and rory comes in from the left
    show claude at right with move
    show rory at left with move
    #Word wave effect - sample in drive
    #"Unknown" "{bt}Clauuuuuuuuuuuuudy~{/bt}"
    Rory "{bt}Clauuuuuuuuuuuuudy~{/bt}"

    show claude smile at right
    #Word wave effect - sample in drive
    Claude "{bt}Roryyyyyyyyyyyyy~{/bt}"

    Lars narration "A figure emerges from where Master Sylvian stood just a few seconds ago, and to my pleasant surprise, it is none other than Rory- my childhood best friend."

    Rory "I believe I mentioned that if I ever catch you bossing [Lars] around, I’d pluck out your lizard eyes to adorn my newest puppet, Agatha."

    Rory "You should know that my threats work quite effectively, especially with how Brittina’s dress is bedazzled with the scales you’ve kindly donated...in your sleep, of course."

    Lars narration "True to her lineage as a bull descendent, Rory possesses a fiery temperament and is quick to charge at those who annoy her."

    Lars narration "The Kyoko blacksmiths and the Dupont merchants have been locked in a spirited rivalry for generations. Both families have passed down their competitive natures to their heirs, adding fuel to the fire."

    Lars narration "However, Rory was an exception to the traditional path of the Kyoko family. While blacksmithing was the cornerstone of their legacy, Rory’s talents lay elsewhere. She found her passion in puppet shows and other forms of artistic expression."

    Rory "[Lars], you’re here too!"

    Rory "Awe, I missed you so much."

    show lars happy
    Lars "Rory, it’s so nice to see you again. I missed you too."

    Claude "If it isn’t our hot-tempered bull, breathing fire as soon as she lays eyes on me."

    Claude "It’s a pleasure to see you again, little Rory. Or should I say, a curse to behold?"

    show lars
    Lars "Guys, stop bickering like two little kids for once—"

    show rory angry at left
    Rory "It’s just RORY! Call me a midget again, and you'll find more of your receding hairline gracing puppet Alex…"

    Claude "Now, now, I would have to say these finely braided silver strands that I’ve so kindly donated to you are what’s bringing half the revenue for your puppet shows, aren’t they little Rory?"

    #Rory jumps up and down once for the next sentence
    show rory at jp
    Rory "You really have the gall to talk to me like that, when all your travel funds are conveniently collected from my shows?!"

    Rory "Such audacity doesn't appear out of nowhere unless the heat has really gotten to your head."

    show rory at left
    Rory "How about a calming dip in the sea to cool off a bit? I could  help you out with a gentle push~"

    Lars "How about we all cool down for a sec—"

    Claude "I'm sure the hydro dragons would be delighted to have me amongst them."

    Rory "Hmph, you could put your merchant skills to use there, too. Ten more seconds to live for a platter of rotten lizard meat."
    show sylvian:
        xalign -1.5
    Sylvian "I’m back with the cargo!"

    #sylvian comes in from the left side, rory stays on the right and claude is in the center
    show claude at center with move
    show rory at right with move
    show sylvian at left with move
    hide lars
    Lars narration "Thankfully, Master Sylvian swiftly intervenes, diffusing the tension with his timely return. It's always a relief when he steps in; the two never listen to me when they start arguing, but his authority commands attention."

    Lars narration "The weight of anticipation fills the air, drawing all eyes toward the mysterious object, and momentarily, the conflict is forgotten."

    jump CS_1_End

label tell_Claude_grab_cargo:

    show lars
    Lars "Sir Claude, can you bring the artifact yourself? I’d like to spend some time with Master Sylvian."

    show claude shocked at center with move
    show lars
    Claude "I’m shocked, Captain. Choosing Boss Sylvian over me?! I wouldn’t have imagined."
    
    show lars
    Claude "You even ignored my request about dropping the ‘Sir’ part."

    show sylvian at left with move
    show lars
    Sylvian "I am grateful that you wish to share your time with me, [Lars], even if you’re tired from your journey."

    show lars
    Sylvian "Rory will arrive soon as well, so we all can spend some time together."

    hide lars
    Lars narration "Master Sylvian gently touches the brim of his hat and a magnificent bouquet blooms forth."

    hide sylvian
    hide claude
    show sylvian_bouquet
    Lars narration "Sunflowers rise proudly, while lavender blossoms intertwine. Brilliant clusters of marigolds sprout forth as well."

    Lars narration "I remember that his hat was one of his personal crafts, a magical creation that bloomed flowers according to his mood."

    Lars narration "It’s unfortunate that I’m not well—versed in flower languages; otherwise, I would be able to decipher the heartfelt messages he wishes to convey through these enchanting floral gifts."

    Lars narration "Nonetheless, I can’t help but feel treasured whenever he gives me gifts. After all, I’ve noticed that he hasn’t given this kind of gift to anyone else, and the thought warms my heart for some reason…"

    hide sylvian_bouquet
    show claude serious at right
    show sylvian at left
    show lars
    Claude "Quite the showmanship, Boss."

    show sylvian mad at left
    Claude "Though I wonder if Captain over here got the message in your subtle gesture."

    show sylvian blush at left
    hide lars
    Lars narration "Without regarding his comment, Master Sylvian comes closer and presents me with the bouquet, throwing a smile at Sir Claude who promptly leaves with his back towards us."

    #claude turns his back towards sylvian and exits the scene here from the right. Sylvian moves to the center and the camera zooms in on him with a blurred background
    show bg_2:
        xalign 0.5
        yalign 0.5
        parallel:
            linear 2.0 blur 15
        parallel:
            linear 2.0 zoom 1.2
    show claude serious:
        linear 1.0 xalign 1.5 
    show sylvian blush:
        parallel:
            linear 1.0 xalign 0.5 
        parallel:
            linear 2.0 zoom 1.1 
    
    Sylvian "These are for you [Lars], I hope you like them. They may not resemble your brilliance the way they should."

    Sylvian "Even still, flowers are the silent poets of our emotions, conveying in colors and scents what words often struggle to express."

    Lars "Thank you, Master. Though I'm a bit uncertain about the sudden gesture, I appreciate it nonetheless."

    Sylvian "That’s more than enough for me."

    #zoom out and unblur background
    show bg_2:
        xalign 0.5
        yalign 0.5
        parallel:
            linear 2.0 blur 0
        parallel:
            linear 2.0 zoom 1.0
    show sylvian:
        linear 2.0 zoom 1.0
    Sylvian "Moving on, it might be best for you to take care of your task, Claude."

    #claude comes in from the right and sylvian goes to the left
    show sylvian at left with move
    show claude at right with move
    Claude "So glad that nauseating scene was over."

    show sylvian mad
    Sylvian "Be careful with your words Claude."

    Claude "Mhm, sure sure."

    Sylvian "Better yet, I believe it's best for you to leave for the moment. We’re still not sure of the origins of the artifact you brought and there needs to be a level of caution involved as well."

    show lars
    Lars "That’s exactly what I said!"

    show sylvian at left
    hide lars
    #claude turns his back towards sylvian and exits the scene here from the right, sylvian comes to the center
    show claude serious:
        linear 1.0 xalign 1.5 
    show sylvian at center with move
    Lars narration "As Sir Claude takes his leave, his silver lizard tail gracefully sways behind him, reminiscent of the rhythmic movements of the sea. His scales, resembling those of the majestic dragons I often encounter in my journeys, captivate my gaze with their intricate detailing, despite their diminutive size."

    Lars narration "However, a familiar voice rings in the air before I can observe any further."

    #sylvian goes to the left and rory comes in from the right
    show sylvian at left with move
    show rory at right
    Rory "[Lars]!"

    show lars happy
    Lars "Rory, it’s so nice to see you again!"

    Rory "You too! And good to see that slithering, slimy tail going away."

    hide lars
    Lars narration "The figure that emerges from where Sir Claude stood just a few seconds ago, is none other than Rory, my childhood best friend. True to her lineage as a bull descendent, Rory possesses a fiery temperament and is quick to charge at those who annoy her."

    Lars narration "Under Master Sylvian’s guidance, she apprenticed as the guild’s head of finance, helping us gather funds for every mission through her puppet shows."

    Rory "Mentor, I was preparing my puppets for the afternoon show at the market square."

    Rory "I feel like something is missing but I don’t know what exactly…"

    Sylvian "Let’s work together to find something to inspire you before the show, shall we?"

    Rory "Thank you, Mentor. I don’t know if my family will be there but I don’t want to disappoint them in case I miss the mark with the show later today."

    Lars narration "The Kyoko blacksmiths and the Dupont merchants have been locked in a spirited rivalry for generations. Both families have passed down their competitive natures to their heirs, adding fuel to the fire."

    Lars narration "However, Rory was an exception to the traditional path of the Kyoko family. While blacksmithing was the cornerstone of their legacy, Rory’s talents lay elsewhere. She found her passion in puppet shows and other forms of artistic expression."

    Rory "They’re already giving me side glances for not working with them in the blacksmiths."

    Sylvian "Do you need me to talk with them, Rory?"

    Lars narration "Rory offers a faint smile, her thumbs anxiously twiddling together."

    Rory "There’s no need. They’re the type to be appeased with actions rather than words. The best I can do is prove that I was made for the puppeteer business."

    Rory "When life gets tough, I just have to remember to stay strong and keep charging!"

    show lars happy
    Lars "Haha! That’s right, Rory, it’s not about the size of the bull, it’s about the size of its determination!"

    show rory angry at right
    Rory "Come on, [Lars]. No shorty jokes. A certain someone spews enough of them already."

    Lars "Alright, alright. I’ll make it up to you by helping you out for the show."

    show rory at right
    Rory "Yay~ Thank you!"

    Claude "I have arrived with our mystery artifact."

    #claude comes in from the right and moves to the center, sylvian is still on the left and rory on the right
    show claude at center with move
    hide lars
    Lars narration "Speaking of the devil, Sir Claude makes his entrance with the grande and ornate box held tightly by his tail. His eyes glimmer with a mixture of anticipation and excitement."

    Lars narration "However, rather than keeping it for himself, he extends the box towards me."

label CS_1_End:

    Lars narration "As the  heavy weight of the artifact transfers to my hands, I feel a sense of responsibility settle in."

    if options["CS1"]==1:

        show lars
        Lars "I think I can take it from here, Master."

        show sylvian at left
        Sylvian "Carrying such things after your tiring journey might affect your health, [Lars]."

        show sylvian blush at left
        Sylvian "But thank you for worrying about me…I really appreciate it coming from you."



    else:

        show lars
        Lars "I think I can take it from here, Sir Claude."

        show claude smile at center
        Claude "Anxious for the reveal. Aren’t you?"

        Claude "Don’t worry, I’m not a fan of breaking promises. Especially, for one I made with you."

    show sylvian at left
    Sylvian "Let me cast an energizing spell for you just in case, [Lars]. I wouldn’t want you to hurt yourself carrying something heavy like that."

    Sylvian "If there’s one thing my academic days have taught me, it is to not overwork when there’s an easier alternative available."

    Sylvian "No one will truly appreciate your effort if you're the sole person assigning value to it…"

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
    Lars "Yes, please. This box isn’t doing me any favors either."

    #Word wave effect for  ‘Claudyyyy’- sample in drive
    Rory "How about you tell me what the trip was like, {bt}Claudyyyy?{/bt}"

    Claude "Hold on, little Rory, where do you think you’re taking me all of a sudden—"

    hide lars
    #sylvian comes to the center and the other two leave the scene
    
    show rory:
        linear 0.5 xalign 2.0
    show claude:
        linear 0.5 xalign 2.0
    #vertigo effect - sample in drive
    show sylvian:
        linear 1.0 xalign 0.5
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

    Lars narration "Instantly, Master Sylvian utters an incantation and a sense of liveliness washes over me, like the exhilaration that follows after completing a marathon."

    Sylvian "Are you feeling better now? I could conjure up some stalks to help with the box as well—"

    show lars
    #Speeding up the rambling text A LOT and make the text itself shake a bit / the screen can also shake a little - whichever you think gives off a better impression for the scene
    Lars "{sc}It’s okay Master, I need to get in my daily dose of exercise too.\n I don’t want you to think that I’m too weak for one box! \n More than that, what would our passengers think if their pilot wasn’t able to pick up\n their luggage or equipment?{/sc}"
    Lars "{sc}My parents wouldn’t let me live this down if they ever heard such rumors \nsince they raised me to give my all to take care of those around me considering—{/sc}"
    show sylvian serious funny at center
    Sylvian "Oh my, such an interesting result…"

    Lars "{sc}Haha, nothing to worry about! But did you know, Master Sylvian? I was researching\n Spotsy and as part of the Roseate Flame species, the intense temperature generated \nthrough their breathing process can cause the air pockets under their scales to bubble \nand expand.{/sc}"
    Lars "{sc}Their flushed distortions aren’t for mere show either, Rory mentioned that certain \nblacksmiths hire them for their forging practices since the heat produced is \n exceptionally hotter than regular flames, making it a valuable resource for crafting \nextraordinary weapons and armor—{/sc}"

    Sylvian "As much as I enjoy hearing you talk about the dragons which you treasure, we need to calm you down a little. Let’s use that breathing technique that I taught you last time. You remember, [Lars]?"

    hide lars
    show bg_2:
        linear 1.0 blur 15
    show sylvian blush:
        linear 1.0 zoom 1.1
    #zoom in on sylvian, blur background / the two effects can go on in the background albeit slower
    Lars narration "{sc}He takes my hand into his own, slowly tracing circles on my palm. His touch feels warm,\n and there’s a slight hint of perspiration, as if he’s nervous about holding it.{/sc}"

    Sylvian "Breathe for 3 seconds…hold it for 6…now release it for 9 seconds…"

    #Word shake ends and the screen shake becomes even slower here and ends after the next sentence
    Lars narration "Obediently, I follow Master’s instructions, allowing my breath to gradually slow down. Despite my heart still thumping in my chest, each measured inhale and exhale brings a sense of calm that envelops me, grounding me in the present moment."

    #screen shake ends
    Sylvian "No one is going to think those things of you, [Lars]."

    Sylvian "If I were a dragon, I wouldn't want any pilot other than you to take care of me. I've seen how you praise their efforts and spoil them senselessly."

    Sylvian "I mean, who wouldn't want to be praised by someone they admire...I mean, not that I admire you in that way, but ughhh...nevermind!"

    Lars narration "Suddenly, he takes hold of the tips of my fingers, as if he’s shying away from holding my hand fully. I'm sure my ears are flushed all the way from the sweetness of his shy gesture."

    Claude "So, what I gather is that Master Sylvian wants to have [Lars] ride him—"

    #zoom out and blur background, claude and rory come in. claude is in center while rory is on the right. Sylvian is pushed to the left
    show bg_2:
        linear 1.0 blur 0
    show sylvian mad:
        parallel:
            linear 0.5 zoom 1.0
        parallel:
            linear 0.5 xalign 0.0
    show claude at center with move
    show rory at right with move
    show lars
    Lars "Since when were you two here?"

    Rory "Sorry Master, I couldn’t keep him occupied any longer."

    Lars narration "In the blink of an eye, Master Sylvian's demeanor shifts. He turns his head away, almost as if he's trying to conceal his reaction to Claude's statement. Yet, even from behind, I catch a glimpse of his ears slightly reddening."

    Claude "My my, my, are you feeling hot all of a sudden, Boss? Maybe it’s because of all the cloaks and layers you’re wearing."

    Lars "He's joking, Master Sylvian. Just forget about him. I appreciate the energizing spell, even if it didn't work out like we thought."

    show sylvian serious funny
    Sylvian "Definitely not. I'll have to look into ways to tweak it for better results in the future."

    show lars happy
    Lars "And not just that...I, um, wanted to thank you for helping me stay calm and for the motivational words. It's not often that someone praises my dragon skills. I thought no one really cared."

    show sylvian blush
    Sylvian "OF COURSE I DO!"

    hide lars
    Lars narration "Wow, it’s not often that he raises his voice like that."

    Sylvian "I don't think it's the right place to talk about this, but know that I always keep you in my mind, Lars. You’re really precious to me- ah, I meant, to our guild. Not only to me, of course. I mean you are but ugh-"

    show lars
    Lars "Haha, I know, Master. You're not just a Boss to me; you're a friend as well."

    Sylvian "Ah, what a joy to be  just a friend to you…"

    Sylvian "Maybe my own lack of directness caused this in the first place."

    Lars "Pardon me?"

    Sylvian "N-N-Nothing, uhm, yeah, nothing to concern yourself with. Let’s analyze the artifact now, shall we?"

    jump S_1_End

label reject_his_offer:

    show lars
    Lars "Thank you for the offer, Master. But it’s nothing I can’t shake off."

    show sylvian sad at left
    hide lars
    Lars narration "He looks dejected, and now I feel guilty about declining his kind proposal. However, just as awkwardness begins to set in, Sir Claude arrives with Rory behind him."

    #push sylvian to the left
    show claude at center
    show rory at right
    Rory "Looks like I didn’t need to keep him occupied in the first place."

label S_1_End:

    show claude serious at center
    show sylvian at left
    Claude "Ehem, I think we’re better off witnessing the artifact before the evening sets in and little Rory decides to pull something off for her puppets again."

    show rory angry at right
    Claude "I can see fumes coming out of her head as we speak. Oh look! I think they got even bigger."

    Rory "Ugh, I can’t deal with this again."

    show lars
    Lars "Alright everyone, settle down. What should we do now, Master?"

    Sylvian "Let me cast a safety spell over the box first, you can never be sure if there are any hidden traps inside."

    hide lars
    Lars narration "After a few seconds of inspection without any notable reactions, Master Sylvian breaks the silence."

    Sylvian "No traps or enchantments detected. It seems we’re in the clear."

    Claude "Time to witness the treasure within, Captain."

    hide rory
    hide claude
    hide sylvian
    show normal_necklace
    Lars narration "As I carefully open the ornate box, I discover a beautiful necklace inside. It features a simple leather band and a captivating centerpiece-a stunning red gem with a mesmerizing ruby hue."

    Lars narration "The longer I gaze at it, the more an unsettling feeling creeps in, as if it could ensnare my focus. Shivers run down my spine, and my fur stands on end, reacting to some unseen energy."

    Claude "Before anyone starts their inspection, I promised our dear Captain he’d be the first person to hold it."

    hide normal_necklace
    show lars serious
    show claude at center
    show sylvian at left
    show rory at right
    Lars "Thanks, but no thanks, Sir Claude. My instincts are warning me about this artifact, something seems off about it."

    Claude "It wouldn’t hurt to at least hold it in your hand, would it?"

    hide lars
    Lars narration "I direct my gaze towards the opened box, feeling the weight of everyone’s anticipation upon me. Carefully lifting the necklace from its resting place, I note its light size despite the box’s heftiness."

    show lars
    Rory "Wow! It’s truly a work of art."

    show sylvian serious funny at left
    Sylvian "Indeed, it’s a testament to the skill and craftsmanship of the civilization that created it. But who and when exactly?"

    show claude at center
    Claude "We have no idea about its origins yet, but that’s the fun part of it all."

    Claude "Not to mention, I could never let go of such a mysterious prize, I need to uncover its secrets all for myself…"

    hide lars
    Lars narration "Sir Claude’s expression undergoes a striking transformation, shifting from one of casual curiosity and playful mirth to that of intense obsession. His eyes fixate unwaveringly on the artifact, a glimmer of determination and fervor dancing within them."

    Lars narration "It is no secret that he possesses a deep-seated fascination with challenges and trials. Though he seldom shares the reasons behind his unwavering obsession, his eyes betray his inner excitement whenever faced with such an opportunity."

    show lars
    show claude smile at center
    Claude "…Ahem, with the help of our prestigious scholar as well of course!"

    Claude "Boss Sylvian, you have quite the reputation in the academic world for your discoveries and inventions. If someone were to understand the potential behind this artifact, it would be none other than you."

    show rory angry at right
    Rory "Ugh, quit trying to suck up and get close to my Mentor with your scale-rotten face."

    Claude "Weren’t these the very same scales you took for that one specific doll of yours? Admit it, you just don’t measure up to scale. Specifically, my scales!"

    Claude "Hmm, what was it called again? Boring-ina? Boorish-ina? Banal-ina?"

    Rory "It was BRITTINA, you dagger-mouthed, bark-bellied, algae-breathing gullet on legs—"

    show sylvian serious funny
    Sylvian "Oh dear…things are starting to get out of hand."

    show lars serious
    Lars "Come on guys, it’s time to stop. We’re losing daylight over here."

    hide lars
    Lars narration "As always, neither side showed any signs of stopping their retort. After all, the first to stop would be the first to lose and their competitive nature wouldn’t allow them this leeway."

    show claude at center
    show lars
    Claude "It’s no wonder that your family legacy is going to die with you. I wouldn’t put myself in the low position of insulting you, though it’s a huge plus if I do."

    show lars serious
    Lars "Claude, that’s not like you to—"

    Rory "Look, I think we all have something to bring to this conversation, but you don’t. Especially when all you ever have to add is self-inserted praise and narcissism."

    Lars "Come on Rory, you don’t really mean that—"

    show sylvian mad
    Sylvian "Both of you, it’s time to stop."

    show claude shocked at center
    show rory at right
    hide lars
    Lars narration "Master Sylvian's voice echoes through the air, instantly commanding everyone's attention and calming the conflict-ridden atmosphere."

    Lars narration "While he typically exudes a collected composure, there are occasions when he utilizes his authoritative voice to instill a sense of order among those around him."

    Lars narration "It's a captivating contrast, witnessing the guild leader within him command respect and bring about a calm atmosphere."

    show lars
    show sylvian at left
    Sylvian "Let us embrace empathy’s grace and refrain from jesting, for each soul carries its own unique beauty. Whether it be lizards, foxes, swans, or bulls."

    Rory "Sorry, Mentor. Looks like I’ve overstepped a bit."

    show claude at center
    Claude "It’s never a good move to annoy your benefactor. Apologies, Boss."

    hide lars
    Lars narration "As Claude and Rory move away to not bump heads again, I quietly make my way towards Master Sylvian."

    #claude and rory exit from the right, sylvian moves to the center
    show rory:
        linear 0.5 xalign 2.0
    show claude:
        linear 0.5 xalign 2.0
    show sylvian:
        linear 1.0 xalign 0.5
    show lars
    Lars "Thanks for easing off the tension, Master. It gets out of hand when they start bickering."

    hide lars
    Lars narration "A shy smile graces Master Sylvian’s lips as he gently rests his hands on my shoulders. The feathers of his swan-like wings delicately brush against my back, imbuing me with a sense of tranquility and ease."

    show lars
    Sylvian "No problem at all, [Lars]. I might not understand your relationship with Rory well, as you have been best friends from a young age…but I would hate to see a rift between us as guild members."

    Sylvian "Your bond with Rory holds a treasure untold. A childhood’s embrace worth more than gold."

    show sylvian sad at center
    Sylvian "I wish I could have that kind of equal friendship too."

    hide lars
    Lars narration "What should I do now?"

    menu:
        " " " "
        "Poke further and ask why he’s feeling that way":
            $ options["S2"]=1
            jump poke_further_and_ask

        "Joke about his statement and steer the conversation":
            $ options["S2"]=2
            jump joke_about_his_statement


label poke_further_and_ask:

    Lars narration "It’s not like Master Sylvian to feel this way, and seeing him slightly melancholic leaves me with a sense of concern."

    show lars
    Lars "What do you mean, Master. Are you saying we aren’t friends? Did our departure make you lonely?"

    hide lars
    Lars narration "He shakes his head a bit, as if trying to clear his thoughts."

    Sylvian "It’s just that as your superior, I don’t have the equal relationship that you have with Rory or Claude—"

    show lars
    Lars "You know, even though I'm just your junior, you're a cherished friend to me. Of course, I value you first and foremost as our Boss, but I also appreciate how you're always kind to everyone."

    hide lars
    Lars narration "Summoning all my courage, I move closer and grasp Master Sylvian’s hands, locking my gaze with his."

    
    #zoom in on sylvian, blur background
    show sylvian blush at center:
        linear 1.0 zoom 1.1
    show bg_2:
        linear 1.0 blur 15
    Lars narration "The initial shock on his face gives way to a warm and genuine smile, a flicker of happiness illuminating his eyes."

    show lars
    #Speeding up the rambling text A LOT
    Lars "{cps=999}I'm sorry if it sounds like I'm trying to, you know, suck up to you or ask for something. That's really not my intention at all. It's just— Well, I tend to be pretty straightforward, especially when dealing with stray dragons. I mean, not that I'm saying you're anything like a stray dragon! I guess what I'm trying to say is, ugh...{/cps}"

    Lars "I get kind of tongue-tied during situations like this."

    Sylvian "Hahahaha! Haha…"

    Sylvian "Ah, what a delight you are [Lars], what would I do without you to brighten up my day? A stray dragon, you say?"

    show lars blush
    Lars "Come on, Master, I have a reputation to keep as a dragon pilot. You can't go around telling everyone that I compared my guild master to a stray dragon. I'll never hear the end of it from Rory and Sir Claude."

    hide lars
    Lars narration "I shake my head in mock frustration, burying my face in my hands. Master Sylvian always falls for these antics, especially when someone asks for his help or a favor."

    show sylvian blush at center:
        linear 1.0 zoom 1.0
    show bg_2:
        linear 1.0 blur 0
    show lars happy
    Sylvian "It's alright, [Lars], just lift your head and look at me. I'll keep our little secret safe, just between us, alright?"

    hide lars
    Lars narration "As if understanding my need for reassurance, he gently pets me on the head, softly rubbing my ears in the process."

    show lars blush
    Sylvian "Don’t worry about me too much, [Lars]. It’s just that…it’s hard to bring out the words that build up in your throat sometimes."

    Sylvian "But I do appreciate your efforts, I just hope that I can be the recipient of your more endearing efforts as well."

    jump S_2_End

label joke_about_his_statement:

    show lars
    Lars "Don’t worry about it, Master!"

    Lars "I have never seen a person more talented than you in casting spells and dazzling up the atmosphere with flower magic. I’m sure that if you whip up a quick spell, you’ll have everyone fighting to be your friend."

    show sylvian sad at center
    Sylvian "It’s no use tricking people into becoming your companions, [Lars]."

    Sylvian "We used to have a lot of rivalry back in the Tower of Magicians. Your comment reminds me of those days where we would try and use every trick up our sleeves to get ahead."

    Sylvian "I wish to never go back to those days if possible. After all, ‘Custodes Sylvae’ is my current solace."

    hide lars
    Lars narration "In an instant, the atmosphere shifts, and a wave of melancholy washes over Master Sylian. His hands, once tranquil, now tremble slightly, and the furrow on his brow deepens as if he's grappling with memories etched on his face."

    Lars narration "His jaw tightens, a silent struggle playing out in the subtle lines that trace his expression. It's as if he's transported himself back to moments he'd rather keep buried, and the weight of untold stories lingers in the air."

    show lars sad
    Lars "Uhm, Master, I might have misphrased it, but we enjoy your company as fellow guild members."

    hide lars
    Sylvian "It’s okay [Lars], I’m just getting upset on my own."

    Lars narration "My words don’t seem to be reaching him anymore, it seems."

label S_2_End:

    show lars
    show sylvian serious funny at center
    Sylvian "EVERYONE! Steadfast now."

    #claude and rory come in again, sylvian on the left, claude in center, and rory on the right
    hide lars
    Lars narration "As everyone settles under Sylvian’s gentle yet authoritative command, he takes hold of the artifact, brimming with curiosity."

    Sylvian "It’s time to get back to business. I’d like to observe this a bit more in my lab as well."

    hide sylvian
    show normal_necklace
    Sylvian "It eerily resembles an artifact that I had previously seen in the Archmage's tower. A one-of-a-kind necklace with a similar gemstone belonging to a family of dragons with our very own half-human, half-animal traits as descendants."

    Sylvian "I haven’t heard of them in quite some time, and though the color of its gem contrasts the descriptions I’ve heard and read, the artistry is quite similar."

    hide normal_necklace
    show lars
    show sylvian at left
    show claude at center
    show rory at right
    Sylvian "Speaking of which, how much did you exchange for it, Claude? We need to see if the funds from Rory’s recent puppet show will be able to cover the costs."

    show claude smile at center
    Claude "A merchant only parts with what they're willing to share. Fortunately, the notorious Claude can conquer any challenge he wishes for at his own behest."

    Claude "I received this curious box free of charge. The seller was practically begging me to take it."

    Claude "Ah, the misery of knowing the world will fit into the palm of my hand as long as I aim for it."

    hide lars
    Lars narration "Rory’s eyes widen to an almost comical extent, as if they’re on the verge of rolling out of their sockets. As for Master Sylvian, he merely closes his eyes, whether he’s focusing on what Sir Claude is saying or mentally preparing himself for any upcoming conflicts…I can’t tell."

    show lars
    Rory "Narcissus left a voicemail, saying he's issuing the world a mental refund for the surplus of self-absorption you're currently exuding."

    Claude "Getting real creative with the insults, aren’t you?"

    show rory angry
    Rory "I have never meant anything more in all my bull years."

    Claude "That explains why you’re such a bullshitting—"

    Sylvian "Ehem! Let’s move on, shall we?"

    hide lars
    Lars narration "Nice save as always."

    show lars
    show rory
    Rory "By the way Mentor, can I take this artifact for a spin before you put it in your lab?"

    Rory "I could whip up a show-stopping puppet in no time with it."

    show claude shocked
    Claude "But that’s absurd, who knows when your puppet project is going to finish?"

    show lars
    Lars "That’s a great idea. We could come and visit your puppet show stall this way too. It’s been quite a while since I last played with the kids."

    Sylvian "If you feel inspired by this artifact, then by all means, go ahead."

    Claude "Not you too, Boss…"

    show claude smile
    Claude "Captain, how about you wear the necklace for now instead of little Rory? It’s color suits your fur, after all."

    show rory angry
    Rory "Not with the little Rory comment again—"

    Claude "It reminds of the red string of fate, though, placing your faith in such notions is for those incapable of steering their own lives."

    show lars
    Lars "These confession jokes are getting really out of hand."

    hide lars
    hide rory
    hide claude
    hide sylvian
    show normal_necklace
    Lars narration "Alas, disregarding Sir Claude’s comment, I take the moment to put on the necklace, the gemstone’s ruby color captures my attention and I marvel at the curious glow that emits from it."
    
    hide normal_necklace
    show shining_necklace
    Lars narration "It’s strange though, I don't recall the color being so vibrant. It’s almost as if it’s shining or signaling something."

    hide shining_necklace
    show rory at center
    Rory "Let’s go [Lars], or you’ll get left behind~"

    show lars
    Lars "I’m coming, wait for me!"

    play sound sfx_grassy_walk
    Lars narration "Shaking off my trance, I hasten toward the others who have gathered ahead."

    #sylvian comes in from the left, and rory moves to the right
    Lars narration "Master Sylvian deliberately slows his steps and I pass him. Looks like he’ll be keeping a watchful eye over the rest of us as we go ahead."

    #claude comes to the center but I want there to be a little distance between sylvian and rory+claude here, like a gap in the center to make it seems like the two are walking further ahead
    Lars narration "Meanwhile, Claude and Rory pick up their pace, engaging in a competition to see who can reach the puppet stall first. Their banter fills the air as they exchange witty remarks, not holding back on their rivalry."

    Lars narration "Hopefully, it’ll be another day without any troubles here in Divonia and ‘Custodes Sylvae’."

    stop sound fadeout 2.0
    #adding this in, let’s make sure to have the sfx fade out instead of suddenly stopping it
    $ renpy.choice_for_skipping()
    play music "track_3_the_town.ogg"
    scene bg black with fade
    show bg_3 at pan with fade

    play sound sfx_people_talking
    #panning effect - sample in drive
    Lars narration "The town square pulsates with vibrant energy with the captivating tapestry of stalls embellishing the grassy pathway."

    show bg_3 at end_pan
    
    Lars narration "As I walk through this bustling scene, my attention is drawn to the medley of merchants enticing passersby with their wares, creating an atmosphere of enchantment and wonder."

    Lars narration "The tantalizing scents of delectable dishes waft through the air, drawing in hungry travelers, including myself, with promises of culinary delights."

    Lars narration "As I stroll along, my mind wanders to my guildmates, and I can’t help but imagine them donning different attire from the clothing boutiques."

    Lars narration "My imagination runs wild with visions of my guildmates donning different attire from the stalls."

    show bg_3:
        parallel:
            linear 1.0 xalign 0.5
        parallel:
            linear 1.0 zoom 1.0
    stop sound fadeout 1.0
    #adding this in, let’s make sure to have the sfx fade out instead of suddenly stopping it
    show rory at center
    #maybe we could do bottom to top zoom on the sprite here, as if we’re showcasing the clothing and then zoom out when finished
    Lars narration "Rory comes to mind first as my best friend. A practical and independent soul, whose artistic flair and unique personality are effortlessly mirrored in her attire."

    Lars narration "Her outfits are accessorized with charming trinkets. Practical short sleeves allow her to move with ease, while thoughtfully designed pockets serve as clever storage for her beloved tools and equipment for her puppet shows."

    Lars narration "Particularly her emergency puppets, which always seem to come to the rescue in unexpected situations."

    hide rory
    Lars narration "Hmm...who else comes to mind?"

    menu:
        " " " "
        "Master Sylvian’s academic outfit":
            $ options["CS2"]=1
            jump master_Sylvian

        "Sir Claude’s merchant outfit":
            $ options["CS2"]=2
            jump sir_Claude

label master_Sylvian:
    show bg_3 at bg_blur:
        linear 0.5 zoom 1.5
    show sylvian at center:
        parallel:
            linear 0.5 zoom 2.0
        parallel:
            linear 0.5 yoffset 600
            linear 9.0 yoffset 200

    #maybe we could do bottom to top zoom on the sprite here (with a blurred bg), as if we’re showcasing the clothing and then zoom out when finished. However, we have to make sure that we move section by section so if the player doesn’t progress through the text, the animation doesn’t end early
    Lars narration "As a flower magician, Master Sylvian weaves his clothing with delicate floral spells, each stitch carrying the soft whisper of his incantations."

    Lars narration "His fondness for deep, shadowy hues consistently manifests in his attire—a seamless blend of midnight-hued blossoms that effortlessly complement the color palette of his elegant, swan-like wings."

    Lars narration "There’s also his signature personally-crafted magician’s hat. He once mentioned that this unique accessory serves to stabilize the emotional energy he channels, transforming it into an array of different blooms."

    Lars narration "I wish I had the ability to decipher the meaning behind the flowers that draw from his emotions. Yet, my knowledge in this area primarily revolves around memorizing names of plants and herbs safe for dragons - avoiding accidental poisonings, preventing ailments, and ensuring respectful offerings, among other practical considerations."

    Lars narration "Nevertheless, next to Master Sylvian, my understanding barely scratches the surface. He may downplay it, but getting to his level of expertise seems like it would take a century, if not more."

    Lars narration "That's one of the many things I admire about him—being so knowledgeable yet never shying away from wanting to discover more about the world and the people around him."

    show bg_3:
        linear 0.5 zoom 1.0
    show sylvian:
        parallel:
            linear 0.5 yoffset 0
        parallel:
            linear 0.5 zoom 1.0
        parallel:
            linear 0.5 xalign 0.0
    show rory at right with dissolve
    show claude at center with dissolve
    show lars

    jump CS_2_End

label sir_Claude:
    show bg_3 at bg_blur:
        linear 0.5 zoom 1.5
    show claude at center:
        parallel:
            linear 0.5 zoom 2.0
        parallel:
            linear 0.5 yoffset 600
            linear 9.0 yoffset 200
    #maybe we could do bottom to top zoom on the sprite here (with a blurred bg), as if we’re showcasing the clothing and then zoom out when finished. However, we have to make sure that we move section by section so if the player doesn’t progress through the text, the animation doesn’t end early
    Lars narration "Sir Claude always holds his appearance with unparalleled pride. I can envision him draped in a new style of opulent faux fur and leather clothing curated from exotic lands courtesy of his family, and even his own, well-established connections."

    Lars narration "Surrounded by a retinue of devoted servants, he could easily present with a garment thoughtfully designed to accentuate and showcase his glistening scales, and maybe even leave an opening for his enormous tail."

    Lars narration "But, given his independent streak, I wouldn't be surprised if he goes with whatever catches his eye, not caring much about what's in vogue among the nobles or even paying attention to the advice of his fashionista advisors."

    Lars narration "Just looking at him now, with those silver braids cascading down his back, I’m served a gentle reminder to do something about my own unruly fox fur and maybe tidy up my ponytail."

    Lars narration "That's one of the many things I admire about him—being his own source of inspiration without having to make a conscious effort to appeal to others or impress them."

    show bg_3:
        linear 0.5 zoom 1.0
    show claude at center:
        parallel:
            linear 0.5 yoffset 0
        parallel:
            linear 0.5 zoom 1.0
        parallel:
            linear 0.5 xalign 0.5
    show rory at right with dissolve
    show sylvian at left with dissolve
    show lars

label CS_2_End:
    
    Rory "I don’t think I need to mention this, but if any of you happen to spot my parents, could you...convince them to attend the show?"

    show claude at center:
        yoffset 0
        zoom 1.0
    show sylvian at left:
        yoffset 0
        zoom 1.0
    Rory "I’ve tried inviting them countless times, but they always manage to find an excuse. Maybe…if someone else were to extend the invitation, they might feel too embarrassed to decline."

    hide lars
    Lars narration "Rory’s family always took pride in showcasing their meticulously crafted armors and weapons, forged over the years. Whenever I pass by their stall, I can’t help but be awestruck by the gleaming steel and the intricate designs that speak of their unwavering dedication to their art."

    Lars narration "It’s no surprise that if anyone were to harness the shimmering blazes of the Roseate Flame, it would be them, for they embody the spirit of the forge and the indomitable strength of their bull lineage."

    show claude serious at center
    Claude "Let it be known that I’m only helping out because I want to spend some more time with Captain [Lars] over here. Otherwise, I’d be indulging in a cool shade at my family’s own tradepost. After all, who knows what new trinkets await to be blessed by my presence when I’m there."

    Lars narration "The Dupont family are notorious for their array of foreign novelties; enticing visitors with a fascination for distant lands and cultures. Their stalls are always filled with rare and luxurious items, each one carefully curated to capture the attention of potential buyers seeking something unique for an exorbitant price."

    show claude serious at center
    show sylvian mad at left
    Claude "Who knows, my dear Captain, some of them might just complement your new necklace perfectly. I'd love to see them on you during our adventures. I can already picture a fantastic matching set—"

    show lars
    Lars "Thanks for the offer, Sir—"

    show claude serious at center
    Claude "Ahem!"

    show claude serious at center
    show sylvian at left
    Lars "—Claude, but what use would I have for them? They’ll only get lost during dragon riding."

    hide lars
    show claude shocked at center
    Lars narration "Ever the showman, he raises his eyebrows in mock shock, pausing with a light gasp."

    show sylvian mad at left
    Claude "So, you’re open to accepting an accessory that’s on you without you needing to pocket it, right?"

    show lars
    show sylvian sad at left
    Lars "I guess so, but I don’t want to force—"

    show claude smile at center
    Claude "Perfect! Now, what would be the ultimate gift to match Captain’s splendor?"

    Claude "Any thoughts, Rory dearest?"

    Lars "What do you mean—"

    show rory angry at right
    Rory "Why should I help you?"

    Claude "How about a friendly competition, then? May the best one, which couldn’t be anyone other than me, win and the prize will be—"

    Rory "I couldn't care any less about prizes. I just want to savor your defeat!"

    show rory at right
    Rory "Now! Let me think this through..."

    Rory "Earrings? Nah, not good. They’d be gone with the wind before you know it!"

    Rory "[Lars] already has that artifact on, so no need for any necklaces."

    Rory "Bracelets or anklets would be a disaster around the dragons too. They’ve got those sharp spikes and claws that could easily get tangled up. We either need to go bigger, like a full-on dragon armor or go smaller like a—"

    Claude "How about a ring then? It could be the perfect accessory to keep on without it getting in the way."

    show claude blush at center
    Claude "What about it, Captain? Are you up for it?"

    show lars blush
    Lars "What are you talking about? That’s basically a proposal, isn’t it?"

    Claude "Not so much a proposal, but more of a heartfelt promise that you’ll keep me in mind whenever you look at it. After all, you always accept Boss’s bouquets and poems. Don’t they count as gifts too?"

    Lars "Well, sure, they do... but I can't picture him having flirtatious intentions like yours, right Master? And weren't you the one cracking confession jokes all the time anyway, Sir Claude? I’m sure it's no different this time."

    hide lars
    Lars narration "As seconds stretched into an uncomfortable silence, I scanned the room, eyes darting between faces, hoping for any sign of acknowledgment. Yet, the absence of a single uttered word left me with an awkward feeling."

    Lars narration "Sir Claude seemed to be already lost in a daydream as he closed his eyes, whispering softly to himself, like he was planning something important and couldn't care less about the current situation."

    Lars narration "Meanwhile, Master Sylvian, who had initially lingered inconspicuously in the background to the point of escaping my notice, now stands quietly. His eyes fixed upon me, silently pleading for acknowledgment."

    Lars narration "Who should I question about the intentions behind their gifts?"

    menu:
        " " " "
        "Ask Master Sylvian about his poems and flowers":
            $ options["CS3"]=1
            jump ask_Master_Sylvian_about

        "Ask Sir Claude about his keepsake ring":
            $ options["CS3"]=2
            jump ask_Sir_Claude_about

label ask_Master_Sylvian_about:

    play music "track_6_romance_scene.ogg"
    hide rory
    hide claude
    show sylvian at center
    Lars narration "It’s best to approach Master Sylvian first, as he tends to take my words more seriously than Sir Claude does."

    show lars
    Lars "Master, why didn’t you answer my question earlier?"

    Lars "Did you…have a different intention behind all the gifts you’ve given me so far?"

    show sylvian blush
    show lars
    Sylvian "Uhm…how do I put it…it’s j-just that—"

    show lars
    Sylvian "W-well, I…I don’t think this is the best time to, you know...uhm...explain my reasoning, but—"

    Lars "So, you do have a reason beyond just our friendship, right? Or is it a secret that you can’t tell me?"

    hide lars
    Lars narration "As if drawn in by the gravity of my serious question, he takes a deep breath and looks me directly in the eyes."

    show lars
    Sylvian "I…I don’t want to lie to you, [Lars]. Concealing my true feelings would only bring harm upon myself, akin to breaking my own neck under the weight of deception. However, this isn’t the right time for me."

    show lars
    Sylvian "You hold a unique place in my heart, [Lars], and I truly admire you. Yet, confessing my secrets now fills me with apprehension, I fear that it might jeopardize the bond we share."

    show lars
    Sylvian "Moreover, the delicate balance of our guild relationship as Boss and member makes my feelings for you... well, somewhat unethical. I'd feel like I'm abusing my power as the leader."

    Lars blush "…"

    Lars blush "Understood, Master. I’m not sure I get it entirely, but I won’t press you further, especially since I’m in doubt if you’re referring to a personal secret or something more."

    Lars blush "But no more gifts for now, I don’t want there to be another misunderstanding between us."

    show lars
    show sylvian
    Sylvian "I’ll hold back on the bouquets as you requested, but I confess that abstaining from the poems might prove to be a more difficult task, haha."

    show lars
    Sylvian "“If metal can be polished to a mirror-like finish, what polishing might the mirror of the heart require?”"

    show lars
    Sylvian "“Between the mirror and the heart is this single difference: The heart conceals secrets, while the mirror does not.”"

    show lars
    Sylvian "Moving forward, I promise to be transparent with you, to let my honesty shine through, if you allow me to."

    Lars "Let’s save that talk for later, per your wish then. Whenever you feel ready to share, I’ll be here to listen."

    show lars
    Sylvian "You have my thanks, [Lars]."
    
    jump CS_3_End

label ask_Sir_Claude_about:

    play music "track_6_romance_scene.ogg"
    hide rory
    hide sylvian
    show claude at center
    Lars narration "It’s best to approach Sir Claude first, since he tends to be more straightforward with his answers."

    show lars
    Lars "Why did you mention a ring, Sir Claude? I feel like you might be taking the teasing a bit too far today."

    show claude shocked
    show lars
    Claude "Captain, why would you ever think that? Especially after promising that you’d wear my gift…so you were toying with my feelings all this time—"

    Lars "I didn’t promise anything in the first place Sir—"

    show lars
    Claude "Cough, Hack, Wheeze, Gasp, and Splutter."

    Lars "—Claude. You’re not even trying to pretend to cough!"

    show lars
    Claude "Obviously, since the previous strategy didn’t work with you so I have to take it up a notch."

    show lars
    Claude "Anyways, I have no qualms about covering the cost for the ring either."

    Lars "But I said—"

    show claude blush
    show lars
    Claude "You could ask for all the gold in this realm, and it would be yours to possess. I’d love to spoil you senseless, you know?"

    show lars
    Claude "Or could it be that you want more? Something that can’t be bought with gold and jewels?"

    Lars "I’m not exactly talking about that, because there’s honestly no need—"

    show lars
    Claude "Need I remind you about Boss Sylvian’s so-called gifts?"

    show lars blush
    Lars blush "His presents are purely gestures of appreciation, but rings usually mean a lot more."

    Lars blush "Proposals, offerings, significant others…what would my passengers think—"

    show claude serious at center
    show lars blush
    Claude "Forget about him for now, this is a matter between you and I."

    show lars
    Lars "Although…some of my human passengers mentioned gifting rings as accessories, is that what you meant?"

    show lars
    Claude "Maybe it’s too soon for you to understand what I mean, Captain."

    show lars
    Claude "But you could say the reason I’m suddenly giving you these rings is because of Boss Sylvian over there. I’ve noticed that he’s been getting too close to you recently, and it’s making me—"

    hide lars
    Lars narration "He runs his fingers through his hair, disturbing its meticulously arranged strands. The subtle scent of his cologne wafts through the air as his intense gaze, like a magnetic force, fixates on me. A crooked smile slowly adorns his face."

    show claude smile at center
    show lars
    Claude "I'm not keen on the idea of losing what I've set my sights on to someone else, especially after being so straightforward about my intentions toward you all this time."

    show lars serious
    Lars serious "So, it’s just a competition to you? A rivalry to see who can get closest to me and then revel in the feeling of winning?"

    show claude sad at center
    show lars serious
    Claude "That’s not what I meant…"

    Lars narration "He takes a deep breath, preparing himself as if he’s about to reveal a significant secret."

    show lars serious
    Claude "I do have special feelings for you, Captain, and I admit they’re not ones as simple as friendship. But you know how I’ve always been hesitant about settling down. It’s a personal struggle that I’m trying to come to terms with, but I can’t openly share all of it here right now."

    show claude blush
    show lars happy
    Lars "Special feelings?"

    show lars happy
    Claude "Why don’t we continue this conversation somewhere private, just the two of us? I’ll truly open up and explain my intentions. Please believe me when I say I have no plans to play with your feelings. I promise you."

    show lars happy
    Claude "My interest in you is genuine, but it’s difficult for me to keep my emotions anchored when my heart always yearns for new adventures and distant horizons. Not to mention, Boss Sylvian…"

    Lars narration "Hearing Claude’s earnest plea, I realize that this situation is more complex than I initially thought. His vulnerability and honesty tug at my heart. I nod, silently agreeing to have this crucial conversation in a more intimate setting."

    show lars blush
    Lars "…"

    Lars "Understood. While I can’t say I’m entirely satisfied, I won’t press you further."

    Lars "Let’s save that talk for later, per your wish then. Whenever you feel ready to share, I’ll be here to listen."

    show claude smile at center
    show lars blush
    Claude "Thank you, Captain. You can count on me to keep that promise. I might even add it to the keepsake I’ll give you later on."

    show lars serious
    Lars serious "No rings! I don’t want to be burdened with uncertain feelings."

    Lars serious "I won’t let myself be strung along especially since I need to keep my mind sharp for the passengers. What would happen if I were to be distracted and something happened to them? What if—"

    show claude blush at center
    show lars serious
    Claude "What about your necklace? Why don’t I promise on that instead?"

    Lars "Uhm…I guess that’s okay."

    Lars narration "Suddenly, he closes in, giving me a quick but strong hug. I catch a glimpse of what can only be a light blush on his cheeks as he holds me closer."

    show lars
    Claude "You mean a lot to me, Captain, and I don’t want to rush my secret. When the time is right, I’ll share everything with you."

label CS_3_End:

    play music "track_3_the_town.ogg"
    show rory at right
    show claude at center
    show sylvian at left
    hide lars
    Rory "Let’s keep on moving, shall we?"

    play sound sfx_grassy_walk
    Lars narration "We effortlessly blended into the diverse crowd of people, a mix of descendants with their distinct tails, wings, and horns representing various species."

    Lars narration "Navigating a bustling town square like this would indeed be a challenge for regular descendants, particularly the scarce humans. Yet, after riding countless dragons and becoming accustomed to their scales, a few feathers or fur become manageable obstacles."

    Lars narration "Now that I’m thinking about it…"

    show lars
    Lars "Hey Rory, since I promised I'd help you out, what's our plan for today going to look like?"

    hide lars
    Lars narration "It was no secret that Rory’s performances provided the main source of funding for our expeditions and negotiations, making it a collective mission for all of us to occasionally advertise her shows."

    Lars narration "The well-being of our guild's dragons heavily relied on those funds, and I cannot bear the thought of them going hungry or enduring any discomfort. I would willingly starve myself before allowing such a situation to come up."

    Rory "I was thinking that we could focus on a children's show for today [Lars], you guys can start gathering the kids up a little further ahead."

    Lars narration "Before long, the collective footsteps of our group come to a halt, a unanimous signal that we had arrived at our destination."

    stop sound fadeout 1.0
    #adding this in, let’s make sure to have the sfx fade out instead of suddenly stopping it
    Rory "Here we go! A one-of-a-kind stall for one-of-a-kind puppets who actually have a purpose in life, unlike a certain someone."

    #Word wave effect for ‘Claudyyyy ‘ - sample in drive
    Rory "Not to mention, Brittina and Alex were very excited to enhance their looks with the help of {bt}Claudyyyy{/bt} over here."

    show claude shocked at center
    Rory "I did want to pluck out the lizard’s eyes for Agatha, but it’s very hard to do that in his sleep especially since he’s such a light sleeper."

    Lars "He’s the heaviest sleeper I know, what’re you talking about?"

    Rory "I wouldn’t put it past him to fake it or something. He’s got some screws missing—"

    Claude "Ehhh, you’ve been watching over me in my sleep, little Rory?"

    show claude smile at center
    Claude "I could excuse the scale stealing incident and the hair cutting fiasco because I’m so benevolent."

    Claude "However, night peeking is a no-no."

    show sylvian mad at left
    Claude "Unless…it’s my lovely Captain who does it."

    Sylvian "That’s enough Claude, you’re making [Lars] uncomfortable."

    hide lars
    Lars narration "Sir Claude’s comment certainly came out of the blue, now they’re both looking at me. What should I do now?"

    menu:
        " " " "
        "Look back at Master Sylvian":
            $ options["CS4"]=1
            jump look_back_at_Master_Sylvian

        "Look back at Sir Claude":
            $ options["CS4"]=2
            jump look_back_at_Sir_Claude

label look_back_at_Master_Sylvian:

    Lars narration "I glance at Master Sylvian, silently seeking his assistance."

    show claude shocked at center
    show lars
    Sylvian "Let’s give [Lars] some space and respect his feelings, Claude."

    hide lars
    Lars narration "I can see him making quite a stupefied face due to the sudden interference. He probably didn’t expect to be scolded like that."

    #maybe we could zoom in a little on sylvian for the next sentence like he’s  leaning for lars from his position on the right
    show sylvian:
        zoom 1.05
    show claude:
        zoom 0.95
    show rory:
        zoom 0.95
    Lars narration "Meanwhile, Master Sylvian regards me with a kind look as  he reaches out and gently rubs my ears, soothing my embarrassment as my ears perk up."

    #zooming out if we do the previous camera trick
    show claude serious:
        zoom 1.0
    show sylvian blush:
        zoom 1.0
    show rory:
        zoom 1.0
    Lars "That’s right, listen to Master Sylvian. He's practically a mind reader when it comes to picking up on my cues and emotions—way ahead of you!"

    show claude sad at center
    Lars narration "He lets out a light sigh, seemingly contemplating his actions."

    Claude "…I suppose. Can’t go against our esteemed Captain’s wishes."

    Claude "But you can’t be serious about Master Sylvian reading you better than I do."

    show lars blush
    show claude shocked at center
    Lars "I am, Master Sylvian has shown genuine care and consideration for my feelings. However, with you, it feels like everything is either taken as a joke or a competition!"

    show sylvian mad at left
    Sylvian "Claude, it’s time to stop with the teasing. As the leader of ‘Custodes Sylvae’, I don’t want you to do anything that jeopardizes our bond as fellow guild members."

    show claude serious at center
    Claude "Hmph, suit yourself Boss. I’ll back off for now."

    Claude "But I’ll have you know that I’m not giving up anytime soon."

    Sylvian "Never use someone’s weaknesses as a weapon against them, for it reflects your own character more than theirs, Claude."

    Claude "As much as I adore your poetry and philosophical quotes, I’ll stand my ground when it comes to teasing Captain over here."

    show claude smile at center
    Claude "You see, it’s fun for me to see which of his buttons I can push."

    Claude "Anyone attempting to be a goody two shoes all the time, like you, is destined for downfall unless they find a way to unleash their deepest desires, Boss. Maybe even share a secret or two!"

    hide lars
    Lars narration "A shadow crosses Master Sylvian's face at Sir Claude's comment, as if a nerve was struck deep within him. The situation seems to be on the verge of getting out of hand, but my curiosity urges me to see how things will unfold."

    show lars
    Claude "I would even dare say that you’re the one who is harboring the most dangerous inner feelings among all of us. At least, I can release my emotions by having fun with my Captain over here."

    hide lars
    Lars narration "…my Captain?"

    show lars
    show sylvian mad at left
    Claude "Yet, it seems like flowers are the only companions you can trust your secrets with."

    Claude "Not to mention, isn’t it time for you to admit to [Lars] that you’ve loved—"

    Sylvian "THAT’S ENOUGH CLAUDE!"

    Sylvian "I treasure you as a guild member of ‘Custodes Sylvae,’ but your snapdragon of a mouth is intolerable."

    Sylvian "Gracefully deceptive petals that press together to bloom in deceit. You certainly have a lot to say, but when it comes to revealing things about yourself, you remain as enigmatic as ever."

    show claude serious at center
    Sylvian "How about revealing the reason behind why you adopted that ‘ambitious’ persona of yours? You certainly try to show it off at every occasion, now don’t you?"

    Claude "Tsk tsk, outing me like this just because you couldn't handle what I said?"

    Rory "Uhm, Mentor, I don’t understand what’s going on here. But can we stop bickering for a second?"

    Lars "Rory’s right, it’s not like you two to argue like this…"

    Claude "It seems that some things—"

    Sylvian "—are overdue for the both of us."

    jump CS_4_End

label look_back_at_Sir_Claude:

    Lars narration "I glance at Sir Claude, silently seeking his assistance."

    show claude smile at center
    hide lars
    Lars narration "He playfully winks, a certain charm in his eyes that's hard to ignore. I'm pretty sure my tail is all ruffled up by the gesture, and who knows what state my cheeks are in right now—they always seem to be in a world of their own."

    #maybe we could zoom in a little on claude for the next sentence like he’s  leaning for lars from his position on the right
    show sylvian:
        zoom 0.95
    show claude:
        zoom 1.05
    show rory:
        zoom 0.95
    Lars narration "He stretches his hand in my direction, entwining our fingers and pulling me closer until we're touching shoulder to shoulder."

    show claude serious:
        zoom 1.0
    show sylvian blush:
        zoom 1.0
    show rory:
        zoom 1.0
    show lars blush
    Claude "Who knows what stage our relationship will reach in the very near future? Am I right, Captain?"

    #zooming out if we do the previous camera trick

    show sylvian mad at left
    Lars narration "As Sir Claude pulls away, releasing my hand, my attention shifts to the impending storm gathering above Master Sylvian’s silhouette. His furrowed brows and crossed arms betray a sense of bitterness."

    Lars narration "To emphasize the point further, delicate hyacinth blossoms, donned in their regal purple hues, frame the brim of his hat. Each subtle shake of his head becomes a silent decree, causing the once-graceful petals to wilt and wither, perfectly reflecting the disappointment etched on his face."

    Lars  "But why is he looking at me like that?"

    Lars narration "I’m not always on board with Sir Claude’s shenanigans, yet, it’s often easier to go along with his wishes. He enjoys the challenge, and the excitement of competition makes resisting him seem pointless."

    Lars narration "Master Sylvian knows that as well, so why would he show such an expression?"

    show claude blush at center
    show lars blush
    Claude "Whether it’s the way your cute tail wags around when you start rambling or how your ears perk up while listening to human’s tales, I can tell each and every one of them apart."

    hide lars
    Lars narration "His scaly hand traces the contours of my ears. I could feel myself slowly heating up even more; my ears and tail are too sensitive for this."

    show lars happy
    Claude "I don’t need magical gimmicks to understand you, Captain. Though, I still enjoy teasing and playfully tugging on the line between us."

    Claude "But rest assured, I’ll turn this line into a strong thread of destiny that will bind us in ways you can never imagine. Nothing is impossible if I put my mind to it, exclusively for you."

label CS_4_End:

    show rory at right
    Rory "Sorry to break up your moment guys, but we have more important things to do right now."

    Rory "Try to gather the kids while I set everything up at the stall."

    #rory exits from the right and claude moves to the right, sylvian still stays on the left
    hide rory
    hide claude
    hide sylvian
    Lars narration "I make my way through the bustling groups of children, intent on grabbing their attention. The excitement in the air is palpable as their laughter and chatter fills the space."

    Lars narration "It’s best that I tuck the artifact beneath my equipment for now. Children are easily captivated by shiny objects, and I wouldn't want them accidentally pulling and damaging the necklace."

    Lars narration "I take a deep breath and shout an announcement that echoes through the crowd."


    #textbox does an up and down shake for the next 2 lines
    Lars "HEY EVERYONE, I’M BACK!"

    Lars "THE PUPPET SHOW IS GOING TO START SOON! GATHER UP YOUR FRIENDS TOO!"

    hide lars
    play sound sfx_children_playing
    Lars narration "The moment I finish my announcement, I am bombarded by a swarm of children running towards me, their voices rising in a crescendo of excitement. Little hands tug at my sleeves, pulling me in different directions, each child eager to share their thoughts or be part of the upcoming event."

    Lars narration "Amidst the joyful chaos, I can see Sir Claude and Master Sylvian observing from afar, their watchful eyes filled with amusement and a glint of…something else that I can’t quite put my finger on."


    "Random Kid 1" "Yay! [Lars] is back from his trip."


    "Random Kid 2" "I missed you, [Lars]; my dragon has been messing with my toys recently. You definitely have to help!"


    "Random Kid 3" "[Lars]! Don’t forget we still have our race for the afternoon. You have to help me win, please!"

    Lars "Heh. This takes me back to when I was a kid."

    stop sound fadeout 1.0
    #adding this in, let’s make sure to have the sfx fade out instead of suddenly stopping it
    show sylvian at center
    Sylvian "I hope I’m not bothering you in the middle of your task, [Lars]."

    Lars "Of course not Master, this would be the perfect time to show off my skills to you in person. I’m the fastest amongst everyone here after all."

    #move sylvian to the right and have claude come to the left
    show claude at left
    Claude "Hmm, how typical of our dear Captain to compare himself with mere children."

    Lars "Just a friendly reminder – I can outrun you anytime. It might be a tad embarrassing for someone who sees themselves as the pioneer of all the competitions and challenges in Divonia, wouldn't you say?"

    show claude smile
    Claude "You think you’re soooo fast, huh? I could leave you speechless If I wanted."

    Lars "Well, Sir–"

    Claude "And so he coughs again until his lungs give out, wheeze and gag."

    Lars "–Claude, with all that coughing, who's to say if you'll have enough time to catch your breath or not? It's not a race if you're just jogging to the finish line."

    Claude "Haha, my dear Captain [Lars], it's more of a dramatic pause for suspense. You know, giving others a chance to catch up and revel in the anticipation of my victory. It's a race with flair!"

    hide lars
    Sylvian "Let’s continue on with our work, shall we?"

    Lars narration "Both guild members stand by my side. Sir Claude, with his innate charisma, effortlessly charms the children surrounding us. Meanwhile, Master Sylvian, mesmerizes them with his expertly performed flower magic."

    show claude at left
    Claude "Awe, I’ll pretend to be hurt, but while we’re on the topic, I believe that you have to challenge yourself more."

    Claude "You won’t be able to show off your talents to anyone when you spend your time with these childish competitions. How will you be able to prove yourself to the elite if you only ever rival with kids?"

    show lars
    Lars "Not everything is a contest to prove oneself, Sir Claude."

    Lars "Sometimes, I can be content with just playing around and enjoying the moment as is. Isn’t that right, Master?"

    Sylvian "Success without heart can be empty and hollow, Claude. While I understand you want to distinguish yourself from your family legacy for the sake of your ambitions, I can't help but worry about the path you're choosing."

    hide lars
    Lars narration "Family legacy…"

    Lars narration "It was certainly true that Sir Claude had the tendency to act out against his family’s wishes from time to time but according to the rumor mills, he didn’t have a reason to."

    Lars narration "The Dupont family, a lovely couple of lizard descendants, never strived Claude of love and affection. Yet, from time to time, he seemed to entertain the notion of separating himself from them, as if he were born from a nameless hermaphrodite, and all he ever was is 'Claude,' not a 'Dupont.'"

    show lars
    Sylvian "Pursuing rivalry solely to prove your self-worth to unfamiliar faces is a fleeting pursuit. In time, the present will slip away from your grasp."

    show claude serious at left
    show sylvian mad at right with move
    Claude "With all due respect Boss, but, isn’t that lack of ambition precisely why you’re here with us today instead of boasting around the academia halls?"

    Claude "While I appreciate your presence in our guild and your support for my endeavors, it seems you've relinquished all your desires, merely allowing yourself to be carried along by the whims of your flowery path."

    show claude smile
    Claude "But, you see, if you’re not determined about your dreams, someone else could come and snatch it right out of your hands."

    hide lars
    Lars narration "I catch Sir Claude throwing a peek at me but he quickly switches his focus back to Master Sylvian."

    Lars narration "When it came to dreams, Master Sylvian had garnered quite the reputation as the ‘Genius of the Century’ during his tenure at the Tower of Magicians in Divonia."

    Lars narration "Although he rarely spoke about his past experiences, a glimpse into his emotions could be seen in the way his feathers drooped and his shoulders slumped with a sense of dejection whenever the topic came up."

    Lars narration "Even his perpetual hunched posture served as a constant reminder of his time as a prestigious state magician. A time where he would work himself to the bone day and night with no rest in between."

    Lars narration "Despite his current focus on flower magic, it was evident that Master Sylvian had a different area of expertise in the past. The secrets and stories behind his prior magic remained locked away, untold."

    Lars narration "Not to mention, the formation of our guild seemed to be a deliberate decision he made in response to his experiences as an academician, though he seldom delves into the specifics."

    show lars
    Claude "It’s in the very motto of ‘Custodes Sylvae’ after all."

    Claude "‘Discere, cogitare, agere— the triad of wisdom. Learning enriches the mind, and thinking sharpens it, but it is through action that we truly manifest our knowledge and shape our reality’."

    Claude "Looks like you're stumbling on that third step."

    Claude "Isn’t that right, Captain?"

    show lars serious
    Lars "…"

    Sylvian "Your statements hold grains of truth, Claude."

    show sylvian sad at right
    Sylvian "Without love or ambition, our lives languish in the shadows of mediocrity."

    Sylvian "They ignite the fire within, propelling us to venture beyond our limits, to dream and to create, shaping a life of purpose and fulfillment."

    Claude "So, you do agree—"

    Sylvian "However…"

    show sylvian mad at right
    show claude shocked
    Sylvian "Amidst our pursuit of them, let us not overlook the tranquility of mediocrity."

    Sylvian "For not every path must lead to grand creations or extraordinary feats."

    Sylvian "In embracing simplicity, we find contentment, and in cherishing the ordinary, we discover the beauty of a life unburdened by the pressures of relentless ambition."

    show claude serious at left
    Claude "Aren’t you only saying that because you were burnt out and having nothing else to pursue?"

    Claude "If you always treasured this so-called ‘contentment’ why did you decide to spread your name onto society as the top academic of Divonia?"

    Claude "You could have simply stuck to the bottom ranks and let your life aimlessly pass by without ever achieving something or dare I say - fall in love."

    if options["CS3"]==1:

        show lars serious
        Lars "What’s he talking about, Master?"

        Lars "Is that part of the secret you wanted to tell me? That you were in love with someone else? Then, what about the mixed signals that I’ve been receiving from you thus far?"

        show sylvian blush at right
        Sylvian "N-no, you’re misunderstanding something here— I-I mean, not you. It’s probably my fault here, but—"

        Lars "I don’t want to sound conceited, but if I were the person you're in love with, I’d like to think that you would have told me about it by now."

        Lars "But then again, you're secretive about your history as well…"

        show sylvian sad at right
        Sylvian "I’m sorry but I can’t tell you any more about it with Claude here."



    if options["CS3"]==2:

        show lars
        Lars "I’ve been so busy with Sir Claude that I didn’t even notice. You’ve fallen for someone, Master?"

        Lars "That’s exciting! When are you going to introduce us?"



    show claude serious at left
    show sylvian mad at right
    Claude "Focus here Captain, we can talk about that later. Unless you’ve already taken someone’s side in this discussion?"

    show lars
    Lars "Uhm, you’re both people that I deeply admire and I don’t really want to—"

    show claude shocked at left
    Claude "Don’t want to? I expect you to at least share your personal opinion if you share the sentiment of taking no side."

    Sylvian "Pay him no mind, [Lars], he’s just upset for himself."

    hide lars
    Lars narration "What do I do now?"

    hide lars
    menu:
        " " " "
        "{size=*0.75}Agree with Master Sylvian about valuing our current contentment{/size}":
            $ options["CS5"]=1
            jump agree_with_Master_Sylvian

        "{size=*0.75}Agree with Sir Claude about the positive value of ambition{/size}":
            $ options["CS5"]=2
            jump agree_with_Sir_Claude


label agree_with_Master_Sylvian:

    show lars
    show sylvian at right
    show claude serious at left
    Lars "I agree with Master Sylvian."

    Lars "I think what he says is true about enjoying what we want instead of simply going after something for the challenge."

    Lars "I like hanging out with my dragons even if we aren't in the middle of an expedition or mission and I wouldn’t change my relationship with them for the world."

    Lars "Going after artifact hunts and transporting passengers without an ounce of love seems depressing to me."

    Sylvian "Thankfully, Claude’s influence hasn’t rubbed on you too much."

    show sylvian blush at right
    Sylvian "I’m always impressed by how well you articulate your words, my dear junior. Perhaps we can delve into these philosophies and other matters when we find some time for ourselves later."

    show sylvian sad at right
    Lars "I would love to spend time with you but Spotsy needs me more after we’re done with this, don’t you think so?"

    Lars "She’s had a long flight after all and I’m the only person who can take care of her."

    Sylvian "I can’t deny that I am a bit disappointed…"

    show sylvian at right
    Sylvian "However, it’s one of the things that I like seeing you do, [Lars]."

    Sylvian "It’s amongst my wishes to someday be a recipient of the same adoration you hold for your dragons."

    Lars "What do you—"

    jump CS_5_End

label agree_with_Sir_Claude:

    show lars
    show claude smile
    show sylvian sad at right
    Lars "I agree with what Sir Claude says."

    Lars "It’s not fair to avoid fighting for what you love and letting it slip out of your reach."

    Lars "I could admire my dragons all day and night but if I never take that leap of fate to touch them and show them my feelings directly, then I’ll only ever be walking in a circle."

    Lars "I also can’t imagine going a day without learning about the new dragon species out there."

    Claude "Glad to see that you’ve learnt a few things about my motto of life, Captain. It’s not complete, but I’ll teach more later, in private."

    Lars "I would love to spend time with you but Spotsy needs me more after we’re done with this, don’t you think so?"

    Lars "She’s had a long flight after all and I’m the only person who can take care of her."

    Claude "At this rate, I don’t think I’ll ever be able to compete with your love for dragons, Captain. But I’ll do my best to win you over, and spoil you rotten the same way you do for your dragons."

    Lars "What do you—"

label CS_5_End:

    hide lars
    #rory comes in from the right, claude stays on the left and sylvian moves to the center
    show claude at left 
    show sylvian at center with move
    show rory at enter_right
    Rory "Guys, why isn’t anyone coming? Where are the kids?"

    Lars narration "Rory suddenly approaches with a faint trace of concern etched on her face."

    show lars
    Lars "Ah, I gathered them all here!"

    #the music music fades to silence and the next track starts
    stop music fadeout 1.0
    Lars "…see?"

    play music "track_4_time_stop.ogg"
    hide lars
    Lars narration "It’s such an eerie scene…the children, once animated, have now come to an abrupt standstill, their vibrant expressions frozen in unnatural stillness."

    Lars narration "A surreal silence blankets not just them but everyone around us; it appears as though the world beyond our group has been caught in the grips of time."

    Lars narration "The once-bustling atmosphere has dissipated, replaced by an unsettling quietude."

    show lars serious
    show sylvian mad at center
    show rory angry at right
    show claude shocked at left
    Rory "Is this a joke? Was there a surprise flash mob that I wasn’t aware of?"

    Rory "{bt}Claudyyyyyy.{/bt}"

    Rory "Bribing children to pull pranks on me again, eh?"

    Claude "As much as I would love to take credit for such an event, I have no clue what’s happening either."

    Sylvian "A strange phenomenon is happening, it seems."

    Lars "What do you think is going on, Master?"

    hide lars
    Lars narration "Acting on instinct, my hand reaches out, grasping at the figures frozen in time, attempting to break the eerie stillness that envelops them. I shake them gently, yet with a growing sense of urgency, hoping to shatter the rigid spell that holds them captive."

    Lars narration "Alas, my efforts yield no response, and the unnatural stillness persists,"

    show lars
    Lars "Kids, come on. We’re getting really worried over here. Why’re you standing frozen like this?"

    show claude serious at left
    Claude "What could have suddenly happened? Everything was fine up until a few minutes ago."

    Lars narration "In the midst of my attempts to shake off the statues, a peculiar sensation courses through me."

    hide rory
    hide sylvian
    hide claude
    show shining_necklace
    Lars narration "The necklace I'm wearing grows warmer, its temperature gradually rising. Intrigued and compelled, I shift my attention towards it. It appears Rory has noticed it too."

    Rory "Hold up! What’s happening to the artifact right now? Take a look everyone."

    Lars narration "Instantly, everyone’s gaze fixates on me."

    Rory "It’s shining like crazy! Do you think it has something to do with what’s going on? Maybe a weird spell that suddenly got activated?"

    Rory "It’s as if we’re the only people moving and everyone else is frozen in time. Don’t you find it weird?"

    Rory "What’s going on, Mentor? Can’t you do something about this?"

    Claude "Calm down little Rory—"

    Rory "Claude, what the heck did you bring with yourself?! If anything goes wrong, I’m holding you responsible!"

    Claude "…"

    hide shining_necklace
    show sylvian serious funny at center
    show rory angry at right
    show claude serious at left
    show lars serious
    Sylvian "I have only ever heard of one artifact having the ability to do such a thing. Remember the one we talked about when we first opened the box?"

    Sylvian "However, the color of the gem in our necklace is different from that I remember."

    Sylvian "Even then, why would such a thing happen so suddenly?"

    Claude "I didn’t hear about an effect like this from the merchant either, there was no mention of it when they handed over the artifact to me. I couldn’t have been duped like this, that’s simply impossible—"

    show lars sad
    Lars "What do we do now? What’s going to happen to them?"

    show sylvian at center
    Sylvian "Steadfast everyone, calm yourselves down."

    show rory at right
    show claude at left
    show lars
    Sylvian "The brave person is not the one who feels no fear, but the one who conquers that fear. Let’s do our best to figure this out."

    Lars "Me too Master! I’m the strongest one among us, I’ll try to protect us in case something goes south."

    show claude shocked at left
    Claude "Wait! Can anyone else see that shadow over there?"

    show claude serious at left
    hide lars
    Lars narration "It appears Sir Claude spotted an approaching figure before any of us did, courtesy of his lizard-sharp eyesight."

    show lars serious
    show sylvian mad at center
    Claude "I think that it’s watching us. Stay on guard."

    hide all
    Lars narration "As the tension in the air grows, I sense the presence of an unknown observer. It sends a chill down my spine, and I can feel my ears perk up."

    Lars narration "A bead of sweat rolls down my forehead, and my ginger fur seems to prickle, almost as if it senses the imminent danger and excitement that lay ahead."

    show lars serious
    show claude shocked at left
    show rory angry at right
    #"Unknown" "Looks like some interesting Divs have entered my domain while I was occupied."
    Zephyr "Looks like some interesting Divs have entered my domain while I was occupied."

    #for the previous line, Zephyr doesn’t show up yet, but for the next, he comes in from the left side. 
    #All the characters turn their heads towards him and then huddle up together on the right, their sprite can be somewhat squashed. 
    #There’s supposed to be a little difference as Zephyr stays on the left, the center empty, and the three other characters squished on the right.
    $ renpy.choice_for_skipping()
    show rory:
        linear 0.5 xalign 1.1
    show claude at flip:
        linear 0.5 xalign 0.9
    show sylvian:
        linear 0.5 xalign 0.7
    
    show zephyr happy at enter_left
    #"Unknown" "I was frozen in anticipation for what would come next, but I have work to do after this. My castle isn’t going to clean up after itself!"
    Zephyr "I was frozen in anticipation for what would come next, but I have work to do after this. My castle isn’t going to clean up after itself!"

    #"Unknown" "Get it? frozen in anticipation. Hehehehehe~"
    Zephyr "Get it? frozen in anticipation. Hehehehehe~"

    show sylvian:
        linear 0.5 xalign 0.4
    show claude:
        linear 1.0 xalign 0.8
    show rory:
        linear 1.0 xalign 1.0
    show zephyr happy:
        linear 0.25 xalign -0.2
        linear 0.75 xalign 0.0
    #for the next sentence, sylvian moves towards the center (the right side becomes less cluttered) and zephyr moves to the left a little before coming back to his original position. 
    #I want to make it seem like he was startled for a sec before he goes back to normal
    Lars narration "In an instant, Master Sylvian’s incantation casts a protective shield of varying blooms and plants around us, shimmering with the combined energies of crystalline dews."

    Lars narration "Even with the shield in place, my predator instincts stay sharp. The tension in the air is palpable, and I'm acutely aware of the figure's every move. Time seems to slow down as I focus intently on its enigmatic presence, poised to react if any threat arises."

    show rory
    Lars narration "With Rory by my side, her cutting tools poised for self-defense, we form a united front against the unknown creature."

    #for the next sentence, claude moves forward on the left side of sylvian. Right now, the order from left to right should be zephyr, claude, sylvian, and rory with equal space between them.
    show sylvian:
        linear 0.75 xalign 0.6
    show claude:
        linear 0.75 xalign 0.4
    hide lars
    Lars narration "Sir Claude, ever bold and quick-witted, leaps forward to question the puzzling figure."

    show claude serious at center_left
    show sylvian mad at center_right
    show rory angry at right
    show lars serious
    Claude "Who’s there? Are you the person behind this? What’s—"

    #"Unknown" "Slow doooown there."
    Zephyr "Slow doooown there."

    #"Unknown" "Times not running away after all. You know?"
    Zephyr "Times not running away after all. You know?"

    Sylvian "…"

    Lars "…"

    Claude "…"

    Rory "Heh—"

    show zephyr sad at jp
    #zephyr sprite jumps up and down for the next sentence. Textbox could do a shake as well.
    #"Unknown" "DON’T JUDGE ME!"
    Zephyr "DON’T JUDGE ME!"

    Rory "Too late for that now."

    show zephyr happy at left
    #"Unknown" "It’s been some time since I could speak with someone without them being brainwashed or stuck in time."
    Zephyr "It’s been some time since I could speak with someone without them being brainwashed or stuck in time."

    Lars "Huh? What’re you talking about?"

    #zephyr does a small side to side shake for the next sentence
    show zephyr happy at shake
    #"Unknown" "Ah, the inquisitive one speaks. Hmm, I’ll call you Scouty from now on since you look the part as well."
    Zephyr "Ah, the inquisitive one speaks. Hmm, I’ll call you Scouty from now on since you look the part as well."

    Lars "My name is [Lars], not Scouty!"

    #"Unknown" "My brain cells will only acknowledge you as Scouty from here on out."
    Zephyr "My brain cells will only acknowledge you as Scouty from here on out."

    #"Unknown" "You're all destined to be new additions to my castle renovation army, so sparing the effort of using two names at once seems reasonable."
    Zephyr "You're all destined to be new additions to my castle renovation army, so sparing the effort of using two names at once seems reasonable."

    show lars
    Lars "But you only have to remember one, which is ‘[Lars]’—"

    #"Unknown" "Well, let's see who else we have in this riveting cohort. I'm sure your names are all yawn-inducing, but let's make this roll call fun, shall we?"
    Zephyr "Well, let's see who else we have in this riveting cohort. I'm sure your names are all yawn-inducing, but let's make this roll call fun, shall we?"

    #"Unknown" "You, the one with the flowery hat, must be the smart one in the group since you haven’t interrupted me so far. I’ll call you Smarty from now on."
    Zephyr "You, the one with the flowery hat, must be the smart one in the group since you haven’t interrupted me so far. I’ll call you Smarty from now on."

    #"Unknown" "But be careful not to interject too much like Scouty."
    Zephyr "But be careful not to interject too much like Scouty."

    Lars "But how is that even related to what I asked—"

    show claude shocked at center_left
    Claude "Hey now, when did I—"

    Rory "—ever interrupt you?"

    #"Unknown" "Scouty, and the other two, I need my main character moment over here, stop blabbering so much."
    Zephyr "Scouty, and the other two, I need my main character moment over here, stop blabbering so much."

    hide lars
    Lars narration "I take a deep breath, frustration bubbling up within me as I watch the scene unfold. The figure’s words are becoming increasingly difficult to make sense of."

    Lars narration "I glance at my companions, hoping someone will step up and challenge their nonsensical monologue. We can’t afford to let them dominate the conversation."

    Lars narration "Come on, someone has to say something."

    show lars serious
    #"Unknown" "As I was saying—"
    Zephyr "As I was saying—"

    show sylvian serious funny at center_right
    Sylvian "Enough banter, who exactly are you?"

    hide lars
    Lars narration "Relief washes over me as Master Sylvian speaks up."

    show lars
    show sylvian mad at center_right
    Sylvian "State the truth, or you'll face the consequences. I prefer not to harm others, but I'll do what needs to be done as the leader."

    play sound sfx_clap
    Lars narration "Suddenly, the sound of a single clap pierces through the stillness. It’s a sharp and commanding sound, one that demands our attention."

    #"Unknown" "Impressive words, especially considering your current disadvantage but I’ll humor you this time."
    Zephyr "Impressive words, especially considering your current disadvantage but I’ll humor you this time."

    #"Unknown" "Since Smarty asked, it’s time for the cliché introduction séance, the kind they do for video games and TV shows."
    Zephyr "Since Smarty asked, it’s time for the cliché introduction séance, the kind they do for video games and TV shows."

    #"Unknown" "Hopefully, they spared no expense in making me the fairest of them all. A little extra villainous charm never hurt anyone~"
    Zephyr "Hopefully, they spared no expense in making me the fairest of them all. A little extra villainous charm never hurt anyone~"

    #"Unknown" "But before that, you’d better cease all your magical theatrics and weapon brandishing if you don't want me to lose interest in this little charade."
    Zephyr "But before that, you’d better cease all your magical theatrics and weapon brandishing if you don't want me to lose interest in this little charade."

    hide lars
    Lars narration "Gradually, Master Sylvian begins to dismantle the defensive walls he had erected, and Rory and I, in sync, follow suit. Hopefully, that’s the right choice to make for now."

    show lars
    show rory at right
    show sylvian at center_right
    show claude at center_left
    #"Unknown" "Anyway, you can address me as the “Omniscient Lord of Bankruptcy” or if it’s easier on the tongue, the “Malevolent Architect of Debt”. Personally, I'm partial to the latter title—it aligns better with my aspirations."
    Zephyr "Anyway, you can address me as the “Omniscient Lord of Bankruptcy” or if it’s easier on the tongue, the “Malevolent Architect of Debt”. Personally, I'm partial to the latter title—it aligns better with my aspirations."


    show lars serious
    Lars "Uhm, does that mean that you cause bankruptcy or that you’re the literal embodiment of bankruptcy?"

    Rory "Do you design debt plans to bankrupt others or are you so bankrupt that you’re already knee-deep in the debt plan already?"

    Rory "But then again, I can’t see if you have knees or not. Are you a talking dog by any chance?"

    Sylvian "I don’t think that’s an issue we need to be discussing right now, my dear juniors."

    "{size=36}{color=#CD4EDD}Malevolent Architect of Debt{/size}" "Ahhh, keep quiet for a second! I’m not used to talking this much. If it weren’t for you meddling Divs, I would have gotten away with my grandiose plan already."

    Rory "Somehow, I really doubt that you’d be capable of doing something like that."

    "{size=36}{color=#CD4EDD}Malevolent Architect of Debt{/size}" "Hmph, don't underestimate me. I could wipe your minds clean right now since you’ve already heard my voice, and even learnt of my grandiose plan —though not completely— and what else…"

    "{size=36}{color=#CD4EDD}Malevolent Architect of Debt{/size}" "…You’re probably going to learn of my real name which is Zephyr but anyway—"

    Rory "Isn’t this the same case of yelling out your attack name before it’s your turn to fight?"

    hide lars
    Lars narration "We're spending too much time here; I need to take a proactive approach and ask him some questions myself before anything bad happens to everyone else who's been frozen."

    play sound track_5_zephyr_theme
    menu:
        " " " "
        "{size=*0.75}Are you the person responsible for freezing everyone?{/size}":
            $ options["G1"]=1
            jump are_you_the_person

        "{size=*0.75}How come you’re freezing everyone for a castle renovation?{/size}":
            $ options["G1"]=2
            jump how_come_you


label are_you_the_person:

    show lars serious
    Lars "I’m curious about this current phenomenon, are you the person responsible for this?"

    #rory jumps up and down a bit for the next sentence
    show rory at jp
    Rory "Come on, [Lars]! He can’t actually lack that many brain cells to spell out his plan like that—"

    Zephyr "Exactly, what do I get in exchange for all this talking and sharing my top-secret agenda? Huh?"

    show claude smile at center_left
    Claude "I’m sure we can reach a compromise if we settle this down like proper negotiators. Threatening someone won’t get you on their side, after all. It will only provoke them to attack."

    Zephyr "Hmph, you’re quite the silver-tongue, aren’t you ?"

    Zephyr "I’ll call you Slicky from now on to match those lizard descendent traits of yours since you think you’re so—"

    Claude "Shadowy figure, calls himself weird titles for attention, keeps talking about freezing time and brainwashing everyone. I think it’s fairly obvious we have a deal-breaking villain on our hands. Unless you’re not actually the person behind this."

    Zephyr "Of course, I am! I wouldn’t brandish my family name with such buffoonery if I didn’t have a grandiose endgame in mind."

    Claude "Are you sure about that? Maybe you’re just a random kid messing with some kind of weird spell?"

    show zephyr sad at left
    Zephyr "K-K-Kid?! I’m older than all of you combined! I mean, I’ve been sleeping for a few centuries but ugh that’s not the point! Let me start from the beginning since you’re so quick to make me out to be a low-class villain, Slicky."

    Claude "So you’re not a villain?"

    Zephyr "Of course, I'm not; I'm the maestro of mischief, the virtuoso of vexation, the puppeteer of pandemonium, the curator of calamity, pulling strings to unveil the grand tapestry of turmoil—"

    show claude serious at center_left
    Claude "Okay, okay, we get it! Now on to answering the question."

    show zephyr happy at left
    Zephyr "Quite the impatient one, aren’t you Slicky?"

    Zephyr "You see, my family has had this unique time freezing artifact for quite a few generations now. We’d have the responsibility of using it to maintain order and peace in the land as noble dragon descendants of the house of—well, never mind that for now."

    Zephyr "You don’t need to know the details."

    show rory at right
    Rory "Seems like we have a delusional con-artist here."

    show zephyr sad at left
    Zephyr "I’m not lying!"

    show rory angry at right
    Rory "You’re clearly not using it responsibly, now, are you?"

    show zephyr happy at left
    Zephyr "Hold on there, bull woman, unless you want to be called Speedy or—"

    show claude smile at center_left
    Claude "I insist you call her Smally, since she fits the size standard."

    Rory "Ernest Jones called from Earth and said he wants his god complex back."

    show zephyr sad at left
    Zephyr "Quit trying to shadow my lore explanation, you two."

    show rory at right
    Rory "Hehe, shadow…"

    show zephyr happy at left
    Zephyr "I’ve decided to use the artifact for my personal gain since my present situation calls for it. But it’ll all be worth it when my castle is renovated."

    show sylvian serious funny  at center_right
    Sylvian "Were there never any countermeasures set up in the case of someone misusing the artifact?"

    Lars narration "Master’s crucial interjection couldn’t have come at a better moment."

    Rory "Mentor, shouldn’t we use some discretion here? What if it decides to cross us—"

    Zephyr "Should we ever deviate from our path and misuse it, the paired artifact would counteract the spell. Anyone who touches it would be immune to the artifact's magic."

    Zephyr "Basically, the same necklace but with a different colored gemstone and the opposite ability—"

    Sylvian "…Did you say, it was a necklace with a gemstone?"

    Zephyr "Hmm, yeah, what about it?"

    Sylvian "Out of curiosity, where is that artifact now?"

    Zephyr "I'm not an all-knowing encyclopedia, now am I? I have no clue about its current whereabouts. It might have been pilfered while I was in my centuries-long slumber; it wasn't there when I woke up."

    show zephyr sad at left
    Zephyr "Hmph, it’s not like you’ll believe me anyways."

    Lars "Come on, we’re listening to your story right now, aren’t we?"

    Zephyr "I’ve tried to convince so many people till now, human and descendent alike."

    Zephyr "What makes your group so special that I shouldn’t instantly freeze right now?"

    Zephyr "You know what? Forget it."

    jump G_1_End

label how_come_you:

    show zephyr sad at left
    show lars  serious at left
    Zephyr "Well, I’ve been sleeping for a few centuries now. When I finally woke up, there was no one around, and I found myself in the form of a ghost-like creature."

    Zephyr "My castle, once grand, had turned into a complete wreck. To make matters worse, not a trace of gold was left!"

    Zephyr "Countless generations of descendants faithfully served us during my decades of wakefulness. However, upon reopening my eyes, not a single soul lingered."

    show rory at center_left
    Rory "Is that why you settled on the title of “Omniscient Lord of Bankruptcy”? Then why would you need two titles like “Malevolent Architect of Debt”?"

    show zephyr happy at left
    Zephyr "Shh, you can’t cut in while I’m laying down my sob story."

    show zephyr sad at left
    Zephyr "Like I said, I couldn’t find anyone and the castle was completely empty."

    Zephyr "I searched for so many days but to no avail, I thought that instead of searching, I should start waiting instead. But who could even recognize our family castle with its broken-down state?"

    Zephyr "Eventually, I decided to hire some descendants to work on restoring my castle to a somewhat presentable state. Yet, to my disbelief, after just a few days, they had the audacity to demand compensation."

    Zephyr "Can you fathom such impertinence?"

    show claude shocked at center_left
    Claude "But how could you? No money, no family, not even a proper place to sleep in, you’d be knee-deep in debt by this point if you decided to hire people."

    Zephyr "T-That’s ugh…totally—not what happened. Hahaha…"

    "Everyone" "So, that's what happened, isn't it?"

    Zephyr "They didn’t believe me when I said I was a noble dragon descendent so it was no use appealing to their loyalty."

    Rory "I mean, I hardly blame them at this point."

    Claude "Long story short, you just wanted free labor."

    Claude "We’re past the stage of paying others with exposure and influencer points, you know?"

    show claude smile at center_left
    Claude "Unless it’s me that does it, because they’re getting their gold’s worth and so much more."

    Zephyr "Stop cutting in, you two! Take a cue from Smarty over there and learn to be a bit more silent."

    Rory "How much longer is this going to take? Can we skip this?"

    #for the next sentence, zephyr jumps up and down and the textbox does a little shake
    show zephyr at jp
    Zephyr "{sc}DON’T! PLEASE! I’m reaching the good part of the story after all.{/sc}"

    show zephyr happy at left
    show sylvian serious funny at center_right
    show rory at center_right
    show claude shocked at center_left
    #make the sprites on screen (except lars) jump up and down in shock like they couldn’t believe what he just said
    Zephyr "Ahem! So, instead of finding descendants looking for compensation, I decided to hire newly transported humans!"

    Zephyr "Genius idea, I know. They wouldn’t have any qualms for gold either since they don’t understand the mechanics of this realm yet."

    Zephyr "Bonus points, they also easily accepted how I’m a noble and that I could give them positions in my castle as soon as it was renovated."

    Zephyr "I need a proper place to rest after all and a castle of that size needs regular maintenance."

    Sylvian "You keep mentioning your castle and innocently slaving away unknowing humans. But where is this castle of yours? None of my maps, scrolls, or academic documents have ever pointed to the existence of a secret and perished household like the one you’re describing."

    Sylvian "Not to mention, how does that even result in your usage of an artifact to freeze time?"

    show claude serious at center_right
    Claude "That’s right! We’ve been walking around this issue for some time now and we haven’t learnt one single coherent thing from you. Just bits and pieces that aren’t helping us get out of this mess. Maybe you’re just a minion for someone else’s plan—"

    show zephyr sad at left
    Zephyr "I think you’re undermining my generosity here; I gave you so much information for nothing. I could even wipe your brains clean."

    Zephyr "After all, I’m only mentioning these because I haven’t had the chance to properly speak with someone for a long time now so you mustn't think that I enjoy talking to people, okay? OKAY?"

    "Everyone" "He definitely enjoys talking with people."

    show lars serious
    Lars "So you’re a noble dragon descendent who's been sleeping for centuries."

    Lars "You woke up, broke and homeless. You decided to use free labor from the descendants to clean up the mess in your castle. However, you couldn’t pay their wages properly. You then decided to slave away unsuspecting humans since they were ignorant about the rules of the realm."

    Lars "But why did you decide to use the time freeze artifact in the first place?"

    Zephyr "How could I bring them back to my castle without explaining the situation to them? They would get suspicious and run away from now. You know how hard I’ve worked to manually capture the humans and brainwash them to fix up my home? Or do you want me to be homeless?"

    Zephyr "You heartless people, you're making me fake sob over here."

    Claude "You’re obviously lacking a certain moral regard to be paying your employees so poorly, not to mention—"

    Zephyr "I didn’t want to, okay? But what other choice did I have?"

    show rory angry at right
    Rory "Literally, anything besides making a house-renovating army of human zombie servants."

    Zephyr "I couldn’t win them over with my title and I couldn’t make them work without compensation either."

    Zephyr "The time freeze did help me in relocating them and ensuring I was the first one I spoke to, making my situation clear. It was the easiest solution for me. I'd pay them back if I got a flow of gold going on."

    Zephyr "Rumor has it that news and gossip about transported humans fetch quite the price these days, rivaling even celebrities and renowned descendants. If I could secure some scandalous scoops, I'd amass enough wealth to renovate my abode without the hassle of this extra business."

    Lars "But you’re still doing the wrong thing. Kidnapping and brainwashing people is only going to work against your gossip column influencer plan here."

    Zephyr "The mind control thingy was always a last resort for me, and even now, I'm just left with an army of zombies, eternally doomed to be bored out of my mind."

    Claude "Weren’t you the same person who tried to threaten us with brainwashing before—"

    Zephyr "It wasn’t like I was bluffing to make you spill what info you had. I’m not that forgetful, okay? OKAY?"

    "Everyone" "He’s definitely that forgetful."

label G_1_End:

    play music "track_1_intro.ogg"
    show lars
    Lars "I don’t need to ask anymore questions for now."

    show claude smile at center_left
    show sylvian at center_right
    show rory at right
    show zephyr happy at left
    Claude "You say that, Captain, but I have a question to ask our mystery person."

    show zephyr sad at left
    Zephyr "Ugh, I’m getting tired of this interview session Slicky."

    Claude "Where’s the proof that you haven’t been speaking gibberish so far?"

    Claude "Merchants always need to showcase their credibility, same goes for someone who’s exchanging our time with childish bluffs."

    Zephyr "This group is going to be the death of me, I swear."

    show sylvian serious funny
    Sylvian "This is going to take us even longer if we continue at this pace. Rory, could you come here for a second?"

    #after the previous line, rory’s sprite moves towards sylvian and they sem huddled up like they’re discussing something
    hide lars
    show rory:
        linear 0.5 xalign 0.85
    Lars narration "Master Sylvian beckons Rory over to his side and starts whispering something in her ear. I can't make out what they're saying, but it seems important enough that he even brings up his wings to cover his mouth."

    #for the next sentence, rory goes back to her position on the right
    show rory at right with move
    Lars narration "However, before I have more time to analyze what was going on, Rory chirps back to our side."

    #word wave effect for ‘Ghostyyyy’ - sample in drive
    show sylvian  at center_right
    Rory "You can't die on us yet {bt}Ghostyyyy{/bt}; I'm planning to give you a timeless puppet show after all!"

    Zephyr "What are you talking about, Speedy?"

    Rory "You mentioned that you wanted to be entertained, right? So why don't I keep you occupied— I mean, uh— keep you \"strung along\" for a private show."

    show claude smile at center_left
    Rory "I'm sure a person of your caliber is also familiar with these kinds of VIP events, aren't you? Because it would be totally embarrassing if you didn't."

    show zephyr happy at left
    Zephyr "Wha- of course I have! What kind of noble descendant would I be if I didn't? Come on, then. Entertain me if you can."

    Rory "As expected. It's a good thing I always have my handy puppets for extreme situations like this."

    Rory "Get ready to be amazed by Brittina and Alex. Unfortunately, Agatha hasn't undergone a complete makeover yet, thanks to a certain someone who keeps stalling."

    Claude "I wonder who that could be…"

    Rory "So, why don't we go around the corner where I have my stall set up?"

    show zephyr sad at left
    Zephyr "Huh, what about my new army additions here?"

    hide lars
    Lars narration "Good to know that we’re demoted past the nicknames as well."

    show lars
    Rory "They can't do anything when the time is frozen like this, so why don't we have some fun without any worries?"

    Zephyr "…"

    hide lars
    Lars narration "Is he going to accept?"

    show lars
    "Everyone" "..."

    Zephyr "Ugh, fine. Might as well enjoy my time with someone who is also interested in the art of puppets."

    Rory "Exactly—"

    Lars narration "However, before Rory has the time to finish her sentence, Zephyr's shadow encloses around her, and they both disperse without a trace, leaving a momentary respite from his presence."

    #during the last sentence, rory and zephyr fade out from the scene and claude and sylvian’s positions change. 
    #Claude moves from center left to left and sylvian moves from center right to right
    hide zephyr with dissolve
    hide rory with dissolve
    show lars
    show claude at left with move
    show sylvian at right with move
    Sylvian "It's good to see my junior using her wit to buy us some extra time for discussing certain matters."

    Lars "That was part of your plan all along?"

    show claude serious
    Claude "Look, Captain, we don't have much time to lavish praise on our precious Boss and little Rory right now."

    show lars sad
    Lars "I'm a bit worried about Rory, though. Maybe I should have convinced Zephyr to let me go with her—"

    show claude smile 
    Claude "Pfft, she's perfectly fine taking care of her own, and that's coming from me."

    show sylvian serious funny 
    Claude "Let's move on, though. The only sensible option here is to graciously accept everything our so-called \"villain\" is saying."

    Lars "How so? Isn’t there even a tiny bit of doubt in your mind?"

    show claude shocked
    Claude "I do believe what he's saying, or more so, I want his story to be true. I've been waiting for a thrilling adventure like this for quite a long time now, and the opportunity is now within my grasp."

    Sylvian "I also think we have to believe what he says. Most notably what he mentioned about the necklace."

    Claude "But he didn't even know that we have his so-called counter-artifact with us. Especially with how [Lars] has been hiding the necklace under his clothing all this time."

    show claude smile 
    Claude "I'd probably miss it too without these handy lizard eyes."

    show sylvian mad 
    Claude "Speaking of eyes, if I happen to overlook something crucial, I might just have to attribute it to being too captivated by your presence, Captain. Gotta take responsibility, you know?"

    Lars narration "A low murmur reaches me and I turn my gaze towards Master Sylvian. His expression has shifted into a stern, disapproving look. It's evident that Sir Claude's nonchalant attitude is grating on his nerves."

    Lars narration "But then again, this has been Sir Claude’s personality for a long time; there’s no helping it."

    show claude shocked 
    show sylvian 
    Lars "For now, why don’t we listen to what Master Sylvian has to say? He's certainly smarter than the both of us."

    show claude serious 
    Claude "I’m sure he can speak for himself—"

    Sylvian "Exactly, and I’d like to take a moment to discuss what's really important here if you could set aside your flirtatious act for a second."

    hide lars
    Lars narration "His eyes lock onto mine, and a serene smile graces his lips."

    show lars
    show sylvian blush 
    Sylvian "Thank you for what you just did, [Lars]."

    Lars "It’s no problem, Master. Now, let’s get back to what you were saying."

    show sylvian 
    Sylvian "From what I understood, that shadowy figure is a noble dragon descendent from the previous dynasty of Divonia."

    Sylvian "Supposedly, he's been sleeping for centuries, using his family's time freeze artifact on himself for some unbeknownst reason."

    Sylvian "After all, a man is not what he thinks he is, he is what he hides."

    Sylvian "This mysterious person can easily be related to us as well when you consider how the artifact fell into our hands in the first place."

    show claude shocked
    Claude "I did think it was suspicious how the merchant was trying to get rid of the box so quickly. No one would try to sell something to the Dupont family at a loss in profits."

    show lars sad
    show sylvian sad 
    Lars "I’m sorry too. I messed up big time. I shouldn’t have put any of you in this situation. What kind of dragon pilot am I if I can't ensure the safety of those around me?"

    Sylvian "Don’t be too hard on yourself, [Lars]. We were all caught up in the excitement of a mysterious artifact. It’s easy to overlook the finer details in such situations."

    show sylvian 
    show claude 
    show lars
    Sylvian "Now that we're aware, let's approach this with caution to avoid falling for any more tricks. Before our young Lord arrives, we should gather all the information we can for now."

    Lars "To summarize, he’s using the legacy necklace to suspend time for everyone, and it’s supposedly structurally identical to the artifact we have albeit with a different gemstone and contrasting ability."

    Lars "I also believe that the reason we escaped from his spells’ effects was because of this necklace right here."

    Lars narration "I glance down at the accessory that I’ve carefully concealed beneath my dragon pilot equipment, and my heart skips a beat when I see that it’s still shining brightly with a vivid red glow."

    hide sylvian
    hide claude
    show shining_necklace
    Lars narration "The heat it emitted during our earlier encounter with Zephyr may have subsided, but its enchanting radiance remains."

    Lars "Now that I think about it, he mentioned not knowing the whereabouts of the artifact, despite being in charge of the two couple necklaces all this time. My question is, why did this variable suddenly exempt us from the time freeze effect? Could it be related to the artifact?"

    Sylvian "If it was related to the presence of the artifact in a known area, then why wasn’t anyone else near the seashore also affected by its counteracting abilities? The weird shadow also said something similar."

    Claude "Perhaps…it’s related to touching the artifact."

    Claude "Think about it, we all experienced this phenomenon after holding the necklace."

    Claude "Not to mention, we were the only people who touched the artifact after opening the box."

    hide shining_necklace
    show claude smile at left
    show sylvian serious funny at right
    show lars
    Lars "Quite the detective, aren't you? I didn't realize I had a master of deduction by my side."

    show lars
    Claude "Oh, Captain, you'll uncover even more intriguing talents if you choose to stick around with me."

    show sylvian mad 
    Sylvian "Enough flirting, Claude."

    show lars
    Claude "Yeah yeah, whatever you say, big Boss."

    show lars serious
    Lars serious "His plan to renovate his castle seems utterly absurd to me, though."

    show sylvian serious funny 
    Claude "Mhm, hiring descendants only to realize he can’t pay his way through. Going for humans and not even offering to inform them of the rules around here. It’s both malicious and strangely naive at the same time."

    Lars "What about the people who are currently captured by him? How do we convince him to let them go?"

    show sylvian 
    Sylvian "“To lose patience is to lose the battle.”"

    Sylvian "Let’s take this one step at a time."

    Sylvian "After our deck is complete, we can use our hidden ace and free the people under his spell. It may be late for those who fell victim to his scheme, but we need to put a stop to this time suspension phenomenon."

    Lars "But how are we supposed to do that? He already wants to stop us by adding us to his zombie human army since he believes we’ll spoil his plans."

    Lars "Also, I can’t figure out why he’s giving all this info to us, knowing it’s going to work against him. Does he have another plan in mind?"

    Claude "Like I said, he’s probably just a naive kid. But we can use that to our advantage."

    Sylvian "Fortunately for us, a threatening tongue reveals a wayward start."

    Sylvian "For in loose words, a tale unfolds, of inner battles and stories untold."

    Claude "I’d like to think that one of his screws is missing."

    Lars "So I'm assuming we're going to act unaware of why we're not affected by the time suspension?"

    Sylvian "I think it's best that we do. Otherwise, we'll be divulging the reason why we're not influenced by his artifact and how the countermeasure necklace has fallen into the palm of our hands."

    Lars "What if he notices though?"

    Claude "He's more preoccupied with being entertained than trying to figure out why we're moving around freely. Do you recall him even questioning us about it?"

    Lars "Now that you mention it…"

    hide lars
    Lars narration "Speaking of the devil, Zephyr’s black particles coalesce once more and he and Rory appear side-by-side. My initial worry dissipates as they emerge with grins plastered across their faces."

    #during the last sentence, zephyr and rory fade in and they take on their previous position. From left to right, zephyr, claude, sylvian, and rory
    $ renpy.choice_for_skipping()
    show sylvian zorder 1:
        linear 0.5 xalign 0.6
    show claude zorder 2:
        linear 0.5 xalign 0.4
    show zephyr happy at left with dissolve
    show rory at right with dissolve
    Zephyr "Finished with the banter and jokes? Speedy here kept me quite occupied, I must say."

    Rory "Petition to designate this guy as our story antagonist. We'll have a 99.9\% chance of success in distracting him, and he won't even make a fuss about it."

    #zephyr does a side to side shake for the next sentence
    show zephyr at shake
    Zephyr "I’d say it’s worth it because of that fabulous puppet show earlier."

    Zephyr "I look forward to seeing you bring in new dolls to the scene as well. This could be my new hobby after reading my daily gossip columns."

    #rory jumps up and down for the next sentence
    show rory at jp
    Rory "Yay, another fan acquired!~"

    Sylvian "I'm glad to see you back safely, my dear junior."

    show claude
    Claude "Can't say I share the sentiment."

    show rory angry 
    Rory "Well, you're a few degrees short of cold-blooded, so I don't blame you."

    Sylvian "That’s enough for now, there's something more important we need to address."

    #for the next sentence, sylvian moves past claude to face zephyr. So from left to rights, it’s going to be zephyr, sylvian, claude, and rory
    show sylvian at center_left with move
    show claude at center_right with move
    Lars narration "Master Sylvian’s steady voice resonates with unwavering conviction as he faces Zephyr."

    show lars serious
    show sylvian serious funny at center_left
    Sylvian "Noble descendent, it’s clear that you’re manipulating a fundamental fabric of time for your personal gain. However, we cannot remain in this state too long."

    hide lars
    Lars narration "It seems like Master Sylvian will not be mentioning our displeasure about the brainwashed army at his castle. It’s probably best to keep a secret for now."

    show lars serious
    Zephyr "Here’s the fact, Smarty. I don’t understand the mechanics of it either and I don’t really have to."

    Zephyr "What I do know is that you guys can escape the effects of my family heirloom either because you’re special in some way or there’s a variable that I’m not aware of, like the counter artifact."

    hide lars
    Lars narration "Oh no, is he catching on to us?"

    Lars narration "I grasp the gemstone beneath my piloting gear, my fingers wrapping around it tightly. It’s as if I’m seeking reassurance that our hidden card remains securely in our possession"

    Lars narration "Looking over my shoulder, I notice my tail wagging at full speed. The rhythmic swaying is almost involuntary, a physical manifestation of the heightened anxiety stirred by Zephyr's comments."

    show lars serious
    show sylvian at center_left
    Zephyr "But…enough of that imaginary scenario because I don’t really care why you’re not affected."

    show claude smile at center_right
    Claude "Told you so, Captain."

    Zephyr "When I take you back to my castle. You’ll join my army and I’ll be able to continue my renovation plans without any worries of someone trying to ruin it."

    Zephyr "Keyword being “try”."

    Zephyr "After all, you guys cannot escape from me while my artifact is still working."

    hide lars
    Lars narration "That’s literally what we’re trying to do here though!"

    show lars serious
    show zephyr sad at left
    Zephyr "However, I can't keep time frozen forever. I need to teach my new minions what they need to do."

    Claude "Before that, I possess a proposition that might pique your interest."

    show zephyr happy at left
    Zephyr "Hmm? What is it Slicky?"

    Claude "It appears you’re seeking some amusement, considering your remarks about the lackluster nature of your current companions. We could be the very diversion you yearn for."

    Zephyr "That won't do. I can't leave you guys alone; you might spoil my plans or decide to play around with the artifact when I'm not looking, especially since I gave you the description for it. Got it, Scouty? Slicky? Smarty?"

    Lars "Why do I feel like we’ve become Earthling pets of some sort with all these weird nicknames?"

    Zephyr "I’ve been surrounded by so many brainwashed humans during the castle renovations that my brain cells are rotting by the lack of creativity and putrid repeated phrases. You could say their antics are rubbing off on me."

    Zephyr "Anywho, how can you convince me that you won’t be an obstacle to my plan until my castle is restored?"

    Rory "We’ll pinky promise"

    Rory "That’s the most you can get from us."

    Zephyr "See? Then there’s no reason for me to let you leave—"

    Lars narration "This won’t do! We must uncover the truth behind all of this."

    Lars narration "I can’t give up right now, not when I have a responsibility to protect my comrades."

    Lars "We’ll earn your trust."

    Zephyr "Somehow, I really doubt—"

    show sylvian mad at center_left
    Sylvian "[Lars]! What’re you trying to do?"

    show claude serious at center_right
    Claude "I’m not a fan of what you’re trying to pull here, Captain. Especially since it’s without me."

    Lars "You can’t pull that on us, you know? We also gave you a chance when you shared your story."

    Zephyr "…"

    Lars "You just need to give us a few minutes and listen to our case."

    Zephyr "…"

    Zephyr "Ugh fine! But just for a little. It’s not like I wanted to repay you back for listening to me, okay? OKAY?"

    "Everyone" "He’s definitely repaying us for listening to him."

    Lars "Master Sylvian, you’re the smartest person amongst us—"

    show claude shocked at center_right
    Claude "I’m hurt that you’re not even considering me Captain, but I also can’t deny that."

    Claude "You should have at least hesitated a bit…"

    Lars "We need you to come up with a plan!"

    show sylvian sad at center_right
    Sylvian "[Lars], why did you suggest such a thing to him?"

    Sylvian "He’s a dangerous person! Time-freezing? Brainwashing? How can you trust him so quickly after only a few conversations?"

    Sylvian "Now, his attention is directed toward you, or whatever you intend to discuss with him."

    show lars
    Lars "I don’t trust him; I just think that it’s best if we decide on a plan so I don’t get tongue tied like the last time he asked me a question."

    Lars "At least, I got us a little time so we can discuss our options."

    show claude serious at center_right
    Claude "Sorry, Captain. But I’m siding with Boss on this one."

    Claude "Just to clarify, my reasons are a bit different."

    show claude smile at center_right
    Claude "Boss Sylvian might want to divert his attention from us and discreetly find a solution to maintain his current peace and order. But I’m more inclined to jump right into the heart of the matter."

    Claude "He could be a secret royal heir for all I care, but I’m driven by curiosity. I can’t resist this challenge and let someone else take the credit for solving the mystery."

    Claude "I mean, a missing noble heir, a potentially unexplored castle, and an artifact that freezes time? When was the last time we faced a challenge like this?"

    hide lars
    Lars narration "Staying true to their personalities, both Master Sylvian and Sir Claude have their distinct motivations for wanting to unravel this mystery."

    Lars narration "As for me, I’m still uncertain about my own stance. Who should I confide in to discuss my decision?"

    menu:
        " " " "
        "Speak with Master Sylvian":
            $ options["CS6"]=1
            jump speak_with_Master_Sylvian

        "Speak with Sir Claude":
            $ options["CS6"]=2
            jump speak_with_Sir_Claude


label speak_with_Master_Sylvian:

    play music "track_6_romance_scene.ogg"
    #have everyone exit the scene and bring sylvian to the center
    hide claude
    hide rory
    hide zephyr
    show sylvian at center
    Lars "How do we present our case?"

    Sylvian "You have to understand, [Lars]. We need to show how weak we are in front of him so he loses interest."

    Sylvian "If he gets curious about the origins of our artifact, things could take a dangerous turn."

    Sylvian "He basically admitted to slaving away humans and descendants alike just for some castle renovations."

    show sylvian serious funny at center
    Sylvian "Does any of that sound rational to you?"

    show lars serious
    Lars "No, but shouldn’t we aim to ruin his plan for the same reason?"

    Lars "He’s robbing unsuspecting humans of their freedom. As members of ‘Custodes Sylvae,’ our duty is to rescue them—"

    show sylvian sad at center
    Sylvian "We’re just a merchant guild, [Lars]. I understand your sentiments, but we can’t rush into things like this."

    show sylvian at center
    Sylvian "We need more information about the artifact and then we can devise a plane, whatever it may be."

    show lars
    Lars "But how can we be sure if we’ll ever get another chance to speak with him like this, or if our countermeasure necklace will work again?"

    Sylvian "“Have patience. All things are difficult before they become easy.”"

    Sylvian "An opportunity will arise if we give it time."

    Sylvian "I can’t let him get his hands on any of my valuable guild members, especially not you."

    show sylvian blush at center
    show lars blush
    Lars "Master Sylvian?"

    Sylvian "[Lars], my world became quite distorted during my days in academia, like a scrambled puzzle. I was in a state where I couldn't progress until each piece fell into place."

    Sylvian "To my surprise, a piece did fall into my grasp, owing to an incredible chance, miracle, or even mere luck, and that piece is my precious guild. I don't want you to do anything irrational and risk losing anyone."

    Lars "I understand Master."

    show lars
    show sylvian at center
    Lars "Don’t worry, I have your back as well. I’m not going to let anyone touch my precious comrades!"

    Lars "Let’s just talk it out with the others for now. Alright?"

    Sylvian "I suppose this conversation can wait for another time."

    hide lars
    Lars narration "As I move away to speak with the other members, a faint whisper reaches me, though I can't discern its exact words."

    show lars
    show sylvian sad at center
    Sylvian "It’s been so long that I’ve reached out for a piece of my own accord that I’ve forgotten how to clench what’s already in the palm of my hand."

    hide lars
    Lars narration "I hope he didn’t say anything too serious."

    Lars "That’s right, let’s get a move on now."

    jump CS_6_End

label speak_with_Sir_Claude:

    play music "track_6_romance_scene.ogg"
    #have everyone exit the scene and bring claude to the center
    hide sylvian
    hide rory
    hide zephyr
    show claude smile at center
    Lars "How do we present our case?"

    Claude "My dearest Captain [Lars], I adore your stubbornness at times like this, so it’s only right that I offer my support."

    Claude "I believe it’s wiser to pique our new Lord’s interest in us rather than dismiss it."

    Claude "Picture this— he realizes we’re ordinary individuals and decides to incorporate us into his team of renovators."

    Claude "However, that would likely cut off our access to any information from the other members of his so-called army."

    Claude "That’s why taking direct action is imperative."

    Claude "I could take a more subtle approach and talk to the merchant again, inquire about possible tools or learn the story behind our artifact."

    Claude "But I can’t risk losing my seat in this interesting show."

    Lars "Sir Claude…"

    show claude blush at center
    show lars blush
    Claude "I would go on ahead on my own but I don’t want to leave my duo behind either."

    Claude "It would be no fun without you by my side, [Lars]."

    hide lars
    Lars narration "He called me [Lars]. I never thought I would hear him say my name in such a way."

    Lars narration "A serious expression is etched on Sir Claude’s face, and he gazes at me with anticipation."

    Lars narration "I suppose it’s only fitting that I match his level of enthusiasm."

    Lars "I understand!"

    show lars
    Lars "I can’t leave you all by yourself and I won’t have you take all the fun for yourself."

    hide lars
    Lars narration "Perhaps it was the surge of my newfound conviction or the palpable anticipation of an impending challenge that sent my adrenaline levels soaring."

    show lars
    show claude smile at center
    Claude "That’s what I wanted to hear."

    Claude "Adventures favor the bold and fortunate."

    Claude "We’ll end up misusing our lifetime of luck if we don’t take up this chance."

    Lars "That’s right, let’s get a move on now."

    hide lars
    Lars narration "As I move away to speak with the other members, I can hear Sir Claude make a loud declaration."

    Claude "I already used up a great portion of my luck so I can have this opportunity with you and I won’t give up on any chances!"

    Lars narration "What a riot…"

label CS_6_End:

    #once the player finishes with either of the two previous choice selections, we have the position change where rory and zephyr enter the scene. 
    #From left to right, it’s going to zephyr, claude, sylvian, rory
    play music "track_1_intro.ogg"
    show claude zorder 2:
        xalign 0.4
        yalign 1.0
    show sylvian:
        xalign 0.6
    show rory at right
    show zephyr happy at left
    show lars serious
    Zephyr "Ah enough talking. Come here Scouty!"

    hide lars
    Lars narration "I stride purposefully towards him and hold my tail straight as a sign of readiness."

    show claude smile at center_left
    Claude "You can’t stop now, Captain."

    Sylvian "You have to make him listen well, [Lars]."

    Rory "I’m rooting for you [Lars], show him what you’re made of!"

    hide lars
    Lars narration "If he truly is as dangerous as we all think, then I should try to get to the root of this issue and make sure he doesn’t use the time freeze artifact again."

    show lars serious
    Zephyr "Hurry up now, I don’t have all day."

    Lars "Young Lord Zephyr!"

    show zephyr sad at left
    Zephyr "Yikes, are you attempting to blast a hole through my non-existent eardrums or something?"

    Lars "We’ll be your private entertainers and provide the scoop you need for your renovation funds."

    hide lars
    Lars narration "I share a meaningful look with my fellow guild members, and it's clear that they are all equally puzzled. The silence that follows my suggestion serves as confirmation."

    show claude serious at center_left
    show sylvian serious funny at center_right
    show lars
    Rory "I don’t think it’s too late to come back just as confidently, [Lars]…"

    show zephyr happy at left
    Zephyr "What’re you trying to scheme Slicky? Are you trying to trick me with this sudden suggestion?"

    show lars
    Lars "It’s simple, we can’t stay suspended for too long."

    Lars "You won’t let us leave either because we could prove to be an obstacle for you. Not to mention, it seems you're more interested in keeping tabs on us than your army of humans."

    Lars "Hence, the best we can do is reach a compromise that suits both our interests."

    show claude blush at center_left
    Claude "That’s the kind of negotiation skill I’d like to see."

    Zephyr "…and your idea of a compromise is for me to have you all entertain me and give me a scoop?"

    show claude at center_left
    show sylvian at center_right
    Lars "You like to be entertained, don’t you? At your disposal, there is a famous merchant, puppet-master, magician, and a dragon pilot."

    Lars "You can earn a column's worth of gossip material and earn your funds without hurting anyone. Didn’t you say that you dislike brainwashing and kidnapping people as well?"

    Zephyr "Hmm, such insolence."

    Zephyr "However, I like to have fun as well. How will you tip the odds in our favor?"

    Lars "I don't need to. We're the only ones aware of your situation and still willing to listen. That's why we're the best suited to cater to your interests."

    show sylvian blush at center_right
    Sylvian "Great work, my dear junior. I knew I could trust you."

    Zephyr "That does make sense, so what will everyone be doing? I’m assuming Speedy will do some kind of puppet show again—"

    Lars "You’ll only take me as your entertainer and you need to promise to let the others go."

    Zephyr "Huh—"

    #for the next sentence, rory/claude/sylvian all jump up and down in surprise. The textbox shakes too.
    show rory at jp
    show claude at jp
    show sylvian at jp
    "Everyone" "{sc}WHAAAAT????{/sc}"

    show rory:
        yoffset 0.0
    show claude:
        yoffset 0.0
    show sylvian:
        yoffset 0.0
    Lars "After all, I'm a dragon pilot, so we already share quite a few common interests, especially considering that you’re a supposed dragon descendent."

    hide lars
    Lars narration "Please, take the bait!"

    show lars
    Zephyr "…"

    show lars
    Zephyr "…two."

    Lars "Hmm?"

    show lars
    Zephyr "I'd like two of you to take on the role of my personal  entertainers."

    show sylvian mad
    show claude serious
    show lars serious
    Zephyr "I’ll take you to my castle and the rest of you can prance around as it."

    Zephyr "It's a win-win situation for me since I can ensure your friends won't attempt anything while you're kept as hostages—uh, entertainers, I mean!"

    Zephyr "You have to keep me well entertained though considering I’m a huge fan of confessions and duo comedy routines."

    Rory "So you're trying to ice-olate us."

    #for the next sentence, zephyr does a small side to side shake
    show zephyr at shake
    Zephyr "Finally! Somehow who understands my sense of humor."

    Lars "But that’s not what I told you, it’s only supposed to be me. Here's the deal: no touching their hair, no messing with furs, feathers, scales, anything!"

    Lars "Also, you can't take us to your castle. Who knows how risky it could be when it's not fully renovated yet?"

    hide lars
    Lars narration "If he does go after the other guild members, he’ll notice that we don’t have any special powers to counteract the artifacts' time suspension effect. We could all get caught without any counter measures! I don’t want to risk going to an unknown location either."

    show lars serious
    Claude "Don’t get too excited now, Captain. I’m not going to let you go down this route by yourself—"

    Sylvian "Forget the plan, we didn’t discuss this self-sacrificing scenario, [Lars]! You mustn’t risk—"

    Zephyr "Hey, Scouty, you didn’t listen to me, it seems. Single confessions are for the holy folk, not for entertainment."

    Zephyr "How are you going to do a duo comedy with only yourself?"

    Zephyr "Are you going to have a heart-to-heart with your reflection in the mirror, or perhaps consult your spineless shadow for therapist advice?"

    Zephyr "You’re lucky I’m a benevolent enough person because I’ll at least give you the option to choose."

    Zephyr "Pick between Smarty and Slicky over there, since I already had Speedy entertain me."

    Lars "…"

    show sylvian sad at center_right
    Sylvian "[Lars], I can’t leave you alone like this, otherwise…"

    show lars
    Lars "Master—"

    show sylvian at center_right
    Sylvian "Let us go to his castle together."

    Sylvian "Even though I disagree with this hasty approach, I’ll do my best to assist you with my knowledge and magical prowess."

    if options["CS6"]==1:

        show sylvian blush at center_right
        show lars blush
        Sylvian "You're a cherished member of my guild, one of the few things I've gotten right—a rare and perfectly fitted puzzle piece that I won't jeopardize or let slip away, even if it means disrupting my current state of peace."

        hide lars
        Lars narration "The intensity of Master Sylvian’s gaze pins me, and my heart skips a beat in response. The heat in his stare seems to sear through me, and I can’t help but feel the weight of his words hanging in the air."

        Lars narration "I can’t believe that I was this important to him."

        Lars narration "Perhaps there’s a chance to uncover more about him in the future."

        Lars narration "Why he departed academia and how it caused him to abandon his past and establish the guild for us, alongside the rationale behind his motto of life to keep things uncomplicated and go with the flow."

        Lars narration "Most importantly, I wonder why he wants me to be safe within his sight…"



    show claude at center_left
    Lars narration "Soon enough, Sir Claude speaks up as well.  His eyes show me a flicker of excitement and he looks at me with an anticipative gaze as if he wants me to choose him"

    show claude smile at center_left
    Claude "Captain, didn’t we talk about our future plans together? What kind of a duo would we be if one left the other behind?"

    Claude "In a world of limitless horizons and uncharted trails, I am a wanderer at heart, forever seeking new thrills and adventures."

    Claude "Yet, amidst the uncertainty that lies ahead, I want you to choose me to walk by your side."

    Claude "I’ll make the journey worthwhile for you with my charm and experience."

    if options["CS6"]==2:

        show claude blush at center_left
        Claude "Plus, we’ll make quite the successful team if we tackle this mystery together."

        Claude "An adventurous duo isn’t complete without its counterpart, and if it’s not you walking that path with me, then I won’t have anyone else to share it with."

        hide lars
        Lars narration "The intensity of Sir Claude’s gaze pins me, and my heart skips a beat in response. The heat in his stare seems to sear through me, and I can’t help but feel the weight of his words hanging in the air."

        Lars narration "I can’t believe that I was this important to him as his guild member."

        Lars narration "Perhaps there’s a chance to uncover more about him in the future—"

        Lars narration "His relationship with his family and his motivations for distancing himself from them, alongside the reason behind his affinity for challenges and ambition."

        Lars narration "Most importantly, I wonder why he wants me as his partner in this venture…"



    Lars narration "It looks like I’m stuck in a dilemma. Who will I choose as my partner?"

    jump select_route

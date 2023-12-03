label part_1:

    play music "track_1_intro.ogg"

    scene bg_1 with fade
    
    Lars default "‘Discere, cogitare, agere— the triad of wisdom.’"

    show bg_2 at bg_blur

    Lars default "‘Learning enriches the mind, and thinking sharpens it, but it is through action that we truly manifest our knowledge and shape our reality.’"

    
    Lars narration "One would think that a merchant guild wouldn’t bother creating such a philosophical motto and instead advertise one plus one dragon ship seats every holiday season."

    Lars narration "We could even offer complementary earthling-made meals by the human chefs who were transported to our realm upon their death."

    Lars narration "But then again, we wouldn’t be embarking on artifact hunts and historical expeditions if the sole purpose of our guild, ‘Custodes Sylvae’, was commerce."

    show claude serious at center
    "Unknown" "Who on Divonia is mumbling this loud to themselves early in the morning?"

    "Unknown" "I’m losing my beauty sleep over here."

    Lars narration "I steal a glance from my perch atop the dragon ship and it looks like one, or should I say, the only passenger, has woken up in quite a grumpy manner."

    menu:
        Lars " "

        "Playfully surprise him":
            $ options["C1"]=1
            jump playfully_surprise_him

        "Resist the urge to surprise him":
            $ options["C1"]=2
            jump resist_the_urge_to_surprise_him


label playfully_surprise_him:

    Lars narration "Something tells me I should surprise him, just to cheer up the mood."

    
    Lars default "It’s me, Sir Claude. Did you already forget about  your comrade after a few hours of sleep?"

    show claude smile at center

    show claude
    Claude "Ah, my dearest Captain [Lars]!"

    Claude "How could I ever get that nightingale-like voice of yours out of my head? It’s almost like my personal alarm clock!"

    
    Lars narration "Up for a challenge this early? Typical."

    
    Lars default "I’m glad you appreciate my vocal talents. But you know, I can’t take all the credit."

    Lars default "You’re the one who inspires me to mumble so loudly during our journeys."

    Lars default "It’s the only way I drown out your snoring."

    show claude default at center
    Claude "You always find a way to turn the tables, don't you?"

    Claude "And my snoring?"

    Claude "Hah! I can capture your attention through other means, if I choose to."

    jump C_1_End

label resist_the_urge_to_surprise_him:

    
    Lars narration "It’s best that I focus on piloting our dragon first. Otherwise, I’ll never hear the end of it."

    
    Lars default "Good morning to you too, Sir Claude."

    show claude shocked at center
    Claude "What a boring reaction. I expected more spunk from you…"

    Lars default "Nevermind then. Hmph!"

label C_1_End:

    
    show claude neutral
    Lars narration "It’s truly a wonder how he managed to stay asleep throughout our entire journey, considering the lack of proper seat arrangements or resting areas on our new dragon ship."

    Lars narration "However, Sir Claude has always been notorious for his resourcefulness in such moments owing to his history of travels and adventurous ordeals despite his comfortable upbringings."

    
    Lars default "I will return to my duties, then, Sir—"

    Claude "Didn’t I already tell you to drop the ‘Sir’ for the umpteenth time, Captain?"

    Lars default "Do we have to go over this cliche back and forth as well?"

    Lars default "I promised I’d do it if you stopped insisting on “Captain this” and “Captain that”."

    show claude smile
    Claude "It makes us seem more of an adventurous pair, though, don’t you think?"

    
    Lars narration "Indeed, and there is a good reason for that."

    Lars narration "My knack in piloting and his remarkable merchant abilities just clicked. Whether it was going on expeditions, dealing in trades, or connecting with the quirky passengers we often had..."

    Lars narration "We always made an efficient team. Maybe even the best among all the guild members."

    Lars narration "Well…at least, if you ignore that there are only four of us."

    Claude "Now that I think about it, what were you talking to yourself about?"

    Claude "Confiding trade-secrets to our lovely dragon, Spotsy? Or even a secret confession for me—"

    
    Lars default "She doesn’t even have any spots. Bad at naming as always, Sir–"

    
    Lars narration "He lets out an intrusive cough."

    
    Lars default "--Claude. Not to mention, the confession jokes won’t work if you keep repeating them over and over again."

    show claude neutral
    Claude "Who knows, maybe one day, I'll surprise you with a confession that will leave you speechless."

    
    hide claude
    show spotsy
    Lars narration "I reach out, my hand confidently caressing the head of our newest guild member who I hope I’m taking good care of."

    Lars narration "Her eyes meet mine in and in a show of trust, her relaxed scale’s part open, revealing mesmerizing azure flames simmering underneath."

    Claude "Don’t let your attention wander off too much, Captain."

    Lars narration "Sir Claude's voice carries a subtle touch of displeasure as he observes me caressing Spotsy's head."

    Lars narration "Maybe the uncomfortable seating arrangement is getting to him— He had always been known to grow a tad irritable when he felt he wasn't receiving the attention or results he desired."

    Claude "No need to spoil her like that. She’s just a glorified lizard with fiery breath."

    show smoke
    Lars narration "As if to express her annoyance, Spotsy lets out a dark, puffy plume of smoke from her nostrils. A low rumbling note resonates from her throat, a clear indication of her irritation."

    hide smoke
    hide spotsy
    
    
    Claude "She doesn’t like it, hmm…that just makes me want to do it even more though."

    Claude "Not to mention, I wouldn’t want to be that poor passenger who accidentally dies early and transports to the Earth realm just because you were adoring our newest ship. There have been too many events like that happening these days."

    
    Lars narration "His sudden change of topic leaves me slightly bewildered. I withdraw my hand from Spotsy's head, and she shakes her head as if still searching for my comforting touch."

    Lars narration "In contrast, a mischievous grin adorns Sir Claude's face. Why would he be happy about it? Maybe the problem wasn’t the seats after all…"

    show claude shocked
    
    Lars default "The numbers of transported humans have certainly increased quite a bit these days."

    Lars default "Even still, they are a precious rarity. In all my years of flying travelers across the lands of Divonia, I have only ever met a handful of them."

    show claude neutral
    Claude "Not many would want to undertake the journey of transitioning to a new realm they know nothing about, after all."

    Lars default "I understand that, but they always fascinate me with the tales of their past life."

    Lars default "All our guild members were born and raised here, so I don’t have the chance to closely work with one of those travelers either."

    show claude smile
    Claude "Tsk, tsk, already thinking of replacing me with someone else, are you, Captain?"

    Lars default "You said it yourself before, one has to admire their bravery, since descending into Divonia is a grand leap of faith into the unknown."

    Lars narration "He chuckles. Claude is always the most spirited one when faced with adversity and adventure. Must feel great."

    Claude "Ah, how gladly I would take their place if I could…"

    Claude "Life can get pretty boring when you have everything you need in the palm of your hand."

    
    Lars default "Always trying to satisfy your thirst for adventure, eh?"

    
    Lars narration "I could hardly recall a day when Sir Claude didn’t turn a simple task into a grand quest. He always was, and still is, on the lookout for opportunities to embark on new escapades."

    show claude default
    Claude "I’d advise you to concentrate on steering for now, Captain, before you get even more distracted. I feel your gaze burning my scales."

    
    Lars default "Oh, don’t flatter yourself, your scales are nothing compared to Spotsy’s."

    
    Lars narration "My playful grin is met with crossed arms and a sulky stare. I suppose I should stop the teasing, he takes too much pride in his appearance."

    Claude "Well, I suppose it's my mistake for attempting to catch the attention of a certain dragon-obsessed pilot. What will become of my grandiose confession now?"

    
    Lars default "Don’t be so hard on yourself, Claude. You know I appreciate you for more than your appearance even if I rank you below Spotsy. Stopping the confession jokes could help though—"

    show claude serious
    Claude "There is no no need for empty flattering. I already get enough of them whenever ‘Dupont’ is mentioned."

    Claude "However, you need to make sure to take care of her well since I did make quite the effort for her exchange."

    
    Lars narration "A quick change of topic per usual. Sir Claude has the habit of doing so whenever his family is mentioned. I used to wonder if he was doing so to maintain his privacy as a renowned golden spoon but despite the many years we spent together as partners, the sentiment never changed."

    Lars narration "If memory serves me right, our negotiator unloaded all his prized possessions onto us the moment he caught wind of the ‘Dupont’ surname. I don’t think that is an “exchange”."

    Lars narration "Though, I suppose having an outrageously high-class family name like Claude makes one’s trade prone to that."

    
    Lars default "I thought I saw you arguing about that one specific artifact, though?"

    Lars default "They were so adamant to wash their hands of it they wanted to add it on top of everything else.."

    show claude shocked
    Claude "I’m not one to accept gifts without scrutiny. But there was something about that artifact—"

    Lars default "You mean artifact box."

    Claude "—that piqued my interest."

    Lars default "What if it turns out to be hazardous or a curse? Scrutiny would have been welcomed."

    Claude "I had plans beforehand of adding some more excitement to my list, so I might as well embrace the opportunity."

    Lars default "Right, because who wouldn’t jump at the chance to receive an artifact with no known origins, suddenly materializing out of thin air, and with no apparent acquisition date?"

    show claude serious
    Claude "Your sarcasm is showing Captain, might want to hide it under a thin layer of worry or, Divs forbid, concern for your partner."

    menu:
        Lars " "

        "Apologize for teasing him":
            $ options["C2"]=1
            jump apologize_for_teasing_him

        "Continue teasing him even more":
            $ options["C2"]=2
            jump continue_teasing_him_even_more


label apologize_for_teasing_him:

    
    Lars default "I apologize, Sir Claude. You know I have no ill intentions."

    Claude "Oh, how it pains me to witness my most faithful, loyal, and devoted companion trying to replace me with some unknown reincarnate, and also MOCKING my skills? My scales are going to shed off from the misery of it all."

    Lars default "Come on, Sir Claude. Don’t be so dramatic. You know I’m only teasing you as payback."

    show claude shocked
    Claude "I am baffled, dumbfounded, bamboozled, shocked, bewildered, and confuzzled to the highest degree."

    Lars default "You’re irreplaceable to me, and your merchant skills are unmatched—"

    Claude "Hmph, why should I trust your word? You should know that actions speak louder after all."

    Lars default "Then…how should I show it to you?"

    Claude "There’s something that I really want but with our relationship as is, you won’t be able to give it to me."

    show claude default
    
    Lars narration "My fur prickles with anticipation. I can sense my ears perked up, betraying my keen interest in his next words and what he could possibly want from me."

    
    Lars default "A gift? For you? But you already have everything you need."

    Lars default "Your family has your pockets lined with all the gold and treasures imaginable too, so I can’t see what you’d want"

    show claude
    Claude "I’ll tell you more about it in due time."

    jump C_2_End
    return

label continue_teasing_him_even_more:

    
    Lars default "The infamous Claude Dupont, not checking the items he negotiates for?"

    show claude serious
    Claude "Please, [Lars], you should know better than blabbering ‘Dupont’ recklessly.."

    Claude "In any case, he was acting suspicious. But even then, I could not resist indulging my curiosity, having seen the artifact or not."

    
    Lars default "Weren’t you going to continue calling me ‘Captain’ as well?"

    Lars narration "He leans close and his fingertips gently brush against my cheek, leaving a trail of warmth in their wake, as his golden eyes lock onto mine with unwavering intensity."

    Lars narration "His voice deepens, resonating with a seductive allure - lips tantalizingly close to my ear. He uses them to send shivers down my spine with a whisper"

    show claude shocked
    Claude "See? I used your name, so you have to call me by mine too...without the titles."

    Claude "I prefer it when you say my name after all. It’s one of the tiny joys of my life."

    Lars narration "The sudden remark takes me by surprise, even though it’s not the first time I’ve heard Sir Claude make such a comment. After all, he possesses a captivatingly flirtatious nature, effortlessly weaving his charm into every interaction."

    Lars narration "However, a part of me hesitates, fearing that surrendering to his banter may lead to my own demise. And so I find myself stumbling over my words, caught in a tangled mess of stuttering syllables."

    
    Lars default "W-w-what are you saying all of a sudden?! Did you lose your mind?"

    Claude "Awe, is our captain getting shy all of a sudden? Did you know your ears get red when you're embarrassed?"

    
    Lars narration "With little time to question his truthfulness, I instinctively place my hands on my ears, hoping to shield any trace of vulnerability that might betray my reaction to his words."

    
    Lars default "I am a dragon pilot, an unwavering force soaring through the skies."

    Claude "Yes, indeed. That much is observable from our current position."

    Lars default "My years of experience have honed my resilience and steeled my resolve. I cannot allow myself to be easily affected by the whimsical words of Sir Claude, no matter how charismatic he may be!"

    show claude smile
    Claude "Awe, did I get under your skin, Captain? So much that you had to switch to third-person commentary?"

    
    Lars narration "Sir Claude remains unfazed by my momentary embarrassment except for a triumphant smile."

    
    Lars default "After all, he’s only joking to gauge my reaction—"

    Claude "Haha look at you! Navigating the skies like a pro with those sharp fox eyes, but missing the obvious right in front of you."

    
    Lars default "Pardon?"

label C_2_End:

    show claude default
    Claude "Let’s continue this conversation late, shall we?"

    Claude "Our dearest Guild Master is signaling our landing spot."

    
    Lars narration "I glance downward, and our destination near the sea comes into view. Like an artist painting delicate strokes on a canvas, Master Sylvian has already lined up the location with an array of enchanting flowers."

    Lars narration "Each bloom carefully chosen to mark our path with a vibrant array of sunflowers and roses. Their vivid colors stand out, captivating the eye and creating a striking contrast against the backdrop of the serene oceanic landscape."

    Lars narration "The gentle breeze carries the sweet fragrance of the flowers, adding to the enchanting ambiance"

    
    Lars default "Ah, it’s a shame we arrived so early. I was hoping to learn something new."

    Lars default "But, most importantly, I have to reward Spotsy well when we get back."

    Claude "I’d be inclined to say that you didn’t manage to tap into our dragon’s full potential captain. Owning up to how I stole your attention for more than half, or better yet, the entire ride."

    Claude "However, since you managed to get us here without any dangerous maneuvers, I’ll allow you to be the first to touch our newest artifact. I tend to appreciate and reward my companions well, especially if they’re my lover—"

    
    Lars default "I’d argue that being the first person to touch a suspicious artifact is the last thing I’d prefer to do."

    show claude smile
    Claude "It’s the first time it’s made its way to our side of the realm, hence the occasion is quite momentous."

    Claude "You could say the thrill is irresistible."

    
    Lars narration "He locks eyes with me, and I can’t help feeling a tad self-conscious under the weight of his declaration, whether it was actually meant for me or not."

    Claude "And let’s not forget, it’s the first person who gets the real taste of discovery, not the second or anyone who follows."

    Claude "If you don’t seize this moment now, who knows when you’ll get another chance to dive into it, learn more, and delight your passengers with captivating stories?"

    
    Lars default "Fine! Now let me focus before any of us plummet to their death."

    show bg 2 with fade
    play music "track_2_field_of_flowers"

    Lars narration "As the sole passengers aboard the dragon ship, guiding Spotsy in her safe descent was a seamless task. The proximity to the water offered a perfect opportunity for her to release some pent-up energy too."

    Lars narration "Hopefully, she’s not too tired from the journey. I’d hate to burn her out from the get-go and leave a negative first impression behind."

    Lars narration "Once we disembark, our attention turns to the tall and slender magician who makes his way towards us."

    show sylvian blush
    Lars narration "A warm smile graces his lips as his obsidian wings flutter gracefully."

    Lars narration "With a hushed incantation, the brim of his hat blossoms into a vibrant tapestry of roses and sunflowers, their delicate petals unfurling in a mesmerizing display. The air is instantly infused with their soft fragrance, which mingles with a refreshment spell."

    "Unknown" "Welcome back, dear members of ‘Custodes Sylvae’. I’m happy to see that you both landed safely."

    "Unknown" "[Lars], your piloting was truly magnificent as always. It’s a sight that I’m honored to witness every time."

    show claude default
    Claude "It wouldn’t be a warm welcome if Master Sylvian weren’t here to receive us."

    show sylvian default
    
    Lars default "Thank you, Master. I wish you could have joined us on the ride too. Sir Claude here almost caused us to plummet to our doom...multiple times I must say."

    show claude shocked
    Claude "Eh, I did promise to reward you later, didn’t I? Drum roll please ~"

    play sound sfx_drum_roll
    
    Lars narration "With a flourish of his hands, Sir Claude performs a series of gestures that mimic a drumroll. Tension fills the air as the anticipation builds up, drawing everyone’s attention."

    Lars narration "Then, in a dramatic display, he spreads his arms wide, showcasing a grand reveal which is…"

    stop sound
    Lars narration "…nothing?"

    Claude "Haha, I seem to have left it on the ship."

    
    Lars default "Should I go get it, then?"

    show claude smile
    Claude "No need, my dear Captain. Boss Sylvian can handle it. You and I have been quite busy, and the cargo box is heavy enough to demand a touch of fresh energy."

    
    Lars default "We can’t ask that from our senior, Sir Claude! Especially when I'm perfectly capable—"


    show sylvian
    Sylvian "Aren’t you tired from guiding our new dragon, [Lars]? I could easily fly and grab it for you. It’s no trouble at all."

    menu:
        Lars " "

        "Ask Master Sylvian to grab the cargo for you":
            $ options["CS1"]=1
            jump ask_Sylvian_grab_cargo

        "Tell Sir Claude to grab the cargo himself":
            $ options["CS1"]=2
            jump tell_Claude_grab_cargo


label ask_Sylvian_grab_cargo:

    
    Lars default "Would that be alright with you Master? I’d like to spend some time with Sir Claude."

    Sylvian "I respect your choice [Lars], even though—"

    show sylvian blush
    Sylvian "I also wanted to spend some time with you…"

    Sylvian "But uhm, never mind, I suggested it in the first place after all."

    show claude serious
    Claude "Awe, you choose to stay with me instead of Boss Sylvian, I’m touched, Captain."

    Claude "I’ll have to give you a special reward later in private."

    
    hide sylvian
    show claude smile at center
    Lars narration "His hands gently encircle my waist, drawing me closer to him as he whispers the last part of his sentence. As his eyes, akin to pools of molten sunlight, meet mine, a mischievous spark dances within them. While I might usually dismiss this as him being more touchy-feely than usual, his last comment makes me think otherwise."

    Lars narration "Yet, beneath that playfulness, there lurked a subtle undertone of competition, evident in the way he regarded Master Sylvian. It was as if they shared a friendly rivalry, each vying to outdo the other in their unique way."

    show sylvian
    
    Sylvian "Ahem! Not to interrupt but I’m sure Rory will arrive soon, so it’s best to prepare yourself, [Lars]."

    Sylvian "As for you, Claude, remember what I said about teasing him too much?"

    show claude default
    Claude "Before worrying about Captain over here, you should head on to where our new dragon is resting, Boss."

    Claude "We wouldn’t want her to accidentally drop our cargo to the depths of the sea."

    hide sylvian
    Lars narration "As Master Sylvian takes flight, his swan-like wings seem to catch every ray of sunlight, causing them to shimmer and gleam like ethereal jewels. The sight is truly breathtaking, and I find myself in awe of the beauty before me."

    "Unknown" "Clauuuuuuuuuuuuudy~"

    show claude smile
    Claude "Roryyyyyyyyyyyyy~"

    Lars narration "A figure emerges from where Master Sylvian stood just a few seconds ago, and to my pleasant surprise, it is none other than Rory, my childhood best friend."

    show rory default

    show rory
    Rory "I believe I mentioned that if I ever catch you bossing [Lars] around, I’d pluck out your lizard eyes to adorn my newest puppet, Agatha."

    Rory "You should know that my threats work quite effectively, especially with how Brittina’s puppet dress is shimmering with the scales you’ve kindly donated...in your sleep, of course."

    Lars narration "True to her lineage as a bull descendent, Rory possesses a fiery temperament and is quick to charge at those who annoy her."

    Lars narration "The Kyoko blacksmiths and the Dupont merchants have been locked in a spirited rivalry for generations. Both families have passed down their competitive natures to their heirs, adding fuel to the fire."

    Lars narration "However, Rory was an exception to the traditional path of the Kyoko family. While blacksmithing was the cornerstone of their legacy, Rory’s talents lay elsewhere. She found her passion in puppet shows and other forms of artistic expression."

    Rory "[Lars], you’re here too! Awe, I missed you so much."

    
    Lars default "Rory, it’s so nice to see you again."

    Claude "If it isn’t our hot-tempered bull, breathing fire as soon as she lays eyes on me."

    Claude "It’s a pleasure to see you again, little Rory. Or should I say, a curse to behold?"

    show rory angry
    Rory "It’s just RORY! Call me a midget again, and you'll find more of your receding hairline gracing puppet Alex…"

    Claude "Now, now, I would have to say these finely braided silver strands that I’ve so kindly donated to you are what’s bringing half the revenue for your puppet shows, aren’t they little Rory?"

    Rory "You really have the gall to talk to me like that, when all your travel funds are conveniently collected from my shows?!"

    Rory "Such audacity doesn't appear out of nowhere unless the heat has really gotten to your head."

    Rory "How about a calming dip in the sea to cool off a bit? Let me help with a gentle push."

    Claude "I'm sure the hydro dragons would be delighted to have me amongst them."

    Rory "Hmph, you could put your merchant skills to use there, too. Ten more seconds to live for a platter of rotten lizard meat."

    show claude default
    show rory default
    show sylvian default
    Sylvian "I’m back with the cargo!"

    Lars narration "Thankfully, Master Sylvian swiftly intervenes, diffusing the tension with his timely return."

    Lars narration "In his grasp, he holds a grand and ornate box, its intricate design hinting at the secrets it conceals within."

    Lars narration "The weight of anticipation fills the air as all eyes turn to the box, momentarily diverting attention from the conflict."

    jump CS_1_End

label tell_Claude_grab_cargo:

    
    Lars default "Sir Claude, can you bring the artifact yourself? I’d like to spend some time with Master Sylvian."

    show claude shocked
    Claude "I’m shocked, Captain. Choosing Boss Sylvian over me?! I wouldn’t have imagined. You even ignored my request about dropping the 'Sir’ part."

    show sylvian default
    Sylvian "I am grateful that you wish to share your time with me, [Lars], even if you’re tired from your journey."

    Sylvian "Rory will arrive soon as well, so we all can spend some time together."

    
    Lars narration "Master Sylvian gently touches the brim of his hat and a magnificent bouquet blooms forth."

    hide all
    show object sylvian flowers
    Lars narration "Sunflowers rise proudly, while lavender blossoms intertwine. Brilliant clusters of marigolds sprout forth as well."

    Lars narration "I remember that his hat was one of his personal crafts, a magical creation that bloomed flowers according to his mood. It’s unfortunate that I’m not well—versed in flower languages; otherwise, I would be able to decipher the heartfelt messages he wishes to convey through these enchanting floral gifts."

    Lars narration "Nonetheless, I can’t help but feel treasured whenever he gives me gifts. Perhaps it’s due to a reaction I had once, or maybe he simply cherishes all moments we share."

    Lars narration "After all, I’ve noticed that he hasn’t given this kind of gift to anyone else, and the thought warms my heart for some reason…"

    show claude serious
    show sylvian default
    Claude "Quite the showmanship, Boss. Though I wonder if Captain over here got the message in your subtle gesture."

    Lars narration "Master Sylvian presents me with the bouquet, throwing a smile at Sir Claude."

    Sylvian "It might be best for you to take care of your task, Claude. We’re still not sure of the origins of the artifact you brought and there needs to be a level of caution involved as well."

    
    Lars default "That’s exactly what I said!"

    
    Lars narration "As Sir Claude takes his leave, his silver lizard tail gracefully sways behind him, reminiscent of the rhythmic movements of the sea. His scales, resembling those of the majestic dragons I often encounter in my journeys, captivate my gaze with their intricate detailing, despite their diminutive size."

    Lars narration "However, before I can fully immerse myself in the enchanting display, a sudden voice slices through the air with an excited tone."

    show rory default
    Rory "[Lars]!"

    
    Lars default "Rory, it’s so good to see you again!"

    Rory "You too! And good to see that slithering, slimy tail going away."

    
    Lars narration "The figure that emerges from where Sir Claude stood just a few seconds ago, is none other than Rory, my childhood best friend. True to her lineage as a bull descendent, Rory possesses a fiery temperament and is quick to charge at those who annoy her."

    Lars narration "Under Master Sylvian’s guidance, she apprenticed as the guild’s head of finance, helping us gather funds for every mission through her puppet shows."

    Rory "Mentor, I was preparing my puppets for the afternoon show at the market square. I feel like something is missing but I don’t know what exactly…"

    Sylvian "Let’s work together to find something to inspire you before the show, shall we?"

    Rory "Thank you, Mentor. I don’t know if my family will be there but I don’t want to disappoint them in case I miss the mark with the show later today."

    Lars narration "The Kyoko blacksmiths and the Dupont merchants have been locked in a spirited rivalry for generations. Both families have passed down their competitive natures to their heirs, adding fuel to the fire."

    Lars narration "However, Rory was an exception to the traditional path of the Kyoko family. While blacksmithing was the cornerstone of their legacy, Rory’s talents lay elsewhere. She found her passion in puppet shows and other forms of artistic expression."

    Rory "They’re already giving me side glances for not working with them in the blacksmiths."

    Sylvian "Do you need me to talk with them, Rory?"

    Lars narration "Rory offers a faint smile, her thumbs anxiously twiddling together."

    Rory "There’s no need. They’re the type to be appeased with actions rather than words. The best I can do is prove that I was made for the puppeteer business."

    Rory "When life gets tough, I just have to remember to stay strong and keep charging!"

    
    Lars default "Haha! That’s right, Rory, it’s not about the size of the bull, it’s about the size of its determination!"

    show rory angry
    Rory "Come on, [Lars]. No shorty jokes. A certain someone spews enough of them already."

    Lars default "Alright, alright. I’ll make it up to you by helping you out for the show."

    show rory default
    Rory "Yay~ Thank you!"

    show claude default
    Claude "I have arrived with our mystery artifact."

    
    Lars narration "Speaking of the devil, Sir Claude makes his entrance with the ornate box cradled in his arms. His eyes glimmer with a mixture of anticipation and excitement as he gazes at the artifact."

    Lars narration "However, rather than keeping it for himself, he extends the box towards me."

label CS_1_End:

    Lars narration "As the  heavy weight of the artifact transfers to my hands, I feel a sense of responsibility settle in."

if options["CS1"]==1:

    
    Lars default "I think I can take it from here, Master."

    show sylvian default
    Sylvian "Carrying such things after your tiring journey might affect your health, [Lars]."

    Sylvian "But thank you for worrying about me…I really appreciate it."



else:

    
    Lars default "I think I can take it from here, Sir Claude."

    show claude smile
    Claude "Anxious for the reveal. Aren’t you?"

    Claude "Don’t worry, I’m not a fan of breaking promises. Especially, for one I made with you."

label if_op_cs_1_end:

    show sylvian default
    Sylvian "Let me cast an energizing spell for you just in case, [Lars]. I wouldn’t want you to hurt yourself carrying something heavy like that."

    Sylvian "If there’s one thing my academic days have taught me, it is to not overwork when there’s an easier alternative available. No one will truly appreciate your effort if you're the sole person assigning value to it."

    menu:
        Lars " "

        "Accept his offer":
            $ options["S1"]=1
            jump accept_his_offer

        "Reject his offer":
            $ options["S1"]=2
            jump reject_his_offer


label accept_his_offer:

    Lars narration "Something is telling me I should accept his offer."

    
    Lars default "Yes, please. I really need a break after all the piloting and this box isn’t doing me any favors either."

    
    Lars narration "Instantly, Master Sylvian utters an incantation and a sense of liveliness washes over me, like the exhilaration that follows after completing a marathon."

#***** ERROR ***** Command not recognized
#[vertigo effect -sample from drive-

    Sylvian "Are you feeling better now? I could conjure up some stalks to help with the box as well—"

    
    Lars default "It’s okay Master, I need to get in my daily dose of exercise too. I don’t want you to think that I’m too weak for one box! More than that, what would our passengers think if their pilot wasn’t able to pick up their luggage or equipment. My parents wouldn’t let me live this down if they ever heard such rumors since they raised me to give my all to take care of those around me considering—"

    show sylvian angry
    Sylvian "Oh, my…"

    Lars default "Haha, nothing to worry about! But did you know, Master Sylvian? I was researching Spotsy and as part of the Azureflame species, the intense temperature generated through their breathing process can cause the air pockets under their scales to bubble and expand. Their azure distortions aren’t for mere show either, Rory mentioned that certain blacksmiths hire them for their forging practices since the heat produced is exceptionally hotter than regular flames, making it a valuable resource for crafting extraordinary weapons and armor—"

    Sylvian "As much as I enjoy hearing you talk—"

    show claude shocked
    Claude "More like ramble."

    show sylvian default
    Sylvian "—about the dragons which you treasure, we need to calm you down a little. Let’s use that breathing technique that I taught you last time. You remember, [Lars]?"

    
    Lars narration "He takes my hand into his own, slowly tracing circles on my palm. His touch feels warm, and there’s a slight hint of perspiration, as if he’s nervous about holding it."

    Sylvian "Breathe for 3 seconds…hold it for 6…now release it for 9 seconds…"

    Lars narration "Obediently, I follow Master’s instructions, allowing my breath to gradually slow down. With each measured inhale and exhale, a sense of calm envelops me, grounding me in the present moment."

    Sylvian "No one is going to think those things of you, [Lars]."

    Sylvian "If I were a dragon, I wouldn't want any other handler than you to take care of me. I've seen how you praise their efforts and spoil them senselessly."

    Sylvian "I mean, who wouldn't want to be praised by someone they admire...I mean, I do admire you, and I hope that, but ughh..."

    Lars narration "Master Sylvian suddenly takes hold of the tips of my fingers, as if he’s shying away from holding my hand fully."

    Lars narration "His gesture is tender and filled with a subtle intimacy. Yet, it also carries an air of vulnerability, as if he’s unsure of how to express his emotions openly."

    show claude smile
    Claude "So, what I gather is that Master Sylvian wants to have [Lars] ride him—"

    Lars narration "A chuckle escapes me at Sir Claude's jest. But in the blink of an eye, Master Sylvian's demeanor shifts. He turns his head away quickly, almost as if he's trying to conceal his reaction. Yet, even from behind, I catch a glimpse of his ears reddening slightly."

    Claude "My my, are you feeling hot all of a sudden, Boss? It must be because of all the cloaks and layers you’re wearing."

    
    Lars default "He's joking, Master Sylvian. Just forget about him. I appreciate the energizing spell, even if it didn't work out like we thought."

    Sylvian "Definitely not. I'll have to look into ways to tweak it for better results in the future."

    Lars default "And not just that...I, um, wanted to thank you for helping me stay calm and for the motivational words. It's not often that someone praises my dragon skills. I thought no one really cared."

    show sylvian angry
    Sylvian "OF COURSE I DO!"

    show sylvian blush
    
    Lars narration "His outburst catches me by surprise because I rarely see Master Sylvian raise his voice."

    Sylvian "I don't think it's the right place to talk about this, but know that I always keep you in my mind."

    
    Lars default "Haha, I know, Master. You're not just a Boss to me; you're a friend as well."

    Sylvian "Ah, what a joy to be  just a friend to you…"

    Sylvian "Maybe my own lack of directness caused this in the first place."

    Lars default "Pardon me?"

    Sylvian "N-N-Nothing, uhm, yeah, nothing to concern yourself with. Let’s analyze the artifact now, s-shall we?"

    jump S_1_End

label reject_his_offer:

    
    Lars default "Thank you for the offer, Master. But it’s nothing I can’t shake off."

    
    Lars narration "A dejected look embraces his face and though I feel guilty about his kind proposal, I stand firm with my decision. Yet, just as the tendrils of awkwardness begin to snake through the air, Sir Claude deftly steps in."

label S_1_End:

    show claude serious
    show sylvian default
    Claude "Ehem, I think we’re better off witnessing the artifact before the evening sets in and little Rory decides to pull something off for her puppets again."

    show rory angry
    Claude "I can see fumes exiting her head as we speak. Oh look! I think they got even bigger."

    Rory "Ugh, I can’t deal with this again."

    
    Lars default "Alright everyone, settle down. What should we do now, Master?"

    
    Sylvian "Let me cast a safety spell over the box first, you can never be sure if there are any hidden traps inside."

    
    Lars narration "After a few seconds of sparking light and anticipation, the box remains unresponsive, devoid of any notable reactions."

    Sylvian "No traps or enchantments detected. It seems we’re in the clear. Let’s unveil the treasure within."

    Lars narration "As I gingerly lift the lid of the ornate box, a breathtaking sight unfolds before me. Resting on a bed of plush velvet is a long necklace, the simplicity of its leather band belying the allure of its design. However, it's the centerpiece that commands attention—a dazzling red gem, radiating a mesmerizing ruby hue that captures the gaze of all who behold it."

    Lars narration "Its allure is so potent that, for a moment, we're all spellbound by its beauty, our gaze completely ensnared by the radiant gem."

    show claude shocked
    Claude "Before anyone starts their inspection, I promised our dear Captain he’d be the first person to hold it."

    
    Lars default "Thanks, but no thanks, Sir Claude. My instincts are warning me about this artifact, something seems off about it."

    Claude "It wouldn’t hurt to at least hold it in your hand, would it?"

    Lars narration "I direct my gaze towards the opened box, feeling the weight of everyone’s anticipation upon me. Carefully lifting the necklace from its resting place, I note its light size despite the box’s heftiness."

    show rory default
    Rory "Wow! Look at the detailing on this artifact. It’s truly a work of art."

    Sylvian "Indeed, it’s a testament to the skill and craftsmanship of the civilization that created it. But who and when exactly?"

    show claude default
    Claude "We have no idea about its origins yet, besides I could never let go of such a mysterious prize, I need to uncover its secrets all for myself…"

    
    Lars narration "Sir Claude’s expression undergoes a striking transformation, shifting from one of casual curiosity and playful mirth to that of intense obsession. His eyes fixate unwaveringly on the artifact, a glimmer of determination and fervor dancing within them."

    Lars narration "It is no secret that Claude possesses a deep-seated fascination with challenges and trials. Though he seldom shares the reasons behind his unwavering obsession, his eyes betray his inner excitement whenever faced with such an opportunity."

    show claude serious
    Claude "…Ahem, with the help of our prestigious scholar as well of course!"

    Claude "Boss Sylvian, you have quite the reputation in the academic world for your discoveries and inventions. If someone were to understand the potential behind this artifact, it would be none other than you."

    show rory angry
    Rory "Ugh, quit trying to suck up and get close to my Mentor with your scale-rotten face."

    Claude "Weren’t these the very same scales you took for your dolls? Admit it, you just don’t measure up to scale. Specifically, my scales!"

    Claude "I was under the impression that they even made you gain a great show last time with your puppet."

    Claude "Hmm, what was it called again? Boring-ina? Boorish-ina? Banal-ina?"

    Rory "It was BRITTINA, you dagger-mouthed, bark-bellied, algae-breathing gullet on legs—"

    Sylvian "Oh dear…things are starting to get out of hand."

    
    Lars default "Come on guys, it’s time to stop. We’re losing daylight over here."

    
    Lars narration "However, neither side showed any signs of stopping their retort. After all, the first to stop would be the first to lose and their competitive nature wouldn’t allow them this leeway."

    show claude default
    Claude "It’s no wonder that your family legacy is going to die with you. I wouldn’t put myself in the low position of insulting you, though it’s a huge plus if I do."

    
    Lars default "Claude, that’s not like you to—"

    Rory "Look, I think we all have something to bring to this conversation, but you don’t. Especially when all you ever have to add is self-inserted praise and narcissism."

    Lars default "Come on Rory, you don’t really mean that—"

    show sylvian angry
    Sylvian "Both of you, it’s time to stop."

    show claude shocked
    show rory default
    
    Lars narration "Master Sylvian’s commanding voice reverberates through the air, instantly commanding the attention and quieting the bustling atmosphere. Though his usual demeanor is one of calm and collected composure, there are moments when he employs his authoritative voice to instill a sense of tranquility and order among those around him."

    Lars narration "It is a fascinating contrast to witness, as the guild leader within him commands respect and brings about a sense of calm."

    show sylvian default
    Sylvian "Let us embrace empathy’s grace and refrain from jesting, for each soul carries its own unique beauty. Whether it be lizards, foxes, swans, or bulls."

    Rory "Sorry, Mentor. Looks like I’ve overstepped a bit."

    show claude default
    Claude "It’s never a good move to annoy your benefactor. Apologies, Boss."

    Lars narration "As Claude and Rory move away to not bump heads again, I quietly move towards Master Sylvian and whisper in a quiet tone."

    
    Lars default "Thanks for easing off the tension, Master. It gets out of hand when they start bickering."

    
    Lars narration "A shy smile graces Master Sylvian’s lips as he gently rests his hands on my shoulders. The feathers of his swan wings delicately brush against my back, imbuing me with a profound sense of tranquility and ease."

    Sylvian "No problem at all, [Lars]. I might not understand your relationship with Rory well as you both are best friends from a young age. But I would hate to see a rift between us as guild members."

    Sylvian "Your bond with Rory holds a treasure untold. A childhood’s embrace worth more than gold. I wish I could have that kind of equal friendship too—"

    Lars narration "What is he talking about?"

    menu:
        Lars " "

        "Poke further and ask why he’s feeling that way'":
            $ options["S2"]=1
            jump poke_further_and_ask

        "Joke about his statement and steer the conversation":
            $ options["S2"]=2
            jump joke_about_his_statement


label poke_further_and_ask:

    Lars narration "It’s not like Master Sylvian to feel this way, and seeing him slightly melancholic leaves me with a sense of concern."

    
    Lars default "What do you mean, Master. Are you saying we aren’t friends? Did our departure make you lonely?"

    
    Lars narration "He shakes his head a bit, as if trying to clear his thoughts, then regards me with an undefinable look."

    show sylvian default
    Sylvian "…We are friends [Lars], it’s just that as your superior, I don’t have the equal relationship that you have with Rory or Claude—"

    
    Lars default "You know, even though I'm just your junior, you're a cherished friend to me. Of course, I value you first and foremost as our Boss, but I also appreciate how you're always kind to everyone."

    
    Lars narration "Summoning all my courage, I move closer and grasp Master Sylvian’s hands, locking my gaze with his. The initial shock on his face gives way to a warm and genuine smile, a flicker of happiness illuminating his eyes."

    
    Lars default "I'm sorry if it sounds like I'm trying to, you know, suck up to you or ask for something. That's really not my intention at all. It's just— Well, I tend to be pretty straightforward, especially when dealing with stray dragons. I mean, not that I'm saying you're anything like a stray dragon! I guess what I'm trying to say is, ugh...I'm not very good at expressing this stuff."

    Lars default "I get kind of tongue-tied during situations like this."

    show sylvian blush
    Sylvian "Hahahaha! Haha…"

    Sylvian "Ah, what a delight you are [Lars], what would I do without you to brighten up my day? A stray dragon, you say?"

    
    Lars default "Come on, Master, I have a reputation to keep as a dragon pilot. You can't go around telling everyone that I compared my guild master to a stray dragon. I'll never hear the end of it from Rory and Sir Claude."

    
    Lars narration "I shake my head in mock frustration, burying my face in my hands. Master Sylvian always seems to fall for these antics, especially when someone asks for his help or a favor."

    show sylvian default
    Sylvian "It's alright, [Lars], just lift your head and look at me. I'll keep our little secret safe, just between us, alright?"

    Lars narration "His eyes sparkle and a hint of a blush graces his face. It seems our shared secret has drawn us closer together. Perhaps he values this kind of personal connection more."

    Lars narration "Master Sylvian wipes away the tears that have gathered around his eyes."

    Lars narration "As if understanding my need for reassurance, he gently pets me on the head, softly rubbing my ears in the process. Their sensitivity amplifies the gestures, turning them into an intimate connection."

    Sylvian "Don’t worry about me too much, [Lars]. It’s just that…it’s hard to bring out the words that bubble up in your throat sometimes."

    Sylvian "But I do appreciate your efforts, I just hope that I can be the recipient of your more endearing efforts as well."

    jump S_2_End

label joke_about_his_statement:

    
    Lars default "Don’t worry about it, Master!"

    Lars default "I have never seen a person more talented than you in casting spells and dazzling up the atmosphere. I’m sure that if you whip up a quick spell, you’ll have everyone fighting to be your friend."

    show sylvian default
    Sylvian "It’s no use to trick people into being your companions, [Lars]."

    Sylvian "We used to have a lot of rivalry back in the Tower of Magicians. Your comment reminds me of those days where we would try and use every trick up our sleeves to get ahead."

    Sylvian "I wish to never go back to those days if possible. After all, ‘Custodes Sylvae’ is my current solace."

    
    Lars narration "In an instant, his expression shifts into a stoic poker face, a perfect mask that hides whatever emotions he might be harboring, even those underlying traces of melancholy. It's as if he's transported himself back to memories he'd rather not share."

    show lars default
    Lars default "Uhm, Master, I might have misphrased it, but we enjoy your company as fellow guild members. Whether it’s how you wind up sunflower stalks or make the lily of the valley bells chime, it’s your magic that brings a smile to our faces."

    Lars default "I get kind of tongue-tied during situations like this."

    
    Lars narration "My words don’t seem to be reaching him."

label S_2_End:

    
    Lars default "Mast—"

    show sylvian default
    Sylvian "EVERYONE! Steadfast now."

    
    Lars narration "As everyone settles under Sylvian’s gentle yet authoritative command, he takes hold of the artifact, brimming with curiosity. I will save the conversation for later."

    Sylvian "It’s time to get back to business. We need to give our dear dragon a break as well."

    Sylvian "I’d like to observe this a bit more in my lab too."

    Lars narration "Seems like Master is wary of the significance and potential of this mysterious item."

    Sylvian "A curious trinket, its secrets untold. An odd accessory with immense power. To shape time’s fragments, to weave its essence."

    hide all
    pause 2.0
    show Normal Necklace
    Sylvian "It eerily resembles an artifact that I had previously seen in the academic domain. A one-of-a-kind necklace with a similar gemstone belonging to a family of dragons with our very own half-human, half-animal traits as descendants."

    Sylvian "I haven’t heard of them in quite some time, and though the color of its gem contrasts the descriptions I’ve heard and read, the artistry and written etchings are quite similar. it’s something worth researching."

    Sylvian "Speaking of which, how much did you exchange for it, Claude? We need to see if the funds from Rory’s recent puppet show will be able to cover the costs."

    Claude "A merchant only exchanges what they are willing to offer. However, the infamous Claude can overcome any trial, as long as he wishes for it, of course."

    Claude "I received this curious box free of charge. The seller was begging me to take it. Ah, the misery of knowing the world will fit into the palm of my hand as long as I aim for it..."

    Claude "Ah, the misery of knowing the world will fit into the palm of my hand as long as I aim for it."

    Lars narration "Rory’s eyes widen to an almost comical extent, as if they’re on the verge of rolling out of their sockets."

    Lars narration "Master Sylvian merely closes his eyes, whether he’s focusing on what Sir Claude is saying or mentally preparing himself for any upcoming conflicts, I can’t tell."

    hide Normal Necklace
    show rory default
    show claude default
    show sylvian default
    Rory "Narcissus left a voicemail, saying he's issuing the world a mental refund for the surplus of self-absorption you're currently exuding."

    Claude "Getting real creative with the insults, aren’t you?"

    show claude serious
    Rory "I have never meant anything more in all my bull years."

    Claude "That explains why you’re such a bullshitting—"

    Rory "Come to think about it, Mentor, can I take this artifact for a spin before you put it in your lab?"

    Rory "This design is perfect for one of my dolls. I can create a new puppet based on these intricate patterns and symbols. It will be a showstopper!"

    show claude shocked
    Claude "But that’s absurd, who knows when your puppet project is going to finish?"

    
    Lars default "That’s a great idea! We could even visit your puppet show stall and see what magic you will create. It’s been some time since I last played with the kids as well."

    Sylvian "If you feel inspired by this artifact, then by all means, go ahead."

    Claude "Not you too, Boss…"

    show claude default
    Claude "Captain, how about you wear the necklace for now instead of little Rory? It’s color suits your fur, after all."

    show rory angry
    Rory "Not with the little Rory comment again—"

    Claude "It reminds of the red string of fate, though placing your faith in such notions is for those incapable of steering their own lives—"

    
    show rory default
    Lars narration "These confession jokes are getting really out of hand."

    Lars narration "I take this moment to put on the necklace, the gemstone’s ruby color captures my attention and I marvel at the curious glow that emits from it."

    hide all
    show Shining Necklace
    Lars narration "Almost as if…it’s shining or signaling something."

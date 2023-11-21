label part_1:

#***** ERROR ***** Command not recognized
#Notes
#***** ERROR ***** Command not recognized
#[Start playing track 1-Intro. This track  starts playing from the OP Screen. However, during the BG transition, it can go mute and start again]
#***** ERROR ***** Command not recognized
#[starting with a pan view]
#***** ERROR ***** Command not recognized
#[scene bg BG 1]
#[with fade]
#***** ERROR ***** Command not recognized
#[lars enters]
    Lars default "‘Discere, cogitare, agere — the triad of wisdom.’"

    Lars default "‘Learning enriches the mind, and thinking sharpens it, but it is through action that we truly manifest our knowledge and shape our reality.’"

#***** ERROR ***** Command not recognized
#[lars exits]
    Lars narration "One would think that a merchant guild wouldn’t bother creating such a philosophical motto and instead advertise one plus one dragon ship seats every holiday season."

    Lars narration "We could even offer complementary earthling-made meals by the human chefs who were transported to our realm upon their death."

    Lars narration "But then again, we wouldn’t be embarking on artifact hunts and historical expeditions if the sole purpose of our guild, ‘Custodes Sylvae’, was commerce."

#***** ERROR ***** Command not recognized
#[Claude enters a bit annoyed -not default-]
    "Unknown" "Who on Divonia is mumbling this loud to themselves early in the morning?"

#***** ERROR ***** Command not recognized
#[finishing pan view]
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


    show claude
    Claude "Ah, my dearest Captain [Lars]!"

    Claude "How could I ever get that nightingale-like voice of yours out of my head? It’s almost like my personal alarm clock!"

    Lars narration "Up for a challenge this early? Typical."

    Lars default "I’m glad you appreciate my vocal talents. But you know, I can’t take all the credit."

    Lars default "You’re the one who inspires me to mumble so loudly during our journeys."

    Lars default "It’s the only way I drown out your snoring."

    Claude "You always find a way to turn the tables, don't you?"

    Claude "And my snoring?"

    Claude "Hah! I can capture your attention through other means, if I choose to."

    jump C_1_End

label resist_the_urge_to_surprise_him:

    Lars narration "It’s best that I focus on piloting our dragon first. Otherwise, I’ll never hear the end of it."

    Lars default "Good morning to you too, Sir Claude."

    Claude "What a boring reaction. I expected more spunk from you…"

    Lars default "Nevermind then. Hmph!"

label C_1_End:

    Lars narration "It’s truly a wonder how he managed to stay asleep throughout our entire journey, considering the lack of proper seat arrangements or resting areas on our new dragon ship."

    Lars narration "However, Sir Claude has always been notorious for his resourcefulness in such moments owing to his history of travels and adventurous ordeals despite his comfortable upbringings."

    Lars default "I will return to my duties, then, Si—"

    Claude "Didn’t I already tell you to drop the ‘Sir’ for the umpteenth time, Captain?"

    Lars default "Do we have to go over this cliche back and forth as well?"

    Lars default "I promised I’d do it if you stopped insisting on “Captain this” and “Captain that”."

    Claude "It makes us seem more of an adventurous pair, though, don’t you think?"

    Lars narration "Indeed, and there is a good reason for that."

    Lars narration "My knack in piloting and his remarkable merchant abilities just clicked. Whether it was going on expeditions, dealing in trades, or connecting with the quirky passengers we often had..."

#***** ERROR ***** Command not recognized
#[MC] (narration)  We always made an efficient team. Maybe even the best among all the guild members.
    Lars narration "Well…at least, if you ignore that there are only four of us."

    Claude "Now that I think about it, what were you talking to yourself about?"

    Claude "Confiding trade-secrets to our lovely dragon, Spotsy? Or even a secret confession for me—"

    Lars default "Bad at naming as always, Sir Claude. Not to mention, the confession jokes won’t work if you keep repeating them over and over again."

    Claude "Who knows, maybe one day, I'll surprise you with a confession that will leave you speechless."

    Lars narration "I reach out, my hand confidently caressing the head of our newest guild member who I hope I’m taking good care of."

    Lars narration "Her eyes meet mine in and in a show of trust, her relaxed scale’s part open, revealing mesmerizing azure flames simmering underneath."

    Claude "Don’t let your attention wander off too much, Captain."

    Lars narration "Sir Claude's voice carries a subtle touch of displeasure as he observes me caressing Spotsy's head."

    Lars narration "Maybe the uncomfortable seating arrangement is getting to him—He had always been known to grow a tad irritable when he felt he wasn't receiving the attention or results he desired."

    Claude "No need to caress her like that. She’s just a glorified lizard with fiery breath."

    Lars narration "As if to express her annoyance, Spotsy lets out a dark, puffy plume of smoke from her nostrils. A low rumbling note resonates from her throat, a clear indication of her irritation."

    Lars default "You're starting to irritate her, Sir Claude, maybe you should—"

    Claude "She doesn’t like it, hmm…That just makes me want to do it even more though."

    Claude "Not to mention, I wouldn’t want to be that poor passenger who accidentally dies early and transports to the Earth realm just because you were adoring our newest ship. There have been too many events like that happening these days."

    Lars narration "His sudden change of topic leaves me slightly bewildered. I withdraw my hand from Spotsy's head, and she shakes her head as if still searching for my comforting touch."

#***** ERROR ***** Command not recognized
#[MC] (Narration) In contrast, a mischievous grin adorns Sir Claude's face. Why would he be happy about it? Maybe the problem wasn’t the seats after all…
    Lars default "The numbers of transported humans have certainly increased quite a bit these days."

    Lars default "Even still, they are a precious rarity. In all my years of flying travelers across the lands of Divonia, I have only ever met a handful of them."

    Claude "Not many would want to undertake the journey of transitioning to a new realm they know nothing about, after all."

    Lars default "I understand that, but they always fascinate me with the tales of their past life."

    Lars default "All our guild members were born and raised here, so I don’t have the chance to closely work with one of those travelers either."

    Claude "Tsk, tsk, already thinking of replacing me with someone else, are you, Captain?"

    Lars default "You said it yourself before, one has to admire their bravery, since descending into Divonia is a grand leap of faith into the unknown."

    Lars narration "He chuckles. Claude is always the most spirited one when faced with adversity and adventure. Must feel great."

    Claude "Ah, how gladly I would take their place if I could…"

    Claude "Life can get pretty boring when you have everything you need in the palm of your hand."

    Lars default "Always trying to satisfy your thirst for adventure, eh?"

    Lars narration "I could hardly recall a day when Sir Claude didn’t turn a simple task into a grand quest. He always was, and still is, on the lookout for opportunities to embark on new escapades."

    Claude "I’d advise you to concentrate on steering for now, Captain, before you get even more distracted. I feel your gaze burning my scales."

    Lars default "Oh, don’t flatter yourself, your scales are nothing compared to Spotsy’s."

    Lars narration "My playful grin is met with crossed arms and a sulky stare. I suppose I should stop the teasing, he takes too much pride in his appearance."

    Claude "Well, I suppose it's my mistake for attempting to catch the attention of a certain dragon-obsessed pilot. What will become of my grandiose confession now?"

    Lars default "Don’t be so hard on yourself, Claude. You know I appreciate you for more than your appearance even if I rank you below Spotsy. Stopping the confession jokes could help though—"

    Claude "There is no no need for empty flattering. I already get enough from my family name."

    Lars default "Why are you referring to your own last name as—"

    Claude "However, you need to make sure to take care of her well since I did make quite the effort for her exchange."

    Lars narration "A quick change of topic per usual. Sir Claude has the habit of doing so whenever his family is mentioned. I used to wonder if he was doing so to maintain his privacy as a renowned golden spoon but despite the many years we spent together as partners, the sentiment never changed."

    Lars narration "If memory serves me right, our negotiator unloaded all his prized possessions onto us the moment he caught wind of the ‘Dupont’ surname. I don’t think that is an “exchange”."

    Lars narration "Though, I suppose having an outrageously high-class family name like Claude makes one’s trade prone to that."

    Lars default "I thought I saw you arguing about that one specific artifact, though?"

    Lars default "They were so adamant to wash their hands of it they wanted to add it on top of everything else.."

    Claude "I’m not one to accept gifts without scrutiny. But there was something about that artifact—"

    Lars default "You mean artifact box."

    Claude "—that piqued my interest."

    Lars default "What if it turns out to be hazardous or a curse? Scrutiny would have been welcomed."

    Claude "I had plans beforehand of adding some more excitement to my list, so I might as well embrace the opportunity."

    Lars default "Right, because who wouldn’t jump at the chance to receive an artifact with no known origins, suddenly materializing out of thin air, and with no apparent acquisition date?"

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

    Claude "I am baffled, dumbfounded, bamboozled, shocked, bewildered, and confuzzled to the highest degree."

    Lars default "You’re irreplaceable to me, and your merchant skills are unmatched—"

    Claude "Hmph, why should I trust your word? You should know that actions speak louder after all."

    Lars default "Then…How should I show it to you?"

    Claude "There’s something that I really want but with our relationship as is, you won’t be able to give it to me."

    Lars narration "My fur prickles with anticipation. I can sense my ears perked up, betraying my keen interest in his next words and what he could possibly want from me."

    Lars default "A gift? For you? But you already have everything you need."

    Lars default "Your family has your pockets lined with all the gold and treasures imaginable too, so I can’t see what you’d want."

    Claude "I’ll tell you more about it in due time."

    jump C_2_End
    return

label continue_teasing_him_even_more:

    Lars default "The infamous Claude Dupont, not checking the items he negotiates for?"

    Claude "He was acting suspicious. But even then, I could not resist indulging my curiosity, having seen the artifact or not."

    Claude "Also, you should know better than to recklessly use the ‘Dupont’ last name, [Lars]."

    Lars default "Weren’t you going to continue calling me ‘Captain’ as well?"

    Lars narration "He leans close and his fingertips gently brush against my cheek, leaving a trail of warmth in their wake, as his golden eyes lock onto mine with unwavering intensity."

    Lars narration "His voice deepens, resonating with a seductive allure - lips tantalizingly close to my ear. He uses them to send shivers down my spine with a whisper."

    Claude "See? I used your name, so you have to call me by mine too...without the titles."

    Claude "I prefer it when you say my name after all. It’s one of the tiny joys of my life."

    Lars narration "The sudden remark takes me by surprise, even though it’s not the first time I’ve heard Sir Claude make such a comment. After all, he possesses a captivatingly flirtatious nature, effortlessly weaving his charm into every interaction."

    Lars narration "However, a part of me hesitates, fearing that surrendering to his banter may lead to my own demise. And so I find myself stumbling over my words, caught in a tangled mess of stuttering syllables."

    Lars default "W-w-what are you saying all of a sudden?! Did you lose your mind?"

    Claude "Awe, is our captain getting shy all of a sudden? Did you know your ears get red when you're embarrassed?"

    Lars narration "With little time to question his truthfulness, I instinctively place my hands on my ears, hoping to shield any trace of vulnerability that might betray my reaction to his words."

    Lars default "I am a dragon pilot, an unwavering force soaring through the skies."

    Claude "Yes, indeed. That much is observable from our current position."

    Lars default "My years of experience have honed my resilience and steeled my resolve. I cannot allow myself to be easily affected by the whimsical words of Sir Claude, no matter how charismatic he may be."

    Claude "Awe, did I get under your skin, Captain? Also, when did we switch to third-person commentary?"

    Lars narration "Sir Claude remains unfazed by my momentary embarrassment except for a triumphant smile."

    Lars default "After all, he’s only joking to gauge my reaction—"

    Claude "Haha look at you! Navigating the skies like a pro with those sharp fox eyes, but missing the obvious right in front of you."

    Lars default "Pardon?"

label C_2_End:

    Claude "Let’s continue this conversation late, shall we?"

    Claude "Our dearest Guild Master is signaling our landing spot."

    Lars narration "I glance downward, and our destination near the sea comes into view. Like an artist painting delicate strokes on a canvas, Master Sylvian has already lined up the location with an array of enchanting flowers."

    Lars narration "Each bloom carefully chosen to mark our path with a vibrant array of sunflowers and roses. Their vivid colors stand out, captivating the eye and creating a striking contrast against the backdrop of the serene oceanic landscape."

    Lars narration "The gentle breeze carries the sweet fragrance of the flowers, adding to the enchanting ambiance."

    Lars default "Ah, it’s a shame we arrived so early. I was hoping to learn something new."

    Lars default "But, most importantly, I have to reward Spotsy well when we get back."

    Claude "I’d be inclined to say that you didn’t manage to tap into our dragon’s full potential captain. Owning up to how I stole your attention for more than half, or better yet, the entire ride."

    Claude "However, since you managed to get us here without any dangerous maneuvers, I’ll allow you to be the first to touch our newest artifact. I tend to appreciate and reward my companions well, especially if they’re my lover—"

    Lars default "I’d argue that being the first person to touch a suspicious artifact is the last thing I’d prefer to do."

    Claude "It’s the first time it’s made its way to our side of the realm, hence the occasion is quite momentous."

    Claude "You could say the thrill is irresistible."

    Lars narration "He locks eyes with me, and I can’t help feeling a tad self—conscious under the weight of his declaration, whether it was actually meant for me or not."

    Claude "And let’s not forget, it’s the first person who gets the real taste of discovery, not the second or anyone who follows."

    Claude "If you don’t seize this moment now, who knows when you’ll get another chance to dive into it, learn more, and delight your passengers with captivating stories?"

    Lars default "Fine! Now let me focus before any of us plummet to their death."

#***** ERROR ***** Command not recognized
#[show bg BG 2]
#[with fade]
#***** ERROR ***** Command not recognized
#[start playing track 2-field of flowers]
#***** ERROR ***** Command not recognized
#[starting with a pan view]
    Lars narration "As the sole passengers aboard the dragon ship, guiding Spotsy in her safe descent was a seamless task. The proximity to the water offered a perfect opportunity for her to release some pent-up energy too."

    Lars narration "Hopefully, she’s not too tired from the journey. I’d hate to burn her out from the get-go and leave a negative first impression behind."

    Lars narration "Once we disembark, our attention turns to the tall and slender magician who makes his way towards us."

#***** ERROR ***** Command not recognized
#[Sylvian enters smiling]
    Lars narration "A warm smile graces his lips as his obsidian wings flutter gracefully."

    Lars narration "With a hushed incantation, the brim of his hat blossoms into a vibrant tapestry of roses and sunflowers, their delicate petals unfurling in a mesmerizing display. The air is instantly infused with their soft fragrance, which mingles with a refreshment spell."

    "Unknown" "Welcome back, dear members of ‘Custodes Sylvae’. I’m happy to see that you both landed safely."

    "Unknown" "[Lars], your piloting was truly magnificent as always. It’s a sight that I’m honored to witness every time."

    Claude "It wouldn’t be a warm welcome if Master Sylvian weren’t here to receive us."

    Lars default "Thank you, Master. I wish you could have joined us on the ride too. Sir Claude here almost caused us to plummet to our doom...multiple times I must say."

    Claude "Eh, I did promise to reward you later, didn’t I? Drum roll please ~"

#***** ERROR ***** Command not recognized
#[Drum Roll SFX Starts]
    Lars narration "With a flourish of his hands, Sir Claude performs a series of gestures that mimic a drumroll. Tension fills the air as the anticipation builds up, drawing everyone’s attention."

    Lars narration "Then, in a dramatic display, he spreads his arms wide, showcasing a grand reveal..."

#***** ERROR ***** Command not recognized
#[Drum Roll SFX Ends]
    Lars narration "…which is nothing?"

    Claude "Haha, I seem to have left it on the ship."

    Lars default "Should I go get it, then?"

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

    Sylvian "I also wanted to spend some time with you…"

    Sylvian "But uhm, never mind, I suggested it in the first place after all."

    Claude "Awe, you choose to stay with me instead of Boss Sylvian, I’m touched, Captain."

    Claude "I’ll have to give you a special reward later in private."

    Lars narration "His hands gently encircle my waist, drawing me closer to him as he whispers the last part of his sentence. As his eyes, akin to pools of molten sunlight, meet mine, a mischievous spark dances within them. While I might usually dismiss this as him being more touchy-feely than usual, his last comment makes me think otherwise."

    Lars narration "Yet, beneath that playfulness, there lurked a subtle undertone of competition, evident in the way he regarded Master Sylvian. It was as if they shared a friendly rivalry, each vying to outdo the other in their unique way."

    Sylvian "Ahem! Not to interrupt but I’m sure Rory will arrive soon, so it’s best to prepare yourself, [Lars]."

    Sylvian "As for you, Claude, remember what I said about teasing him too much?"

    Claude "Before worrying about Captain over here, you should head on to where our new dragon is resting, Boss."

    Claude "We wouldn’t want her to accidentally drop our cargo to the depths of the sea."

    Lars narration "As Master Sylvian takes flight, his swan—like wings seem to catch every ray of sunlight, causing them to shimmer and gleam like ethereal jewels. The sight is truly breathtaking, and I find myself in awe of the beauty before me."

    "Unknown" "Clauuuuuuuuuuuuudy~ [Word shake, is there also a way to make the individual letters appear more slowly?]"

    Claude "Roryyyyyyyyyyyyy~ [Word shake, is there also a way to make the individual letters appear more slowly?]"

    Lars narration "A figure emerges from where Master Sylvian stood just a few seconds ago, and to my pleasant surprise, it is none other than Rory, my childhood best friend."


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

    Rory "It’s just Rory! Call me a midget again, and MORE of your receding hairline will adorn puppet Alex!"

    Claude "Now, now, I would have to say these finely braided silver strands that I’ve so kindly donated to you are what’s bringing half the revenue for your puppet shows, aren’t they little Rory?"

    Rory "You cheap lizard!"

    Rory "You really have the gall to talk to me like that, when all your travel funds are conveniently collected from my shows?!"

    Rory "I will compensate you by throwing Claude Junior into the sea, or have he meet my nifty scissors. Your call."

    Claude "I'm sure the hydro dragons would be delighted to embrace my  presence amongst them."

    Rory "You could put your merchant skills to use there, too. Ten more seconds to live for a platter of rotten lizard meat."

    Sylvian "I’m back with the cargo!"

    Lars narration "Thankfully, Master Sylvian swiftly intervenes, diffusing the tension with his timely return."

    Lars narration "In his grasp, he holds a grand and ornate box, its intricate design hinting at the secrets it conceals within."

    Lars narration "The weight of anticipation fills the air as all eyes turn to the box, momentarily diverting attention from the conflict."

    jump CS_1_End

label tell_Claude_grab_cargo:

    Lars default "Sir Claude, can you bring the artifact yourself? I’d like to spend some time with Master Sylvian."

    Claude "I’m shocked, Captain. Choosing Boss Sylvian over me?! I wouldn’t have imagined."

    Sylvian "I am grateful that you wish to share your time with me, [Lars], even if you’re tired from your journey."

    Sylvian "Rory will arrive soon as well, so we all can spend some time together."

    Lars narration "Master Sylvian gently touches the brim of his hat and a magnificent bouquet blooms forth. Sunflowers rise proudly, while lavender blossoms intertwine. Brilliant clusters of marigolds sprout forth as well."

    Lars narration "I remember that his hat was one of his personal crafts, a magical creation that bloomed flowers according to his mood. It’s unfortunate that I’m not well—versed in flower languages; otherwise, I would be able to decipher the heartfelt messages he wishes to convey through these enchanting floral gifts."

    Lars narration "Nonetheless, I can’t help but feel treasured whenever he gives me gifts. Perhaps it’s due to a reaction I had once, or maybe he simply cherishes all moments we share."

    Lars narration "After all, I’ve noticed that he hasn’t given this kind of gift to anyone else, and the thought warms my heart for some reason…"

    Claude "Quite the showmanship, Boss. Though I wonder if Captain over here got the message in your subtle gesture."

    Lars narration "Master Sylvian presents me with the bouquet, throwing a smile at Claude."

    Sylvian "It might be best for you to take care of your task, Claude. We’re still not sure of the origins of the artifact you brought and there needs to be a level of caution involved as well."

    Lars default "That’s exactly what I said!"

    Lars narration "As Sir Claude takes his leave, his silver lizard tail gracefully sways behind him, reminiscent of the rhythmic movements of the sea. His scales, resembling those of the majestic dragons I often encounter in my journeys, captivate my gaze with their intricate detailing, despite their diminutive size."

    Lars narration "However, before I can fully immerse myself in the enchanting display, a sudden voice slices through the air with an excited tone."

    Rory "[Lars]!"

    Lars default "Rory, it’s so good to see you again!"

    Rory "You too! And good to see that slithering, slimy tail going about."

    Lars narration "The figure that emerges from where Sir Claude stood just a few seconds ago, is none other than Rory, my childhood best friend. True to her lineage as a bull descendent, Rory possesses a fiery temperament and is quick to charge at those who annoy her."

    Lars narration "Under Master Sylvian’s guidance, she apprenticed as the guild’s head of finance, helping us gather funds for every mission through her puppet shows."

    Rory "Mentor, I I was preparing my puppets for the afternoon show at the market square. I feel like something is missing but I don’t know what exactly…"

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

    Rory "Come on, [Lars]. No shorty jokes. A certain someone spews enough of them already."

    Lars default "Alright, alright. I’ll make it up to you by helping you out for the show."

    Rory "Yay~ Thank you!"

    Claude "I have arrived with our mystery artifact."

    Lars narration "Speaking of the devil, Sir Claude makes his entrance with the ornate box cradled in his arms. His eyes glimmer with a mixture of anticipation and excitement as he gazes at the artifact."

    Lars narration "However, rather than keeping it for himself, he extends the box towards me."

label CS_1_End:

    Lars narration "As the  heavy weight of the artifact transfers to my hands, I feel a sense of responsibility settle in."

if options["CS1"]==1:

    Lars default "I think I can take it from here, Master."

    Sylvian "Carrying such things after your tiring journey might affect your health, [Lars]."

    Sylvian "But thank you for worrying about me…I really appreciate it."



else:

    Lars default "I think I can take it from here, Sir Claude."

    Claude "Anxious for the reveal. Aren’t you?"

    Claude "Don’t worry, I’m not a fan of breaking promises. Especially, for one I made with you."

label if_op_cs_1_end:

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
#[vertigo effect -sample from drive-]
    Sylvian "Are you feeling better now? I could conjure up some stalks to help with the box as well—"

    Lars default "It’s okay Master, I need to get in my daily dose of exercise too. I don’t want you to think that I’m too weak for one box! More than that, what would our passengers think if their pilot wasn’t able to pick up their luggage or equipment. My parents wouldn’t let me live this down if they ever heard such rumors since they raised me to give my all to take care of those around me considering— [Speeding up the rambling text A LOT and making [Lars] jump up and down / I want it to show that he’s being hyperactive of sorts]"

    Sylvian "Oh, my..."

    Lars default "Haha, nothing to worry about, Master! But did you know, Master? I was researching Spotsy and as part of the Spotted Azureflame species, the intense temperature generated through their breathing process can cause the air pockets under their scales to bubble and expand. Their azure distortions aren’t for mere show either, Rory mentioned that certain blacksmiths hire them for their forging practices since the heat produced is exceptionally hotter than regular flames, making it a valuable resource for crafting extraordinary weapons and armor— [Speeding up the rambling text A LOT and making [Lars] jump up and down / I want it to show that he’s being hyperactive of sorts]"

    Sylvian "As much as I enjoy hearing you talk—"

    Claude "More like ramble."

    Sylvian "—about the dragons which you treasure, we need to calm you down a little. Let’s use that breathing technique that I taught you last time. You remember, [Lars]?"

    Lars narration "He takes my hand into his own, slowly tracing circles on my palm. His touch feels warm, and there’s a slight hint of perspiration, as if he’s nervous about holding it."

    Sylvian "Breathe for 3 seconds…Hold it for 6…Now release it for 9 seconds…"

#***** ERROR ***** Command not recognized
#[For this breathing sequence, let’s make the auto mode slow down according to the seconds and the next part of the text appears after the previous sequence is completed. Ergo, ‘Breathe for 3 seconds’ comes up and in auto mode, it has to wait 3 seconds before the ‘Hold it for 6’ comes up.]
    Lars narration "Obediently, I follow Master’s instructions, allowing my breath to gradually slow down. With each measured inhale and exhale, a sense of calm envelops me, grounding me in the present moment."

    Sylvian "No one is going to think those things of you, [Lars]."

    Sylvian "If I were a dragon, I wouldn't want any other handler than you to take care of me. I've seen how you praise their efforts and spoil them senselessly."

    Sylvian "I mean, who wouldn't want to be praised by someone they admire...I mean, I do admire you, and I hope that, but ughh..."

    Lars narration "Master Sylvian suddenly takes hold of the tips of my fingers, as if he’s shying away from holding my hand fully."

    Lars narration "His gesture is tender and filled with a subtle intimacy. Yet, it also carries an air of vulnerability, as if he’s unsure of how to express his emotions openly."

    Claude "So, what I gather is that Master Sylvian wants to have [Lars] ride him—"

    Lars narration "A chuckle escapes me at Sir Claude's jest. But in the blink of an eye, Master Sylvian's demeanor shifts. He turns his head away quickly, almost as if he's trying to conceal his reaction. Yet, even from behind, I catch a glimpse of his ears reddening slightly."

    Claude "My my, are you feeling hot all of a sudden, Boss? It must be because of all the cloaks and layers you’re wearing."

    Lars default "He's joking, Master Sylvian. Just forget about him. I appreciate the energizing spell, even if it didn't work out like we thought."

#***** ERROR ***** character not recognized
    Slyvian "Definitely not. I'll have to research ways to lower their dose later on."

    Lars default "And not just that... I, um, wanted to thank you for helping me stay calm and for the motivational words. It's not often that someone praises my dragon skills. I thought no one really cared."

    Sylvian "OF COURSE I DO!"

    Lars narration "His outburst catches me by surprise because I rarely see Master Sylvian raise his voice."

    Sylvian "I don't think it's the right place to talk about this, but know that I always keep you in my mind."

    Lars default "Haha, I know, Master. You're not just a boss to me; you're a friend as well."

    Sylvian "Ah, what a joy to be  just a friend to you…"

    Sylvian "Maybe my own lack of directness caused this in the first place."

    Lars default "Pardon?"

    Sylvian "N-N-Nothing, uhm, yeah, nothing to concern yourself with. Let’s analyze the artifact now, s-shall we?"

    jump S_1_End

label reject_his_offer:

    Lars default "Thank you for the offer, Master. But it’s nothing I can’t shake off."

    Lars narration "A dejected look embraces his face and though I feel guilty about his kind proposal, I stand firm with my decision. Yet, just as the tendrils of awkwardness begin to snake through the air, Sir Claude deftly steps in."

label S_1_End:

    Claude "Ehem, I think we’re better off witnessing the artifact before the evening sets in and little Rory decides to pull something off for her puppets again."

    Claude "I can see fumes exiting her head as we speak. Oh look! I think they got even bigger."

    Rory "Ugh, I can’t deal with this again."

    Lars default "Alright everyone, settle down. What should we do now, Master?"

    Sylvian "Let me cast a safety spell over the box first, you can never be sure if there are any hidden traps inside."

    Lars narration "After a few seconds of sparking light and anticipation, the box remains unresponsive, devoid of any notable reactions."

    Sylvian "No traps or enchantments detected. It seems we’re in the clear. Let’s unveil the treasure within."

    Lars narration "As I gingerly lift the lid of the ornate box, a breathtaking sight unfolds before me. Resting on a bed of plush velvet is a long necklace, the simplicity of its leather band belying the allure of its design. However, it's the centerpiece that commands attention—a dazzling red gem, radiating a mesmerizing ruby hue that captures the gaze of all who behold it."

    Lars narration "Its allure is so potent that, for a moment, we're all spellbound by its beauty, our gaze completely ensnared by the radiant gem."

    Claude "Before anyone starts their inspection, I promised our dear Captain he’d be the first person to hold it."

    Lars default "Thanks, but no thanks, Sir Claude. My instincts are warning me about this artifact, something seems off about it."

    Claude "It wouldn’t hurt to at least hold it in your hand, would it?"

    Lars narration "I direct my gaze towards the opened box, feeling the weight of everyone’s anticipation upon me. Carefully lifting the necklace from its resting place, I note its light size despite the box’s heftiness."

    Rory "Wow! Look at the detailing on this artifact. It’s truly a work of art."

    Sylvian "Indeed, it’s a testament to the skill and craftsmanship of the civilization that created it. But who and when exactly?"

    Claude "We have no idea about its origins yet, besides I could never let go of such a mysterious prize, I need to uncover its secrets all for myself…"

    Lars narration "Sir Claude’s expression undergoes a striking transformation, shifting from one of casual curiosity and playful mirth to that of intense obsession. His eyes fixate unwaveringly on the artifact, a glimmer of determination and fervor dancing within them."

    Lars narration "It is no secret that Claude possesses a deep-seated fascination with challenges and trials. Though he seldom shares the reasons behind his unwavering obsession, his eyes betray his inner excitement whenever faced with such an opportunity."

    Claude "…Ahem, with the help of our prestigious scholar as well of course!"

    Claude "Boss Sylvian, you have quite the reputation in the academic world for your discoveries and inventions. If someone were to understand the potential behind this artifact, it would be none other than you."

    Rory "Ugh, quit trying to suck up and get close to my Mentor with your scale-rotten face."

    Claude "Weren’t these the very same scales you took for your dolls? Admit it, you just don’t measure up to scale. Specifically, my scales!"

    Claude "I was under the impression that they even made you gain a great show last time with your puppet."

    Claude "Hmm, what was it called again? Boring-ina? Boorish-ina? Banal-ina? —"

    Rory "It was BRITTINA, you dagger-mouthed, bark-bellied, algae-breathing gullet on legs—"

    Sylvian "Oh dear…things are starting to get out of hand."

    Lars default "Come on guys, it’s time to stop. We’re losing daylight over here."

    Lars narration "However, neither side showed any signs of stopping their retort. After all, the first to stop would be the first to lose and their competitive nature wouldn’t allow them this leeway."

    Claude "It’s no wonder that your family legacy is going to die with you. I wouldn’t put myself in the low position of insulting you, though it’s a huge plus if I do."

    Lars default "Claude, that’s not like you to—"

    Rory "Look, I think we all have something to bring to this conversation, but you don’t. Especially when all you ever have to add is self-inserted praise and narcissism."

    Lars default "Come on Rory, you don’t really mean that—"

    Sylvian "Both of you, it’s time to stop."

    Lars narration "Master Sylvian’s commanding voice reverberates through the air, instantly commanding the attention and quieting the bustling atmosphere. Though his usual demeanor is one of calm and collected composure, there are moments when he employs his authoritative voice to instill a sense of tranquility and order among those around him."

    Lars narration "It is a fascinating contrast to witness, as the guild leader within him commands respect and brings about a sense of calm."

    Sylvian "Let us embrace empathy’s grace and refrain from jesting, for each soul carries its own unique beauty. Whether it be lizards, foxes, swans, or bulls."

    Rory "Sorry, Mentor. Looks like I’ve overstepped a bit."

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

    Sylvian "…We are friends [Lars], it’s just that as your superior, I don’t have the equal relationship that you have with Rory or Claude—"

    Lars default "You know, even though I'm just your junior, you're a cherished friend to me. Of course, I value you first and foremost as our boss, but I also appreciate how you're always kind to everyone."

    Lars narration "Summoning all my courage, I move closer and grasp Master Sylvian’s hands, locking my gaze with his. The initial shock on his face gives way to a warm and genuine smile, a flicker of happiness illuminating his eyes."

    Lars default "I'm sorry if it sounds like I'm trying to, you know, suck up to you or ask for something. That's really not my intention at all. It's just — Well, I tend to be pretty straightforward, especially when dealing with stray dragons. I mean, not that I'm saying you're anything like a stray dragon! I guess what I'm trying to say is, ugh...I'm not very good at expressing this stuff. [Speeding up the rambling text A LOT and making [Lars] jump up and down / I want it to show that he’s being hyperactive of sorts]"

    Lars default "I get kind of tongue—tied during situations like this."

    Sylvian "Hahahaha! Haha…"

    Sylvian "Ah, what a delight you are [Lars], what would I do without you to brighten up my day? A stray dragon, you say?"

    Lars default "Come on, Master, I have a reputation to keep as a dragon pilot. You can't go around telling everyone that I compared my guild master to a stray dragon. I'll never hear the end of it from Rory and Sir Claude."

    Lars narration "I shake my head in mock frustration, burying my face in my hands. Master Sylvian always seems to fall for these antics, especially when someone asks for his help or a favor."

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

    Sylvian "It’s no use to trick people into being your companions, [Lars]."

    Sylvian "We used to have a lot of rivalry back in the Tower of Magicians. Your comment reminds me of those days where we would try and use every trick up our sleeves to get ahead."

    Sylvian "I wish to never go back to those days if possible. After all, ‘Custodes Sylvae’ is my current solace."

    Lars narration "In an instant, his expression shifts into a stoic poker face, a perfect mask that hides whatever emotions he might be harboring, even those underlying traces of melancholy. It's as if he's transported himself back to memories he'd rather not share."

    Lars default "Uhm, Master, I might have misphrased it, but we enjoy your company as fellow guild members. Whether it’s how you wind up sunflower stalks or make the lily of the valley bells chime, it’s your magic that brings a smile to our faces."

    Lars default "I get kind of tongue-tied during situations like this."

    Lars narration "My words don’t seem to be reaching him."

label S_2_End:

    Lars default "Mast—"

    Sylvian "EVERYONE! Steadfast now."

    Lars narration "As everyone settles under Sylvian’s gentle yet authoritative command, he takes hold of the artifact, brimming with curiosity. I will save the conversation for later."

    Sylvian "It’s time to get back to business. We need to give our dear dragon a break as well."

    Sylvian "I’d like to observe this a bit more in my lab too."

    Lars narration "Seems like Master is wary of the significance and potential of this mysterious item."

    Sylvian "A curious trinket, its secrets untold. An odd accessory with immense power. To shape time’s fragments, to weave its essence."

    Sylvian "It eerily resembles an artifact that I had previously seen in the academic domain. A one-of-a-kind necklace with a similar gemstone belonging to a family of dragons with our very own half-human, half-animal traits as descendants."

    Sylvian "I haven’t heard of them in quite some time, and though the color of its gem contrasts the descriptions I’ve heard and read, the artistry and written etchings are quite similar. it’s something worth researching."

    Sylvian "Speaking of which, how much did you exchange for it, Claude? We need to see if the funds from Rory’s recent puppet show will be able to cover the costs."

    Claude "A merchant only exchanges what they are willing to offer. However, the infamous Claude can overcome any trial, as long as he wishes for it, of course."

    Claude "I received this curious box free of charge. The seller was begging me to take it. Ah, the misery of knowing the world will fit into the palm of my hand as long as I aim for it..."

    Claude "Ah, the misery of knowing the world will fit into the palm of my hand as long as I aim for it."

    Lars narration "Rory’s eyes widen to an almost comical extent, as if they’re on the verge of rolling out of their sockets."

    Lars narration "Master Sylvian merely closes his eyes, whether he’s focusing on what Sir Claude is saying or mentally preparing himself for any upcoming conflicts, I can’t tell."

    Rory "Narcissus left a voicemail, saying he's issuing the world a mental refund for the surplus of self-absorption you're currently exuding."

    Claude "Getting real creative with the insults, aren’t you?"

    Rory "I have never meant anything more in all my bull years."

    Claude "That explains why you’re such a bullshitting—"

    Rory "Come to think about it, Mentor, can I take this artifact for a spin before you put it in your lab?"

    Rory "This design is perfect for one of my dolls. I can create a new puppet based on these intricate patterns and symbols. It will be a showstopper!"

    Claude "But that’s absurd, who knows when your puppet project is going to finish?"

    Lars default "That’s a great idea! We could even visit your puppet show stall and see what magic you will create. It’s been some time since I last played with the kids as well."

    Sylvian "If you feel inspired by this artifact, then by all means, go ahead."

    Claude "Not you too, boss…"

    Claude "Captain, how about you wear the necklace for now instead of little Rory? It’s color suits your fur, after all. It reminds of the red string of fate—"

    Rory "Not with the little Rory comment again—"

    Lars narration "These confession jokes are getting really out of hand."

    Lars narration "I take this moment to put on the necklace, the gemstone’s ruby color captures my attention and I marvel at the curious glow that emits from it. Almost as if…it’s shining or signaling something."

    Lars narration "Soon enough though, my name is called and the four of us make our way towards the open area adorned with numerous stalls. Master Sylvian deliberately slows his steps, keeping a watchful eye over the rest of us as we go ahead."

    Lars narration "Meanwhile, Claude and Rory pick up their pace, engaging in a competition to see who can reach the stall first. Their banter fills the air as they exchange witty remarks, not holding back on their rivalry."

    Lars narration "Hopefully, it’ll be another day without any troubles here in Divonia and ‘Custodes Sylvae’."

    scene bg 3 at bg_size

#***** ERROR ***** Command not recognized
#[start playing track 3-the town]
#***** ERROR ***** Command not recognized
#[panning effect again]
#***** ERROR ***** Command not recognized
#[people talking + birds SFX starts]
    Lars narration "The town square pulsates with vibrant energy with the captivating tapestry of stalls embellishing the grassy pathway."

    Lars narration "As I walk through this bustling scene, my attention is drawn to the medley of merchants enticing passersby with their wares, creating an atmosphere of enchantment and wonder."

    Lars narration "The tantalizing scents of delectable dishes waft through the air, drawing in hungry travelers, including myself, with promises of culinary delights."

    Lars narration "As I stroll along, my mind wanders to my guildmates, and I can’t help but imagine them donning different attire from the clothing boutiques."

    Lars narration "My imagination runs wild with visions of my guildmates donning different attire from the stalls."

#***** ERROR ***** Command not recognized
#[people talking + birds SFX end]
#***** ERROR ***** Command not recognized
#[rory sprite appears]
    Lars narration "Rory comes to mind first as my best friend. A practical and independent soul, whose artistic flair and unique personality are effortlessly mirrored in her attire."

    Lars narration "Her outfits are accessorized with charming trinkets. Practical short sleeves allow her to move with ease, while thoughtfully designed pockets serve as clever storage for her beloved tools and equipment for her puppet shows."

    Lars narration "Particularly her emergency puppets, which always seem to come to the rescue in unexpected situations."

#***** ERROR ***** Command not recognized
#[panning effect ends]
    Lars narration "Hmm...who else would benefit from a new imaginary outfit?"

    menu:
        Lars " "

        "Master Sylvian":
            $ options["CS2"]=1
            jump master_Sylvian

        "Sir Claude":
            $ options["CS2"]=2
            jump sir_Claude


label master_Sylvian:

    Lars narration "Master Sylvian himself, as a flower magician, could effortlessly conjure his clothing using floral magic. Whereby, every thread is spun with enchanting intentions, and each stitch is softly whispered with a spell."

    Lars narration "His preference for dark colors has always made its way to his costumes, as evident by his current attire, which could have very well been woven from midnight—hued flowers such as black roses, velvety tulips, and elusive calla lilies."

    Lars narration "I figured that he chose this attire to harmonize with the color of his swan—like wings while retaining a touch of vibrant hue throughout his ensemble using delicate petals and intricate floral patterns."

    Lars narration "Also, one component that has been ever—present in his attire is his personally crafted magician’s hat."

    Lars narration "He once revealed that this unique tool stabilizes the emotional energy he channels, transforming it into an array of different blooms. Yet, I have never tried to delve into learning them."

    Lars narration "My studies have been about memorizing the names of plants and herbs that dragons can consume safely. Avoiding poisoning oneself is...useful, to say the least. Nevertheless, my familiarity with the flowers has grown to the extent that I can finally remember their names even if my academic knowledge is nowhere near Master Sylvian."

    jump CS_2_End

label sir_Claude:

    Lars narration "Sir Claude always holds his appearance with unparalleled pride. I can envision him draped in a new style of opulent faux fur and leather clothing, masterfully curated from exotic lands."

    Lars narration "While we do not resort to savagery by hunting our fellow descendants who have not yet undergone their human evolution, acquiring such materials still requires magical instruments and carefully selected components."

    Lars narration "However, this never poses a problem for Sir Claude, courtesy of his family, and even his own, well—established connections."

    Lars narration "Surrounded by a retinue of devoted servants, he could easily present with a garment thoughtfully designed to accentuate and showcase his glistening scales, and maybe even leave an opening for his enormous tail."

    Lars narration "However, knowing his independent spirit, I wouldn’t be surprised if he follows his own instincts and chooses something that catches his eye, disregarding the counsel of the fashionista advisors of his lavish estate."

    Lars narration "Even now, as I observe him, his cascading braids of shimmering silver gracefully flow down his back, a sight that serves as a reminder for me to attend to my own unkempt fox fur and strive to neaten my ponytail."

label CS_2_End:

    Rory "I don’t think I need to keep reminding everyone, but if any of you happen to spot my parents about, could you... convince them to attend the show?"

    Rory "I’ve tried inviting them countless times, but they always manage to find an excuse. It’s just that, if someone else were to extend the invitation, they might feel too embarrassed to decline."

    Lars narration "Rory’s family always took pride in showcasing their meticulously crafted armors and weapons, forged with skill and passion over months and years."

    Lars narration "Whenever I pass by their impressive stall, I can’t help but be awestruck by the gleaming steel and the intricate designs that speak of their unwavering dedication to their art."

    Lars narration "It’s no surprise that if anyone were to harness the shimmering blazes of the Spotted Azureflame, it would be them, for they embody the spirit of the forge and the indomitable strength of their bull lineage."

    Claude "Let it be known that I’m only helping out from the Captain’s wishes. Otherwise, I’d be indulging in a cool shade at my family’s own tradepost."

    Lars narration "The glint in his eyes hints at the allure of the treasures that await. After all, the Dupont family are notorious for their array of foreign trinkets; enticing visitors with a fascination for distant lands and cultures."

    Lars narration "Their stalls are always filled with rare and luxurious items, each one carefully curated to capture the attention of potential buyers seeking something unique and extraordinary, for the right price, of course."

    Claude "Who knows, my dear Captain, some of them might perfectly complement your new necklace artifact, and we’d both have the pleasure of admiring them on our adventures. I can already imagine a perfect matching set of —"

    Lars default "Thanks for the offer, Sir Claude, but what use would I have for them? They’ll only get lost during dragon riding."

    Lars narration "Ever the showman, he raises his eyebrows in mock shock, dramatically pausing."

    Claude "So, you’re open to accepting an accessory that’s on you without you needing to pocket it, right?"

    Lars default "I guess so, but I don’t want to force—"

    Claude "Perfect! What would be the ultimate gift to match Captain’s splendor? Any thoughts, Rory?"

    Lars default "What do you mean—"

    Rory "Why would I help you?"

    Claude "How about a friendly competition, then? May the best one win and the prize will be…"

    Rory "I couldn't care less about prizes. I just want to savor your defeat!"

    Rory "Now! Let me think this through..."

    Rory "Earrings? Nah, not good. They’d be gone with the wind before you know it!"

    Rory "[Lars] already has that fancy necklace artifact, so no need for now. Well, until Mentor gives it the look."

    Rory "Bracelets or anklets would be a disaster around the dragons too. They’ve got those sharp pikes and claws that could easily tangle things up. We either need to go bigger as in armor size or go smaller like a—"

    Claude "How about a ring then? It could be the perfect accessory to keep on without it getting in the way!"

    Claude "What about it, Captain? Are you up for it?"

    Lars default "What are you talking about? That’s basically a proposal, isn’t it?"

    Claude "Not so much a proposal, but more of a heartfelt promise that you’ll keep me in mind whenever you look at it. After all, you always accept Boss’s bouquets and poems. Don’t they count as gifts too?"

    Lars default "Well, they do count as gifts, but I find it more convenient to keep notes in my pockets. And flowers are not rings."

    Lars default "I’m sure Master Sylvian doesn’t have such intentions for our relationship either. We\re just friends, right?"

    Lars default "The same goes for you, Sir Claude; weren’t you the person always making confession jokes in the first place?"

    Lars narration "I waited for someone to respond. However, all I was met with was silence."

    Lars narration "Sir Claude seemed to be already lost in a daydream as he closed his eyes, whispering softly to himself, as if he were planning something important and couldn't care less about the current situation."

    Lars narration "Who should I question about the intentions behind their gifts?"

    menu:
        Lars " "

        "Ask Master Sylvian about his poems and flowers":
            $ options["CS3"]=1
            jump ask_Master_Sylvian_about

        "Ask Sir Claude about his keepsake ring":
            $ options["CS3"]=2
            jump ask_Sir_Claude_about


label ask_Master_Sylvian_about:

    Lars narration "I decide that it’s best to approach Master Sylvian first, as he tends to take my words more seriously than Sir Claude does. With Sir Claude occupied with himself, this seems like a better choice."

    Lars default "Master, why didn’t you answer my question earlier?"

    Lars default "Was there a different intention behind all the gifts you’ve given me?"

    Lars narration "I steal a glance at Master's concealed face, obscured by his dark wings. He bore a resemblance to the very flowers he acquired, his cheeks flushing into the vibrant hue of a blooming rose."

    Sylvian "Uhm…How do I put it…it’s j-just that—"

    Sylvian "W-w-well, I…I don’t think this is the best time to, you know...uhm...explain my reasoning, but—"

    Lars default "So, you do have a reason aside from our friendship, correct?"

    Lars narration "As if drawn in by the gravity of my serious question, he takes a deep breath and looks me directly in the eyes. Slowly, his face regains its natural color, and he begins to speak."

    Sylvian "I…I don’t want to lie to you, [Lars]. Concealing my true feelings would only bring harm upon myself, akin to breaking my own neck under the weight of deception. However, this isn’t the right time for me."

    Sylvian "You hold a unique place in my heart, [Lars], and I truly admire you. Yet, confessing my secrets now fills me with apprehension, I fear that it might jeopardize the bond we share."

    Sylvian "Moreover, the delicate balance of our guild relationship as boss and guild member makes my feelings for you... somewhat unethical."

    Lars default "…"

    Lars default "Understood, Master. I’m not sure I get it entirely, but I won’t press you further, especially since I’m in doubt if you’re referring to a personal secret or something more. But no more gifts for now, I don’t want there to be another misunderstanding between us."

    Sylvian "I’ll hold back on the bouquets as you requested, but I confess that abstaining from the poems might prove to be a more difficult task, after all…"

    Sylvian "“If metal can be polished to a mirror—like finish, what polishing might the mirror of the heart require?”"

    Sylvian "“Between the mirror and the heart is this single difference:”"

    Sylvian "“The heart conceals secrets, while the mirror does not.”"

    Sylvian "In the future, I promise to make you my mirror and show my honesty, if you allow me to."

    Lars default "Let’s save that talk for later, per your wish then. Whenever you feel ready to share, I’ll be here to listen."

    Sylvian "You have my thanks, [Lars]."

    Lars narration "His sincerity and genuine care touch my heart, leaving me with a mix of emotions and questions that I know will find answers in due time. For now, I’ll cherish this moment and the promise he’s made."

    jump CS_3_End

label ask_Sir_Claude_about:

    Lars narration "Maybe it is best to approach Sir Claude first, since Master is not currently in a state to discuss these things. Claude tends to be more forthright with his answers as well, so..."

    Lars default "Why did you mention a ring, Sir Claude? I feel like you might be taking the teasing a bit too far today."

    Claude "Oh, Captain, why would you ever think that? After all, you did say you could wear it, didn’t you?"

    Claude "I have no qualms about covering the cost either. You could ask for all the gold in this realm, and it would be yours to possess."

    Claude "Or could it be that you want more? Not that I have any issue with it; I adore the idea of endlessly spoiling the person I —."

    Lars default "I’m not exactly talking about that, but there’s honestly no need—"

    Claude "Need I remind you about Master Sylvian’s gifts?"

    Lars default "His presents are purely gestures of appreciation, but rings usually mean a lot more. Proposals, offerings, significant others... What would my passengers think—"

    Claude "Forget about it for now, this is a matter between you and I."

    Lars default "Although… some human passengers mentioned gifting rings as accessories, is that what you meant?"

    Claude "Maybe it’s too soon for you to understand me, Captain, but you should know this…"

    Claude "You could say the reason I’m suddenly giving you these rings is because of Boss Sylvian over there. I’ve noticed that he’s been getting too close to you recently, and it’s making me—"

    Lars narration "He throws his hair backwards, intense gaze locked onto me."

    Claude "I don’t like the thought of losing what I’ve set my sights on to someone else, particularly when I’ve been showing my intentions to you all this time."

    Lars default "So, it’s just a competition to you? A rivalry to see who can get closest to me and then revel in the feeling of winning?"

    Claude "That’s not what I meant…"

    Lars narration "He takes a deep breath, preparing himself as if he’s about to reveal a significant secret."

    Claude "I do have special feelings for you, Captain, and I admit they’re not ones as simple as friendship. But you know how I’ve always been hesitant about settling down. It’s a personal struggle that I’m trying to come to terms with, but I can’t openly share all of it here with everyone else."

    Lars default "What do you mean by special feelings—"

    Claude "Why don’t we continue this conversation somewhere private, just the two of us? I’ll truly open up and explain my intentions. Please believe me when I say I have no plans to play with your feelings."

    Claude "My interest in you is genuine, but it’s difficult for me to express myself and keep my emotions anchored when my heart always yearns for new adventures and distant horizons. Not to mention, Boss Sylvian…"

    Lars narration "Hearing Claude’s earnest plea, I realize that this situation is more complex than I initially thought. His vulnerability and honesty tug at my heart, and I know I need to hear him out, away from prying eyes and distractions."

    Lars narration "I nod, silently agreeing to have this crucial conversation in a more intimate setting."

    Lars default "…"

    Lars default "Understood, Sir Claude. While I can’t say I’m entirely satisfied, I won’t press you further."

    Lars default "Just know that I’m open to hearing your explanations and understanding your feelings whenever you’re ready to share them whether personal or more."

    Claude "Thank you, Captain. I promise I’ll tell you later, and you can count on me to keep that promise. I might even add it to the keepsake I’ll give you later on."

    Lars default "No rings! I don’t want to be burdened with uncertain feelings. I won’t let myself be strung along especially since I need to keep my mind sharp for the passengers. What would happen if I were to be distracted and—"

    Claude "What about your necklace? Why don’t I promise on that instead?"

    Lars default "Uhm…I guess that’s okay."

    Lars narration "Suddenly, Claude closes in, giving me a quick but strong hug. I catch a glimpse of what can only be a light blush on his cheeks as he holds me closer."

    Claude "You mean a lot to me, Captain, and I don’t want to rush my secret. When the time is right, I’ll share everything with you, and I hope you’ll understand."

    Lars narration "His sincerity and genuine care touch my heart, leaving me with a mix of emotions and questions that I know will find answers in due time. For now, I’ll cherish this moment and the promise he’s made."

label CS_3_End:

    Rory "Let’s keep moving on, shall we? (start grassy footsteps SFX)"

    Lars narration "We managed to blend seamlessly into the diverse crowd of people, encompassing both humans and descendants. It was quite a challenge to navigate through the various tails, wings, and horns of different species."

    Lars narration "Yet, after riding countless dragons and growing accustomed to their scales, a few feathers or fur proved to be manageable obstacles. Speaking of which…"

    Lars default "By the way Rory, what’s our plan for today?"

    Lars narration "It was no secret that Rory’s performances provided the main source of funding for our expeditions and negotiations, making it a collective mission for all of us to advertise her show today."

    Lars narration "The well—being of our guild dragons heavily relied on those funds, and I cannot bear the thought of them going hungry or enduring any discomfort. I would willingly starve myself before allowing such a situation to come up."

    Rory "I was thinking that we could focus on a kids show for today [Lars], you guys can gather the kids up ahead."

    Lars narration "Before long, the collective footsteps of our group came to a halt, a unanimous signal that we had arrived at our destination. (stop grassy footsteps SFX)"

    Rory "Here we go! A one-of-a-kind stall for one-of-a-kind puppets who actually have a purpose in life, unlike a certain someone."

    Rory "Not to mention, Brittina and Alex were very excited to enhance their looks with the help of Claudy over here."

    Rory "I did want to pluck out the lizard’s eyes for Agatha, but it’s very hard to do that in his sleep especially since he’s such a light sleeper."

    Lars default "He’s the heaviest sleeper I know, what’re you talking about?"

    Rory "I wouldn’t put it past him to fake it or something. He’s got some screws missing—"

    Claude "Ehhh, you’ve been watching over me in my sleep, little Rory?"

    Claude "I could excuse the scale stealing incident and the hair cutting fiasco because I’m so benevolent."

    Claude "However, night peeking is a no-no."

    Claude "Unless it’s my lovely Captain who does it."

    Lars narration "His comment certainly came out of the blue, what should I do now? They’re both looking at me."

    Lars narration "Oh, no..."

    Lars narration "What do I do?"

    menu:
        Lars " "

        "Look back at Master Sylvian":
            $ options["CS4"]=1
            jump look_back_at_Master_Sylvian

        "Look back at Sir Claude":
            $ options["CS4"]=2
            jump look_back_at_Sir_Claude


label look_back_at_Master_Sylvian:

    Lars narration "I glance at Master Sylvian, silently seeking his assistance."

    Sylvian "I think it’s time to stop teasing [Lars], Claude. Let’s give him some space and respect his feelings."

    Lars narration "I can see Sir Claude making a stupefied face due to Master Sylvian’s interference."

    Lars narration "Meanwhile, Master Sylvian regards me with a kind look, silently assuring me that he has my back. He reaches out and gently rubs my ears, soothing my embarrassment as my ears perk up."

    Lars default "That’s right, listen to Master Sylvian. He is far better at understanding my cues and emotions than you."

    Lars narration "Sir Claude puts on an even brighter smile, and I can’t help but wonder if it’s a display of sarcasm or not. Soon enough, he lets out a light sigh, seemingly contemplating his actions."

    Claude "…I suppose. Can’t go against our esteemed Captain’s wishes."

    Claude "But you can’t be serious about Master Sylvian reading you better than I do."

    Lars default "I am, Master Sylvian has shown genuine care and consideration for my feelings. However, with you, it often feels like everything is taken as a joke or a competition!"

    Lars narration "As if prompted by my sudden outburst, Master Sylvian steps in with his own words of support while Sir Claude adorns a stupefied look."

    Sylvian "Claude, it’s time to stop with the teasing. [Lars] and I have made a promise, and I don’t want you to interfere in a way that jeopardizes our relationship, especially if it goes in a direction you may not be prepared for."

    Claude "Fine, fine. I’ll back off for now."

    Claude "Just know that I’m not giving up."

    Sylvian "I think it’s best to give up entirely, never use someone’s weaknesses as a weapon against them, for it reflects your own character more than theirs, Claude."

    Claude "As much as I adore your poetry and philosophical quotes, I’ll stand my ground when it comes to teasing Captain over here."

    Claude "You see, it’s fun for me to see which of his buttons I can push."

    Claude "And any person who tries to be good all the time, like you, is destined for downfall unless they find a way to unleash their deepest desires."

    Lars narration "A shadow crosses Master Sylvian's face at Sir Claude's comment, as if it had struck a nerve deep within him. The situation appears to be teetering on the edge of getting out of hand, but my curiosity urges me to see how things will unfold."

    Claude "I would even dare say that you’re the one who is harboring the most dangerous inner feelings among all of us. Because, at least, I can release my emotions by having fun with my Captain."

    Lars narration "…my...Captain...?"

    Claude "Yet, you only ever have your flowers to bear your secrets with."

    Claude "I think it’s about time for your head to equally start fuming like little Rory over here."

    Rory "Hmph! I’d lower myself to your idiotic level, but then you’d beat me with experience."

    Claude "Not to mention, isn’t it time for you to admit to [Lars] that you’ve loved—"

    Sylvian "CLAUDE!"

    Sylvian "I treasure you as a guild member of ‘Custodes Sylvae,’ but your snapdragon of a mouth is intolerable."

    Sylvian "Gracefully deceptive petals that press together to bloom in beauty. You certainly have a lot to say, but when it comes to revealing things about yourself, you remain as enigmatic as ever."

    Sylvian "How about revealing the reason behind that ‘ambitious’ persona which you so often try to show off?"

    Claude "I thought we had a deal not to—"

    Rory "Uhm, Mentor, I don’t understand what’s going on here. But can we stop bickering for a second?"

    Lars default "Rory’s right, it’s not like you two to argue like this…"

    Claude "It seems that some things—"

    Sylvian "—are overdue for the both of us."

    jump CS_4_End

label look_back_at_Sir_Claude:

    Lars narration "I glance at Master Sylvian, silently seeking his assistance."

    Claude "Who knows what stage our relationship will reach in the very near future, especially considering our promise."

    Lars narration "He winks at me, exuding a seductive charm that is hard to resist. I can’t help but be captivated by the look in his eyes, which are solely focused on me. There’s a magnetic quality to his gaze, drawing me in and making my heart race."

    Lars narration "He stretches his hand in my direction, entwining our fingers and pulling me closer. I unfortunately blush upon touching shoulder to shoulder with him."

    Lars narration "Yet, I can’t help but notice a storm forming above Master Sylvian’s head. His eyebrows knit together embittered while crossing his arms."

    Lars narration "At the same time, delicate hyacinth blossoms, with a regal purple hue, line the brim of his hat. However, with each subtle shake of his head, the petals wilt and wither away, mirroring the disappointment etched on his face."

    Lars narration "But why?"

    Lars narration "I’m not always on board with Sir Claude’s shenanigans, but it’s often easier to go along with his wishes rather than challenge him. The thrill of competition turns resistance futile. He loves it."

    Lars narration "Master Sylvian knows that as well, so why would he…show such an expression?"

    Claude "Whether it’s the way your cute tail wags around when you start rambling or how your ears perk up while listening to human’s tales, I can tell each and every one of them apart."

    Lars narration "His scaly hand traces the contours of my ears. I could feel myself slowly heating up even more; my ears and tail are too sensitive for this."

    Claude "I don’t need magical gimmicks to understand you, Captain. Though, I still enjoy teasing and playfully tugging on the line between us."

    Claude "But rest assured, I’ll turn this line into a strong thread of destiny that will bind us in ways you can never imagine. Nothing is impossible if I put my mind to it, exclusively for you."

    Lars narration "This mix of charm and intrigue keeps me flustered and curious. His confidence is...quite romantic."

label CS_4_End:

    Rory "Sorry to break up your moment guys, but in the meanwhile…"

    Rory "Try to gather the kids while I set everything up."

    Lars narration "I make my way through the bustling groups of kids, determined to gather their attention. The excitement in the air is palpable as their laughter and chatter fill the space."

    Lars narration "With a deep breath, I project my voice, shouting out an announcement that echoes through the crowd."

    Lars default "HEY EVERYONE, I’M BACK!"

    Lars default "THE PUPPET SHOW IS GOING TO START SOON! GATHER UP YOUR FRIENDS TOO!"

    Lars narration "The moment I finish my announcement, I am instantly bombarded by a swarm of enthusiastic children. They run towards me, their voices rising in a crescendo of excitement as they vie for my attention. (children playing SFX starts)"

    Lars narration "Little hands tug at my sleeves, pulling me in different directions, each child eager to share their thoughts or be part of the upcoming event."

    Lars narration "Amidst the joyful chaos, I can see Sir Claude and Master Sylvian observing from afar, their watchful eyes filled with amusement and a glint of… something else that I can’t quite put my finger on."

    "Random Kid 1" "Yay! [Lars] is back from his trip."

    "Random Kid 2" "I missed you, [Lars]; my dragon has been messing with my toys recently. You definitely have to help!"

    "Random Kid 3" "[Lars]! Don’t forget we still have our race for the afternoon. You have to help me win, please!"

    Lars default "Heh. This takes me back to when I was a kid."

#***** ERROR ***** Command not recognized
#(children playing SFX ends)
    Sylvian "I hope I’m not bothering you in the middle of your duty, [Lars]."

    Lars default "Of course, not Master, this would be the perfect time to show off my skills to you in person. I’m the fastest amongst everyone here after all."

    Claude "Hmm, how typical of our dear Captain to compare himself with mere children."

    Lars default "I can outrun you any time."

    Claude "You think yourself soooo \"fast\", huh? I could leave you speechless If I wanted."

    Lars default "Well, Sir Claude, it's not a race if you're just jogging to the finish line."

    Lars narration "At this moment, both guild members stand by my side. Sir Claude, with his innate charisma, effortlessly charms the children surrounding us. Meanwhile, Master Sylvian, mesmerizes them with his expertly performed flower magic."

    Claude "Awe, I’ll pretend to be hurt, but while I’m still here, take my advice. You have to challenge yourself more."

    Claude "You won’t be able to show off your talents to anyone when you spend your time with these childish competitions. How will you be able to prove yourself to the elite if you only ever rival with kids?"

    Lars default "Not everything is a contest to prove oneself, Sir Claude."

    Lars default "Sometimes, I can be content with just playing around and enjoying the moment as is. Isn’t that right, Master?"

    Sylvian "Success without heart can be empty and hollow, Claude. I worry for the sake of your ‘ambition’ you carry yourself differently from your family legacy."

    Lars narration "Family legacy…"

    Lars narration "It was certainly true that Sir Claude had the tendency to act out against his family’s wishes from time to time but according to the rumor mills, he didn’t have a reason to."

    Lars narration "The Dupont family, a lovely couple of lizard descendants, never strived Claude of love and affection."

    Lars narration "However, he had the notion of removing them from his character from time to time, as if he were born from a nameless hermaphrodite and all he ever was is one ‘Claude’ and not a ‘Dupont’."

    Sylvian "If you merely pursue rivalry to prove your self-worth to unknown faces, it will only be a matter of time before the present escapes your reach."

    Claude "With all due respect, Boss, but, isn’t that lack of ambition precisely why you’re here with us today instead of boasting around the academia halls?"

    Rory "Not cool, Claude. You can’t poke into someone's past like this."

    Sylvian "Hold on, Rory. I want him to explain himself."

    Rory "If you say so…"

    Claude "Though I value your presence in our guild and your support of my endeavors, Boss, you have let go of all your desires and merely follow the direction that your flowery path takes you."

    Claude "But, you see, if you’re not determined about your dreams, someone else could come and snatch it right out of your hands."

    Lars narration "I catch Sir Claude throwing a peek at me but he quickly switches his focus back to Master Sylvian."

    Lars narration "When it came to dreams, Master Sylvian had garnered quite the reputation as the ‘genius of the century’ during his tenure at the Tower of Magicians in Divonia."

    Lars narration "Although he rarely spoke about his past experiences, a glimpse into his emotions could be seen in the way his feathers drooped and his shoulders slumped with a sense of dejection whenever the topic came up."

    Lars narration "Even his perpetual hunched posture served as a constant reminder of his time as a prestigious state magician. A time where he would work himself to the bone day and night with no rest in between."

    Lars narration "Despite his current focus on flower magic, it was evident that Master Sylvian had a different area of expertise in the past. The secrets and stories behind his prior magic remained locked away, untold."

    Lars narration "The formation of our guild seemed to be a deliberate decision he made in response to his experiences as an academician, though he seldom delves into the specifics."

    Claude "It’s in the very motto of ‘Custodes Sylvae’ after all."

    Claude "‘Discere, cogitare, agere— the triad of wisdom. Learning enriches the mind, and thinking sharpens it, but it is through action that we truly manifest our knowledge and shape our reality’."

    Claude "You are tripping on the third step."

    Claude "Isn’t that right, Captain?"

    Lars default "…"

    Sylvian "These statements hold grains of truth, Claude."

    Sylvian "Without love or ambition, our lives languish in the shadows of mediocrity."

    Sylvian "They ignite the fire within, propelling us to venture beyond our limits, to dream and to create, shaping a life of purpose and fulfillment."

    Claude "So, you do agree—"

    Sylvian "However…"

    Sylvian "Amidst our pursuit of them, let us not overlook the tranquility of mediocrity."

    Sylvian "For not every path must lead to grand creations or extraordinary feats."

    Sylvian "In embracing simplicity, we find contentment, and in cherishing the ordinary, we discover the beauty of a life unburdened by the pressures of relentless ambition."

    Claude "Aren’t you saying that only because you were burnt out and having nothing else to pursue?"

    Claude "If you always treasured this so-called ‘contentment’ why did you decide to spread your name onto society as the top academic of Divonia?"

    Claude "You could have simply stuck to the bottom ranks and let your life aimlessly pass by without ever achieving something or falling in love."

    Sylvian "You exude the scent of conceit and arrogance, Claude. It's a disappointing fragrance to bear witness to in the presence of such a beautiful flower."

    Claude "I wonder who you could be referring to…any clues, [Lars]?"

if options["CS3"]==1:

    Lars default "What’s he talking about, Master?"

    Lars default "Is that part of the secret you wanted to tell me? That you were in love with someone else? Then, what about the mixed signals that I’ve been receiving from you thus far?"

    Sylvian "N-no, you’re misunderstanding something here— I-I mean, not you. It’s probably my fault here, but—"

    Lars default "I don’t want to sound conceited, but if I were the person you're in love with, I’d like to think that you would have told me about it by now."

    Lars default "But then again, you're secretive about your history as well…"

    Sylvian "I’m sorry that I can’t tell you any more about it."



else:

    Lars default "I’ve been so busy with Sir Claude that I didn’t even notice. You’ve fallen for someone, Master?"

    Lars default "That’s exciting! When are you going to introduce us?"

label if_op_cs_3_end:

    Claude "Focus here Captain, we can talk about that later. Unless you’ve already taken someone’s side?"

    Lars default "Uhm, you’re both people that I deeply admire and I don’t really want to—"

    Claude "Don’t want to? I expect you to at least share your personal opinion if you share the sentiment of taking no side."

    Sylvian "Pay him no mind, [Lars], he’s just upset for himself."

    menu:
        Lars " "

        "Agree with Master Sylvian about valuing our current contentment":
            $ options["CS5"]=1
            jump agree_with_Master_Sylvian

        "Agree with Sir Claude about the positive value of ambition":
            $ options["CS5"]=2
            jump agree_with_Sir_Claude


label agree_with_Master_Sylvian:

    Lars default "I agree with Master Sylvian."

    Lars default "I think what he says is true about enjoying what we want instead of simply going after it for the challenge."

    Lars default "I like hanging out with my dragons even if we weren’t in the middle of an expedition or mission and I wouldn’t change my relationship with them for the world."

    Lars default "Going after artifact hunts and transporting passengers without an ounce of love seems depressing to me."

    Sylvian "Thankfully, Claude’s influence hasn’t rubbed on you too much."

    Sylvian "Amidst the circle we tread, like the Ouroboros we find. Forever chasing our tails, destiny intertwined."

    Sylvian "I’m always impressed by how well you articulate your words, my dear junior. Maybe, we can discuss these philosophies and some other things once we have free time."

    Lars default "I would love to spend time with you but Spotsy needs me more, don’t you think so?"

    Lars default "She’s had a long flight after all."

    Sylvian "I can’t deny that I am a bit disappointed…"

    Sylvian "However, it’s one of the things that I like seeing you do, [Lars]."

    Sylvian "It’s amongst my wishes to someday be a recipient of the same adoration you hold for your dragons."

    Lars default "Haha, it’s best if we call a truce with everyone for now."

    jump CS_5_End

label agree_with_Sir_Claude:

    Lars default "I agree with what Sir Claude says."

    Lars default "It’s not fair to avoid fighting for what you love and desire."

    Lars default "I could admire my dragons all day and night but if I never take that leap of fate to touch them and show them my feelings directly, then I’ll only ever be walking in a circle."

    Lars default "I also can’t imagine going a day without learning about the new dragon species out there."

    Claude "Glad to see that you’ve learnt a few things about my motto of life, Captain. It’s not complete, but I’ll teach more later, in private."

    Lars default "I would love to spend time with you but Spotsy needs me more, don’t you think so?"

    Lars default "She’s had a long flight after all."

    Claude "At this rate, I don’t think I’ll ever be able to compete with your love for dragons, Captain. But I’ll do my best to win you over, and spoil you rotten the same way you do for your dragons."

    Lars default "Haha, it’s best if we call a truce with everyone for now."

label CS_5_End:

    Lars narration "While I’m engrossed in our conversation, Rory approaches us with a somewhat worried expression etched on her face."

    call part_2 from _call_part_2
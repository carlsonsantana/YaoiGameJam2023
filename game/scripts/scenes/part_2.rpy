#linear 0.5 xalign 0.5
label select_route: 

    $ calc_relations()
    #$ txt_temp = f'{options["C1"]}-{options["C2"]}-{options["CS1"]}-{options["S1"]}-{options["S2"]}-{options["CS2"]}-{options["CS3"]}-{options["CS4"]}-{options["CS5"]}-{options["CS6"]}'
    #$ txt_temp2 = f'c:{relations["claude"]} s:{relations["sylvian"]}'
    
    menu:
        " " " "    
        "Select Claude route":
            jump claude_route

        "Select Sylvian route":
            jump sylvian_route

label sylvian_route:
    show zephyr happy at left:
        yalign 0
    show claude zorder 2 at center_left with dissolve:
        xzoom -1.0
    show sylvian zorder 1 at center_2right with dissolve:
        xalign 0.65
    show rory at right with dissolve:
        xalign 1.05
    
    $ zephyr_name = "Zephyr"
    voice "audio/voice/zephyr/zephyr_077_take02.ogg"
    show lars
    Zephyr "Did you pick someone already? I need something big to spark my gossip debut if I plan to pay off my debt and renovation costs with your confession shenanigan."

    "I grab Master Sylvian's hand in mine and interlace our fingers as I raise them up for Zephyr to see."

    show lars blush
    Lars "I choose him."

    $ renpy.choice_for_skipping()
    show claude sad with dissolve
    
    "Upon my declaration, Sir Claude's holds his hand on his chest, a sour expression etching on his face as he blankly stares ahead."
    
    "But I can't worry about that now. I need to concentrate on Master Sylvian."
    
    hide claude sad with dissolve

    show sylvian at center with move
    show sylvian blush at center
    voice "audio/voice/sylvian/sylvian_088_take02.ogg"
    show lars blush
    Sylvian "Thank you, [Lars]. I truly mean it."

    voice "audio/voice/sylvian/sylvian_089_take04.ogg"
    show lars blush
    Sylvian "Now my heart can rest at ease knowing I'm allowed to selfishly stay by your side."

    show zephyr at jp
    voice "audio/voice/zephyr/zephyr_078_take01.ogg"
    show sylvian
    show lars
    Zephyr "So, Smarty it is then!"

    voice "audio/voice/zephyr/zephyr_079_take02.ogg"
    show lars
    Zephyr "Now tell me, what makes him so special? How's the scoop going to be different from all the other celebrity gossip columns and panels?"

    show rory
    voice "audio/voice/rory/rory_048_take02.ogg"
    show lars
    Rory "He's one of Divonia's brilliant minds, a leading researcher who uncovered the connection between human travelers from Earth and Divonia. Plus, he's a master of flower magic."

    voice "audio/voice/sylvian/sylvian_091_take01.ogg"
    show lars
    Sylvian "My dear junior..."

    voice "audio/voice/rory/rory_049_take02.ogg"
    show lars
    Rory "If I'm not going to vouch for my mentor, then who will?"

    voice "audio/voice/zephyr/zephyr_081_take02.ogg"
    show lars
    Zephyr "That does indeed sound like a juicy tale for the gossip mill {i}'the renowned swan-tist of Divonia and his hidden discovery'{/i} but it's missing something. Perhaps a love confession would—"

    show lars serious
    Lars "Before we get started on anything, didn't you promise that you'd unfreeze the others?"

    show lars serious
    Lars "I don't want to risk getting the other guild members hurt, or have anyone else suffering from the time freeze's effects."

    show lars serious
    Zephyr "Fine, I wouldn't dishonor my family by breaking my oaths, but you better cough up a scoop worthy of my undivided attention!"

    show lars serious
    Zephyr "Let's spice up the setting while we're at it; I wouldn't want someone else to hijack my headline when I finally release them from their frozen state."
    
    show lars serious
    Zephyr "Scouty, pick a fancy locale worthy of my grandiose presence, won't you?"

    hide zephyr
    hide claude
    hide sylvian
    hide rory
    with dissolve
    $ renpy.choice_for_skipping()

    play music "track_6_romance_scene.ogg" fadeout 2.0 fadein 2.0

    scene bg black with fade
    show bg_5 at pan

    "The sun is gradually sinking towards the horizon, casting cold hues across the sky as late afternoon approaches."

    show lars
    Zephyr "Whose brilliant idea was it to choose the seaside for a confession scene?"

    show lars
    Zephyr "I had to bring a dragon for the ride just to carry you two over here."

    show lars
    Lars "You wanted a place with few to no people, and here we are."

    show bg_5 at end_pan

    show zephyr at center_2left with dissolve:
        yalign 0

    show sylvian at center_2right with dissolve
    show lars
    Zephyr "Whatever! I'm focused on keeping the coast clear, especially since I had to unfreeze everyone but I've got my eyes and ears on you two. Make it count while we're down here."

    $ renpy.choice_for_skipping()
    show zephyr:
        xzoom -1
        pause 0.5
        linear 3.0 xalign -2.0
    
    pause 1.0
    show sylvian blush with dissolve
    show sylvian blush at center with move
    
    show lars
    Lars "..."
    
    "I shoot a glance at Master Sylvian and bite my lips in frustration. I chose him as my partner, but with Zephyr so close by, I'm unsure of our next move."

    show lars serious
    Lars "There's not much time, we have to do something."

    show sylvian serious funny
    show lars serious
    Sylvian "It's indeed disheartening to witness such a scenario, where the transported humans' unique and sporadic presence is taken advantage of."

    show lars serious
    Sylvian "Being a rarity, they can be subjected to exploitation due to their infrequent encounters. However, this is the first time I've witnessed such a situation up close."

    show sylvian
    show lars serious
    Lars "Zephyr should have taken up the role of the prime content for his beloved gossip column with all the antics he's pulling."

    show lars serious
    Lars "Exploiting the humans' unfamiliarity with Div customs and culture would certainly shock everyone once they learn what's been happening under their noses."
    
    show zephyr with dissolve:
        xzoom 1
        linear 1.0 xalign 0.0
    
    show lars serious
    Zephyr "{size=*2.0}I HEARD THAT!" with vpunch

    show zephyr:
        pause 0.5
    
    show lars serious
    Zephyr "Enough with the chatter, spill the confessions instead! Since I went through all that effort to ice-olate you two."

    show zephyr with dissolve:
        xzoom -1
        pause 1.0
        linear 0.5 xalign -1.0

    pause 1.0
    show lars sad
    Lars "How do you suggest we proceed, Master? I'm worried more people will get caught up in this mess if we don't act swiftly."

    show sylvian
    show lars sad
    Sylvian "Give me a moment."

    show sylvian at shake
    pause 0.5
    show sylvian at shake
    pause 0.5
    show sylvian at shake
    pause 0.5
    show sylvian at shake
    
    hide sylvian with dissolve
    show vial with dissolve
    
    "Master Sylvian's hands glide with practiced grace, weaving a spell that envelops him in an ethereal aura of blossoms."

    "I'm momentarily entranced by the display, but my attention swiftly shifts to the vial he seemingly conjures from thin air."

    "As per his signature touch, the vial houses an arrangement of flowers, all sharing a captivating purplish hue. Though I can't discern the specific ingredients within."
    
    "I wonder what he's planning on using it for..."
    
    hide vial with dissolve
    show sylvian with dissolve

    show lars
    Sylvian "A small concoction for easing my nerves. There's a chance I might speak of rather {i}personal{/i} affairs in our young Lords' presence."

    show lars 
    Lars "There's no need to be nervous, Master Sylvian. It's not like we'll be doing a love confession like what Zephyr said."

    show sylvian mad
    show lars 
    "Wearing an awkward grin, he lets out a hesitant laugh. Today has shown me sides of him that I'd never imagined before."

    show lars
    Sylvian "Haha, of course not! I-I don't know... what I would— or what I should do if you grew to despise someone like me because of what I might say for a {i}supposed{/i} confession."

    show sylvian serious funny
    show lars
    Sylvian "But fret not, [Lars]. My tenure in academia provided access to restricted sections, and I'm confident in my ability to fashion a fitting gossip source for our young Lord."

    show lars
    Sylvian "Particularly considering his apparent lack of discrimination when it comes to topics or specific requests."
    
    "Feeling a sense of optimism at hearing the news, I enthusiastically chime in."

    show lars
    Lars "You're right. Why didn't I think of that earlier? You could even use your connections to ask for extra help, can't you? So, we can make sure nothing like this ever happens again."

    show sylvian sad
    show sylvian sad at shake
    show lars
    Sylvian "That's going to be a bit difficult."

    "A haunting shadow descends over him, as if a storm cloud has eclipsed the sun. From the edges of his magician's hat, wilted flowers creep out, a stark contrast to their once vibrant bloom."

    "His brows furrow and a warm flush of embarrassment tints his cheeks, like a delicate watercolor painting tainted by an unexpected hue."

    Lars "But weren't you one of the top academics in the past? Surely, there's someone who can—"

    show lars
    Sylvian "{size=*1.25}[Lars]!" with vpunch

    "Ah, that tone again— the one that resonates like a guild leader's command. The weight in his words is palpable, leaving me curious about the sudden shift in his demeanor. But perhaps it's better to divert the conversation for now."

    Lars "Got it. I won't talk about it if you don't want to."

    "I cross my arms in confusion. So, there really isn't a need for us to work together if Master Sylvian already has his plan set... he seems to have a better grasp of the situation, having planned this far ahead without informing me."

    "I should at least avoid giving him any extra burdens to shoulder. Not to mention, I brought him along without discussing it first. Good thing he seemed excited enough to come along though."

    "Ah, I wish Spotsy were near so I could soothe my nerves by caressing her or something. I feel somewhat useless right now."

    show sylvian
    show lars
    Sylvian "Were you thinking of your dragons again, [Lars]?"

    show lars blush
    Lars "How on Divonia did you find that out? Was my tail wagging again? I swear it always keeps-"

    show sylvian blush
    show sylvian blush at jp
    show lars blush
    Sylvian "Hahaha! It's nothing of that sort. It's just that I've been observing you for such a long time that I can't help but pick up on your subtlest of gestures."

    "Hearing that is making me somewhat embarrassed. I'm sure he simply wanted to see if I was doing a good job or not, so I hope I haven't disappointed him."

    Lars "Speaking of which, Master. I did bring you along like this, but to think you had a plan of your own..."

    Lars "What kind of academic gossip tale will you be telling him? Will you be needing my help—"

    show sylvian
    show lars
    Sylvian "You needn't worry, [Lars]."

    show lars
    Lars "But I'd still like to have something to do."

    show sylvian serious funny
    show lars
    Sylvian "Ah, are you searching for purpose? It can be a bit of a maze, and the answers you find might not be the ones you expect."

    Lars "So, should I just sit here and do nothing?"

    show sylvian blush:
        parallel:
            linear 1.0 yalign 0.0
        parallel:
            linear 3.0 zoom 1.50
    
    show lars blush
    Sylvian "Not necessarily. Perhaps I should suggest— or, if I may, show you— an alternative where we could... uhm, if that's okay with you, of course... share a love confession?"

    show sylvian blush at jp
    show lars blush
    Sylvian "It's going to be from my side though, not yours! Obviously not from you; that wouldn't make sense."

    show sylvian blush:
        parallel:
            linear 1.0 yalign 0.0
        parallel:
            linear 1.0 zoom 1.0 

    "It's rather unlikely of Master Sylvian to act in such a manner. My mind drifts to other instances where he displayed a hint of romance, only to revert to the role of a caring yet distant master."

    show sylvian blush with dissolve:
        zoom 1.0    

    "However, this time, his shaking hands and the glistening look in his eyes suggest it's not another session of false bravado but something else— something unknown yet exciting for the first time."

    hide sylvian blush with dissolve
    
label menu_s3:
    $ calc_relations()
    menu:
        " " " "

        "Poke further about his comment":
            jump S3_sylvian_bad_end
        
        " " (blocked=True) if relations["sylvian"]<5:
            jump menu_s3

        "Pass over his comment" if relations["sylvian"]>=5:
            jump S3_sylvian_neutral_end
 
        " " (blocked=True) if relations["sylvian"]<7:
            jump menu_s3

        "Stay silent about his comment " if relations["sylvian"]>=7:
            jump S3_sylvian_good_end

label S3_sylvian_bad_end:
    
    play music "track_4_time_stop.ogg" fadeout 2.0 fadein 2.0
    
    show sylvian blush at center with dissolve

    "I should poke further about his comment."

    "It might get him a bit ruffled up but I can't contain my curiosity. It wouldn't hurt to tease him a little."

    show lars blush
    Lars "How long have you harbored these romantic thoughts, Master? I recall you mentioning that entertaining the idea of such a relationship between you and me was, as you put it... {i}unethical{/i}."

    show sylvian sad
    show lars blush
    Sylvian "Oh, did I really say that? Y-you can dismiss— um... I mean, feel free to forget what I just said. It was rather foolish— an error on my part to make such a bold declaration."

    show lars blush
    Lars "Pfft, are you feeling alright? Did the concoction not calm your nerves like you wanted?"

    "A snort escapes me, the sound cutting through the air like a fleeting burst of amusement. Yet, instead of joining in laughter, Master Sylvian abruptly falls silent, his features tightening as he begins to bite his lips."

    show sylvian sad at shake
    show lars blush
    Sylvian "No, nothing of the sort. I-I was simply taken aback because I didn't anticipate your reaction. I suppose it's because I've become accustomed to how you always manage to say the right thing."

    show lars blush
    Sylvian "It's a bit difficult for my heart when you openly point out the things I keep trying to keep concealed..."

    show lars blush
    Lars "There's a limit to discretion, Master. I mean, not everyone is oblivious enough to not notice how you treat me differently than the others."

    show lars blush
    Lars "When did it start? How did you feel when I took your hand in front of Zephyr? I always see dragons cuddling and playing around with their mate, do you also have such thoughts—"

    show sylvian sad at jp
    show lars sad
    Sylvian "{size=*2.0}[Lars]!" with vpunch

    show lars sad
    Sylvian "Y-you can't say such a thing out loud! Or better yet, why would y-you... or no, my mind can't take this anymore-"
    
    show sylvian sad at shake
    pause 0.5
    show sylvian sad at shake
    pause 0.5
    show lars blush
    "Poor Master Sylvian, his delicate feathers appear tousled, as if on the brink of unraveling at any given moment."

    show sylvian sad with dissolve:
        xzoom -1.0
    show lars
    Sylvian "You've never acted like this before."

    Lars "I could say the same for you. You're usually the one guiding us as the leader, giving instructions on what to do and what to avoid."

    Lars "Now, it seems like you've taken matters into your own hands for the first time."

    show sylvian sad at right with move:
    show lars
    Sylvian "So, what you're saying is, this {i}boldness{/i} doesn't quite align with my usual demeanor?"

    Lars "More or less. This just means that I brought you along for nothing. You could say I shouldn't have taken your hand back there."

    show lars
    Sylvian "{size=*0.90}...for nothing?"

    "If my eyes weren't mistaken, it almost seemed like Master Sylvian was pouting. His eyes squinted in contemplation, and his petite beard scrunched up."

    "A subtle furrow creased his brow, casting an endearing yet troubled expression across his features."
    
    show lars
    Sylvian "Tell me [Lars], is that really what you mean?"

    Lars "Come on, Master. It's really not that serious."

    Lars "You've already done what was needed and sorted out a secret scoop to share with Zephyr."

    "Contrary to my expectations, praising him doesn't seem to work. Instead of the anticipated joy, his pout deepens. The corners of his eyes seem to glisten as tears start to well up."

    show lars
    Sylvian "I suppose... it was my mistake to have expected more, I shouldn't have indulged in my greed."

    Lars "Haha, what are you talking about, Master? Or were you planning on doing a secret confession since the beginning or something?"

    "The lack of a response urges me to stick to my earlier strategy and poke him even further."

    Lars "Or could it be- is that why you sorted the gossip deal beforehand?"

    "A heavy silence lingers, seems like we're in quite an awkward situation..."

    play music "track_9_bad_ending.ogg" fadeout 2.0 fadein 2.0

    show lars serious
    Sylvian "I-I-I... need to leave— I need to get out of here!"

    hide sylvian sad with moveoutright
    
    "He flutters his large swan wings open causing his feathers to ruffle. They catch the cold hues of the afternoon sun as he lifts off the ground, soaring into the sky."
    
    "The sudden display captures Zephyr's attention, prompting him to shout out."

    voice "audio/voice/zephyr/zephyr_094_take02.ogg"
    show zephyr sad with dissolve:
        xzoom 1
        linear 1.0 xalign 0.5
    
    Zephyr "{size=*1.5}SMARTY!" with vpunch
    show zephyr at jp
    voice "audio/voice/zephyr/zephyr_095_take02.ogg"
    show lars serious
    Zephyr "Where do you think you're going?! You have to give me some gossip material first!"

    voice "audio/voice/zephyr/zephyr_096_take02.ogg"
    show lars serious
    Zephyr "{size=*1.25}I'm not letting you get away!"

    hide zephyr sad with dissolve
    show spotsy with dissolve

    "But before he has the chance to grumble any further, I swiftly move to the spot where Spotsy is resting."
    
    "Smoothly climbing onto her back, I feel the afternoon air gently bristling against my fur."

    show smoke
    "Spotsy responds with a subtle shiver and releases a puff of smoke as if bracing herself for the impending journey."

    voice "audio/voice/zephyr/zephyr_097_take02.ogg"
    show lars serious
    Zephyr "Ouch, were you planning on blinding me with that glitter-bomb breath of yours?!"

    "Now's not the time to humor him, unfortunately."

    hide smoke
    hide spotsy

    show zephyr sad at center with dissolve:
        yalign 0
    show lars serious
    Lars "I'm going to need your help, Spotsy."

    voice "audio/voice/zephyr/zephyr_098_take01.ogg"
    show zephyr sad at shake
    show lars serious
    Zephyr "Hey! When did I allow you guys to leave without my permission?! Hohoho, I'm going to make you pay for-"

    hide zephyr sad with moveoutbottom

    play sound sfx_smack
    "A thwacking sound instantly rings in the air and I look back to see that our not-so-friendly ghost has been knocked to the ground looking completely unconscious."

    show spotsy with dissolve
    show lars serious
    Lars "Normally, I'd have to give you a scolding for smacking people like that, Spotsy. But there's something more important at stake now."

    show smoke
    "She murmurs and wags her tail back and forth- most likely the instrument of the crime behind Zephyr's unexpected tumble."

    show lars serious
    Lars "Can you please follow after Master Sylvian?"

    show lars narration
    hide spotsy
    hide smoke
    with dissolve

    scene bg black with fade
    show bg_4 at up_pan

    "Spotsy instantly fluffs up her wings, taking flight. The ocean gradually shrinks beneath us as we ascend into the sky."
    
    show bg_4 at end_pan

    scene bg black with fade
    show bg_7 at pan

    play music "track_8_neutral_ending.ogg" fadeout 2.0 fadein 2.0

    "We glide through billowy clouds, soft as cotton candy, as the world below turns into a distant patchwork of greens and blues."

    "The air feels crisp, the wind hums gently, and the sun bathes the clouds in hues of pink and blue, creating a tranquil haven above the world."

    "Soon enough, the familiar figure of the slender magician comes into view. His silhouette, somewhat hunched at the neck but always rising to the occasion, is cross-legged at the top of a cloud."

    "Wilting flowers have blossomed around him, bowing down in a withering manner mirroring the posture of Master Sylvian himself."

    show bg_7 at end_pan

    Lars "{size=*2.0}MASTER SYLVIAN!" with vpunch
    
    show sylvian sad at right
    with dissolve
    
    show lars serious
    Lars "Can you hear me?"
    
    "I observe his back shrinking even more, without any response coming my way."

    show lars serious
    Lars "If you don't answer, I might just dive into the cloud you're lounging on the count of three!"

    show lars serious
    Lars "{size=*1.5}ONE!" with vpunch

    show lars serious
    Lars "{size=*1.75}TWO!" with vpunch

    show lars serious
    Lars "{size=*2.0}THREE!" with vpunch

    scene bg black with fade
    show bg_7 with fade

    show bg_7:
        easein 0.2 yoffset -10
        easeout 0.2 yoffset 0
        easein 0.2 yoffset 10
        easeout 0.2 yoffset 0
    
    "Determined, I leap off Spotsy's back, ready to embrace the uncertainty of landing on the cloud's flowery spots."
    
    "Yet, before I can experience the leap of fate, a flurry of petals swirl beneath my dragon-riding boots, guiding my descent."

    "The petals gracefully direct me towards Master Sylvian, aligning with my steps. As soon as he concludes his incantation, the petals disassemble, leaving me standing seamlessly on the cloud, unfazed by the unconventional landing."

    show sylvian with dissolve
    show sylvian at center with move
    show lars serious
    Sylvian "Why..."

    show lars serious
    Sylvian "Why are you here, [Lars]?"

    show sylvian sad
    show lars serious
    Lars "I was worried for you! You know how I felt, suddenly seeing you fly off like that in the middle of our talk?!" with vpunch
    
    show lars serious
    Lars "Even that ghost-faced Zephyr's soul, if he had one in the first place, left him because of what you did." with vpunch

    show lars sad
    Lars "You didn't need to run away like that..."

    show lars sad
    Sylvian "You're right. I guess I simply wanted to have a moment for myself."

    show lars sad
    Lars "What's going on, Master? This isn't like you at all."

    show sylvian sad with dissolve:
        xzoom -1.0

    show sylvian sad at center_3right with move
    show lars sad
    voice "audio/voice/sylvian/sylvian_095_take01.ogg"
    Sylvian "{i}Discere, cogitare, agere{/i}— the triad of wisdom."

    show sylvian sad at right with move
    show lars sad
    voice "audio/voice/sylvian/sylvian_096_take02.ogg"
    Sylvian "I made that our guild motto while thinking of someone who I had yet to meet."

    show lars sad
    Lars "Uhm, not to interrupt, but is this an appropriate time to talk about this? Shouldn't we get back to Zephyr first?"

    show sylvian sad at shake
    show lars sad
    Sylvian "Is that what you want, [Lars]?"

    show lars sad
    Sylvian "Whatever choice you make, I'll do my best to respect it."

    if options["CS3"]==1:

        show lars sad
        Sylvian "It's unfortunate that I couldn't mirror what's in my heart as I vowed to do for you..."

    show lars
    Lars "To start off... shouldn't we get back on land? I don't want to keep Spotsy flying for too long."

    show sylvian sad at jp
    show lars
    Sylvian "I don't think I'm ready to descend yet..."

    show lars sad
    Lars "Are you upset with me, Master? Did I do something wrong?"

    "His back, crooked and hunched, still remains turned towards me, amplifying the sense that I'm speaking to an impassive wall."
    
    show sylvian mad
    show lars sad
    Sylvian "Certainly not; it's just a product of your imagination."

    "That peculiar expression resurfaces once more. An awkward smile concealing a hidden joke meant solely for his own amusement."

    show lars sad
    Sylvian "I'm just getting upset on my own."

    show lars sad
    Lars "No, it's okay. Just tell me what you need me to do."

    show sylvian sad
    show lars sad
    Sylvian "I-I... don't have the courage to say it out loud."

    show lars sad
    Sylvian "I shouldn't say it to you of all people."

    show lars sad
    Sylvian "Yet, I don't believe my heart can endure any more of this stagnation."

    show lars sad
    Sylvian "The once tumultuous dance of butterflies' wings within my soul has ceased, leaving only the remnants of a storm's aftermath— no longer the enchanting spectacle that it once was."

    show lars 
    Lars "It's never too late to share what's on that brilliant mind of yours. After all, what good is intelligence if you keep it all to yourself?"

    show sylvian sad with dissolve:
        xzoom 1.0

    show lars
    Sylvian "..."

    play music "track_10_bad_ending_2.ogg" fadeout 2.0 fadein 2.0

    show lars blush
    Sylvian "The truth is, [Lars], I can't help but be utterly petrified of the thought of losing you."

    show lars blush
    Sylvian "It's a never-ending battle against the gnawing fear that I'll never quite measure up, never truly be enough for someone like you."

    show lars blush
    Lars "What are you talking about? I'm your confession partner, aren't I? Share those pent-up emotions with me. I'm curious to know what my wise master has been hiding all this time."

    show sylvian sad at shake
    show lars blush
    Sylvian "Considering this is a matter I haven't shared with anyone, I hesitated to speak of it."

    show lars blush
    Sylvian "I kept pulling back whenever my emotions were close to the surface, only to regret it repeatedly in my head, convinced that what I did was wrong."

    show sylvian sad at center with move
    show lars blush
    Sylvian "Curiosity is indeed a virtue, but consider this— what if the object of your curiosity is beyond your reach?"

    show lars blush
    Sylvian "It's a gentle reminder that our aspirations may not always align with our destiny. It is wiser to accept this truth gracefully than to diminish the value of what eludes our grasp."

    show lars sad
    Sylvian "That's... what held me back from loving you the way you deserve."

    show lars sad
    Lars "Why do your words sound so cruel... when you're saying them softly?"

    show lars sad
    Sylvian "Amidst the certainty of truth, lies have found a sanctuary in the hearts of those who chose to believe, even when confronted with undeniable facts."

    show lars sad
    Sylvian "There's an undeniable truth that I've been deluding myself with, but I suppose seeing your bold approach and your general choices today really made me realize the gravity of the situation."

    show lars blush
    Lars "I figured you'd enjoy my response to your subtle flirting. Given the special treatment I've been receiving from you, it only makes sense for me to inquire more about your intentions."

    show sylvian sad at jp
    show lars
    Sylvian "Do you... truly mean that?"

    Lars "Of course, when push comes to shove, all you do is run away. It's quite frustrating I have to say."

    show sylvian sad with dissolve:
        xzoom -1.0

    show lars
    Sylvian "So that's what this is all about..."

    show sylvian sad at right with move
    show lars
    Sylvian "It's clear to me now..."

    show lars
    Sylvian "That's why... I don't think I have the heart to accept your pity, [Lars]. It would be devastating to know that you're wasting your time on someone like me."

    hide sylvian with dissolve 
    show black_feather with dissolve

    "I can see his feathers falling as he walks away, leaving a trail of imprints in the cloud. I try catching them at first, but then I realize he's pulling them himself, intentionally shedding them."
    
    "I start picking them up one by one but the distance between us keeps getting wider and wider. Each feather feels like a piece of something lost, and the air is heavy with the unspoken weight of the moment."
    
    show lars sad
    Lars "You have to stop Master, you're hurting yourself..."
    
    "He gracefully turns back and pulls a single feather from the folds of his wings, idly twirling it between his fingers as if lost in thought."

    hide black_feather with dissolve
    
    show sylvian sad at right with dissolve:
        xzoom -1.0
    show lars sad
    Sylvian "Did you know, [Lars]? Swans form a lifelong bond with a single mate, remaining together until the bond is broken, either by death or if one of them is preyed upon."

    show lars sad
    Sylvian "Concealing this confession might have preserved my existence, but being aware of your pity is a fate no less agonizing than succumbing to heartache."

    show lars sad
    Lars "You can't say something like that, Master! I'm not going to let anything happen to you. I'll protect you-"

    show lars sad
    Sylvian "Some things are just out of our control, [Lars]. Even my escape from the realm of academia was such a tale."

    show lars sad
    Sylvian "..."

    voice "audio/voice/sylvian/sylvian_120_take04.ogg"
    show lars sad
    Sylvian "You should know that I used to adore the academic world."

    voice "audio/voice/sylvian/sylvian_121_take01.ogg"
    show lars sad
    Sylvian "It was the one place where I could marvel over the many intricacies of life without feeling... overwhelmed by my lack of knowledge."
    
    voice "audio/voice/sylvian/sylvian_121_take02.ogg"
    show lars sad
    Sylvian "I would read the many scrolls, books, journals, and whatever I could get my hands on, even in the private library of the Archmage of Divonia who seldom grants people his audience."

    voice "audio/voice/sylvian/sylvian_122_take03.ogg"
    show lars sad
    Sylvian "However... things started to change once I started getting the attention of other academics for my {i}cursed{/i} achievements."

    voice "audio/voice/sylvian/sylvian_123_take04.ogg"
    show lars sad
    Sylvian "Suddenly, it wasn't the endless nights of poring over my notes, hunching my back, and using my feathers as quills to jot down whatever came to mind that wore me out. Instead..."

    voice "audio/voice/sylvian/sylvian_124_take03.ogg"
    show lars sad
    Sylvian "It was the {i}jealousy{/i} and looks of {i}hatred{/i} from my fellow magicians and academics, those whom I yearned to share my thoughts with."

    "His voice starts shaking a little, and I can sense a sob that he's trying to hold down, but his attempts are futile as tears prickle in the corner of his eyes."

    "Here was the descendent whom I had admired as a wise and poetic leader. Yet, all this time, he held such sorrows in his heart, hidden away from everyone."

    voice "audio/voice/sylvian/sylvian_125_take02.ogg"
    show lars sad
    Sylvian "I, who had earned their scorn, was ostracized and couldn't show my face in public anymore because of... because of the nasty slurs they would throw at me."

    voice "audio/voice/sylvian/sylvian_126_take02.ogg"
    show lars sad
    Sylvian "They were intelligent descendants, of course, and would never resort to physical violence if they could do what was needed with their words..."

    voice "audio/voice/sylvian/sylvian_127_take01.ogg"
    show lars sad
    Sylvian "And their words were powerful, [Lars], for I was made to be a lonely swan, simply swimming on a pond with no one's company to enjoy but my own reflection in the water."

    voice "audio/voice/sylvian/sylvian_128_take02.ogg"
    show lars sad
    Sylvian "No voice to hear, but the very ripples of the water I moved on. No one to touch or embrace except... the very wind that seemed to caress my feathers with the breeze. Only through flowers was I able to express myself and find a new path to choose."
    
    show lars sad
    Lars "..."

    voice "audio/voice/sylvian/sylvian_129_take02.ogg"
    show sylvian with dissolve
    show lars sad
    Sylvian "I've always adored flowers; why they take on certain colors, where to cultivate them, it {i}all{/i} fascinates me."

    voice "audio/voice/sylvian/sylvian_130_take02.ogg"
    show lars sad
    Sylvian "When I care for them, they bloom. They leave seeds and produce a new generation of plants. They don't concern themselves with my past and never leave my side. They reciprocate what I give them, and I revel in being spoiled by their unintentional kindness."

    voice "audio/voice/lars/lars_153_take02.ogg"
    show lars serious
    Lars "So all this time, you had lost your self-confidence because of a bunch of know-it-alls who couldn't bear to see you succeed?!"

    show lars
    Sylvian "That's a unique way to phrase it indeed."

    Lars "But it's in the past now, isn't it Master?"

    Lars "How about I give you some self-confidence tips once all this is over? I ought to do at least that much as your junior. So don't mope around anymore like this; getting upset and crying certainly doesn't suit a leader like you."

    show sylvian sad
    show lars
    Sylvian "But there's no point to it anymore..."

    show lars blush
    Lars "Awe, are you saying that because I teased you about your love confession idea earlier? I mean, I appreciate that you trusted me enough to share your thoughts, but I guess, seeing my choices today-"

    show lars sad
    Sylvian "I don't think I can bear to listen to you, [Lars]..."

    show sylvian sad with dissolve:
        xzoom -1.0

    show lars sad
    Sylvian "I don't think I can bear to listen to anyone from this point on."

    show lars sad
    Sylvian "I... I think I'd prefer some time alone to gather my thoughts."

    show lars serious
    Lars "What're you talking about? Who's going to take care of the guild without you? What's going to happen to Zephyr and the rest of the people captured by him?"

    play music "track_8_neutral_ending.ogg" fadeout 2.0 fadein 2.0

    show lars serious
    Sylvian "I'll provide him with the necessary information. Sharing a couple of magician secrets won't be much trouble."

    voice "audio/voice/lars/lars_167_take02.ogg"
    show lars sad
    Lars "But won't that tarnish your reputation?"

    show sylvian with dissolve:
        xzoom 1.0

    voice "audio/voice/sylvian/sylvian_148_take04.ogg"
    show lars serious
    Sylvian "Ah, no need to worry. The Archmage will have silenced him long before any reputable gossip columns consider his story. He doesn't tolerate his academics engaging in such... {i}activities{/i}."

    voice "audio/voice/lars/lars_196_take01.ogg"
    show lars serious
    Lars "What about the artifact under Zephyr's control and the trapped descendants?"

    voice "audio/voice/sylvian/sylvian_149_take03.ogg"
    show lars serious
    Sylvian "I'm confident Claude and my dear junior, Rory, have already handled that."

    voice "audio/voice/sylvian/sylvian_150_take01.ogg"
    show lars serious
    Sylvian "I gave her instructions before she started her private puppet show with Zephyr earlier today, and with Claude's extensive connections, he's likely found a solution to ease all your concerns."

    voice "audio/voice/sylvian/sylvian_151_take01.ogg"
    show lars serious
    Sylvian "They are capable members of the guild, after all."

    play music "track_10_bad_ending_2.ogg" fadeout 2.0 fadein 2.0

    show sylvian sad
    Sylvian "Much better than their pathetic excuse of a guild leader..."

    show lars sad
    Lars "Master..."

    show lars sad
    Sylvian "I suppose it was an unattainable goal to desire more. I dreamt of it and lost what was already in my grasp."

    "His eyes drop. Everything happened so quickly, in a way I never saw coming. Maybe he'd made up his mind before I could react, or perhaps my choices led us here."
    
    "I simply stare at him, feeling utterly helpless."

    "I wish for him to meet my gaze once more, but I fear he won't lift his head again."

    show sylvian sad with dissolve:
        xzoom -1.0
    
    show lars sad
    Sylvian "Who knows... if this feeling will eventually pass or not."

    show lars sad
    Sylvian "Who knows... if I'll ever be worthy of love again."

    $ renpy.choice_for_skipping()
    $ persistent.ending[2] = 1
    scene bg black with fade
    "" "Sylvian - Bad End Achieved"
    jump end

label S3_sylvian_neutral_end:

    play music "track_4_time_stop.ogg" fadeout 2.0 fadein 2.0
    
    show sylvian blush at center with dissolve
    "I should move past his comment."

    "There are more pressing matters at hand."

    show sylvian sad
    show lars
    Lars "We can discuss that later, Master Sylvian."

    show lars
    Sylvian "Oh, is that so? Y-you can dismiss— um... I mean, feel free to forget what I just said. It was rather foolish— an error on my part to make such a bold declaration."

    Lars "Are you feeling alright? Did the tonic not calm your nerves like you wanted?"

    show lars
    Sylvian "No, nothing of the sort. I-I was simply taken aback because I didn't anticipate your reaction. I suppose it's because I've become accustomed to how you always manage to say the right thing."

    Lars "That's nice and all, but I'm not some mind reader, Master."
    
    Lars "You should just outright tell me what you want instead of looking for things that may not exist."

    show lars
    Sylvian "..."

    show sylvian sad with dissolve:
        xzoom -1.0
        pause 1.0
    show sylvian sad at center_3right with move
    show lars
    Sylvian "I suppose you're right. True power comes from within, and those who seek it elsewhere are merely fooling themselves."

    Lars "Exactly. I mean, you've already taken care of this Zephyr dilemma as best as you could, mostly by yourself."

    Lars "This just means that I brought you along for nothing. You could say I shouldn't have taken your hand back there."

    show lars
    Sylvian "... for nothing?"

    "If my eyes weren't mistaken, it almost seemed like Master Sylvian was pouting. His eyes squinted in contemplation, and his petite beard scrunched up."

    "A subtle furrow creased his brow, casting an endearing yet troubled expression across his features."

    show lars
    Sylvian "Tell me [Lars], is that really what you mean?"

    Lars "Come on, Master. It's really not that serious."

    show lars
    Sylvian "I suppose... it was my mistake to have expected more, I shouldn't have indulged in my greed."

    show lars
    Lars "Haha, what are you talking about, Master? Or were you planning on doing a secret confession since the beginning or something?"

    "The lack of a response urges me to stick to my earlier strategy and pass over his comment again."

    show lars
    Lars "Or could it be- is that why you sorted the gossip deal beforehand?"

    "A heavy silence lingers, seems like we're in quite an awkward situation..."

    play music "track_9_bad_ending.ogg" fadeout 2.0 fadein 2.0

    show lars serious
    Sylvian "I-I-I... need to leave— I need to get out of here!"

    hide sylvian sad with moveoutright
    
    "He flutters his large swan wings open causing his feathers to ruffle. They catch the cold hues of the afternoon sun as he lifts off the ground, soaring into the sky."
    
    "The sudden display captures Zephyr's attention, prompting him to shout out."

    voice "audio/voice/zephyr/zephyr_094_take02.ogg"
    show zephyr sad with dissolve:
        xzoom 1
        linear 1.0 xalign 0.5
    
    Zephyr "{size=*1.5}SMARTY!" with vpunch
    show zephyr at jp
    voice "audio/voice/zephyr/zephyr_095_take02.ogg"
    show lars serious
    Zephyr "Where do you think you're going?! You have to give me some gossip material first!"

    voice "audio/voice/zephyr/zephyr_096_take02.ogg"
    show lars serious
    Zephyr "{size=*1.25}I'm not letting you get away!"

    hide zephyr sad with dissolve
    show spotsy with dissolve

    "But before he has the chance to grumble any further, I swiftly move to the spot where Spotsy is resting."
    
    "Smoothly climbing onto her back, I feel the afternoon air gently bristling against my fur."

    show smoke
    "Spotsy responds with a subtle shiver and releases a puff of smoke as if bracing herself for the impending journey."

    voice "audio/voice/zephyr/zephyr_097_take02.ogg"
    show lars serious
    Zephyr "Ouch, were you planning on blinding me with that glitter-bomb breath of yours?!"

    "Now's not the time to humor him, unfortunately."

    hide smoke
    hide spotsy

    show zephyr sad at center with dissolve:
        yalign 0
    show lars serious
    Lars "I'm going to need your help, Spotsy."

    voice "audio/voice/zephyr/zephyr_098_take01.ogg"
    show zephyr sad at shake
    show lars serious
    Zephyr "Hey! When did I allow you guys to leave without my permission?! Hohoho, I'm going to make you pay for-"

    hide zephyr sad with moveoutbottom

    play sound sfx_smack
    "A thwacking sound instantly rings in the air and I look back to see that our not-so-friendly ghost has been knocked to the ground looking completely unconscious."

    show spotsy with dissolve
    show lars serious
    Lars "Normally, I'd have to give you a scolding for smacking people like that, Spotsy. But there's something more important at stake now."

    show smoke
    "She murmurs and wags her tail back and forth- most likely the instrument of the crime behind Zephyr's unexpected tumble."

    show lars serious
    Lars "Can you please follow after Master Sylvian?"

    show lars narration
    hide spotsy
    hide smoke
    with dissolve

    scene bg black with fade
    show bg_4 at up_pan

    "Spotsy instantly fluffs up her wings, taking flight. The ocean gradually shrinks beneath us as we ascend into the sky."
    
    show bg_4 at end_pan

    scene bg black with fade
    show bg_7 at pan

    play music "track_8_neutral_ending.ogg" fadeout 2.0 fadein 2.0

    "We glide through billowy clouds, soft as cotton candy, as the world below turns into a distant patchwork of greens and blues."

    "The air feels crisp, the wind hums gently, and the sun bathes the clouds in hues of pink and blue, creating a tranquil haven above the world."

    "Soon enough, the familiar figure of the slender magician comes into view. His silhouette, somewhat hunched at the neck but always rising to the occasion, is cross-legged at the top of a cloud."

    "Wilting flowers have blossomed around him, bowing down in a withering manner mirroring the posture of Master Sylvian himself."

    show bg_7 at end_pan

    Lars "{size=*2.0}MASTER SYLVIAN!" with vpunch
    
    show sylvian sad at right
    with dissolve
    
    show lars serious
    Lars "Can you hear me?"
    
    "I observe his back shrinking even more, without any response coming my way."

    show lars serious
    Lars "If you don't answer, I might just dive into the cloud you're lounging on the count of three!"

    show lars serious
    Lars "{size=*1.5}ONE!" with vpunch

    show lars serious
    Lars "{size=*1.75}TWO!" with vpunch

    show lars serious
    Lars "{size=*2.0}THREE!" with vpunch

    scene bg black with fade
    show bg_7 with fade

    show bg_7:
        easein 0.2 yoffset -10
        easeout 0.2 yoffset 0
        easein 0.2 yoffset 10
        easeout 0.2 yoffset 0
    
    "Determined, I leap off Spotsy's back, ready to embrace the uncertainty of landing on the cloud's flowery spots."
    
    "Yet, before I can experience the leap of fate, a flurry of petals swirl beneath my dragon-riding boots, guiding my descent."

    "The petals gracefully direct me towards Master Sylvian, aligning with my steps. As soon as he concludes his incantation, the petals disassemble, leaving me standing seamlessly on the cloud, unfazed by the unconventional landing."

    show sylvian with dissolve
    show sylvian at center with move
    show lars serious
    Sylvian "Why..."

    show lars serious
    Sylvian "Why are you here, [Lars]?"

    show sylvian sad with dissolve
    show lars serious
    Lars "I was worried for you! You know how I felt, suddenly seeing you fly off like that in the middle of our talk?!" with vpunch
    
    show lars serious
    Lars "Even that ghost-faced Zephyr's soul, if he had one in the first place, left him because of what you did." with vpunch

    show lars sad
    Lars "You didn't need to run away like that..."

    show sylvian sad with dissolve
    show lars sad
    Sylvian "You're right. I guess I simply wanted to have a moment for myself."

    show lars sad
    Lars "What's going on, Master? This isn't like you at all."

    show sylvian sad with dissolve:
        xzoom -1.0

    show sylvian sad at center_3right with move
    show lars sad
    voice "audio/voice/sylvian/sylvian_095_take01.ogg"
    Sylvian "{i}Discere, cogitare, agere{/i}— the triad of wisdom."

    show sylvian sad at right with move
    show lars sad
    voice "audio/voice/sylvian/sylvian_096_take02.ogg"
    Sylvian "I made that our guild motto while thinking of someone who I had yet to meet."

    show lars sad
    Lars "Uhm, not to interrupt, but is this an appropriate time to talk about this? Shouldn't we get back to Zephyr first?"

    show sylvian sad at shake
    show lars sad
    Sylvian "Is that what you want, [Lars]?"

    show lars sad
    Sylvian "Whatever choice you make, I'll do my best to respect it."

    if options["CS3"]==1:

        show lars sad
        Sylvian "It's unfortunate that I couldn't mirror what's in my heart as I vowed to do for you..."

    show lars
    Lars "To start off... shouldn't we get back on land? I don't want to keep Spotsy flying for too long."

    show sylvian sad at jp
    show lars
    Sylvian "I don't think I'm ready to descend yet..."

    show lars sad
    Lars "Are you upset with me, Master? Did I do something wrong?"

    "His back, crooked and hunched, still remains turned towards me, amplifying the sense that I'm speaking to an impassive wall."
    
    show sylvian mad with dissolve
    show lars sad
    Sylvian "Certainly not; it's just a product of your imagination."

    "That peculiar expression resurfaces once more. An awkward smile concealing a hidden joke meant solely for his own amusement."

    show lars sad
    Sylvian "I'm just getting upset on my own."

    show lars sad
    Lars "No, it's okay. Just tell me what you need me to do."

    show sylvian sad with dissolve
    show lars sad
    Sylvian "I-I... don't have the courage to say it out loud."

    show lars sad
    Sylvian "I shouldn't say it to you of all people."

    show lars sad
    Sylvian "Yet, I don't believe my heart can endure any more of this stagnation."

    show lars sad
    Sylvian "The once tumultuous dance of butterflies' wings within my soul has ceased, leaving only the remnants of a storm's aftermath— no longer the enchanting spectacle that it once was."

    show lars 
    Lars "It's never too late to share what's on that brilliant mind of yours. After all, what good is intelligence if you keep it all to yourself?"

    show sylvian sad with dissolve:
        xzoom 1.0

    show lars blush
    Sylvian "..."

    play music "track_10_bad_ending_2.ogg" fadeout 2.0 fadein 2.0

    show lars blush
    Sylvian "The truth is, [Lars], I can't help but be utterly petrified of the thought of losing you."

    show lars blush
    Sylvian "It's a never-ending battle against the gnawing fear that I'll never quite measure up, never truly be enough for someone like you."

    show lars 
    Lars "Is this what's it all about? I'm your friend, aren't I? We already talked about this, you shouldn't be undermining yourself like this."

    show lars 
    Sylvian "Ah, just as a friend, is that right..."

    show lars 
    Sylvian "Well, I suppose it's my fault too since I never had the courage to state what was in my heart... that's precisely why I hesitated to speak of it."

    show lars 
    Sylvian "Then again, even the title of a {i}'friend'{/i} might be too much for a coward like me."

    "Coward? Does Master Sylvian really think of himself like that... ?"

    show lars 
    Sylvian "Amidst the certainty of truth, lies have found a sanctuary in the hearts of those who chose to believe, even when confronted with undeniable facts."

    show lars 
    Sylvian "There's an undeniable truth that I've been deluding myself with, but I suppose having you pass over my comment and your general choices today really made me realize the gravity of the situation."

    show lars serious
    Lars "But I had a reason behind passing over what you said, because there are more important things at stake here."

    show lars serious
    Lars "Balancing numerous responsibilities and ensuring the well-being of those around me is a priority. Seeing both descendants and humans smile while under my care is what fills me with joy."

    show lars sad
    Lars "That's why, while I understand where your romantic intentions are coming from, I can't give you a response right now amidst all this drama. I still–"

    show sylvian sad with dissolve:
        xzoom -1.0

    show sylvian sad at right with move
    show lars sad
    Sylvian "Is that so..."

    show lars sad
    Sylvian "You know [Lars]... In my pursuit of profound truths, I found myself chasing the distant winds, oblivious to the wisdom carried by the nearby breeze."

    show sylvian sad with dissolve:
        xzoom 1.0

    show lars sad
    Sylvian "I sought friendship as if it were a dream, blind to the companionship that surrounded me, even if it fell short of the true friendship I imagined day and night."

    show sylvian sad at center with move
    show lars sad
    Sylvian "Such is the nature of existence, where I must accept what is, for I cannot alter the course of destiny."
    
    show lars sad
    Sylvian "I should have... simply been satisfied with what was in the palm of my hand instead of yearning for more."

    show lars sad
    Sylvian "That's why... I don't think I have the heart to accept your pity, [Lars]. This is the fate that I must accept for I am worthy of no other"

    hide sylvian with dissolve 
    show black_feather with dissolve

    "I can see his feathers falling as he walks away, leaving a trail of imprints in the cloud. I try catching them at first, but then I realize he's pulling them himself, intentionally shedding them."
    
    "I start picking them up one by one but the distance between us keeps getting wider and wider. Each feather feels like a piece of something lost, and the air is heavy with the unspoken weight of the moment."
    
    show lars sad
    Lars "You have to stop Master, you're hurting yourself..."
    
    "He gracefully turns back and pulls a single feather from the folds of his wings, idly twirling it between his fingers as if lost in thought."

    hide black_feather with dissolve
    
    show sylvian sad at right with dissolve:
        xzoom -1.0
    show lars sad
    Sylvian "Did you know, [Lars]? Swans form a lifelong bond with a single mate, remaining together until the bond is broken, either by death or if one of them is preyed upon."

    show lars sad
    Sylvian "Concealing this confession might have preserved my existence, but being aware of your pity is a fate no less agonizing than succumbing to heartache."

    show lars sad
    Lars "You can't say something like that, Master! I'm not going to let anything happen to you. I'll protect you-"

    show lars sad
    Sylvian "Some things are just out of our control, [Lars]. Even my escape from the realm of academia was such a tale."

    show lars sad
    Sylvian "..."

    voice "audio/voice/sylvian/sylvian_120_take04.ogg"
    show lars sad
    Sylvian "You should know that I used to adore the academic world."

    voice "audio/voice/sylvian/sylvian_121_take01.ogg"
    show lars sad
    Sylvian "It was the one place where I could marvel over the many intricacies of life without feeling... overwhelmed by my lack of knowledge."
    
    voice "audio/voice/sylvian/sylvian_121_take02.ogg"
    show lars sad
    Sylvian "I would read the many scrolls, books, journals, and whatever I could get my hands on, even in the private library of the Archmage of Divonia who seldom grants people his audience."

    voice "audio/voice/sylvian/sylvian_122_take03.ogg"
    show lars sad
    Sylvian "However... things started to change once I started getting the attention of other academics for my {i}cursed{/i} achievements."

    voice "audio/voice/sylvian/sylvian_123_take04.ogg"
    show lars sad
    Sylvian "Suddenly, it wasn't the endless nights of poring over my notes, hunching my back, and using my feathers as quills to jot down whatever came to mind that wore me out. Instead..."

    voice "audio/voice/sylvian/sylvian_124_take03.ogg"
    show lars sad
    Sylvian "It was the {i}jealousy{/i} and looks of {i}hatred{/i} from my fellow magicians and academics, those whom I yearned to share my thoughts with."

    "His voice starts shaking a little, and I can sense a sob that he's trying to hold down, but his attempts are futile as tears prickle in the corner of his eyes."

    "Here was the descendent whom I had admired as a wise and poetic leader. Yet, all this time, he held such sorrows in his heart, hidden away from everyone."

    voice "audio/voice/sylvian/sylvian_125_take02.ogg"
    show lars sad
    Sylvian "I, who had earned their scorn, was ostracized and couldn't show my face in public anymore because of... because of the nasty slurs they would throw at me."

    voice "audio/voice/sylvian/sylvian_126_take02.ogg"
    show lars sad
    Sylvian "They were intelligent descendants, of course, and would never resort to physical violence if they could do what was needed with their words..."

    voice "audio/voice/sylvian/sylvian_127_take01.ogg"
    show lars sad
    Sylvian "And their words were powerful, [Lars], for I was made to be a lonely swan, simply swimming on a pond with no one's company to enjoy but my own reflection in the water."

    voice "audio/voice/sylvian/sylvian_128_take02.ogg"
    show lars sad
    Sylvian "No voice to hear, but the very ripples of the water I moved on. No one to touch or embrace except... the very wind that seemed to caress my feathers with the breeze. Only through flowers was I able to express myself and find a new path to choose."
    
    show lars sad
    Lars "..."

    voice "audio/voice/sylvian/sylvian_129_take02.ogg"
    show sylvian
    show lars sad
    Sylvian "I've always adored flowers; why they take on certain colors, where to cultivate them, it {i}all{/i} fascinates me."

    voice "audio/voice/sylvian/sylvian_130_take02.ogg"
    show lars sad
    Sylvian "When I care for them, they bloom. They leave seeds and produce a new generation of plants. They don't concern themselves with my past and never leave my side. They reciprocate what I give them, and I revel in being spoiled by their unintentional kindness."

    voice "audio/voice/lars/lars_153_take02.ogg"
    show lars serious
    Lars "So all this time, you had lost your self-confidence because of a bunch of know-it-alls who couldn't bear to see you succeed?!"

    show lars
    Sylvian "That's a unique way to phrase it indeed."

    Lars "But it's in the past now, isn't it Master?"

    Lars "How about I give you some self-confidence tips once all this is over? I ought to do at least that much as your junior. So don't mope around anymore like this; getting upset and crying certainly doesn't suit a leader like you."

    show sylvian sad
    show lars
    Sylvian "I suppose that marks my confession as null."

    Lars "I wouldn't say that. I appreciate your trust in sharing your thoughts with me. However, considering my choices today, I don't think I'm ready..."

    Lars "For now, I believe it's best that we maintain our relationship as Master and Junior... It's a given that I'd want to remain as your friend too."

    show lars
    Sylvian "{size=*0.75}Of course, it should have been like this from the start."
    
    Lars "What was that, Master?"

    show sylvian
    show lars
    Sylvian "N-n-nothing of importance."

    show lars serious
    Lars "Now then, what do we do about Zephyr though?"

    play music "track_8_neutral_ending.ogg" fadeout 2.0 fadein 2.0

    show sylvian serious funny with dissolve
    show lars
    Sylvian "I'll provide him with the necessary information. Sharing a couple of magician secrets won't be much trouble."

    voice "audio/voice/lars/lars_167_take02.ogg"
    show lars sad
    Lars "But won't that tarnish your reputation?"

    show sylvian with dissolve:
        xzoom 1.0

    voice "audio/voice/sylvian/sylvian_148_take04.ogg"
    show lars serious
    Sylvian "Ah, no need to worry. The Archmage will have silenced him long before any reputable gossip columns consider his story. He doesn't tolerate his academics engaging in such... {i}activities{/i}."

    voice "audio/voice/lars/lars_196_take01.ogg"
    show lars serious
    Lars "What about the artifact under Zephyr's control and the trapped descendants?"

    voice "audio/voice/sylvian/sylvian_149_take03.ogg"
    show lars serious
    Sylvian "I'm confident Claude and my dear junior, Rory, have already handled that."

    voice "audio/voice/sylvian/sylvian_150_take01.ogg"
    show lars serious
    Sylvian "I gave her instructions before she started her private puppet show with Zephyr earlier today, and with Claude's extensive connections, he's likely found a solution to ease all your concerns."

    voice "audio/voice/sylvian/sylvian_151_take01.ogg"
    show lars serious
    Sylvian "They are capable members of the guild, after all."

    Lars "That's what friends are for, right? Thanks to them, we ended up with the safest option."

    show sylvian sad with dissolve
    show lars
    Sylvian "Indeed, what an outcome... couldn't have wished for a better one..."

    $ renpy.choice_for_skipping()
    $ persistent.ending[1] = 1
    scene bg black with fade
    " " "Sylvian - Neutral End Achieved"
    jump end

label S3_sylvian_good_end:
    
    play music "track_8_neutral_ending.ogg" fadeout 2.0 fadein 2.0
    
    show sylvian blush at center with dissolve    
    "I should stay silent for now."

    show lars
    Lars "..."

    voice "audio/voice/sylvian/sylvian_092_take04.ogg"
    show lars
    Sylvian "Don't you... wish to know more?"

    "A wistful sigh escapes his lips, followed by a subtle smile."

    voice "audio/voice/lars/lars_135_take01.ogg"
    show lars
    Lars "I didn't want to pressure you into saying something you didn't want to."

    voice "audio/voice/sylvian/sylvian_093_take01.ogg"
    show sylvian blush
    show lars
    Sylvian "... It's simply amazing—"

    voice "audio/voice/sylvian/sylvian_094_take03.ogg"
    show lars blush
    Sylvian "—how effortlessly you make me feel at ease, even in silence."

    voice "audio/voice/sylvian/sylvian_095_take01.ogg"
    show sylvian
    show lars
    Sylvian "{i}Discere, cogitare, agere—{/i} the triad of wisdom."

    voice "audio/voice/sylvian/sylvian_096_take02.ogg"
    show lars
    Sylvian "I made that our guild motto while thinking of someone who I had yet to meet."

    voice "audio/voice/lars/lars_137_take02.ogg"
    Lars "What do you mean, Master?"

    voice "audio/voice/sylvian/sylvian_097_take03.ogg"
    show lars
    Sylvian "Learning enriches the mind, and thinking sharpens it, but it is through action that we truly manifest our knowledge and shape our reality."

    voice "audio/voice/sylvian/sylvian_098_take02.ogg"
    show lars
    Sylvian "In envisioning the principles I wanted to embody, the person I admired played a significant role. Someone who would never hesitate to learn more despite their ever-expanding knowledge. A sharp mind that wouldn't confine itself to merely fulfilling tasks."

    voice "audio/voice/lars/lars_138_take02.ogg"
    Lars "You already embody those ideals, don't you?"

    voice "audio/voice/sylvian/sylvian_099_take01.ogg"
    show lars
    Sylvian "There's still a certain component left for me to achieve — the action needed to manifest knowledge and wit. However, I failed to do that in many ways."

    voice "audio/voice/lars/lars_139_take02.ogg"
    show sylvian blush
    show lars blush
    Lars "You've already done so much, Master! You've always worked very hard for everyone in the guild."

    voice "audio/voice/lars/lars_140_take02.ogg"
    show lars blush
    Lars "You don't need me to tell you this, but... none of the things we do would ever be possible without you."

    voice "audio/voice/sylvian/sylvian_100_take03.ogg"
    show sylvian sad
    show sylvian sad with dissolve:
        xzoom -1.0
    show lars blush
    Sylvian "Surely, it would. Once there's nothing more for me to do, I'll be left alone again, naturally."

    voice "audio/voice/lars/lars_141_take02.ogg"
    show sylvian sad at center_3right with move
    show lars sad
    Lars "You know that isn't true."

    voice "audio/voice/sylvian/sylvian_101_take02.ogg"
    show sylvian sad at right with move
    show lars sad
    Sylvian "It is, though. I speak of cherishing our current contentment, but what value is there in doing so if I'm aimlessly wandering without purpose?"

    voice "audio/voice/lars/lars_142_take02.ogg"
    show lars sad
    Lars "Please, Master, you should know better than to trust those negative thoughts which do you no good."

    voice "audio/voice/lars/lars_143_take02.ogg"
    show sylvian blush
    show sylvian blush at shake
    show lars blush
    Lars "You're the one who consistently leads us on our expeditions, the very leader who keeps our guild afloat."

    voice "audio/voice/lars/lars_144_take01.ogg"
    show sylvian blush with dissolve:
        xzoom 1.0

    show lars blush
    Lars "Not to mention, the warm welcome you give us whenever we return, that feeling of being home wouldn't work out with anyone else! Do you understand what I mean right now?"

    voice "audio/voice/sylvian/sylvian_102_take01.ogg"
    show sylvian blush at center_3right with move
    show lars blush
    Sylvian "You're a good one, aren't you, [Lars]?"

    voice "audio/voice/sylvian/sylvian_103_take03.ogg"
    show sylvian blush at center with move
    show lars blush
    Sylvian "Makes me want you for myself even more..."

    voice "audio/voice/lars/lars_145_take01.ogg"
    show lars happy
    Lars "Master... I-I feel the same way—"

    play music "track_10_bad_ending_2.ogg" fadeout 2.0 fadein 2.0 

    voice "audio/voice/sylvian/sylvian_104_take03.ogg"
    show sylvian sad
    show lars happy
    Sylvian "I know I'm not worthy of your attention. You're probably saying those things because I'm your superior, am I right?"

    voice "audio/voice/lars/lars_146_take01.ogg"
    show lars serious
    Lars "Why entertain such thoughts when I'm telling you myself? So, just listen to me, and don't let those negative thoughts confuse your mind!"

    "It may be a tad late, but my ears are curling up from the embarrassment of it all."

    show sylvian blush
    show lars happy
    Sylvian "[Lars]..."

    "Despite his academic brilliance, he seems to struggle with recognizing his own worth. It's time for me to be straightforward with him."

    voice "audio/voice/sylvian/sylvian_105_take02.ogg"
    show lars happy
    Sylvian "The value of companionship, even in its simplest form, should not be dismissed."

    voice "audio/voice/sylvian/sylvian_106_take01.ogg"
    show lars happy
    Sylvian "But... what if I told you I don't want to be only your friend anymore? What if I want to reach out for something more?"

    if options["CS3"]==1:

        show lars blush
        Sylvian "You inquired about the meaning behind the flowers and poems I've shared with you, didn't you? I made a promise to lay my heart bare, and I can't muster the courage to keep my secrets from you any longer."

        show lars blush
        Sylvian "“Between the mirror and the heart is this single difference: The heart conceals secrets, while the mirror does not.”"

        show sylvian blush at shake
        show lars blush
        Sylvian "It's time for me to show you what truly reflects in my heart."

        "His hands are clenched tight, and the rhythmic rise and fall of his Adam's apple mirrors his palpable anxiety."

        show sylvian blush
        show lars blush
        Sylvian "Perhaps you've even picked up on some of my clues by now."

        show lars blush
        Lars "I-I don't know when I started noticing your gifts and how they were specific to me."

        show sylvian sad
        show lars sad 
        Sylvian "That's to be expected, of course. It's my fault that—"

        show sylvian blush
        show lars blush
        Lars "But I always felt special when you gave them to me, as if we had this unbreakable bond that was only between the two of us."

        show lars blush
        Lars "Even today, when you gave me that bouquet for my safe return. I may not be well-versed in the art of flower arrangement or knowledgeable in their names and meanings, but I can always appreciate the effort you put into preparing them."

        show sylvian
        show lars blush 
        Sylvian "I'm curious to see how you'd respond if you knew the meaning behind those flowers. Attaching significance to things that may not hold as much meaning for others has been my unfortunate philosophy for some time now."

        show lars blush
        Lars "Why don't you tell me? I'm curious to know. Maybe I could even share it with my dragons next time around."

        show sylvian sad
        show lars blush
        Sylvian "I've always held an envy of the way they held your attention. There were even days where I dreamt I could replace them and be the sole recipient of your attention."

        show lars blush
        Sylvian "Yet, I fear you might see me as someone who has lost his mind."

        "His unexpected boldness takes me by surprise. Whether it's the influence of the earlier drink or a newfound resolve, his declaration resonates within me. My heart pounds louder, with my tail mirroring its pulse."

    if options["CS3"]==2:

        show sylvian sad with dissolve
        show lars sad
        Sylvian "In reality, you inquired Claude about a potential gift, right? It pains me to realize that everything I've given so far may never measure up to what he could potentially offer."

        show lars sad
        Lars "You shouldn't bring yourself down like that."

        show lars
        Lars "I asked Sir Claude because that's what I was curious about most at that moment."

        show sylvian mad with dissolve
        show lars sad
        Sylvian "I understand, [Lars]. There's no need for you to explain yourself. You're free to pick and do what you want."

        show sylvian sad with dissolve
        show lars sad
        Sylvian "I was simply scolding myself..."
    
    show sylvian sad with dissolve
    "Soon enough though, an awkward silence envelops the air. Even someone as clueless as Zephyr turns back to look at us and see what's going on."
    
    "But before he has the chance to say anything, A sigh escapes Master Sylvian as he slowly shakes his head, lifting his gaze to the expanse of the stars."

    show lars sad
    Sylvian "..."

    voice "audio/voice/sylvian/sylvian_120_take04.ogg"
    show lars sad
    Sylvian "You should know that I used to adore the academic world."

    voice "audio/voice/sylvian/sylvian_121_take01.ogg"
    show lars sad
    Sylvian "It was the one place where I could marvel over the many intricacies of life without feeling... overwhelmed by my lack of knowledge."
    
    voice "audio/voice/sylvian/sylvian_121_take02.ogg"
    show lars sad
    Sylvian "I would read the many scrolls, books, journals, and whatever I could get my hands on, even in the private library of the Archmage of Divonia who seldom grants people his audience."

    voice "audio/voice/sylvian/sylvian_122_take03.ogg"
    show lars sad
    Sylvian "However... things started to change once I started getting the attention of other academics for my {i}cursed{/i} achievements."

    voice "audio/voice/sylvian/sylvian_123_take04.ogg"
    show lars sad
    Sylvian "Suddenly, it wasn't the endless nights of poring over my notes, hunching my back, and using my feathers as quills to jot down whatever came to mind that wore me out. Instead..."

    voice "audio/voice/sylvian/sylvian_124_take03.ogg"
    show lars sad
    Sylvian "It was the {i}jealousy{/i} and looks of {i}hatred{/i} from my fellow magicians and academics, those whom I yearned to share my thoughts with."

    "His voice starts shaking a little, and I can sense a sob that he's trying to hold down, but his attempts are futile as tears prickle in the corner of his eyes."

    "Here was the descendent whom I had admired as a wise and poetic leader. Yet, all this time, he held such sorrows in his heart, hidden away from everyone."

    voice "audio/voice/sylvian/sylvian_125_take02.ogg"
    show lars sad
    Sylvian "I, who had earned their scorn, was ostracized and couldn't show my face in public anymore because of... because of the nasty slurs they would throw at me."

    voice "audio/voice/sylvian/sylvian_126_take02.ogg"
    show lars sad
    Sylvian "They were intelligent descendants, of course, and would never resort to physical violence if they could do what was needed with their words..."

    voice "audio/voice/sylvian/sylvian_127_take01.ogg"
    show lars sad
    Sylvian "And their words were powerful, [Lars], for I was made to be a lonely swan, simply swimming on a pond with no one's company to enjoy but my own reflection in the water."

    voice "audio/voice/sylvian/sylvian_128_take02.ogg"
    show lars sad
    Sylvian "No voice to hear, but the very ripples of the water I moved on. No one to touch or embrace except... the very wind that seemed to caress my feathers with the breeze. Only through flowers was I able to express myself and find a new path to choose."
    
    show lars sad
    Lars "..."

    voice "audio/voice/sylvian/sylvian_129_take02.ogg"
    show sylvian with dissolve
    show lars sad
    Sylvian "I've always adored flowers; why they take on certain colors, where to cultivate them, it {i}all{/i} fascinates me."

    voice "audio/voice/sylvian/sylvian_130_take02.ogg"
    show lars sad
    Sylvian "When I care for them, they bloom. They leave seeds and produce a new generation of plants. They don't concern themselves with my past and never leave my side. They reciprocate what I give them, and I revel in being spoiled by their unintentional kindness."

    voice "audio/voice/lars/lars_153_take02.ogg"
    show lars serious
    Lars "So all this time, you had lost your self-confidence because of a bunch of know-it-alls who couldn't bear to see you succeed?! You should have told me this sooner, Master; I would have given them the perfect torching session with Spotsy's help."

    play music "track_8_neutral_ending.ogg" fadeout 2.0 fadein 2.0

    voice "audio/voice/sylvian/sylvian_133_take01.ogg"
    show sylvian blush at jp
    show lars blush
    Sylvian "Hahahaha! [Lars], what would I do without you..." with vpunch

    voice "audio/voice/sylvian/sylvian_134_take01.ogg"
    show lars blush
    Sylvian "I'm glad to have shared these thoughts with you. It's true that I've gained a sense of insecurity from those events."

    voice "audio/voice/sylvian/sylvian_135_take01.ogg"
    show sylvian
    show lars blush
    Sylvian "My solitude used to be a burden I carried alone, but it led me to seek companionship, resulting in the creation of our guild."

    voice "audio/voice/lars/lars_155_take02.ogg"
    show lars
    Lars "It's a common struggle, isn't it? I always feel a bit uneasy when I start boarding people onto a dragon ship, fearing that I might not meet their expectations."

    voice "audio/voice/lars/lars_156_take01.ogg"
    show lars
    Lars "The same goes for taking care of dragons. There's always that doubt about whether I'm doing a good job, and it was no different when we first got Spotsy."

    voice "audio/voice/lars/lars_157_take02.ogg"
    show lars
    Lars "But the key is to overcome those doubts. You're the one who spends the entire day with... well, yourself. So, finding your self-worth from within just makes sense."

    voice "audio/voice/lars/lars_158_take01.ogg"
    show sylvian blush
    show lars blush
    Lars "We'll obviously take care of you whenever we can. Especially me, of course! I'm not dense enough not to pick up on your little shows of affection, especially with how much time we spend together."

    voice "audio/voice/lars/lars_159_take02.ogg"
    show lars blush
    Lars "But... you have to make the final decision yourself on what you want {i}us{/i} to be."

    voice "audio/voice/sylvian/sylvian_136_take01.ogg"
    show sylvian blush at shake
    show lars blush
    Sylvian "I..."

    hide sylvian with dissolve
    
    play music "track_7_good_ending.ogg" fadeout 2.0 fadein 2.0
    
    "I hold my breath in anticipation when suddenly... he wraps me in a solid embrace."
    
    scene bg black with fade
    show cg_lars_sylvian_ge at slow_pan

    "His touch, though sweaty and trembling, carries an irresistible loveliness."
    
    "The subtle bump on his middle finger from his days in academia and the grazings and minor calluses of his palm from his magical experiments all seem to capture my attention."

    "As our fingers entwine, he bestows upon them a gentle kiss, his eyes closing with grace."

    voice "audio/voice/sylvian/sylvian_137_take01.ogg"
    Sylvian "What a joy it is to lean on you at this moment."

    voice "audio/voice/lars/lars_160_take02.ogg"
    show lars narration
    Lars "You'll get to do that even more in the future."

    voice "audio/voice/sylvian/sylvian_138_take01.ogg"
    Sylvian "Even now, this is enough. I'm afraid of being greedy. I saw what it did back when I tried to achieve more."

    voice "audio/voice/lars/lars_161_take02.ogg"
    show lars narration
    Lars "Shhh... there's no need to reminisce on the bad memories."

    voice "audio/voice/sylvian/sylvian_139_take03.ogg"
    Sylvian "Do... do I really deserve to be spoiled by you like this? Is it fine to cherish this moment and aim to have even more momentous occasions like this with you, by my side?"

    scene bg black with fade

    "The fear of meeting his glistening eyes holds me back. I know it will stir my own emotions, yet, for the moment, I must play the role of the steady anchor for this newfound love."

    "He kisses my fingers again, a subtle execution with reverent trembling and closed eyes. There's a slow sensuality about him, and as his gaze creeps up to meet mine, a charged connection lingers in the air."

    "Yet, in the same breath, I feel the beads of sweat on the palm of his hand and the gentle flutter of his long lashes as he rests his head on my chest."

    show cg_lars_sylvian_ge with fade:
        xalign 0.5
        yalign 0.5
        zoom 2.0
        linear 20.0 zoom 1.0

    Sylvian "Hearing such a declaration... seems like I might start to like myself, just a little bit."

    Sylvian "I tend to like the things that the person I love is fond of."

    show lars narration
    Lars "In that case, I'll make sure my love for you exceeds your expectations."

    Sylvian "Haha, looks like I'll have to work on appreciating myself more then."

    "He leans in and rests his head on my chest, seeing as how I was taller than him. I want to ruffle those wings of his. I wonder how that would feel."

    "I bring up my hand to the top of his wings, delicately brushing the tip of a wing feather. I sense a slight tension, prompting me to scoot closer to his side, where I feel the warmth emanating from his body."

    "My hand continues its journey, gliding from the notch to the upcurved edge of his barbs where the shafts converge. At times, I flutter my touch along the inner vanes of his feathers, punctuating the sensation with gentle kisses."

    "It's a breathtaking experience, a privilege to touch these magnificent wings and witness his face squirm and flush with each tender movement."

    show lars narration
    Lars "You're so beautiful..."

    show lars narration
    Lars "Can I..."

    show lars narration
    Lars "... kiss you, Master?"

    "He almost seems to stagger from my question, staying in silence for a brief moment before recovering his composure."

    Sylvian "That would be a dream, but not right now. My heart is beating far too loudly for me to keep calm and share a proper first kiss with you. Let's take it slow, shall we?"

    "No other words are needed as I gently cup him in my arms. The gesture seemed to have appeased him as a flurry of blossoms rained and enveloped us."

    scene bg black with fade
    show bg_5 with fade

    show sylvian blush at center with dissolve
    show lars
    Lars "Come to think of it, what do we do about Zephyr? As much as I'd like us to spend time together, we—"

    voice "audio/voice/zephyr/zephyr_099_take02.ogg"
    show zephyr at center_2left with moveinleft:
        yalign 0
    show sylvian serious funny with dissolve
    show sylvian serious funny at right with move
    show lars serious
    Zephyr "I've been acting like a third wheel all this time, hehe. You guys just focus on your lovey-dovey confession scene. I'm gathering gossip material as it is."

    voice "audio/voice/zephyr/zephyr_100_take02.ogg"
    show zephyr at shake
    show lars serious
    Zephyr "{i}'The renowned scientist —or should I say, swan-tist— and his ice-pectacle love confession'.{/i} The gossip mill will have a field day with this!"

    show zephyr with dissolve:
        xzoom -1.0

    hide zephyr with moveoutleft

    "Looks like we're all alone for good this time."
    
    "Master Sylvian seems to have the same idea as well as he quickly hurries to close the distance between us."

    show sylvian blush with dissolve
    show sylvian blush at center with move
    show sylvian blush:
        parallel:
            linear 1.0 yalign 0.2
        parallel:
            linear 3.0 zoom 1.50

    "I lift his chin, fixing him with a somewhat serious gaze."

    voice "audio/voice/lars/lars_167_take02.ogg"
    show lars sad
    Lars "But won't that tarnish your reputation?"

    voice "audio/voice/sylvian/sylvian_148_take04.ogg"
    show sylvian
    show lars sad
    Sylvian "Ah, no need to worry. The Archmage will have silenced him long before any reputable gossip columns consider his story. He doesn't tolerate his academics engaging in such... {i}activities{/i}."

    voice "audio/voice/lars/lars_196_take01.ogg"
    show lars serious
    Lars "What about the artifact under Zephyr's control and the trapped descendants?"

    voice "audio/voice/sylvian/sylvian_149_take03.ogg"
    show sylvian serious funny
    show lars 
    Sylvian "I'm confident Claude and my dear junior, Rory, have already handled that."

    voice "audio/voice/sylvian/sylvian_150_take01.ogg"
    show lars 
    Sylvian "I gave her instructions before she started her private puppet show with Zephyr earlier today, and with Claude's extensive connections, he's likely found a solution to ease all your concerns."

    voice "audio/voice/sylvian/sylvian_151_take01.ogg"
    show sylvian
    show lars 
    Sylvian "They are capable members of the guild, after all."

    hide sylvian with dissolve

    scene bg black with fade
    show cg_lars_sylvian_ge with fade

    voice "audio/voice/sylvian/sylvian_152_take01.ogg"
    Sylvian "Thank you, [Lars]..."

    voice "audio/voice/sylvian/sylvian_153_take03.ogg"
    Sylvian "I... I love you, my everlasting bloom."

    $ renpy.choice_for_skipping()
    $ persistent.ending[0] = 1
    scene bg black with fade
    " " "Sylvian - Good End Achieved"
    jump end

label claude_route:
    
    show zephyr happy at left:
        yalign 0
    show claude zorder 2 at center_left with dissolve:
        xzoom -1.0
    show sylvian zorder 1 at center_2right with dissolve:
        xalign 0.65
    show rory at right with dissolve:
        xalign 1.05
    
    voice "audio/voice/zephyr/zephyr_077_take02.ogg"
    show lars
    Zephyr "Did you pick someone already? I need something big to spark my gossip debut if I plan to pay off my debt and renovation costs with your confession shenanigan."

    "I grab Sir Claude's hand in mine and interlace our fingers as I raise them up for Zephyr to see."

    show sylvian sad
    show claude smile 

    "Out of the corner of my eye, I catch Master Sylvian donning a sullen expression, his silhouette gradually slipping into the shadows."
    
    "I notice a few black feathers cascading from his retreat, leaving behind a trail, much like footprints fading away."
    
    hide sylvian sad with dissolve
    show claude smile at center_right with move
    show zephyr at center_1left with move:
        yalign 0
    "A sense of unease flickers within me, but my immediate focus shifts to Sir Claude."

    voice "audio/voice/claude/claude_138_take_02.ogg"
    show lars blush
    Claude "It appears that Captain [Lars] has quite the discerning eye. I'm honored to be beheld by it."

    voice "audio/voice/zephyr/zephyr_084_take01.ogg"
    show lars
    Zephyr "So, Slicky it is then!"

    voice "audio/voice/zephyr/zephyr_085_take01.ogg"
    show lars
    Zephyr "Now tell me, what makes him so special? How's the scoop going to be different from all the other celebrity gossip columns and panels?"

    Lars "Well, he's  a renowned merchant—"

    voice "audio/voice/zephyr/zephyr_080_take02.ogg"
    show claude shocked
    show zephyr sad
    show lars serious
    Zephyr "Boring! Anyone could just slap a make-shift title for themselves; that doesn't make you're gossip-worthy."

    voice "audio/voice/rory/rory_050_take02.ogg"
    show lars
    Rory "Claude here is the heir of the infamous Dupont family, even though he might deny being a nepo baby. They're always globe-slithering, selling exotic trinkets for the price of a whole wing and tail."

    show claude shocked with dissolve:
        xzoom 1.0
        pause 0.5
    
    voice "audio/voice/claude/claude_139_take_03.ogg"
    show claude shocked at shake
    show lars
    Claude "Little Rory, you could have at least tried a more subtle approach to throw me under the dragon ship."

    show rory at jp
    show lars
    voice "audio/voice/rory/rory_051_take01.ogg"
    Rory "Payback time~"

    show lars
    voice "audio/voice/zephyr/zephyr_086_take02.ogg"
    Zephyr "That does indeed sound like a juicy tale for the gossip mill {i}'the tail-smacking adventures of Slicky'{/i} but it's missing something. Perhaps a love confession would—"

    show lars
    voice "audio/voice/rory/rory_052_take01.ogg"
    Rory "Ah, he wouldn't be able to do that. After all, his name starts with a 'C' for conceited and ends with an 'E' for egotistical."

    voice "audio/voice/claude/claude_140_take_03.ogg"
    show claude 
    show rory 
    show lars
    Claude "You're having me in splits, little Rory; I might even consider doing a tail-shedding ceremony just to honor your sense of humor."

    voice "audio/voice/rory/rory_053_take02.ogg"
    show lars
    Rory "Hmph, it was about time I gave you a taste of your own medicine!"

    show claude
    show claude with dissolve:
        xzoom -1.0
        pause 0.5
    
    show lars serious
    Lars "Before we get started on anything, didn't you promise that you'd unfreeze the others?"

    "I don't want to risk getting the other guild members hurt, or have anyone else suffering from the time freeze's effects."

    show lars serious
    Zephyr "Fine, I wouldn't dishonor my family by breaking my oaths, but you better cough up a scoop worthy of my undivided attention!"

    show zephyr happy with dissolve
    show zephyr happy at jp
    show lars serious
    Zephyr "Let's spice up the setting while we're at it; I wouldn't want someone else to hijack my headline when I finally release them from their frozen state."
    
    Zephyr "Scouty, pick a fancy locale worthy of my grandiose presence, won't you?"

    hide zephyr
    hide rory
    hide claude
    with dissolve
    
    play music "track_6_romance_scene.ogg" fadeout 2.0 fadein 2.0

    scene bg black with fade
    show bg_4 at up_pan

    "The sun is gradually sinking towards the horizon, casting cold hues across the sky as late afternoon approaches."

    show zephyr sad at center_3left with dissolve:
        yalign 0
    show claude at center_3right with dissolve:
        xzoom -1.0

    show lars
    Zephyr "Whose brilliant idea was it to ride a dragon for a confession scene?"

    show lars
    Lars "You wanted a place with few to no people, and here we are."

    show zephyr happy
    show lars
    Zephyr "Whatever! I'm focusing on steering this ship but I've got my eyes and ears on you two. Make it count while we're down here."

    show zephyr with dissolve:
        xzoom -1.0 
    hide zephyr with moveoutleft
    show claude at center with move

    "I shoot a glance at Sir Claude and bite my lips in frustration. I chose him as my partner, but with Zephyr so close by, I'm unsure of our next move."

    show lars
    Lars "There's not much time, we have to do something."

    show claude smile
    show lars
    Claude "I could do a skydiving trick from up here. The tabloids would have a field day if I were to fall off under these conditions."

    "I cross my arms, determined to make Sir Claude understand the gravity of the situation."
    
    Lars "Zephyr would be quite upset if we only got noticed for your publicity stunt rather than a confession or comedy routine."

    show lars serious
    Lars "Then again, he should have taken up the role of the prime content for his beloved gossip column with all the antics he's pulling."

    show lars serious
    Lars "Exploiting the humans' unfamiliarity with Div customs and culture would certainly shock everyone once they learn what's been happening under their noses."
    
    show zephyr with moveinleft:
        xzoom 1
        linear 1.0 xalign 0.0
    
    show lars serious
    Zephyr "{size=*2.0}I HEARD THAT!" with vpunch

    show zephyr:
        pause 0.5
    
    show lars serious
    Zephyr "Enough with the chatter, spill the confessions instead! Since I went through all that effort to ice-olate you two."

    show zephyr with dissolve:
        xzoom -1
        pause 1.0
        linear 0.5 xalign -1.0

    pause 1.0
    show lars sad
    Lars "How do you suggest we proceed? I'm worried more people will get caught up in this mess if we don't act swiftly."

    show claude smile at shake
    show lars
    Claude "I doubt we can do comedy under these conditions..."

    "Says the person who can't resist cracking confession jokes every waking hour."

    show lars
    Claude "So a love confession it is then!"

    Lars "Ugh, at this rate, we're going to be renovation minions."

    show lars 
    Claude "Exactly, now picture this - {i}\"The Renovation Duo\"{/i} - I'll tell my terrible jokes, and you can loudly groan as we paint walls and fix leaky pipes for a rundown castle."

    Lars "We should strive to leave an impression on Zephyr that goes beyond shoddy repair work."

    Lars "Imagine what would become of your family legacy if word got out about our current dilemma..."

    show claude shocked
    "Sir Claude, as he always does, theatrically places a hand on his chest, feigning deep offense at my comments. Despite my attempt to maintain seriousness, I couldn't help but crack a smile at his playful antics."

    show lars
    Claude "Tsk, tsk, Captain, you should know that all publicity is good publicity, it's the standard industry cliché."

    show claude smile
    show lars
    Claude "It's because I only ever seek to be the greatest merchant there is that I will use every tool at my disposal to achieve it."

    "Hmph, the same audacious statements, as always. Even under pressure, Sir Claude remains the unwavering bold merchant and adventurer that he is."

    "It was a quality of his that I deeply admired and aspired to learn from."

    "In a realm where courage and determination were paramount, witnessing someone like him fearlessly chasing after his dreams was truly inspiring, and it ignited a fire within me to pursue my own aspirations with equal fervor."

    show claude sad
    Lars "Really? I didn't know our noble scion liked being the center of attention. You always seem to be hiding that you're the only heir of the infamous Dupont merchant family."

    Lars "At first, I thought it was so there wouldn't be any rumors of our Guild being associated with your family name, but you've always been acting suspiciously about it."

    Lars "You never seem to give out your last name during our expeditions or client meetings and even before, with Zephyr—"

    show claude smile at shake
    show lars
    Claude "Captain, I didn't think you were interested in my personal life all that much."

    show bg_4:
        subpixel True
        linear 2.0 blur 10
    show claude smile at center:
        parallel:
            linear 1.0 yalign -0.1
        parallel:
            linear 3.0 zoom 1.50

    "His voice is a soft whisper that caresses my ear, and I can savor the sweetness of his breath. It’s a mysterious and enticing flavor, like a rare fruit from a faraway land."
    
    "I can't believe how quickly he closed the gap between us. Did he do it while I was lost in my rambling? Now, his forehead is almost touching mine, and his eyes..."

    "His piercing golden orbs, which melt into the afternoon sunlight, are fixed directly on me. Why's he looking at me like that? Ugh, this isn't good for my heart."

    show claude blush with dissolve
    show lars blush 
    Claude "I could satisfy your curiosity by merely saying that I enjoy the challenge of forging my own legacy."
    
    show lars blush
    Claude "But then, you'll have to satisfy my curiosity as well – what's the reason behind that little wagging tail you're trying to hide so adorably?"

    "My embarrassment skyrockets and the heat quickly rushes to my cheeks. A quick glance at my tail confirms my nerves, as it wags uncontrollably behind me. Desperately, I begin searching for a way to divert his attention."

    "The line always blurs between his teasing and genuine flirtation, even when he playfully passes it off as a joke."
    
    "Succumbing to his allure is something I'd rather avoid, having witnessed how easily others have fallen for him."

    hide claude smile with dissolve
    show claude_lars_banter with dissolve
    show lars narration
    Lars "{i}Then I suppose{/i}... you wouldn't mind if the headlines read something like this–" with vpunch

    show lars narration
    Lars "'Claude Dupont, the shining star of the Commerce Guild 'Custodes Sylvae', scion of the infamous merchant family, tragically falls to his death.'"

    show lars narration
    Lars "'The consequence of enraging the esteemed dragon pilot [Lars].'"

    show lars narration
    Lars "'Aiming for the skies, only to plummet into the depths of the sea.'"

    Claude "Haha, are you getting shy Captain? Or did you pick up those catchy headline titles from your human passengers again?"

    hide claude_lars_banter with dissolve
    
    show claude smile at center:
        xzoom -1.0

    show lars
    Lars "You have to admit, it does carry a certain dramatic flair."

    show claude smile at jp
    show lars
    Claude "Ah, my dear Captain, I'll oblige to your lie. You always know how to spin an intriguing tale, after all."

    "In the blink of an eye, Sir Claude's hand cups one side of my cheek, and a rush of self-consciousness floods my senses. His touch, though cold and scaly, carries an irresistible sensation."

    show claude blush with dissolve
    pause 1.0
    show bg_4:
        subpixel True
        linear 2.0 blur 10
    show claude blush at center:
        parallel:
            linear 1.0 yalign -0.1
        parallel:
            linear 3.0 zoom 1.50

    show lars blush
    Claude "I've missed talking with you like this, Captain. I've been occupying myself with so many tasks that I haven't had the chance to appreciate our time together like this."

    show lars blush
    Lars "You could always skip them, you know? Taking some time to settle down might do you good."

    show claude sad
    show lars blush
    Claude "Ah, you see, I'm just too restless for that. I'd rather bask in the glory of achieving a dream, rather than the journey towards attaining it."

    show claude
    show lars blush
    Claude "There's something captivating about that period in-between, where aspirations linger and possibilities seem endless."

    show claude smile
    show claude smile at jp
    show lars blush
    Claude "Not to mention, I have no intention of letting you share your company with anyone else."

    show lars blush
    Lars "It's more like, I'm the only one who can keep up with your reckless antics in the first place."

    show bg_4:
        linear 2.0 blur 0
    show claude blush at center:
        parallel:
            linear 2.0 zoom 1.0
        parallel:
            linear 1.0 yalign 0.5
            linear 1.0 ypos 0.5
    
    show lars blush
    Claude "Haha that's right. Maybe... it's time to confess my secret after all, better seize the moment while it lasts before my antics become too much for you."
    
    show claude blush with dissolve:
        zoom 1.0 

    "Though well-known for his love of humor and jest, this time, his response carries an unmistakable sincerity. What could he possibly mean, though?"
    
    hide claude blush with dissolve

label menu_c3:
    $ calc_relations()
    #$ txt_temp = f'{options["C1"]}-{options["C2"]}-{options["CS1"]}-{options["S1"]}-{options["S2"]}-{options["CS2"]}-{options["CS3"]}-{options["CS4"]}-{options["CS5"]}-{options["CS6"]}'
    #$ txt_temp2 = f'c:{relations["claude"]} s:{relations["sylvian"]}'
    
    menu:
        #" " " [txt_temp] \n [txt_temp2]"
        " " " "

        " " (blocked=True) if relations["claude"]<7:
            jump menu_c3

        "Poke further about his comment" if relations["claude"]>=7:
            jump C3_claude_good_end
        
        " " (blocked=True) if relations["claude"]<5:
            jump menu_c3

        "Pass over his comment" if relations["claude"]>=5:
            jump C3_claude_neutral_end
        
        "Stay silent about his comment":
            jump C3_claude_bad_end

label C3_claude_good_end:
    
    play music "track_8_neutral_ending.ogg" fadeout 2.0 fadein 2.0
    
    show claude blush at center with dissolve:
        xzoom -1.0
    
    "I should poke further about his comment."

    show lars
    Lars "What do you mean, Sir Claude?"

    show lars blush
    Claude "Admit it, you were barely containing your curiosity about my secret confession, weren't you?"

    if options["CS3"]==1:

        Lars "Oh, look at you, the epitome of self-assurance!"
        
        show claude serious
        Lars "I distinctly recall our little chat about gifts, where I asked about Master Sylvian's secret, not that I'm the least bit interested in yours."
        
        "A little white lie wouldn't hurt anyone, now would it?"
        
        Lars "But do go on—"

        show claude serious at jp
        show lars serious
        Claude "It's always {i}Master Sylvian{/i} this and {i}Master Sylvian{/i} that. Why can't I ever catch a break from him?"

        show lars serious
        Lars "What's going on? Why the sudden—"
        
        show lars serious
        Claude "You know what? I can't take this anymore."

    if options["CS3"]==2:

        show lars blush
        Claude "Recall that promise I made about sharing everything once we're alone? If memory serves me right, you were quite eager to unravel my secrets at the time, weren’t you?"
        
        show lars blush
        Lars "That's not true! I only wanted you to know that I'm here for you as a friend and fellow guild member, should you ever want to share—"
        
        show lars blush
        Claude "Haha, I'm just joking, [Lars]. I understand your intentions well enough."
        
        show lars blush
        Claude "After all, your close bond with dragons is the reason behind your sincere way of talking, isn’t that right? I’ve admired that for some time now…"

        "He admires something about me? He's certainly teased me so much till now that I've grown accustomed to not receiving any honest praise from him."
        
        Lars "Well, yes, you’re right. My parents would always tell me to be direct with my words, as dragons can have trouble reading your intentions if you're not straightforward or heartfelt in your interactions."
        
        Lars "So, it would be best to just say what’s on your mind, which is kind of what I’m doing. But then again, I’m supposed to be the dragon trainer here, not you—"
        
        show lars blush
        Lars "Ugh, forget it. You were probably just teasing me again."
        
        show lars blush
        Claude "I didn't say I had special feelings for you just for the sake of it, I was quite serious."

        show lars blush
        Claude "I'll even fulfill my promise to you right here and now, just as I swore on that necklace I gave you."

    show claude
    show lars
    Claude "Now, I need you to listen to me carefully, [Lars]"

    "He rarely ever calls me by my name like this, so witnessing this side of him is..."

    play music "track_10_bad_ending_2.ogg" fadeout 2.0 fadein 2.0

    show lars
    Claude "You remember how I've always skirted around the fact that I'm a Dupont heir?"

    Lars "Yes, it's been a constant mystery to me."

    voice "audio/voice/claude/claude_142_take_01_1.ogg"
    show claude sad
    show lars
    Claude "Well, the truth is, I've avoided mentioning it because..."
    
    voice "audio/voice/claude/claude_142_take_01_2.ogg"
    show lars sad
    Claude "I didn't want to be defined by that name."

    voice "audio/voice/claude/claude_143_take_02.ogg"
    show lars sad
    Claude "I've always struggled with titles and appearances growing up."

    voice "audio/voice/claude/claude_144_take_01.ogg"
    show lars sad
    Claude "The burden of being the Dupont family heir, with its myriad of expectations, it all felt like a shallow act that I had to uphold, and I... I felt imprisoned in that superficial world."

    "His voice cracks and trembles, and I notice a muscle in his jaw twitch as he quaveringly attempts to speak up."
    
    "The urge to reach out and subtly brush his cheek or offer a comforting hug to reassure him tugs at me." 
    
    "Yet, at the same time, I'm wholly captivated, giving him my unwavering attention, determined not to disrupt the fragile flow of his confession."

    "His furrowed brows unveil the weight of unpleasant memories, and as much as I yearn to unravel the tangled threads, he begins to shake his head in dismay."
    
    voice "audio/voice/claude/claude_145_take_02.ogg"
    show claude smile
    show lars blush
    Claude "However, with you [Lars], it was a rare chance to shed the mask and simply be myself, the playful companion who loved to tease his partner in crime."

    show claude blush
    show claude blush:
        linear 1.0 zoom 1.1
    "Drawing closer, he delicately runs his fingers through my hair with a tender touch. The scabrous texture of his fingernails traces a deliberate path downward, following the curve of my ear."
    
    "In its wake, a lingering tingle persists, imprinting the sensation on my skin."

    voice "audio/voice/claude/claude_146_take_02.ogg"
    show claude sad
    show lars blush
    Claude "But, over time, my feelings changed..."

    voice "audio/voice/claude/claude_147_take_02.ogg"
    show claude sad
    show lars blush
    Claude "I stopped seeing you as just the guild's pilot or my work partner."

    "A tightening sensation grips my chest, each heartbeat resonating like the rhythmic murmur of a dragon. A flush of warmth colors my cheeks, and my tingling ears gently droop under the weight of his words."

    "I'm hesitant to raise my head, yet, the same hand that had been tenderly caressing my hair and tracing my ear gently takes my chin, coaxing it upwards."

    voice "audio/voice/lars/lars_178_take01.ogg"
    show lars happy
    Lars "Are you saying what I think you're saying?"

    voice "audio/voice/claude/claude_148_take_02.ogg"
    show claude blush
    show lars happy
    Claude "Relationships have always come easily to me, but you... you're the only person who's made me feel this way."

    show claude sad with dissolve:
        linear 1.0 zoom 1.0
    
    "He releases my chin and retreats, leaving behind a noticeable chill in his departure."

    voice "audio/voice/claude/claude_149_take_01.ogg"
    show claude sad
    show lars sad
    Claude "Yet, I fear that settling down would dilute my ambition, the only thing that has allowed me to distance myself from the façade I've grown up with."

    voice "audio/voice/claude/claude_150_take_02.ogg"
    show claude serious
    show lars sad
    Claude "All the efforts I've put into building my own legacy as a merchant, the bravado and arrogance... eh, it would all be meaningless if I realized I had let slip the chance to build something meaningful with you."

    voice "audio/voice/claude/claude_151_take_02_1.ogg"
    show claude smile
    show lars sad
    Claude "I teased you about it as well even though it was just my lingering feelings trying to surface."
    
    voice "audio/voice/claude/claude_151_take_02_2.ogg"
    show lars sad
    Claude "You could say that my candid lizard-like tongue was more honest than its faux owner."

    voice "audio/voice/claude/claude_152_take_01.ogg"
    show claude sad
    show lars sad
    Claude "In reality, I'm the one ensnared by fear, unwilling to relinquish even a fraction of my ambition to battle for what truly matters."

    voice "audio/voice/claude/claude_153_take_01.ogg"
    show claude serious
    show lars sad
    Claude "When push comes to shove, I'm addicted to the concept of competition. I can't break free, can't even take the time to savor the joys of life and the people around me."

    "So, all those jokes about confessions and everything, were they really his sincere way of hiding his inner fears?"

    "I look at him with suspicion, desperately seeking any hint of deceit in his words, his eyes meet mine with an earnest sincerity that pierces through my doubt."

    "Whether it's the hollow look on his face as he attempts nonchalance or the subtle quiver in his voice trying to shield itself from the world."

    "Yet, at this moment, all I can do is witness the loneliness reflected in his glistening eyes, while his braids gracefully dance to the rhythmic sway of the icy wind enveloping us."
   
    voice "audio/voice/claude/claude_157_take_01.ogg"
    show claude smile
    show lars happy
    Claude "You've always been your own strong-willed individual, adorned with that clever, foxlike charm, courageously taking a stand without voicing your fears, all in the name of protecting others."

    voice "audio/voice/claude/claude_158_take_02.ogg"
    show lars happy
    Claude "Today's events have only served to highlight this matter."

    "My heart leaps with excitement at his words. The prospect of being with him is undeniably thrilling, and the uncertainty of what lies ahead fills me with a delightful, if somewhat anxious, anticipation."

    show lars happy
    Lars "..."

    voice "audio/voice/claude/claude_159_take_01_1.ogg"
    show claude sad
    Claude "Perhaps it's time for me to stand here with you, to stop constantly reaching out to the future."
    
    voice "audio/voice/claude/claude_159_take_01_2.ogg"
    Claude "Maybe cherishing the present with you is the ultimate challenge that will truly fulfill me—"

    voice "audio/voice/lars/lars_180_take01.ogg"
    show lars
    Lars "But that's not entirely what you want either, is it?"

    show claude
    show lars
    Claude "What do you mean?"

    show lars blush
    Lars "You've always been the adventurous type, haven't you? Just being content with the present, while wonderful, doesn't seem entirely like you."
    
    show lars blush
    Lars "Are you sure you're ready to let go of all those grand aspirations?"

    show claude shocked
    "His face registers a stunned expression, his mouth hanging open as if he can't quite believe the words I'm saying."
    
    "Perhaps he was in the process of firming up his resolve to let go of his goals, but I can't allow him to have his way that easily."

    show lars blush
    Lars "Regardless of your status as the heir to a prominent family or my unwavering partner who never spared me in teasing, you've always been Claude to me."

    show lars blush
    Lars "I'd like to think that these are the very facets that define who you are, the so-called appearances that you're trying to conceal."

    show lars blush
    Lars "I may not be an expert in understanding all the complexities that define us, but there's one thing I wholeheartedly agree with..."
    
    show lars blush 
    Lars "I want to cherish this moment with you right now, without having you give up on the versions of yourself you may find less appealing."

    show lars blush
    Lars "It's those very facets that make you the intricate person I admire."

    show claude blush
    show lars blush
    Claude "...you've rendered me speechless."

    show lars blush
    Claude "[Lars], you have an uncanny ability to see through the layers I've built around myself."

    show lars
    Lars "Courtesy of spending so much time as your partner."

    show lars
    Claude "You always have a way of making me question my perspective, my ambitions..."

    show lars
    Lars "It's not just about having you question them. It's about cherishing every layer, every facet of who you are, without expecting you to change for me or anyone else."

    show lars
    Lars "There's certainly room for improvement if you want to better yourself, but don't abandon what you've yearned for so long just because there are other dreams you want to attain."

    show lars blush
    Lars "You're the person I admire, and you shouldn't have to choose between your goals. Pursue both, revel in the moment, and tackle those challenges that define you."

    show lars blush
    Lars "You're supposed to be an untouchable merchant for Div's sake!"

    voice "audio/voice/claude/claude_160_take_01.ogg"
    show claude blush at jp
    show lars blush
    Claude "Haha, you've effortlessly resolved my dilemma."

    show bg_4:
        subpixel True
        linear 2.0 blur 10
    show claude blush at center:
        parallel:
            linear 1.0 yalign -0.1
        parallel:
            linear 3.0 zoom 1.50

    pause 2.0
    voice "audio/voice/claude/claude_161_take_01.ogg"
    show lars happy
    Claude "That's what I love about you..."

    voice "audio/voice/lars/lars_191_take01.ogg"
    show lars happy
    Lars "Hey, I wanted to say it first—"

    voice "audio/voice/claude/claude_162_take_01.ogg"
    show claude blush at shake
    show lars happy
    Claude "The first person gets to savor the real taste of discovery, not the second or anyone who comes after. But then again, we're both confessing our feelings for the first time, so I suppose it's a unique experience for the both of us."

    voice "audio/voice/claude/claude_163_take_03.ogg"
    show lars happy
    Claude "Who knew I'd find such a remarkable discovery so close by."

    "I never thought his words would hit me this hard; I might as well transform into a butterfly descendant at this rate."

    "Yeah, he's all sappy and haughty with his self-assured language, but you know what? Being the exclusive audience to this rare, softer side just fuels my prideful joy."
    
    show lars happy
    Lars "..."
    
    voice "audio/voice/claude/claude_164_take_02.ogg"
    show lars happy
    Claude "You gave me the most precious gift I could have asked for, and I'm going to savor every moment I have you to myself."

    voice "audio/voice/lars/lars_194_take02.ogg"
    show lars happy
    Lars "Haha, didn't you just say how I was my own person and all that?"

    voice "audio/voice/claude/claude_165_take_01.ogg"
    show lars happy
    Claude "Then tell me, should I follow my desire to make you mine? Or do you want me to treat you gently?"

    "However, before I can respond, he takes my hand and pulls me closer to him."

    hide claude blush with dissolve

    $ renpy.choice_for_skipping()
    
    play music "track_7_good_ending.ogg" fadeout 2.0 fadein 2.0
    scene bg black with fade
    show cg_lars_claude_ge at slow_pan

    voice "audio/voice/claude/claude_166_take_02.ogg"
    Claude "Call me Claude just like you did a little while ago, won't you, my darling fox?"

    show lars narration
    Lars "Claude..."

    "We stand closely together, our faces mere inches apart. Our lips are naturally drawn toward each other, and with a gentle lift of my chin, he pulls me even closer."
    
    "Our eyes lock and a kiss is shared to seal the moment."

    "My ponytail is likely tousled, gripped by his hand at the back of my head. His fingers glide through my already unruly hair, moving down to my nape." 
    
    "With his other hand on my waist, he pulls me towards him, his rough fingers brushing against the softness of my fur."
    
    scene bg black with fade

    show cg_lars_claude_ge with fade:
        xalign 0.5
        yalign 0.5
        zoom 2.0
        linear 20.0 zoom 1.0

    
    show lars narration
    "Bring it on."

    "Our breathing becomes deep, and in another shared moment of passion, our bodies press against each other, his silky braids brushing against me."
    
    "For a few blissful moments, or perhaps even longer, it's just him and me, cocooned in our own world."

    voice "audio/voice/zephyr/zephyr_108_take02.ogg"
    Zephyr "Ah, what a headline! {i}'The infamous Slicky Dupont and his love affair with the dragon pilot, Scouty'.{/i} I'll have to work around the details later, but what a story it will be."

    scene bg black with fade
    show bg_4 with fade

    voice "audio/voice/zephyr/zephyr_109_take01.ogg"

    show zephyr at center_2left:
        yalign 0
    show claude smile at center_1right:
        xzoom -1.0
    with dissolve

    show lars serious
    Zephyr "I'll earn back the costs of my renovations plans tenfold, or maybe even a hundredfold! {sc}{size=*1.25}MUAHAHAHAHA!{/sc}"

    voice "audio/voice/lars/lars_195_take01.ogg"
    show lars sad
    Lars "Aren't you worried about what he might publish with your name? What if—"

    "Yet before I can finish my sentence, his fingers encircle my face, firm and possessive, as he presses a weighty, fervent kiss upon my lips. His forked tongue prying the opening with an unexpected intensity."

    show zephyr with dissolve:
        xzoom -1.0
    hide zephyr with moveoutleft

    "The audacity of his actions, especially with Zephyr so close, leaves me dumbfounded. But what really gets me is his mischievously childish grin that creates a warm flutter within me."
    
    "I'm surely going to lose my sanity at this rate."

    voice "audio/voice/claude/claude_168_take_01_1.ogg"
    show claude smile at center with move
    show lars happy
    Claude "I couldn't care less about what he does. I may have been obsessed with escaping my family name in the past, but not anymore."
    
    voice "audio/voice/claude/claude_168_take_01_3.ogg"
    show lars happy
    Claude "Not when I have you to adore and cherish, my darling fox."

    voice "audio/voice/claude/claude_169_take_02.ogg"
    show lars happy
    Claude "Not to mention, no reputable publishing house would dare mess with the mighty Duponts."
    
    voice "audio/voice/claude/claude_169_take_03.ogg"
    show lars happy
    Claude "Zephyr will be history before he can even spell our family name out loud."

    voice "audio/voice/lars/lars_196_take01.ogg"
    show lars sad
    Lars "What about the artifact under Zephyr's control and the trapped descendants?"

    voice "audio/voice/claude/claude_170_take_02.ogg"
    show lars sad
    Claude "Awe, leave the worrying to big Boss Sylvian and our little Rory back at the guild."
    
    show lars sad
    Claude "I'm sure they're orchestrating a plan to aid the trapped individuals, all the while scheming my punishment for spiriting you away."

    show bg_4:
        subpixel True
        linear 2.0 blur 10
    show claude smile at center:
        parallel:
            linear 1.0 yalign -0.1
        parallel:
            linear 3.0 zoom 1.50

    voice "audio/voice/lars/lars_197_take02.ogg"
    show lars blush
    Lars "{i}Spiriting me away{/i}, didn't I choose you first when asking Zephyr to let me bring you along?"

    voice "audio/voice/claude/claude_171_take_02.ogg"
    show lars happy
    Claude "Only because I made myself irresistibly selectable."

    hide claude smile with dissolve

    scene bg black with fade
    show cg_lars_claude_ge with fade

    voice "audio/voice/claude/claude_172_take_02.ogg"
    Claude "Now, how about indulging me with a few more kisses?"

    voice "audio/voice/lars/lars_198_take02.ogg"
    show lars narration
    Lars "Alright, you've convinced me. There's no contesting your unparalleled negotiation prowess, obviously."

    voice "audio/voice/claude/claude_173_take_02.ogg"
    Claude "Haha, you are effortlessly showcasing why I love you, [Lars]. After all, no abundance of exotic treasures in the world will ever come close to matching how precious you are to me."

    $ renpy.choice_for_skipping()
    $ persistent.ending[3] = 1
    scene bg black with fade
    " " "Claude - Good End Achieved"
    jump end

label C3_claude_neutral_end:
    
    play music "track_8_neutral_ending.ogg" fadeout 2.0 fadein 2.0
    
    show claude blush at center with dissolve:
        xzoom -1.0
        
    "I should move past his comment."

    "He probably meant it as a joke, like always. It would be best to steer the conversation before I get swept up in his flirty act."

    show claude
    show lars serious
    Lars "Let's focus on the problem at hand first."
    
    show lars serious
    Lars "Don't you have any gossip-worthy tidbits from all those seasonal galas and parties you frequent? Or perhaps some rare intel you came across during your networking sessions?"

    show claude smile
    show lars
    Claude "Well, you could say I prefer crashing those parties at the very end rather than participating and mingling with all the other snooty descendants."

    Lars "Is that why you're always {i}fashionably late{/i}?"
    
    Lars "Perhaps enjoying the process of dressing up and getting ready more than the actual party?"

    show claude smile at shake
    show lars
    Claude "Not at all, dressing up and formalities tend to dull my momentum."

    show claude smile:
        zoom 1.0

    show lars
    Claude "I'd rather envision the way I'll disrupt the party. That spontaneous thrill and unscripted excitement!"

    show lars
    Claude "There's an allure in seeing reality not quite align with my expectations."

    Lars "You're speaking like Master Sylvian all of a sudden. Did his philosophical influence rub off on you?"

    show lars
    Claude "Haha, unlike Boss Sylvian, I prefer being a slave to my desires. It gives me a sense of fulfillment; knowing that I'm capable of pouring my heart and soul into every endeavor that I pursue."

    show lars
    Claude "Leaving something in an ambiguous state or surrendering to simple pleasures doesn't sit well with me; it feels like I'm betraying the very essence of who I am."

    "He chuckles, his eyes holding a playful glint. I didn't realize they had a friendly competition going on."
    
    Lars "Then again, you act like everyone is your rival, don't you? Whether it's Master Sylvian, Rory, or even me—"

    show claude sad
    show lars sad
    Claude "Let's... end the conversation here, Captain. I don't want to spoil the mood with my personal issues, and I can tell you're not that enthusiastic about it either."

    show lars 
    Lars "Come on! You can't just decide that on your own. Spill the juicy details! I already know you've got something up your sleeve."  

    show claude serious
    show lars
    Claude "You say you do, don't you, huh?"
    
    show lars
    Claude "If so, [Lars]. I need you to listen to me carefully."

    "The air around us takes on a charged intensity. He seldom reveals his vulnerabilities, so witnessing this side of him is like catching a glimpse of something rare, like the way his Adam's apple bobs with a subtle tension and the way he calls my name..."
    
    "There's a desperate look in his eyes, and as his silver braids blow in the evening sky, capturing the fading light, the atmosphere crackles with a blend of stress and excitement that I can almost taste."
    
    show lars
    Claude "..."

    show claude sad
    show lars sad
    Claude "You know what? I don't think I'm ready to share my secret with you yet, Captain."

    show lars sad
    Lars "What do you mean? What's wrong—"

    show claude sad with dissolve
    show lars sad
    Claude "I couldn't help but notice how you were so engrossed with Master Sylvian today. I wanted your attention solely on me, without needing to spell it out."

    show lars serious
    Lars "Why are you acting like we're some couple? What does my chat with Master Sylvian got to do with what's happening now?"

    show lars serious
    Claude "Well, if you don't understand it yourself, perhaps we're not on the same page yet when it comes to our feelings."

    "His expression shifts to a melancholic tone, accompanied by a wistful sigh. A few strands of hair lose their perfect arrangement as his fingers comb through them."

    "I've never witnessed him so troubled before."

    "While I've always treasured our partnership, I had no idea that Sir Claude's possessive feelings ran so deep."

    Lars "I promise it'll be okay, just tell me what's on your mind. Maybe it's something I can help with."
    
    show lars
    Claude "..."

    show claude serious
    show lars sad
    Claude "You know what, maybe it's time to confess, just so I can this over with once and for all."

    play music "track_10_bad_ending_2.ogg" fadeout 2.0 fadein 2.0

    show claude sad
    show lars sad
    Claude "You remember how I've always skirted around the fact that I'm a Dupont heir?"

    show lars serious
    Lars "I do, but... what does that have to do with anything right now?"

    voice "audio/voice/claude/claude_142_take_01_1.ogg"
    show lars serious
    Claude "Well, the truth is, I've avoided mentioning it because..."
    
    voice "audio/voice/claude/claude_142_take_01_2.ogg"
    show lars sad
    Claude "I didn't want to be defined by that name."

    voice "audio/voice/claude/claude_143_take_02.ogg"
    show lars sad
    Claude "I've always struggled with titles and appearances growing up."

    voice "audio/voice/claude/claude_144_take_01.ogg"
    show lars sad
    Claude "The burden of being the Dupont family heir, with its myriad of expectations, it all felt like a shallow act that I had to uphold, and I... I felt imprisoned in that superficial world."
    
    "His voice cracks and trembles, and I notice a muscle in his jaw twitch as he quaveringly attempts to speak up. The urge to reach out and subtly brush his cheek or offer a comforting hug to reassure him tugs at me." 
    
    "Yet, at the same time, I'm wholly captivated, giving him my unwavering attention, determined not to disrupt the fragile flow of his confession."

    "His furrowed brows unveil the weight of unpleasant memories, and as much as I yearn to unravel the tangled threads, he begins to shake his head in dismay."
    
    voice "audio/voice/claude/claude_145_take_02.ogg"
    show claude blush
    show lars 
    Claude "However, with you [Lars], it was a rare chance to shed the mask and simply be myself, the playful companion who loved to tease his partner in crime."

    show claude blush:
        linear 1.0 zoom 1.1
    "Drawing closer, he delicately runs his fingers through my hair with a tender touch. The scabrous texture of his fingernails traces a deliberate path downward, following the curve of my ear."
    
    "In its wake, a lingering tingle persists, imprinting the sensation on my skin."

    voice "audio/voice/claude/claude_146_take_02.ogg"
    show claude sad
    show lars 
    Claude "But, over time, my feelings changed..."

    voice "audio/voice/claude/claude_147_take_02.ogg"
    show lars 
    Claude "I stopped seeing you as just the guild's pilot or my work partner."

    "A tightening sensation grips my chest, each heartbeat resonating like the rhythmic murmur of a dragon. A flush of warmth colors my cheeks, and my tingling ears gently droop under the weight of his words."

    "I'm hesitant to raise my head, yet, the same hand that had been tenderly caressing my hair and tracing my ear gently takes my chin, coaxing it upwards."

    voice "audio/voice/lars/lars_178_take01.ogg"
    show lars
    Lars "Are you saying what I think you're saying?"

    voice "audio/voice/claude/claude_148_take_02.ogg"
    show claude blush
    show lars
    Claude "Relationships have always come easily to me, but you... you're the only person who's made me feel this way."

    show claude sad with dissolve:
        linear 1.0 zoom 1.0
    "He releases my chin and retreats, leaving behind a noticeable chill in his departure."

    voice "audio/voice/claude/claude_149_take_01.ogg"
    show lars sad
    Claude "Yet, I fear that settling down would dilute my ambition, the only thing that has allowed me to distance myself from the façade I've grown up with."

    voice "audio/voice/claude/claude_150_take_02.ogg"
    show claude serious
    show lars sad
    Claude "All the efforts I've put into building my own legacy as a merchant, the bravado and arrogance... eh, it would all be meaningless if I realized I had let slip the chance to build something meaningful with you."

    voice "audio/voice/claude/claude_151_take_02_1.ogg"
    show claude smile
    show lars sad
    Claude "I teased you about it as well even though it was just my lingering feelings trying to surface."
    
    voice "audio/voice/claude/claude_151_take_02_2.ogg"
    show lars sad
    Claude "You could say that my candid lizard-like tongue was more honest than its faux owner."

    voice "audio/voice/claude/claude_152_take_01.ogg"
    show claude sad
    show lars sad
    Claude "In reality, I'm the one ensnared by fear, unwilling to relinquish even a fraction of my ambition to battle for what truly matters."

    voice "audio/voice/claude/claude_153_take_01.ogg"
    show lars sad
    Claude "When push comes to shove, I'm addicted to the concept of competition. I can't break free, can't even take the time to savor the joys of life and the people around me."

    "So, all those jokes about confessions and everything, were they really his sincere way of hiding his inner fears?"

    "I look at him with suspicion, desperately seeking any hint of deceit in his words, his eyes meet mine with an earnest sincerity that pierces through my doubt."

    "Whether it's the hollow look on his face as he attempts nonchalance or the subtle quiver in his voice trying to shield itself from the world."

    "Yet, at this moment, all I can do is witness the loneliness reflected in his glistening eyes, while his braids gracefully dance to the rhythmic sway of the icy wind enveloping us."

    show lars sad
    Lars "Sir Claude, I appreciate your feelings, but—"

    show claude serious at jp
    show lars sad
    Claude "Still calling me that obnoxious title even in this situation. Won't you humor me and call me by my name for once?"

    show lars sad
    Lars "..."

    show claude sad
    show lars sad
    Claude "Well, at least I'll have the chance to put these feelings to rest once and for all."

    "In an attempt to offer some comfort, my hand tentatively reaches out to him."
    
    show claude with dissolve:
        xzoom 1.0
    show claude at center_2right with move
    "Yet, he firmly pushes it away, and the gravity of the situation bears down on me."
    
    "Here I am, standing with someone I truly admire -despite our recent clash- who has just confessed his feelings."

    "However, I know deep down that I can't reciprocate them."

    show claude sad
    show lars sad
    Lars "I'm sorry..."

    show lars sad
    Claude "..."

    show claude sad:
        xzoom -1.0
    show lars sad
    Claude "You..."

    voice "audio/voice/claude/claude_157_take_01.ogg"
    show claude smile
    show lars sad
    Claude "You've always been your own strong-willed individual, adorned with that clever, fox-like charm, courageously taking a stand without voicing your fears, all in the name of protecting others."

    show claude smile at center with move
    voice "audio/voice/claude/claude_158_take_02.ogg"
    show lars sad
    Claude "Today's events have only served to highlight this matter."

    show lars sad
    Claude "It's truly unfortunate that things turned out this way."

    show lars sad
    Lars "..."
    
    if options["CS3"]==2:

        show lars sad
        Claude "I did make a promise to you, but I suppose I'm not as good at keeping my word as I believed I would be."

    $ zephyr_name = "Zephyr"
    voice "audio/voice/zephyr/zephyr_106_take02.ogg"
    show claude smile at center_2right with move
    
    play music "track_5_zephyr_theme.ogg" fadeout 2.0 fadein 2.0

    show zephyr at center_3left with moveinleft:
        xzoom 1
        linear 1.0  yalign 0
    show lars serious
    Zephyr "Hey, I know you two had your heartfelt exchange, but I'm in the mood for a grand, dramatic confession. This subtle stuff won't cut it; it's barely a snack when I was hoping for a feast."

    show claude smile at center_2right:
        zoom 1

    voice "audio/voice/zephyr/zephyr_107_take01.ogg"
    show lars serious
    Zephyr "Honestly, if you're not up to the task, you might as well just leap off this dragon's back; you're just extra baggage right now. Come on, give me the theatrics, the flair! THE SCOOP!"

    show lars serious
    Claude "Skydiving right off Spotsy at this very moment... that doesn't sound too bad."

    show lars serious
    Claude "We could descend to the Earth realm together, Captain."

    show lars sad
    Claude "Even if you're not exclusively mine to cherish..."
    
    show lars sad
    Lars "What—"

    $ renpy.choice_for_skipping()

    show claude sad at center_2right with move
    
    show zephyr at center_3left with moveinleft:
        xzoom 1
        linear 1.0  yalign 0

    $ zephyr_name = "Zephyr"
    show lars sad
    Zephyr "OI OI OI, I'm not looking to make my hands any messier; bloody theatrics tend to repel future fans, you know!"

    show claude smile
    show lars sad
    Claude "Don't worry Captain."

    show lars sad
    Claude "I wouldn't mind starting over as long as there's something new to conquer."
    
    show lars sad
    Claude "Perhaps it's a chance to begin with my genuine feelings, leaving behind the pretentious grandeur that my wealth and name affords me."

    show claude sad
    show claude sad at shake
    show lars sad
    Claude "Maybe that's why the Boss Sylvian and little Rory intensely have their walls up against me— they can see through the facade that I've created."
    
    show lars sad
    Lars "It's probably just a misunderstanding. Let's not jinx the journey when we're this close to our destination, especially with the blood rushing to our heads in this altitude—"

    show claude smile
    show lars sad
    Claude "Too late! Catch me if you can Captain."

    $ renpy.choice_for_skipping()
    show claude smile:
        yoffset 0.0
        easein 0.2 yoffset -120
        easein 1.0 yoffset 1000

    show zephyr sad with dissolve:
        yalign 0
    show zephyr sad at center with move:
        yalign 0

    play music "track_9_bad_ending.ogg" fadeout 2.0 fadein 2.0

    "However, before I can ask any more questions, he jumps off Spotsy's back into the sea below."

    show lars serious
    Lars "{size=*2.0}SIR CLAUUUUDE!!!" with vpunch

    show zephyr sad at jp
    show lars serious
    voice "audio/voice/zephyr/zephyr_102_take01.ogg"
    Zephyr "{bt}{size=*2.0}SLICKYYYYY!!!!{/bt}" with vpunch

    show zephyr
    show lars serious
    voice "audio/voice/zephyr/zephyr_103_take01.ogg"
    Zephyr "Oh wait, I should be happy instead~ Buckle up for the show, Scouty! I'm unleashing the scandal of the century to every gossip-hungry magazine and tabloid out there."

    voice "audio/voice/zephyr/zephyr_104_take02.ogg"
    show lars serious
    Zephyr "Watch the gold and treasure roll in as the Duponts scramble to buy the news of their only heir dying first hand. Ah, the perks of having no moral compass!"

    voice "audio/voice/zephyr/zephyr_105_take01.ogg"
    show zephyr at jp
    show lars serious
    Zephyr "{sc}{size=*1.75}MUAHAHAHAHA!{/sc}" with vpunch

    show zephyr at jp:
        linear 1.0 xalign 2.0

    "Panic surges through me as Zephyr's heartless laughter echoes in my ears."
    
    "Ignoring the unsettling sound, I quickly seize the reins from him and spur Spotsy toward Sir Claude's descending form, determined to reach him in time."

    show bg_4:
        linear 10 blur 50
    
    "The biting chill of the wind stings my face as I race to reach Sir Claude."
    
    "Time seems to slow as his figure plummets downward, and desperation fuels my actions."
    
    "My fingers claw at the air as I stretch out, desperately trying to catch him, but he's falling too fast."

    "In a split-second decision, I jump from Spotsy's back, the world spinning as I dive headfirst to intercept him. The wind roars in my ears, and the world blurs into a disorienting whirl as we plunge into the frigid sea."

    play music "track_4_time_stop.ogg" fadeout 2.0 fadein 2.0

    play sound sfx_splash
    show bg_black with fade
    "The impact is brutal, the cold water envelops us in a merciless embrace."
    
    "My fur becomes waterlogged, dragging me down as I struggle to keep both of us afloat. Sir Claude's weight pulls me deeper, and my lungs burn for air."

    show bg_6 with fade:
        blur 40
    "My consciousness... is fading..."

    show bg black with fade
    "I'm... slipping away..."

    show bg_6 with fade:
        linear 0.5 blur 20
    "What's that scaly tail... why's it wrapping around me... ?"

    "Could it be..."

    show bg black with fade
    "Sir Claude's presence surfaces in my fading awareness as he breathes life into me once more."

    show bg_6 with fade:
        linear 0.5 blur 0

    show claude sad with dissolve:
        xalign 0.5
        yalign 1.0
        yoffset 0.0
        xoffset 0.0
        alpha 0.0
        blur 5
        parallel:
            linear 1.0 alpha 1.0
        parallel:
            linear 1.0 blur 0.0

    "Amidst the chaos of the waves, I catch a glimpse of his eyes— those yellow orbs resembling the sun breaking through stormy clouds."

    show lars sad
    show claude sad:
        blur 0.0
        alpha 1.0
        parallel:
            linear 1.0 zoom 1.2
        parallel:
            linear 1.0 yoffset 200
    
    show lars sad

    Lars  "Claude..."

    show lars sad
    Claude "What a joy to hear you call my name."

    show claude sad:
        blur 0.0
        alpha 1.0
        parallel:
            linear 1.0 zoom 1.5
        parallel:
            linear 1.0 yoffset 450
    
    show lars sad
    Claude "I shouldn't have asked you to jump after me, my dear fox. I'm sorry for hurting you."

    show bg_6:
        linear 2.0 blur 20
    show claude sad:
        parallel:
            linear 1.0 zoom 1.0
        parallel:
            linear 1.0 yoffset 0
    
    "I can barely make out his words..."

    show bg_black with dissolve
    pause 1.0

    "With every ounce of strength left in me, I try to fight back the encroaching black spell that threatens to take me. My arms tighten around Sir Claude, and I hold onto him for dear life."

    window hide
    pause 1.0
    
    show bg black with fade
    
    scene bg_5 with fade
    pause 1.0

    play music "track_8_neutral_ending.ogg" fadeout 2.0 fadein 2.0

    show claude sad at center:
        xzoom -1.0
    with dissolve
    "We tumble ashore in a tangled mess of limbs, drenched in salty waves. My fur clings to his rough scales, and a turbulent mix of relief and exasperation engulfs me."

    "What was I thinking? I had overlooked the fundamental fact that Sir Claude is a descendant of lizards, equally adept on land and in the sea. I should have reined in my impulsiveness before plunging us into potential disaster."

    "It's embarrassing. While I'm thankful that we're both safe, the fear of losing him drove me to the edge."

    "How could I save him? What should I do to save him? These thoughts raced through my mind before the realization hit me: he didn't need me to leap after him."

    "Come to think of it, that was probably his plan all along, indulging in an impulsive leap for the sake of some gossip material, and I didn't even see through it!"

    show lars serious
    Lars "Why in Divonia's name would you pull such a stunt? Have you lost your mind? You could have—" with vpunch

    show lars sad
    Lars "You nearly gave me a heart attack. What kind of partner does that?" with vpunch

    show claude smile
    show lars serious
    Claude "A partner for life, obviously. We've just solidified our bond as a duo for eternity, though I'll always hold hope in my heart for more."

    show lars serious
    Lars "Don't give me that kind of lip service."

    show claude sad
    show lars serious
    Claude "Come on, humor me a bit. Share some of the excitement about our future as, you know, {i}just friends{/i}."

    "He extends his hand toward me. It's an odd shift from the usual playful flirtations and spontaneous embraces he's known for."

    "Perhaps it's the coolness of his hand or the way his eyes glisten under the soft, setting sun that makes me realize he's barely holding it together."

    "Perhaps one final question will bring me peace of mind..."

    show lars sad
    Lars "Sir Claude, are you truly satisfied with how things have become between us?"

    show lars sad
    Lars "I just want to be sure I'm not misunderstanding."

    show claude
    show lars sad
    Claude "There's nothing to misunderstand."
    
    show lars sad
    Claude "If my feelings had gotten through, you'd be certain. If they haven't, it might already be too late."
    
    show lars sad
    Claude "Zephyr can freeze time, but he can't turn it back. So, perhaps I'll have to leave that dream for another version of me with more courage."

    show claude sad
    show claude sad at shake
    show lars sad
    Claude "For now, my only ambition is to remain friends with you, because straining our relationship would be too painful."

    play music "2nd_bad_ending_MIX_loop_2nd_ver.ogg" fadeout 2.0 fadein 2.0 
    "He appears quite determined, and I can't help but feel a tinge of sadness. My actions today seem to have influenced this outcome, and I have no choice but to accept it with a heavy heart."

    Lars "Same here, Sir Claude. But no more antics like that."

    show claude smile
    show lars
    Claude "Haha, as much as I'd love to, my tail is still aching from that little splash earlier."

    show claude
    show lars
    Claude "Looks like my recovery will take a {i}long time{/i}."

    $ renpy.choice_for_skipping()
    $ persistent.ending[4] = 1
    scene bg black with fade
    " " "Claude - Neutral End Achieved"
    jump end
    
label C3_claude_bad_end:
    
    play music "track_9_bad_ending.ogg" fadeout 2.0 fadein 2.0
    
    show claude blush at center with dissolve:
        xzoom -1.0
    
    "I should stay silent for now."

    "Master Sylvian and Rory might get in trouble if we stall for too long."

    show claude
    show lars serious
    Lars "Let's focus on the problem at hand first."
    
    show lars serious
    Lars "Don't you have any gossip-worthy tidbits from all those seasonal galas and parties you frequent? Or perhaps some rare intel you came across during your networking sessions?"

    show claude smile
    show lars serious
    Claude "Well, you could say I prefer crashing those parties at the very end rather than participating and mingling with all the other snooty descendants."

    show claude shocked
    show lars serious
    Lars "Let's save story time for later, shall we?"

    show claude shocked at shake
    show lars serious
    Claude "Why rush? What harm could possibly come from delaying a bit longer?"

    show claude shocked:
        zoom 1.0
    show lars serious
    Claude "Maybe I just want to spend more time with you—"

    show lars serious
    Lars "Ugh, enough of this. You only ever know how to flirt and act like a showman."

    "I'm a dragon pilot for Div's sake, a responsible person who is supposed to take care of the people around him."
    
    "I can't just sit back and watch innocent people get dragged into this mess just because Sir Claude wants to have some fun."

    show lars serious
    Lars "If you don't start acting seriously about this, we'll never be able to save the enslaved humans, and Zephyr is going to continue suspending time for Div knows how long."

    show lars serious
    Claude "Come on, Captain, I know you value your duties, but no one said we couldn't have a little fun on the journey!"

    show lars serious
    Lars "Master Sylvian wouldn't have been so nonchalant about this matter like you are."

    show claude serious
    show lars serious
    Claude "Hmm? Is that what this is? A ploy to show me that you wanted {i}Sylvian{/i} to come along instead?"

    "Tension tightens his expression, a silent storm brewing in his golden eyes. As his fingers thread through tightly braided silver hair, unraveling a few strands, the disheveled tendrils mirror the chaos within— a poignant departure from his usual confidence."

    show lars serious
    Lars "I only mentioned him as an example, Sir Claude. What's going on with you? Why are you so riled up?"

    show claude serious at jp
    show lars serious
    Claude "You know what? I can't take this anymore."

    show claude serious:
        zoom 1.0
    show lars serious
    Claude "I've been trying to impress you and win your favor for such a long time, yet your gaze is always fixed on the one and only cherished {i}Master Sylvian{/i}."

    "Venom drips from his words, catching me off guard. I never expected such a strong undercurrent of negative feelings from someone usually so charismatic and positive."

    show lars serious
    Claude "Everyone loves him, why wouldn't they?"

    show lars serious
    Claude "Question is, why didn't you choose him instead?"
    
    show lars serious
    Claude "Is it enjoyable to see me in such a state? To coax my confession, and then, in the end, respond with silence?"

    show lars sad
    Lars "Sir Claude, you've got it all wrong—"

    show claude serious:
        blur 0.0
        alpha 1.0
        parallel:
            linear 1.0 zoom 1.2
        parallel:
            linear 1.0 yoffset 200

    show lars sad       
    Claude "Drop the 'Sir' once and for all! It's clear you don't even bother to hear me out, do you?"

    show lars sad  
    Lars "I never intended to hurt you or make you feel this way..."

    show claude serious:
        blur 0.0
        alpha 1.0
        parallel:
            linear 1.0 zoom 1.5
        parallel:
            linear 1.0 yoffset 450

    show lars serious       
    Claude "You certainly did a 'fantastic' job with that."

    show lars serious 
    Lars "Whatever, let's just put this aside for now and focus on the mission."

    show lars serious
    Lars "We'll talk about this later when our heads are less clouded."

    show claude serious at jp:
        blur 0.0
        alpha 1.0
        parallel:
            linear 1.0 zoom 1.5
        parallel:
            linear 1.0 yoffset 450

    show lars serious
    Claude "Oh, so now my head is {i}clouded{/i}, huh? My brain is lost on its own little adventure, isn't it?"

    "My fur unruffles, and an electric charge courses through my body. A ringing sensation pounds in my head, and it's difficult to restrain the words that spill from my mouth."

    show lars serious
    Lars "Do you always have to act like such a spoiled kid? Didn't your parents give you enough affection as is? Why do you have to cling to me so much?"

    play music "track_10_bad_ending_2.ogg" fadeout 2.0 fadein 2.0 

    show claude sad
    show lars serious
    Claude "I... I didn't expect that from you [Lars]."

    show claude sad:
        parallel:
            linear 1.0 zoom 1.0
        parallel:
            linear 1.0 yoffset 0

    show lars serious
    Lars "You don't expect much from anyone aside from yourself, now do you?"

    "Why did I say such a thing? Was it just anger talking, or did I truly mean what I said? "

    show lars sad
    Claude "I didn't imagine I'd ever say this but I'm... disappointed in you [Lars]."

    show lars sad
    Claude "You deliberately used my family name to hurt me, didn't you? Even though you know better than anyone else, that I... ugh, forget it."

    "It doesn't matter now; I can't take back my words. I've hurt the person I admired, and guilt is staining my honor."
    
    "Sir Claude's pained face looks pale and drawn. His eyes are lifeless, and his lips tight. He seems like a broken man, and I'm the one who broke him. Now he's merely a shell of his former self."
    
    show claude serious
    show lars sad
    Claude "You know what, maybe it's time to confess, just so I can get over you once and for all."

    show lars sad
    Claude "You remember how I've always skirted around the fact that I'm a Dupont heir?"

    show lars serious
    Lars "I do, but... what does that have to do with anything right now?"

    voice "audio/voice/claude/claude_142_take_01_1.ogg"
    show claude sad
    show lars serious
    Claude "Well, the truth is, I've avoided mentioning it because..."
    
    voice "audio/voice/claude/claude_142_take_01_2.ogg"
    show lars serious
    Claude "I didn't want to be defined by that name."

    voice "audio/voice/claude/claude_143_take_02.ogg"
    show lars serious
    Claude "I've always struggled with titles and appearances growing up."

    voice "audio/voice/claude/claude_144_take_01.ogg"
    show lars serious
    Claude "The burden of being the Dupont family heir, with its myriad of expectations, it all felt like a shallow act that I had to uphold, and I... I felt imprisoned in that superficial world."
    
    "His voice cracks and trembles, and I notice a muscle in his jaw twitch as he quaveringly attempts to speak up. The urge to shut my eyes, sparing myself from witnessing this pitiful scene, tugs at me." 
    
    "Will we finally be able to get over this hurdle and be done with the confession?"

    "His furrowed brows unveil the weight of unpleasant memories, an irritating habit I've grown weary of."
    
    voice "audio/voice/claude/claude_145_take_02.ogg"
    show claude blush
    show lars serious
    Claude "However, with you [Lars], it was a rare chance to shed the mask and simply be myself, the playful companion who loved to tease his partner in crime."

    "My heart quickens its pace, a sense of dread sparking through every fiber of my being while he absentmindedly strokes his braids."
    
    voice "audio/voice/claude/claude_146_take_02.ogg"
    show claude sad
    show lars serious
    Claude "But, over time, my feelings changed..."

    voice "audio/voice/claude/claude_147_take_02.ogg"
    show lars sad
    Claude "I stopped seeing you as just the guild's pilot or my work partner."

    "A heavy weight settles on my chest, and my heart races, each beat echoing my growing unease. Weariness seeps into my bones as I find myself in an awkward role– the unwilling recipient of Sir Claude's love confession."

    "I really don't want to look at him right now."

    voice "audio/voice/lars/lars_178_take01.ogg"
    show lars serious
    Lars "Are you saying what I think you're saying?"

    voice "audio/voice/claude/claude_148_take_02.ogg"
    show claude blush
    show lars serious
    Claude "Relationships have always come easily to me, but you... you're the only person who's made me feel this way."

    voice "audio/voice/claude/claude_149_take_01.ogg"
    show claude sad
    show lars sad
    Claude "Yet, I fear that settling down would dilute my ambition, the only thing that has allowed me to distance myself from the façade I've grown up with."

    voice "audio/voice/claude/claude_150_take_02.ogg"
    show claude serious
    show lars sad
    Claude "All the efforts I've put into building my own legacy as a merchant, the bravado and arrogance... eh, it would all be meaningless if I realized I had let slip the chance to build something meaningful with you."

    voice "audio/voice/claude/claude_151_take_02_1.ogg"
    show claude smile
    show lars sad
    Claude "I teased you about it as well even though it was just my lingering feelings trying to surface."
    
    voice "audio/voice/claude/claude_151_take_02_2.ogg"
    show lars sad
    Claude "You could say that my candid lizard-like tongue was more honest than its faux owner."

    voice "audio/voice/claude/claude_152_take_01.ogg"
    show claude sad
    show lars sad
    Claude "In reality, I'm the one ensnared by fear, unwilling to relinquish even a fraction of my ambition to battle for what truly matters."

    voice "audio/voice/claude/claude_153_take_01.ogg"
    show claude serious
    show lars sad
    Claude "When push comes to shove, I'm addicted to the concept of competition. I can't break free, can't even take the time to savor the joys of life and the people around me."

    "So, all those jokes about confessions and everything, were they really his sincere way of hiding his inner fears?"

    "I look at him with suspicion, desperately seeking any hint of deceit in his words, his eyes meet mine with an earnest sincerity that pierces through my doubt."

    "Whether it's the hollow look on his face as he attempts nonchalance or the subtle quiver in his voice trying to shield itself from the world."

    "Yet, at this moment, all I can do is witness the loneliness reflected in his glistening eyes, while his braids gracefully dance to the rhythmic sway of the icy wind enveloping us."

    show lars sad
    Lars "..."

    show claude sad
    show lars sad
    Claude "Well, at least I'll have the chance to put these feelings to rest once and for all."

    "In an attempt to offer some comfort, my hand tentatively reaches out to him."
    
    show claude with dissolve:
        xzoom 1.0
    show claude at center_2right with move
    "Yet, he firmly pushes it away, and the gravity of the situation bears down on me."
    
    "Here I am, standing with someone I truly admire -despite our recent clash- who has just confessed his feelings."

    "However, I know deep down that I can't reciprocate them."

    show claude sad
    show lars sad
    Lars "I'm sorry..."

    show lars sad
    Claude "..."

    if options["CS3"]==2:

        show lars sad
        Claude "I did make a promise to you, but I suppose I'm not as good at keeping my word as I believed I would be."

    $ zephyr_name = "Zephyr"
    voice "audio/voice/zephyr/zephyr_106_take02.ogg"

    play music "track_5_zephyr_theme.ogg" fadeout 2.0 fadein 2.0

    show claude smile at center_2right with move
    
    show zephyr at center_3left with moveinleft:
        xzoom 1
        linear 1.0  yalign 0
    show lars serious
    Zephyr "Hey, I know you two had your heartfelt exchange, but I'm in the mood for a grand, dramatic confession. This subtle stuff won't cut it; it's barely a snack when I was hoping for a feast."

    voice "audio/voice/zephyr/zephyr_107_take01.ogg"
    show lars serious
    Zephyr "Honestly, if you're not up to the task, you might as well just leap off this dragon's back; you're just extra baggage right now. Come on, give me the theatrics, the flair! THE SCOOP!"

    show lars serious
    Claude "Skydiving right off Spotsy at this very moment... that doesn't sound too bad."

    show lars serious
    Claude "We could descend to the Earth realm together, Captain."

    show lars sad
    Claude "Because wherever you are, I'm confident I will find you, and we will always remain our own unique duo."
    
    show lars sad
    Lars "What—"

    $ renpy.choice_for_skipping()

    show claude sad at center_2right with move
    
    show zephyr at center_3left with moveinleft:
        xzoom 1
        linear 1.0  yalign 0

    $ zephyr_name = "Zephyr"
    show lars sad
    Zephyr "OI OI OI, I'm not looking to make my hands any messier; bloody theatrics tend to repel future fans, you know!"

    show claude sad
    show claude sad at shake
    show lars sad
    Claude "Maybe that's why the Boss Sylvian and little Rory intensely have their walls up against me— they can see through the facade that I've created."
    
    show lars sad
    Lars "It's probably just a misunderstanding. Let's not jinx the journey when we're this close to our destination, especially with the blood rushing to our heads in this altitude—"

    show claude smile
    show lars sad
    Claude "Don't worry Captain."

    show lars sad
    Claude "Did you forget that I'm a lizard descendent? I'll be fine, so..."

    show lars sad
    Claude "Don't catch me."

    $ renpy.choice_for_skipping()
    show claude smile:
        yoffset 0.0
        easein 0.2 yoffset -120
        easein 1.0 yoffset 1000

    show zephyr sad with dissolve:
        yalign 0
    show zephyr sad at center with move:
        yalign 0

    play music "track_9_bad_ending.ogg" fadeout 2.0 fadein 2.0

    "However, before I can ask any more questions, he jumps off Spotsy's back into the sea below."

    show lars serious
    Lars "{size=*2.0}SIR CLAUUUUDE!!!" with vpunch

    show zephyr sad at jp
    show lars serious
    voice "audio/voice/zephyr/zephyr_102_take01.ogg"
    Zephyr "{bt}{size=*2.0}SLICKYYYYY!!!!{/bt}" with vpunch

    voice "audio/voice/zephyr/zephyr_103_take01.ogg"
    show zephyr
    show lars serious
    voice "audio/voice/zephyr/zephyr_103_take01.ogg"
    Zephyr "Oh wait, I should be happy instead~ Buckle up for the show, Scouty! I'm unleashing the scandal of the century to every gossip-hungry magazine and tabloid out there."

    voice "audio/voice/zephyr/zephyr_104_take02.ogg"
    show lars serious
    Zephyr "Watch the gold and treasure roll in as the Duponts scramble to buy the news of their only heir dying first hand. Ah, the perks of having no moral compass!"

    voice "audio/voice/zephyr/zephyr_105_take01.ogg"
    show zephyr at jp
    show lars serious
    Zephyr "{sc}{size=*1.75}MUAHAHAHAHA!{/sc}" with vpunch

    show zephyr at jp:
        linear 1.0 xalign 2.0

    "Panic surges through me as Zephyr's heartless laughter echoes in my ears."
    
    "Ignoring the unsettling sound, I quickly seize the reins from him and spur Spotsy toward Sir Claude's descending form, determined to reach him in time."

    show bg_4:
        linear 10 blur 50
    
    "The biting chill of the wind stings my face as I race to reach Sir Claude."
    
    "Time seems to slow as his figure plummets downward, and desperation fuels my actions."
    
    "My fingers claw at the air as I stretch out, desperately trying to catch him, but he's falling too fast."

    "In a split-second decision, I jump from Spotsy's back, the world spinning as I dive headfirst to intercept him. The wind roars in my ears, and the world blurs into a disorienting whirl as we plunge into the frigid sea."

    play sound sfx_splash
    show bg_black with fade
    "The impact is brutal, the cold water envelops us in a merciless embrace."
    
    "My fur becomes waterlogged, dragging me down as I struggle to keep both of us afloat. Sir Claude's weight pulls me deeper, and my lungs burn for air."

    show bg_6 with fade:
        blur 40
    "My consciousness... is fading..."

    show bg black with fade
    "I'm... slipping away..."

    show bg_6 with fade:
        linear 0.5 blur 20
    "What's that scaly tail... why's it wrapping around me... ?"
    
    "Could it be..."

    show bg black with fade
    "Sir Claude's presence surfaces in my fading awareness as he breathes life into me once more."

    show bg_6 with fade:
        linear 0.5 blur 0

    show claude sad with dissolve:
        xalign 0.5
        yalign 1.0
        yoffset 0.0
        xoffset 0.0
        alpha 0.0
        blur 5
        parallel:
            linear 1.0 alpha 1.0
        parallel:
            linear 1.0 blur 0.0

    "Amidst the chaos of the waves, I catch a glimpse of his eyes— those yellow orbs resembling the sun breaking through stormy clouds."

    show lars sad
    show claude sad:
        blur 0.0
        alpha 1.0
        parallel:
            linear 1.0 zoom 1.2
        parallel:
            linear 1.0 yoffset 200
    
    show lars sad
    Lars  "Claude..."

    show lars sad
    Claude "What a joy to hear you call my name."

    show claude sad:
        blur 0.0
        alpha 1.0
        parallel:
            linear 1.0 zoom 1.5
        parallel:
            linear 1.0 yoffset 450
    
    show lars sad
    Claude "I shouldn't have asked you to jump after me, my dear fox. I'm sorry for hurting you."

    show bg_6:
        linear 2.0 blur 20
    show claude sad:
        parallel:
            linear 1.0 zoom 1.0
        parallel:
            linear 1.0 yoffset 0
    
    "I can barely make out his words..."

    show bg_black with dissolve
    pause 1.0

    "With every ounce of strength left in me, I try to fight back the encroaching black spell that threatens to take me. My arms tighten around Sir Claude, and I hold onto him for dear life."

    window hide
    pause 1.0
    
    show bg black with fade
    
    scene bg_5 with fade
    pause 1.0

    play music "track_8_neutral_ending.ogg" fadeout 2.0 fadein 2.0

    show claude serious at center:
        xzoom -1.0
    with dissolve

    "We tumble ashore in a tangled mess of limbs, drenched in salty waves. My fur clings to his rough scales, and a turbulent mix of relief and exasperation engulfs me."

    "What was I thinking? I had overlooked the fundamental fact that Sir Claude is a descendant of lizards, equally adept on land and in the sea. I should have reined in my impulsiveness before plunging us into potential disaster."

    "It's embarrassing. While I'm thankful that we're both safe, the fear of losing him drove me to the edge."

    "How could I save him? What should I do to save him? These thoughts raced through my mind before the realization hit me: he didn't need me to leap after him."

    "Come to think of it, that was probably his plan all along, indulging in an impulsive leap for the sake of some gossip material, and I didn't even see through it!"

    show lars serious
    Lars "Why in Divonia's name would you pull such a stunt? Have you lost your mind? You could have—" with vpunch

    show lars sad
    Lars "You nearly gave me a heart attack. What kind of partner does that?" with vpunch

    show lars serious
    Claude "What partner... I told you not to catch me, didn't I?"

    show lars serious
    Lars "Is that how you plan on acting from now on?"

    show lars serious
    Claude "Do me a little favor and stay away from me for a while, [Lars]."

    "He breaks away from his stagnant position and slowly begins to walk away. Is this how it all ends?"

    "The partner I've worked alongside for so long, my dearest friend, just walking away without a word or challenge?"

    "A part of me yearns to reach out, to call his name, but the risk of causing misunderstandings or giving false hope holds me back."

    "So, I remain rooted to my spot, watching his retreating form."

    "Perhaps one final question will bring me peace of mind..."

    play music "track_10_bad_ending_2.ogg" fadeout 2.0 fadein 2.0

    show lars sad
    Lars "Sir Claude, are you truly satisfied with how things have become between us?"

    show lars sad
    Lars "I just want to be sure I'm not misunderstanding."

    show lars sad
    Claude "If my feelings had gotten through, you'd be certain. If they haven't, it might already be too late."
    
    show lars sad
    Claude "Zephyr can freeze time, but he can't turn it back. So, perhaps I'll have to leave that dream for another version of me with more courage."

    show claude sad
    show claude sad at shake
    show lars sad
    Claude "I'll walk away from this like the coward that I am, a small lizard who couldn't achieve what he wanted. Staying with you would only remind me of the failure that I am, you even said it yourself..."

    show lars sad
    Lars "But I didn't mean it like that; it was just the heat of the moment. I'm sorry about that."

    show lars sad
    Lars "Why are you deciding everything on your own?"

    show lars sad
    Claude "I might as well claim the victory of having the last word since I didn't succeed in having the best one."

    show lars sad
    Claude "Goodbye, [Lars]... take care of yourself."

    $ renpy.choice_for_skipping()
    $ persistent.ending[5] = 1
    scene bg black with fade
    " " "Claude - Bad End Achieved"
    jump end

label end:
    stop music fadeout 1.5
    scene bg black with fade
    pause 1.5
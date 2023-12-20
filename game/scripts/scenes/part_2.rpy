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
    show zephyr happy at left
    show claude at center_left
    show sylvian at center_right
    show rory at right
    show lars
    Zephyr "Did you pick someone already? I need something big to spark my gossip debut if I plan to pay off my debt and renovation costs with your confession shenanigan."

    hide lars
    Lars narration "I grab Master Sylvian's hand in mine and interlace our fingers as I raise them up for Zephyr to see."

    show lars
    Lars "I choose him."

    #here the arrangement will change as claude gets turned into claude_sad during the last sentence and then he exits the scene. 
    #sylvian will move to the center, rory  and zephyr will be in the same position
    $ renpy.choice_for_skipping()
    show claude sad:
        linear 0.5 xalign -1.0
    show sylvian blush at center with move
    Sylvian "Thank you [Lars]. I truly mean it."

    show lars blush
    Sylvian "Now my heart can rest at ease knowing I’m allowed to selfishly stay by your side."

    show lars
    show sylvian at center
    Zephyr "So, Smarty it is then!"

    Zephyr "Now tell me, what makes him so special? How's the scoop going to be different from all the other celebrity gossip columns and panels?"

    Sylvian "Well, he’s  a renowned magician—"

    show zephyr sad at left
    Zephyr "Boring! Anyone could just slap a make-shift title for themselves; that doesn't make you’re gossip-worthy."

    Rory "He's one of Divonia's brilliant minds, a leading researcher who uncovered the connection between human travelers from Earth and Divonia. Plus, he's a master of flower magic."

    Sylvian "My dear junior…"

    Rory "If I'm not going to vouch for my mentor, then who will?"

    show zephyr happy at left
    Zephyr "That does indeed sound like a juicy tale for the gossip mill — the renowned swan-tist of Divonia and his hidden discovery —  but it's missing something. Perhaps a love confession would…"

    show lars serious
    Lars "Before we get started on anything, didn't you promise that you'd unfreeze the others?"

    hide lars
    Lars narration "I don't want to risk getting the other guild members hurt, and more importantly, I don't want anyone else suffering from the time freeze's effects."

    show lars serious
    Zephyr "Fineeee, I wouldn't dishonor my family by breaking my oaths, but you better cough up a scoop worthy of my undivided attention!"

    Zephyr "Let's spice up the setting while we're at it; I wouldn't want someone else to hijack my headline when I finally release them from their frozen state. Scouty, pick a fancy locale, won't you?"

    hide zephyr
    hide claude
    hide zylvian
    hide rory
    $ renpy.choice_for_skipping()
    #black screen transition fade in/fade out
    #scene bg black
    show bg_5 with fade

    Lars narration "The sun is gradually sinking towards the horizon, casting cold hues across the sky as late afternoon approaches."

    show zephyr sad at left
    show sylvian at center
    Zephyr "Whose brilliant idea was it to choose the seaside for a confession scene?"

    Zephyr "I had to bring a dragon for the ride just to carry you two over here."

    show lars
    Lars "You wanted a place with few to no people, and here we are."

    show zephyr happy at left
    Zephyr "Whatever! I'm focused on keeping the coast clear, especially since I had to unfreeze everyone but I've got my eyes and ears on you two. Make it count while we're down here."

    hide lars
    #zephyr exits the scene, and sylvian stays in the center
    $ renpy.choice_for_skipping()
    show zephyr:
        linear 0.5 xalign 2.0
    show sylvian blush at center
    Lars narration "I shoot a glance at Master Sylvian and bite my lips in frustration. I chose him as my partner, but with Zephyr so close by, I'm unsure of our next move."

    show lars serious
    Lars "There’s not much time, we have to do something."

    show sylvian serious funny at center
    Sylvian "It's indeed disheartening to witness such a scenario, where the transported humans' unique and sporadic presence is taken advantage of."

    Sylvian "Being a rarity, they can be subjected to exploitation due to their infrequent encounters. However, this is the first time I've witnessed such a situation up close."

    Lars "Perhaps Zephyr should have taken up the role of the prime content for his beloved gossip column with all the antics he's pulling. Exploiting the humans' unfamiliarity with Div customs and culture would certainly add a mysterious twist for everyone once they learn what's been happening under their noses."

    #zephyr_happy suddenly comes in from the right and zooms in super close to MC, almost as if his sprite is covering up everything behind the textbox
    show zephyr:
        linear 0.5 xalign 1.0
    Zephyr "I HEARD THAT!"

    Zephyr "Enough with the chatter, spill the icy confessions instead!"

    #zephyr_happy exits the scene from the right
    show zephyr:
        linear 0.5 xalign 2.0
    Lars "How do you suggest we proceed, Master? I'm worried more people will get caught up in this mess if we don’t act swiftly."

    show sylvian at center
    Sylvian "Give me a moment."

    hide lars
    Lars narration "Master Sylvian's hands glide with practiced grace, weaving a spell that summons blossoms, enveloping him in an ethereal aura. My focus is momentarily entranced by the display, but it swiftly shifts to the vial of liquid he seemingly conjures from thin air."

    Lars narration "Caught in his scrutiny, his focus shifts from performing the magical spectacle to the vial in his hand."

    show lars
    Lars "…"

    show sylvian mad
    Sylvian "A slight tonic to ease my nerves. In Zephyr's company, there's a chance I might speak of rather personal matters during confessions."

    show lars blush
    show sylvian blush
    Lars "There's no need to be nervous, Master Sylvian. It's not like we'll be doing a love confession like what Zephyr said."

    show sylvian blush
    hide lars
    Lars narration "He bears a fake grin and begins to give out an awkward laugh as if he's trying to make up for what he's about to say. Today has shown me sides of him that I'd never imagined before."

    show lars
    Sylvian "Haha, of course not! I-I don’t know...what I would— or what I should do if you grew to despise —or even loathe— someone like me because of what I might say for a supposed confession."

    show sylvian at center
    Sylvian "But fret not, [Lars]. My tenure in academia provided access to restricted sections, and I'm confident in my ability to fashion a fitting gossip source for our young Lord. Particularly considering his apparent lack of discrimination when it comes to topics or specific requests."

    hide lars
    Lars narration "Feeling a sense of optimism at hearing the news, I enthusiastically chime in."

    show lars
    Lars "You're right. Why didn’t I think of that earlier? You could even use your connections to ask for extra help, can’t you? So, we can make sure nothing like this ever happens again."

    show sylvian sad at center
    Sylvian "That’s going to be a bit difficult."

    hide lars
    Lars narration "A haunting shadow descends over him, as if a storm cloud has eclipsed the sun. From the edges of his magician's hat, wilted flowers creep out, a stark contrast to their once vibrant bloom."

    Lars narration "His brows furrow and a warm flush of embarrassment tints his cheeks, like a delicate watercolor painting tainted by an unexpected hue."

    show lars sad
    Lars "But weren’t you one of the top academics in the past? Surely, there’s someone who can—"

    Sylvian "[Lars]!"

    hide lars
    Lars narration "Ah, that tone again— the one that resonates like a guild leader's command. The weight in his words is palpable, leaving me curious about the sudden shift in his demeanor. But perhaps it's better to divert the conversation for now."

    show lars sad
    Lars "Got it. I won't talk about it if you don't want to."

    hide lars
    Lars narration "I cross my arms, displaying my confusion. So, there really isn't a need for us to work together if Master Sylvian already has his plan set? He seems to have a better grasp of the situation, having planned this far ahead without informing me."

    Lars narration "I should at least avoid giving him any extra burdens to shoulder. Not to mention, I brought him along without discussing it first. It's true that he seemed enthusiastic enough to come along though, and the thought of that excites me."

    Lars narration "Speaking of excitement, it's probably best to keep my tail perfectly still. As for my fox ears, I delicately adjust them, trying to maintain an appearance of composure. The subtle flicker of my ears betrays the underlying nervousness of being in the presence of my Master’s watchful gaze."

    Lars narration "Ah, I wish Spotsy were near so I could soothe my nerves by caressing her or something. I feel really useless right now."

    show sylvian
    show lars
    Sylvian "Were you thinking of your dragons again, [Lars]?"

    show lars blush
    Lars "How on Divonia did you find that out? Was my tail wagging again? I swear it always keeps-"

    show sylvian blush at jp
    #sylvian does a little up and down jum for the laughing part
    Sylvian "Hahaha! It's nothing of that sort. It's just that I've been observing you for such a long time that I can't help but pick up on your subtlest of gestures."

    hide lars
    Lars narration "Ah, hearing that is making me somewhat embarrassed. To think that I was being observed by him. Surely, he wanted to see if I was doing a good job or not, so I hope I haven't disappointed him."

    show lars
    Lars "Speaking of which, Master. I did bring you along like this, but to think you had a plan of your own…"

    Lars "What kind of academic gossip tale will you be telling him? Will you be needing my help—"

    show sylvian
    Sylvian "You needn't worry, [Lars]."

    show lars
    Lars "But I'd still like to have something to do."

    Sylvian "Are you searching for purpose? It can be a bit of a maze, and the answers you find might not be the ones you expect."

    Lars "So, should I just sit here and do nothing?"

    show sylvian blush
    Sylvian "Not necessarily. Perhaps I should suggest— or, if I may, show you— an alternative where we could...uhm, if that’s okay with you, of course…share a love confession?"

    Sylvian "It’s going to be from my side though, not yours! Obviously not from you; that wouldn’t make sense."

    show sylvian sad
    Sylvian "It’s not like you feel the same way I do…"

    hide lars
    Lars narration "It's rather unlikely of Master Sylvian to act in such a manner. My mind drifts to other instances where he displayed a hint of romance, only to revert to the role of a caring yet distant master."

    Lars narration "However, this time, his shaking hands and the glistening look in his eyes suggest it's not another session of false bravado but something else— something unknown yet exciting for the first time."

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
    play music "track_9_bad_ending.ogg"
    Lars narration "I should poke further about his comment."

    Lars narration "It might get him a bit ruffled up but I can’t contain my curiosity."

    show lars
    Lars "How long have you harbored these romantic thoughts, Master? I recall you mentioning that entertaining the idea of such a relationship between you and me was, as you put it, unethical."

    show sylvian sad
    Sylvian "Oh, did I really say that? Y-you can dismiss— um… I mean, feel free to forget what I just said. It was rather foolish— an error on my part to make such a bold declaration."

    Lars "Are you feeling alright? Did the tonic not calm your nerves like you wanted?"

    hide lars
    Lars narration "A snort escapes me, the sound cutting through the air like a fleeting burst of amusement. Yet, instead of joining in laughter, Master Sylvian abruptly falls silent, his features tightening as he begins to bite his lips."

    Sylvian "No, nothing of the sort. I-I was simply taken aback because I didn't anticipate your reaction. I suppose it's because I've become accustomed to how you always manage to say the right thing."

    Sylvian "It's a bit difficult for my heart when you openly point out the things I keep trying to keep concealed…"

    show lars
    Lars "There’s a limit to discretion, Master. I mean, not everyone is oblivious enough not to notice the difference in your treatment."

    Lars "When did it start? How did you feel when I took your hand in front of Zephyr? I always see dragons cuddling and playing around with their mate, do you also have such thoughts—"

    show sylvian blush
    #textbox shake for the next line
    Sylvian "{sc}[Lars]!{/sc}"

    #sylvian’s sprite starts shaking a bit like he’s super nervous
    show sylvian blush at shake
    Sylvian "Y-you can’t -you m-musn’t- say such a thing out loud! Or better yet, why would y-you… or no, my mind can’t take this anymore-"

    hide lars
    Lars narration "Poor Master Sylvian looks like he's about to explode; his face is ablaze in varying shades of red. Upon closer examination, it's as if imaginary steam is wafting, suggesting his head might be on the verge of overheating. His delicate feathers appear tousled, as if on the brink of unraveling at any given moment."

    show sylvian sad:
        xoffset 0.0
        yoffset 0.0
    Sylvian "You’ve never acted like this before."

    Lars "I could say the same for you. You're usually the one guiding us as the leader, giving instructions on what to do and what to avoid."

    show lars
    Lars "Now, it seems like you've taken matters into your own hands for the first time."

    Sylvian "So, what you're saying is, this boldness doesn't quite align with my usual demeanor?"

    Lars "More or Less. This just means that I brought you along for nothing, you could say. I shouldn’t have taken your hand back there."

    Sylvian "…for nothing?"

    hide lars
    Lars narration "If my eyes weren't mistaken, it almost seemed like Master Sylvian was pouting. His eyes squinted in contemplation, and his petite beard scrunched up. A subtle furrow creased his brow, casting an endearing yet troubled expression across his features."

    show lars
    Sylvian "Tell me [Lars], is that really what you mean?"

    Lars "Come on, Master. It’s really not that serious."

    Lars "You’ve already done what was needed and sorted out a secret scoop to share with Zephyr."

    hide lars
    Lars narration "That...didn’t seem to work. Instead of the anticipated joy, his pout deepens, and a tinge of sadness creeps into his eyes. The corners of his eyes seem to glisten, hinting at the possibility of tears welling up."

    Sylvian "I suppose…it was my mistake to have expected more, I shouldn’t have indulged in my greed."

    show lars
    Lars "Haha, what are you talking about, Master? Or were you planning on doing a secret confession since the beginning or something?"

    hide lars
    Lars narration "A heavy silence lingers, urging me to stick to my earlier strategy and poke him even further."

    show lars serious
    Lars "Or could it be- is that why you sorted the gossip deal beforehand?"

    Lars "Seems like we’re in quite an awkward situation…"

    hide lars
    Lars narration "All at once, his expression transforms into one of horror."

    hide lars
    Sylvian "I-I-I…need to leave— I need to get out of here!"

    #after the last sentence, sylvian exits from either direction
    show sylvian:
        linear 0.5 xalign 2.0
    Lars narration "He flutters his large swan wings open causing his feathers to ruffle. They catch the cold hues of the afternoon sun as he lifts off the ground and soars into the sky. The sudden display captures Zephyr's attention, prompting him to shout out."

    hide sylvian
    show zephyr sad
    Zephyr "SMARTY!"

    Zephyr "Where do you think you’re going?! You have to give me some gossip material first!"

    Zephyr "I’m not letting you get away!"

    hide sylvian
    hide zephyr
    show spotsy
    Lars narration "But before he has the chance to grumble any further, I swiftly move to the spot where Spotsy is resting. I climb onto her back and feel the afternoon air bristling against my fur."

    #the smoke is supposed to show on top of the spotsy insertion
    show smoke
    Lars narration "Spotsy responds with a subtle shiver and releases a puff of smoke as if bracing herself for the impending journey."

    Zephyr "Ouch, were you planning on blinding me with that glitter-bomb breath of yours?!"

    Lars narration "Now’s not the time to humor him, unfortunately."

    hide spotsy
    hide smoke
    show zephyr sad
    show lars serious
    Lars "I’m going to need your help, Spotsy."

    Zephyr "Hey! When did I allow you guys to leave without my permission?! I’m going to make you pay for-"

    hide lars
    #I want to time the ending of the last sentence with the upcoming sfx sound so it seems like he got caught off as spotsy smacks him. Effect-wise, once the sfx is played, he should do a slight jump and start to move downwards like he’s falling until he disappears out of the frame
    play sound sfx_smack
    Lars narration "A thwacking sound instantly rings in the air and I look back to see that our not-so-friendly ghost has been knocked to the ground looking completely unconscious."

    show lars
    Lars "Normally, I’d have to give you a scolding for smacking people like that, Spotsy. But there’s something more important at stake now."

    hide lars
    Lars narration "She murmurs and wags her tail back and forth- most likely the culprit behind Zephyr's unexpected tumble."

    show lars
    Lars "Can you please follow after Master Sylvian, Spotsy?"

    hide lars
    #black screen transition fade in/fade out
    show bg_4 with fade:
        zoom 1.5
        xalign 0.0
        yalign 0.5
    Lars narration "Spotsy instantly fluffs up her wings, taking flight. The ocean gradually shrinks beneath us as we ascend into the sky."

    #black screen transition fade in/fade out
    show bg_7 at pan with fade:
    #panning effect - sample in drive
    Lars narration "We glide through billowy clouds, soft as cotton candy, as the world below turns into a distant patchwork of greens and blues. The air feels crisp, the wind hums gently, and the sun bathes the clouds in hues of pink and blue, creating a tranquil haven above the world."

    Lars narration "Soon enough, the familiar figure of the slender magician comes into view. His silhouette, somewhat hunched at the neck but always rising to the occasion, is cross-legged at the top of a cloud."

    Lars narration "Wilting flowers have blossomed around him, bowing down in a withering manner mirroring the posture of Master Sylvian himself."

    show bg_7 at end_pan
    show lars serious
    show sylvian sad at right
    #next line, the textbox does a little up and down jump
    Lars "{bt}MASTER SYLVIAN!{/bt}"

    Lars "Can you hear me?"

    
    Lars narration "I could see his back shrivel up even more, but I couldn't hear a response while sitting on Spotsy’s back."

    Lars "If you don't respond, I might just dive into the cloud you're lounging on the count of three!"

    #next 3 lines, the textbox does a little up and down jump
    Lars "{bt}ONE!{/bt}"

    Lars "{bt}TWO!{/bt}"

    Lars "{bt}THREE!{/bt}"

    #After the last sentence, the screen does and up and down shake like he just jumped
    show bg_7:
        easein 0.2 yoffset -10
        easeout 0.2 yoffset 0
        easein 0.2 yoffset 10
        easeout 0.2 yoffset 0
    Lars narration "Determined, I leap off Spotsy's back, ready to embrace the uncertainty of landing on the cloud's flowery spots. Yet, before I can experience the leap of fate, a flurry of petals swirls beneath my dragon-riding boots, guiding my descent."

    Lars narration "The petals gracefully direct me towards Master Sylvian, aligning with my steps. As soon as he concludes his incantation, the petals disassemble, leaving me standing seamlessly on the cloud, unfazed by the unconventional landing."

    #sylvian moves to the center
    show sylvian at center with move
    Sylvian "Why…"

    Sylvian "Why are you here, [Lars]?"

    show lars serious
    Lars "I was worried for you! Why did you fly off like that in the middle of our talk? Even that ghost-faced Zephyr got scared of what you were doing."

    show lars
    Lars "You didn't need to run away like that."

    Sylvian "You're right. I guess I simply wanted to have a moment for myself."

    Lars "What’s going on, Master? This isn’t like you at all."

    Sylvian "‘Discere, cogitare, agere— the triad of wisdom’."

    Sylvian "I made that our guild motto while thinking of someone who I had yet to meet."

    Lars "Uhm, is this an appropriate time to talk about this? Shouldn’t we get back to Zephyr first?"

    Sylvian "Is that what you want, [Lars]?"

    Sylvian "Whatever choice you make, I'll do my best to respect it."

    if options["CS3"]==1:

        Sylvian "It's unfortunate that I couldn't mirror what's in my heart as I vowed to do for you..."



    Lars "Before that…shouldn’t we get back on land? I don’t want to keep Spotsy flying for too long."

    Sylvian "I don’t think I’m ready to descend yet…"

    show lars sad
    Lars "Are you upset with me, Master? Did I do something wrong?"

    Sylvian "Certainly not; it’s just a product of your imagination."

    Lars "..."

    Sylvian "I'm sorry, Lars."

    Sylvian "I'm just getting upset on my own."

    show lars
    Lars "No, it’s okay. Just tell me what you need me to do."

    show sylvian sad
    Sylvian "I-I...don't have the courage to say it out loud."

    Sylvian "I shouldn't say it to you of all people."

    Sylvian "Yet, I don't believe my heart can endure any more of this stagnation."

    Sylvian "The once tumultuous dance of butterflies' wings within my soul has ceased, leaving only the remnants of a storm's aftermath—no longer the enchanting spectacle that sets off the intricate chaos of the butterfly effect."

    show lars
    Lars "It's never too late to share what's on your brilliant mind. After all, what good is intelligence if you keep it all to yourself?"

    Sylvian "…"

    Sylvian "The truth is, [Lars], I can't help but be utterly petrified of the thought of losing you."

    Sylvian "It's a never-ending battle against the gnawing fear that I'll never quite measure up, never truly be enough for someone like you."

    show lars blush
    Lars "What are you talking about? I'm your confession partner, aren’t I? Share those pent-up emotions with me. I'm curious to know what my wise master has been hiding all this time."

    show sylvian blush
    Sylvian "Ah, you persist with that bold approach of yours. Considering this is a matter I haven't shared with anyone, I…hesitated to speak of it."

    show sylvian sad
    Sylvian "I kept pulling back whenever my emotions were close to the surface, only to regret it repeatedly in my head, convinced that what I did was wrong."

    Sylvian "Curiosity is indeed a virtue, but consider this—what if the object of your curiosity is beyond your reach?"

    Sylvian "It's a gentle reminder that our aspirations may not always align with our destiny. It is wiser to accept this truth gracefully than to diminish the value of what eludes our grasp."

    Sylvian "That's...what held me back from loving you the way you deserve."

    show lars sad
    Lars "Why do your words sound so cruel…?"

    Sylvian "Amidst the certainty of truth, lies have found a sanctuary in the hearts of those who chose to believe, even when confronted with undeniable facts."

    Sylvian "There’s an undeniable truth that I’ve been deluding myself with, but I suppose seeing your bold approach and your general choices today really made me realize the gravity of the situation."

    show lars blush
    Lars "I figured you'd enjoy my response to your subtle flirting. Given the special treatment I've been receiving from you, it only makes sense for me to inquire more about your intentions."

    Sylvian "Do you…truly mean that?"

    show lars
    Lars "Of course, when push comes to shove, all you do is run away. It's quite frustrating I have to say, so I have to step in and handle things myself, or else nothing would get done."

    Sylvian "So that’s what this is all about."

    Sylvian "It’s clear to me now…"

    Sylvian "I don’t think I have the heart to accept your pity, [Lars]. It would be devastating to know that you're wasting your time on someone like me."

    hide sylvian

    show black_feather
    Lars narration "He gracefully pulls a single feather from the folds of his wings, idly twirling it between his fingers as if lost in thought."

    Sylvian "Did you know, [Lars]? Swans form a lifelong bond with a single mate, remaining together until the bond is broken, either by death or if one of them is preyed upon."

    Sylvian "Concealing this confession might have preserved my existence, but being aware of your pity is a fate no less agonizing than succumbing to heartache."

    Sylvian "I made a solemn pledge to cherish my love for you as long as I could."

    Sylvian "If facing the sorrow of heartbreak is the consequence of your departure, then that's a burden I will shoulder by myself."

    hide black_feather
    show sylvian sad at center
    show lars sad
    Lars "You can’t say something like that, Master! I’m not going to let anything happen to you. I’ll protect you-"

    Sylvian "Some things are just out of our control, [Lars]. Even my escape from the realm of academia was such a tale."

    Sylvian "You should know that I used to adore the academic world."

    Sylvian "It was the one place where I could marvel over the many intricacies of life without feeling overwhelmed by my lack of knowledge. I would read the many scrolls, books, journals, and whatever I could get my hands on, even in the private library of the Archmage of Divonia who seldom grants people his audience."

    Sylvian "However, things started to change once I started getting the attention of other academics for my cursed achievements."

    Sylvian "Suddenly, it wasn't the endless nights of poring over my notes, hunching my back, and using my feathers as quills to jot down whatever came to mind that wore me out. Instead..."

    Sylvian "It was the jealousy and looks of hatred from my fellow magicians and academics, those whom I yearned to share my thoughts with."

    hide lars
    Lars narration "His voice starts shaking a little, and I can sense a sob that he’s trying to hold down, but his attempts are futile as tears prickle in the corner of his eyes."

    Lars narration "Here was the descendent whom I had admired as a wise and poetic leader. Yet, all this time, he held such sorrows in his heart, hidden away from everyone."

    show sylvian sad at center
    Sylvian "I, who had earned their scorn, was ostracized and couldn’t show my face in public anymore because of the nasty slurs they would throw at me."

    Sylvian "They were intelligent descendants, of course, and would never resort to physical violence if they could do what was needed with their words…"

    Sylvian "And their words were powerful, [Lars], for I was made to be a lonely swan, simply swimming on a pond with no one's company to enjoy but my own reflection in the water."

    Sylvian "No voice to hear, but the very ripples of the water that I moved on. No one to touch or embrace except the very wind that seemed to caress my feathers with the breeze. Only through flowers was I able to express myself and find a new path to choose."

    show sylvian
    Sylvian "I've always adored flowers; why they take on certain colors, where to cultivate them, it all fascinates me."

    Sylvian "When I care for them, they bloom. They leave seeds and produce a new generation of plants. They don't concern themselves with my past and never leave my side. They reciprocate what I give them, and I revel in being spoiled by their unintentional kindness."

    show lars sad
    Lars "So all this time, you had lost your self-confidence because of a bunch of know-it-alls who couldn’t bear to see you succeed?!"

    Sylvian "That’s a unique way to phrase it indeed."

    Lars "But it’s in the past now, isn’t it Master?"

    Lars "How about I give you some self-confidence tips once all this is over? I ought to do at least that much as your junior. So don’t mope around anymore like this; getting upset and crying certainly doesn't suit a leader like you."

    show sylvian sad
    Sylvian "But there’s no point to it anymore…"

    show lars blush
    Lars "Awe, are you saying that because I teased you about your love confession idea earlier? I mean, I appreciate that you trusted me enough to share your thoughts, but I guess, seeing my choices today-"

    Sylvian "I don’t think I can bear to listen to you, [Lars]..."

    Sylvian "I don’t think I can bear to listen to anyone from this point on."

    Sylvian "I'm feeling a bit embarrassed about what I just shared, and I think I'd prefer some time alone to gather my thoughts."

    show lars serious
    Lars "What’re you talking about? Who’s going to take care of the guild without you? What’s going to happen to Zephyr and the rest of the people captured by him?"

    show sylvian
    Sylvian "I'll provide him with the necessary information when we land. Sharing a couple of magician secrets won't be much trouble."

    Lars "But won’t that tarnish your reputation?"

    Sylvian "No need to worry. The Archmage will have silenced him long before any reputable gossip columns consider his story. He doesn't tolerate his academics engaging in such activities."

    Lars "What about the artifact under Zephyr’s control and the trapped descendants?"

    Sylvian "I’m confident Claude and my dear junior, Rory, have already handled that."

    Sylvian "I gave her instructions before she started her private puppet show with Zephyr earlier today, and with Claude’s extensive connections, he's likely found a solution to ease all your concerns."

    Sylvian "They are capable members of the guild, after all."

    show sylvian sad
    Sylvian "Much better than their pathetic excuse of a guild leader…"

    show lars sad
    Lars "Master…"

    Sylvian "I suppose it was an unattainable goal to desire more. I dreamt of it and lost what was already in my grasp."

    hide lars
    Lars narration "His eyes drop. Everything happened so quickly, in a way I never saw coming. Maybe he'd made up his mind before I could react, or perhaps my choices led us here. I just stare at him, feeling utterly helpless."

    Lars narration "I wish for him to meet my gaze once more, but I fear he won't lift his head again."

    show lars sad
    Sylvian "Who knows…if this feeling will eventually pass or not."

    Sylvian "Who knows…if I’ll ever be worthy of love again."

    #Sylvian - Bad End Achieved
    $ renpy.choice_for_skipping()
    $ persistent.ending[2] = 1
    "" "Sylvian - Bad End Achieved"
    jump end

label S3_sylvian_neutral_end:

    play music "track_8_neutral_ending.ogg"
    Lars narration "I should move past his comment."

    Lars narration "There are more pressing matters at hand."

    show lars
    Lars "We can discuss that later, Master Sylvian."

    show sylvian blush
    Sylvian "Oh, pardon me. Y-you can dismiss— um… I mean, feel free to forget what I just said. It was rather foolish— an error on my part to make such a bold declaration."

    Lars "Are you feeling alright? Did the tonic not calm your nerves like you wanted?"

    Sylvian "No, nothing of the sort. I-I was simply taken aback because I didn't anticipate your reaction. I suppose it's because I've become accustomed to how you always manage to say the right thing."

    Lars "That’s nice and all, but I’m not some mind reader, Master. You should just outright tell me what you want instead of looking for things that may not exist."

    Sylvian "..."

    show sylvian
    Sylvian "I suppose you're right. True power comes from within, and those who seek it elsewhere are merely fooling themselves."

    Lars "Exactly. I mean, you've already taken care of this Zephyr dilemma as best as you could, mostly by yourself."

    Lars "This just means that I brought you along for nothing, you could say. I shouldn’t have taken your hand back there."

    show sylvian sad
    Sylvian "…for nothing?"

    hide lars
    Lars narration "If my eyes weren't mistaken, it almost seemed like Master Sylvian was pouting. His eyes squinted in contemplation, and his petite beard scrunched up. A subtle furrow creased his brow, casting an endearing yet troubled expression across his features."

    show lars
    Sylvian "Tell me [Lars], is that really what you mean?"

    Lars "Come on, Master. It’s really not that serious."

    Sylvian "I suppose…it was my mistake to have expected more, I shouldn’t have indulged in my greed."

    Lars "Haha, what are you talking about, Master? Or were you planning on doing a secret confession since the beginning or something?"

    hide lars
    Lars narration "A heavy silence lingers, urging me to stick to my earlier strategy and pass over his comment once again."

    show lars serious
    Lars "Or could it be- is that why you sorted the gossip deal beforehand?"

    Lars "Seems like we’re in quite an awkward situation…"

    hide lars
    Lars narration "All at once, his expression transforms into one of horror."

    hide lars_serious
    Sylvian "I-I-I…need to leave— I need to get out of here!"

    #after the last sentence, sylvian exits from either direction
    show sylvian:
        linear 0.5 xalign 2.0
    Lars narration "He flutters his large swan wings open causing his feathers to ruffle. They catch the cold hues of the afternoon sun as he lifts off the ground and soars into the sky. The sudden display captures Zephyr's attention, prompting him to shout out."

    show zephyr sad
    Zephyr "SMARTY!"

    Zephyr "Where do you think you’re going?! You have to give me some gossip material first!"

    Zephyr "I’m not letting you get away!"

    hide all
    show spotsy
    Lars narration "But before he has the chance to grumble any further, I swiftly move to the spot where Spotsy is resting. I climb onto her back and feel the afternoon air bristling against my fur."

    #the smoke is supposed to show on top of the spotsy insertion
    show smoke
    Lars narration "Spotsy responds with a subtle shiver and releases a puff of smoke as if bracing herself for the impending journey."

    Zephyr "Ouch, were you planning on blinding me with that glitter-bomb breath of yours?!"

    Lars narration "Now’s not the time to humor him, unfortunately."

    hide spotsy
    hide smoke
    show zephyr sad
    show lars serious
    Lars "I’m going to need your help, Spotsy."

    Zephyr "Hey! When did I allow you guys to leave without my permission?! I’m going to make you pay for-"

    hide lars
    #I want to time the ending of the last sentence with the upcoming sfx sound so it seems like he got caught off as spotsy smacks him. Effect-wise, once the sfx is played, he should do a slight jump and start to move downwards like he’s falling until he disappears out of the frame
    play sound sfx_smack
    Lars narration "A thwacking sound instantly rings in the air and I look back to see that our not-so-friendly ghost has been knocked to the ground looking completely unconscious."

    show lars
    Lars "Normally, I’d have to give you a scolding for smacking people like that, Spotsy. But there’s something more important at stake now."

    hide lars
    Lars narration "She murmurs and wags her tail back and forth- most likely the culprit behind Zephyr's unexpected tumble."

    show lars
    Lars "Can you please follow after Master Sylvian, Spotsy?"

    hide lars
    #black screen transition fade in/fade out
    show bg_4 with fade
    Lars narration "Spotsy instantly fluffs up her wings, taking flight. The ocean gradually shrinks beneath us as we ascend into the sky."

    #black screen transition fade in/fade out
    show bg_7 at pan with fade
    #panning effect - sample in drive
    Lars narration "We glide through billowy clouds, soft as cotton candy, as the world below turns into a distant patchwork of greens and blues. The air feels crisp, the wind hums gently, and the sun bathes the clouds in hues of pink and blue, creating a tranquil haven above the world."

    Lars narration "Soon enough, the familiar figure of the slender magician comes into view. His silhouette, somewhat hunched at the neck but always rising to the occasion, is cross-legged at the top of a cloud."

    Lars narration "Wilting flowers have blossomed around him, bowing down in a withering manner mirroring the posture of Master Sylvian himself."

    #panning ends
    show bg_7 at end_pan
    show lars serious
    show sylvian sad at right
    #next line, the textbox does a little up and down jump
    Lars "MASTER SYLVIAN!"

    Lars "Can you hear me?"

    hide lars
    Lars narration "I could see his back shrivel up even more, but I couldn't hear a response while sitting on Spotsy’s back."

    show lars
    Lars "If you don't respond, I might just dive into the cloud you're lounging on the count of three!"

    #next 3 lines, the textbox does a little up and down jump
    Lars "{bt}ONE!{/bt}"

    Lars "{bt}TWO!{/bt}"

    Lars "{bt}THREE!{/bt}"

    #After the last sentence, the screen does and up and down shake like he just jumped
    hide lars
    Lars narration "Determined, I leap off Spotsy's back, ready to embrace the uncertainty of landing on the cloud's flowery spots. Yet, before I can experience the leap of fate, a flurry of petals swirls beneath my dragon-riding boots, guiding my descent."

    Lars narration "The petals gracefully direct me towards Master Sylvian, aligning with my steps. As soon as he concludes his incantation, the petals disassemble, leaving me standing seamlessly on the cloud, unfazed by the unconventional landing."

    #sylvian moves to the center
    show sylvian at center with move
    Sylvian "Why…"

    Sylvian "Why are you here, [Lars]?"

    show lars serious
    Lars "I was worried for you! Why did you fly off like that in the middle of our talk? Even that ghost-faced Zephyr got scared of what you were doing."

    show lars
    Lars "You didn't need to run away like that."

    Sylvian "You're right. I guess I simply wanted to have a moment for myself."

    Lars "What’s going on, Master? This isn’t like you at all."

    Sylvian "‘Discere, cogitare, agere— the triad of wisdom’."

    Sylvian "I made that our guild motto while thinking of someone who I had yet to meet."

    Lars "Uhm, is this an appropriate time to talk about this? Shouldn’t we get back to Zephyr first?"

    Sylvian "Is that what you want, [Lars]?"

    Sylvian "Whatever choice you make, I'll do my best to respect it."

    if options["CS3"]==1:

        Sylvian "It's unfortunate that I couldn't mirror what's in my heart as I vowed to do for you..."



    show lars
    Lars "Are you upset with me, Master? Did I do something wrong?"

    Sylvian "Certainly not; it’s just a product of your imagination."

    Lars "..."

    Sylvian "I'm sorry, Lars."

    Sylvian "I'm just getting upset on my own."

    show lars
    Lars "No, it’s okay. Just tell me what you need me to do."

    show sylvian sad
    Sylvian "I-I...don't have the courage to say it out loud."

    Sylvian "I shouldn't say it to you of all people."

    Sylvian "Yet, I don't believe my heart can endure any more of this stagnation."

    Sylvian "The once tumultuous dance of butterflies' wings within my soul has ceased, leaving only the remnants of a storm's aftermath—no longer the enchanting spectacle that sets off the intricate chaos of the butterfly effect."

    show lars
    Lars "It's never too late to share what's on your brilliant mind. After all, what good is intelligence if you keep it all to yourself?"

    Sylvian "…"

    Sylvian "The truth is, [Lars], I can't help but be utterly petrified of the thought of losing you."

    Sylvian "It's a never-ending battle against the gnawing fear that I'll never quite measure up, never truly be enough for someone like you."

    show lars
    Lars "What are you talking about? I’m your friend, aren’t I? We already talked about this, didn’t we? You shouldn’t be undermining yourself like this."

    Sylvian "Ah, just as a friend, is that right…"

    Sylvian "Well, I suppose it’s my fault too since I never had the courage to state what I wanted to be with you… that’s precisely why I hesitated to speak of it."

    Sylvian "Then again, even the title of a 'friend' might be too much for someone like me."

    Sylvian "Amidst the certainty of truth, lies have found a sanctuary in the hearts of those who chose to believe, even when confronted with undeniable facts."

    Sylvian "There’s an undeniable truth that I’ve been deluding myself with, but I suppose having you pass over my comment and your general choices today really made me realize the gravity of the situation."

    show lars serious
    Lars "But I had a reason behind passing over what you said because there are more important things at stake here."

    Lars "I have a responsibility to uphold and need to take care of the people around me. Seeing both descendants and humans smile while under my care fills me with joy. It’s my philosophy of being the bridge between dragons and passengers, a legacy I’m honored to leave behind."

    Lars "That’s why, while I understand where your romantic intentions are coming from, I can’t give you a response right now amidst all this drama. I still–"

    show lars sad
    Sylvian "That’s enough, [Lars] ..."

    Sylvian "It appears that all that lies ahead for me is finding contentment in what's within my reach."

    Lars "Within your reach…?"

    show sylvian sad
    Sylvian "Allow me to share a piece of poetry with you, [Lars]. One that's nestled in the deepest recesses of my heart."

    Sylvian "“In the garden of solitude, I wander lost. A traveler without companions, I pay the cost. The nightingale’s melody, though sweet and clear, fails to reach the desolation I hold dear."

    Sylvian "“In the garden of solitude, I remain. A heart that longs for love’s sweet refrain. Oh, how I yearn for a friend so true. To end this solitude, to start anew.”"

    show lars blush
    Lars "That’s truly beautiful, Master."

    show lars
    Lars "But…what does it have to do with you?"

    show sylvian sad
    Sylvian "In my pursuit of profound truths, I found myself chasing the distant winds, oblivious to the wisdom carried by the nearby breeze."

    Sylvian "I sought friendship as if it were a dream, blind to the companionship that surrounded me, even if it fell short of the true friendship I imagined day and night."

    Sylvian "Such is the nature of existence, where I must accept what is, for I cannot alter the course of destiny. I should have simply valued what was in the palm of my hand instead of yearning for more."

    show lars sad
    Sylvian "This is the fate that I must accept for I am worthy of no other."

    
    show black_feather
    hide sylvian
    Lars narration "He gracefully pulls a single feather from the folds of his wings, idly twirling it between his fingers as if lost in thought."

    Sylvian "Did you know, [Lars]? Swans form a lifelong bond with a single mate, remaining together until the bond is broken, either by death or if one of them is preyed upon."

    Sylvian "Concealing this confession might have preserved my existence, but being aware of your pity is a fate no less agonizing than succumbing to heartache."

    Sylvian "I made a solemn pledge to cherish my love for you as long as I could."

    Sylvian "If facing the sorrow of heartbreak is the consequence of your departure, then that's a burden I will shoulder by myself."

    hide black_feather
    show sylvian sad at center
    show lars sad
    Lars "You can’t say something like that, Master! I’m not going to let anything happen to you. I’ll protect you-"

    Sylvian "Some things are just out of our control, [Lars]. Even my escape from the realm of academia was such a tale."

    Sylvian "You should know that I used to adore the academic world."

    Sylvian "It was the one place where I could marvel over the many intricacies of life without feeling overwhelmed by my lack of knowledge. I would read the many scrolls, books, journals, and whatever I could get my hands on, even in the private library of the Archmage of Divonia who seldom grants people his audience."

    Sylvian "However, things started to change once I started getting the attention of other academics for my cursed achievements."

    Sylvian "Suddenly, it wasn't the endless nights of poring over my notes, hunching my back, and using my feathers as quills to jot down whatever came to mind that wore me out. Instead..."

    Sylvian "It was the jealousy and looks of hatred from my fellow magicians and academics, those whom I yearned to share my thoughts with."

    hide lars
    Lars narration "His voice starts shaking a little, and I can sense a sob that he’s trying to hold down, but his attempts are futile as tears prickle in the corner of his eyes."

    Lars narration "Here was the descendent whom I had admired as a wise and poetic leader. Yet, all this time, he held such sorrows in his heart, hidden away from everyone."

    show sylvian sad at center
    Sylvian "I, who had earned their scorn, was ostracized and couldn’t show my face in public anymore because of the nasty slurs they would throw at me."

    Sylvian "They were intelligent descendants, of course, and would never resort to physical violence if they could do what was needed with their words…"

    Sylvian "And their words were powerful, [Lars], for I was made to be a lonely swan, simply swimming on a pond with no one's company to enjoy but my own reflection in the water."

    Sylvian "No voice to hear, but the very ripples of the water that I moved on. No one to touch or embrace except the very wind that seemed to caress my feathers with the breeze. Only through flowers was I able to express myself and find a new path to choose."

    show sylvian
    Sylvian "I've always adored flowers; why they take on certain colors, where to cultivate them, it all fascinates me."

    Sylvian "When I care for them, they bloom. They leave seeds and produce a new generation of plants. They don't concern themselves with my past and never leave my side. They reciprocate what I give them, and I revel in being spoiled by their unintentional kindness."

    show lars sad
    Lars "So all this time, you had lost your self-confidence because of a bunch of know-it-alls who couldn’t bear to see you succeed?!"

    Sylvian "That’s a unique way to phrase it indeed."

    Lars "But it’s in the past now, isn’t it Master?"

    Lars "How about I give you some self-confidence tips once all this is over? I ought to do at least that much as your junior. So don’t mope around anymore like this; getting upset and crying certainly doesn't suit a leader like you."

    show sylvian sad
    Sylvian "I suppose that marks my confession as null."

    show lars
    Lars "I wouldn't say that. I appreciate your trust in sharing your thoughts with me. However, considering my choices today, I don't think I'm ready to embrace the romantic aspect of your affection."

    Lars "For now, I believe it's best that we remain master and junior, and if you’ll let me continue, I’d want to remain as your friend."

    Sylvian "Of course, it's like that. Even if he realizes that I'm in love with him… to him, I'm just his friend, his senior colleague."

    Lars "What was that, Master?"

    Sylvian "N-n-nothing of importance."

    show lars serious
    Lars "Now then, what do we do about Zephyr though?"

    show sylvian
    Sylvian "I’ll give him the gossip he needs when we get down to land."

    show sylvian
    show sylvian
    Sylvian "I'll provide him with the necessary information when we land. Sharing a couple of magician secrets won't be much trouble."

    Lars "But won’t that tarnish your reputation?"

    Sylvian "No need to worry. The Archmage will have silenced him long before any reputable gossip columns consider his story. He doesn't tolerate his academics engaging in such activities."

    Lars "What about the artifact under Zephyr’s control and the trapped descendants?"

    Sylvian "I’m confident Claude and my dear junior, Rory, have already handled that."

    Sylvian "I gave her instructions before she started her private puppet show with Zephyr earlier today, and with Claude’s extensive connections, he's likely found a solution to ease all your concerns."

    Sylvian "They are capable members of the guild, after all."

    Lars "That’s what friends are for, right? Thanks to them, we ended up with the safest option."

    Sylvian "Indeed, what an outcome…"

    $ renpy.choice_for_skipping()
    $ persistent.ending[1] = 1
    " " "Sylvian - Neutral End Achieved"
    jump end

label S3_sylvian_good_end:
    play music "track_7_good_ending.ogg"
    Lars narration "I should stay silent for now."

    show lars
    Lars "…"

    Sylvian "Don’t you..wish to know more?"

    hide lars
    Lars narration "His words linger in the air while the wind stands still. A wistful sigh escapes his lips, followed by a subtle smile."

    show lars
    Lars "I didn’t want to pressure you into saying something you didn’t want to."

    show sylvian
    Sylvian "...It’s simply amazing—"

    Lars "What is?"

    show sylvian blush
    Sylvian "—how you effortlessly make me feel at ease, even in silence."

    show sylvian
    Sylvian "‘Discere, cogitare, agere— the triad of wisdom’."

    Sylvian "I made that our guild motto while thinking of someone who I had yet to meet."

    Lars "What do you mean, Master?"

    Sylvian "Learning enriches the mind, and thinking sharpens it, but it is through action that we truly manifest our knowledge and shape our reality."

    Sylvian "In envisioning the principles I wanted to embody, the person I admired played a significant role. Someone who would never hesitate to learn more despite their ever-expanding knowledge. A sharp mind that wouldn't confine itself to merely fulfilling tasks."

    Lars "You already embody those ideals, don’t you?"

    Sylvian "There’s still a certain component left for me to achieve — the action needed to manifest knowledge and wit. However, I failed to do that in many ways."

    show sylvian
    show lars
    Lars "You’ve already done so much, Master! You’ve always worked very hard for everyone in the guild."

    Lars "You don't need me to tell you this, but...none of the things we do would ever be possible without you."

    show sylvian sad
    Sylvian "Surely, it would. Once there's nothing more for me to do, I'll be left alone again, naturally."

    show lars sad
    Lars "You know that isn’t true."

    Sylvian "It is, though. I speak of cherishing our current contentment, but what value is there in doing so if I’m aimlessly wandering without purpose?"

    Lars "Please, Master, you should know better than to trust those negative thoughts which do you no good."

    show sylvian blush
    show lars blush
    Lars "You're the one who consistently leads us on our expeditions, the very leader who keeps our guild afloat."

    Lars "Not to mention, the warm welcome you give us whenever we return, that feeling of being home wouldn’t work with anyone else! Do you understand what I mean right now?"

    Sylvian "You're a good one, aren't you, [Lars]?"

    Sylvian "Makes me want you for myself even more…"

    show lars happy
    Lars "Master…I-I feel the same way—"

    Sylvian "I know I'm not worthy of your attention. You're probably saying those things because I’m your superior, am I right?"

    Lars "Why entertain such thoughts when I'm telling you myself? So, just listen to me, and don't let those negative thoughts confuse your mind!"

    hide lars
    Lars narration "It may be a tad late, but my ears are curling up from the embarrassment of it all."

    show lars happy
    Sylvian "[Lars]..."

    Lars narration "There's no turning back now. Despite his academic brilliance, he seems to struggle with recognizing his own worth. It's time for me to be straightforward with him."

    show lars
    Sylvian "The value of companionship, even in its simplest form, should not be dismissed."

    Sylvian "But…what if I told you I don’t want to be only your friend anymore? What if I want to reach out for something more?"

    if options["CS3"]==1:

        Sylvian "You inquired about the meaning behind the flowers and poems I've shared with you, didn't you? I made a promise to lay my heart bare, and I can't muster the courage to keep my secrets from you any longer."

        show sylvian blush
        Sylvian "“Between the mirror and the heart is this single difference: The heart conceals secrets, while the mirror does not.”"

        Sylvian "It's time for me to show you what truly reflects in my heart."

        hide lars
        Lars narration "His hands are clenched tight, and the rhythmic rise and fall of his Adam's apple mirrors his palpable anxiety."

        show sylvian
        Sylvian "You shouldn't worry yourself, [Lars]."

        show sylvian blush
        Sylvian "That beautifully groomed tail of yours is so full of static [Lars], perhaps you’ve already picked on some of my clues."

        show lars blush
        Lars "I—I don't know when I started noticing your gifts and how they were specific to me."

        show sylvian sad
        Sylvian "That's to be expected, of course. It's my fault that—"

        show lars happy
        show sylvian blush
        Lars "But I always felt special when you gave them to me, as if we had this unbreakable bond that was only between the two of us."

        Lars "Even today, when you gave me that bouquet for my safe return. I may not be well-versed in the art of flower arrangement or knowledgeable in their names and meanings, but I can always appreciate the effort you put into preparing them."

        Sylvian "I'm curious about how you'd react if you knew the meaning behind those flowers. Attaching significance to things that may not hold as much meaning for others has been my unfortunate philosophy for some time now."

        Lars "Why don’t you tell me? I’m curious to know. Maybe I could even share it with my dragons next time around."

        Sylvian "I've always held an envy of the way they held your attention. There were even days where I dreamt I could replace them and be the sole recipient of your attention."

        Sylvian "Yet, I fear you might see me as someone who has lost his mind."

        hide lars
        Lars narration "His unexpected boldness takes me by surprise. Whether it's the influence of the earlier drink or a newfound resolve, his declaration resonates within me. My heart pounds louder, with my tail mirroring its pulse."

        #show lars happy


    if options["CS3"]==2:

        show sylvian sad
        Sylvian "The truth is, you inquired Claude about a potential gift, right? It pains me to realize that everything I've given so far may never measure up to what he could potentially offer."

        show lars
        Lars "You shouldn't bring yourself down like that."

        Lars "I asked Sir Claude because that's what I was curious about most at that moment."

        Sylvian "I understand, [Lars]. There’s no need for you to explain yourself. You’re free to pick and do what you want."

        Sylvian "I was simply scolding myself…"




    show sylvian
    Lars narration "An awkward silence envelops the air. Even someone as clueless as Zephyr turns back to look at us and see what's going on. But before he has the chance to say anything, Master Sylvian speaks up again."

    show sylvian
    Sylvian "I suppose it’s time to share the secrets from my past if we are to follow through on this path of clarity."

    hide lars
    Lars narration "A sigh escapes him, and he slowly shakes his head, lifting his gaze to the expanse of the sky above."

    show lars
    Sylvian "You should know that I used to adore the academic world."

    Sylvian "It was the one place where I could marvel over the many intricacies of life without feeling overwhelmed by my lack of knowledge. I would read the many scrolls, books, journals, and whatever I could get my hands on, even in the private library of the Archmage of Divonia who seldom grants people his audience."

    Sylvian "However, things started to change once I started getting the attention of other academics for my cursed achievements."

    Sylvian "Suddenly, it wasn't the endless nights of poring over my notes, hunching my back, and using my feathers as quills to jot down whatever came to mind that wore me out. Instead..."

    Sylvian "It was the jealousy and looks of hatred from my fellow magicians and academics, those whom I yearned to share my thoughts with."

    hide lars
    Lars narration "His voice starts shaking a little, and I can sense a sob that he’s trying to hold down, but his attempts are futile as tears prickle in the corner of his eyes."

    Lars narration "Here was the descendent whom I had admired as a wise and poetic leader. Yet, all this time, he held such sorrows in his heart, hidden away from everyone."

    show sylvian sad at center
    Sylvian "I, who had earned their scorn, was ostracized and couldn’t show my face in public anymore because of the nasty slurs they would throw at me."

    Sylvian "They were intelligent descendants, of course, and would never resort to physical violence if they could do what was needed with their words…"

    Sylvian "And their words were powerful, [Lars], for I was made to be a lonely swan, simply swimming on a pond with no one's company to enjoy but my own reflection in the water."

    Sylvian "No voice to hear, but the very ripples of the water that I moved on. No one to touch or embrace except the very wind that seemed to caress my feathers with the breeze. Only through flowers was I able to express myself and find a new path to choose."

    show sylvian
    Sylvian "I've always adored flowers; why they take on certain colors, where to cultivate them, it all fascinates me."

    Sylvian "When I care for them, they bloom. They leave seeds and produce a new generation of plants. They don't concern themselves with my past and never leave my side. They reciprocate what I give them, and I revel in being spoiled by their unintentional kindness."

    show lars sad
    Lars "So all this time, you had lost your self-confidence because of a bunch of know-it-alls who couldn’t bear to see you succeed?!"

    Sylvian "That’s a unique way to phrase it indeed."

    show lars serious
    Lars "You should have told me this sooner, Master; I would have given them a piece of my mind. Or better yet, a torching session with Spotsy’s help would have done the job perfectly."

    show lars
    #textbox shake for the next line + sylvian’s sprite does an up and down jump a few times
    Sylvian "{sc}Hahahaha!{/sc}"

    show sylvian blush
    Sylvian "Ah, [Lars], what would I do without you…"

    Sylvian "I’m glad to have shared these thoughts with you. It’s true that I gained a sense of insecurity from those events."

    show sylvian
    Sylvian "My solitude used to be a burden I carried alone, but it led me to seek companionship,  resulting in the creation of our guild."

    Lars "It's a common struggle, isn't it? I always feel a bit uneasy when I start boarding people onto a dragon ship, fearing that I might not meet their expectations."

    Lars "The same goes for taking care of dragons. There's always that doubt about whether I'm doing a good job, and it was no different when we first got Spotsy."

    Lars "But the key is to overcome those doubts. You're the one who spends the entire day with... well, yourself. So, finding your self-worth from within just makes sense."

    show lars blush
    Lars "We'll obviously take care of you whenever we can. Especially me, of course! I'm not dense enough not to pick up on your little shows of affection, especially with how much time we spend together."

    Lars "But…you have to make the final decision yourself on what you want us to be."

    show sylvian blush
    Sylvian "I-I…"

    hide lars
    hide sylvian
    Lars narration "I hold my breath in anticipation when suddenly, he wraps me in a solid embrace."

    
    #Do a little fade and insert cg_slyvian_good + some cinematography effect
    #camera foScuses on Sylvian -does a little pan - right to left
    
    show cg_lars_sylvian_ge:
        xalign 0.5
        yalign 0.5
        zoom 2.0
        linear 6.0 zoom 1.0

    Lars narration "His touch, though sweaty and trembling, carries an irresistible loveliness. The subtle bump on his middle finger from his days in academia and the grazings and minor calluses of his palm from his magical experiments all seem to capture my attention."

    Lars narration "As our fingers entwine, he bestows upon them a gentle kiss, his eyes closing in reverence."

    Sylvian "What a joy it is to lean on you at this moment."

    Lars "You'll get to do that even more in the future."

    Sylvian "Even now, this is enough. I'm afraid of being greedy. I saw what it did back when I tried to achieve more."

    Lars "Shh, there's no need to reminisce on those bad memories."

    Sylvian "Do...do I really deserve to be spoiled by you like this? Is it fine to cherish this moment and aim to have even more momentous occasions like this with you, by my side?"

    Lars narration "The fear of meeting his glistening eyes holds me back. I know it will stir my own emotions, yet, for the moment, I must play the role of the steady anchor for this newfound love."

    Lars narration "He kisses my fingers again, a subtle execution with reverent trembling and closed eyes. There's a slow sensuality about him, and as his gaze creeps up to meet mine, a charged connection lingers in the air."

    Sylvian "You are the only thing right [Lars], the only correctly placed puzzle piece in this life of mine."

    Lars "Do you really mean that, Master?"

    Sylvian "Believe me, [Lars]. I pledge to love you for eternity and beyond."

    Sylvian "The courage that my lovely companion, the vision of my dreams, my hero, has given me, I will never betray it. The way you protect others, empathize with those around you, and never give up on those who don’t believe in themselves."

    Sylvian "What did I do to earn an ever-lasting bloom like you?"

    #camera focuses on lars -does a little pan - left to right
    Lars "Shhh…didn't you say that you’d stop demeaning yourself? I can’t spoil you like this, now can I?"

    Sylvian "Hearing such a declaration... seems like I might start to like myself, just a little bit."

    Sylvian "I tend to like the things that the person I love is fond of."

    Lars "Then I plan to love you even more than you can imagine."

    Sylvian "Seems like I have to start liking myself more then."

    #zoom out to the entire scene
    show bg_5
    show sylvian blush
    Lars narration "He leans in and rests his head on my chest, seeing as how I was taller than him.  I want to ruffle those wings of his. I wonder how that would feel."

    Lars narration "I bring up my hand to the top of his wings, delicately brushing the tip of a wing feather. I sense a slight tension, prompting me to scoot closer to his side, where I feel the warmth emanating from his body."

    Lars narration "My hand continues its journey, gliding from the notch to the upcurved edge of his barbs where the shafts converge. At times, I flutter my touch along the inner vanes of his feathers, punctuating the sensation with gentle kisses."

    Lars narration "It's a breathtaking experience, a privilege to touch these magnificent wings and witness his face squirm and flush with each tender movement."

    Lars "You’re so beautiful…"

    Lars "Can I..."

    Lars "...kiss you, Master?"

    Lars narration "He almost seems to stagger from my question, staying in silence for a brief moment before recovering his composure."

    Sylvian "That would be a dream, but not right now. My heart is beating far too loudly for me to keep calm and share a proper first kiss with you. Let’s take it slow, shall we?"

    Lars narration "No other words are needed as I gently cup him in my arms. The gesture seemed to have appeased him as a flurry of blossoms rained and enveloped us."

    Lars "What do we do about Zephyr, then?"

    #zephyr’s happy sprite appears where lars’s side sprite usually is because I don’t want to ruin the CG
    show zephyr happy at left
    Zephyr "I’ve been acting like a third wheel all this time, hehe. You guys just focus on your lovey-dovey confession scene. I’m gathering gossip material as is."

    Zephyr "“The renowned scientist —or should I say, swan-tist— and his ice-pectacle love confession”. The gossip mill will have a field day with this!"

    hide zephyr
    Lars narration "I lift Master Sylvian's chin, fixing him with a somewhat serious gaze."

    show lars blush
    Lars "But won’t that tarnish your reputation?"

    Sylvian "No need to worry. The Archmage will have silenced him long before any reputable gossip columns consider his story. He doesn't tolerate his academics engaging in such activities."

    Lars "What about the artifact under Zephyr’s control and the trapped descendants?"

    Sylvian "I’m confident Claude and my dear junior, Rory, have already handled that."

    Sylvian "I gave her instructions before she started her private puppet show with Zephyr earlier today, and with Claude’s extensive connections, he's likely found a solution to ease all your concerns."

    Sylvian "They are capable members of the guild, after all."

    Lars "Indeed they are, and the end result is even better with you by my side, Master."

    Sylvian "Thank you [Lars]..."

    Sylvian "I…I love you, my everlasting bloom."

    #screen fades to black and the next line appears in the textbox, music also fades into silence
    $ renpy.choice_for_skipping()
    $ persistent.ending[0] = 1
    " " "Sylvian - Good End Achieved"
    jump end

label claude_route:
    show zephyr happy at left
    show claude at center_left
    show sylvian at center_right
    show rory at right
    show lars
    Zephyr "Did you pick someone already? I need something big to spark my gossip debut if I plan to pay off my debt and renovation costs with your confession shenanigan."

    hide lars
    Lars narration "I grab Sir Claude's hand in mine and interlace our fingers as I raise them up for Zephyr to see."

    show lars
    Lars "I choose him."

    #here the arrangement will change as sylvian gets turned into sylvian_sad during the last sentence and then he exits the scene. Claude will move to the center, rory  and zephyr will be in the same position
    show sylvian sad:
        linear 1.0 xalign 2.0
    show claude smile at center with move
    Claude "It appears that the Captain [Lars] has quite the discerning eye. I’m honored to be beheld by it."

    Zephyr "So, Slicky it is then!"

    Zephyr "Now tell me, what makes him so special? How's the scoop going to be different from all the other celebrity gossip columns and panels?"

    Sylvian "Well, he’s  a renowned merchant—"

    show sylvian serious funny
    show zephyr sad at left
    Zephyr "Boring! Anyone could just slap a make-shift title for themselves; that doesn't make you’re gossip-worthy."

    Rory "Claude here is the heir of the infamous Dupont family, even though he might deny being a nepo baby. They're always globe-slithering, selling exotic trinkets for the price of a whole wing and tail."

    show claude shocked at center
    Claude "Little Rory, you could have at least tried a more subtle approach to throw me under the dragon ship."

    Rory "Payback time~"

    Zephyr "That does indeed sound like a juicy tale for the gossip mill — the tail-smacking adventures of Slicky — but it's missing something.  Perhaps a love confession would…"

    Rory "Ah, he wouldn't be able to do that. After all, his name starts with a 'C' for conceited and ends with an 'E' for egotistical."

    show claude smile at center
    Claude "You're having me in splits, little Rory; I might even consider doing a tail-shedding ceremony just to honor your sense of humor."

    show rory angry at right
    Rory "Hmph, It was about time I gave you a taste of your own medicine!"

    show lars serious
    Lars "Before we get started on anything, didn't you promise that you'd unfreeze the others?"

    hide lars
    Lars narration "I don't want to risk getting the other guild members hurt, and more importantly, I don't want anyone else suffering from the time freeze's effects."

    show lars serious
    Zephyr "Fineeee, I wouldn't dishonor my family by breaking my oaths, but you better cough up a scoop worthy of my undivided attention!"

    Zephyr "Let's spice up the setting while we're at it; I wouldn't want someone else to hijack my headline when I finally release them from their frozen state. Scouty, pick a fancy locale, won't you?"

    hide all
    #black screen transition fade in/fade out
    show bg_4 with fade
    Lars narration "The sun is gradually sinking towards the horizon, casting cold hues across the sky as late afternoon approaches."

    show zephyr sad at left
    show claude at center
    Zephyr "Whose brilliant idea was it to ride a dragon for a confession scene?"

    show lars serious
    Lars "You wanted a place with few to no people, and here we are."

    show zephyr happy at left
    Zephyr "Whatever! I'm focusing on steering this ship but I've got my eyes and ears on you two. Make it count while we're down here."

    hide lars
    #zephyr exits the scene, and claude stays in the center
    Lars narration "I shoot a glance at Sir Claude and bite my lips in frustration. I chose him as my partner, but with Zephyr so close by, I'm unsure of our next move."

    hide zephyr
    show lars
    Lars "There’s not much time, we have to do something."

    show claude smile
    Claude "I could do a skydiving trick from up here. The tabloids would have a field day if I were to fall off under these conditions."

    hide lars
    Lars narration "I cross my arms, determined to make Sir Claude understand the gravity of the situation. However, the more serious I try to be, the more my anxiety seems to rise."

    Lars narration "I should at least avoid giving him any more ammunition for teasing me. Best to keep my tail perfectly still. As for my fox ears, well, I can only hope they won’t start drooping and betray my inner turmoil."

    show lars
    Lars "Zephyr would be quite upset if we only got noticed for your publicity stunt rather than a confession or comedy routine."

    Claude "I doubt we can do comedy under these conditions. So a confession it is then!"

    Claude "Unless I resort to my old jokes or something."

    Lars "Ughh, at this rate, we're going to be renovation slaves."

    Claude "Picture this - \"The Renovation Duo\" - I'll tell my terrible jokes, and you can loudly groan as we paint walls and fix leaky pipes for a rundown castle."

    Lars "We should strive to leave an impression on Zephyr that goes beyond shoddy repair work."

    Lars "Imagine what would become of your family legacy if word got out about our current dilemma…"

    hide lars
    show claude shocked
    Lars narration "Sir Claude, as he always does, theatrically places a hand on his chest, feigning deep offense at my comments. Despite my attempt to maintain seriousness, I couldn't help but crack a smile at his playful antics."

    show lars blush
    Claude "Tsk, tsk, Captain, you should know that all publicity is good publicity, it’s the standard industry cliché."

    show claude smile
    Claude "It’s because I only ever seek to be the greatest merchant there is that I will use every tool at my disposal to achieve it."

    hide lars
    Lars narration "Hmph, the same audacious statements, as always. Even under pressure, Sir Claude remains the unwavering bold merchant and adventurer that he is."

    Lars  narration "It was a quality of his that I deeply admired and aspired to learn from."

    Lars narration "In a realm where courage and determination were paramount, witnessing someone like him fearlessly chasing after his dreams was truly inspiring, and it ignited a fire within me to pursue my own aspirations with equal fervor."

    show lars
    Lars "Really? I didn’t know our noble scion liked being the center of attention. You always seem to be hiding that you’re the only heir of the infamous Dupont merchant family."

    Lars "At first, I thought it was so there wouldn’t be any rumors of our Guild being associated with your family name, but you’ve always been acting suspiciously about it."

    Lars "You never seem to give out your last name during our expeditions or client meetings and even before, with Zephyr—"

    show claude shocked
    Claude "Captain, I didn’t think you were interested in my personal life all that much."

    show claude smile:
        linear 1.0 zoom 1.1
    #claude’s sprite comes closer to the screen a little
    hide lars
    Lars narration "Wow, his voice is so close...I can't believe how quickly he closed the gap between us. Did he do it while I was lost in my rambling? Now, his forehead is almost touching mine, and his eyes…"

    Lars narration "His  piercing golden eyes are fixed directly on me. Why’s he looking at me like that? Ugh, this isn’t good for my heart."

    show lars blush
    Claude "I could satisfy your curiosity by merely saying that I enjoy the challenge of forging my own legacy."

    #claude’s sprite goes back to original position
    Claude "But then, you'll have to satisfy my curiosity as well – what's the reason behind that little wagging tail you're trying to hide so adorably?"

    Lars narration "My embarrassment skyrockets as the heat rushes to my cheeks. A quick glance at my tail confirms my nerves, as it wags uncontrollably behind me. Desperately, I begin  searching for a way to divert his attention."

    Lars narration "The line blurs between his teasing and genuine flirtation, leaving me defenseless against his charm, even when he playfully passes it off as a joke. Succumbing to his allure is something I’d rather avoid, having witnessed how easily others have fallen for him."

    show lars blush
    #textbox jumps and down for next sentence
    Lars "THEN I SUPPOSE...you wouldn't mind if the headlines read something like this–"

    Lars "“Claude Dupont, the shining star of the Commerce Guild 'Custodes Sylvae’, scion of the infamous merchant family, tragically falls to his death.”"

    Lars "“The consequence of enraging the esteemed dragon pilot [Lars].”"

    Lars "“Aiming for the skies, only to plummet into the depths of the sea.”"

    show claude smile
    #claude’s sprite does an up and down jump for the laughing part of the next sentence
    Claude "Haha, are you getting shy Captain? Or did you pick up those catchy headline titles from your human passengers again?"

    show lars serious
    #textbox jumps and down for next sentence
    Lars "Firstly, NO I WASN’T!"

    show lars
    Lars "Secondly, you have to admit, it does carry a certain dramatic flair."

    Claude "Ah, my dear Captain, I’ll oblige to your lie. You always know how to spin an intriguing tale, after all."

    hide lars
    Lars narration "In the blink of an eye, Sir Claude's hand cups one side of my cheek, and a rush of self-consciousness floods my senses. His touch, though cold and scaly, carries an irresistible sensation."

    show claude blush
    Claude "I've missed talking with you like this, Captain. I've been occupying myself with so many tasks that I haven't had the chance to appreciate our time together like this."

    show lars blush
    Lars "You could always skip them, you know? Taking some time to settle down might do you good."

    Claude "Ah, you see, I’m just too restless for that. I’d rather bask in the glory of achieving a dream, rather than the journey towards attaining it."

    Claude "There's something captivating about that period in-between, where aspirations linger and possibilities seem endless."

    Claude "Not to mention, I have no intention of letting you share your company with anyone else."

    Lars "It’s more like, I’m the only one who can keep up with your reckless antics in the first place."

    Claude "Haha that’s right. Maybe…it’s time to confess my secret after all, better seize the moment while it lasts before my antics become too much for you."

    hide lars
    Lars narration "Though well-known for his love of humor and jest, this time, his response carries an unmistakable sincerity. What could he possibly mean, though?"

label menu_c3:
    menu:
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
    play music "track_7_good_ending.ogg"
    Lars narration "I should poke further about his comment."

    show claude serious
    show lars
    Lars "What do you mean, Sir Claude?"

    hide lars
    Lars narration "To my astonishment, a subtle shadow of melancholy dances in his eyes, and the corners of his lips, usually curved upwards, now descend."

    show lars blush
    Claude "Admit it, you were barely containing your curiosity about my secret confession, weren't you? My darling little fox."

    if options["CS3"]==1:

        show lars
        Lars "I remember asking about Master Sylvian’s during our talk about gifts , but not about yours, so—"

        show claude serious
        #for the next line, claude does a side to side shake + a jump. Preferably, he does a shake to the left from ‘It’s always Sylvian this’ and does another shake from ‘and Sylvian that’, then does a jump from ‘Why can't I ever catch a break from him?’
        Claude "It’s always Sylvian this and Sylvian that. Why can't I ever catch a break from him?"

        show lars serious
        Lars "What's going on? Why the sudden—"

        Claude "You know what? I can't take this anymore."



    if options["CS3"]==2:

        show claude smile
        Claude "Recall that promise I made about sharing everything once we're alone? If memory serves me right, you were quite eager to unravel my secrets at the time, weren’t you?"

        show lars blush
        Lars "That's not true! I only wanted you to know that I'm here for you as a friend and fellow guild member, should you ever want to share—"

        Claude "Haha, I'm just joking, [Lars]. I understand your intentions well enough. Your close bond with dragons is the reason behind your sincere way of talking, isn’t that right? I’ve admired that for some time now…"

        hide lars
        Lars narration "He admires something about me? He's certainly teased me so much till now that I've grown accustomed to not receiving any honest praise from him."

        show lars
        Lars "Well, yes, you’re right. My parents would always tell me to be direct with my words, as dragons can have trouble reading your intentions if you're not straightforward or heartfelt in your interactions."

        Lars "So, it would be best to just say what’s on your mind, which is kind of what I’m doing. But then again, I’m supposed to be the dragon trainer here, not you—"

        show lars sad
        Lars "Ugh, forget it. You were probably just teasing me again."

        show lars blush
        Claude "I didn't say I had special feelings for you just for the sake of it, I was quite serious. To show my resolve, I'll fulfill my promise right here and now, just as I swore on that necklace I gave you."



    show lars
    show claude
    Claude "[Lars]."

    Claude "I need you to listen to me carefully."

    hide lars
    Lars narration "He rarely ever shows his vulnerability, so witnessing this side of him is…"

    show lars
    Claude "You remember how I've always skirted around the fact that I'm a Dupont heir?"

    Lars "Yes, it's been a constant mystery to me."

    show claude sad
    Claude "Well, the truth is, I've avoided mentioning it because...I didn't want to be defined by that name."

    show lars sad
    Claude "I've always struggled with titles and appearances growing up."

    Claude "The burden of being the Dupont family heir, with its myriad of expectations,  it all felt like a shallow act that I had to uphold, and I...I felt imprisoned in that superficial world."

    hide lars
    Lars narration "His voice quivers with emotion, and I'm completely engrossed, giving him unwavering attention, determined not to shatter the fragile flow of his confession."

    Lars narration "His furrowed brows reveal the burden of unpleasant memories, and as much as I long to unravel the tangled threads, he begins to shake his head in dismay."

    show claude smile
    show lars blush
    Claude "Spending time with you, [Lars], offered me a respite from all of that. It was a rare chance to shed the mask and simply be myself, the playful companion who loved to tease his partner in crime."

    show claude blush
    Claude "But, over time, my feelings changed…"

    #claude moves closer
    hide lars
    Lars narration "Drawing closer, he delicately runs his fingers through my hair with a tender touch. The scabrous texture of his fingernails traces a deliberate path downward, following the curve of my ear. In its wake, a lingering tingle persists, imprinting the sensation on my skin."

    show lars happy
    Claude "I stopped seeing you as just the guild's pilot or my work partner…"

    hide lars
    Lars narration "A tightening sensation grips my chest, each heartbeat resonating like the rhythmic murmur of a dragon. A flush of warmth colors my cheeks, and my tingling ears gently droop under the weight of his words."

    Lars narration "I'm hesitant to raise my head, yet, the same hand that had been tenderly caressing my hair and tracing my ear gently takes my chin, coaxing it upwards."

    show lars happy
    Lars "Are you saying what I think you're saying?"

    Claude "Relationships have always come easily to me, but you...you're the only person who's made me feel this way."

    show claude sad
    hide lars
    #claude moves to original position
    Lars narration "He releases my chin and retreats, leaving behind a noticeable chill in his departure."

    show lars sad
    Claude "Yet, I fear that settling down would dilute my ambition, the only thing that has allowed me to distance myself from the façade I've grown up with."

    Claude "All the efforts I've put into building my own legacy as a merchant, the bravado and arrogance...it would all be meaningless if I realized I had let slip the chance to build something meaningful with you."

    show claude smile
    show lars
    Claude "I teased you about it as well even though it was just my lingering feelings trying to surface. You could say that my candid lizard–like tongue was more honest than its faux owner."

    show claude sad
    show lars sad
    Claude "I argued with Boss Sylvian about the importance of seeking challenges and not embracing contentment without a fight. But, in reality, I'm the one ensnared by fear, unwilling to relinquish even a fraction of my ambition to battle for what truly matters."

    Claude "When push comes to shove, I'm addicted to the concept of competition. I can't break free, can't even take the time to savor the joys of life and the people around me."

    Claude "I can't even express my feelings for you without the fear of losing face because that's a sign that I'm not working hard enough to forge my own legacy."

    Lars "So, those jokes about confessions and everything, were they your way of hiding your fear of getting stuck and not growing as a person?"

    show claude
    Claude "Close. There’s one thing you’re missing though…"

    show lars
    show claude
    Claude "You were never mine from the start, so I lacked the courage to let go of my aspirations."

    show claude smile
    show lars happy
    Claude "You've always been your own strong-willed individual, adorned with that clever, fox-like charm, courageously taking a stand without voicing your fears, all in the name of protecting others."

    Claude "Today's events have only served to highlight this matter."

    hide lars
    Lars narration "My heart leaps with excitement at his words. The prospect of being with him is undeniably thrilling, and the uncertainty of what lies ahead fills me with a delightful, if somewhat anxious, anticipation."

    show lars happy
    Lars "…"

    show claude smile
    Claude "Perhaps it's time for me to stand here with you, to stop constantly reaching out to the future. Maybe cherishing the present with you is the ultimate challenge that will truly fulfill me—"

    show lars
    Lars "But that's not entirely what you want either, is it?"

    show claude
    Claude "What do you mean?"

    show lars happy
    Lars "You've always been the adventurous type, haven’t you? Just being content with the present, while wonderful, doesn't seem entirely like you. Are you sure you're ready to let go of all those grand aspirations?"

    hide lars
    show claude shocked
    Lars narration "His face registers a stunned expression, his mouth hanging open as if he can't quite believe the words I'm saying. Perhaps he was in the process of firming up his resolve to let go of his goals, but I can’t allow him to have his way that easily."

    show lars blush
    show claude blush
    Lars "Regardless of your status as the heir to a prominent family or my unwavering partner who never spared me in teasing, you've always been Claude to me."

    Lars "I'd like to think that these are the very facets that define who you are, the so-called appearances that you're trying to conceal."

    Lars "I may not be an expert in comprehending all the complexities that define us, but there's one thing I wholeheartedly agree with— I want to cherish this moment with you right now, without having you give up on the versions of yourself you may find less appealing."

    Lars "It's those very facets that make you the intricate person I admire."

    show claude smile
    Claude "…you’ve rendered me speechless."

    Claude "[Lars], you have an uncanny ability to see through the layers I've built around myself."

    Lars "Courtesy of spending so much time as your partner."

    Claude "You always have a way of making me question my perspective, my ambitions..."

    show lars blush
    Lars "It's not just about having you question them, Sir Claude. It's about cherishing every layer, every facet of who you are, without expecting you to change for me or anyone else."

    Lars "There's certainly room for improvement if you want to better yourself, but don't abandon what you've yearned for so long just because there are other dreams you want to attain."

    Lars "You're the person I admire, and you shouldn't have to choose between your goals. Pursue both, revel in the moment, and tackle those challenges that define you."

    Lars "You’re supposed to be an untouchable merchant for Div’s sake!"

    show claude blush
    Claude "Haha, you've effortlessly resolved my dilemma."

    Claude "That's what I love about you..."

    show lars happy
    Lars "Hey, I wanted to say it first—"

    Claude "The first person gets to savor the real taste of discovery, not the second or anyone who comes after. But then again, we're both confessing our feelings for the first time, so I suppose it's a unique experience for the both of us."

    Claude "Who knew I'd find such a remarkable discovery so close by."

    Lars "We may have taken a rather…unconventional route, using confessions for a gossip column to save everyone from being frozen in time. Yet, I can’t help but want you right here with me."

    Claude "…"

    Lars "Cat got your tongue?"

    Claude "More like my charming fox did. You captivating little delight, I'm going to savor every moment while having you to myself."

    Lars "Haha, didn't you just say how I was my own person and all that?"

    Claude "Then tell me, should I follow my desire to make you mine? Or do you want me to treat you gently?"

    hide lars
    Lars narration "Before I can respond, he takes my hand and pulls me closer to him."

    hide all
    #Do a little fade Insert cg_claude_good + some cinematography effect
    #camera does a little pan from left to right
    Claude "Call me Claude just like you did a little while ago, won't you, my darling fox?"

    Lars "Claude…"

    Lars narration "We stand closely together, our faces mere inches apart. Our lips are naturally drawn toward each other, and with a gentle lift of my chin, he pulls me even closer. Our eyes lock and a kiss is shared to seal the moment."

    Lars narration "My ponytail is likely tousled, gripped by his hand at the back of my head. His fingers glide through my already unruly hair, moving down to the nape of my neck. With his other hand on my waist, he pulls me even closer, his rough fingers brushing against the softness of my fur."

    Lars narration "Our breathing becomes deep, and in another shared moment of passion, our bodies press against each other, his silky hair brushing against me. For a few blissful moments, or perhaps even longer, it's just him and me, cocooned in our own world."

    Claude "You're the one who challenged me. Might as well see this through to the end, so we can determine who wins."

    #zoom out to the entire scene
    Lars "Bring it on."

    #zephyr’s happy sprite appears where lars’s side sprite usually is because I don’t want to ruin the CG
    Zephyr "Ah, what a headline! “The infamous Slicky Dupont and his love affair with the dragon pilot, Scouty”. I'll have to work around the details later, but what a story it will be."

    #textbox shake while he’s laughing
    Zephyr "I'll earn back the costs of my renovations plans tenfold, or maybe even a hundredfold! MUAHAHAHAHA!"

    Lars "Aren't you worried about what he might publish with your name?"

    Lars narration "He grabs my face with his hand and plants a heavy, passionate kiss upon my lips."

    Claude "I couldn't care less about what he does. I may have been obsessed with escaping my family name in the past, but not anymore. Not when I have you to adore and cherish, my daring fox."

    Claude "Not to mention, no reputable publishing house would dare mess with the mighty Duponts. Zephyr will be history before he can even spell our family name out loud."

    Lars "What about the artifact under Zephyr’s control and the trapped descendants?"

    Claude "Awe, leave the worrying to big Boss Sylvian and our little Rory back at the guild. I'm sure they're orchestrating a plan to aid the trapped individuals, all the while scheming my punishment for spiriting you away."

    Lars "‘Spiriting me away’, didn't I choose you first when asking Zephyr to let me bring you along?"

    Claude "Only because I made myself irresistibly pickable."

    Claude "Anyway, they've got it all figured out, I'm sure. Now, how about a few more stolen kisses?"

    Lars "Alright, you've convinced me. But you have to say the magic words first."

    Claude "Haha, brace yourself!"

    Claude "I love you, [Lars], and no amount of exotic treasures in the world will ever change how precious you are to me."

    #screen fades to black and the next line appears in the textbox, music also fades into silence
    $ renpy.choice_for_skipping()
    $ persistent.ending[3] = 1
    " " "Claude - Good End Achieved"
    jump end

label C3_claude_neutral_end:
    play music "track_8_neutral_ending.ogg"
    Lars narration "I should move past his comment."

    Lars narration "He probably meant it as a joke, like always. I should steer the conversation before I get swept up in his flirty act."

    show claude
    show lars
    Lars "Look, we'll have to prepare a confession for Zephyr, or else he'll carry out his plan to enslave people. Don't you have any gossip-worthy news from all the galas you go to?"

    show claude
    Claude "Well, you could say I prefer crashing those parties at the very end rather than participating and mingling with all the other snooty descendants."

    Lars "Is that why you're always fashionably late? Do you enjoy the process of dressing up and getting ready more than the actual party?"

    Claude "Not at all, dressing up and formalities tend to dull my momentum. I do, however, appreciate the artistry!"

    show claude smile
    Claude "I'd rather envision the way I'll disrupt the party."

    Claude "After all, who would I be if not Claude, the Showstopper? The one and only dazzling presence that can outshine the grandeur of Earth and Divonia alike."

    Claude "I crave that spontaneous thrill and unscripted excitement! It’s appealing when reality doesn't match my expectations."

    Lars "You're speaking like Master Sylvian all of a sudden. Did his philosophical influence rub off on you?"

    Claude "Haha, unlike Boss Sylvian, I prefer being a slave to my desires. It gives me a sense of fulfillment; knowing that I poured my heart and soul into every endeavor that I pursue."

    Claude "Leaving something in an ambiguous state or surrendering to simple pleasures doesn't sit well with me; it feels like I'm betraying the very essence of who I am."

    hide lars
    Lars narration "He chuckles, his eyes holding a playful hint of competition. I didn't realize they had a friendly rivalry going on. I'll have to ask about it later; I don't want to feel left out."

    show lars
    show claude serious
    Lars narration "Without much thought, a sudden question crosses my mind. Perhaps it was a subconscious desire to seek wisdom from someone I admired for his ambition and boldness."

    show lars
    Lars "What happens when you fall in love with someone? Will you end up leaving them for the next person who catches your interest? Or the next adventure that you come across?"

    show claude sad
    Claude "Let's…end the conversation here, Captain. I don't want to spoil the mood with my personal issues, and I can tell you're not that enthusiastic about it either."

    Claude "Our relationship hasn't reached the level where I feel comfortable sharing my story."

    show lars serious
    Lars "And what intriguing story could that be? I already know you're—"

    show claude serious
    Claude "Yes, I know. I come from a well-off family that arranges everything for me. Some might say I'm just a thrill-seeker, chasing the undiscovered future for my own amusement. You could say it’s my calling from nature."

    hide lars
    Lars narration "The air around us feels different. Claude isn't usually someone who starts talking about his family out of nowhere."

    show lars
    show claude
    Claude "[Lars]."

    Claude "I need you to listen to me carefully."

    hide lars
    Lars narration "He rarely ever shows his vulnerability, so witnessing this side of him is…"

    show lars
    Claude "…"

    Claude "You know what? I don’t think I’m ready to share my secret with you yet, Captain."

    show lars serious
    Lars "What do you mean? What’s wrong—"

    show claude sad
    Claude "I couldn't help but notice how you were so engrossed with Master Sylvian today. I wanted your attention solely on me, without needing to spell it out."

    Lars "Why are you acting like we're some couple? What's my chat with Master Sylvian got to do with what's happening now?"

    Claude "Well, if you don't understand it yourself, perhaps we're not on the same page yet when it comes to our feelings."

    hide lars
    Lars narration "His expression shifts to a melancholic tone, accompanied by a wistful sigh. A few strands of hair lose their perfect arrangement as his fingers comb through them."

    Lars narration "I've never witnessed him so troubled before."

    Lars narration "While I've always treasured our partnership, I had no idea that Sir Claude's feelings ran so deep."

    if options["CS3"]==2:

        Claude "I did make a promise to you, but I suppose I'm not as good at keeping my word as I believed I would be."



    show claude
    show lars serious
    Claude "You know what would be riskier than what I had planned to tell you?"

    Claude "Skydiving right off Spotsy at this very moment."

    Claude "If we ever crash, we could descend to the Earth realm together, you and I."

    Lars "What—"

    #for the next line, zephyr_sad anxiously comes in from the left and starts moving side to side
    Zephyr "OI OI OI, I'm not looking to make my hands any messier; bloody theatrics tend to repel future fans, you know!"

    show claude smile
    Claude "Don’t worry Captain."

    Claude "I wouldn't mind starting over as long as there's something new to conquer. Perhaps it's a chance to begin with my genuine feelings, leaving behind the pretentious grandeur that my wealth and name affords me."

    show lars serious
    Lars "Let's not jinx the journey when we're so close to our destination."

    show claude smile
    Claude "All I'm saying is that we would make quite the adventurous pair, even in a different realm as different people."

    Claude "Because wherever you are, I'm confident I will find you, and we will always remain our own unique duo, even if you're not exclusively mine to cherish."

    Lars "I'm not following, you’re just running off your mouth—"

    Claude "Too late, catch me if you can Captain!"

    #for the next scene, claude exits the scene as if he jumped off, perhaps a frame shake could better illustrate this
    hide lars
    Lars narration "Before I can ask any more questions, he jumps off Spotsy's back into the sea below."

    show lars
    #textbox shake for the next two lines
    Lars "SIR CLAUUUUDE!!!"

    Zephyr "SLICKYYYYY!!!!"

    Zephyr "Oh wait, I should be happy instead~ Buckle up for the show, Scouty! I'm unleashing the scandal of the century to every gossip-hungry magazine and tabloid out there."

    Zephyr "Watch the gold and treasure roll in as the Duponts scramble to buy the news of their only heir dying first hand. Ah, the perks of having no moral compass!"

    #screen shake while he’s laughing
    Zephyr "MUAHAHAHAHA!"

    #zephyr exits the scene while jumping up and down
    hide lars
    Lars narration "Panic surges through me as Zephyr's heartless laughter echoes in my ears. Ignoring the unsettling sound, I quickly seize the reins from him and spur Spotsy toward Sir Claude's descending form, determined to reach him in time."

    #bg starts blurring
    Lars narration "The biting chill of the wind stings my face as I race to reach Sir Claude. Time seems to slow as his figure plummets downward, and desperation fuels my actions. My fingers claw at the air as I stretch out, desperately trying to catch him, but he's falling too fast."

    #bg blurs even more
    Lars narration "In a split-second decision, I jump from Spotsy's back, the world spinning as I dive headfirst to intercept him. The wind roars in my ears, and the world blurs into a disorienting whirl as we plunge into the frigid sea."

    play sound sfx_splash
    #fade the blurred bg into black
    Lars narration "The impact is brutal, the cold water envelops us in a merciless embrace. My fur becomes waterlogged, dragging me down as I struggle to keep both of us afloat. Sir Claude's weight pulls me deeper, and my lungs burn for air."

    #Screen fades to bg_6, from here on out, the screen will go black every once in a while to show that he’s fighting back drowning + blur effect - sample in drive-]
    Lars narration "My consciousness...is fading…"

    #fades to black
    Lars narration "I’m... slipping away..."

    #fades to bg_6 blurred
    Lars narration "What’s that scaly tail…why’s it wrapping around me…?"

    Lars narration "Sir Claude's presence resurfaces in my fading awareness as he breathes life into me once more."

    #fades to bg_6
    show claude sad at center
    Lars narration "Amidst the chaos of the waves, I catch a glimpse of his eyes—those yellow orbs that resemble the sun breaking through stormy clouds."

    show lars sad
    #zoom in on claude a bit and for the ‘You'll...only...make me...fall...even...harder…’ part, have him gradually zoom out for each word until he’s back in his original position for the last part.
    Lars  "Claude…"

    Claude "What a joy to hear you call my name. Alas, I shouldn’t have asked you to jump after me, my dear fox. You'll...only...make me...fall...even...harder…"

    #zoom out on claude
    #fades to bg_6 blurred
    Lars  narration "I can barely make out his words…"

    #fades to black
    Lars narration "With every ounce of strength left in me, I try to fight back the encroaching black spell that threatens to take me. My arms tighten around Sir Claude, and I hold onto him for dear life."

    #3 seconds without dialogue box
    #fade in bg_5
    #claude comes on to scene with a transition
    show claude smile
    Lars narration "We tumble ashore in a tangled mess of limbs, drenched in salty waves. My fur clings to his rough scales, and a turbulent mix of relief and exasperation engulfs me."

    Lars narration "What was I thinking? I had overlooked the fundamental fact that Sir Claude is a descendant of lizards, equally adept on land and in the sea. I should have reined in my impulsiveness before plunging us into potential disaster."

    Lars narration "It's embarrassing. While I'm thankful that we're both safe, the fear of losing him drove me to the edge."

    Lars narration "How could I save him? What should I do to save him? These thoughts raced through my mind before the realization hit me: he didn't need me to leap after him."

    Lars narration "Come to think of it, that was probably his plan all along, indulging in an impulsive leap for the sake of some gossip material, and I didn't even see through it!"

    show lars serious
    Lars "Why in Divonia's name would you pull such a stunt? Have you lost your mind? You could have—"

    show claude blush
    Claude "I knew I could trust you with my life, Captain. After all, we make the best work couple in the guild."

    show lars sad
    Lars "You nearly gave me a heart attack. What kind of partner does that?"

    Claude "A partner for life, obviously. We've just solidified our bond as a duo for eternity, though I'll always hold hope in my heart for more."

    show lars serious
    Lars "Don't give me that kind of lip service."

    show claude sad
    Claude "Come on, humor me a bit. Share some of the excitement about our future as, you know, friends."

    hide lars
    Lars narration "He extends his hand toward me, a subtle invitation for a fist bump. It's an odd shift from the usual playful flirtations and spontaneous embraces he's known for."

    Lars narration "Perhaps it's the coolness of his hand or the way his eyes glisten under the soft, setting sun that makes me realize he's barely holding it together."

    Lars narration "Perhaps one final question will bring me peace of mind…"

    show lars
    Lars "Sir Claude, are you truly satisfied with how things have become between us?"

    Lars "I just want to be sure I'm not misunderstanding."

    show claude
    Claude "There's nothing to misunderstand. If my feelings had gotten through, you'd be certain. If they haven't, it might already be too late. Zephyr can freeze time, but he can't turn it back. So, perhaps I'll have to leave that dream for another version of me with more courage."

    Claude "For now, my only ambition is to remain friends with you, because straining our relationship would be too painful."

    hide lars
    Lars narration "He appears quite determined, and I can't help but feel a tinge of sadness. My actions today seem to have influenced this outcome, and I have no choice but to accept it with a heavy heart."

    show lars
    Lars "Same here, Sir Claude. But no more antics like that."

    Claude "Haha, as much as I'd love to, my tail is still recovering from that little splash earlier."

    #screen fades to black and the next line appears in the textbox, music also fades into silence
    $ renpy.choice_for_skipping()
    $ persistent.ending[4] = 1
    " " "Claude - Neutral End Achieved"
    jump end
    
label C3_claude_bad_end:
    play music "track_9_bad_ending.ogg"
    Lars narration "I should stay silent for now."

    Lars narration "Master Sylvian and Rory might get in trouble if we stall for too long."

    show claude at center
    show lars
    Lars "Look, we'll have to prepare a confession for Zephyr, or else he'll carry out his plan to enslave people. Don't you have any gossip-worthy news from all the galas you go to?"

    show claude
    Claude "Well, you could say I prefer crashing those parties at the very end rather than participating and mingling with all the other snooty descendants."

    Lars "Let’s save that story for later."

    show claude smile
    Claude "Why? What's the harm in stalling a little bit more?"

    Claude "Maybe I just want to spend more time with you—"

    show lars serious
    show claude shocked
    Lars "Ugh, enough of this. You only ever know how to flirt and act like a showman."

    hide lars
    Lars narration "I'm a dragon pilot for Div's sake, a responsible person who is supposed to take care of the people around him. I can't just sit back and watch innocent people get dragged into this mess."

    show lars serious
    Lars "If you don't start acting seriously about this, we'll never be able to save the enslaved humans, and Zephyr is going to continue suspending time for who knows how long."

    Claude "Come on, Captain, I know you value your duties, but no one said we couldn't have a little fun on the journey!"

    Lars "Master Sylvian wouldn't have been so nonchalant about this matter like you are."

    show claude serious
    Claude "Hmm? Is that what this is? A ploy to show me that you wanted Sylvian to come along instead?"

    hide lars
    Lars narration "Tension tightens his expression, a silent storm brewing in his golden eyes. As his fingers thread through tightly braided silver hair, unraveling a few strands, the disheveled tendrils mirror the chaos within— a poignant departure from his usual confidence."

    show lars serious
    #for the next line, claude does a side to side shake + a jump. Preferably, he does a shake to the left from ‘It’s always Sylvian this’ and does another shake from ‘and Sylvian that’, then does a jump from ‘Why can't I ever catch a break from him?’
    Claude "It’s always Sylvian this and Sylvian that. Why can't I ever catch a break from him?"

    hide lars
    Lars narration "Venom drips from his words with each mention of the Master, catching me off guard. I never expected such a strong undercurrent of negative feelings from someone usually so charismatic and positive."

    show lars serious
    Lars "I only mentioned him as an example, Sir Claude. What's going on with you? Why are you so riled up?"

    show claude sad
    Claude "You know what? I can't take this anymore."

    Claude "I've been trying to impress you and win your favor for such a long time, yet your gaze remains fixed on your cherished Master Sylvian."

    Claude "Why didn’t you choose him instead? Is it enjoyable to see me in such a state? To coax my confession, and then, in the end, respond with silence?"

    show claude serious
    Claude "Frankly, I don't care about saving others and whatnot."

    show lars sad
    Lars "Sir Claude, you've got it all wrong—"

    Claude "Drop the 'Sir' once and for all! It's clear you don't even bother to hear me out, do you?"

    Lars "I never intended to hurt you or make you feel this way…"

    Claude "You certainly did a 'fantastic' job with that."

    show lars serious
    Lars "Ugh, you really outdid yourself with that, didn't you? Let's just put this misunderstanding aside for now and focus on the mission."

    Lars "We'll talk about this later when our heads are less clouded."

    show claude serious
    Claude "Oh, so now my head is clouded? So you think my brain is lost on its own little adventure, don't you?"

    hide lars
    Lars narration "My fur unruffles, and an electric charge courses through my body. A ringing sensation pounds in my head, and it's difficult to restrain the words that spill from my mouth."

    show lars serious
    Lars "Do you always have to act like such a spoiled kid? Didn't your parents give you enough affection as is? Why do you have to cling to me so much?"

    Lars "Not to mention, did I ask for your hugs, embraces, or your attention? I didn't, so why are you now having a problem with me staying silent about it?"

    show claude sad
    Claude "I…I didn’t expect that from you [Lars]."

    Lars "You don’t expect much from anyone aside from yourself, now do you?"

    Claude "I didn’t imagine I’d ever say this but I’m…disappointed in you [Lars]."

    Claude "I don't like people bringing up my family name; you should know that better than anyone else—"

    hide lars
    Lars narration "Why is he looking at me with such a pitiful gaze?"

    show claude serious
    Claude "You know what, maybe it's time to confess, just so I can get over you once and for all."

    Claude "You remember how I've always skirted around the fact that I'm a Dupont heir?"

    show lars serious
    Lars "What does that have to do with anything right now?"

    show claude sad
    Claude "Well, the truth is, I've avoided mentioning it because...I didn't want to be defined by that name."

    show lars serious
    Claude "I've always struggled with titles and appearances growing up."

    Claude "The burden of being the Dupont family heir, with its myriad of expectations,  it all felt like a shallow act that I had to uphold, and I...I felt imprisoned in that superficial world."

    hide lars
    Lars narration "His furrowed brows reveal the burden of unpleasant memories, and as much as I long to unravel the tangled threads, he begins to shake his head in dismay."

    show claude sad
    show lars serious
    Claude "Spending time with you, [Lars], offered me a respite from all of that. It was a rare chance to shed the mask and simply be myself, the playful companion who loved to tease his partner in crime."

    Claude "But, over time, my feelings changed…"

    hide lars
    Lars narration "My heart quickens its pace, a sense of dread sparking through every fiber of my being as I prepare for what lies ahead. Will we finally be able to get over this hurdle and be done with the confession?"

    Lars narration "He starts to absentmindedly stroke his hair, an irritating habit I've grown weary of. With a frustrated sigh, he looks up, as if lost in some memory, before reluctantly shifting his gaze to the horizon and continuing his speech."

    show lars serious
    Claude "I stopped seeing you as just the guild's pilot or my work partner…"

    hide lars
    Lars narration "A heavy weight settles on my chest, and my heart races, each beat echoing my growing unease. Weariness seeps into my bones as I find myself in an awkward role – the unwilling recipient of Sir Claude’s love confession."

    Lars narration "I really don’t want to look at his eyes right now."

    show lars serious
    Lars "Are you saying what I think you're saying?"

    Claude "Relationships have always come easily to me, but you...you're the only person who's made me feel this way."

    Claude "Yet, I fear that settling down would dilute my ambition, the only thing that has allowed me to distance myself from the façade I've grown up with."

    Claude "All the efforts I've put into building my own legacy as a merchant, the bravado and arrogance...it would all be meaningless if I realized I had let slip the chance to build something meaningful with you."

    Claude "I teased you about it as well even though it was just my lingering feelings trying to surface. You could say that my candid lizard–like tongue was more honest than its faux owner."

    Claude "I teased you about it, but it was just my lingering feelings trying to surface. You could say that my candid, lizard-like tongue was more honest than my faux appearance."

    Claude "I argued with Boss Sylvian about the importance of seeking challenges and not embracing contentment without a fight. But, in reality, I'm the one ensnared by fear, unwilling to relinquish even a fraction of my ambition to battle for what truly matters."

    Claude "When push comes to shove, I'm addicted to the concept of competition. I can't break free, can't even take the time to savor the joys of life and the people around me."

    Claude "I can't even express my feelings for you without the fear of losing face because that's a sign that I'm not working hard enough to forge my own legacy."

    Lars "So, those jokes about confessions and everything, what was the deal behind them?"

    show claude serious
    Claude "I don't want you to analyze it any further than I've told you. If we were on the same wavelength, there would have been no need to explain it more than that."

    show lars
    Lars "Sir Claude, I appreciate your feelings, but—"

    Claude "Still calling me that obnoxious title even in this situation. Won't you humor me and call me by my name for once?"

    Lars "..."

    show claude sad
    Claude "Well, at least I'll have the chance to put these feelings behind me once and for all."

    hide lars
    Lars narration "In an attempt to offer some comfort, my hand tentatively reaches out to him. Yet, he gently but firmly pushes it away, and the gravity of the situation bears down on me. Here I am, standing with someone I truly admire -despite our recent clash- who has just confessed his feelings."

    Lars narration "However, I know deep down that I can't reciprocate those feelings."

    show lars sad
    Lars "I’m sorry…"

    show claude serious
    Claude "I'm sorry too, [Lars]."

    Claude "You've always been your own strong-willed individual, adorned with that clever, fox-like charm, courageously taking a stand without voicing your fears, all in the name of protecting others."

    Claude "Today's events have only served to highlight this matter."

    Claude "So I’m sorry things turned out this way."

    Lars "…"

    show claude sad
    Claude "Let's…end the conversation here, Captain. I don't want to spoil the mood with my personal issues, and I can tell you're not that enthusiastic about it either."

    if options["CS3"]==2:

        Claude "I did make a promise to you, but I suppose I'm not as good at keeping my word as I believed I would be."



    #zephyr comes in from the left does a little jump at first
    Zephyr "Hey, I know you two had your heartfelt exchange, but I'm in the mood for a grand, dramatic confession. This subtle stuff won't cut it; it's barely a snack when I was hoping for a feast."

    Zephyr "Honestly, if you're not up to the task, you might as well just leap off this dragon's back; you're just extra baggage right now. Come on, give me the theatrics, the flair! THE SCOOP!"

    show claude
    Claude "Skydiving right off Spotsy at this very moment."

    Claude "That doesn't sound like a bad idea, maybe it will help me clear my head a little."

    Lars "What—"

    #for the next line, zephyr_sad starts moving side to side
    Zephyr "OI OI OI, I'm not looking to make my hands any messier; bloody theatrics tend to repel future fans, you know!"

    show claude serious
    Claude "Did you forget that I'm a lizard descendent? I'll be fine, so..."

    Claude "Don't catch me."

    #for the next scene, claude exits the scene as if he jumped off, perhaps a frame shake could better illustrate this
    hide lars
    Lars narration "Before I can ask any more questions, he jumps off Spotsy's back into the sea below."

    show lars
    #textbox shake for the next two lines
    Lars "SIR CLAUUUUDE!!!"

    Zephyr "SLICKYYYYY!!!!"

    Zephyr "Oh wait, I should be happy instead~ Buckle up for the show, Scouty! I'm unleashing the scandal of the century to every gossip-hungry magazine and tabloid out there."

    Zephyr "Watch the gold and treasure roll in as the Duponts scramble to buy the news of their only heir dying first hand. Ah, the perks of having no moral compass!"

    #screen shake while he’s laughing
    Zephyr "MUAHAHAHAHA!"

    #zephyr exits the scene while jumping up and down
    hide lars
    Lars narration "Panic surges through me as Zephyr's heartless laughter echoes in my ears. Ignoring the unsettling sound, I quickly seize the reins from him and spur Spotsy toward Sir Claude's descending form, determined to reach him in time."

    #bg starts blurring
    Lars narration "The biting chill of the wind stings my face as I race to reach Sir Claude. Time seems to slow as his figure plummets downward, and desperation fuels my actions. My fingers claw at the air as I stretch out, desperately trying to catch him, but he's falling too fast."

    #bg blurs even more
    Lars narration "In a split-second decision, I jump from Spotsy's back, the world spinning as I dive headfirst to intercept him. The wind roars in my ears, and the world blurs into a disorienting whirl as we plunge into the frigid sea."

    play sound sfx_splash
    #fade the blurred bg into black
    #fade the blurred bg into black
    Lars narration "The impact is brutal, the cold water envelops us in a merciless embrace. My fur becomes waterlogged, dragging me down as I struggle to keep both of us afloat. Sir Claude's weight pulls me deeper, and my lungs burn for air."

    #Screen fades to bg_6, from here on out, the screen will go black every once in a while to show that he’s fighting back drowning + blur effect - sample in drive-]
    Lars narration "My consciousness...is fading…"

    #fades to black
    Lars narration "I’m... slipping away..."

    #fades to bg_6 blurred
    Lars narration "What’s that scaly tail…why’s it wrapping around me…?"

    Lars narration "Sir Claude's presence resurfaces in my fading awareness as he breathes life into me once more."

    #fades to bg_6
    show claude sad at center
    Lars narration "Amidst the chaos of the waves, I catch a glimpse of his eyes—those yellow orbs that resemble the sun breaking through stormy clouds."

    show lars sad
    #zoom in on claude a bit
    Lars  "Claude…"

    show claude serious
    Claude "What a joy to hear you call my name. Alas, I shouldn’t have asked you to jump after me, my dear fox. You'll...only...make me...fall...even...harder…"

    #zoom out on claude
    #fades to bg_6 blurred
    Lars  narration "I can barely make out his words…"

    #fades to black
    Lars narration "With every ounce of strength left in me, I try to fight back the encroaching black spell that threatens to take me. My arms tighten around Sir Claude, and I hold onto him for dear life."

    #3 seconds without dialogue box
    #fade in bg_5
    #claude comes on to scene with a transition
    show claude serious
    Lars narration "We tumble ashore in a tangled mess of limbs, drenched in salty waves. My fur clings to his rough scales, and a turbulent mix of relief and exasperation engulfs me."

    Lars narration "What was I thinking? I had overlooked the fundamental fact that Sir Claude is a descendant of lizards, equally adept on land and in the sea. I should have reined in my impulsiveness before plunging us into potential disaster."

    Lars narration "It's embarrassing. While I'm thankful that we're both safe, the fear of losing him drove me to the edge."

    Lars narration "How could I save him? What should I do to save him? These thoughts raced through my mind before the realization hit me: he didn't need me to leap after him."

    Lars narration "Come to think of it, that was probably his plan all along, indulging in an impulsive leap for the sake of some gossip material, and I didn't even see through it!"

    show lars serious
    Lars "Why in Divonia's name would you pull such a stunt? Have you lost your mind? You could have—"

    Claude "I told you not to catch me, didn't I?"

    show lars sad
    Lars "You nearly gave me a heart attack. What kind of partner does that?"

    show claude sad
    Claude "Do me a little favor and stay away from me for a while, [Lars]."

    Claude "I may trust you with my life in the future as a fellow guild member, but I can no longer trust you with my heart as a  friend or my partner in crime."

    hide lars
    Lars narration "He breaks away from his stagnant position and slowly begins to walk away. Is this how it all ends?"

    Lars narration "The partner I've worked alongside for so long, my dearest friend, the person whose ambition I've admired, just walking away without a word or challenge?"

    Lars narration "A part of me yearns to reach out, to call his name, but the risk of causing misunderstandings or giving false hope holds me back."

    Lars narration "So, I remain rooted to my spot, watching his retreating form."

    Lars narration "Perhaps one final question will bring me peace of mind…"

    show lars sad
    Lars "Sir Claude, are you truly satisfied with how things have become between us?"

    Lars "I just want to be sure I'm not misunderstanding."

    show claude serious
    Claude "There's nothing to misunderstand. If my feelings had gotten through, you'd be certain. If they haven't, it might already be too late. Zephyr can freeze time, but he can't turn it back. So, perhaps I'll have to leave that dream for another version of me with more courage."

    Claude "I'll walk away from this like the coward that I am, a small lizard who couldn't achieve what he wanted. Staying with you would only remind me of the failure that I am, you even said it yourself..."

    Lars "But I didn't mean it like that; it was just the heat of the moment."

    Lars "Why are you deciding everything on your own?"

    Lars "I might as well claim the victory of having the last word since I didn't succeed in having the best one."

    hide lars
    Lars narration "Looks like he had achieved what he sought after all – another victory in his competitive mind."

    Claude "Goodbye, [Lars] ...take care of yourself."

    #screen fades to black and the next line appears in the textbox, music also fades into silence
    $ renpy.choice_for_skipping()

    $ persistent.ending[5] = 1
    " " "Claude - Bad End Achieved"
    jump end

label end:
    #screen fades to black and the next line appears in the textbox, music also fades into silence
    scene bg black with fade
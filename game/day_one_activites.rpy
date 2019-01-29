label day0_select:

    menu:
        "[do_text]"
        "Use vending machine" if location == "hallway":
            "Hmm...."
            $ nextscene = "day" + str(chapter) + "_select"
            jump expression nextscene
        "Go to school with Sayori" if time == "morning":
            $ school_sayo = True
            if location != "street":
                scene bg residential_day
                with wipeleft_scene
            jump day0_school_Sayori

        "Enter" if location == "school_gate":
            if time == "morning":
                $ school_sayo = False
                $ location = "class"
                jump day0_school
            if time == "day":
                scene bg corridor
                with wipeleft_scene
                $ location = "hallway"
                $ nextscene = "day" + str(chapter) + "_select"
                jump expression nextscene
            if time == "evening":
                scene bg corridor
                with wipeleft_scene
                $ location = "hallway"
                $ nextscene = "day" + str(chapter) + "_select"
                jump expression nextscene
            if time == "night":
                "Why would I want to go to school now?"
                $ nextscene = "day" + str(chapter) + "_select"
                jump expression nextscene

        "Use phone" if energy >= 25:
            jump use_phone
        "Go to sleep" if location == "room":
            if energy >= 50:
                "I still have a lot of energy left."
                menu:
                    "Am I sure I want to go to sleep?"
                    "Yes":
                        $ skip_poem = True
                    "No":
                        $ do_text = "What to do, what to do?"
                        jump day0_select
            else:
                $ skip_poem = True
            return
        "Use Computer" if location == "room":
            if energy >= 10:
                "It's broken."
                "Maybe it will work soon?"
                jump day0_select
            else:
                "For some reason I am too tired to use my PC."
                $ do_text = "Sleep is a wonderful thing."
                jump day0_select
        "Write my poem" if location == "room":
            if energy >= 10:
                return
            else:
                "I am too tired to write my poem."
                $ do_text = "I should go to sleep."
                jump day0_select
        "Vist Sayori" if location == "sayo_house":
            "I knock on the door."
            if time == "day":
                "No response."
                "She must not be home."
                jump day0_select
            if time == "night":
                "Hmm..."
                "I turn to leave."
                s "[player]?"
                jump day0_select
        "Watch anime" if location == "room":
            if anime0 == False:
                jump day0_anime
            else:
                "I already did that."
                $ do_text = "What should I do then?"
                jump day0_select
        "Go shopping" if food == False:
            if time == "morning":
                "I can't go shopping.  I have to go to school."
                $ do_text = "What should I do then?"
                jump day0_select
            if time == "day":
                jump day0_shopping
            if time == "night":
                "It's too late to go shopping."
                $ do_text = "What should I do then?"
                jump day0_select
        "Go somewhere":
            jump move

label day0_sayori:
    if energy >=10:
        if time == "day":
            "Yeah it's been a while since we have hanged out together."
            "I guess I better call her."
            "..."
            "..."
            "Hmm... She is not answering."
            "Maybe she is busy."
            $ called_sayo1 = True
            $ do_text = "I can't see Sayori so what should I do now?"
            jump day0_select
        else:
            "It's too late to do that."
            $ do_text = "What should I do instead?"
            jump day0_select
    else:
        "I am too tired to do that."
        $ do_text = "I need to sleep."
        jump day0_select

label day0_shopping:
    "I might as well go shopping"
    "I really need to get more food."
    if location == "town":
        "It's also a good idea, because I am already near the store."
    else:
        "..."
        "Well, I should get going before it gets late."
        scene bg town_day
        with wipeleft_scene
        "I have always been happy that I lived so close to the town."
    m "[player]?"
    show monika 1a zorder 1 at t11
    mc "Monika?  What are you doing here?"
    m 2b "Well, I came to get some supplies for the club.  You?"
    mc "I came to buy some food."
    m "It sounds like we are going to the same store."
    m "Do you want to shop together?"
    menu:
        "Do I?"
        "Yes":
            jump day0_monika
        "No":
            jump day0_shop_alone
label day0_monika:
    mc "Sure!"
    play music t6
    "I follow Monika to the candy section in the store."
    mc "This is club supples?"
    m "Haha~ No, these are for Sayori."
    m "She thinks it would be a good idea to have snacks in the club."
    mc "And she wants you to get them?"
    m "Exactly! Hehe~"
    "Sounds like Sayori."
    mc "Well, what are you getting then?"
    m "I was thinking about getting some chocolate."
    mc "Isn't that supposed to be in the candy aisle?"
    m "Yes, but I am getting some cookies too."
    mc "Oh...Okay!"
    "Wow, Monika has a sweet tooth!"
    scene bg town_after
    with wipeleft_scene
    "After I bought my food, Monika and I leave the store."
    show monika 1a zorder 1 at t11
    mc "Wow!  We really spent a long time in there."
    m "Yeah, we did."
    m "It was fun catching up with you."
    mc "It definitly was."
    play music t8
    "We start on our way home."
    scene bg residential_night
    with wipeleft_scene
    show monika 1a zorder 1 at t11
    "We arrive at the street near my house."
    mc "Well, I guess I will see you tomorrow then."
    m "Yep!"
    m "See you tomorrow!"
    scene bg home_night
    with wipeleft_scene
    "Wow!  It's late!"
    $ food = True
    $ day0_monika = True
    $ energy -= 70
    $ do_text = "I am tired.  I don't have many things to do right now."
    $ time = "night"
    $ location = "front_door"
    jump day0_select
    
label day0_shop_alone:
    mc "Well, its a quick trip.  I don't want to get home late or anything."
    m "Thats okay [player]."
    m "See you tomorrow."
    hide monika
    "Well, I just refused to spend time with a girl."
    "Nice job [player]."
    "I enter the store and grab the food I need."
    "..."
    "Well, that did not take as long as I thought."
    "Time to go back home I guess"
    scene bg kitchen
    with wipeleft_scene
    "I put all of the food up."
    "Looks Like I still have time left in the day."
    $ location = "kitchen"
    $ energy -=40
    $ food = True
    $ do_text = "What should I do now?"
    jump day0_select
    
label day0_anime:
    scene bg kitchen
    with wipeleft_scene
    if food == False:
        "I head to the kitchen and get some aged tacos."
        "I have a thing for them for some reason."
    if food == True:
        if day0_monika == True:
            mc "I guess I better put my food up first"
            "I make some soup and put the rest of the food in the fridge."
        else:
            "I make some soup then head to my room."
    scene bg bedroom
    with wipeleft_scene
    "I sit on my bed and turn on a action anime"
    "It's one I have already seen before, but I love it."
    if day0_monika == True:
        "Suddenly I get a message."
        "It's from Monika!"
        "Wait, how did she get my number?"
        m "[player], this is Monika."
        m "I had fun hanging out with you this evening."
        m "We should do it again sometime."
        m "See you tomorrow!"
        "..."
        "..."
        "Wow!"
        "I have not even been in the club for more then a day and I already have a girl's number!"
        "I better make sure I keep this up."
    scene bg bedroom
    with wipeleft_scene
    "..."
    "I really wonder how well the club will go tomorrow."
    "My mind starts wondering, and before I know it, it's late."
    $ anime0 = True
    $ time = "night"
    $ energy = 0
    jump day0_select

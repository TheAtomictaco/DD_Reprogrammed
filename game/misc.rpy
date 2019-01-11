label move:
     menu:
        "Where should I go?"
        "School" if location != "school_gate":
            if time == "morning":
                scene bg gate
            if time == "day":
                scene bg gate
            if time == "evening":
                scene bg gate_evening
            if time == "night":
                scene bg gate_night
            with wipeleft_scene
            $ location = "school_gate"
            $ nextscene = "day" + str(chapter) + "_select"
            jump expression nextscene

        "Library" if location == "town":
            if time == "day":
                scene bg library
                with wipeleft_scene
                $ location = "library"
            if time == "night":
                "The library is closed."
            $ nextscene = "day" + str(chapter) + "_select"
            jump expression nextscene

        "Town" if location != "town":
            if time == "day":
                scene bg town_day
            if time == "night":
                scene bg town_night
            with wipeleft_scene
            $ location = "town"
            $ nextscene = "day" + str(chapter) + "_select"
            jump expression nextscene

        "Park" if location != "park":
            if time == "day":
                scene bg park
                with wipeleft_scene
                $ location = "park"
            if time == "night":
                "It's too late to go to the park."
            $ nextscene = "day" + str(chapter) + "_select"
            jump expression nextscene

        "My Street" if location != "street":
            if time == "day":
                scene bg residential_day
            if time == "night":
                scene bg residential_night
            with wipeleft_scene
            $ location = "street"
            $ nextscene = "day" + str(chapter) + "_select"
            jump expression nextscene


        "Sayori's House" if location == "street":
            if time == "day":
                scene bg house
            if time == "night":
                scene bg home_night
            with wipeleft_scene
            $ location = "sayo_house"
            $ nextscene = "day" + str(chapter) + "_select"
            jump expression nextscene

        "My House" if location == "street":
            if time == "day":
                scene bg house
            if time == "night":
                scene bg home_night
            with wipeleft_scene
            $ location = "front_door"
            $ nextscene = "day" + str(chapter) + "_select"
            jump expression nextscene

        "Go inside" if location == "front_door":
            scene bg kitchen
            with wipeleft_scene
            $ location = "kitchen"
            $ nextscene = "day" + str(chapter) + "_select"
            jump expression nextscene

        "Kitchen" if location == "room":
            scene bg kitchen
            with wipeleft_scene
            $ location = "kitchen"
            $ nextscene = "day" + str(chapter) + "_select"
            jump expression nextscene

        "My room" if location == "kitchen":
            scene bg bedroom
            with wipeleft_scene
            $ location = "room"
            $ nextscene = "day" + str(chapter) + "_select"
            jump expression nextscene

        "leave" if location == "kitchen":
            if time == "day":
                scene bg house
            if time == "night":
                scene bg home_night
            with wipeleft_scene
            $ location = "front_door"
            $ nextscene = "day" + str(chapter) + "_select"
            jump expression nextscene

        "Cancel":
            $ nextscene = "day" + str(chapter) + "_select"
            jump expression nextscene

label use_phone:
    menu:
        "Who should I call?"
        "Sayori" if called_sayo1 == False:
            jump day0_sayori
        "Cancel":
            $ nextscene = "day" + str(chapter) + "_select"
            jump expression nextscene
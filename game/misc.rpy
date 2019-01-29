label move:
     $ nextscene = "day" + str(chapter) + "_select"
     menu:
        "Where should I go?"
        "ClassRoom" if location == "hallway":
            if time == "morning":
                scene bg class_day
                with wipeleft_scene
                $ location = "class"
            if time == "day":
                scene bg class_day
                with wipeleft_scene
                $ location = "class"
            if time == "evening":
                scene bg class_day
                with wipeleft_scene
                $ location = "class"
            jump expression nextscene

        "ClubRoom" if location == "hallway":
            if time == "morning":
                scene bg club_day
                with wipeleft_scene
                $ location = "club"
            if time == "day":
                scene bg club_day
                with wipeleft_scene
                $ location = "club"
            if time == "evening":
                scene bg club_day
                with wipeleft_scene
                $ location = "club"
            jump expression nextscene

        "Hallway" if location == "class":
            if time == "morning":
                scene bg corridor
                with wipeleft_scene
                $ location = "hallway"
            if time == "day":
                scene bg corridor
                with wipeleft_scene
                $ location = "hallway"
            if time == "evening":
                scene bg corridor
                with wipeleft_scene
                $ location = "hallway"
            jump expression nextscene

        "Hallway" if location == "club":
            if time == "morning":
                scene bg corridor
                with wipeleft_scene
                $ location = "hallway"
            if time == "day":
                scene bg corridor
                with wipeleft_scene
                $ location = "hallway"
            if time == "evening":
                scene bg corridor
                with wipeleft_scene
                $ location = "hallway"
            jump expression nextscene

        "Hallway" if location == "library":
            if time == "morning":
                scene bg corridor
                with wipeleft_scene
                $ location = "hallway"
            if time == "day":
                scene bg corridor
                with wipeleft_scene
                $ location = "hallway"
            if time == "evening":
                scene bg corridor
                with wipeleft_scene
                $ location = "hallway"
            jump expression nextscene

        "School Entrance" if location != "gate":
            if time == "morning":
                scene bg gate
            if time == "day":
                scene bg gate
            if time == "evening":
                scene bg gate_evening
            if time == "night":
                scene bg gate_night
            with wipeleft_scene
            $ location = "gate"
            jump expression nextscene

        "Library" if location == "hallway":
            if time == "morning":
                scene bg library
                with wipeleft_scene
                $ location = "library"
            if time == "day":
                scene bg library
                with wipeleft_scene
                $ location = "library"
            if time == "evening":
                scene bg library
                with wipeleft_scene
                $ location = "library"
            if time == "night":
                "The library is closed."
            jump expression nextscene

        "Town" if location != "town":
            if time == "morning":
                scene bg town_day
            if time == "day":
                scene bg town_day
            if time == "evening":
                scene bg town_after
            if time == "night":
                scene bg town_night
            with wipeleft_scene
            $ location = "town"
            jump expression nextscene

        "Park" if location == "town":
            if time == "morning":
                scene bg park
                with wipeleft_scene
                $ location = "park"
            if time == "day":
                scene bg park
                with wipeleft_scene
                $ location = "park"
            if time == "evening":
                scene bg park
                with wipeleft_scene
                $ location = "park"
            if time == "night":
                "It's too late to go to the park."
            jump expression nextscene

        "My Street" if location != "street":
            if time == "morning":
                scene bg street_day
                with wipeleft_scene
                $ location = "street"
                jump expression nextscene
            if time == "day":
                scene bg street_day
                with wipeleft_scene
                $ location = "street"
                jump expression nextscene
            if time == "night":
                scene bg street_night
                with wipeleft_scene
                $ location = "street"
                jump expression nextscene
            if time == "evening":
                scene bg street_day
                with wipeleft_scene
                $ location = "street"
                jump expression nextscene

        "Sayori's House" if location == "street":
            if time == "morning":
                scene bg house
            if time == "day":
                scene bg house
            if time == "evening":
                scene bg house
            if time == "night":
                scene bg home_night
            with wipeleft_scene
            $ location = "s_home"
            jump expression nextscene

        "My House" if location == "street":
            if time == "morning":
                scene bg house
            if time == "day":
                scene bg house
            if time == "evening":
                scene bg house
            if time == "night":
                scene bg home_night
            with wipeleft_scene
            $ location = "home"
            jump expression nextscene

        "Go inside" if location == "home":
            scene bg kitchen
            with wipeleft_scene
            $ location = "kitchen"
            jump expression nextscene

        "Kitchen" if location == "room":
            scene bg kitchen
            with wipeleft_scene
            $ location = "kitchen"
            jump expression nextscene

        "My room" if location == "kitchen":
            scene bg bedroom
            with wipeleft_scene
            $ location = "room"
            jump expression nextscene

        "leave" if location == "kitchen":
            if time == "morning":
                scene bg house
            if time == "day":
                scene bg house
            if time == "evening":
                scene bg house
            if time == "night":
                scene bg home_night
            with wipeleft_scene
            $ location = "front_door"
            jump expression nextscene

        "Cancel":
            jump expression nextscene

label use_phone:
    menu:
        "Who should I call?"
        "Sayori" if called_sayo1 == False:
            jump day0_sayori
        "Cancel":
            $ nextscene = "day" + str(chapter) + "_select"
            jump expression nextscene
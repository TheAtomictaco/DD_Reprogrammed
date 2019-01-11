# Entry point
label start:

    # ID of this playtrhoguh
    $ anticheat = persistent.anticheat

    # keep track of chapter

    # if they quit during a pause, we have to set _dismiss_pause to false again
    $ _dismiss_pause = config.developer

    # girl names
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True


    $ chapter = 0
    call day0_main from _call_day0_main

    if skip_poem == False:
        call new_m_poem from _call_new_m_poem_0
    else:
        stop music fadeout 2.0
        with dissolve_scene_full


    $ chapter = 1
    call day2_main from _call_day2_main
    call poemresponse_start from _call_poemresponse_start
    call day2_end from _call_day2_end


    call new_m_poem from _call_new_m_poem_1


    $ chapter = 2
    call day3_main from _call_day3_main
    call poemresponse_start from _call_poemresponse_start_1
    call day3_end from _call_day3_end


    call new_m_poem from _call_new_m_poem_2


    $ chapter = 3
    call day4_main from _call_day4_main
    call poemresponse_start from _call_poemresponse_start_2
    call day4_end from _call_day4_end

    $ chapter = 4
    call day5_main from _call_day5_main

    python:
        try: renpy.file(config.basedir + "/hxppy thxughts.png")
        except: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
    $ chapter = 5
    call day6_main from _call_day6_main

    call endgame from _call_endgame

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

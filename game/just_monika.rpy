
image splash-glitch2 = "images/bg/splash-glitch2.png"

label beginning_monika:
    $ m_name = "Monika"
    scene white
    play music "bgm/monika-start.ogg" noloop
    pause 0.5
    show splash-glitch2 with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash-glitch2 with Dissolve(0.5, alpha=True)
    scene black
    stop music
    $ consolehistory = []

    call updateconsole ("os.install(\"game\mod-installer.rpyc\")", "installed successfully.") from _call_updateconsole_15
    call updateconsole ("os.mod-install", "Mod install started...") from _call_updateconsole_16
    call hideconsole from _call_hideconsole_2
    jump splashscreen

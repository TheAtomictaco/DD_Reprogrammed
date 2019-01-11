#This code was made by jadebenn
#You must credit me in your mod if you use this code!

image m_sticker smile:
    "m_sticker"
    pause 0.1
    xoffset monikaOffset xzoom monikaZoom
    "gui/poemgame/m_sticker_2.png"
    
image s_sticker smile:
    "s_sticker"
    pause 0.1
    xoffset sayoriOffset xzoom sayoriZoom
    "gui/poemgame/s_sticker_2.png"
    
image y_sticker smile:
    "y_sticker"
    pause 0.1
    xoffset yuriOffset xzoom yuriZoom
    "gui/poemgame/y_sticker_2.png"
    
image n_sticker smile:
    "n_sticker"
    pause 0.1
    xoffset natsukiOffset xzoom natsukiZoom
    "gui/poemgame/n_sticker_2.png"
    
init python:
    import random
    from datetime import datetime
    display_words = []
    
    #I might actually want to move this to definitions, this could be REALLY useful later
    class CooldownTimer:
        def __init__(self, cooldown):
            self.init_time = datetime.min
            self.cooldown = cooldown
        def start(self):
            self.init_time = datetime.now()
        def hasFinished(self):
            current_time = datetime.now()
            if self.init_time > current_time:
                self.init_time = current_time #If you somehow went back in time, we fix that.
            elapsed_time = current_time - self.init_time
            if elapsed_time.total_seconds() >= self.cooldown:
                return True
            else:
                return False

    # This class holds a word, and point values for each of the four heroines
    class NewPoemWord:
        def __init__(self, word, sPoint, nPoint, yPoint, mPoint, glitch=False):
            self.word = word
            self.sPoint = sPoint
            self.nPoint = nPoint
            self.yPoint = yPoint
            self.mPoint = mPoint
            self.glitch = glitch

    # Building the word list
    full_new_wordlist = []
    with renpy.file('m_poemwords.txt') as wordfile:
        for line in wordfile:
            # Ignore lines beginning with '#' and empty lines
            line = line.strip()

            if line == '' or line[0] == '#': continue

            # File format: word,sPoint,nPoint,yPoint,mPoint
            x = line.split(',')
            full_new_wordlist.append(NewPoemWord(x[0], float(x[1]), float(x[2]), float(x[3]), float(x[4])))
                
    #This function draws the poemwords
    def draw_words(cTimer):
        ystart = 160
        pstring = str(progress)
        ui.text(pstring + "/" + str(numWords), style="poemgame_text", xpos=810, ypos=80, color='#000')
        for j in range(2):
            if j == 0: x = 440
            else: x = 680
            ui.vbox()
            for i in range(5):
                z = i + (j * 5)
                word = random.choice(wordlist)
                wordlist.remove(word)
                ui.textbutton(word.word, clicked=Function(select_doki, word, cTimer, _update_screens=False), hovered=Function(show_doki, word, cTimer, "smile"), unhovered=Function(show_doki, word, cTimer), text_style="poemgame_text", xpos=x, ypos=i * 56 + ystart)
            ui.close()
        
    #This function shows the dokis
    def show_doki(t, cTimer, action = ""):
        if action == "hop" or cTimer.hasFinished():
            if t.sPoint >= 3:
                renpy.show("s_sticker " + action)
            if t.nPoint >= 3:
                renpy.show("n_sticker " + action)
            if t.yPoint >= 3:
                renpy.show("y_sticker " + action)
            if t.mPoint >= 3:
                renpy.show("m_sticker " + action)        
    
    #This function selects the doki and the correct word and saves the score change
    def select_doki(t, cTimer, action = "hop"):
        renpy.play(gui.activate_sound)
        store.sPointTotal += t.sPoint
        store.nPointTotal += t.nPoint
        store.yPointTotal += t.yPoint
        store.mPointTotal += t.mPoint
        store.progress += 1
        #Added stuff that is important to only do on selection
        show_doki(t, cTimer, action) #Show the animation
        cTimer.start() #Start cooldown timer
        return ui.returns() #End the UI interaction
      
label new_m_poem(transition=True):
    stop music fadeout 2.0
    scene bg notebook
    show screen quick_menu
    show s_sticker at sticker_leftest
    show n_sticker at sticker_lmid
    show y_sticker at sticker_rmid
    show m_sticker at sticker_rightest
    if transition:
        with dissolve_scene_full
    play music t4
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    if persistent.playthrough == 0 and chapter == 0:
        call screen dialog("It's time to write a poem!\n\nPick words you think your favorite club member\nwill like. Something good might happen with\nwhoever likes your poem the most!", ok_action=Return())
    python:
        poemgame_glitch = False
        played_baa = False
        progress = 1
        numWords = 20
        sPointTotal = 0
        nPointTotal = 0
        yPointTotal = 0
        mPointTotal = 0 #added Monika!
        
        #Wordlist
        wordlist = list(full_new_wordlist)

        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        monikaTime = renpy.random.random() * 4 + 4
        sayoriPos = renpy.random.randint(-1,1)
        natsukiPos = renpy.random.randint(-1,1)
        yuriPos = renpy.random.randint(-1,1)
        monikaPos = renpy.random.randint(-1,1)
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        monikaOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        monikaZoom = 1

        # Main loop for drawing and selecting words
        hopTimer = CooldownTimer(0.72)
        while True:
            draw_words(hopTimer)
            ui.interact() #Begin a UI interaction
            if progress > numWords:
                break
                
        # Logic for taking point totals and assigning poem appeal, scene order, etc.
        unsorted_pointlist = {"sayori": sPointTotal, "natsuki": nPointTotal, "yuri": yPointTotal, "monika": mPointTotal}
        pointlist = sorted(unsorted_pointlist, key=unsorted_pointlist.get)
        
        # Set poemwinner to the highest scorer   
        poemwinner[chapter] = pointlist[-1]

        # Add appeal point based on poem winner
        exec(poemwinner[chapter][0] + "_appeal += 1")

        # Set poemappeal
        if sPointTotal < POEM_DISLIKE_THRESHOLD: s_poemappeal[chapter] = -1
        elif sPointTotal > POEM_LIKE_THRESHOLD: s_poemappeal[chapter] = 1
        if nPointTotal < POEM_DISLIKE_THRESHOLD: n_poemappeal[chapter] = -1
        elif nPointTotal > POEM_LIKE_THRESHOLD: n_poemappeal[chapter] = 1
        if yPointTotal < POEM_DISLIKE_THRESHOLD: y_poemappeal[chapter] = -1
        elif yPointTotal > POEM_LIKE_THRESHOLD: y_poemappeal[chapter] = 1
        if mPointTotal < POEM_DISLIKE_THRESHOLD: m_poemappeal[chapter] = -1
        elif mPointTotal > POEM_LIKE_THRESHOLD: m_poemappeal[chapter] = 1

        # Poem winner always has appeal 1 (loves poem)
        exec(poemwinner[chapter][0] + "_poemappeal[chapter] = 1")

    $ config.allow_skipping = True
    $ allow_skipping = True
    stop music fadeout 2.0
    hide screen quick_menu
    show black as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    pause 1.0
    return

transform sticker_leftest:
    xcenter 60 yalign 0.9 subpixel True
    
transform sticker_lmid:
    xcenter 160 yalign 0.9 subpixel True

transform sticker_rmid:
    xcenter 260 yalign 0.9 subpixel True

transform sticker_rightest:
    xcenter 360 yalign 0.9 subpixel True

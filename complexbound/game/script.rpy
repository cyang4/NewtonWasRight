﻿# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eve', color="#000040", kind=nvl)
define c = Character('Chadwick', color="#004000", kind = nvl)
define k = Character('Kentin', color="#c00000", kind=nvl)
define a = Character('Adam', color="#741b47", kind=nvl)
define l = Character('Lorella', color="#00ff80", kind=nvl)
image eveHome = "roomnight.png"

# The game starts here.
label start:
    scene eveHome

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"
    
    c "I am Narcissus?! What the heck?!"
    k "Heh, serves you right."
    nvl clear
    a "Hi guys"
    e "omg who r u"
    

    return

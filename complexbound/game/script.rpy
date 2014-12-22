# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image eveHome = "roomnight.png"
image hallwayNight = "hallwaynight.png" # This hallway is the 13th floor only.
image stairsNight = "flightstairsnight.png"
image windowOpen = "window2.png"

# Declare characters used by this game.
define eve = Character('Eve', color="#000040", kind=nvl)
define chadwick = Character('Chadwick', color="#004000", kind = nvl)
define kentin = Character('Kentin', color="#c00000", kind=nvl)
define adam = Character('Adam', color="#741b47", kind=nvl)
define lorella = Character('Lorella', color="#00ff80", kind=nvl)

define daedalus = Character('Daedalus', color="#000040", kind=nvl)
define narcissus = Character('Narcissus', color="#004000", kind=nvl)
define pygmalion = Character('pygmalion', color ="#c00000", kind=nvl)
define icarus = Character('Icarus', color="#741b47", kind=nvl)
define galatea = Character('Galatea', color="#00ff80", kind=nvl)
define medusa = Character('Medusa', color="#6B238E", kind=nvl)

# The game starts here.
label start:
    scene eveHome

    eve "You've created a new Ren'Py game."

    eve "Once you add a story, pictures, and music, you can release it to the world!"
    
    chadwick "I am Narcissus?! What the heck?!"
    kentin "Heh, serves you right."
    nvl clear
    adam "Hi guys"
    eve "omg who r u"
    

    return

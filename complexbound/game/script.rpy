# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image eveHome = "roomnight.png"
image hallwayNight13 = "hallwaynight.png" # This hallway is the 13th floor only.
image stairsNight = "flightstairsnight.png"
image windowOpen = "window2.png"
image rooftop = "rooftop.jpg"
image eveRoom = "everoom.jpg"
image kentinRoom = "bedroom-3.png"

# Declare characters used by this game.
define narrator = Character(None, what_color="#ffffff", kind=nvl)

define eve = Character('Eve', color="#000040", what_color="#ffffff", kind=nvl)
define chadwick = Character('Chadwick', color="#004000", what_color="#ffffff", kind = nvl)
define kentin = Character('Kentin', color="#c00000", what_color="#ffffff", kind=nvl)
define adam = Character('Adam', color="#741b47", what_color="#ffffff", kind=nvl)
define lorella = Character('Lorella', color="#00ff80", what_color="#ffffff", kind=nvl)

define daedalus = Character('Daedalus', color="#000040", what_color="#ffffff", kind=nvl)
define narcissus = Character('Narcissus', color="#004000", what_color="#ffffff", kind=nvl)
define pygmalion = Character('Pygmalion', color ="#c00000", what_color="#ffffff", kind=nvl)
define icarus = Character('Icarus', color="#741b47", what_color="#ffffff", kind=nvl)
define galatea = Character('Galatea', color="#00ff80", what_color="#ffffff", kind=nvl)
define medusa = Character('Medusa', color="#6B238E", what_color="#ffffff", kind=nvl)

# The game starts here.
label start:
    jump DayOneEve

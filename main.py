# My Turtle Race Program
# My Name is:
# -    -    -    -    -    -    -    -    -    -    -

# let us use the SpringBoard turtle race_utility
# as our framework to code this game.
from race_utility import f_draw_finish
from race_utility import f_createTurtle
from race_utility import f_startRace


# Three Steps: Add your lines of code here
# -    -    -    -    -    -    -    -    -    -    -
f_draw_finish()
# Step 1: draw the markers as lines

# Step 2: create one or 4 turtles eg. f_createTurtle('color', 1)
t1=f_createTurtle('blue', 1)
t2=f_createTurtle('red', 2)
t3=f_createTurtle('orange', 3)
t4=f_createTurtle('green', 4)
# Step 3: start the race
f_startRace(t1, t2, False, t4)


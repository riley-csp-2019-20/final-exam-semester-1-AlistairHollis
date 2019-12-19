#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
# Alistair Hollis
#Date
# 12/19/2019


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle # imports the turtle module

#create turtle
drawer = turtle.Turtle() # creates the drawer module


#movement functions
up = 270
down = 90
left = 180
right = 0
def move_up(): # defines the move forward function
    if 
    drawer.setheading(90)
    drawer.forward(10)
def move_down(): # defines the move backward function
    drawer.setheading(270)
    drawer.forward(10)
def move_left(): # defines the turn left (CCW) function
    drawer.setheading(180)
    drawer.forward(10)
def move_right(): # defines the turn right (CW) function
    drawer.setheading(0)
    drawer.forward(10)

#color/drawing functions
drawing = True # initializes a variable that is used in the pen_check function
sizepen = 1 # initializes a variable that is used in the pen_check function
drawer_state = "visible" # initializes a variable that is used in the visibility function

def pen_check(): # defines a function that changes the pen state
    global drawing
    if (drawing == True): # if the pen is down, take the pen up
        drawing = False
        drawer.pu()
    elif (drawing == False): # if the pen is up, put the pen down
        drawing = True
        drawer.pd()

def size_bigger(): # defines the pen size increase function
    global sizepen
    sizepen += 2
    drawer.pensize(sizepen)
    drawer.shapesize(sizepen)

def size_smaller(): # defines the pen size decrease function
    global sizepen
    sizepen -= 2
    if (sizepen <= 0):
        sizepen = 1
    drawer.pensize(sizepen)
    drawer.shapesize(sizepen)

def board_clear(): # defines the function that clears the board
    drawer.clear()

def visibility(): # defines the function that hides the turtle
    global drawer_state
    if (drawer_state == "visible"):
        drawer_state = "invisible"
        drawer.ht()
    elif (drawer_state == "invisible"):
        drawer_state = "visible"
        drawer.st()

#create screen
wn = turtle.Screen() #  you literally commented this one for me

#bind to keypresses
wn.onkeypress(move_up,"Up") # checks for key "Up" and runs the function
wn.onkeypress(move_down,"Down") # checks for key "Down" and runs the function
wn.onkeypress(move_left,"Left") # checks for key "Left" and runs the function
wn.onkeypress(move_right,"Right") # checks for key "Right" and runs the function
wn.onkeyrelease(pen_check,"u") # checks for key "u" and runs the function
wn.onkeyrelease(size_bigger,"o") # checks for key "o" and runs the function
wn.onkeyrelease(size_smaller,"p") # checks for key "p" and runs the function
wn.onkeyrelease(board_clear,"space") # checks for key "space" and runs the function
wn.onkeyrelease(visibility,"v") # checks for key "v" and runs the function

#listen
wn.listen() # listens for the keyboard checks

#mainloop
wn.mainloop() # makes the window persist after all commands are finished running
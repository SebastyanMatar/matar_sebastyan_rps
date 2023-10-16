#This file was created by Sebastyan matar

#This file was created by Sebastyan Matar

'''
Goals - when a user clicks on their choice the computer randomly chooses and displays the result


'''

# import package
import turtle
from turtle import *
# The os module allows us to access the current directory in order to access assets
import os
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

from random import randint

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')



cpu_choice = ""
# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

rock_w, rock_h = 256, 280

paper_w, paper_h = 256, 204

scissors_w, scissors_h = 256, 170


# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")


# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)


# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
# instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()
# add the rock image as a shape
screen.addshape(rock_image)
# attach the rock_image to the rock_instance
rock_instance.shape(rock_image)
# remove the pen option from the rock_instance so it doesn't draw lines when moved
rock_instance.penup()
#Assign vars for paper position
rock_pos_x = -300
rock_pos_y = 0

# set the position of the rock_instance
rock_instance.setpos(rock_pos_x,rock_pos_y)


# setup the paper image using the os module as paper_image
paper_image = os.path.join(images_folder, 'paper.gif')
# instantiate (create an instance of) the Turtle class for the paper
paper_instance = turtle.Turtle()
# add the paper image as a shape
screen.addshape(paper_image)
# attach the paper_image to the paper_instance
paper_instance.shape(paper_image)
# remove the pen option from the paper_instance so it doesn't draw lines when moved
paper_instance.penup()
# assign vars for paper position
paper_pos_x = 0
paper_pos_y = 0
# set the position of the paper_instance
paper_instance.setpos(paper_pos_x,paper_pos_y)


# setup the scissors image using the os module as scissors_image
scissors_image = os.path.join(images_folder, 'scissors.gif')
# instantiate (create an instance of) the Turtle class for the scissors
scissors_instance = turtle.Turtle()
# add the scissors image as a shape
screen.addshape(scissors_image)
# attach the scissors_image to the scissors_instance
scissors_instance.shape(scissors_image)
# remove the pen option from the scissors_instance so it doesn't draw lines when moved
scissors_instance.penup()
# assign vars for scissors position
scissors_pos_x = 300
scissors_pos_y = 0
# set the position of the scissors_instance
scissors_instance.setpos(scissors_pos_x,scissors_pos_y)


# instantiate a generic turtle
t = turtle.Turtle()
# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('deep pink')
text.hideturtle()

# hide that turtle
t.hideturtle()

choices = ["rock", "paper", "scissors"]
cpu_choice = choices[randint(0,len(choices)-1)]

# this function uses and x y value, an obj/ 
# This function sets a square shape with turtle that if you collide with it it returns the value "true"
# It works by going to the center of whatever object and then just basically expands outwards making a square around that point
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] -  w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

#This sets the previous collide function to our rock instance so it forms the hitbox around the rock and if you collide with the hitbox it prints it collided with rock
# function that passes through wn onlick
def mouse_pos(x, y):
    global playerchoice
    if collide(x,y,rock_instance,rock_w,rock_h):
        print("i chose rock...")
        playerchoice = "rock"
        print ("cpu chooses " + cpu_choice)
        paper_instance.hideturtle()
        scissors_instance.hideturtle()
    elif collide(x,y,paper_instance,paper_w,paper_h):
        print("i chose paper...")
        playerchoice = "paper"
        print ("cpu chooses " + cpu_choice)
        rock_instance.hideturtle()
        scissors_instance.hideturtle()
    elif collide(x,y,scissors_instance,scissors_w,scissors_h):
        print("i chose scissors...")
        playerchoice = "scissors"
        print ("cpu chooses " + cpu_choice)
        rock_instance.hideturtle()
        paper_instance.hideturtle()
    else:
        print("Choose something please")
#This allows the code to determine who won/lost depending on what the player and cpu choose
    if cpu_choice == playerchoice:
        print("You tied!")
    if playerchoice == "rock":
        if cpu_choice == "paper":
            print("You lost")
        elif cpu_choice == "scissors":
            print("You won")
    elif playerchoice == "paper":
        if cpu_choice == "rock":
            print("You won")
        elif cpu_choice == "scissors":
            print("You lost")
    elif playerchoice == "scissors":
        if cpu_choice == "paper":
            print("You won")
        elif cpu_choice == "rock":
            print("You lost")


text.penup()
text.setpos(0,150)
text.write("Choose rock or paper or scissors", False,"left", ("Arial"))


screen.onclick(mouse_pos)
# runs mainloop for Turtle - required to be last
#Calls your functions
screen.mainloop()



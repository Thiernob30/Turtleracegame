#author
#date
#Desrcription
#revision history
#Name   Date     Desc
#scl    2/12/24     initial code base
#
#

import random
import turtle
import time
number_list = []

start_pos_x = -100
start_pos_y = 0
level = 3
offset = 100

def drawsquare(x,y):

    turtle.down()
for x in range(4):
    turtle.forward(100)
    turtle.left(90)

for x in range(level):
    # data structure
    a = random.randint(1,99)
    number_list.append(a)
    
    turtle.write(str(a), font=("verdana",50, "normal"))
    turtle.up()
    save_pos = (x * offset,0)
    turtle.goto(save_pos)
    time.sleep(3)

turtle.clear()

# please enter the answers
for x in range(level):
 answer = int(input("The numbers were: "))

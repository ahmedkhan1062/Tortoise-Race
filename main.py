from turtle import Turtle, Screen
import random
sc = Screen()

red = Turtle()
blue = Turtle()
green = Turtle()
yellow = Turtle()


turtles = [red, blue, green, yellow]

def moveFor(thing = Turtle):
    steps = random.randint(1, 15)
    thing.forward(steps)

#print(red.)
red.color("red")
red.shape("turtle")

#print(red.color())
blue.color("blue")
blue.shape("turtle")

green.color("green")
green.shape("turtle")

yellow.color("black")
yellow.shape("turtle")

red.penup()
blue.penup()
green.penup()
yellow.penup()

red.goto(-300,-100)
blue.goto(-300, 0)
green.goto(-300, 100)
yellow.goto(-300, 200)

winner = "nobody"
prediction = input("Bet of a turtle to win the race")

while winner == "nobody":
    for i in turtles:

        moveFor(i)
        #print(i.position)
        if i.position()[0] > 300:
            winner = i.pencolor()


if prediction == winner:
    print("Congratulations, the "+ winner+ " turtle has won the race!")
else:
    print("You lose, the "+winner+" turtle has won the race...")
sc.exitonclick()
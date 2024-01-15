import turtle
from random import randint
import time
import threading
#Screen
game_screen = turtle.Screen()
game_screen.bgcolor("light blue")
game_screen.title("Catch The Turtle")
game_screen.listen()



#Turtle
turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("green")
turtle_instance.shapesize(3,3,1)
turtle_instance.penup()
turtle_instance.speed(0)

#Timer
pen_2 = turtle.Turtle()
pen_2.speed(0)
pen_2.hideturtle()
pen_2.color("black")
pen_2.penup()
pen_2.goto(0, 300)

#Scoreboard
score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.shape("square")
pen.color("black")
pen.penup()
pen.goto(0, 330)
pen.write(f"Score: 0", align="center", font=("Courier", 24, "normal"))


def score_board(x,y):
    global score
    score = score + 1
    pen.clear()
    pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

def score_board_2(x,y):
    global score
    score = score + 0
    pen.clear()
    pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))



def main_2():


    def countdown_timer():


        t = 10

        while t >= 0:
            pen_2.write(f"Kalan Süre: {t}", align="center", font=("Courier", 24, "normal"))
            time.sleep(1)
            t -= 1
            pen_2.clear()
            if t > 0:
                turtle_instance.onclick(score_board, 1)
            else:
                turtle_instance.hideturtle()
        pen_2.write("Game Over!", align="center", font=("Courier", 24, "normal"))




    def turtle_movement():

        for i in range(20):
            turtle_instance.color("light blue")
            turtle_instance.goto(randint(-340,340), randint(-320,225))
            turtle_instance.color("green")
            time.sleep(0.5)


    threading_timer = threading.Thread(target=countdown_timer)
    threading_move = threading.Thread(target=turtle_movement)

    threading_timer.start()
    threading_move.start()

main_2()


turtle.mainloop()

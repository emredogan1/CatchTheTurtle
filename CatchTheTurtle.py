import turtle
import random

#ekranımızı oluşturuyoruz
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
FONT = ("Arial",30,"normal")

score = 0
game_over = False


turtle_list = []

#score bölümünü oluşturuyoruz
score_turtle = turtle.Turtle()

#time bölümü oluşturuyoruz
countdown_turtle = turtle.Turtle()

#turtle oluşması için gerekli koordinatlar
x_coordinates = [-20,-10,0,10,20]
y_coordinates = [20,10,0,-10]


def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen.window_height()
    y = top_height * 0.8


    score_turtle.setpos(0, y/2 )
    score_turtle.write(arg="Score:0",move=False,align="center",font=FONT)

#turtle oluşturuyoruz

def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=FONT)

    t.onclick(handle_click)
    grid_size = 10
    t.penup()
    t.color("green")
    t.shape("turtle")
    t.shapesize(2)
    t.goto(grid_size*x,grid_size*y)
    turtle_list.append(t)



def set_up_turtle():
    for i in x_coordinates:
        for j in y_coordinates:
            make_turtle(i,j)

def hide_turtle():
    for t in turtle_list:
        t.hideturtle()

def show_turtle_randomly():
    if not game_over:
        hide_turtle()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtle_randomly,1000)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("dark blue")
    countdown_turtle.penup()

    top_height = screen.window_height()
    y = top_height * 0.7

    countdown_turtle.setpos(0, y / 2)
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.color("black")
        countdown_turtle.write(arg="Time:{}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda:countdown(time-1),1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtle()
        countdown_turtle.write(arg="Game Over", move=False, align="center", font=FONT)

def start_game_up():
    turtle.tracer(0)
    setup_score_turtle()
    set_up_turtle()
    hide_turtle()
    show_turtle_randomly()
    countdown(10)
    turtle.tracer(1)

start_game_up()
turtle.mainloop()






import turtle

screen = turtle.Screen()
screen.title("BMW Logo")
screen.setup(width=600, height=600)
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)


def draw_circle(radius, outline_color, fill_color=None, width=2):
    t.penup()
    t.goto(0, -radius)
    t.setheading(0)
    t.pendown()
    t.pensize(width)
    t.pencolor(outline_color)
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()


def draw_quadrant(radius, start_angle, color):
    t.penup()
    t.goto(0, 0)
    t.setheading(start_angle)
    t.pendown()
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.forward(radius)
    t.left(90)
    t.circle(radius, 90)
    t.goto(0, 0)
    t.end_fill()


def write_text():
    t.penup()
    t.goto(0, 180)
    t.color("black")
    t.write("BMW", align="center", font=("Arial", 32, "bold"))


def draw_bmw_logo():
    draw_circle(145, "black", fill_color="black")
    draw_circle(135, "white", fill_color="white")
    draw_circle(120, "black", fill_color="black")

    radius_inner = 95
    draw_quadrant(radius_inner, 0, "white")
    draw_quadrant(radius_inner, 90, "#0066ad")
    draw_quadrant(radius_inner, 180, "white")
    draw_quadrant(radius_inner, 270, "#0066ad")

    write_text()


draw_bmw_logo()

turtle.done()

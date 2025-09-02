import turtle
import time

# Ventana
wn = turtle.Screen()
wn.title("Arcade Pong, GDHS")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(1)

# Marcador
marcador_1 = 0
marcador_2 = 0

# Jugador 1
jugador_1 = turtle.Turtle()
jugador_1.speed(0)
jugador_1.shape("square")
jugador_1.color("white")
jugador_1.penup()
jugador_1.goto(-350, 0)
jugador_1.shapesize(stretch_wid=5, stretch_len=1)

# Jugador 2
jugador_2 = turtle.Turtle()
jugador_2.speed(0)
jugador_2.shape("square")
jugador_2.color("white")
jugador_2.penup()
jugador_2.goto(350, 0)
jugador_2.shapesize(stretch_wid=5, stretch_len=1)

# Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 7
pelota.dy = 7

# Linea divisoria
division = turtle.Turtle()
division.color("white")
division.goto(0, 400)
division.goto(0, -400)

# Marcador en pantalla
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jugador 1: 0         Jugador 2: 0",
          align="center", font=("Courier", 24, "bold"))

#  FUNCIONES 
# Jugador 1
def jugador_1_up():
    y = jugador_1.ycor()
    if y < 250:  # límite superior
        y += 20
        jugador_1.sety(y)

def jugador_1_down():
    y = jugador_1.ycor()
    if y > -250:  # límite inferior
        y -= 20
        jugador_1.sety(y)

# Jugador 2
def jugador_2_up():
    y = jugador_2.ycor()
    if y < 250:
        y += 20
        jugador_2.sety(y)

def jugador_2_down():
    y = jugador_2.ycor()
    if y > -250:
        y -= 20
        jugador_2.sety(y)

# CONTROLES 
wn.listen()
wn.onkeypress(jugador_1_up, "w")
wn.onkeypress(jugador_1_down, "s")
wn.onkeypress(jugador_2_up, "Up")
wn.onkeypress(jugador_2_down, "Down")

# BUCLE PRINCIPAL 
while True:
    wn.update()

    # Movimiento de la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Bordes superior / inferior
    if pelota.ycor() > 290:
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.dy *= -1

    # Bordes derecho / izquierdo
    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        marcador_1 += 1
        pen.clear()
        pen.write("Jugador 1: {}         Jugador 2: {}".format(marcador_1, marcador_2),
                  align="center", font=("Courier", 24, "bold"))
        time.sleep(1)

    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        marcador_2 += 1
        pen.clear()
        pen.write("Jugador 1: {}         Jugador 2: {}".format(marcador_1, marcador_2),
                  align="center", font=("Courier", 24, "bold"))
        time.sleep(1)

    # Colisiones con las paletas
    # Jugador 2
    if (pelota.xcor() > 340 and pelota.xcor() < 350) and \
       (jugador_2.ycor() - 50 < pelota.ycor() < jugador_2.ycor() + 50):
        pelota.dx *= -1

    # Jugador 1
    if (pelota.xcor() < -340 and pelota.xcor() > -350) and \
       (jugador_1.ycor() - 50 < pelota.ycor() < jugador_1.ycor() + 50):
        pelota.dx *= -1

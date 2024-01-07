import turtle

WIDTH, HEIGHT = 800, 600
PADDLE_SPEED = 35
BALL_SPEED_X = 0.05
BALL_SPEED_Y = -0.05

wn = turtle.Screen()
wn.title("BaoPong")
wn.bgcolor("black")
wn.setup(width=WIDTH, height=HEIGHT)
wn.tracer(0)

score_a = 0
score_b = 0

def create_paddle(x, y):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape('square')
    paddle.color('white')
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(x, y)
    return paddle

paddle_a = create_paddle(-350, 0)
paddle_b = create_paddle(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = BALL_SPEED_X
ball.dy = BALL_SPEED_Y

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

def update_score():
    pen.clear()
    pen.write(f'Player 1: {score_a} | Player 2: {score_b}', align='center', font=("Calibri", 24, 'underline'))

def paddle_up(paddle):
    y = paddle.ycor()
    y += PADDLE_SPEED
    paddle.sety(y)

def paddle_down(paddle):
    y = paddle.ycor()
    y -= PADDLE_SPEED
    paddle.sety(y)

wn.listen()
wn.onkey(lambda: paddle_up(paddle_a), 'w')
wn.onkey(lambda: paddle_down(paddle_a), 's')
wn.onkey(lambda: paddle_up(paddle_a), 'W')
wn.onkey(lambda: paddle_down(paddle_a), 'S')
wn.onkey(lambda: paddle_up(paddle_b), 'Up')
wn.onkey(lambda: paddle_down(paddle_b), 'Down')

def reset_ball():
    ball.goto(0, 0)
    ball.dx = BALL_SPEED_X
    ball.dy = BALL_SPEED_Y

while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() > 390:
        score_a += 1
        update_score()
        reset_ball()

    if ball.xcor() < -390:
        score_b += 1
        update_score()
        reset_ball()

    if (ball.xcor() > 340 and ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1.2

    if (ball.xcor() < -340 and ball.xcor() > -350) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1.2

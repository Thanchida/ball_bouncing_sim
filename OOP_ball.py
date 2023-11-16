import turtle
import random


class Ball:
    def __init__(self, canvas_width, canvas_height, ball_radius):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.ball_radius = ball_radius
        self.num_balls = 0
        self.color = []
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []

    def draw_circle(self, color, size, x, y):
        turtle.penup()
        turtle.color(color)
        turtle.fillcolor(color)
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(size)
        turtle.end_fill()

    def move_circle(self, i):
        self.xpos[i] += self.vx[i]
        self.ypos[i] += self.vy[i]

        if abs(self.xpos[i] + self.vx[i]) > (self.canvas_width - self.ball_radius):
            self.vx[i] = -self.vx[i]

        if abs(self.ypos[i] + self.vy[i]) > (self.canvas_height - self.ball_radius):
            self.vy[i] = -self.vy[i]

    def initializing(self, num_balls):
        self.num_balls = num_balls
        for i in range(self.num_balls):
            x = random.randint(-1 * self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius)
            y = random.randint(-1 * self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius)
            vx = random.randint(1, 0.01 * self.canvas_width)
            vy = random.randint(1, 0.01 * self.canvas_height)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            self.xpos.append(x)
            self.ypos.append(y)
            self.vx.append(vx)
            self.vy.append(vy)
            self.color.append(color)

    def simulation(self):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()

        turtle.colormode(255)
        while True:
            turtle.clear()
            for i in range(self.num_balls):
                self.draw_circle(self.color[i], self.ball_radius, self.xpos[i], self.ypos[i])
                self.move_circle(i)
            turtle.update()


num_balls = int(input("Number of balls to simulate: "))
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
ball_radius = 0.05 * canvas_width
ball = Ball(canvas_width, canvas_height, ball_radius)
ball.initializing(num_balls)
ball.simulation()

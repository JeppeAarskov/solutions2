import turtle
import math
import random

class Fuld(turtle.Turtle):

    def rotate_prey(self, positions):
        degree = 50
        return degree

    def rotate_hunter(self, positions):
        degree = -5
        return degree

class Traktor(turtle.Turtle):

    def rotate_prey(self, positions):
        degree = 2.2
        return degree

    def rotate_hunter(self, positions):
        degree = 1
        return degree

def distance(pos1, pos2):
    delta_x = pos1[0] - pos2[0]
    delta_y = pos1[1] - pos2[1]
    return math.sqrt(delta_x ** 2 + delta_y ** 2)


def direction(start_turtle, end_turtle):
    delta_x = end_turtle.position()[0] - start_turtle.position()[0]
    delta_y = end_turtle.position()[1] - start_turtle.position()[1]
    angle = math.atan2(delta_y, delta_x) * 180 / math.pi
    if delta_y < 0:
        return -angle
    else:
        return 360 - angle


def move(turtle_):
    turtle_.forward(STEP_SIZE)
    x, y = turtle_.position()
    if abs(x) > MAX_POS or abs(y) > MAX_POS:
        turtle_.right(360)
        turtle_.forward(BOUNCE_STEP_SIZE)
        turtle_.right(360)


def caught(turtles_, max_distance):
    positions = [t.position() for t in turtles_]
    for hunter_position in positions[1:]:
        if distance(positions[0], hunter_position) < max_distance:
            return True
    return False


def init_positions(turtles_):  # move turtles to their initial random positions
    for turtle_, min_angle, max_angle in zip(turtles_, START_ANGLES_MIN, START_ANGLES_MAX):
        angle = random.randint(min_angle, max_angle)
        turtle_.right(360)
        turtle_.penup()
        turtle_.forward(random.randint(START_DISTANCE_MIN, START_DISTANCE_MAX))
        turtle_.right(-180)
        turtle_.pendown()


def hunt(prey_class, hunter_class, color):
    screen = turtle.Screen()
    screen.setup(2 * MAX_POS, 2 * MAX_POS)
    # initialize turtles:
    prey = prey_class()
    hunter1 = hunter_class()
    hunter2 = hunter_class()
    hunter3 = hunter_class()
    hunters = [hunter1, hunter2, hunter3]
    turtles = [prey, hunter1, hunter2, hunter3]
    prey.pencolor(color)
    for t in turtles:
        t.speed(SPEED)
        t.shape("turtle")
    init_positions(turtles)

    turn = 0
    positions = [t.position() for t in turtles]
    while not caught(turtles, CAUGHT_DISTANCE) and turn < MAX_TURNS:
        turn += 1
        for h in hunters:
            h.right(h.rotate_hunter(positions))
        prey.right(prey.rotate_prey(positions))
        for t in turtles:
            move(t)
            positions = [t.position() for t in turtles]

    turtle.clearscreen()
    if turn < MAX_TURNS:
        print(f'Caught after {turn} turns.')
    else:
        print(f'Prey not caught after {turn} turns. Prey receives {turn} bonus points on top.')
        turn *= 2
    return turn

MAX_TURNS = 200
ROUNDS = 10
STEP_SIZE = 3
SPEED = 0
CAUGHT_DISTANCE = 10

random.seed(2)
class1 = Fuld
class2 = Traktor

MAX_POS = 300
BOUNCE_STEP_SIZE = 2 * STEP_SIZE
START_ANGLES_MIN = [0, 90, 180, 270]
START_ANGLES_MAX = [30, 120, 210, 300]
START_DISTANCE_MIN = int(MAX_POS * 0.6)
START_DISTANCE_MAX = int(MAX_POS * 0.9)

score1 = score2 = 0
for r in range(ROUNDS):
    score1 += hunt(class1, class2, "red")
    score2 += hunt(class2, class1, "green")
    print(f"Score after round {r + 1}: {class1.__name__}: {score1}    {class2.__name__}: {score2}")
turtle.done()
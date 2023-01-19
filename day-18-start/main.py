import turtle as t
import random

tim = t.Turtle()
# tim.shape("turtle")
# tim.color("OliveDrab")
# tim.fd(100)
# tim.right(90)

# Square
# for _ in range(4):
#     tim.fd(100)
#     tim.left(90)

# Dashed Line
# for _ in range(10):
#     tim.color("black")
#     tim.fd(10)
#     tim.pendown
#     tim.color("white")
#     tim.penup
#     tim.fd(10)

# Dynamic Shape
# for _ in range(3): #triangle
#     tim.color("DarkTurquoise")
#     tim.forward(100)
#     tim.right(120)

# for _ in range(4): #square
#     tim.color("gray60")
#     tim.forward(100)
#     tim.right(90)

# for _ in range(5): #pentagon
#     tim.color("brown4")
#     tim.forward(100)
#     tim.right(72)

# for _ in range(6): #hexagon
#     tim.color("gold")
#     tim.forward(100)
#     tim.right(60)

# for _ in range(7): #heptagon
#     tim.color("HotPink")
#     tim.forward(100)
#     tim.right(51.4)

# for _ in range(8): #octagon
#     tim.color("DarkTurquoise")
#     tim.forward(100)
#     tim.right(45)

# for _ in range(9): #nonagon
#     tim.color("gray90")
#     tim.forward(100)
#     tim.right(40)


# Second Method
# colors = ["DarkTurquoise", "gray60", "brown4"," gold", "HotPink", "DarkTurquoise", "gray90", "OrangeRed", "IndianRed"]
# def draw_shapes(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tim.fd(100)
#         tim.right(angle)


# for shape_side_n in range(3, 13):
#     # color = colors[shape_side_n]
#     tim.color(random.choice(colors))
#     draw_shapes(shape_side_n)

# Random Walk
# t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color


# direction_list = [0, 90, 180, 270]
# tim.width(15)
# tim.speed("fastest")

# # steps = [10, 20, 30]

# # def move(direct):
# #     tim.left(direct)


# for _ in range(2000):
#     tim.color(random_color())
#     # tim.fd(random.choice(steps))
#     tim.fd(30)
#     # direction = random.choice(direction_list)
#     tim.setheading(random.choice(direction_list))
#     # move(random.choice(direction_list))

## Spirograph
# t.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color

# tim.speed("fastest")
# size = 200
# current_heading = tim.heading()

# for _ in range(72):
#     tim.color(random_color())
#     tim.circle(size)
#     current_heading += 5
#     tim.setheading(current_heading)



screen = t.Screen()
screen.exitonclick()

import turtle

tim = turtle.Turtle()
tim.color('red')
tim.pensize(5)
tim.shape('turtle')


steps = [
    ("forward", 100),
    ("left", 90),
    ("forward", 100),
    ("right", 90),
    ("backward", 100),
    ("left", 90),
    ("backward", 100)
]

i = 0
while i < len(steps):
    action, value = steps[i]
    getattr(tim, action)(value)
    i += 1

tim.right(30)
for _ in range(3):
    tim.forward(100)
    tim.right(120)

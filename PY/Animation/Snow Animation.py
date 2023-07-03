import turtle as t
t.bgcolor('#252525')
t.pensize(2)
t.pencolor('cyan')
t.speed(0)
for i in range(139):
    for j in range(2):
        t.forward(i)
        t.right(20)
        t.left(50)
        t.right(120)
        t.forward(i)
    t.right(120)
t.done()
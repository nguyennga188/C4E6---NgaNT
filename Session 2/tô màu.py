from turtle import *
speed(-1)
shape("turtle")

for n in range(12, 2, -1):
    if n % 2 == 0:
        color("green", "yellow")
        begin_fill()
        for _ in range(n):
            forward(60)
            left(180 - 180 * (n-2) / n)
        end_fill()
    else:
        color("red", "violet")
        begin_fill()
        for _ in range(n):
            forward(60)
            left (180 - 180 * (n-2) / n)
        end_fill()
            
        

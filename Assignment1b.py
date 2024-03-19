Python 3.13.0a4 (tags/v3.13.0a4:9d34f60, Feb 15 2024, 17:00:30) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import turtle
>>> import random
>>> 
>>> def screenLeftClick(x, y) :
...     global r, g, b
...     turtle.pencolor((r, g, b))
...     turtle.pendown()
...     turtle.goto(x,y)
... 
...     
>>> def screenRightClick(x, y) :
...     turtle.penup()
...     turtle.goto(x, y)
... 
...     
>>> def screenMidClick(x, y) :
...     global r, g, b
...     tSize = random.randrange(1, 10)
...     turtle.shapesize(tSize)
...     r = random.random()
...     g = random.random()
...     b = random.random()
... 
...     
>>> pSize = 10
>>> r, g, b = 0.0, 0.0, 0.0
>>> 
>>> turtle.title('거북이로 그림 그리기')
>>> turtle.shape('turtle')
>>> turtle.pensize(pSize)
>>> 
>>> turtle.onscreenclick(screenLeftClick, 1)
>>> turtle.onscreenclick(screenMidClick, 2)
>>> turtle.onscreenclick(screenRightClick, 3)
>>> 
>>> turtle.done()

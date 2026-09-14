from tkinter import Canvas
from turtle import *
import numpy as np
import tensorflow as tf

#Loading model
model = tf.keras.models.load_model('digit_classifier.keras')

#setup teh grid so our model can use
grid = np.zeros((28,28))

#turtle setup
pen = Turtle()

#screen setup
screen = Screen()
screen.bgcolor("black")
screen.setworldcoordinates(0,28,28,0)
screen.setup(width=560,height=560)
screen.tracer(0)
canvas = screen.getcanvas()


def paint(event):
    col = event.x // 20
    row = event.y // 20

    grid[row,col] = 1.0
    pen.goto(col,row)
    pen.dot(20,"white")

   

canvas.bind('<B1-Motion>',paint)
screen.mainloop()
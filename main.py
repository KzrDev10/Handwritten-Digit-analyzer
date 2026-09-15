from turtle import Turtle
from tkinter import Canvas
from turtle import *
import numpy as np
import tensorflow as tf

#Loading model
model = tf.keras.models.load_model('digit_classifier.keras')

#setup the grid so our model can use
grid = np.zeros((28,28))

#screen setup
screen = Screen()
screen.bgcolor("black")
screen.setworldcoordinates(0,28,28,0)
screen.setup(width=560,height=560)
screen.tracer(0)
canvas = screen.getcanvas()

#turtle setup
pen = Turtle()

text = Turtle()
text.hideturtle()
text.penup()
text.goto(x=10,y=2)
text.color("white")
text.write("Draw a digit. Enter: Predict. C: Clear")


#functions

def paint(event):
    col = event.x // 20
    row = event.y // 20

    grid[row,col] = 1.0
    pen.goto(col,row)
    pen.dot(20,"white")

def clear_canvas():
    pen.clear()
    grid.fill(0)

def predict_num():
    model_input = grid.reshape(1,28,28)
    raw_predict = model.predict(model_input)
    final_prediction = np.argmax(raw_predict)

    print(f"The model predicts {final_prediction}")

canvas.bind('<B1-Motion>',paint)

screen.onkey(clear_canvas,"c")
screen.onkey(predict_num, "Return")
screen.listen()
screen.mainloop()
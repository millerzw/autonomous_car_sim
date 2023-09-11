from tkinter import *
class Car():
    
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width=width
        self.height=height
        
    
    def draw(self, canvas):
        canvas.create_rectangle(20,20,40,40, fill='white', tag='car')
        
    
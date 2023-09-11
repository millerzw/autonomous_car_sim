from tkinter import *
class Car():
    
    
    def __init__(self, x, y, width, height, canvas):
        self.x = x
        self.y = y
        self.width=width
        self.height=height
        self.canvas=canvas
        
        self.controller = Controller()
        
    
    def draw(self):
        self.canvas.delete('car')
        self.canvas.create_rectangle(self.x-self.width/2,self.y-self.height/2,self.x+self.width/2,self.y+self.height/2, 
                                fill='white', 
                                tag='car')
        
    def update(self):
        #self.canvas.delete('car')
        self.draw()
        if (self.controller.forward):
            self.y-=2
            
        window.after(2,self.update)
        
    
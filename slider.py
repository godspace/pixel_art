#test mode
if __name__ == "__main__":
    print(__name__)
else:
    print(__name__)

from turtle import *

sc = Screen()
sc.tracer(0)
sc.colormode(255)

box_size = 22
scale = 3

class Slider(Turtle):
    def __init__(self, x, y, clor):
        super().__init__()
        self.x = x
        self.y = y
        self.pencolor(clor)
        self.penup()
        self.speed(0)
        self.shade = 0
        self.setpos(x, y)
        self.shape("circle")
        self.ondrag(self.slide)
    def slide(self, x, y):
        if x >= self.x and x <= self.x + 255/2:
            self.setx(x)
            self.shade = int(x-self.x)*2
            color_box.color(R.shade, G.shade, B.shade)
            color_box.pencolor("black")
            sc.update()

color_box = Turtle()
color_box.penup()
color_box.speed(0)
color_box.setpos(-sc.window_width()/2 + box_size, sc.window_height()/2 - box_size)
color_box.shape("square")

R = Slider(-sc.window_width()/2 + box_size, sc.window_height()/2 - box_size*2, (255,0,0))
R.ondrag(R.slide)
G = Slider(-sc.window_width()/2 + box_size, sc.window_height()/2 - box_size*3, (0,255,0))
G.ondrag(G.slide)
B = Slider(-sc.window_width()/2 + box_size, sc.window_height()/2 - box_size*4, (0,0,255))
B.ondrag(B.slide)

#test mode
if __name__ == "__main__":
    sc.update()
    sc.mainloop()
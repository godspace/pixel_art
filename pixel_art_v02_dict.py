from slider import *

pixel_dict = {}

class Pixel(Turtle):
    def __init__(self, x, y, R, G, B):
        super().__init__()
        self.ht()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.shape("square")
        self.shapesize(scale)
        self.color(R, G, B)
        self.st()
        self.onclick(self.set_color, 1)
        self.onclick(self.remove, 3)
    
    def set_color(self,x,y):
        x = round(x/22/scale)*22*scale
        y = round(y/22/scale)*22*scale
        self.color(R.shade, G.shade, B.shade)
        pixel_dict[(x,y)] = (R.shade, G.shade, B.shade)
        save_pic()
        sc.update()
    
    def remove(self,x,y):
        x = round(x/22/scale)*22*scale
        y = round(y/22/scale)*22*scale
        self.ht()
        del pixel_dict[(x,y)]
        save_pic()
        sc.update()

def spawn(x, y):
    if x > -sc.window_width()/2 + 22*3 and y < sc.window_height()/2 - 22*5:
        x = round(x/22/scale)*22*scale
        y = round(y/22/scale)*22*scale
        if (x,y) not in pixel_dict:
            pixel = Pixel(x, y, R.shade, G.shade, B.shade)
            pixel_dict[(x,y)] = (R.shade, G.shade, B.shade)
            pixel.st()
            save_pic()
            sc.update()
        
def save_pic():
    with open("pixel.txt","w") as file:
        for cor in pixel_dict:
            file.write(str(cor[0]) + " " + str(cor[1]) + " " + " ".join(tuple(map(str, pixel_dict[cor]))) + "\n")

def open_pic():
    with open("pixel.txt","r") as file:
        for line in file:
            pixel_info = line.split()
            pixel_dict[tuple(map(int, pixel_info[:2]))] = tuple(map(int, pixel_info[2:]))
    for cor in pixel_dict:
        Pixel(cor[0], cor[1], pixel_dict[cor][0], pixel_dict[cor][1], pixel_dict[(cor)][2])

try:
    open_pic()
except:
    print("No file")

sc.onclick(spawn, 1)
sc.update()
sc.mainloop()
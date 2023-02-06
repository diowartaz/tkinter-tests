import random as rd
import math
import tkinter

#valeurs modifiables
dim_pixel = 1000
pourcentage_angle = 0.1
delai_iteration = 1
L = []


class Moving_element():
    def __init__(self, x, y, r, d, angle, color):
        self.x = x
        self.y = y
        self.r = r
        self.d = d
        self.angle = angle
        self.color = color

    def move(self):
        random_angle = pourcentage_angle*2*math.pi*(rd.random()-0.5)
        self.angle = self.angle + random_angle
        self.x = self.x + self.d*math.cos(self.angle)
        self.y = self.y + self.d*math.sin(self.angle)
        self.x = self.x%dim_pixel
        self.y = self.y%dim_pixel


    def toString(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def draw(self, canv):
        return canv.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill = self.color, outline="")

class Worm(Moving_element):
    def __init__(self, x, y, r, d, angle, color, max_length):
        super().__init__(x, y, r, d, angle, color)
        self.max_length = max_length
        self.current_length = 0
        self.L = []
    
    def move(self):
        super().move()

    def draw(self, canv, wind):
        elem = super().draw(canv)
        self.L.append(elem)
        self.current_length = self.current_length + 1
        if(self.current_length > self.max_length):
            elem = self.L.pop(0)
            canv.delete(wind, elem)

def iteration():
    for worm in worm_list:
        worm.move()
        worm.draw(canvas, window)

    window.after(delai_iteration, iteration)


color_list = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
worm_list = []

#valeurs modifiables
for i in range(50):
    x = rd.randint(1,dim_pixel)
    y = rd.randint(1,dim_pixel)
    r = (rd.random()*0.5 + 1.5)*5
    d = (rd.random()+1)
    angle = rd.random()*2*math.pi
    color = rd.choice(color_list)
    max_length = 50
    worm_list.append(Worm(x, y, r, d, angle, color, max_length))


window = tkinter.Tk()
window.geometry(str(dim_pixel) + "x" + str(dim_pixel))
canvas = tkinter.Canvas(window, width=dim_pixel, height=dim_pixel)


canvas.pack()
window.after(0, iteration)
window.mainloop()
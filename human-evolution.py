from tkinter import *
import random as rd


def oval(x, y, mass, color="green"):
    return canvas.create_oval(x-mass**0.33, y-mass**0.33, x+mass**0.33, y+mass**0.33, fill=color)


class Food:
    def __init__(self):
        self.x = rd.randint(0, 1000)
        self.y = rd.randint(0, 1000)
        self.mass = 300
        self.radius = 3
        self.available = True
        self.canvasElement = None

    def draw(self):
        if self.available:
            self.canvasElement = oval(self.x, self.y, self.mass, "green")

    def undraw(self):
        if (self.canvasElement != None):
            canvas.delete(self.canvasElement)


class Human:
    def __init__(self, x, y, mass, vision_radius):
        self.x = x
        self.y = y
        self.mass = mass
        self.vision_radius = vision_radius
        self.food = None
        self.canvasElement = None
        self.canvasElement2 = None
        self.color = "magenta"
        self.default_x_direction = 1
        self.default_y_direction = 1

    def draw(self):
        self.canvasElement = oval(self.x, self.y, self.mass, self.color)
        self.canvasElement2 = canvas.create_oval(self.x-self.vision_radius, self.y-self.vision_radius,
                                                 self.x+self.vision_radius, self.y+self.vision_radius)

    def undraw(self):
        if (self.canvasElement != None):
            canvas.delete(self.canvasElement)
        if (self.canvasElement2 != None):
            canvas.delete(self.canvasElement2)

    def locate_food(self):
        if self.food != None and self.food.available:
            self.color = "yellow"
            return

        for food in foods:
            if (self.x-food.x)**2 + (self.y-food.y)**2 <= self.vision_radius**2:
                self.color = "yellow"
                self.food = food
                return

        self.color = "magenta"
        self.food = None

    def move(self):
        if self.food != None and self.food.available and (self.x-self.food.x)**2 + (self.y-self.food.y)**2 <= self.vision_radius**2:
            # print(self.food.available)
            # print((self.x-self.food.x)**2 + (self.y-self.food.y)**2)
            if self.food.x > self.x:
                self.x = self.x + 1
            else:
                if self.food.x < self.x:
                    self.x = self.x - 1

            if self.food.y > self.y:
                self.y = self.y + 1
            else:
                if self.food.y < self.y:
                    self.y = self.y - 1

            if self.food.y == self.y and self.food.x == self.x:
                self.mass += self.food.mass
                self.food.available = False
                self.food = None

        else:
            self.food = None
            self.color = "magenta"
            if self.x == 0:
                self.default_x_direction = 1
            elif self.x == 1000:
                self.default_x_direction = -1

            if self.y == 0:
                self.default_y_direction = 1
            elif self.y == 1000:
                self.default_y_direction = -1

            self.x = self.x + self.default_x_direction
            self.y = self.y + self.default_y_direction

        self.mass -= 1


def setup():
    nb_humans_init = 10
    mass_init = 1000
    vision_init = 100

    nb_foods = 20
    for i in range(nb_humans_init):
        humans.append(Human(rd.randint(0, 1000), rd.randint(
            0, 1000), mass_init, vision_init))

    for i in range(nb_foods):
        foods.append(Food())

    canvas.after(1, iteration)


def iteration():
    for food in foods:
        food.undraw()
        food.draw()

    for human in humans:
        human.undraw()
        if human.mass > 0:
            human.locate_food()
            human.move()
            human.draw()

    clean_foods()
    canvas.after(20, iteration)


def clean_foods():
    for food in foods:
        if not (food.available):
            food.x = rd.randint(0, 1000)
            food.y = rd.randint(0, 1000)
            food.available = True


fenetre = Tk()

canvas = Canvas(fenetre, width=1000, height=1000)
canvas.pack()

humans = []
foods = []
setup()


fenetre.mainloop()

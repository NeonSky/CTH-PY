import pygame as pg
import random as r

class Func:
    def __init__(self, func_string):
        print("hej!")

    def calc(self, x):
        return x * 2


#user_func = raw_input("Function: ");

background_colour = (255,255,255)
plot_color = (255, 0, 0)
plot_width = 4.0
(width, height) = (640, 480)

screen = pg.display.set_mode((width, height))
pg.display.set_caption('Plot 2D')
screen.fill(background_colour)

x_max = 10.0
y_max = 10.0

ppu_x = width / x_max
ppu_y = height / y_max

resolution = width
points = []

def to_pixles((x,y)):
    return (ppu_x*x,ppu_y*y)

def to_pixel_list(points):
    converted_points = []
    for i in range(0, len(points)):
        converted_points.append(to_pixles(points[i]))
    return converted_points

def to_units((x,y)):
    return (x/ppu_x,y/ppu_y)


def rev((x,y)):
   return (x,height-y)

def rev_list(points):
    converted_points = []
    for i in range(0, len(points)):
        converted_points.append(rev(points[i]))
    return converted_points

def draw_lines(points):
    pg.draw.lines(screen, plot_color, False, rev_list(to_pixel_list(points)), plot_width)

def draw_line((x1,y1),(x2,y2)):
    pg.draw.line(screen, plot_color, rev(to_pixles((x1,y1))), rev(to_pixles((x2,y2))), plot_width)

#NOT DONE
for i in range(0, resolution):
    points.append((to_units(1.0 * i * (1.0 * width / 1.0 * resolution)), r.randint(0.0, 10.0)))

pg.display.flip()

running = True
while running:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False
from argparse import _AppendAction

import pygame as pg
import random as r

class Func:
    polynoms = {}

    def __init__(self, func_string):
        polynom_strings = []
        char_index = 0
        polynom_string = ""

        while True:
            if char_index == len(func_string):
                polynom_strings.append(polynom_string)
                polynom_string = ""
                break

            char = func_string[char_index]
            if polynom_string == "" or char != "+" and char != "-":
                polynom_string += char
                char_index += 1
            else:
                polynom_strings.append(polynom_string)
                polynom_string = ""
                continue


        print(polynom_strings)
        print("############")

        for polynom in polynom_strings:
            j = 0
            multiplier = 1

            if polynom[j] == "+" or polynom[j] == "-":
                j += 1

            if polynom[j].isdigit():
                multiplier = self.get_number_at(polynom, j)
                while j < len(polynom):
                    if not polynom[j].isdigit():
                        break
                    j += 1
                j += 1

            if j >= len(polynom):
                if 0 in self.polynoms.keys():
                    self.polynoms[0] += multiplier
                else:
                    self.polynoms[0] = multiplier
                continue

            if polynom[j] == "*":
                j += 1

            print(polynom + ", " + str(multiplier) + ", " + str(j))

            # Polynom
            j += 2
            power = self.get_number_at(polynom, j)

            if power in self.polynoms.keys():
                self.polynoms[power] += multiplier
            else:
                self.polynoms[power] = multiplier

        print(self.polynoms)

    def get_number_at(self, s, i):
        numb_str = "0"
        counter = 0
        while s[i + counter].isdigit():
            numb_str += s[i + counter]
            counter += 1
            if i + counter >= len(s):
                break

        numb = int(numb_str)
        if s[0] == "-":
            numb *= -1

        return numb

    def calc(self, x):
        output = 0
        for power, constant in self.polynoms.iteritems():
            print(str(power) + " " + str(constant))
            output += constant * pow(x, power)
        return output

#user_func = raw_input("Function: ");

func = Func("2*x^2-1*x^3")
print(func.calc(2))

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
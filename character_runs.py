import math

from pico2d import *

open_canvas()

grass = load_image("grass.png")
character = load_image('character.png')


def render_all(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)

def run_circle():
    cx, cy, r = 800 / 2, 600 / 2, 200
    for deg in range(270, 360 + 270, 5):
        x = cx + r * math.cos(deg / 360 * 2 * math.pi)
        y = cy + r * math.sin(deg / 360 * 2 * math.pi)
        render_all(x, y)

        
def run_rectangle():
    # bottom line
    for x in range(400, 750+1, 5):
        render_all(x, 90)

    # right line
    for y in range(90,550+1,5):
        render_all(750,y)

    # top line
    for x in range(750, 50-1, -5):
        render_all(x, 550)

    # left_line
    for y in range(550,90-1,-5):
        render_all(50,y)

    # bottom line
    for x in range(50, 400+1, 5):
        render_all(x, 90)
    


while True:
    run_circle()
    run_rectangle()

close_canvas()

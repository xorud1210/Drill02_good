from pico2d import *

open_canvas()

grass = load_image("grass.png")
character = load_image('character.png')


def run_circle():
    print('CIRLCE')
    pass
def run_rectangle():
    print('RECTANGLE')
    pass


while True:
    run_circle()
    run_rectangle()
    break

close_canvas()

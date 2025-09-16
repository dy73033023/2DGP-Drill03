from pico2d import *

open_canvas()

boy = load_image("character.png")

def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.1)

def move_top():
    print("move_top")
    for x in range(0,800,5):
        draw_boy(x,550)
    pass

def move_right():
    print("move_right")
    pass

def move_bottom():
    print("move_bottom")
    pass

def move_left():
    print("move_left")
    pass

def move_rectangle():
    print("move_rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass

def move_circle():
    print("move_circle")
    r = 200

    for deg in range(0, 360, 5):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        draw_boy(x, y)
    pass

while True:
    # move_circle()
    move_rectangle()
    break
    pass #패스

close_canvas()

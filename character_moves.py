from pico2d import *

open_canvas()

boy = load_image("character.png")

def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.1)

def move_top():
    print("move_top")
    for x in range(770,30,-20):
        draw_boy(x,550)
    pass

def move_right():
    print("move_right")
    for y in range(50,550,20):
        draw_boy(770,y)
    pass

def move_bottom():
    print("move_bottom")
    for x in range(30,770,20):
        draw_boy(x,50)
    pass

def move_left():
    print("move_left")
    for y in range(550,50,-20):
        draw_boy(30,y)
    pass

def move_bottom_to_top(): #삼각형 우측하단에서 중앙상단
    pass


def move_top_to_bottom(): #삼각형 중앙상단에서 좌측하단
    pass

def move_rectangle():
    print("move_rectangle")
    move_bottom()
    move_right()
    move_top()
    move_left()
    pass

def move_triangle():
    print("move_triangle")
    move_bottom()
    move_bottom_to_top()
    move_top_to_bottom()
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
    # move_rectangle()
    move_triangle()
    # move_circle()

    break
    pass #패스

close_canvas()

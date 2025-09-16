from pico2d import *
import math

open_canvas(800, 600)

boy = load_image("character.png")

def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.1)

def move_circle():
    print("원 운동 시작")
    radius = 250  # 화면 여백을 위해 반지름 축소
    center_x, center_y = 400, 300  # 화면 중앙
    for deg in range(0, 360, 5):
        x = radius * math.cos(math.radians(deg)) + center_x
        y = radius * math.sin(math.radians(deg)) + center_y
        draw_boy(x, y)

def move_rectangle():
    print("사각 운동 시작")
    points = [
        (30, 570),     # 좌상단 (여백 추가)
        (770, 570),    # 우상단 (여백 추가)
        (770, 30),     # 우하단 (여백 추가)
        (30, 30)       # 좌하단 (여백 추가)
    ]
    for i in range(len(points)):
        current = points[i]
        next = points[(i + 1) % len(points)]
        for t in range(40):
            x = (next[0] - current[0]) * (t / 40) + current[0]
            y = (next[1] - current[1]) * (t / 40) + current[1]
            draw_boy(x, y)

def move_triangle():
    print("삼각 운동 시작")
    points = [
        (400, 570),    # 상단 중앙 (여백 추가)
        (770, 30),     # 우하단 (여백 추가)
        (30, 30)       # 좌하단 (여백 추가)
    ]
    for i in range(len(points)):
        current = points[i]
        next = points[(i + 1) % len(points)]
        for t in range(40):
            x = (next[0] - current[0]) * (t / 40) + current[0]
            y = (next[1] - current[1]) * (t / 40) + current[1]
            draw_boy(x, y)

while True:
    move_rectangle()
    move_triangle()
    move_circle()

close_canvas()

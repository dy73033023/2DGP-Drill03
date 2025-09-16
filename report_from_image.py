from pico2d import *
import math

open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')

def render_world():
    grass.draw_now(400, 30)

def draw_character(x, y):
    character.draw_now(x, y)

def run_circle():
    print("원 운동 시작")
    cx, cy = 400, 300  # 원의 중심점
    r = 200  # 반지름
    angular_speed = 5  # 각도 변화량

    for deg in range(0, 360, angular_speed):
        clear_canvas_now()
        render_world()

        rad = math.radians(deg)
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        draw_character(x, y)

        delay(0.01)

def run_rectangle():
    print("사각형 운동 시작")
    points = [
        (100, 500),   # 좌상단
        (700, 500),   # 우상단
        (700, 100),   # 우하단
        (100, 100)    # 좌하단
    ]

    for i in range(4):
        start = points[i]
        end = points[(i + 1) % 4]

        for t in range(0, 50):
            clear_canvas_now()
            render_world()

            x = (end[0] - start[0]) * (t / 50) + start[0]
            y = (end[1] - start[1]) * (t / 50) + start[1]
            draw_character(x, y)

            delay(0.01)

def main_loop():
    while True:
        run_circle()      # 원 운동 실행
        run_rectangle()   # 사각형 운동 실행

main_loop()

close_canvas()

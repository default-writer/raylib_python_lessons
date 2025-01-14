from raylib_turtle import DrawTurtle
from raylib import *

hello_raylib_str = "Hello,world!".encode()

InitWindow(800, 450, hello_raylib_str)

def DrawRainbowCircle(animation_1):
    # Draw sun body
    DrawCircle(400, 200, 50, YELLOW)
    # Draw sun rays
    colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
    num_colors = len(colors)
    for i, color in enumerate(colors):
        start_angle = (i * (360 / num_colors)) + (animation_1 * 360)
        end_angle = start_angle + (360 / num_colors)
        DrawCircleSector((400, 200), 70, start_angle, end_angle, 0, color)

animation_1 = 0.0

while not WindowShouldClose():
    duration = 1.0
    animation_1 += GetFrameTime() * (1.0 / duration)
    if animation_1 > 1.0:
        animation_1 -= 1.0

    BeginDrawing()
    ClearBackground(WHITE)
    DrawText(hello_raylib_str, 190, 200, 20, BLACK)
    DrawRainbowCircle(animation_1)
    DrawTurtle(500 + int(animation_1 * 100), 250, line_width=2)  # Example animation
    EndDrawing()

CloseWindow()


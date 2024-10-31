"""
File: 
Name:
-------------------------
TODO:
"""
"""
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 5
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
# 設定一個布林值來追蹤球的運動狀態
is_moving = False
window = GWindow(800, 500, title='bouncing_ball.py')
count = 0

def main():
    global hole
    hole = set_up_circle()
    window.add(hole, START_X, START_Y)
    onmouseclicked(start_bounce)


def start_bounce(event):
    global is_moving,count
    # 如果球已經在移動中，忽略後續的點擊事件
    if not is_moving:
        is_moving = True
        count+=1
        if count <= 3: #小於三次才能被執行
            bounce()
        else:
            is_moving = True


def bounce():
    VY = 0
    print(VY)
    while True:
        global is_moving
        hole.move(VX,VY)
        if hole.y + SIZE//2 >= window.height:
            VY = -VY*REDUCE # 反彈
        else: # 下墜
            VY+=GRAVITY
        pause(DELAY)  # 降速毫秒
        # 當球離開視窗的右邊緣後，停止運動並重置狀態
        if hole.x > window.width:
            is_moving = False
            hole.x = START_X
            hole.y = START_Y
            break


def set_up_circle():
    hole = GOval(SIZE, SIZE)
    hole.filled = True
    return hole


if __name__ == "__main__":
    main()

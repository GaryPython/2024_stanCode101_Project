"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousemoved,onmouseclicked


SIZE = 15
count = 0
holes = []  # 用於存儲洞的位置和物件
hole = GOval(SIZE,SIZE)
window = GWindow()

def main():
	global count,x1,y1,x2,y2
	onmousemoved(chqnge_position)
	onmouseclicked(create_hole)
	hole.filled = False
	window.add(hole)

def chqnge_position(event):
	hole.x = event.x - SIZE//2
	hole.y = event.y - SIZE // 2


def create_hole(event):
	global count, holes, line
	if count < 2:
		# 創建並添加新的洞
		hole = GOval(SIZE, SIZE)
		hole.filled = False
		hole.x = event.x - SIZE // 2
		hole.y = event.y - SIZE // 2
		window.add(hole)

		# 記錄洞的 GOval 物件
		holes.append(hole)
		count += 1

		# 當有兩個洞時，創建連線
		if count == 2:
			x1, y1 = holes[0].x + SIZE // 2, holes[0].y + SIZE // 2
			x2, y2 = holes[1].x + SIZE // 2, holes[1].y + SIZE // 2
			# 計算連線的坐標
			line = GLine(x1, y1, x2, y2)
			window.add(line)
			# 清除所有物件
			window.remove(holes[0])
			window.remove(holes[1])
			# 重置
			holes = []  # 清空洞列表
			count = 0  # 重置計數器



if __name__ == "__main__":
    main()

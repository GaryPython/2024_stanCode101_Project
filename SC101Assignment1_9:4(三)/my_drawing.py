"""
Title: 小火龍
Name:賴巖鑫
之前一個人離開家來台北工作，妹妹送我一個拼豆的吊飾，因此給我靈感想做一個“點陣圖”回送給我妹妹。
那為什麼是小火龍，因為我最喜歡的遊戲是寶可夢
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect,GLabel
from campy.graphics.gwindow import GWindow
size = 20
def main():
    window = GWindow(width=1200, height=800, title='Pokémon')

    #肚子
    list =[(430, 470), (440, 470), (450, 470), (460, 470), (440, 480), (450, 480), (460, 480), (470, 480), (460, 490),
     (470, 490), (470, 500), (690, 500), (470, 510), (480, 510), (680, 510), (690, 510), (470, 520), (480, 520),
     (680, 520), (460, 530), (470, 530), (480, 530), (670, 530), (680, 530), (460, 540), (470, 540), (480, 540),
     (490, 540), (500, 540), (510, 540), (520, 540), (530, 540), (650, 540), (660, 540), (670, 540), (460, 550),
     (470, 550), (480, 550), (490, 550), (500, 550), (510, 550), (520, 550), (530, 550), (540, 550), (640, 550),
     (650, 550), (660, 550), (460, 560), (470, 560), (520, 560), (530, 560), (540, 560), (550, 560), (590, 560),
     (600, 560), (610, 560), (620, 560), (630, 560), (640, 560), (520, 570), (530, 570), (540, 570), (550, 570),
     (560, 570), (570, 570), (580, 570), (590, 570), (600, 570), (610, 570), (620, 570), (630, 570), (520, 580),
     (530, 580), (540, 580), (550, 580), (560, 580), (570, 580), (580, 580), (590, 580), (600, 580), (610, 580),
     (620, 580), (520, 590), (530, 590), (540, 590), (550, 590), (560, 590), (570, 590), (580, 590), (590, 590),
     (600, 590), (520, 600), (530, 600), (540, 600), (550, 600), (560, 600), (520, 610), (530, 610), (540, 610)]
    for x, y in list:
        print(x, y)
        boby = GRect(30, 30, x=x, y=y)
        boby.filled = True
        boby.fill_color = "Cornsilk"
        boby.color = "Cornsilk"  # 設置邊框顏色
        window.add(boby)
    #身體
    list = [(370, 110), (380, 110), (390, 110), (400, 110), (410, 110), (420, 110), (430, 110), (440, 110), (450, 110), (460, 110), (350, 120), (360, 120), (370, 120), (380, 120), (390, 120), (400, 120), (410, 120), (420, 120), (430, 120), (440, 120), (450, 120), (460, 120), (470, 120), (480, 120), (320, 130), (330, 130), (340, 130), (350, 130), (360, 130), (370, 130), (380, 130), (390, 130), (400, 130), (410, 130), (420, 130), (430, 130), (440, 130), (450, 130), (460, 130), (470, 130), (480, 130), (490, 130), (320, 140), (330, 140), (340, 140), (350, 140), (360, 140), (410, 140), (420, 140), (430, 140), (440, 140), (450, 140), (460, 140), (470, 140), (480, 140), (490, 140), (500, 140), (320, 150), (330, 150), (340, 150), (350, 150), (400, 150), (410, 150), (420, 150), (430, 150), (440, 150), (450, 150), (460, 150), (470, 150), (480, 150), (490, 150), (500, 150), (510, 150), (320, 160), (330, 160), (340, 160), (350, 160), (400, 160), (410, 160), (420, 160), (430, 160), (440, 160), (450, 160), (460, 160), (470, 160), (480, 160), (490, 160), (500, 160), (510, 160), (520, 160), (310, 170), (320, 170), (330, 170), (340, 170), (350, 170), (400, 170), (410, 170), (420, 170), (430, 170), (440, 170), (450, 170), (460, 170), (470, 170), (480, 170), (490, 170), (500, 170), (510, 170), (520, 170), (530, 170), (310, 180), (320, 180), (330, 180), (340, 180), (350, 180), (360, 180), (370, 180), (380, 180), (390, 180), (400, 180), (410, 180), (420, 180), (430, 180), (440, 180), (450, 180), (460, 180), (470, 180), (480, 180), (490, 180), (500, 180), (510, 180), (520, 180), (530, 180), (540, 180), (300, 190), (310, 190), (320, 190), (330, 190), (340, 190), (350, 190), (360, 190), (370, 190), (380, 190), (390, 190), (400, 190), (410, 190), (420, 190), (430, 190), (440, 190), (450, 190), (460, 190), (470, 190), (480, 190), (490, 190), (500, 190), (510, 190), (520, 190), (530, 190), (540, 190), (300, 200), (310, 200), (320, 200), (330, 200), (340, 200), (350, 200), (360, 200), (370, 200), (380, 200), (390, 200), (400, 200), (410, 200), (420, 200), (430, 200), (440, 200), (450, 200), (460, 200), (470, 200), (480, 200), (490, 200), (500, 200), (510, 200), (520, 200), (530, 200), (540, 200), (290, 210), (300, 210), (310, 210), (320, 210), (330, 210), (340, 210), (350, 210), (360, 210), (370, 210), (380, 210), (390, 210), (400, 210), (410, 210), (420, 210), (430, 210), (440, 210), (450, 210), (460, 210), (470, 210), (480, 210), (490, 210), (500, 210), (510, 210), (520, 210), (530, 210), (540, 210), (550, 210), (290, 220), (300, 220), (310, 220), (320, 220), (330, 220), (340, 220), (350, 220), (360, 220), (370, 220), (380, 220), (390, 220), (400, 220), (410, 220), (420, 220), (430, 220), (440, 220), (450, 220), (460, 220), (470, 220), (480, 220), (490, 220), (500, 220), (510, 220), (520, 220), (530, 220), (540, 220), (550, 220), (290, 230), (300, 230), (310, 230), (320, 230), (330, 230), (340, 230), (350, 230), (360, 230), (370, 230), (380, 230), (390, 230), (400, 230), (410, 230), (420, 230), (430, 230), (440, 230), (450, 230), (460, 230), (470, 230), (480, 230), (490, 230), (500, 230), (510, 230), (520, 230), (530, 230), (540, 230), (550, 230), (290, 240), (300, 240), (310, 240), (320, 240), (330, 240), (340, 240), (350, 240), (360, 240), (370, 240), (380, 240), (390, 240), (400, 240), (410, 240), (420, 240), (430, 240), (440, 240), (450, 240), (460, 240), (470, 240), (480, 240), (490, 240), (500, 240), (510, 240), (520, 240), (530, 240), (540, 240), (550, 240), (290, 250), (300, 250), (310, 250), (320, 250), (330, 250), (340, 250), (350, 250), (360, 250), (370, 250), (380, 250), (390, 250), (400, 250), (410, 250), (420, 250), (430, 250), (440, 250), (450, 250), (460, 250), (470, 250), (480, 250), (490, 250), (520, 250), (530, 250), (540, 250), (550, 250), (290, 260), (300, 260), (310, 260), (320, 260), (330, 260), (340, 260), (350, 260), (360, 260), (370, 260), (380, 260), (390, 260), (400, 260), (410, 260), (440, 260), (450, 260), (460, 260), (470, 260), (480, 260), (490, 260), (520, 260), (530, 260), (540, 260), (550, 260), (290, 270), (300, 270), (310, 270), (320, 270), (330, 270), (340, 270), (350, 270), (360, 270), (370, 270), (380, 270), (390, 270), (400, 270), (410, 270), (420, 270), (440, 270), (450, 270), (460, 270), (470, 270), (480, 270), (490, 270), (500, 270), (510, 270), (520, 270), (530, 270), (540, 270), (550, 270), (560, 270), (290, 280), (300, 280), (310, 280), (320, 280), (330, 280), (340, 280), (350, 280), (360, 280), (370, 280), (380, 280), (390, 280), (400, 280), (410, 280), (420, 280), (450, 280), (460, 280), (470, 280), (480, 280), (490, 280), (500, 280), (510, 280), (520, 280), (530, 280), (540, 280), (550, 280), (560, 280), (290, 290), (300, 290), (310, 290), (320, 290), (330, 290), (340, 290), (350, 290), (360, 290), (370, 290), (380, 290), (390, 290), (400, 290), (410, 290), (420, 290), (430, 290), (460, 290), (470, 290), (480, 290), (490, 290), (500, 290), (510, 290), (550, 290), (560, 290), (290, 300), (300, 300), (310, 300), (320, 300), (330, 300), (340, 300), (350, 300), (360, 300), (370, 300), (380, 300), (390, 300), (400, 300), (410, 300), (420, 300), (430, 300), (440, 300), (450, 300), (460, 300), (470, 300), (480, 300), (490, 300), (500, 300), (540, 300), (550, 300), (560, 300), (290, 310), (300, 310), (310, 310), (320, 310), (330, 310), (340, 310), (350, 310), (360, 310), (370, 310), (420, 310), (430, 310), (440, 310), (450, 310), (460, 310), (470, 310), (480, 310), (490, 310), (500, 310), (530, 310), (540, 310), (550, 310), (560, 310), (290, 320), (300, 320), (310, 320), (320, 320), (330, 320), (340, 320), (350, 320), (360, 320), (370, 320), (380, 320), (390, 320), (440, 320), (450, 320), (460, 320), (470, 320), (480, 320), (490, 320), (500, 320), (510, 320), (520, 320), (530, 320), (540, 320), (550, 320), (560, 320), (290, 330), (300, 330), (310, 330), (320, 330), (330, 330), (340, 330), (350, 330), (360, 330), (370, 330), (380, 330), (390, 330), (400, 330), (410, 330), (420, 330), (430, 330), (440, 330), (450, 330), (460, 330), (470, 330), (480, 330), (490, 330), (500, 330), (510, 330), (520, 330), (530, 330), (540, 330), (550, 330), (290, 340), (300, 340), (310, 340), (320, 340), (330, 340), (340, 340), (350, 340), (360, 340), (370, 340), (380, 340), (390, 340), (400, 340), (410, 340), (420, 340), (430, 340), (440, 340), (450, 340), (460, 340), (470, 340), (480, 340), (490, 340), (500, 340), (510, 340), (520, 340), (530, 340), (540, 340), (550, 340), (290, 350), (300, 350), (310, 350), (320, 350), (330, 350), (340, 350), (350, 350), (360, 350), (370, 350), (380, 350), (390, 350), (400, 350), (410, 350), (420, 350), (430, 350), (440, 350), (450, 350), (460, 350), (470, 350), (480, 350), (490, 350), (500, 350), (510, 350), (520, 350), (530, 350), (290, 360), (300, 360), (310, 360), (320, 360), (330, 360), (340, 360), (350, 360), (360, 360), (370, 360), (380, 360), (390, 360), (400, 360), (410, 360), (420, 360), (430, 360), (440, 360), (450, 360), (460, 360), (470, 360), (480, 360), (490, 360), (500, 360), (510, 360), (520, 360), (290, 370), (300, 370), (310, 370), (320, 370), (330, 370), (340, 370), (360, 370), (370, 370), (380, 370), (390, 370), (400, 370), (410, 370), (420, 370), (430, 370), (440, 370), (450, 370), (460, 370), (470, 370), (480, 370), (290, 380), (300, 380), (310, 380), (320, 380), (330, 380), (340, 380), (290, 390), (300, 390), (310, 390), (320, 390), (330, 390), (340, 390), (290, 400), (300, 400), (310, 400), (320, 400), (330, 400), (340, 400), (350, 400), (290, 410), (300, 410), (310, 410), (320, 410), (330, 410), (340, 410), (350, 410), (360, 410), (290, 420), (300, 420), (310, 420), (320, 420), (330, 420), (340, 420), (350, 420), (360, 420), (370, 420), (380, 420), (390, 420), (400, 420), (410, 420), (420, 420), (430, 420), (490, 420), (500, 420), (290, 430), (300, 430), (310, 430), (320, 430), (330, 430), (340, 430), (350, 430), (360, 430), (370, 430), (380, 430), (390, 430), (400, 430), (410, 430), (420, 430), (430, 430), (440, 430), (450, 430), (460, 430), (490, 430), (500, 430), (510, 430), (520, 430), (290, 440), (300, 440), (310, 440), (320, 440), (330, 440), (340, 440), (350, 440), (360, 440), (370, 440), (380, 440), (420, 440), (430, 440), (490, 440), (500, 440), (510, 440), (520, 440), (530, 440), (290, 450), (300, 450), (310, 450), (320, 450), (330, 450), (340, 450), (350, 450), (360, 450), (370, 450), (380, 450), (390, 450), (420, 450), (490, 450), (500, 450), (510, 450), (520, 450), (580, 450), (720, 450), (290, 460), (300, 460), (310, 460), (320, 460), (330, 460), (340, 460), (350, 460), (360, 460), (370, 460), (380, 460), (390, 460), (400, 460), (420, 460), (490, 460), (500, 460), (510, 460), (570, 460), (580, 460), (590, 460), (650, 460), (720, 460), (280, 470), (290, 470), (300, 470), (310, 470), (320, 470), (330, 470), (340, 470), (350, 470), (360, 470), (370, 470), (380, 470), (390, 470), (400, 470), (410, 470), (490, 470), (500, 470), (550, 470), (560, 470), (570, 470), (580, 470), (590, 470), (600, 470), (610, 470), (650, 470), (720, 470), (280, 480), (290, 480), (300, 480), (310, 480), (320, 480), (330, 480), (340, 480), (350, 480), (360, 480), (370, 480), (380, 480), (390, 480), (400, 480), (410, 480), (420, 480), (490, 480), (500, 480), (540, 480), (550, 480), (560, 480), (570, 480), (580, 480), (590, 480), (600, 480), (610, 480), (620, 480), (630, 480), (640, 480), (650, 480), (710, 480), (720, 480), (280, 490), (290, 490), (300, 490), (310, 490), (320, 490), (330, 490), (340, 490), (350, 490), (360, 490), (370, 490), (380, 490), (390, 490), (400, 490), (410, 490), (420, 490), (430, 490), (490, 490), (540, 490), (550, 490), (560, 490), (570, 490), (580, 490), (590, 490), (600, 490), (610, 490), (620, 490), (630, 490), (640, 490), (650, 490), (700, 490), (710, 490), (720, 490), (280, 500), (290, 500), (300, 500), (310, 500), (320, 500), (330, 500), (340, 500), (350, 500), (380, 500), (390, 500), (400, 500), (410, 500), (420, 500), (430, 500), (440, 500), (560, 500), (570, 500), (580, 500), (590, 500), (600, 500), (610, 500), (620, 500), (630, 500), (640, 500), (710, 500), (280, 510), (290, 510), (300, 510), (310, 510), (320, 510), (330, 510), (340, 510), (350, 510), (360, 510), (560, 510), (570, 510), (580, 510), (590, 510), (600, 510), (610, 510), (620, 510), (630, 510), (700, 510), (710, 510), (280, 520), (290, 520), (300, 520), (310, 520), (320, 520), (330, 520), (340, 520), (350, 520), (360, 520), (570, 520), (580, 520), (590, 520), (600, 520), (610, 520), (620, 520), (700, 520), (710, 520), (280, 530), (290, 530), (300, 530), (310, 530), (320, 530), (330, 530), (340, 530), (350, 530), (360, 530), (370, 530), (700, 530), (710, 530), (280, 540), (290, 540), (300, 540), (310, 540), (320, 540), (330, 540), (340, 540), (350, 540), (360, 540), (370, 540), (380, 540), (680, 540), (690, 540), (700, 540), (280, 550), (290, 550), (300, 550), (310, 550), (320, 550), (330, 550), (340, 550), (670, 550), (680, 550), (690, 550), (700, 550), (290, 560), (300, 560), (310, 560), (320, 560), (330, 560), (340, 560), (350, 560), (360, 560), (370, 560), (380, 560), (650, 560), (660, 560), (670, 560), (680, 560), (690, 560), (700, 560), (290, 570), (300, 570), (310, 570), (320, 570), (330, 570), (340, 570), (350, 570), (360, 570), (370, 570), (380, 570), (390, 570), (400, 570), (640, 570), (650, 570), (660, 570), (670, 570), (680, 570), (690, 570), (290, 580), (300, 580), (310, 580), (320, 580), (330, 580), (340, 580), (350, 580), (360, 580), (370, 580), (380, 580), (390, 580), (400, 580), (410, 580), (490, 580), (630, 580), (640, 580), (650, 580), (660, 580), (670, 580), (680, 580), (300, 590), (310, 590), (320, 590), (330, 590), (340, 590), (350, 590), (360, 590), (370, 590), (380, 590), (390, 590), (400, 590), (410, 590), (420, 590), (480, 590), (490, 590), (610, 590), (620, 590), (630, 590), (640, 590), (650, 590), (660, 590), (670, 590), (310, 600), (320, 600), (330, 600), (340, 600), (350, 600), (360, 600), (370, 600), (380, 600), (390, 600), (400, 600), (410, 600), (420, 600), (430, 600), (440, 600), (450, 600), (460, 600), (470, 600), (480, 600), (490, 600), (580, 600), (590, 600), (600, 600), (610, 600), (620, 600), (630, 600), (640, 600), (650, 600), (660, 600), (310, 610), (320, 610), (330, 610), (340, 610), (350, 610), (360, 610), (370, 610), (380, 610), (390, 610), (400, 610), (410, 610), (420, 610), (430, 610), (440, 610), (450, 610), (460, 610), (470, 610), (480, 610), (550, 610), (560, 610), (570, 610), (580, 610), (590, 610), (600, 610), (610, 610), (620, 610), (630, 610), (640, 610), (320, 620), (330, 620), (340, 620), (350, 620), (360, 620), (370, 620), (380, 620), (390, 620), (400, 620), (410, 620), (420, 620), (430, 620), (440, 620), (450, 620), (460, 620), (470, 620), (520, 620), (530, 620), (540, 620), (550, 620), (560, 620), (570, 620), (580, 620), (590, 620), (600, 620), (610, 620), (620, 620), (330, 630), (340, 630), (350, 630), (360, 630), (370, 630), (380, 630), (390, 630), (400, 630), (410, 630), (420, 630), (430, 630), (440, 630), (450, 630), (460, 630), (470, 630), (520, 630), (530, 630), (540, 630), (550, 630), (560, 630), (570, 630), (580, 630), (590, 630), (600, 630), (610, 630), (340, 640), (350, 640), (360, 640), (370, 640), (380, 640), (390, 640), (400, 640), (410, 640), (420, 640), (430, 640), (440, 640), (450, 640), (460, 640), (520, 640), (530, 640), (540, 640), (550, 640), (560, 640), (570, 640), (580, 640), (590, 640), (600, 640), (610, 640), (340, 650), (350, 650), (360, 650), (370, 650), (380, 650), (390, 650), (400, 650), (410, 650), (420, 650), (430, 650), (440, 650), (450, 650), (520, 650), (530, 650), (540, 650), (550, 650), (560, 650), (570, 650), (580, 650), (590, 650), (380, 660), (390, 660), (400, 660), (410, 660), (520, 660), (530, 660), (540, 660), (550, 660), (560, 660), (570, 660), (580, 660), (500, 670), (510, 670), (520, 670), (530, 670), (540, 670), (550, 670), (470, 680), (480, 680), (490, 680), (500, 680), (510, 680), (520, 680)]

    for x, y in list:
        #print(x, y)
        boby = GRect(20, 20, x=x, y=y)
        boby.filled = True
        boby.fill_color = "coral"  # 設置填充顏色
        boby.color = "coral"  # 設置邊框顏色
        window.add(boby)


    # 尾巴火焰
    list = [(720, 390), (730, 390), (720, 400), (730, 400), (720, 410), (730, 410), (740, 410), (720, 420), (730, 420), (740, 420), (710, 430), (720, 430), (740, 430), (710, 440), (740, 440), (740, 450)]
    for x, y in list:
        print(x, y)
        boby = GRect(20, 20, x=x, y=y)
        boby.filled = True
        boby.fill_color = "Yellow"
        boby.color = "Yellow"  # 設置邊框顏色
        window.add(boby)

    # 尾巴火焰
    list = [(730, 350), (720, 360), (730, 360), (740, 360), (710, 370), (720, 370), (730, 370), (740, 370), (750, 370), (760, 370), (710, 380), (720, 380), (730, 380), (740, 380), (750, 380), (760, 380), (710, 390), (740, 390), (750, 390), (760, 390), (710, 400), (750, 400), (760, 400), (770, 400), (710, 410), (760, 410), (770, 410), (700, 420), (710, 420), (760, 420), (770, 420), (680, 430), (690, 430), (700, 430), (760, 430), (770, 430), (680, 440), (690, 440), (700, 440), (760, 440), (770, 440), (680, 450), (690, 450), (700, 450), (760, 450), (770, 450), (670, 460), (680, 460), (690, 460), (750, 460), (760, 460), (670, 470), (680, 470), (740, 470), (750, 470), (740, 480)]

    for x, y in list:
        print(x, y)
        boby = GRect(20, 20, x=x, y=y)
        boby.filled = True
        boby.fill_color = "Tomato"
        boby.color = "Tomato"  # 設置邊框顏色
        window.add(boby)


    list = [(500, 250), (420, 260), (430, 260), (500, 260), (430, 270), (540, 350), (530, 360), (350, 370), (490, 370), (500, 370), (350, 380), (360, 380), (370, 380), (380, 380), (390, 380), (400, 380), (410, 380), (420, 380), (430, 380), (440, 380), (450, 380), (460, 380), (470, 380), (480, 380), (490, 380), (360, 390), (370, 390), (380, 390), (390, 390), (400, 390), (410, 390), (420, 390), (360, 400), (370, 400), (380, 400), (390, 400), (400, 400), (410, 400), (420, 400), (370, 410), (380, 410), (440, 410), (450, 410), (460, 410), (470, 410), (480, 410), (490, 410), (440, 420), (450, 420), (460, 420), (470, 420), (470, 430), (470, 440), (540, 440), (520, 470), (520, 480), (500, 490), (660, 490), (360, 500), (370, 500), (490, 500), (500, 500), (530, 500), (540, 500), (550, 500), (650, 500), (660, 500), (370, 510), (380, 510), (390, 510), (400, 510), (410, 510), (420, 510), (430, 510), (440, 510), (530, 510), (540, 510), (550, 510), (640, 510), (650, 510), (380, 520), (390, 520), (400, 520), (410, 520), (420, 520), (430, 520), (440, 520), (530, 520), (540, 520), (550, 520), (630, 520), (640, 520), (530, 530), (540, 530), (550, 530), (560, 530), (570, 530), (580, 530), (590, 530), (600, 530), (610, 530), (620, 530), (630, 530), (400, 540), (410, 540), (540, 540), (550, 540), (560, 540), (570, 540), (580, 540), (590, 540), (600, 540), (610, 540), (620, 540), (400, 550), (410, 550), (550, 550), (560, 550), (280, 570), (280, 580), (280, 590), (290, 590), (290, 600), (300, 600), (290, 610), (300, 610), (490, 610), (650, 610), (300, 620), (310, 620), (480, 620), (490, 620), (310, 630), (320, 630), (480, 630), (320, 640), (480, 640), (500, 640), (470, 650), (500, 650), (600, 650), (610, 650), (350, 660), (360, 660), (370, 660), (420, 660), (430, 660), (440, 660), (490, 660), (500, 660), (590, 660), (600, 660), (370, 670), (380, 670), (390, 670), (400, 670), (410, 670), (420, 670), (470, 670), (480, 670), (490, 670), (560, 670), (400, 680), (410, 680), (420, 680), (430, 680), (440, 680), (450, 680), (530, 680), (540, 680), (550, 680), (430, 690), (440, 690), (450, 690), (460, 690), (470, 690), (480, 690), (490, 690), (500, 690), (440, 700), (450, 700), (460, 700), (470, 700), (480, 700), (490, 700), (500, 700), (450, 710), (460, 710), (470, 710)]
    for x, y in list:
        print(x, y)
        boby = GRect(15, 15, x=x, y=y)
        boby.filled = True
        boby.fill_color = "#CA531A"
        boby.color = "#CA531A"  # 設置邊框顏色
        window.add(boby)
    # 編筐
    list = [(370, 95), (375, 95), (380, 95), (385, 95), (390, 95), (395, 95), (400, 95), (405, 95), (410, 95), (415, 95), (420, 95), (425, 95), (430, 95), (435, 95), (440, 95), (445, 95), (450, 95), (455, 95), (460, 95), (370, 100), (375, 100), (380, 100), (385, 100), (390, 100), (395, 100), (400, 100), (405, 100), (410, 100), (415, 100), (420, 100), (425, 100), (430, 100), (435, 100), (440, 100), (445, 100), (450, 100), (455, 100), (460, 100), (350, 105), (355, 105), (360, 105), (365, 105), (470, 105), (475, 105), (480, 105), (485, 105), (350, 110), (355, 110), (360, 110), (365, 110), (470, 110), (475, 110), (480, 110), (485, 110), (325, 120), (330, 120), (335, 120), (340, 120), (490, 120), (495, 120), (325, 125), (330, 125), (335, 125), (340, 125), (495, 125), (315, 130), (505, 130), (510, 130), (310, 135), (315, 135), (505, 135), (510, 135), (310, 140), (315, 140), (310, 145), (315, 145), (515, 145), (520, 145), (310, 150), (315, 150), (520, 150), (300, 155), (305, 155), (310, 155), (315, 155), (530, 155), (535, 155), (300, 160), (305, 160), (310, 160), (315, 160), (530, 160), (535, 160), (300, 165), (305, 165), (540, 165), (545, 165), (300, 170), (305, 170), (540, 170), (545, 170), (300, 175), (305, 175), (290, 180), (295, 180), (300, 180), (305, 180), (550, 180), (555, 180), (290, 185), (295, 185), (300, 185), (305, 185), (550, 185), (555, 185), (290, 190), (295, 190), (550, 190), (555, 190), (290, 195), (295, 195), (550, 195), (555, 195), (285, 200), (290, 200), (295, 200), (550, 200), (555, 200), (275, 205), (280, 205), (285, 205), (290, 205), (295, 205), (550, 205), (555, 205), (275, 210), (280, 210), (285, 210), (290, 210), (555, 210), (275, 215), (280, 215), (565, 215), (570, 215), (275, 220), (280, 220), (565, 220), (570, 220), (275, 225), (280, 225), (565, 225), (570, 225), (275, 230), (280, 230), (565, 230), (570, 230), (275, 235), (280, 235), (565, 235), (570, 235), (275, 240), (280, 240), (565, 240), (570, 240), (275, 245), (280, 245), (565, 245), (570, 245), (275, 250), (280, 250), (565, 250), (570, 250), (275, 255), (280, 255), (565, 255), (570, 255), (275, 260), (280, 260), (565, 260), (570, 260), (275, 265), (280, 265), (565, 265), (570, 265), (275, 270), (280, 270), (565, 270), (275, 275), (280, 275), (575, 275), (580, 275), (275, 280), (280, 280), (575, 280), (580, 280), (275, 285), (280, 285), (530, 285), (535, 285), (540, 285), (545, 285), (575, 285), (580, 285), (275, 290), (280, 290), (530, 290), (535, 290), (540, 290), (545, 290), (575, 290), (580, 290), (275, 295), (280, 295), (525, 295), (530, 295), (535, 295), (575, 295), (580, 295), (275, 300), (280, 300), (515, 300), (520, 300), (525, 300), (530, 300), (535, 300), (575, 300), (580, 300), (275, 305), (280, 305), (515, 305), (520, 305), (525, 305), (530, 305), (575, 305), (580, 305), (275, 310), (280, 310), (385, 310), (390, 310), (395, 310), (400, 310), (405, 310), (410, 310), (515, 310), (520, 310), (575, 310), (580, 310), (275, 315), (280, 315), (385, 315), (390, 315), (395, 315), (400, 315), (405, 315), (410, 315), (415, 315), (515, 315), (520, 315), (575, 315), (580, 315), (275, 320), (280, 320), (405, 320), (410, 320), (415, 320), (575, 320), (580, 320), (275, 325), (280, 325), (410, 325), (415, 325), (420, 325), (425, 325), (430, 325), (435, 325), (575, 325), (580, 325), (720, 325), (725, 325), (730, 325), (735, 325), (275, 330), (280, 330), (410, 330), (415, 330), (420, 330), (425, 330), (430, 330), (435, 330), (580, 330), (720, 330), (725, 330), (730, 330), (735, 330), (275, 335), (280, 335), (565, 335), (570, 335), (720, 335), (725, 335), (730, 335), (735, 335), (740, 335), (745, 335), (750, 335), (275, 340), (280, 340), (565, 340), (570, 340), (720, 340), (725, 340), (730, 340), (735, 340), (740, 340), (745, 340), (750, 340), (275, 345), (280, 345), (555, 345), (560, 345), (565, 345), (570, 345), (710, 345), (715, 345), (720, 345), (725, 345), (745, 345), (750, 345), (755, 345), (760, 345), (275, 350), (280, 350), (550, 350), (555, 350), (560, 350), (565, 350), (570, 350), (710, 350), (715, 350), (720, 350), (725, 350), (745, 350), (750, 350), (755, 350), (760, 350), (275, 355), (280, 355), (550, 355), (555, 355), (560, 355), (705, 355), (710, 355), (715, 355), (755, 355), (760, 355), (275, 360), (280, 360), (540, 360), (545, 360), (550, 360), (555, 360), (695, 360), (700, 360), (705, 360), (710, 360), (715, 360), (755, 360), (760, 360), (765, 360), (770, 360), (775, 360), (275, 365), (280, 365), (540, 365), (545, 365), (550, 365), (555, 365), (695, 365), (700, 365), (705, 365), (710, 365), (755, 365), (760, 365), (765, 365), (770, 365), (775, 365), (275, 370), (280, 370), (515, 370), (520, 370), (525, 370), (530, 370), (535, 370), (540, 370), (545, 370), (695, 370), (700, 370), (770, 370), (775, 370), (275, 375), (280, 375), (515, 375), (520, 375), (525, 375), (530, 375), (535, 375), (540, 375), (545, 375), (695, 375), (700, 375), (770, 375), (775, 375), (275, 380), (280, 380), (515, 380), (520, 380), (695, 380), (700, 380), (770, 380), (775, 380), (275, 385), (280, 385), (505, 385), (510, 385), (515, 385), (520, 385), (695, 385), (700, 385), (770, 385), (775, 385), (275, 390), (280, 390), (505, 390), (510, 390), (515, 390), (520, 390), (695, 390), (700, 390), (770, 390), (275, 395), (280, 395), (430, 395), (435, 395), (440, 395), (445, 395), (450, 395), (455, 395), (460, 395), (465, 395), (470, 395), (475, 395), (480, 395), (485, 395), (490, 395), (495, 395), (500, 395), (505, 395), (510, 395), (695, 395), (700, 395), (780, 395), (785, 395), (275, 400), (280, 400), (430, 400), (435, 400), (440, 400), (445, 400), (450, 400), (455, 400), (460, 400), (465, 400), (470, 400), (475, 400), (480, 400), (485, 400), (490, 400), (495, 400), (500, 400), (505, 400), (510, 400), (695, 400), (700, 400), (780, 400), (785, 400), (275, 405), (280, 405), (400, 405), (405, 405), (410, 405), (415, 405), (420, 405), (425, 405), (430, 405), (435, 405), (505, 405), (510, 405), (515, 405), (520, 405), (695, 405), (700, 405), (780, 405), (785, 405), (275, 410), (280, 410), (395, 410), (400, 410), (405, 410), (410, 410), (415, 410), (420, 410), (425, 410), (430, 410), (435, 410), (505, 410), (510, 410), (515, 410), (520, 410), (695, 410), (700, 410), (780, 410), (785, 410), (275, 415), (280, 415), (515, 415), (520, 415), (780, 415), (785, 415), (275, 420), (280, 420), (480, 420), (485, 420), (515, 420), (520, 420), (525, 420), (530, 420), (535, 420), (685, 420), (690, 420), (780, 420), (785, 420), (275, 425), (280, 425), (480, 425), (485, 425), (515, 425), (520, 425), (525, 425), (530, 425), (535, 425), (685, 425), (690, 425), (780, 425), (785, 425), (275, 430), (280, 430), (480, 430), (485, 430), (530, 430), (535, 430), (540, 430), (545, 430), (675, 430), (735, 430), (780, 430), (785, 430), (275, 435), (280, 435), (480, 435), (485, 435), (530, 435), (535, 435), (540, 435), (545, 435), (670, 435), (675, 435), (730, 435), (735, 435), (780, 435), (785, 435), (275, 440), (280, 440), (480, 440), (485, 440), (670, 440), (675, 440), (730, 440), (735, 440), (780, 440), (785, 440), (275, 445), (280, 445), (395, 445), (400, 445), (405, 445), (410, 445), (415, 445), (480, 445), (485, 445), (550, 445), (555, 445), (575, 445), (580, 445), (585, 445), (590, 445), (595, 445), (650, 445), (655, 445), (660, 445), (665, 445), (670, 445), (675, 445), (720, 445), (725, 445), (730, 445), (735, 445), (780, 445), (785, 445), (275, 450), (280, 450), (400, 450), (405, 450), (410, 450), (415, 450), (480, 450), (485, 450), (550, 450), (555, 450), (580, 450), (585, 450), (590, 450), (650, 450), (655, 450), (660, 450), (665, 450), (670, 450), (675, 450), (720, 450), (725, 450), (730, 450), (735, 450), (780, 450), (785, 450), (275, 455), (280, 455), (410, 455), (415, 455), (480, 455), (485, 455), (540, 455), (545, 455), (550, 455), (555, 455), (560, 455), (565, 455), (570, 455), (600, 455), (605, 455), (610, 455), (615, 455), (635, 455), (640, 455), (660, 455), (665, 455), (710, 455), (715, 455), (730, 455), (735, 455), (780, 455), (785, 455), (275, 460), (280, 460), (410, 460), (415, 460), (480, 460), (485, 460), (540, 460), (545, 460), (550, 460), (555, 460), (560, 460), (565, 460), (570, 460), (600, 460), (605, 460), (610, 460), (615, 460), (635, 460), (640, 460), (660, 460), (665, 460), (710, 460), (715, 460), (730, 460), (735, 460), (780, 460), (785, 460), (265, 465), (420, 465), (425, 465), (480, 465), (485, 465), (530, 465), (535, 465), (540, 465), (545, 465), (625, 465), (630, 465), (635, 465), (640, 465), (660, 465), (665, 465), (700, 465), (705, 465), (710, 465), (715, 465), (730, 465), (735, 465), (770, 465), (265, 470), (270, 470), (420, 470), (425, 470), (480, 470), (485, 470), (530, 470), (535, 470), (540, 470), (545, 470), (625, 470), (630, 470), (635, 470), (640, 470), (660, 470), (665, 470), (695, 470), (700, 470), (705, 470), (710, 470), (715, 470), (730, 470), (735, 470), (770, 470), (775, 470), (265, 475), (270, 475), (480, 475), (485, 475), (530, 475), (535, 475), (660, 475), (665, 475), (695, 475), (700, 475), (705, 475), (730, 475), (735, 475), (265, 480), (270, 480), (430, 480), (435, 480), (480, 480), (485, 480), (530, 480), (535, 480), (660, 480), (665, 480), (670, 480), (675, 480), (680, 480), (685, 480), (690, 480), (695, 480), (700, 480), (730, 480), (735, 480), (755, 480), (760, 480), (265, 485), (270, 485), (435, 485), (480, 485), (485, 485), (530, 485), (535, 485), (660, 485), (665, 485), (670, 485), (675, 485), (680, 485), (685, 485), (690, 485), (695, 485), (700, 485), (730, 485), (735, 485), (755, 485), (760, 485), (265, 490), (270, 490), (445, 490), (450, 490), (480, 490), (485, 490), (515, 490), (520, 490), (525, 490), (530, 490), (535, 490), (670, 490), (675, 490), (680, 490), (685, 490), (690, 490), (730, 490), (735, 490), (740, 490), (745, 490), (750, 490), (755, 490), (760, 490), (265, 495), (270, 495), (445, 495), (450, 495), (480, 495), (485, 495), (515, 495), (520, 495), (525, 495), (530, 495), (535, 495), (670, 495), (675, 495), (680, 495), (685, 495), (690, 495), (730, 495), (735, 495), (740, 495), (745, 495), (750, 495), (755, 495), (760, 495), (265, 500), (270, 500), (480, 500), (485, 500), (515, 500), (520, 500), (670, 500), (675, 500), (680, 500), (265, 505), (270, 505), (455, 505), (460, 505), (480, 505), (485, 505), (515, 505), (520, 505), (670, 505), (675, 505), (720, 505), (725, 505), (265, 510), (270, 510), (455, 510), (460, 510), (480, 510), (485, 510), (515, 510), (520, 510), (670, 510), (675, 510), (720, 510), (725, 510), (265, 515), (270, 515), (455, 515), (460, 515), (490, 515), (495, 515), (500, 515), (505, 515), (510, 515), (515, 515), (520, 515), (660, 515), (665, 515), (670, 515), (675, 515), (720, 515), (725, 515), (265, 520), (270, 520), (455, 520), (460, 520), (490, 520), (495, 520), (500, 520), (505, 520), (510, 520), (515, 520), (520, 520), (660, 520), (665, 520), (670, 520), (675, 520), (720, 520), (725, 520), (265, 525), (270, 525), (400, 525), (405, 525), (410, 525), (415, 525), (420, 525), (425, 525), (430, 525), (435, 525), (440, 525), (445, 525), (650, 525), (655, 525), (660, 525), (665, 525), (720, 525), (725, 525), (265, 530), (270, 530), (395, 530), (400, 530), (405, 530), (410, 530), (415, 530), (420, 530), (425, 530), (430, 530), (435, 530), (440, 530), (445, 530), (450, 530), (650, 530), (655, 530), (660, 530), (665, 530), (720, 530), (725, 530), (265, 535), (270, 535), (265, 540), (270, 540), (635, 540), (640, 540), (710, 540), (715, 540), (265, 545), (270, 545), (635, 545), (640, 545), (710, 545), (715, 545), (265, 550), (270, 550), (350, 550), (355, 550), (360, 550), (365, 550), (370, 550), (375, 550), (380, 550), (385, 550), (390, 550), (575, 550), (580, 550), (585, 550), (590, 550), (595, 550), (600, 550), (605, 550), (610, 550), (615, 550), (620, 550), (625, 550), (630, 550), (710, 550), (715, 550), (265, 555), (270, 555), (350, 555), (355, 555), (360, 555), (365, 555), (370, 555), (375, 555), (380, 555), (385, 555), (390, 555), (575, 555), (580, 555), (585, 555), (590, 555), (595, 555), (600, 555), (605, 555), (610, 555), (615, 555), (620, 555), (625, 555), (630, 555), (710, 555), (715, 555), (265, 560), (270, 560), (575, 560), (580, 560), (710, 560), (715, 560), (265, 565), (270, 565), (395, 565), (400, 565), (405, 565), (410, 565), (415, 565), (420, 565), (425, 565), (480, 565), (485, 565), (490, 565), (495, 565), (500, 565), (505, 565), (510, 565), (565, 565), (570, 565), (575, 565), (580, 565), (710, 565), (715, 565), (265, 570), (270, 570), (400, 570), (405, 570), (410, 570), (415, 570), (420, 570), (425, 570), (480, 570), (485, 570), (490, 570), (495, 570), (500, 570), (505, 570), (510, 570), (565, 570), (570, 570), (575, 570), (580, 570), (710, 570), (265, 575), (270, 575), (420, 575), (425, 575), (430, 575), (435, 575), (470, 575), (475, 575), (480, 575), (485, 575), (505, 575), (510, 575), (695, 575), (700, 575), (265, 580), (270, 580), (420, 580), (425, 580), (430, 580), (435, 580), (470, 580), (475, 580), (480, 580), (485, 580), (505, 580), (510, 580), (695, 580), (700, 580), (265, 585), (270, 585), (430, 585), (435, 585), (440, 585), (445, 585), (450, 585), (455, 585), (460, 585), (465, 585), (470, 585), (475, 585), (505, 585), (510, 585), (685, 585), (265, 590), (270, 590), (430, 590), (435, 590), (440, 590), (445, 590), (450, 590), (455, 590), (460, 590), (465, 590), (470, 590), (475, 590), (505, 590), (510, 590), (685, 590), (690, 590), (505, 595), (510, 595), (275, 600), (280, 600), (505, 600), (510, 600), (670, 600), (675, 600), (275, 605), (280, 605), (505, 605), (510, 605), (675, 605), (275, 610), (280, 610), (505, 610), (510, 610), (660, 610), (665, 610), (275, 615), (280, 615), (505, 615), (510, 615), (660, 615), (665, 615), (505, 620), (510, 620), (290, 625), (295, 625), (505, 625), (510, 625), (650, 625), (655, 625), (290, 630), (505, 630), (650, 630), (300, 635), (305, 635), (490, 635), (495, 635), (635, 635), (640, 635), (300, 640), (305, 640), (490, 640), (495, 640), (635, 640), (640, 640), (315, 645), (480, 645), (485, 645), (490, 645), (495, 645), (625, 645), (310, 650), (315, 650), (480, 650), (485, 650), (490, 650), (495, 650), (625, 650), (630, 650), (480, 655), (485, 655), (325, 660), (330, 660), (335, 660), (340, 660), (455, 660), (460, 660), (465, 660), (470, 660), (475, 660), (480, 660), (485, 660), (610, 660), (615, 660), (325, 665), (330, 665), (335, 665), (340, 665), (455, 665), (460, 665), (465, 665), (470, 665), (475, 665), (480, 665), (485, 665), (615, 665), (350, 670), (355, 670), (360, 670), (365, 670), (435, 670), (440, 670), (445, 670), (450, 670), (455, 670), (460, 670), (575, 670), (580, 670), (585, 670), (590, 670), (595, 670), (600, 670), (605, 670), (350, 675), (355, 675), (360, 675), (365, 675), (430, 675), (435, 675), (440, 675), (445, 675), (450, 675), (455, 675), (460, 675), (575, 675), (580, 675), (585, 675), (590, 675), (595, 675), (600, 675), (605, 675), (370, 685), (375, 685), (380, 685), (385, 685), (390, 685), (565, 685), (570, 685), (375, 690), (380, 690), (385, 690), (565, 690), (395, 695), (400, 695), (405, 695), (410, 695), (415, 695), (420, 695), (425, 695), (515, 695), (520, 695), (525, 695), (530, 695), (535, 695), (540, 695), (545, 695), (550, 695), (555, 695), (395, 700), (400, 700), (405, 700), (410, 700), (415, 700), (420, 700), (425, 700), (515, 700), (520, 700), (525, 700), (530, 700), (535, 700), (540, 700), (545, 700), (550, 700), (555, 700), (435, 705), (480, 705), (485, 705), (490, 705), (495, 705), (500, 705), (505, 705), (430, 710), (435, 710), (480, 710), (485, 710), (490, 710), (495, 710), (500, 710), (505, 710), (510, 710), (445, 720), (450, 720), (455, 720), (460, 720), (465, 720), (470, 720), (475, 720), (445, 725), (450, 725), (455, 725), (460, 725), (465, 725), (470, 725)]
    for x, y in list:
        print(x, y)
        boby = GRect(8, 8, x=x, y=y)
        boby.filled = True
        boby.fill_color = "black"
        window.add(boby)


    label = GLabel("小火龍")
    label.font = '-50'
    label.color = "red"
    window.add(label, x=0, y=63)


if __name__ == '__main__':
    main()


from PIL import Image

# 加載圖片
image = Image.open('/Users/mac/Desktop/截圖 2024-08-26 下午10.50.41.png')

# 設置縮小的區塊大小
block_size = 5

# 獲取圖片的寬度和高度
width, height = image.size

# 初始化一個空列表來存儲黑色點的座標
black_pixels = []

# 遍歷圖片，每次以10x10的區塊進行計算
for y in range(0, height, block_size):
    for x in range(0, width, block_size):
        # 計算這個區塊的黑色像素數量
        black_pixel_count = 0
        for i in range(block_size):
            for j in range(block_size):
                if x + i < width and y + j < height:
                    pixel = image.getpixel((x + i, y + j))
                    if pixel == (64, 32, 10, 255)  :
                        black_pixel_count += 1

        # 如果區塊內的黑色像素數量大於某個閾值，記錄該區塊的左上角座標
        threshold = block_size * block_size * 0.5  # 閾值設為該區塊50%的像素是黑色
        if black_pixel_count >= threshold:
            black_pixels.append((x, y))

# 打印黑色點的座標
print(black_pixels)

'''
import webcolors
from PIL import Image

def get_closest_color_name(rgb_color):
    try:
        return webcolors.rgb_to_name(rgb_color)
    except ValueError:
        min_colors = {}
        for hex_code, name in webcolors.CSS3_HEX_TO_NAMES.items():
            r_c, g_c, b_c = webcolors.hex_to_rgb(hex_code)
            rd = (r_c - rgb_color[0]) ** 2
            gd = (g_c - rgb_color[1]) ** 2
            bd = (b_c - rgb_color[2]) ** 2
            min_colors[(rd + gd + bd)] = name
        return min_colors[min(min_colors.keys())]

# 加載圖片
image = Image.open('/Users/mac/Desktop/截圖 2024-08-26 下午10.50.41.png')

# 獲取圖片的寬度和高度
width, height = image.size

# 初始化一個字典來存儲顏色及其出現次數
color_count = {}

# 遍歷圖片的每個像素點，統計顏色的出現次數
for y in range(height):
    for x in range(width):
        pixel = image.getpixel((x, y))
        if pixel in color_count:
            color_count[pixel] += 1
        else:
            color_count[pixel] = 1

# 對顏色出現次數進行排序
sorted_colors = sorted(color_count.items(), key=lambda item: item[1], reverse=True)

# 打印不同顏色的數量
print(f"這張圖片中有 {len(color_count)} 種不同的顏色。")

# 列出排序後的顏色及其出現次數，並顯示顏色名稱
print("圖片中的顏色碼及其出現次數（按次數從多到少排序）分別是：")
for color, count in sorted_colors:
    # 去掉Alpha通道，保留RGB
    rgb_color = color[:3]
    # 獲取最接近的顏色名稱
    color_name = get_closest_color_name(rgb_color)
    print(f"顏色: {color} 名稱: {color_name} 出現次數: {count}")

(255, 255, 255, 255) - 名稱: 白色 (White) 出現次數: 487552
(255, 127, 39, 255) - 名稱: 珊瑚橙 (Coral) 出現次數: 116780
(0, 0, 0, 255) - 名稱: 黑色 (Black) 出現次數: 33948
(202, 83, 26, 255) - 名稱: 巧克力色 (Chocolate) 出現次數: 19012
(254, 249, 216, 255) - 名稱: 玉米絲色 (Cornsilk) 出現次數: 10036
(251, 67, 57, 255) - 名稱: 番茄紅 (Tomato) 出現次數: 5500
(102, 102, 102, 255) - 名稱: 暗灰色 (Dimgray) 出現次數: 3065
(191, 191, 191, 255) - 名稱: 銀色 (Silver) 出現次數: 2508
(64, 64, 64, 255) - 名稱: 深灰藍 (Dark Slate Gray) 出現次數: 2508
(236, 223, 162, 255) - 名稱: 蒼麥色 (Pale Goldenrod) 出現次數: 2436
(64, 32, 10, 255) - 名稱: 栗色 (Maroon) 出現次數: 2416
(191, 95, 29, 255) - 名稱: 巧克力色 (Chocolate) 出現次數: 2416
(255, 242, 0, 255) - 名稱: 黃色 (Yellow) 出現次數: 1732
'''
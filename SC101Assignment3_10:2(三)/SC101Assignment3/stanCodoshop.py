"""
File: stanCodoshop.py
Name: 
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    color_distance = math.sqrt((red - pixel.red)**2+(green - pixel.green)**2+(blue - pixel.blue)**2)

    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    pixels_red = 0
    pixels_green = 0
    pixels_blue = 0
    for i in range(len(pixels)):
        #print(i)
        pixels_red += pixels[i].red
        pixels_green += pixels[i].green
        pixels_blue += pixels[i].blue

    red = pixels_red // len(pixels)
    green = pixels_green // len(pixels)
    blue = pixels_blue // len(pixels)

    return [red, green, blue]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    # 初始化最短距離及對應像素
    best_pixel = None
    min_dist = float('inf')
    # 計算平均 RGB 值
    avg = get_average(pixels)
    for pixel in pixels:
        dist = get_pixel_dist(pixel, avg[0], avg[1], avg[2])

        # 如果當前距離小於最小距離，更新最佳像素及最小距離
        if dist < min_dist:
            min_dist = dist
            best_pixel = pixel
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    #TEST Milestone 1
    # green_im = SimpleImage.blank(20,20,'green')
    # green_pixel = green_im.get_pixel(0,0)
    # print(get_pixel_dist(green_pixel,5,255,10))

    #TEST Milestone 2
    # green_pixel = SimpleImage.blank(20,20,'green').get_pixel(0,0)
    # red_pixel = SimpleImage.blank(20,20,'red').get_pixel(0,0)
    # blue_pixel = SimpleImage.blank(20,20,'blue').get_pixel(0,0)
    # print(get_average([green_pixel,green_pixel,green_pixel,blue_pixel]))

    # TEST Milestone 3
    # green_pixel = SimpleImage.blank(20,20,'green').get_pixel(0,0)
    # red_pixel = SimpleImage.blank(20,20,'red').get_pixel(0,0)
    # blue_pixel = SimpleImage.blank(20,20,'blue').get_pixel(0,0)
    # best1 = get_best_pixel([green_pixel,red_pixel,blue_pixel])
    # print(best1.red,best1.green,best1.blue)
    # ----- YOUR CODE ENDS HERE ----- #
    # 遍歷每個像素位置
    for x in range(width):
        for y in range(height):
            # 收集所有圖像中該位置 (x, y) 的像素
            pixels = [image.get_pixel(x, y) for image in images]
            #print(pixels)

            # 使用 get_best_pixel 找出最佳像素
            best_pixel = get_best_pixel(pixels)

            # 將該最佳像素的 RGB 值賦予結果影像的對應位置
            result_pixel = result.get_pixel(x, y)
            result_pixel.red = best_pixel.red
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()

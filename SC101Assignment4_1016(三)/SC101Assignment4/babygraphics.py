"""
File: babygraphics.py
Name: Gary
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    num_years = len(YEARS)
    spacing = (width-GRAPH_MARGIN_SIZE) // num_years
    return year_index * spacing


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    for YEAR in range(len(YEARS)):
        canvas.create_line(GRAPH_MARGIN_SIZE+get_x_coordinate(CANVAS_WIDTH, YEAR), 0, GRAPH_MARGIN_SIZE+get_x_coordinate(CANVAS_WIDTH, YEAR), CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(GRAPH_MARGIN_SIZE+TEXT_DX+get_x_coordinate(CANVAS_WIDTH, YEAR),CANVAS_HEIGHT-GRAPH_MARGIN_SIZE , text=YEARS[YEAR], anchor=tkinter.NW,)



def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """

    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    p = CANVAS_HEIGHT / MAX_RANK
    for name in range(len(lookup_names)):
        # 使用字典推導式來補全缺失的年份
        data = name_data[lookup_names[name]]
        full_data = {str(year): data.get(str(year), '0') for year in YEARS}

        # 繪製線條和文字
        for YEAR in range(len(YEARS) - 1):
            print(str(YEARS[YEAR]))
            print(str(YEARS[YEAR + 1]))
            print(full_data[str(YEARS[YEAR])])
            print(full_data[str(YEARS[YEAR + 1])])

            # 計算當前年份和下一年份的 y1 和 y2 座標
            if int(full_data[str(YEARS[YEAR])]) == 0:
                y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                text = lookup_names[name] + '*'
            else:
                y1 = GRAPH_MARGIN_SIZE + int(full_data[str(YEARS[YEAR])]) * p
                text = lookup_names[name] + full_data[str(YEARS[YEAR])]

            if int(full_data[str(YEARS[YEAR + 1])]) == 0:
                y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            else:
                y2 = GRAPH_MARGIN_SIZE + int(full_data[str(YEARS[YEAR + 1])]) * p

            # 繪製線條
            canvas.create_line(
                GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, YEAR), y1,
                GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, YEAR + 1), y2,
                width=LINE_WIDTH, fill=COLORS[name % len(COLORS)]  # 取餘數
            )

            # 繪製當前年份的文字
            canvas.create_text(
                GRAPH_MARGIN_SIZE + TEXT_DX + get_x_coordinate(CANVAS_WIDTH, YEAR),
                y1, text=text, anchor='sw', fill=COLORS[name % len(COLORS)]  # 取餘數
            )

            print('--' * 10)

        # 單獨處理最後一年的文字繪製
        if int(full_data[str(YEARS[-1])]) == 0:
            y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            text = lookup_names[name] + '*'
        else:
            y1 = GRAPH_MARGIN_SIZE + int(full_data[str(YEARS[-1])]) * p
            text = lookup_names[name] + full_data[str(YEARS[-1])]

        canvas.create_text(
            GRAPH_MARGIN_SIZE + TEXT_DX + get_x_coordinate(CANVAS_WIDTH, len(YEARS) - 1),
            y1, text=text, anchor='sw', fill=COLORS[name % len(COLORS)]  # 取餘數
        )


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()

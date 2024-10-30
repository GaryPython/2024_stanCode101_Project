"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # 初始化速度變數
        self.__dx = 0
        self.__dy = 0
        #初始化生命
        self.lives = 0
        # 追蹤遊戲是否開始
        self.game_started = False
        # 追蹤剩餘的磚塊數量
        self.total_bricks = brick_rows * brick_cols



        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)


        # Create a paddle
        self.paddle = GRect(width=PADDLE_WIDTH, height=PADDLE_HEIGHT)
        self.paddle.filled = True
        self.window.add(self.paddle,x=(self.window.width-self.paddle.width)//2,y=self.window.height-PADDLE_OFFSET)


        # Center a filled ball in the graphical window
        self.ball = GOval(width=BALL_RADIUS*2,height=BALL_RADIUS*2)
        self.ball.filled = True
        self.window.add(self.ball,x=self.window.width//2- BALL_RADIUS,y= self.window.height//2- BALL_RADIUS)

        # 在上方顯示剩餘生命次數的標籤
        self.lives_label = GLabel(f"Lives: {self.lives}")
        self.lives_label.font = "-20"
        self.window.add(self.lives_label, x=10, y=20)


        # Default initial velocity for the ball
        # Initialize our mouse listeners
        # 初始化滑鼠監聽器
        # Draw bricks
        # 定義每兩行磚塊的顏色
        BRICK_COLORS = ['red', 'orange', 'yellow', 'green', 'blue']
        for row in range(brick_rows):
            for col in range(brick_cols):
                # 計算每個磚塊的x, y位置
                x = col * (brick_width + brick_spacing)
                y = brick_offset + row * (brick_height + brick_spacing)

                # 創建磚塊並將其添加到視窗中
                brick = GRect(width=brick_width, height=brick_height)
                brick.filled = True
                # 設定每兩行使用一種顏色
                color_index = (row // 2) % len(BRICK_COLORS)  # 每兩行換一個顏色
                brick.fill_color = BRICK_COLORS[color_index]
                brick.color = BRICK_COLORS[color_index]
                self.window.add(brick, x=x, y=y)
        onmousemoved(self.handle_mouse_move)  # paddle位置
        onmouseclicked(self.handle_click)  # 點擊開關



    def handle_mouse_move(self, event):
            """
            讓板子隨滑鼠移動，並且板子始終位於視窗內。
            """
            # 計算板子新的 x 座標，使板子正中間與滑鼠的 x 座標對齊
            new_x = event.x - self.paddle.width // 2
            # 限制板子不能超出視窗左邊界
            if new_x < 0:
                new_x = 0
            # 限制板子不能超出視窗右邊界
            elif new_x + self.paddle.width > self.window.width:
                new_x = self.window.width - self.paddle.width
            # 更新板子的 x 座標，保持 y 座標不變
            self.paddle.x = new_x

    def handle_click(self, event):
        """
        當點擊滑鼠時，若遊戲尚未開始，初始化球的速度並開始遊戲。
        """
        if not self.game_started: #點擊開關、確保過中部會誤觸
            # 設定初始水平和垂直速度
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

            # 標記遊戲開始
            self.game_started = True

    def move_ball(self):
        """
        控制球的移動，並檢查與邊界和板子的碰撞。
        """
        if self.game_started:
            self.ball.move(self.__dx, self.__dy)

            # 檢查球的四個頂點是否與物件發生碰撞
            self.check_collision()

            # 檢查與邊框的碰撞
            if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
                self.__dx = -self.__dx
            if self.ball.y <= 0:
                self.__dy = -self.__dy

            # 檢查與板子的碰撞
            # if self.ball.y + self.ball.height >= self.paddle.y+self.paddle.height:
            #     ball_bottom_center_x = self.ball.x + self.ball.width / 2
            #     if self.paddle.x <= ball_bottom_center_x <= self.paddle.x + self.paddle.width:
            #         self.__dy = -self.__dy  # 球反彈

            # # 檢查球是否掉出視窗底部（遊戲結束）
            # if self.ball.y + self.ball.height > self.window.height:
            #     self.reset_ball()

    def check_collision(self):
            """
            檢查球的四個頂點是否與物件碰撞，並處理反彈或移除磚塊。
            """
            # 取得球的四個頂點
            ball_x = self.ball.x
            ball_y = self.ball.y
            ball_size = self.ball.width
            points_to_check = [
                (ball_x, ball_y),  # 左上
                (ball_x + ball_size, ball_y),  # 右上
                (ball_x, ball_y + ball_size),  # 左下
                (ball_x + ball_size, ball_y + ball_size)  # 右下
            ]

            for point in points_to_check:
                obj = self.window.get_object_at(point[0], point[1])
                # True: True ,not None
                if obj and obj is not self.lives_label:
                    if obj is self.paddle:
                        if self.__dy > 0:
                            self.__dy = -self.__dy  # 碰到板子反彈
                    else:
                        self.__dy = -self.__dy  # 碰到磚塊反彈
                        self.window.remove(obj)  # 移除磚塊
                        self.total_bricks -= 1  # 更新剩餘磚塊數量
                    break  # 一旦有碰撞發生，停止檢查其餘頂點

    def reset_ball(self):
        """
        重置球的位置到畫面中間，並停止移動。
        """
        self.window.add(self.ball, x=self.window.width // 2 - BALL_RADIUS,
                        y=self.window.height // 2 - BALL_RADIUS)
        self.game_started = False


    def end_game(self, won):
        """
        結束遊戲並顯示勝利或失敗的訊息。
        """
        self.game_started = False
        message = GLabel("You Win!" if won else "Game Over")
        message.font = "-35"
        self.window.add(message, x=(self.window.width - message.width) // 2,
                        y=self.window.height // 2)

    def update_lives_label(self):
        """
        更新顯示的生命次數。
        """
        self.lives_label.text = f"Lives: {self.lives}"



"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    breakout_graphics = BreakoutGraphics(brick_rows=5, brick_cols=5)  # 創建遊戲實例
    breakout_graphics.lives = NUM_LIVES   #初始化玩家生命值、更新遊戲初始生命值顯示

    while True:
        breakout_graphics.move_ball()  # 控制球的移動
        pause(FRAME_RATE)  # 暫停一段時間以控制遊戲速度
        # 檢查遊戲的終止條件
        if breakout_graphics.total_bricks == 0:  # 所有磚塊消滅，遊戲勝利
            breakout_graphics.end_game(True)
            break  # 結束遊戲

        if breakout_graphics.ball.y + breakout_graphics.ball.height > breakout_graphics.window.height:
            # 球的位置＋球的高度 超過視窗範圍
            breakout_graphics.lives -= 1  # 當球掉出視窗底部時，減少生命值
            breakout_graphics.update_lives_label()  # 更新生命值標籤
            if breakout_graphics.lives > 0:
                breakout_graphics.reset_ball()  # 重置球的位置並繼續遊戲
            else:
                breakout_graphics.end_game(False)  # 生命值用盡，遊戲失敗
                break  # 結束遊戲

if __name__ == '__main__':
    main()



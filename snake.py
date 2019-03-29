import pygame
from random import choice
'''
贪吃蛇
'''

# 食物
class Food():
    def __init__(self):
        # 判断区域是否被占用
        while True:
            self.x = choice(xy_list)
            self.y = choice(xy_list)
            if [self.x, self.y] not in xy_list_in:
                break

    # 出现一个食物
    def create_food(self):
        pygame.draw.circle(window, [255, 255, 255], [self.x+5, self.y+5], 5)


# 蛇
class Snake():
    def __init__(self):
        self.x = 250
        self.y = 250

    # 创建身体
    def create_snake(self):
        pygame.draw.rect(window, [255, 255, 255], [self.x, self.y, 10, 10])
        xy_list_in.append([self.x, self.y])

    # 消除身体
    def delete_snake(self):
        if len(xy_list_in) > 2:
            pygame.draw.rect(window, [0, 0, 0], [xy_list_in[0][0], xy_list_in[0][1], 10, 10])
            xy_list_in.pop(0)

    # 移动
    def move(self):
        if [self.x, self.y] not in xy_list_in:
            self.create_snake()
            if (food.x, food.y) != (self.x, self.y):
                self.delete_snake()

if __name__ == '__main__':

    # 初始化
    pygame.init()
    # 创建窗口
    window = pygame.display.set_mode((500, 500))
    # 设置窗口名字
    pygame.display.set_caption("贪吃蛇")
    # 背景色
    window.fill([0, 0, 0])
    # 分块
    xy_list = []
    for i in range(0, 500, 10):
        xy_list.append(i)
    # 占用区域
    xy_list_in = []

    # 创建对象
    snake = Snake()
    food = Food()

    # 创建蛇和食物
    snake.create_snake()
    food.create_food()

    # 判断方向变量
    k = 0

    while True:
        # 食物被吃掉了就出现新的
        if (food.x, food.y) == (snake.x, snake.y):
            food = Food()
            food.create_food()

        # 创建事件
        walk = pygame.event.get()
        for l in walk:
            # 关闭窗口
            if l.type == pygame.QUIT:
                exit()
            # 判断是否按键
            if l.type == pygame.KEYDOWN:
                if l.key == pygame.K_DOWN or l.key == pygame.K_s:
                    if k != 2:
                        k = 1
                if l.key == pygame.K_UP or l.key == pygame.K_w:
                    if k != 1:
                        k = 2
                if l.key == pygame.K_LEFT or l.key == pygame.K_a:
                    if k != 4:
                        k = 3
                if l.key == pygame.K_RIGHT or l.key == pygame.K_d:
                    if k != 3:
                        k = 4

        # 持续移动
        # 判断移动方向
        if k == 1:
            if snake.y == 500:
                snake.y = -10
            snake.y += 10
            snake.move()
        if k == 2:
            if snake.y == 0:
                snake.y = 500
            snake.y -= 10
            snake.move()
        if k == 3:
            if snake.x == 0:
                snake.x = 500
            snake.x -= 10
            snake.move()
        if k == 4:
            if snake.x == 500:
                snake.x = -10
            snake.x += 10
            snake.move()

        # 判断结束游戏
        if (len(xy_list_in) >= 5) & (([snake.x, snake.y] in xy_list_in) & ([snake.x, snake.y] != xy_list_in[-1])):
            game_over = pygame.font.SysFont('arial', 40)
            text = game_over.render("Game Over", True, [255, 255, 255])
            window.blit(text, (150, 200))
            k = 0

        # 延迟
        pygame.time.delay(100)

        # 刷新
        pygame.display.update()








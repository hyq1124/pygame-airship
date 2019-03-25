import pygame
from random import randint
import time


class Game():
    # 初始化
    pygame.init()

    # 创建窗口
    window = pygame.display.set_mode((622, 350))

    # 设置窗口名字
    pygame.display.set_caption("飞船")

    # 背景色
    # window.fill([255, 255, 255])

    # 加载图片
    background = pygame.image.load("bg.jpg").convert()
    airship = pygame.image.load("airship.jpg").convert()

    # 添加背景音乐
    filename = 'bgmusic.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(-1, 10)


class AirShip():
    def __init__(self):
        # 飞船的坐标
        self.x = 0
        self.y = 170

    # 向上移动
    def move_up(self):
        if self.y > 0:
            self.y -= 1

    # 向下移动
    def move_down(self):
        if self.y < 315:
            self.y += 1

    # 向左移动
    def move_left(self):
        if self.x > 0:
            self.x -= 1

    # 向右移动
    def move_right(self):
        if self.x < 570:
            self.x += 1

    @staticmethod
    def move():
        # 持续移动

        # 判断按键状态
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_s]:
            airship.move_down()
        if key_pressed[pygame.K_UP] or key_pressed[pygame.K_w]:
            airship.move_up()
        if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]:
            airship.move_left()
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]:
            airship.move_right()


# 动画精灵
# 用该方法承载障碍物使其移动
class SkierClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # 加载图片
        self.image = pygame.image.load("start.jpg")
        # 矩形框选图片获取位置，大小
        self.rect = self.image.get_rect()
        # 设置位置
        self.rect.left, self.rect.top = [Game.background.get_width()+randint(50, 200), randint(0, Game.background.get_height() - 50 )]
        # 设置速度
        self.speed = [-1, 0]

    def move(self):
        self.rect = self.rect.move(self.speed)



# 创建图形
# class Bown():
#     def __init__(self):
#         self.x = 700
#         self.y = randint(0, 350)
#
#     def createbown(self):
#         pygame.draw.circle(Game.background, [randint(0, 256), randint(0, 256), randint(0, 256)], [self.x, self.y], 15)

    # circle(Surface, color, pos, radius, width=0)


if __name__ == '__main__':
    # 创建对象
    g = Game()
    airship = AirShip()
    skl = []
    for i in range(10):
        sk = SkierClass()
        skl.append(sk)
    
    # 出现障碍物数量
    r = 5
    # 计时器
    sc = 0
    # 辅助控制计时器
    a = 50
    # 等级
    level = 0

    # 控制速度
    sleep_time = 0.01
    while True:
        # 添加背景图
        g.window.blit(g.background, (0, 0))
        # 添加飞船图片
        g.window.blit(g.airship, (airship.x, airship.y))
        # 添加障碍物图片
        # 移动飞船
        airship.move()
        # 移动障碍物
        for j in range(r):
            g.window.blit(skl[j].image, skl[j].rect)
            skl[j].move()

        # 障碍物循环出现
        for k in range(r):
            if skl[k].rect.left < -randint(50, 200):
                skl[k].rect.left, skl[k].rect.top = [Game.background.get_width() + randint(50, 1000), randint(0, Game.background.get_height() - 50) ]

        # 调整速度等级
        time.sleep(0.0005)
        sc += 1
        # 保证sleep函数不会出错
        if sleep_time > 0:
            time.sleep(sleep_time)
            # 升级速度
            if sc >= a:
                sleep_time -= 0.0002
                a += a/10
                sc = 0
                level += 1
                
        # 根据等级增加障碍物数量
        r = 5 + (level // 10)

        # 创建事件
        walk = pygame.event.get()

        # 每个事件是一个列表
        for l in walk:
            # 关闭窗口
            if l.type == pygame.QUIT:
                exit()
            # 判断是否按键
            # if l.type == pygame.KEYDOWN:
            # if l.key == pygame.K_DOWN or l.key == pygame.K_s:
            #    pass
        # 停止音乐
        # pygame.mixer.music.stop()

        # 刷新
        pygame.display.update()
        # pygame.display.flip()
        # 延时
        # pygame.time.delay(10)


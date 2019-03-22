import pygame

class Game():
    # 创建窗口
    window = pygame.display.set_mode((622, 350))

    # 设置窗口名字
    pygame.display.set_caption("飞船")

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

    def move_up(self):
        if airship.y > 0:
            airship.y -= 0.1

    def move_down(self):
        if self.y < 315:
            self.y += 0.1

    def move_left(self):
        if self.x > 0:
            self.x -= 0.1

    def move_right(self):
        if self.x < 570:
            self.x += 0.1

    @staticmethod
    def move():
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


if __name__ == '__main__':
    # 创建对象
    g = Game()
    airship = AirShip()
    while True:
        # 添加背景图
        g.window.blit(g.background, (0, 0))
        # 添加飞船图片
        g.window.blit(g.airship, (airship.x, airship.y))
        # 移动飞船
        airship.move()


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
                #     if airship.y < 315:
                #         airship.y += 5
                #         print('↓')
                # if l.key == pygame.K_UP or l.key == pygame.K_w:
                #     if airship.y > 0:
                #         airship.y -= 5
                #         print('↑')
                # if l.key == pygame.K_LEFT or l.key == pygame.K_a:
                #     if airship.x > 0:
                #         airship.x -= 5
                #         print('←')
                # if l.key == pygame.K_RIGHT or l.key == pygame.K_d:
                #     if airship.x < 570:
                #         airship.x += 5
                #         print('→')

        # 停止音乐
        # pygame.mixer.music.stop()

        # 刷新
        pygame.display.update()
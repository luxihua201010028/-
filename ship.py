import pygame


class Ship:

    def __init__(self, screen):
        """初始化飞船，并设置其初始位置"""
        self.screen = screen

        # 加载飞船图像并且获取其外接矩形
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx  # 飞船中心的x坐标
        self.rect.bottom = self.screen_rect.bottom  # 飞船下边缘的y坐标

    def blitme(self):
        """在指定的位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

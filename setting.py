import pygame


class settings:
    """存储外星人入侵的所有泪"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.image = 'image/aircraft.jpeg'
        self.game_title = 'Alien Invasion'


# 初始化pygame ,设置和屏幕对象
pygame.init()
ai_settings = settings()
# 初始化窗口大小
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
# 创建标题
pygame.display.set_caption(ai_settings.game_title)
# 设置背景图片
back_ground_image = pygame.image.load(ai_settings.image).convert()

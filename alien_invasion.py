import pygame  # 导入整个模块

import game_functions as gf  # 为导入的模块指定别名
from setting import settings  # 导入某个类
from ship import Ship  # 导入某个类
from pygame.sprite import Group


def run_game():
    # 初始化pygame ,设置和屏幕对象
    pygame.init()
    ai_settings = settings()
    # 初始化窗口大小
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 创建标题
    pygame.display.set_caption(ai_settings.game_title)
    # 设置背景图片
    back_ground_image = pygame.image.load(ai_settings.image).convert()
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, back_ground_image, bullets)
        gf.update_bulltes(bullets)


run_game()

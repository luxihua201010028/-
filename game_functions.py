import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_fleet_edges(ai_setting, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_setting, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, aliens):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


def get_number_aliens(ai_settings, alien_width):
    # 计算水平空间=行空间-两个外星人宽度，也就是左右各预留一个外星人宽度
    available_space_x = ai_settings.screen_width - 2 * alien_width
    # 计算外星人的个数,强制取整，一个外星人预留两个外星人的宽度
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def creat_aliens(ai_settings, screen, aliens, alien_number, row_number):
    # 创建一行外星人并将其加入到当前行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    # 外星人的位置=2*N+1
    alien.x = (2 * alien_number + 1) * alien_width
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.width + 2 * alien.rect.height * row_number
    alien.add(aliens)


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕上可以容纳多少加密和外星人"""
    available_space_y = (ai_settings.screen_height - ship_height - (3 * alien_height))
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建外星人，并计算一行可以容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_aliens(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.width)
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            creat_aliens(ai_settings, screen, aliens, alien_number, row_number)


def check_keydown_event(event, ai_setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:  # 检测到是向右的键
        ship.moving_right = True
    if event.key == pygame.K_LEFT:  # 检测到是向左的键
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:  # 空格发射子弹
        fire_bullet(ai_setting, screen, ship, bullets)
    elif event.key == pygame.K_q:  # q退出
        sys.exit()


def fire_bullet(ai_setting, screen, ship, bullets):
    # 创建一颗子弹并将其加入到编组bullets
    if len(bullets) < ai_setting.bullets_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)


def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:  # 检测到是向右的键
        ship.moving_right = False
    if event.key == pygame.K_LEFT:  # 检测到是向左的键
        ship.moving_left = False


def check_events(ai_setting, screen, ship, bullets):
    # 监视键盘和鼠标状态
    for event in pygame.event.get():
        # 如果单击关闭按钮，退出游戏
        if event.type == pygame.QUIT:
            # 退出
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 响应按键
            check_keydown_event(event, ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:  # 响应松开
            check_keyup_event(event, ship)


def update_screen(ai_settings, screen, ship, back_ground_image, aliens, bullets):
    """更新屏幕上的图像，并切换到新图像"""
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    # 缓冲区中绘制图像
    screen.blit(back_ground_image, (0, 0))
    # 在飞船和外星人后面重新绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bulltes(aliens, bullets):
    """更新子弹位置，并删除已消失的子弹"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 检查是否有子弹击中外星人，如果是这样，删除子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

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
        self.ship_speed_factor = 3

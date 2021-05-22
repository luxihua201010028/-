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
        self.ship_speed_factor = 5
        self.ship_limit = 3
        # 子弹设置
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # 将微笑时的子弹限制为10颗
        self.bullets_allowed = 20
        # 外星人设置
        self.alien_speed_factor = 1

        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右，为-1表示向左
        self.fleet_direction = 1

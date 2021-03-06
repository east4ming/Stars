"""星星相关的类和函数.

- 星星类
- 星星相关函数
    - 获取一行的星星数
    - 获取一列的星星数
    - 添加星星群组
"""
import pygame
from pygame.sprite import Sprite
import random


class Star(Sprite):
    """一个星星的类"""
    def __init__(self, screen):
        super(Star, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/StarLogoMini.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width // 2
        self.rect.y = self.rect.height // 2

    def blitme(self):
        self.screen.blit(self.image, self.rect)


def cal_star_number_x(screen_width, star_width):
    available_space_x = screen_width - star_width // 2
    star_number_x = int(available_space_x / (1.5 * star_width))
    return star_number_x


def cal_star_number_y(screen_height, star_height):
    available_space_y = screen_height - star_height // 2
    star_number_y = int(available_space_y / (1.5 * star_height))
    return star_number_y


def create_stars(the_screen, screen_width, screen_height, stars):
    sample_star = Star(the_screen)
    star_width = sample_star.rect.width
    star_height = sample_star.rect.height
    star_number_x = cal_star_number_x(screen_width, star_width)
    star_number_y = cal_star_number_y(screen_height, star_height)
    for line in range(star_number_y):
        for num in range(star_number_x):
            star_x = random.randint(0, star_width) + \
                     num * 2 * random.randint(star_width // 2, star_width)
            star_y = random.randint(0, star_height) + \
                     line * 2 * random.randint(star_height // 2, star_height)
            star = Star(the_screen)
            star.rect.x = star_x
            star.rect.y = star_y
            stars.add(star)

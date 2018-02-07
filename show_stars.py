"""显示星星.

- 主函数
"""
import pygame
import sys
from pygame.sprite import Group

import star_func
import scr_func


def main():
    pygame.init()
    the_screen = scr_func.screen_init(scr_func.screen_width,
                                      scr_func.screen_height)
    pygame.display.set_caption('Stars')
    stars = Group()
    star_func.create_stars(the_screen,
                           scr_func.screen_width,
                           scr_func.screen_height,
                           stars)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        scr_func.screen_fill(the_screen,
                             scr_func.screen_bg_color)
        stars.draw(the_screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()

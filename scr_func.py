"""游戏屏幕相关的函数"""
import pygame

screen_width = 800
screen_height = 600
screen_bg_color = (19, 70, 149)


def screen_init(screen_width, screen_height):
    screen = pygame.display.set_mode((screen_width, screen_height))
    return screen


def screen_fill(screen, screen_bg_color):
    screen.fill(screen_bg_color)

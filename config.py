import pygame
import note

HEIGHT = 1000
WIDTH = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
fill_color = (0, 0, 0)
score = 0
color_timer = 250
note_dict = {"blue":["assets/blue.png", 100, pygame.K_LEFT], "green":["assets/green.png", 233, pygame.K_UP],
             "purple":["assets/purple.png", 366, pygame.K_RIGHT], "red":["assets/red.png", 500, pygame.K_DOWN]}
notes = []
chord_rect = pygame.Rect(0, 800, 700, 50)
target_notes = [note.Note("blue",  775), note.Note("green",  775), note.Note("red",  775), note.Note("purple", 775)]
note_chart = [(1000, "red"), (2000, "blue"), (3000, "green")]

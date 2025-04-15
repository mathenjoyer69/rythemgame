import pygame
import note

HEIGHT = 1000
WIDTH = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))

note_dict = {"blue":["assets/blue.png", 100], "green":["assets/green.png", 233], "purple":["assets/purple.png", 366], "red":["assets/red.png", 500]}
chord_rect = pygame.Rect(0, 800, 700, 50)
target_notes = [note.Note("blue",  775), note.Note("green",  775), note.Note("red",  775), note.Note("purple", 775)]
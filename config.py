import pygame
import note

HEIGHT = 1000
WIDTH = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("rythem game")
fill_color = (0, 0, 0)
score = 0
velocity = 0.5 #0.5 in the minimum
color_timer = 50
note_dict = {"blue":["assets/blue.png", 100, pygame.K_LEFT], "green":["assets/green.png", 233, pygame.K_DOWN],
             "purple":["assets/purple.png", 366, pygame.K_UP], "red":["assets/red.png", 500, pygame.K_RIGHT]}
notes = []
chord_rect = pygame.Rect(0, 800, 700, 50)
target_notes = [note.Note("blue",  775), note.Note("green",  775), note.Note("red",  775), note.Note("purple", 775)]
note_chart = [(1000, "red"),(1500, "blue"),(2000, "green"),(2500, "purple"),(3000, "red"),(3500, "blue"),(4000, "green"),(4500, "red"),(5000, "purple"),(5500, "green"),(6000, "blue"),(6500, "red"),(7000, "red"),(7500, "blue"),(8000, "green"),(8500, "purple"),(9000, "red"),(9500, "green"),(10000, "blue"),(10500, "purple"),(11000, "red")]


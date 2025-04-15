import pygame
import config

class Note:
    def __init__(self, color, y):
        self.color = color
        self.x = config.note_dict[self.color][1]
        self.y = y
        self.velocity = 0.5
        self.rect = pygame.Rect(self.x, self.y, 100, 100)
        self.note = pygame.image.load(config.note_dict[self.color][0])
        #config.screen.blit(self.note, self.rect)

    def update_position(self):
        self.rect.y += self.velocity

def moving_note(note):
    note.update_position()
    config.screen.blit(note.note, note.rect)

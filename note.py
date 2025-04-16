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
        self.hit = False

    def update_position(self):
        self.rect.y += self.velocity

    @staticmethod
    def check(keys, note):
        note_key = config.note_dict[note.color][2]
        if not note.hit and keys[note_key]:
            if note.rect.colliderect(config.chord_rect):
                config.fill_color = (0, 255, 0)
                config.score += 1
                note.hit = True
            else:
                config.fill_color = (255, 0, 0)

    @staticmethod
    def moving_note(note):
        note.update_position()
        config.screen.blit(note.note, note.rect)
import pygame
import config
import note
from note import moving_note


def main():
    running = True
    red_note = note.Note("red", 0)
    while running:
        config.screen.fill((0, 0, 0))
        pygame.draw.rect(config.screen, (0, 0, 255), config.chord_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #target notes
        for n in config.target_notes:
            config.screen.blit(n.note, n.rect)

        moving_note(red_note)

        pygame.display.flip()

main()
import pygame
import config
import note

def main():
    pygame.init()
    notes = []
    start_time = pygame.time.get_ticks()
    note_index = 0
    running = True
    while running:
        config.screen.fill(config.fill_color)
        pygame.draw.rect(config.screen, (0, 0, 255), config.chord_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if config.fill_color != (0, 0, 0):
            config.color_timer -= 1
            if config.color_timer <= 0:
                config.fill_color = (0, 0, 0)
                config.color_timer = 50

        #target notes
        for n in config.target_notes:
            config.screen.blit(n.note, n.rect)

        #falling notes
        #for n in config.notes:
        #    note.Note.moving_note(n)
        keys = pygame.key.get_pressed()
        #config.notes[0].check(keys, config.notes[0])

        current_time = pygame.time.get_ticks() - start_time

        if note_index < len(config.note_chart) and current_time >= config.note_chart[note_index][0]:
            color = config.note_chart[note_index][1]
            notes.append(note.Note(color, 0))
            note_index += 1

        for n in notes:
            n.moving_note(n)

        for n in notes:
            if not n.hit:
                n.update_position()
                note.Note.check(keys, n)

        pygame.display.flip()

main()
import pygame
import random

def draw_grid(screen):
    for x in range(0, 640, 32):
        pygame.draw.line(screen, (0, 0, 255), (x, 0), (x, 512))
    for y in range(0, 512, 32):
        pygame.draw.line(screen, (255, 165, 0), (0, y), (640, y))
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()

        x, y = 0, 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click_x, click_y = event.pos
                    if x <= click_x <= x + 32 and y <= click_y <= y + 32:
                        x = random.randrange(0, 640, 32)
                        y = random.randrange(0, 512, 32)
                        



            screen.fill("light green")
            draw_grid(screen)

            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
            pygame.display.flip()
            clock.tick(60)


    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

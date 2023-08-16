import pygame


def main():
    width = 800
    height = 600
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    running = True

    delta_time = 0
    player_pos = pygame.Vector2(width / 2, height / 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("purple")

        pygame.draw.circle(screen, "red", player_pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * delta_time
        if keys[pygame.K_s]:
            player_pos.y += 300 * delta_time
        if keys[pygame.K_a]:
            player_pos.x -= 300 * delta_time
        if keys[pygame.K_d]:
            player_pos.x += 300 * delta_time

        pygame.display.flip()
        delta_time = clock.tick(60) / 1000

    pygame.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

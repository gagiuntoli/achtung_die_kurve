import pygame

from constants import WHITE, BLACK, RED, GREEN, FPS, MINIMUM_PLAYERS, MAXIMUM_PLAYERS

class menu:
    def show_players_counter(screen, clock, font):
        players = 2
        running = True

        while running:
            screen.fill(BLACK)
            img = font.render('Select the number of players: Up/Down + Enter ', True, RED)
            screen.blit(img, (200, 350))
            img = font.render('Players: ', True, RED)
            screen.blit(img, (400, 400))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        running = False
                    elif event.key == pygame.K_UP and players < MAXIMUM_PLAYERS:
                        players += 1
                    elif event.key == pygame.K_DOWN and players > MINIMUM_PLAYERS:
                        players -= 1

            img = font.render(str(players), True, RED)
            screen.blit(img, (600, 400))

            pygame.display.flip()
            clock.tick(FPS)
            
        screen.fill(BLACK)

        return players

    def show_winner(screen, clock, winner, font):
        pygame.draw.rect(screen, (GREEN), (250, 300, 600, 200))
        screen.blit(font.render('Player '+ str(winner) + ' Won!', True, RED), (300, 380))
        
        img = font.render('Do you want to play again? Y/N', True, RED)
        screen.blit(img, (300, 420))

        pygame.display.flip()

        running = True
        answer = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        answer = False
                        running = False
                    elif event.key == pygame.K_y:
                        answer = True
                        running = False

            clock.tick(FPS)

        screen.fill(BLACK)

        return answer

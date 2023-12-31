import pygame

from quad_tree import quad_tree

from physics import \
    init_random_velocities, \
    init_random_positions, \
    init_actives, \
    update_position, \
    update_velocity

from constants import \
    LINE_WIDTH, \
    FPS, \
    HEIGHT, \
    WIDTH, \
    SPEED, \
    ROTATION_SPEED, \
    DELTA_TIME, \
    ROTATION_KEYS, \
    PLAYERS_COLORS, \
    CONTACT_RADIUS, \
    SPACE_INTERVAL, \
    SPACE_WIDTH

from menu import menu

def compute_new_positions_and_velocities(positions, velocities, actives):
    keys = pygame.key.get_pressed()

    new_positions = []
    new_velocities = []

    for player in range(len(positions)):
        [cw_key, acw_key] = ROTATION_KEYS[player]

        direction = None
        if keys[cw_key]:
            direction = True
        elif keys[acw_key]:
            direction = False
        
        new_positions.append(update_position(positions[player], velocities[player], DELTA_TIME))

        if actives[player]:
            if direction != None:
                new_velocities.append(update_velocity(velocities[player], direction, ROTATION_SPEED, DELTA_TIME))
            else:
                new_velocities.append(velocities[player])
        else:
            new_velocities.append([0.0, 0.0])

    return new_positions, new_velocities, actives

def check_winner(actives):
    if actives.count(True) == 1:
        for player in range(len(actives)):
            if actives[player]:
                return player
    return None

def draw_new_paths(screen, old_positions, new_positions):
    for player in range(len(old_positions)):
        pygame.draw.line(screen, PLAYERS_COLORS[player], old_positions[player], new_positions[player], LINE_WIDTH)

def has_crashed(position, visited_tree: quad_tree, radius):
    [x, y] = position
    return x < 0 or y < 0 or x > WIDTH or y > HEIGHT or visited_tree.check_collision(position, radius)

def update_actives(positions, visited_tree: quad_tree, radius, actives):
    for player in range(len(positions)):
        if actives[player] == True and has_crashed(positions[player], visited_tree, radius):
            actives[player] = False
    return actives

def updated_visited_tree(visited_tree: quad_tree, positions):
    for player in range(len(positions)):
        visited_tree.insert_point(positions[player])
    return visited_tree

def run_game(positions, velocities, actives, visited_tree: quad_tree):
    distance = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

        new_positions, velocities, actives = compute_new_positions_and_velocities(positions, velocities, actives)

        if (distance % SPACE_INTERVAL) < SPACE_INTERVAL - SPACE_WIDTH:
            visited_tree = updated_visited_tree(visited_tree, positions)
            draw_new_paths(screen, positions, new_positions)
            actives = update_actives(new_positions, visited_tree, CONTACT_RADIUS, actives)

        positions = new_positions

        winner = check_winner(actives)
        if winner != None:
            return winner, distance

        distance += SPEED * DELTA_TIME

        pygame.display.flip()
        clock.tick(FPS)

# Init game
pygame.init()

pygame.display.set_caption("Achtung die Curve!")

font = pygame.font.SysFont('freemono', size=28, bold=True)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

menu_obj = menu(screen, clock, font)

num_of_players = menu_obj.show_players_counter()
if num_of_players == None:
    pygame.quit()
    exit()

players = menu_obj.select_player_names(num_of_players)

while True:
    positions = init_random_positions(WIDTH, HEIGHT, num_of_players)
    velocities = init_random_velocities(num_of_players, SPEED)
    actives = init_actives(num_of_players)

    visited_tree = quad_tree([0, WIDTH, 0, HEIGHT], min(WIDTH, HEIGHT) / 20.0)
    winner, distance = run_game(positions, velocities, actives, visited_tree)

    if winner == None:
        break

    if not menu_obj.show_winner(players[winner], distance):
        break

pygame.quit()

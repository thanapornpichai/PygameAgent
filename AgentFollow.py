import pygame

VELOCITY         = 1
LERP_FACTOR      = 0.05
maximum_distance = 500

# Agent class
class Agent:
    def __init__(self, pos, color, minimum_distance):
        self.pos = pygame.math.Vector2(*pos)
        self.color = color
        self.minimum_distance = minimum_distance
    
    def follow(self, target_pos):
        target_vector = pygame.math.Vector2(*target_pos)
        distance = self.pos.distance_to(target_vector)

        if distance > self.minimum_distance:
            direction_vector = (target_vector - self.pos) / distance
            min_step = max(0, distance - maximum_distance)
            max_step = distance - self.minimum_distance
            step_distance = min_step + (max_step - min_step) * LERP_FACTOR
            self.pos += direction_vector * step_distance

    def draw(self, window):
        pygame.draw.circle(window, self.color, (round(self.pos.x), round(self.pos.y)), 10)

# Initialize
pygame.init()
window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Initialize player
player = (150, 150)

# List of agents with their starting positions, colors, and individual minimum distances
agents = [
    Agent((100, 100), (255, 0, 0), 30),
    Agent((200, 200), (255, 255, 0), 50),
    Agent((300, 300), (0, 255, 0), 40),
    Agent((400, 400), (0, 255, 255), 60),
    Agent((350, 400), (0, 150, 255), 35)
]

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update player's position
    player = pygame.mouse.get_pos()

    # Make all agents follow the player
    for agent in agents:
        agent.follow(player)

    # Clear screen with grey background
    window.fill((128, 128, 128))

    # Draw player and agents
    pygame.draw.circle(window, (0, 0, 255), player, 15)
    for agent in agents:
        agent.draw(window)

    pygame.display.flip()

pygame.quit()
exit()
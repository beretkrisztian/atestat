import pygame, sys

pygame.init()
clock = pygame.time.Clock()

# Window setup
pygame.display.set_caption("Joc Atestat")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Models
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('Animations/idle/idle1.png'))
        self.sprites.append(pygame.image.load('Animations/idle/idle2.png'))
        self.sprites.append(pygame.image.load('Animations/idle/idle3.png'))
        self.sprites.append(pygame.image.load('Animations/idle/idle4.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

        self.pos_x = int(pos_x)
        self.pos_y = int(pos_y)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4

    def animate(self):
        self.is_animating = True

    def update(self):
        # Reset velocity
        self.velX = 0
        self.velY = 0

        # Handle movement
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed

        # Update position
        self.pos_x += self.velX
        self.pos_y += self.velY

        # Update rect position
        self.rect.topleft = (self.pos_x, self.pos_y)

        # Handle animation
        if self.is_animating:
            self.current_sprite += 0.13
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            self.image = self.sprites[int(self.current_sprite)]

moving_sprites = pygame.sprite.Group()
player = Player(100, 100)
moving_sprites.add(player)

# Main game loop
run = True
while run:
    # Drawing
    screen.fill((189, 182, 120))
    moving_sprites.draw(screen)
    moving_sprites.update()
    clock.tick(60)
    pygame.display.flip()

    # Handle animation
    player.animate()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.left_pressed = True
            if event.key == pygame.K_d:
                player.right_pressed = True
            if event.key == pygame.K_w:
                player.up_pressed = True
            if event.key == pygame.K_s:
                player.down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.left_pressed = False
            if event.key == pygame.K_d:
                player.right_pressed = False
            if event.key == pygame.K_w:
                player.up_pressed = False
            if event.key == pygame.K_s:
                player.down_pressed = False

pygame.quit()

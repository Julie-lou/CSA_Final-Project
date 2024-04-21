import pygame
import time
import random
pygame.font.init()
# Sizing the window
WIDTH, HEIGHT = 1000,  800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sky Strike")

BG = pygame.transform.scale(pygame.image.load("sky.jpeg"), (WIDTH,HEIGHT))

# Define player
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 50
PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 10
STAR_VEL = 3
FONT = pygame.font.SysFont("Time News Roman", 50)
def draw(player_image,player, elapsed_time, stars):
    WIN.blit(BG, (0,0))
    time_text = FONT.render(f"Time: {round(elapsed_time)}s",1, "white")
    WIN.blit(time_text, (10,10))
    WIN.blit(player_image, (player.x, player.y))
    # pygame.draw.rect(WIN, "cyan", player)
    
    for star in stars:
        pygame.draw.rect(WIN, "white", star)
    
    pygame.display.update()
    
def main():
    run = True
    
    # player = pygame.Rect(200, HEIGHT-PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    
    clock = pygame.time.Clock()
    player_image = pygame.transform.scale(pygame.image.load("realastronaut.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
    player = player_image.get_rect(center=(WIDTH // 2, HEIGHT - PLAYER_HEIGHT // 2))

    
    start_time = time.time()
    elapsed_time = 0
    
    star_add_increment = 2000
    star_count = 0
    
    stars = []
    hit = False
    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT) 
                stars.append(star)
              
            star_add_increment = max(200, star_add_increment-50)  
            star_count = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x- PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL  
            
        if keys[pygame.K_RIGHT] and player.x+ PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
            
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        if hit:
            lost_text = FONT.render("You lost!",2,"white")
            score = FONT.render(f"Your score: {round(elapsed_time)}s",2,"white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            WIN.blit(score, (WIDTH/2 - score.get_width()/2, HEIGHT/3 - score.get_height()/2))

            pygame.display.update()
            pygame.time.delay(4000)
            break 
                   
        draw(player_image, player, elapsed_time, stars)
    pygame.quit()
if __name__ == "__main__":
    main()

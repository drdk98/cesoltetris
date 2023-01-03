import pygame

an, al = 10, 20
TILE= 45
GAME_RES = 800, 600
FPS=60

pygame.init()
game_sc = pygame.display.set_mode(GAME_RES)
clock = pygame.Clock()

#creando la reticula con ancho 10 y altura 20
grid = [pugame.rect(x * TILE, y * TILE, TILE, TILE) for x in range(an) for y in range(al)]

while True:
  game_sc.fill(pygame.Color('black'))
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
    exit()
  
  #dibujando la reticula
  [pygame.draw.rect(game_sc, (40, 40, 40), i_rect, 1) for i_rect in grid]                                           
    
  pygame.display.flip()
  clock.tick(FPS)

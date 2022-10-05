import pygame


Width = 500
Height = 300

FPS = 35
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
running = True 
pygame.font.init()
font = pygame.font.SysFont("Arial", 20)
scoreP1 = 0
scoreP2 = 0
ball = pygame.Rect(Width/2-5,Height/2 - 5,10,10)
player1 = pygame.Rect(Width/2 +230,Height/2 - 30,10,60)
player2 = pygame.Rect(10,Height/2 - 30,10,60)

ballSpeedx = 5
ballSpeedy = 5


while running:
  clock.tick(FPS)
  pygame.display.flip()
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
  
 
  ball.x += ballSpeedx
  ball.y += ballSpeedy
  if ball.top <= 0 or ball.bottom >= Height :
    ballSpeedy *= -1
  if ball.left <= 0:
    ballSpeedx *= -1
    ball.x =Width/2 -5
    ball.y =Height/2 -5
    scoreP1 +=1
  if ball.right >= Width: 
    ballSpeedx *= -1
    ball.x =Width/2 -5
    ball.y =Height/2 -5
    scoreP2 +=1
  if ball.colliderect(player1) or ball.colliderect(player2):
    ballSpeedx *= -1


  if pygame.key.get_pressed()[pygame.K_UP]:
    player1.y -= 5
  if pygame.key.get_pressed()[pygame.K_DOWN]:
    player1.y += 5
  if player1.top <= 0:
    player1.top = 0
  if player1.bottom >= Height:
    player1.bottom = Height 

  if pygame.key.get_pressed()[pygame.K_w]:
    player2.y -= 5
  if pygame.key.get_pressed()[pygame.K_s]:
    player2.y += 5
  if player2.top <= 0:
    player2.top = 0
  if player2.bottom >= Height:
    player2.bottom = Height 
  img1 = font.render(str(scoreP1), True, WHITE)
  img2 = font.render(str(scoreP2), True, WHITE)
  screen.fill(BLACK)
  screen.blit(img2, (Width/2 -25,20))
  screen.blit(img1, (Width/2 +20,20))
  pygame.draw.ellipse(screen,WHITE,ball)
  pygame.draw.rect(screen,WHITE,player1)
  pygame.draw.rect(screen,WHITE,player2)
  pygame.draw.aaline(screen,WHITE,(Width/2,0),(Width/2,Height))

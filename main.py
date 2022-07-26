import pygame
import random
import sys
from pygame.locals import*
#loading pygame
pygame.init()

#displays info onto screen
screen_info=pygame.display.Info()

#setting up the size of the window
size = (width,height)=(int(screen_info.current_w),
int(screen_info.current_h))

screen= pygame.display.set_mode(size)

#Clock 
clock = pygame.time.Clock()

#load fish image
fish_image=pygame.image.load("fish.png")
fish_image=pygame.transform.smoothscale(fish_image,(80,80))
fish_rect=fish_image.get_rect()
fish_rect.center=(width//2,height//2)

#set fish speed and direction
speed = pygame.math.Vector2((0,10))
rotate=random.randint(0,360)
speed.rotate_ip(rotate)
fish_image=pygame.transform.rotate(fish_image,180-rotate)

#Function to move the fish
def move_fish():
  global speed, fish_image
   #get screen info
  screen_info=pygame.display.Info() 
  fish_rect.move_ip(speed)

  #Collision detection
  if fish_rect.left<0 or fish_rect.right>screen_info.current_w:
    speed[0]*=-1
    fish_image=pygame.transform.flip(fish_image,True,False)
    fish_rect.move_ip(speed[0],0)

  if fish_rect.top<0 or fish_rect.bottom>screen_info.current_h:
    speed[1]*=-1
    fish_image=pygame.transform.flip(fish_image,False,True)
    fish_rect.move_ip(speed[1],0)

  
def main():
  #main code
  while True:
    clock.tick(60) #refreshing the page
    #listening for events happening
    for event in pygame.event.get():
      if event.type == QUIT: 
        sys.exit()
    move_fish() #Moves the fish
    screen.fill((0,0,100))  
    screen.blit(fish_image,fish_rect) #Displays the fish
    pygame.display.flip()

if __name__=="__main__":
  main()
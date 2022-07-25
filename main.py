import pygame

#loading pygame
pygame.init()

#displays info onto screen
screen_info=pygame.display.Info()

#setting up the size of the window
size = (width,length)=(int(screen_info.current_w),
int(screen_info.current_h))

screen= pygame.display.set_mode(size)

#Clock 
clock = pygame.time.Clock()

def main():
  #main code
  pass

if __name__=="__main__":
  
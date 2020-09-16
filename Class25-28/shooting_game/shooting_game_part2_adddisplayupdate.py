import pygame,sys #inbuilt module

#Initiate Pygame
pygame.init()

##game goes here##
#first create display surface- the window being displayed for the player
screen=pygame.display.set_mode((980,540)) #specify the width & height of screen in pixels
##A pixel is represented by a dot or square on a computer monitor display screen. Pixels are the basic building blocks of a digital image or display and are created using geometric coordinates.

#Game loop - Updates the display surface & draws on it regularly(literally like while loop)
#check events- events are mostly inputs from a player like pressing a button
while True:
   #to close window on clicking close button-pygame keeps on checking all events until it meets quit event
   for event in pygame.event.get():
       if event.type==pygame.QUIT:
           pygame.quit()#only closes pygame as a module
       #to close pygaame fully
           sys.exit()#closes program fully

    #to continuously update screen
   pygame.display.update()
##problem is update rate for screen is inconsistent-so lets discuss how we can achieve consistent frame rate in next part




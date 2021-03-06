##In last script , we have fixed coordinates in each for loop.Here we will slightly change coordinates of image with each for loop
import pygame,sys #inbuilt module

#Initiate Pygame
pygame.init()
#this will only import image & not display.For display go to screen.blit
wood_bg=pygame.image.load('Wood_BG.png') #import the image and store in its variable.Imported images are always on their surface & needs to be added to a display surface
land_bg=pygame.image.load('Land_BG.png')
water_bg=pygame.image.load('Water_BG.png')
cloud_1=pygame.image.load('Cloud1.png')
cloud_2=pygame.image.load('Cloud2.png')
#to change position of land, create variable with origibal position of land
land_position_y=420
land_speed=1
#to change position of water, create variable with origibal position of water
water_position_y=480
water_speed=1.2
##game goes here##
#first create display surface- the window being displayed for the player
screen=pygame.display.set_mode((980,540)) #specify the width & height of screen in pixels
#to solve the problem of frame rate consistency
clock=pygame.time.Clock()
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

    #Place image on display surface
   #here it is placed on the left side of display surface
   screen.blit(wood_bg,(0,0))
   land_position_y -= land_speed
   if land_position_y<=400 or land_position_y>=450:
     land_speed*=-1
   screen.blit(land_bg,(0,land_position_y))##need to be placed over background image#update coordinates so land moves at the bottom
   water_position_y -= water_speed
   if water_position_y<=440 or water_position_y>=500:
     water_speed*=-1
   screen.blit(water_bg, (0, water_position_y))
   screen.blit(cloud_1, (10, 80))
   screen.blit(cloud_2, (120, 80))
   screen.blit(cloud_1, (350, 50))
   screen.blit(cloud_2, (520, 40))
   screen.blit(cloud_1, (720, 50))

    #to continuously update screen
   pygame.display.update()
   clock.tick(120)#this fixes framerate and hence speed of display update





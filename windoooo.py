import pygame

pygame.init()

screen=pygame.display.set_mode((400,500))

while True:
    
    for event in pygame.display.get():
        
        if event.type==pygame.QUIT:
            
            pygame.quit()
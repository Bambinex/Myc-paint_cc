import pygame

pygame.init()

screen = pygame.display.set_mode((800,800))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mouse.get_pos()
            pygame.mouse.get_rel()
            screen.set_at(pygame.mouse.get_pos(), Color(255,255,255))
    pygame.display.flip()
        
            
        
    
    

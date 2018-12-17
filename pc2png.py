import pygame
import sys
import math

# local:
import coloring
import style
import cloud as cloudd

def preview(cloud, win_width, win_height, function=None, *args):

    window_main = pygame.display.set_mode([win_width, win_height])
    window_main.fill([0,0,0])
    pygame.display.flip()

    # main loop
    running = True
    while running:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False

        window_main.fill([0,0,0])
        for p in cloud.points:
            s = style.square(p, cloud)
            window_main.blit(s, cloudd.get_pos(p))
        pygame.display.flip()

        if function != None:
            function(*args)

        # pygame.image.save(window_main, "output/"+str(i)+".png")
        # i += 1
        

c = cloudd.PointCloud(sys.argv[1])
cloudd.color(c, coloring.DEFAULT_COLORING)
preview(c, 800, 600, cloudd.rotate_cloud, c, 0.3, 2)
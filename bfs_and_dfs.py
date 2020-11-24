import pygame,sys
from random import randint
from pygame.locals import *
from text import text
from node import *
from menu import *

pygame.init()


swidth,sheight=640,360
screen=pygame.display.set_mode((swidth,sheight),0,32)

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREY = (200,200,200)


clear = Button(swidth-150,sheight-300,GREY,"NEW")
start_dfs = Button(swidth-150,sheight-260,GREY,"START DFS")
start_bfs = Button(swidth-150,sheight-220,GREY,"START BFS")
stop = Button(swidth-150,sheight-180,GREY,"STOP")
undo = Button(swidth-150,sheight-140,GREY,"UNDO")

while True:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            check = is_button(x,y)
            
            if check:
                check.action()
                continue
            
            if not is_near(x,y):
                n = Node(x,y)
                n.draw_node(screen)
            else:
                cur_node = is_in(x,y)
                if cur_node:
                    if cur_node.color == BLACK:
                        if len(two_nodes) < 2:
                            cur_node.color = RED
                            two_nodes.append(cur_node)
                            #problem here when a node selected is removed from node list it still has existance in the two_node list
                            if len(two_nodes) == 2:
                                e = Edge(two_nodes)
                                
                    else:
                        cur_node.color = BLACK
                        two_nodes.remove(cur_node)
                        
    draw_all_buttons(screen)
    draw_all_edges(screen)      
    draw_all_nodes(screen)       
    pygame.display.update()

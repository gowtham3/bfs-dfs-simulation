import pygame,sys
from random import randint
from pygame.locals import *
from text import text
from node import *


two_nodes = []
BLACK = (0,0,0)
BLUE = (0,0,255)
class Button:
    width = 120
    height = 30
    all_buttons = []
    
    def __init__(self,x,y,color,text):
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.text_color = BLUE
        Button.all_buttons.append(self)

    def draw_button(self,screen):
        pygame.draw.rect(screen,self.color,Rect((self.x,self.y),(Button.width,Button.height)))
        text(screen,self.text,self.x + 5,self.y + 5,20,self.text_color)

    def action(self):
        if self.text == "NEW":
            clear_everything()
        if self.text == "UNDO":
            undo()

def draw_all_buttons(screen):
    for button in Button.all_buttons:
        button.draw_button(screen)


def undo():
    x = None
    if len(everything)>0:
        x = everything[-1]
        everything.remove(x)
    if x in Edge.all_edges:
        Edge.all_edges.remove(x)
    if x in Node.all_nodes:
        Node.all_nodes.remove(x)
    if x in two_nodes:
        two_nodes.remove(x)
        
def clear_everything():
    for i in range(len(Edge.all_edges)):
        Edge.all_edges.remove(Edge.all_edges[-1])
    for i in range(len(Node.all_nodes)):
        Node.all_nodes.remove(Node.all_nodes[-1])
    for i in range(len(two_nodes)):
        two_nodes.remove(two_nodes[-1])
    for i in range(len(everything)):
        everything.remove(everything[-1])
    
        
def is_button(x,y):
    for button in Button.all_buttons:
        if x > button.x and x < button.x + Button.width and y > button.y and y < button.y + Button.height:
            return button
    return False
        
        

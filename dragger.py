import pygame

from const import *

class Dragger:
    def __init__(self):
        self.piece=None
        self.dragging = False
        self.mouseX=0
        self.mouseY=0
        self.initial_row=0
        self.initial_col=0

    
    def update_blit(self,surface):
        
        if self.piece is not None:
        #texture
         self.piece.set_texture(size=128)
         texture=self.piece.texture
        #image
         img=pygame.image.load(texture)
         if self.dragging:
            surface.blit(self.piece.image, (self.mouseX, self.mouseY))
        #rect
            img_center=(self.mouseX,self.mouseY)
            self.piece.texture_rect=img.get_rect(center=img_center)
            surface.blit(img,self.piece.texture_rect)


    def update_mouse(self,pos):
        if isinstance(pos,tuple) and len(pos)==2:
         self.mouseX,self.mouseY=pos
        else:
           raise ValueError("Invalid pos argument")
    

    def save_initial(self,pos):
        if isinstance(pos,tuple) and len(pos)==2:
         self.inital_row=pos[1]//SQSIZE
         self.initial_col=pos[0]//SQSIZE
        else:
            raise ValueError("Invalid pos argument")
    
    def drag_piece(self,piece):
       if not self.dragging:
            self.piece = piece
            self.dragging = True
       else:
            raise RuntimeError("A piece is already being dragged")
           
    def undrag_piece(self):
        if self.dragging:
           
            self.piece = None
            self.dragging = False
        else:
            raise RuntimeError("No piece is being dragged")
       

        
         
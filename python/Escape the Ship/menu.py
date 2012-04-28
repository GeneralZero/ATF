import pygame
import time

class Menu(object):
    def __init__(self, Game):
        self.Game=Game
        pygame.init()
        self.rect=pygame.Rect(0,0,1350,900)
        self.menuItems = [[pygame.Rect(45,373,447,54), self.start],[pygame.Rect(126,452,447,54), self.controls],[pygame.Rect(219,524,447,54),self.credits],[pygame.Rect(926,687,447,54),self.quit]]
        self.imagelist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.imagelist[0] = pygame.image.load("menu/PNGFRAMES/menuanimated_00.png").convert_alpha()
        self.imagelist[1] = pygame.image.load("menu/PNGFRAMES/menuanimated_01.png").convert_alpha()
        self.imagelist[2] = pygame.image.load("menu/PNGFRAMES/menuanimated_02.png").convert_alpha()
        self.imagelist[3] = pygame.image.load("menu/PNGFRAMES/menuanimated_03.png").convert_alpha()
        self.imagelist[4] = pygame.image.load("menu/PNGFRAMES/menuanimated_04.png").convert_alpha()
        self.imagelist[5] = pygame.image.load("menu/PNGFRAMES/menuanimated_05.png").convert_alpha()
        self.imagelist[6] = pygame.image.load("menu/PNGFRAMES/menuanimated_06.png").convert_alpha()
        self.imagelist[7] = pygame.image.load("menu/PNGFRAMES/menuanimated_07.png").convert_alpha()
        self.imagelist[8] = pygame.image.load("menu/PNGFRAMES/menuanimated_08.png").convert_alpha()
        self.imagelist[9] = pygame.image.load("menu/PNGFRAMES/menuanimated_09.png").convert_alpha()
        self.imagelist[10] = pygame.image.load("menu/PNGFRAMES/menuanimated_10.png").convert_alpha()
        self.imagelist[11] = pygame.image.load("menu/PNGFRAMES/menuanimated_11.png").convert_alpha()
        self.imagelist[12] = pygame.image.load("menu/PNGFRAMES/menuanimated_12.png").convert_alpha()
        self.imagelist[13] = pygame.image.load("menu/PNGFRAMES/menuanimated_13.png").convert_alpha()
        self.imagelist[14] = pygame.image.load("menu/PNGFRAMES/menuanimated_14.png").convert_alpha()
        self.imagelist[15] = pygame.image.load("menu/PNGFRAMES/menuanimated_15.png").convert_alpha()
        self.imagelist[16] = pygame.image.load("menu/PNGFRAMES/menuanimated_16.png").convert_alpha()
        self.imagelist[17] = pygame.image.load("menu/PNGFRAMES/menuanimated_17.png").convert_alpha()
        self.imagelist[18] = pygame.image.load("menu/PNGFRAMES/menuanimated_18.png").convert_alpha()
        self.imagelist[19] = pygame.image.load("menu/PNGFRAMES/menuanimated_19.png").convert_alpha()
        self.imagelist[20] = pygame.image.load("menu/PNGFRAMES/menuanimated_20.png").convert_alpha()
        self.imagelist[21] = pygame.image.load("menu/PNGFRAMES/menuanimated_21.png").convert_alpha()
        self.imagelist[22] = pygame.image.load("menu/PNGFRAMES/menuanimated_22.png").convert_alpha()
        self.imagelist[23] = pygame.image.load("menu/PNGFRAMES/menuanimated_23.png").convert_alpha()
        self.imagelist[24] = pygame.image.load("menu/PNGFRAMES/menuanimated_24.png").convert_alpha()
        self.imagelist[25] = pygame.image.load("menu/PNGFRAMES/menuanimated_25.png").convert_alpha()
        self.imagelist[26] = pygame.image.load("menu/PNGFRAMES/menuanimated_26.png").convert_alpha()
        self.imagelist[27] = pygame.image.load("menu/PNGFRAMES/menuanimated_27.png").convert_alpha()
        self.imagelist[28] = pygame.image.load("menu/PNGFRAMES/menuanimated_28.png").convert_alpha()
        self.imagelist[29] = pygame.image.load("menu/PNGFRAMES/menuanimated_29.png").convert_alpha()
        self.imagelist[30] = pygame.image.load("menu/PNGFRAMES/menuanimated_30.png").convert_alpha()
        self.imagelist[31] = pygame.image.load("menu/PNGFRAMES/menuanimated_31.png").convert_alpha()
        self.imagelist[32] = pygame.image.load("menu/PNGFRAMES/menuanimated_32.png").convert_alpha()
        self.imagelist[33] = pygame.image.load("menu/PNGFRAMES/menuanimated_33.png").convert_alpha()

        self.list = self.imagelist[0]
        self.frame = 0
        self.animation_rate = 10
        self.animation_counter = 0
        
        self.music_menu = pygame.mixer.music.load("Music/truthofthelegend.ogg")
        self.music_menuPlay = pygame.mixer.music.play(-1)
        
        #event.mouse = pygame.mouse.get_pos()

        
    def update(self):
        self.Game.screen.blit(self.list, self.rect)
        pygame.display.flip()
        self.music_menuPlay
        self.animation_counter+=1
        if self.animation_counter>self.animation_rate:
            self.animation_counter=0
            self.frame+=1
            if self.frame>33:
                self.frame=0
        self.list = self.imagelist[self.frame]
    
    def process_input(self):
        events=pygame.event.get()
        #print pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.Game.game_over = True
                if event.key == pygame.K_TAB:
                    pygame.mixer.music.fadeout(2000)
                    time.sleep(1)
                    self.Game.game_menu = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for (rect, action) in self.menuItems:
                        if rect.collidepoint(event.pos):
                            action()
                    
                #print "pos:", event.pos
                
                    

            #elif event.type == pygame.MOUSEBUTTONDOWN:
            
               # if pygame.mouse.get_pos() > ((110, 320)) and pygame.mouse.get_pos() < ((400, 375)) :
                  #  self.Game.game_menu == False
                #if event.mouse > ((190, 395)) and event.mouse < ((468, 445)) 
                #	self.Game.game_credits == True
                #if event.mouse > ((273, 465)) and event.mouse < ((
                
    def main_menu(self):
        self.Game.game_menu = True
    def start(self):
        self.imageloadinglist = [0,0,0,0]
        self.imageloadinglist[0] = pygame.image.load("menu/loading0.png").convert_alpha()
        self.imageloadinglist[1] = pygame.image.load("menu/loading1.png").convert_alpha()
        self.imageloadinglist[2] = pygame.image.load("menu/loading2.png").convert_alpha()
        self.imageloadinglist[3] = pygame.image.load("menu/loading3.png").convert_alpha()
        anime_count = 0
        anime_rate = 40
        anime_frame = 0
        anime_exit = 0
        while self.Game.game_menu == True:
            anime_count+= 1
            if anime_count ==1 and anime_exit == 0:
                pygame.mixer.music.fadeout(3000)
            if anime_count>anime_rate:
                anime_count=0
                anime_frame+=1
                if anime_frame !=4:
                    self.update()
                    self.Game.screen.blit(self.imageloadinglist[anime_frame],self.rect)
                if anime_frame>3:
                    anime_frame=0
                    anime_exit+= 1
                    if anime_exit == 6:
                        break
            pygame.display.flip()
        pygame.mixer.music.fadeout(3000)
        time.sleep(3)
        self.Game.game_menu = False
    def controls(self):
        self.controlImage = pygame.image.load("menu/controlmenu.png").convert_alpha()
        self.controlItems = [[pygame.Rect(866,635,447,53),self.main_menu]]
        self.Game.screen.blit(self.controlImage,self.rect)
        pygame.display.flip()
        while 1:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for (rect, action) in self.controlItems:
                            if rect.collidepoint(event.pos):
                                action()
                        return
            #if event.type == pygame.KEYDOWN:
 
        
    def credits(self):
        self.imagetofade1 = pygame.image.load("menu/credit1.png").convert()
        self.imagetofade1.set_alpha(None)
         #Credit Tile One
        i = 255
        while i>0:
            i-=1
            self.imagetofade1.set_alpha(i)
            self.Game.screen.fill((0,0,0))
            self.Game.screen.blit(self.imagetofade1, self.rect)
            pygame.display.flip()
            pygame.time.wait(17)
            
        #Credit Tile 2
        self.imagetofade2 = pygame.image.load("menu/credit2.png").convert()
        self.imagetofade2.set_alpha(None)
        i = 255
        while i>0:
            i-=1
            self.imagetofade2.set_alpha(i)
            self.Game.screen.fill((0,0,0))
            self.Game.screen.blit(self.imagetofade2, self.rect)
            pygame.display.flip()
            pygame.time.wait(17)   

        #Credit Tile 3
        self.imagetofade3 = pygame.image.load("menu/credit3.png").convert()
        self.imagetofade3.set_alpha(None)
        i = 255
        while i>0:
            i-=1
            self.imagetofade3.set_alpha(i)
            self.Game.screen.fill((0,0,0))
            self.Game.screen.blit(self.imagetofade3, self.rect)
            pygame.display.flip()
            pygame.time.wait(17)        
        
        self.imagetofade4 = pygame.image.load("menu/credit4.png").convert()
        self.imagetofade4.set_alpha(None)
        i = 255
        while i>0:
            i-=1
            self.imagetofade4.set_alpha(i)
            self.Game.screen.fill((0,0,0))
            self.Game.screen.blit(self.imagetofade4, self.rect)
            pygame.display.flip()
            pygame.time.wait(17)
        
        self.imagetofade5 = pygame.image.load("menu/credit5.png").convert()
        self.imagetofade5.set_alpha(None)
        i = 255
        while i>0:
            i-=1
            self.imagetofade5.set_alpha(i)
            self.Game.screen.fill((0,0,0))
            self.Game.screen.blit(self.imagetofade5, self.rect)
            pygame.display.flip()
            pygame.time.wait(17)        
        
        
        self.imagetofade6 = pygame.image.load("menu/credit6.png").convert()
        self.imagetofade6.set_alpha(None)
        i = 255
        while i>0:
            i-=1
            self.imagetofade6.set_alpha(i)
            self.Game.screen.fill((0,0,0))
            self.Game.screen.blit(self.imagetofade6, self.rect)
            pygame.display.flip()
            pygame.time.wait(17)        
        
        
        self.imagetofade7 = pygame.image.load("menu/credit7.png").convert()
        self.imagetofade7.set_alpha(None)
        i = 255
        while i>0:
            i-=1
            self.imagetofade7.set_alpha(i)
            self.Game.screen.fill((0,0,0))
            self.Game.screen.blit(self.imagetofade7, self.rect)
            pygame.display.flip()
            pygame.time.wait(17)
                
  
            
    def quit(self):
        self.Game.game_over = True
        
        
                
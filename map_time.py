## This code use pygame 
import pygame # Import pygame graphics library
import wireframe_map
import os # for OS calls

import RPi.GPIO as GPIO
import subprocess
import logging
import sys
import time
import math
import random
import pygame.mixer
from pygame.locals import* # for event mouse variables


class ProjectionViewer:
    #""" Displays 3D objects on a Pygame screen """

    def __init__(self, width, height):
        #self.ball = pygame.image.load("magic_ball.png") # load ball imige
        #self.ballrect = self.ball.get_rect(center=(150, 230))
        self.ballx = 150
        self.bally = 230
        self.ballr = 5;
        self.time_del = 0.25
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Wireframe Display')
        self.background = (0,0,0)
        self.ballcolor = (5,100,100)

        self.wireframes = {}
        self.displayNodes = True
        self.displayEdges = True
        self.nodeColour = (255,255,255)
        self.edgeColour = (200,200,200)
        self.StartEndColor = (255,10,10) 
        self.nodeRadius = 4

    def addWireframe(self, name, wireframe):
        #""" Add a named wireframe object. """

        self.wireframes[name] = wireframe
        
    def detect(self, name):
        if (self.ballx >= self.wireframes[name].nodes[0].x and self.ballx <= self.wireframes[name].nodes[1].x):
            if (self.bally >= self.wireframes[name].nodes[0].y and self.bally <= self.wireframes[name].nodes[3].y):
                return True
        return False

    def run(self):
        #""" Create a pygame screen until it is closed. """

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
            self.display()  
            pygame.display.flip()
            
    def display_progress(self):

        #self.screen.fill(self.background)
        self.screen.fill(self.background)
        for wireframe in self.wireframes.values():
            
            if self.displayNodes:
                poly_4edge=[]
                for node in wireframe.nodes:
                    poly_4edge.append([node.x,node.y])
                pygame.draw.polygon(self.screen, self.nodeColour, poly_4edge, 0)
            pygame.draw.polygon(self.screen, self.nodeColour, [[20,210],[300,210],[300,220],[20,220]], 1)

        
        
    def display(self):
        #""" Draw the wireframes on the screen. """
        self.ballx = self.ballx + vx * self.time_del
        self.bally = self.bally + vy * self.time_del
        #self.ballrect = self.ballrect.move([vx,vy]) 
        self.screen.fill(self.background)
        
        for wireframe in self.wireframes.values():

            if self.displayNodes:
                poly_4edge=[]
                for node in wireframe.nodes:
                    poly_4edge.append([node.x,node.y])
                    #pygame.draw.circle(self.screen, self.nodeColour, (int(node.x), int(node.y)), self.nodeRadius, 0)
                pygame.draw.polygon(self.screen, self.nodeColour, poly_4edge, 0)
        pygame.draw.polygon(self.screen, self.StartEndColor, [[140,0],[140,20],[180,20],[180,0]], 0)
        pygame.draw.polygon(self.screen, self.StartEndColor, [[140,240],[180,240],[180,220],[140,220]], 0)
        

def progress():
    i = 0;
    
    progress_bar = [[25,215],[35,215],[45,215],[55,215],[65,215],[75,215],[85,215],[95,215],[105,215],
                    [115,215],[125,215],[135,215],[145,215],[155,215],[165,215],[175,215],[185,215],[195,215],[205,215],
                    [215,215],[225,215],[235,215],[245,215],[255,215],[265,215],[275,215],[285,215],[295,215]]
    
    progress_show = ProjectionViewer(320, 240)
    progress_node = []
    
    while( i < len(progress_bar) ):
        x = wireframe_map.Wireframe(len)  
        progress_node.append(x)


                
        
        progress_node[i].addNodes([(progress_bar[i][0] - 4, progress_bar[i][1] - 4),
                                   (progress_bar[i][0] + 4, progress_bar[i][1] - 4),
                                   (progress_bar[i][0] + 4, progress_bar[i][1] + 4),
                                   (progress_bar[i][0] - 4, progress_bar[i][1] + 4)])
        
        
        progress_show.addWireframe('Progress'+str(i), progress_node[i])
        
        progress_show.display_progress()
        text_surface=my_font_time.render('L o a d i n g . . . ', True, WHITE)
        rect=text_surface.get_rect(center=(160,200))
        screen.blit(text_surface,rect)
        pygame.display.flip()
        time.sleep(0.15)
        i=i+1;
            
    
        

if __name__ == '__main__':
    
    #os.system('sudo rmmod stmpe_ts')
    #os.system('sudo modprobe stmpe_ts')
    
    map_simple = []
    map_medium = []
    map_hard = []
    
    #map1
    map_simple.append([[150,10],[170,10],[150,30],[170,30],[150,150],[170,50],[150,70],
                 [170,70],[130,50],[130,70],[110,50],[110,70],[90,50],[90,70],
                 [70,50],[70,70],[70,90],[90,90],[70,110],[90,110],[70,130],
                 [90,130],[70,150],[90,150],[70,170],[90,170],[110,150],
                 [130,150],[150,150],[170,150],[110,170],[130,170],[150,170],[170,170]
                 ,[150,190],[150,50],[170,190],[150,210],[170,210],[150,230],[170,230]])


    map_simple.append([[150,10], [150,30], [150,50], [150,70], [150,110], [150,130],
                 [150,150], [150,170], [150,190], [150,210], [150,230],[170,10],
                 [170,30], [170,50], [170,70], [170,110], [170,130], [170,150],
                 [170,170], [170,190], [170,210], [170,230],[190,50], [190,70],
                 [190,110], [190,130],[210,50], [210,70],[210,110], [210,130],
                 [210,150], [210,170],[230,50], [230,70],[230,110], [230,130],
                 [230,150], [230,170],[250,50], [250,70],[250,150], [250,170],
                 [270,50], [270,70],[270,90],[270,110], [270,130], [270,150],
                 [270,170],[290,50], [290,70],[290,90],[290,110], [290,130],
                 [290,150], [290,170]])
    map_simple.append([[50,110], [50,130], [50,150], [50,170], [50,190], [50,210], [50,230],
                        [70,110], [70,130], [70,150], [70,170], [70,190], [70,210], [70,230],
                        [90,110], [90,130], [90,210], [90,230],
                        [110,110], [110,130], [110,210], [110,230],
                        [130,10], [130,30], [130,110], [130,130], [130,210], [130,230],
                        [150,10], [150,30], [150,110], [150,130], [150,210], [150,230],
                        [170,10], [170,30], [170,110], [170,130], [170,210], [170,230],
                        [190,10], [190,30], [190,110], [190,130], [190,210], [190,230],
                        [210,10], [210,30], [210,110], [210,130], [210,210], [210,230],
                        [230,10], [230,30], [230,50], [230,70], [230,90], [230,110], [230,130],
                        [250,10], [250,30], [250,50], [250,70], [250,90], [250,110], [250,130]])


    
    map_medium.append([[150,230],[150,10],[170,30],[170,10],[190,30],[210,30],[230,30],[250,30],[270,30],[270,50],[270,70],[250,70],[250,90]
            ,[270,90],[70,110],[90,110],[110,110],[130,110],[150,110],[170,110],[190,110],[210,110],[230,110],[250,110]
            ,[270,110],[70,130],[110,170],[110,210],[170,230],[150,210],[130,210],[110,190],[90,170],[70,170],[70,150],[150,10],[170,10]])
    
    #map2
    map_medium.append([[150,170],[150,170],[170,30],[190,30],[210,30],[230,30],[230,50],[250,50],[270,50],[290,50],[290,70],[290,90],[290,110]
            ,[290,130],[290,150],[290,170],[270,170],[250,170],[250,150],[250,130],[250,110],[230,110],[210,110],[210,130]
            ,[210,150],[210,170],[190,170],[170,170],[150,170],[130,170],[130,190],[130,210],[150,210],[150,230],[170,230],[150,10],[170,10]])
    map_medium.append([[70,110], [70,130], [70,150], [70,50], [70,90], [70,70],
                        [90,50], [90,150],[110,90], [110,70], [110,150], [110,170], [110,190], [110,210], [110,110], [110,50],[130,110], [130,210],
                        [150,110], [150,130], [150,10], [150,30], [150,50], [150,210], [150,70], [150,230],[170,10], [170,130], [170,230], [170,70],
                        [190,70], [190,130], [190,90],[210,90], [210,130],[230,90], [230,130], [230,150],[250,70], [250,90], [250,150],[270,70], [270,150],
                        [290,110], [290,130], [290,90], [290,150], [290,70]])
    map_hard.append([[30,70], [30,90], [30,110], [30,130], [30,150], [30,170],
                [50,70], [50,170], [50,190], [50,210], [50,230], 
                [70,50],[70,70], [70,90], [70,110], [70,130], [70,230],
                [90,130], [90,50],[90,150],[90,190], [90,210], [90,230], 
                [110,50],[110,70],[110,190],
                [130,70], [130,110], [130,130], [130,150], [130,170], [130,190],
                [150,10],[150,30],[150,70],[150,150],[150,230],
                [170,10],[170,30],[170,50],[170,70],[170,130],[170,150],[170,210],[170,230],
                [190,110],[190,130],[190,210],
                [210,50],[210,110],[210,170],[210,190],[210,210],
                [230,30],[230,50],[230,110],[230,130],[230,150],[230,170],[230,210],[230,230],
                [250,50],[250,90],[250,110],[250,210],
                [270,50], [270,90], [270,150], [270,170], [270,190], [270,210],
                [290,50], [290,90], [290,150], [290,210],
                [310,50], [310,70], [310,90], [310,150], [310,210]])
    map_hard.append( [[30,70], [30,110], [30,130], [30,150], [30,190], [30,210], [30,230],
                [50,70], [50,110], [50,150], [50,190], [50,230],
                [70,70],[70,90], [70,110],  [70,150], [70,170], [70,190], [70,230],
                [90,230],[90,70],[90,50],[110,50] ,[110,90] ,[110,110] ,[110,130] ,[110,150] ,[110,170] ,[110,190] ,[110,210] ,[110,230] ,
                [130,90] ,[130,50],[150,90] , [150,50] , [150,10] , [150,230] , 
                [170,10] , [170,50],[170,90] , [170,150] , [170,170] , [170,210] , [170,230],[170,130],
                [190,10] , [190,30] , [190,50] , [190,90] , [190,130] , [190,170] , [190,210] ,[210,90] , [210,130] , [210,170] , [210,210] ,
                [230,30] , [230,50] , [230,70] , [230,90] , [230,130] , [230,170] , [230,210] ,
                [310,30] , [310,50] , [310,70] , [310,90] , [310,110], [310,130] , [310,170] ,[310,190], [310,210] ,
                [250,30] , [250,130] , [250,170] , [250,210] ,[270,30] , [270,130] , [270,170] , [270,210] ,
                [290,30] , [290,130] , [290,170] , [290,210]])
    map_hard.append([[10,170], [10,130], [10,150],[30,130], [30,50], [30,70], [30,170],[50,70], [50,170], [50,90], [50,130],
                    [70,130], [70,70], [70,170],[90,50], [90,70], [90,90], [90,130], [90,170],[110,90], [110,130], [110,170], [110,190], [110,210],
                    [130,30], [130,50], [130,90], [130,130], [130,210],[150,10], [150,50], [150,90], [150,130], [150,150], [150,170], [150,210], [150,230],
                    [170,10], [170,50], [170,90], [170,170], [170,230],[190,10], [190,50], [190,150], [190,90], [190,110], [190,130], [190,170], [190,230],
                    [210,10], [210,50], [210,70], [210,90], [210,230], [210,210],[230,10], [230,110], [230,130], [230,190], [230,210], 
                    [250,10], [250,30], [250,50], [250,70], [250,150], [250,130], [250,170], [250,190],[270,10], [270,30], [270,130], [270,170], [270,150],
                    [290,130], [290,30],[310,30], [310,50], [310,70], [310,90], [310,110], [310,130]])
    map_hard.append([[10,110], [10,130], [10,90], [10,70],[30,110], [30,130], [30,50], [30,70],[50,130], [50,90], [50,70],[70,130], [70,90], [70,70],
                     [90,130], [90,70],[110,130], [110,50], [110,70], [110,90],[130,10], [130,130], [130,90],[150,10], [150,50], [150,70], [150,90], [150,130], [150,230],
                     [170,10], [170,70], [170,130], [170,210], [170,230],[190,10], [190,70], [190,90], [190,130], [190,170], [190,210], [190,190],
                     [210,10], [210,50], [210,90], [210,130], [210,190], [210,210], [210,170],[230,10], [230,30], [230,50], [230,90], [230,130], [230,170], [230,190],
                     [250,30], [250,90], [250,130], [250,170], [250,190],[270,30], [270,50], [270,70], [270,90], [270,130], [270,150], [270,190],
                     [290,150], [290,170], [290,190]])
    
    block_len = 10
    
    End = [[150,10],[170,10]]
    Start = [[150,230],[170,230]]
    #print(len(map))
    
    
    
    # PiTFT setup
    os.putenv('SDL_VIDEODRIVER','fbcon') #display on piTFT
    os.putenv('SDL_FBDEV','/dev/fb1') 
    os.putenv('SDL_MOUSEDRV','TSLIB') #track mouse clicks on piTFT
    os.putenv('SDL_MOUSEDEV','/dev/input/touchscreen')
    
    pygame.init()
    pygame.mouse.set_visible(False) # Disappear mouse
    
    pygame.mixer.init(48000, -16, 1, 1024)
    pygame.mixer.music.load('Game-Menu.mp3')
    pygame.mixer.music.play(3)
    
    WHITE=255,255,255 # RGB value of WHITE
    PINK = 200,100,100
    BLACK=0,0,0 # RGB value of BLACK
    BallColor = 5,100,100
    screen=pygame.display.set_mode((320,240))
    my_font_name = pygame.font.Font("/home/pi/project/12_4/Alice.ttf",45)
    my_font_button=pygame.font.Font(None,30)
    my_font_status=pygame.font.Font(None,60)
    my_font_time=pygame.font.Font(None,20)
    my_fng_quit = pygame.font.Font(None,20)
    my_buttons={'Single Map':(80,150),'Unlimit Map':(240,150)}
    my_choices={'Hard':(160, 210),'Medium':(160,160),'Easy':(160,110)}
    
    
    
    
    
    ball_start = pygame.image.load("/home/pi/project/12_4/magic_ball.png") # load ball imige
    ballrect_start = ball_start.get_rect(center=(100, 60))
    screen.blit(ball_start, ballrect_start)
    
    text_surface=my_font_time.render("QUIT", True, WHITE)
    rect=text_surface.get_rect(center=(280,210))
    screen.blit(text_surface,rect)
    
    text_surface=my_font_name.render("R   lling Ball", True, WHITE)
    rect=text_surface.get_rect(center=(172,60))
    screen.blit(text_surface,rect)
    
    pygame.draw.polygon(screen, PINK, [[20,130],[140,130],[140,170],[20,170]], 1)
    pygame.draw.polygon(screen, PINK, [[175,130],[305,130],[305,170],[175,170]], 1)
    
    for my_text,text_pos in my_buttons.items():
        text_surface=my_font_button.render(my_text, True, WHITE)
        rect=text_surface.get_rect(center=text_pos)
        screen.blit(text_surface,rect)
    
    pygame.display.flip()
    
    
    
    
    ###### Sensor initial setup ###########
    from Adafruit_BNO055 import BNO055

    bno = BNO055.BNO055(serial_port='/dev/serial0', rst=18)

    # Enable verbose debug logging if -v is passed as a parameter.
    if len(sys.argv) == 2 and sys.argv[1].lower() == '-v':
        logging.basicConfig(level=logging.DEBUG)

    # Initialize the BNO055 and stop if something went wrong.
    if not bno.begin():
        raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')

    # Print system status and self test result.
    status, self_test, error = bno.get_system_status()
    print('System status: {0}'.format(status))
    print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
    # Print out an error if system status is in error mode.
    if status == 0x01:
        print('System error: {0}'.format(error))
        print('See datasheet section 4.3.59 for the meaning.')
    # Initialize the BNO055 and stop if something went wrong.
    print('Read data, press Ctrl-C to quit...')
    
    
    ####### Flag #######
    
    map_flag = 0 # indicate map index 
    
    Code_Running = True # Detect_quit or 
    Start_flag = False # Flag of Level2 (Ball Collision)
    
    End_flag = 0 # 0: false, 1: Successful + Time, 2: Game Over
    
    TimeLimit = 60;
    
    condition_flag = 1;

    while(Code_Running):
        
        
        ##### Initial Start Interface #####
        if (condition_flag==1):
            
            
    
            screen.fill(BLACK)
            
            
            
            for my_text,text_pos in my_buttons.items():
                text_surface=my_font_button.render(my_text, True, WHITE)
                rect=text_surface.get_rect(center=text_pos)
                screen.blit(text_surface,rect)
            
            ball_start = pygame.image.load("/home/pi/project/12_4/magic_ball.png") # load ball imige
            ballrect_start = ball_start.get_rect(center=(100, 60))
            screen.blit(ball_start, ballrect_start)
            
            text_surface=my_font_time.render("QUIT", True, WHITE)
            rect=text_surface.get_rect(center=(280,210))
            screen.blit(text_surface,rect)
            
            text_surface=my_font_name.render("R   lling Ball", True, WHITE)
            rect=text_surface.get_rect(center=(172,60))
            screen.blit(text_surface,rect)
            
            pygame.draw.polygon(screen, PINK, [[20,130],[140,130],[140,170],[20,170]], 1)
            pygame.draw.polygon(screen, PINK, [[175,130],[305,130],[305,170],[175,170]], 1)
            
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if(event.type is MOUSEBUTTONDOWN):
                    pos=pygame.mouse.get_pos()
                elif(event.type is MOUSEBUTTONUP): # Detect ScreenTouch
                    pos=pygame.mouse.get_pos()
                    x,y=pos
                    # If button 'quit' is pressed -> Quit Code
                    print("Detect")
            
                    print('x:' + str(x))
                    print('y:' + str(y))
                    if x > 260 and  x < 300:
                        if y > 200 and y < 220:
                            print('quit is pressed')
                            Code_Running=False
                       
                
                  
                    # If button 'single map' is pressed -> Enter Level Two (Reverse Flag Start)
                    if x > 20 and  x < 240:
                        if y > 130 and y < 170:
                            condition_flag=2
                        # Record start time
                       
                        
                    # If button 'unlimit map' is pressed -> Enter Level Two (Reverse Flag Start)
                    if x > 175 and  x < 305:
                        if y > 130 and y < 170:
                            condition_flag=4
                            progress()
                            start_time=time.time() # Record start time
                        
         ##### Choose difficulties  condit_flag==2 #####
        if (condition_flag==2):
            screen.fill(BLACK)
            
            for my_text,text_pos in my_choices.items():
                text_surface=my_font_button.render(my_text, True, WHITE)
                rect=text_surface.get_rect(center=text_pos)
                screen.blit(text_surface,rect)
                
            ball_start = pygame.image.load("/home/pi/project/12_4/magic_ball.png") # load ball imige
            ballrect_start = ball_start.get_rect(center=(100, 60))
            screen.blit(ball_start, ballrect_start)
        
            
            text_surface=my_font_name.render("R   lling Ball", True, WHITE)
            rect=text_surface.get_rect(center=(172,60))
            screen.blit(text_surface,rect)
            
            pygame.draw.polygon(screen, PINK, [[130,95],[190,95],[190,125],[130,125]], 1)
            pygame.draw.polygon(screen, PINK, [[115,145],[205,145],[205,175],[115,175]], 1)
            pygame.draw.polygon(screen, PINK, [[130,195],[190,195],[190,225],[130,225]], 1)
    
            pygame.display.flip()
    
            
            for event in pygame.event.get():
                if(event.type is MOUSEBUTTONDOWN):
                    pos=pygame.mouse.get_pos()
                elif(event.type is MOUSEBUTTONUP): # Detect ScreenTouch
                    pos=pygame.mouse.get_pos()
                    x,y=pos
                    
                    
                    # If button 'easy' is pressed -> Quit Code
                    
                    if x > 130 and  x < 190:
                        if y > 95 and y < 125:
                            map_difficulty=1
                            condition_flag=3
                            start_time=time.time() 
                                                                
                    # If button 'medium' is pressed -> Enter Level Two (Reverse Flag Start)
                    
                    if x > 115 and  x < 205:
                        if y > 145 and y < 175:
                            map_difficulty=2
                            condition_flag=3
                            start_time=time.time() # Record start time
                       
                        
                    # If button 'hard' is pressed -> Enter Level Two (Reverse Flag Start)
                    if x > 130 and  x < 190:
                        if y > 195 and y < 225:
                            map_difficulty=3
                            condition_flag=3
                            start_time=time.time() # Record start time
        
        ##### End Interface flag==5######
        if ( condition_flag == 5 ):
             
             screen.fill(BLACK)
             pygame.mixer.music.load('Lose.mp3')
             pygame.mixer.music.play(0)
             
                 
             text_surface=my_font_time.render('You have conquered '+str(int(map_flag-1)) +' maps.', True, WHITE)
             rect=text_surface.get_rect(center=(160,160))
             screen.blit(text_surface,rect)
             
             text_surface=my_font_status.render('Game Over', True, WHITE)
             rect=text_surface.get_rect(center=(160,120))
             screen.blit(text_surface,rect)
                 
             
             pygame.display.flip()
             while(condition_flag == 5):    
                for event in pygame.event.get():
                    if(event.type is MOUSEBUTTONDOWN):
                        pos=pygame.mouse.get_pos()
                    elif(event.type is MOUSEBUTTONUP): # Detect ScreenTouch
                        pos=pygame.mouse.get_pos()
                        x,y=pos
                        print(y)
                     # If button 'quit' is pressed -> Quit Code
                        if y>0 and y<240:
                            #print("hahaah")
                            condition_flag=1
                            pygame.mixer.music.load('Game-Menu.mp3')
                            pygame.mixer.music.play(3)
             map_flag = 0
                       
        ##### End Interface  single map flag==7######
        if ( condition_flag == 7 ):
             
             screen.fill(BLACK)
             pygame.mixer.music.load('Lose.mp3')
             pygame.mixer.music.play(0)
             
             text_surface=my_font_button.render('You fail the game', True, WHITE)
             rect=text_surface.get_rect(center=(160,120))
             screen.blit(text_surface,rect)
                 
             
             pygame.display.flip()
             while(condition_flag == 7):    
                for event in pygame.event.get():
                    if(event.type is MOUSEBUTTONDOWN):
                        pos=pygame.mouse.get_pos()
                    elif(event.type is MOUSEBUTTONUP): # Detect ScreenTouch
                        pos=pygame.mouse.get_pos()
                        x,y=pos
                        print(y)
                     # If button 'quit' is pressed -> Quit Code
                        if y>0 and y<240:
                            
                            condition_flag=1
                            pygame.mixer.music.load('Game-Menu.mp3')
                            pygame.mixer.music.play(3)
             map_flag = 0            


#### success Interface  flag==6 ######
        if ( condition_flag==6 ):
             
             screen.fill(BLACK)
             pygame.mixer.music.load('Win.mp3')
             pygame.mixer.music.play(0)
             text_surface=my_font_status.render('Successful', True, WHITE)
             rect=text_surface.get_rect(center=(160,120))
             screen.blit(text_surface,rect)
             text_surface=my_font_time.render('Time: '+str(TimeUsed)+'s', True, WHITE)
             rect=text_surface.get_rect(center=(160,160))
             screen.blit(text_surface,rect)
                 
           
            
             pygame.display.flip()
                 
             while(condition_flag == 6):    
                for event in pygame.event.get():
                 if(event.type is MOUSEBUTTONDOWN):
                     pos=pygame.mouse.get_pos()
                 elif(event.type is MOUSEBUTTONUP): # Detect ScreenTouch
                     pos=pygame.mouse.get_pos()
                     x,y=pos
                     # If button 'quit' is pressed -> Quit Code
                     if y>0 and y<240:
                        condition_flag=1
                        pygame.mixer.music.load('Game-Menu.mp3')
                        pygame.mixer.music.play(3)
                        
            
        
        #### Play Interface unlimited map###
        if (condition_flag==4):
            pygame.mixer.music.load('Playing.mp3')
            pygame.mixer.music.play(3)
            
            #print(map_flag)
            pv = ProjectionViewer(320, 240)
            if map_flag >=0 and map_flag < 2:
                block_center = map_simple[random.randint(0, len(map_simple)-1)]
                TimeLimit = 60;
                TimeLimitStart =time.time()
            if map_flag >=2 and map_flag < 4:
                block_center = map_medium[random.randint(0, len(map_medium)-1)]
                TimeLimit = 60;
                TimeLimitStart =time.time()
            if map_flag >=4:
                block_center = map_hard[random.randint(0, len(map_hard)-1)]
                TimeLimit = 90;
                TimeLimitStart =time.time()
    
            plane = []
            start_node = []
            end_node = []
    

            for i, center in enumerate(block_center):
                #print(i)
                #print(center)
                x = wireframe_map.Wireframe(len)
                plane.append(x)
                plane[i].addNodes([(center[0] - block_len, center[1] - block_len),
                                   (center[0] + block_len, center[1] - block_len),
                                   (center[0] + block_len, center[1] + block_len),
                                   (center[0] - block_len, center[1] + block_len)])
            for i, center in enumerate(Start):
                x = wireframe_map.Wireframe(len)
                start_node.append(x)
                start_node[i].addNodes([(center[0] - block_len, center[1] - block_len),
                                   (center[0] + block_len, center[1] - block_len),
                                   (center[0] + block_len, center[1] + block_len),
                                   (center[0] - block_len, center[1] + block_len)])
            for i, center in enumerate(End):
                x = wireframe_map.Wireframe(len)
                end_node.append(x)
                end_node[i].addNodes([(center[0] - block_len, center[1] - block_len),
                                   (center[0] + block_len, center[1] - block_len),
                                   (center[0] + block_len, center[1] + block_len),
                                   (center[0] - block_len, center[1] + block_len)])
    
    
            for i, center in enumerate(block_center):
                pv.addWireframe('plane_'+str(i), plane[i])
            for i, center in enumerate(end_node):
                pv.addWireframe('end_'+str(i), end_node[i])
    
        
            while (not (pv.detect('end_0') or pv.detect('end_1')) ):
                TimeLimitNow = time.time()
                heading, roll, pitch = bno.read_euler()
                angle_x = (-roll)/180*math.pi
                if (pitch >= 0):
                    angle_y = (180-pitch)/180*math.pi
                elif (pitch < 0):
                    angle_y = (-180-pitch)/180*math.pi
                vx = -8*angle_x;
                vy = -8*(angle_y);
                
       
                # Print everything out.
                #print('Heading={0:0.2F} Roll={1:0.2F} Pitch={2:0.2F}'.format(heading, roll, pitch))
                
        
                pv.display()
        
                ball_on_board = False
                i = 0;
                #print(len(block_center))
                while ( not ball_on_board and i < len(block_center) ):
                    if(pv.detect('plane_'+str(i))):
                        ball_on_board = True
                    i = i + 1;
                    
                if (ball_on_board):
                    pygame.draw.circle(pv.screen, pv.ballcolor, (int(pv.ballx),int(pv.bally)), pv.ballr, 0)
                else:
                    condition_flag=5;
                    break
                
                
                TimeLimitLeft = float("{0:.1f}".format(TimeLimit - TimeLimitNow + TimeLimitStart))
                if (TimeLimitLeft < 0):
                    condition_flag=5;
                    break
                text_surface=my_font_time.render( 'Time Limit: '+ str( TimeLimitLeft ) + 's', True, WHITE)
                rect=text_surface.get_rect(center=(60,20))
                screen.blit(text_surface,rect)

                pygame.display.flip()
                time.sleep(0.01)
                
            map_flag = map_flag + 1;
            
 #### Play Interface for single map  condition_flag==3###
        if (condition_flag==3):
            progress()
            pygame.mixer.music.load('Playing.mp3')
            pygame.mixer.music.play(3)
    
            #print(map_flag)
            pv = ProjectionViewer(320, 240)
            if map_difficulty==1:
                block_center = map_simple[random.randint(0, len(map_simple)-1)]
                TimeLimit = 60;
                TimeLimitStart =time.time()
            if map_difficulty==2:
                block_center = map_medium[random.randint(0, len(map_medium)-1)]
                TimeLimit = 60;
                TimeLimitStart =time.time()
            if map_difficulty==3:
                #block_center = map_hard[random.randint(0, len(map_hard)-1)]
                block_center = map_hard[random.randint(0, len(map_hard)-1)]
                TimeLimit = 90;
                TimeLimitStart =time.time()
    
            plane = []
            start_node = []
            end_node = []
    

            for i, center in enumerate(block_center):
                #print(i)
                #print(center)
                x = wireframe_map.Wireframe(len)
                plane.append(x)
                plane[i].addNodes([(center[0] - block_len, center[1] - block_len),
                                   (center[0] + block_len, center[1] - block_len),
                                   (center[0] + block_len, center[1] + block_len),
                                   (center[0] - block_len, center[1] + block_len)])
            for i, center in enumerate(Start):
                x = wireframe_map.Wireframe(len)
                start_node.append(x)
                start_node[i].addNodes([(center[0] - block_len, center[1] - block_len),
                                   (center[0] + block_len, center[1] - block_len),
                                   (center[0] + block_len, center[1] + block_len),
                                   (center[0] - block_len, center[1] + block_len)])
            for i, center in enumerate(End):
                x = wireframe_map.Wireframe(len)
                end_node.append(x)
                end_node[i].addNodes([(center[0] - block_len, center[1] - block_len),
                                   (center[0] + block_len, center[1] - block_len),
                                   (center[0] + block_len, center[1] + block_len),
                                   (center[0] - block_len, center[1] + block_len)])
    
    
            for i, center in enumerate(block_center):
                pv.addWireframe('plane_'+str(i), plane[i])
            for i, center in enumerate(end_node):
                pv.addWireframe('end_'+str(i), end_node[i])
    
        
            while (not (pv.detect('end_0') or pv.detect('end_1')) ):
               TimeLimitNow = time.time()
               heading, roll, pitch = bno.read_euler()
               angle_x = (-roll)/180*math.pi
               if (pitch >= 0):
                    angle_y = (180-pitch)/180*math.pi
               elif (pitch < 0):
                    angle_y = (-180-pitch)/180*math.pi
               vx = -8*angle_x;
               vy = -8*(angle_y);
       
                # Print everything out.
                #print('Heading={0:0.2F} Roll={1:0.2F} Pitch={2:0.2F}'.format(heading, roll, pitch))
                
        
               pv.display()
        
               ball_on_board = False
               i = 0;
                #print(len(block_center))
               while ( not ball_on_board and i < len(block_center) ):
                    if(pv.detect('plane_'+str(i))):
                        ball_on_board = True
                    i = i + 1;
                    
               if (ball_on_board):
                    pygame.draw.circle(pv.screen, pv.ballcolor, (int(pv.ballx),int(pv.bally)), pv.ballr, 0)
               else:
                    pv.ballx = 150
                    pv.bally = 230
            
                
               TimeLimitLeft = float("{0:.1f}".format(TimeLimit - TimeLimitNow + TimeLimitStart))
               if (TimeLimitLeft < 0):
                    condition_flag=7;
                    break
                    
               text_surface=my_font_time.render( 'Time Limit: '+ str( TimeLimitLeft ) + 's', True, WHITE)
               rect=text_surface.get_rect(center=(60,20))
               screen.blit(text_surface,rect)

               pygame.display.flip()
               time.sleep(0.01)
                
            if ( pv.detect('end_0') or pv.detect('end_1')):
                condition_flag = 6
                print("Successful")
                now_time = time.time()
                TimeUsed = float("{0:.2f}".format(now_time - start_time))

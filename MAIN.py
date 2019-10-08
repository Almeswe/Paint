import pygame
import sys,os
import random
from tkinter import *
from collections import *

###SAVE/OPEN###
def save_file(matrix):
    global window,NAME
    if NAME == None:
        try:
            os.mkdir(os.getcwd()+"\\PaintWorks")
            print("DIR CREATED")

        except:
            print("DIR ALREADY CREATED")

        window = Tk()
        window.geometry('250x100')
        window.resizable(False, False)

        message = StringVar()
        Label(window, text="Name your file(without expansion):").pack()
        Entry(window, textvariable=message).pack()
        Button(window, text="OK", command=close_window).pack()
        window.mainloop()
        if message.get() != '':
            try:
                file = open("PaintWorks"+"\\"+str(message.get())+".txt",'w')
                NAME = message.get()
                file.write(str(matrix))
                print("FILE SAVED")
            except:
                print("CANT CREATE FILE")

    else:
        file = open("PaintWorks" + "\\" + NAME + '.txt', 'w')
        file.write(str(matrix))
        print("FILE SAVED")

def open_file(screen):
        global NAME,window,MATRIX

        window = Tk()
        window.geometry('250x200')
        window.resizable(False, False)

        filename = StringVar()
        Label(window,text = "All file names:(you can scroll)").pack()
        browse = Text(window,width =20,height =5,wrap = WORD)
        browse.pack()

        i = 1
        for file in os.listdir('PaintWorks'):
            browse.insert(str(float(i)),file+'\n')
            i+=1


        Label(window, text="Name of file:").pack()
        Entry(window, textvariable=filename).pack()
        Button(window, text="OK", command=close_window).pack()
        window.mainloop()
        try:
            file = open('PaintWorks\\'+str(filename.get())+'.txt','r')

            for line in file:
                matrixx = line

            y = 0
            color = []
            one_rgb = ''
            newmatrix = matrix(WINDOW_HEIGHT)

            for symbol in matrixx:
                try:
                    int(symbol)
                    one_rgb += symbol
                except:
                    if symbol == ',':
                        color.append(int(one_rgb))
                        one_rgb = ''

                if len(newmatrix[y]) == WINDOW_WIDTH:
                    y += 1


                if len(color) == 3:
                    newmatrix[y].append(color)
                    color = []

            MATRIX = newmatrix


            for y in range(WINDOW_HEIGHT-1):
                for x in range(WINDOW_WIDTH-1):
                    pygame.draw.rect(screen,MATRIX[y][x], (x, y, 1, 1))
            NAME = filename.get()
        except:
            print("INCORRECT PATH")
###---------###

####TKINTER APP###
def check_color(color):
    if len(color) != 3:
        print("INCORRECT,MUST BE 3 ARGUMENTS")
        return (0,0,0)
    else:
        truecolor = []
        for num in color:
            try:
                if int(num) <= 255 and int(num) >= 0:
                    truecolor.append(int(num))
                else:
                    print("INCORRECT VALUE")
                    return (0,0,0)
            except:
                print("INCORRECT,VALUES MUST BE INTEGER")
                return (0,0,0)
        return truecolor

def check_size(size):
    global BRUSHSIZE
    try:
        if int(size) > 100:
            SIZE = 100
            print("MAX SIZE 100px(FIXED FROM "+str(int(size))+"px)")
            return SIZE
        return int(size)
    except:
        print("SIZE MUST BE INTEGER")
        return BRUSHSIZE

def close_window():
    window.destroy()

def create_window(boolean):
    global window

    window = Tk()
    window.geometry('150x100')
    window.resizable(False,False)

    message = StringVar()
    if boolean:
        Label(window,text = "Put RGB value here:").pack()
    else:
        Label(window,text = "Put size here(pixels):").pack()

    Entry(window, textvariable=message).pack()
    Button(window,text = "OK",command = close_window).pack()
    window.mainloop()

    if boolean:#Color
        digit = ''
        colorRGB = []
        string = message.get()
        string += ','
        for i in string:
            if i != ',':
                digit += i
            else:
                colorRGB.append(digit)
                digit = ''
        return (colorRGB)

    if boolean == False:#BrushSize
        return message.get()
###-----------###

###FUNCTIONS###
def events(window,size,matrix):
    global MOUSE_MOTION,CURRENT_COLOR,WINDOW_WIDTH,WINDOW_HEIGHT,BRUSHSIZE
    global CREATED_COLOR
    global NAME
    color = CURRENT_COLOR

    k = pygame.key.get_pressed()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            save_file(matrix)
            sys.exit()

        if k[pygame.K_x]:
            clear_all(matrix,WINDOW_HEIGHT,WINDOW_WIDTH)
            window.fill((255,255,255))

        if k[pygame.K_s]:
            save_file(matrix)

        if k[pygame.K_o]:
            open_file(window)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                draw(size,window,matrix,color,x,y)
                MOUSE_MOTION = True


                if y in range(WINDOW_HEIGHT-150,WINDOW_HEIGHT-150+50):
                    if x in range(0,50):
                        CURRENT_COLOR = (0,255,0)
                    if x in range(51,100):
                        CURRENT_COLOR = (255,0,0)
                    if x in range(101,150):
                        CURRENT_COLOR = (0,0,255)

                    if x in range(WINDOW_WIDTH-150,WINDOW_WIDTH-150+50):
                        BRUSHSIZE = 1
                    if x in range(WINDOW_WIDTH-150+50,WINDOW_WIDTH-150+100):
                        BRUSHSIZE = 3
                    if x in range(WINDOW_WIDTH-150+100,WINDOW_WIDTH-150+150):
                        BRUSHSIZE = 5


                if y in range(WINDOW_HEIGHT-150+50+1,WINDOW_HEIGHT-150+100):
                    if x in range(0,50):
                        CURRENT_COLOR = (151,54,249)
                    if x in range(51,100):
                        CURRENT_COLOR = (245,243,5)
                    if x in range(101,150):
                        CURRENT_COLOR = (225,52,128)

                    if x in range(WINDOW_WIDTH-150,WINDOW_WIDTH-150+50):
                        BRUSHSIZE = 30
                    if x in range(WINDOW_WIDTH-150+50,WINDOW_WIDTH-150+100):
                        BRUSHSIZE = 20
                    if x in range(WINDOW_WIDTH-150+100,WINDOW_WIDTH-150+150):
                        BRUSHSIZE = 10

                if y in range(WINDOW_HEIGHT-150+101,WINDOW_HEIGHT-150+150):
                    if x in range(0,50):
                        CURRENT_COLOR = (194,202,225)
                    if x in range(51,100):
                        CURRENT_COLOR = (225,144,22)
                    if x in range(101,150):
                        CURRENT_COLOR = CREATED_COLOR

                    if x in range(WINDOW_WIDTH-150,WINDOW_WIDTH-150+50):
                        BRUSHSIZE = check_size(create_window(False))
                    if x in range(WINDOW_WIDTH-150+50,WINDOW_WIDTH-150+100):
                        CURRENT_COLOR = check_color(create_window(True))
                        CREATED_COLOR = CURRENT_COLOR
                    if x in range(WINDOW_WIDTH-150+100,WINDOW_WIDTH-150+150):
                        CURRENT_COLOR = (255,255,255)


            if event.button == 3:
                x,y = event.pos
                color_fill(window,color,matrix[y][x],matrix,x,y)


        if MOUSE_MOTION:
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                draw(size,window,matrix,color,x,y)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                x, y = event.pos
                draw(size,window,matrix,color,x,y)
                MOUSE_MOTION = False



def matrix(w_height):
    matrix = []
    for i in range(w_height):
        matrix.append([])

    return matrix

def redraw_pixels(window,size,matrix,height,width):
    for y in range(height):
        for x in range(width):
            pygame.draw.rect(window,matrix[y][x],(x,y,size,size))

def coloring_matrix(matrix,height,width):
    for y in range(height):
        for x in range(width):
            matrix[y].append([255,255,255])

def clear_all(matrix,height,width):
    for y in range(height):
        for x in range(width):
            matrix[y][x] = [255,255,255]

def draw(size,window,matrix,color,x,y):
    high_size = size//2
    low_size = size-high_size
    if size == 1:
        pygame.draw.rect(window, color, (x, y, 1, 1))
        try:
            matrix[y][x] = [color[0], color[1], color[2]]

        except:
            pass
    else:
        for coord_y in range(y-high_size,y+low_size):
            for coord_x in range(x-high_size,x+low_size):
                pygame.draw.rect(window,color,(coord_x,coord_y,1,1))
                try:
                    matrix[coord_y][coord_x] = [color[0],color[1],color[2]]

                except:
                    pass

def color_fill(window,color,areacolor,matrix,x,y):
    global WINDOW_WIDTH,WINDOW_HEIGHT

    current_queue = deque()
    current_queue.append([x,y])

    if [color[0],color[1],color[2]] != areacolor:
        while current_queue:
            first = current_queue.popleft()

            for current in neighbours(first[0],first[1],WINDOW_WIDTH-1,WINDOW_HEIGHT-1):
                    if matrix[current[1]][current[0]] == [areacolor[0],areacolor[1],areacolor[2]]:
                        if current[1] < WINDOW_HEIGHT-150:
                            pygame.draw.rect(window,color,(current[0],current[1],1,1))
                            matrix[current[1]][current[0]] = [color[0],color[1],color[2]]
                            current_queue.append(current)
                        else:
                            if current[0]>150 and current[0] < WINDOW_WIDTH-150:
                                pygame.draw.rect(window, color, (current[0], current[1], 1, 1))
                                matrix[current[1]][current[0]] = [color[0], color[1], color[2]]
                                current_queue.append(current)

def neighbours(posX,posY,width,height):
    neighbours = []

    if posY - 1 >= 0:
        neighbours.append([posX,posY-1])

    if posY - 1 >= 0 and posX-1 >= 0:
        neighbours.append([posX-1,posY-1])

    if posX-1 >= 0:
        neighbours.append([posX-1,posY])

    if posY + 1 <= height:
        if posX - 1 >= 0:
            neighbours.append([posX-1,posY+1])

    if posY+1 <= height:
            neighbours.append([posX,posY+1])

    if posY+1 <= height:
        if posX+1 <= width:
            neighbours.append([posX+1,posY+1])

    if posX+1 <= width:
        neighbours.append([posX+1,posY])

    if posY-1 >= 0:
        if posX+1 <= width:
            neighbours.append([posX+1,posY-1])

    return neighbours

def color_interface(window,height,created):
    pygame.draw.rect(window,(0,0,0),(0,height-150,150,150),2)
    for y in range(3):
        for x in range(3):
            if y == 0 and x == 0:
                pygame.draw.rect(window,(0,255,0),(x*50,y*50+height-150,50,50))
            if y == 0 and x == 1:
                pygame.draw.rect(window,(255,0,0),(x*50,y*50+height-150,50,50))
            if y == 0 and x == 2:
                pygame.draw.rect(window,(0,0,255),(x*50,y*50+height-150,50,50))

            if y == 1 and x == 0:
                pygame.draw.rect(window,(151,54,249),(x*50,y*50+height-150,50,50))
            if y == 1 and x == 1:
                pygame.draw.rect(window, (245,243,5), (x * 50, y * 50 + height - 150, 50, 50))
            if y == 1 and x == 2:
                pygame.draw.rect(window, (225,52,128), (x * 50, y * 50 + height - 150, 50, 50))

            if y == 2 and x == 0:
                pygame.draw.rect(window, (194,202,225), (x * 50, y * 50 + height - 150, 50, 50))
            if y == 2 and x == 1:
                pygame.draw.rect(window, (225,144,22), (x * 50, y * 50 + height - 150, 50, 50))
            if y == 2 and x == 2:
                pygame.draw.rect(window, created, (x * 50, y * 50 + height - 150, 50, 50))

            pygame.draw.rect(window, (0,0,0), (x * 50, y * 50 + height - 150, 50, 50),1)

def settings_interface(window,width,height):
    for y in range(3):
        for x in range(3):
            pygame.draw.rect(window, (255,255,255), (width-x * 50-50, y * 50 + height - 150, 50, 50))
    pygame.draw.rect(window,(0,0,0),(width-150,height-150,150,150),2)
    textfont = pygame.font.Font(None,35)
    textfont2 = pygame.font.Font(None,30)
    textfont3 = pygame.font.Font(None,22)

    for y in range(3):
        for x in range(3):
            if y == 0 and x == 0:
                window.blit(textfont.render("5px",0,(0,0,0)),(width-x*50-50,y*50+height-150))
            if y == 0 and x == 1:
                window.blit(textfont.render("3px",0,(0,0,0)),(width-x*50-50,y*50+height-150,50,50))
            if y == 0 and x == 2:
                window.blit(textfont.render("1px",0,(0,0,0)),(width-x*50-50,y*50+height-150,50,50))

            if y == 1 and x == 0:
                window.blit(textfont2.render("10px",0,(0,0,0)),(width-x*50-50,y*50+height-150))
            if y == 1 and x == 1:
                window.blit(textfont2.render("20px",0,(0,0,0)),(width-x*50-50,y*50+height-150))
            if y == 1 and x == 2:
                window.blit(textfont2.render("30px",0,(0,0,0)),(width-x*50-50,y*50+height-150))

            if y == 2 and x == 0:
                window.blit(textfont2.render("Blur",0,(0,0,0)),(width-x*50-50,y*50+height-150))
            if y == 2 and x == 1:
                window.blit(textfont3.render("Create",0,(0,0,0)),(width-x*50-50,y*50+height-150))
                window.blit(textfont3.render("Color",0,(0,0,0)),(width-x*50-50,y*65+height-150))
            if y == 2 and x == 2:
                window.blit(textfont3.render("Create",0,(0,0,0)),(width-x*50-50,y*50+height-150))
                window.blit(textfont3.render("Size",0,(0,0,0)),(width-x*50-50,y*65+height-150))

            pygame.draw.rect(window, (0,0,0), (width-x * 50-50, y * 50 + height - 150, 50, 50),1)

def update_window(window):
    global WINDOW_WIDTH,WINDOW_HEIGHT
    lilfont = pygame.font.Font(None,20)
    window.blit(lilfont.render("O-open file",0,(CURRENT_COLOR)),(0,0))
    window.blit(lilfont.render("S-save file",0,(CURRENT_COLOR)),(0,20))

    settings_interface(window,WINDOW_WIDTH,WINDOW_HEIGHT)
    color_interface(window,WINDOW_HEIGHT,CREATED_COLOR)
    pygame.display.update()
###---------###

##CONSTANTS###
WINDOW_WIDTH = 1300
WINDOW_HEIGHT = 800
WINDOW_CAPTION = ("Paint")

BRUSHSIZE = 10
CURRENT_COLOR = (255,0,0)
CREATED_COLOR = (255,255,255)

WHITE_COLOR = (255,255,255)
GREEN_COLOR = (0,255,0)
RED_COLOR = (255,0,0)
BLUE_COLOR = (0,0,255)
BLACK_COLOR = (0,0,0)
YELLOW_COLOR = (245,243,5)
PURPLE_COLOR = (151,54,249)
PINK_COLOR = (225,52,128)
RANDOM_COLOR = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

MATRIX = matrix(WINDOW_HEIGHT)

MOUSE_MOTION = False
NAME = None
###--------###

###MAIN###
def Paint():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_CAPTION)
    window.fill((WHITE_COLOR))

    coloring_matrix(MATRIX, WINDOW_HEIGHT, WINDOW_WIDTH)

    while True:
        events(window,BRUSHSIZE,MATRIX)
        update_window(window)

Paint()

###----###

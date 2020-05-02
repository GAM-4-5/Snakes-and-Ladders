import pygame
import sys
import random
import tkinter

start = tkinter.Tk()
def close_start(): 
    start.destroy()
B = tkinter.Button(start, text ="START", command = close_start)
B.pack()
start.mainloop()

pygame.init()
pygame.font.init()

ekran = pygame.display.set_mode((500, 500))
pygame.display.set_caption ("Snakes & Ladders") #naziv_displaya

pozicije = {1:[25, 475], 2:[75, 475], 3:[125, 475], 4:[175, 475], 5:[225, 475], 6:[275, 475], 7:[325, 475], 8:[375, 475], 9:[425, 475], 10:[475, 475],
            20:[25, 425], 19:[75, 425], 18:[125, 425], 17:[175, 425], 16:[225, 425], 15:[275, 425], 14:[325, 425], 13:[375, 425], 12:[425, 425], 11:[475, 425],
            21:[25, 375], 22:[75, 375], 23:[125, 375], 24:[175, 375], 25:[225, 375], 26:[275, 375], 27:[325, 375], 28:[375, 375], 29:[425, 375], 30:[475, 375],
            40:[25, 325], 39:[75, 325], 38:[125, 325], 37:[175, 325], 36:[225, 325], 35:[275, 325], 34:[325, 325], 33:[375, 325], 32:[425, 325], 31:[475, 325],
            41:[25, 275], 42:[75, 275], 43:[125, 275], 44:[175, 275], 45:[225, 275], 46:[275, 275], 47:[325, 275], 48:[375, 275], 49:[425, 275], 50:[475, 275],
            60:[25, 225], 59:[75, 225], 58:[125, 225], 57:[175, 225], 56:[225, 225], 55:[275, 225], 54:[325, 225], 53:[375, 225], 52:[425, 225], 51:[475, 225],
            61:[25, 175], 62:[75, 175], 63:[125, 175], 64:[175, 175], 65:[225, 175], 66:[275, 175], 67:[325, 175], 68:[375, 175], 69:[425, 175], 70:[475, 175],
            80:[25, 125], 79:[75, 125], 78:[125, 125], 77:[175, 125], 76:[225, 125], 75:[275, 125], 74:[325, 125], 73:[375, 125], 72:[425, 125], 71:[475, 125],
            81:[25, 75], 82:[75, 75], 83:[125, 75], 84:[175, 75], 85:[225, 75], 86:[275, 75], 87:[325, 75], 88:[375, 75], 89:[425, 75], 90:[475, 75],
            100:[25, 25], 99:[75, 25], 98:[125, 25], 97:[175, 25], 96:[225, 25], 95:[275, 25], 94:[325, 25], 93:[375, 25], 92:[425, 25], 91:[475, 25]
    }
     

x = 0
y = 0
blue = (100, 100, 255)
pink = (255, 100, 100)
z = 100
x1 = 30
y1 = 35
for j in range (5): #crta svaki drugi red ploče
    x = 0
    x1 = 30
    for i in range (5):
        pygame.draw.rect (ekran, blue, (x, y, 50, 50))

        font = pygame.font.SysFont('Comic Sans MS', 10)
        img = font.render(str(z), True, (0,0,0))
        ekran.blit(img, (x1, y1)) #piše brojeve polja
        z -= 1
        x1 += 50

        pygame.draw.rect (ekran, pink, (x+50, y, 50, 50))

        font = pygame.font.SysFont('Comic Sans MS', 10)
        img = font.render(str(z), True, (0,0,0))
        ekran.blit(img, (x1, y1)) #piše brojeve polja
        z -= 1
        x1 += 50

        x += 100
    y += 100
    y1 += 100
    z -= 10


y = 50
z = 81
x1 = 30
y1 = 85
for j in range (5): #crta svaki drugi red ploče (počevši od drugog reda)
    x = 0
    x1 = 30
    for i in range (5):
        pygame.draw.rect (ekran, pink, (x, y, 50, 50))

        font = pygame.font.SysFont('Comic Sans MS', 10)
        img = font.render(str(z), True, (0,0,0))
        ekran.blit(img, (x1, y1)) #piše brojeve polja
        z += 1
        x1 += 50

        pygame.draw.rect (ekran, blue, (x+50, y, 50, 50))

        font = pygame.font.SysFont('Comic Sans MS', 10)
        img = font.render(str(z), True, (0,0,0))
        ekran.blit(img, (x1, y1)) #piše brojeve polja
        z += 1
        x1 += 50

        x += 100
    y += 100
    y1 += 100
    z -= 30





brown = (139,69,19)
pygame.draw.line (ekran, brown, (275, 475), (175, 375), 7)
pygame.draw.line (ekran, brown, (25, 425), (125, 325), 7)
pygame.draw.line (ekran, brown, (475, 125), (475, 25), 6)
pygame.draw.line (ekran, brown, (325, 375), (175, 125), 7)
pygame.draw.line (ekran, brown, (75, 225), (75, 75), 6)
pygame.draw.line (ekran, brown, (375, 325), (425, 175), 7)
pygame.draw.line (ekran, brown, (375, 425), (425, 375), 7)
pygame.draw.line (ekran, brown, (325, 125), (275, 25), 7) #crta ljestve (8) na ploči

green = (0, 200, 0)
pygame.draw.lines (ekran, green, False, [(75, 25), (110, 45), (105, 85), (125, 125)], 3)
pygame.draw.circle (ekran, green, (75, 24), 5)
pygame.draw.lines (ekran, green, False, [(375, 125), (285,170), (245, 270), (175,325)], 3)
pygame.draw.circle (ekran, green, (375, 126), 5)
pygame.draw.lines (ekran, green, False, [(125, 425), (170, 440), (195, 465), (225, 475)], 3)
pygame.draw.circle (ekran, green, (125, 424), 5)
pygame.draw.lines (ekran, green, False, [(425, 325), (460, 360), (455, 395), (475, 425)], 3)
pygame.draw.circle (ekran, green, (425, 326), 5)
pygame.draw.lines (ekran, green, False, [(125, 175), (115, 220), (55, 270), (25, 325)], 3)
pygame.draw.circle (ekran, green, (125, 176), 5)
pygame.draw.lines (ekran, green, False, [(325, 275), (340, 315), (315, 380), (325, 425)], 3)
pygame.draw.circle (ekran, green, (325, 275), 5)
pygame.draw.lines (ekran, green, False, [(425, 75), (435, 115), (455, 140), (475, 175)], 3)
pygame.draw.circle (ekran, green, (425, 76), 5)
pygame.draw.lines (ekran, green, False, [(325, 75), (270, 70), (220, 80), (175, 75)], 3)
pygame.draw.circle (ekran, green, (325, 75), 5) #crta zmije (8) na ploči


pygame.display.update()
    
z1 = 0
z2 = 0

while z1 < 101 and z2 < 101:
    
    pygame.time.delay (100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
            
    start = tkinter.Tk()
    def close_start(): 
        start.destroy()

    prvi = random.randint(1, 6)
    drugi = random.randint(1, 6)
    z1 = z1 + prvi
    z2 = z2 + drugi
    B = tkinter.Button(start, text ="PRVI IGRAČ: " + str(prvi) + '  POZICIJA: ' + str(z1) +
                       '\n' + "DRUGI IGRAČ: " + str(drugi) + '  POZICIJA: ' + str(z2), command = close_start)
    B.pack()
    start.mainloop()


    x = 0
    y = 0
    blue = (100, 100, 255)
    pink = (255, 100, 100)
    z = 100
    x1 = 30
    y1 = 35
    for j in range (5): #crta svaki drugi red ploče
        x = 0
        x1 = 30
        for i in range (5):
            pygame.draw.rect (ekran, blue, (x, y, 50, 50))

            font = pygame.font.SysFont('Comic Sans MS', 10)
            img = font.render(str(z), True, (0,0,0))
            ekran.blit(img, (x1, y1)) #piše brojeve polja
            z -= 1
            x1 += 50

            pygame.draw.rect (ekran, pink, (x+50, y, 50, 50))

            font = pygame.font.SysFont('Comic Sans MS', 10)
            img = font.render(str(z), True, (0,0,0))
            ekran.blit(img, (x1, y1)) #piše brojeve polja
            z -= 1
            x1 += 50

            x += 100
        y += 100
        y1 += 100
        z -= 10


    y = 50
    z = 81
    x1 = 30
    y1 = 85
    for j in range (5): #crta svaki drugi red ploče (počevši od drugog reda)
        x = 0
        x1 = 30
        for i in range (5):
            pygame.draw.rect (ekran, pink, (x, y, 50, 50))

            font = pygame.font.SysFont('Comic Sans MS', 10)
            img = font.render(str(z), True, (0,0,0))
            ekran.blit(img, (x1, y1)) #piše brojeve polja
            z += 1
            x1 += 50

            pygame.draw.rect (ekran, blue, (x+50, y, 50, 50))

            font = pygame.font.SysFont('Comic Sans MS', 10)
            img = font.render(str(z), True, (0,0,0))
            ekran.blit(img, (x1, y1)) #piše brojeve polja
            z += 1
            x1 += 50

            x += 100
        y += 100
        y1 += 100
        z -= 30





    brown = (139,69,19)
    pygame.draw.line (ekran, brown, (275, 475), (175, 375), 7)
    pygame.draw.line (ekran, brown, (25, 425), (125, 325), 7)
    pygame.draw.line (ekran, brown, (475, 125), (475, 25), 6)
    pygame.draw.line (ekran, brown, (325, 375), (175, 125), 7)
    pygame.draw.line (ekran, brown, (75, 225), (75, 75), 6)
    pygame.draw.line (ekran, brown, (375, 325), (425, 175), 7)
    pygame.draw.line (ekran, brown, (375, 425), (425, 375), 7)
    pygame.draw.line (ekran, brown, (325, 125), (275, 25), 7) #crta ljestve (8) na ploči

    green = (0, 200, 0)
    pygame.draw.lines (ekran, green, False, [(75, 25), (110, 45), (105, 85), (125, 125)], 3)
    pygame.draw.circle (ekran, green, (75, 24), 5)
    pygame.draw.lines (ekran, green, False, [(375, 125), (285,170), (245, 270), (175,325)], 3)
    pygame.draw.circle (ekran, green, (375, 126), 5)
    pygame.draw.lines (ekran, green, False, [(125, 425), (170, 440), (195, 465), (225, 475)], 3)
    pygame.draw.circle (ekran, green, (125, 424), 5)
    pygame.draw.lines (ekran, green, False, [(425, 325), (460, 360), (455, 395), (475, 425)], 3)
    pygame.draw.circle (ekran, green, (425, 326), 5)
    pygame.draw.lines (ekran, green, False, [(125, 175), (115, 220), (55, 270), (25, 325)], 3)
    pygame.draw.circle (ekran, green, (125, 176), 5)
    pygame.draw.lines (ekran, green, False, [(325, 275), (340, 315), (315, 380), (325, 425)], 3)
    pygame.draw.circle (ekran, green, (325, 275), 5)
    pygame.draw.lines (ekran, green, False, [(425, 75), (435, 115), (455, 140), (475, 175)], 3)
    pygame.draw.circle (ekran, green, (425, 76), 5)
    pygame.draw.lines (ekran, green, False, [(325, 75), (270, 70), (220, 80), (175, 75)], 3)
    pygame.draw.circle (ekran, green, (325, 75), 5) #crta zmije (8) na ploči


    pygame.display.update()

    if z1 == 6:
        pygame.draw.circle (ekran, (0, 0, 0), (pozicije [24]), 15)
        z1 = 24
    elif z1 == 13:
        pygame.draw.circle (ekran, (0, 0, 0), (pozicije [29]), 15)
        z1 = 29
    elif z1 == 20:
        pygame.draw.circle (ekran, (0, 0, 0), (pozicije [38]), 15)
        z1 = 38
    elif z1 == 27:
        pygame.draw.circle (ekran, (0, 0, 0), (pozicije [77]), 15)
        z1 = 77
    elif z1 == 33:
        pygame.draw.circle (ekran, (0, 0, 0), (pozicije [69]), 15)
        z1 = 69
    elif z1 == 59:
        pygame.draw.circle (ekran, (0, 0, 0), (pozicije [82]), 15)
        z1 = 82
    elif z1 == 71:
        pygame.draw.circle (ekran, (0, 0, 0), (pozicije [91]), 15)
        z1 = 91
    elif z1 == 74:
        pygame.draw.circle (ekran, (0, 0, 0), (pozicije [95]), 15)
        z1 = 95

    elif z1 == 18:
        pygame.draw.circle (ekran, (0, 0, 0), (pozicije [5]), 15)
        z1 = 5
    elif z1 == 32:
        pygame.draw.circle (ekran, (0, 0, 0), (pozicije [11]), 15)
        z1 = 11
    elif z1 == 47:
        pygame.draw.circle (ekran, (0, 0, 0), (pozicije [14]), 15)
        z1 = 14
    elif z1 == 63:
        pygame.draw.circle (ekran, (0, 0, 0), (pozicije [40]), 15)
        z1 = 40
    elif z1 == 73:
        pygame.draw.circle (ekran, (0, 0, 0), (pozicije [37]), 15)
        z1 = 37
    elif z1 == 89:
        pygame.draw.circle (ekran, (0, 0, 0), (pozicije [70]), 15)
        z1 = 70
    elif z1 == 87:
        pygame.draw.circle (ekran, (0, 0, 0), (pozicije [84]), 15)
        z1 = 84
    elif z1 == 99:
        pygame.draw.circle (ekran, (0, 0, 0), (pozicije [78]), 15)
        z1 = 78
    else:
        pygame.draw.circle (ekran, (0, 0, 0), (pozicije [z1]), 15) #crta ikonu igrača
    pygame.display.update()



    if z2 == 6:
        pygame.draw.circle (ekran, (255, 255, 255), (pozicije [24]), 15)
        z2 = 24
    elif z2 == 13:
        pygame.draw.circle (ekran, (255, 255, 255), (pozicije [29]), 15)
        z2 = 29
    elif z2 == 20:
        pygame.draw.circle (ekran, (255, 255, 255), (pozicije [38]), 15)
        z2 = 38
    elif z2 == 27:
        pygame.draw.circle (ekran, (255, 255, 255), (pozicije [77]), 15)
        z2 = 77
    elif z2 == 33:
        pygame.draw.circle (ekran, (255, 255, 255), (pozicije [69]), 15)
        z2 = 69
    elif z2 == 59:
        pygame.draw.circle (ekran, (255, 255, 255), (pozicije [82]), 15)
        z2 = 82
    elif z2 == 71:
        pygame.draw.circle (ekran, (255, 255, 255), (pozicije [91]), 15)
        z2 = 91
    elif z2 == 74:
        pygame.draw.circle (ekran, (255, 255, 255), (pozicije [95]), 15)
        z2 = 95

    elif z2 == 18:
        pygame.draw.circle (ekran, (255, 255, 255), (pozicije [5]), 15)
        z2 = 5
    elif z2 == 32:
        pygame.draw.circle (ekran, (255, 255, 255), (pozicije [11]), 15)
        z2 = 11
    elif z2 == 47:
        pygame.draw.circle (ekran, (255, 255, 255), (pozicije [14]), 15)
        z2 = 14
    elif z2 == 63:
        pygame.draw.circle (ekran, (255, 255, 255), (pozicije [40]), 15)
        z2 = 40
    elif z2 == 73:
        pygame.draw.circle (ekran, (255, 255, 255), (pozicije [37]), 15)
        z2 = 37
    elif z2 == 89:
        pygame.draw.circle (ekran, (255, 255, 255), (pozicije [70]), 15)
        z2 = 70
    elif z2 == 87:
        pygame.draw.circle (ekran, (255, 255, 255), (pozicije [84]), 15)
        z2 = 84
    elif z2 == 99:
        pygame.draw.circle (ekran, (255, 255, 255), (pozicije [78]), 15)
        z2 = 78
    else:
        pygame.draw.circle (ekran, (255, 255, 255), (pozicije [z2]), 15) #crta ikonu igrača
    pygame.display.update()

    




pygame.quit()

    



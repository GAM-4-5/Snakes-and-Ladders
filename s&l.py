import pygame
import sys
pygame.init()
pygame.font.init()

ekran = pygame.display.set_mode((500, 500))
pygame.display.set_caption ("Snakes & Ladders") #naziv_displaya

vel = 5

class start_button():
    def __init__ (self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
    def draw (self, ekran, outline):
        pygame.draw.rect (ekran, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
        pygame.draw.rect (ekran, self.color, (self.x,self.y,self.width,self.height), 0)
        if self.text != '':
            font = pygame.font.SysFont ('Comic Sans MS', 60)
            text = font.render (self.text, 1, (0, 0, 0))
            ekran.blit (text, (self.x + int(self.width/2 - text.get_width()/2), self.y + int(self.height/2 - text.get_height()/2)))
    def isOver (self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False



run = True
startButton = start_button ((0, 255, 0), 125, 200, 250, 100, 'START')
while run:
    pygame.time.delay (100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    startButton.draw(ekran, (0,0,0))
    pygame.display.update()
    

    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        if startButton.isOver(pos):
            print ('IGRA JE KRENULA')
            ekran.fill((255,255,255))


    

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

            pygame.draw.circle (ekran, (0, 0, 0), (25, 475), 15) #crta ikonu igrača
            pygame.display.update()

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
            pygame.draw.circle (ekran, (0, 0, 0), (75, 475), 15)
            pygame.draw.circle (ekran, (0, 0, 0), (125, 475), 15)
            pygame.display.update()

    

pygame.quit()

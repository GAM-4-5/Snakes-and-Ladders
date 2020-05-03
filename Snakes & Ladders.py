import pygame
import sys
import random
import tkinter

# pojavljuje se gumb "START" (tkinter) te se pritiskom tog gumba pokreće igra
start = tkinter.Tk()

# definira klasu kojom nestaje prozor gumba (tkinter)
def close_start(): 
    start.destroy()
B = tkinter.Button(start, text ="START", command = close_start)
B.pack()
start.mainloop()

pygame.init()
pygame.font.init()

# postavlja se display (dimenzije i naziv)
ekran = pygame.display.set_mode((500, 500))
pygame.display.set_caption ("Snakes & Ladders")

# koordinate pozicija na koje igrače figurice (krugovi) odlaze nakon osvajanja nekog broja "bacanjem kockice" - konačne pozicije ako igrač stane na dno ljestvi ili glavu zmije
pozicije = {1:[25, 475], 2:[75, 475], 3:[125, 475], 4:[175, 475], 5:[225, 475], 6:[175, 375], 7:[325, 475], 8:[375, 475], 9:[425, 475], 10:[475, 475],
            20:[125, 325], 19:[75, 425], 18:[225, 475], 17:[175, 425], 16:[225, 425], 15:[275, 425], 14:[325, 425], 13:[425, 375], 12:[425, 425], 11:[475, 425],
            21:[25, 375], 22:[75, 375], 23:[125, 375], 24:[175, 375], 25:[225, 375], 26:[275, 375], 27:[175, 125], 28:[375, 375], 29:[425, 375], 30:[475, 375],
            40:[25, 325], 39:[75, 325], 38:[125, 325], 37:[175, 325], 36:[225, 325], 35:[275, 325], 34:[325, 325], 33:[425, 175], 32:[475, 425], 31:[475, 325],
            41:[25, 275], 42:[75, 275], 43:[125, 275], 44:[175, 275], 45:[225, 275], 46:[275, 275], 47:[325, 425], 48:[375, 275], 49:[425, 275], 50:[475, 275],
            60:[25, 225], 59:[75, 75], 58:[125, 225], 57:[175, 225], 56:[225, 225], 55:[275, 225], 54:[325, 225], 53:[375, 225], 52:[425, 225], 51:[475, 225],
            61:[25, 175], 62:[75, 175], 63:[25, 325], 64:[175, 175], 65:[225, 175], 66:[275, 175], 67:[325, 175], 68:[375, 175], 69:[425, 175], 70:[475, 175],
            80:[25, 125], 79:[75, 125], 78:[125, 125], 77:[175, 125], 76:[225, 125], 75:[275, 125], 74:[275, 25], 73:[175, 325], 72:[425, 125], 71:[475, 25],
            81:[25, 75], 82:[75, 75], 83:[125, 75], 84:[175, 75], 85:[225, 75], 86:[275, 75], 87:[175, 75], 88:[375, 75], 89:[475, 175], 90:[475, 75],
            100:[25, 25], 99:[125, 125], 98:[125, 25], 97:[175, 25], 96:[225, 25], 95:[275, 25], 94:[325, 25], 93:[375, 25], 92:[425, 25], 91:[475, 25]
    }

# koordinate središta polja 1 - 100
pozicije2 = {1:[25, 475], 2:[75, 475], 3:[125, 475], 4:[175, 475], 5:[225, 475], 6:[275, 475], 7:[325, 475], 8:[375, 475], 9:[425, 475], 10:[475, 475],
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

# definira se klasa ploče društvene igre (polja, ljestve i zmije)
def ploca():
    x = 0
    y = 0
    blue = (100, 100, 255)
    pink = (255, 100, 100)
    z = 100
    x1 = 30
    y1 = 35
    
    # crta redove ploče (svaki drugi) - naizmjence jedno polje rozo jedno plavo
    for j in range (5): 
        x = 0
        x1 = 30
        for i in range (5):
            pygame.draw.rect (ekran, blue, (x, y, 50, 50))

            font = pygame.font.SysFont('Comic Sans MS', 10)
            img = font.render(str(z), True, (0,0,0))
            ekran.blit(img, (x1, y1)) # piše brojeve polja
            z -= 1
            x1 += 50

            pygame.draw.rect (ekran, pink, (x+50, y, 50, 50))

            font = pygame.font.SysFont('Comic Sans MS', 10)
            img = font.render(str(z), True, (0,0,0))
            ekran.blit(img, (x1, y1)) # piše brojeve polja
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
    # crta redove ploče (svaki drugi, ali počevši od drugog reda) - naizmjence jedno polje rozo jedno plavo
    for j in range (5): 
        x = 0
        x1 = 30
        for i in range (5):
            pygame.draw.rect (ekran, pink, (x, y, 50, 50))

            font = pygame.font.SysFont('Comic Sans MS', 10)
            img = font.render(str(z), True, (0,0,0))
            ekran.blit(img, (x1, y1)) # piše brojeve polja
            z += 1
            x1 += 50

            pygame.draw.rect (ekran, blue, (x+50, y, 50, 50))

            font = pygame.font.SysFont('Comic Sans MS', 10)
            img = font.render(str(z), True, (0,0,0))
            ekran.blit(img, (x1, y1)) # piše brojeve polja
            z += 1
            x1 += 50

            x += 100
        y += 100
        y1 += 100
        z -= 30




    # crta ljestve (8) na ploči
    brown = (139,69,19)
    pygame.draw.line (ekran, brown, (275, 475), (175, 375), 7)
    pygame.draw.line (ekran, brown, (25, 425), (125, 325), 7)
    pygame.draw.line (ekran, brown, (475, 125), (475, 25), 6)
    pygame.draw.line (ekran, brown, (325, 375), (175, 125), 7)
    pygame.draw.line (ekran, brown, (75, 225), (75, 75), 6)
    pygame.draw.line (ekran, brown, (375, 325), (425, 175), 7)
    pygame.draw.line (ekran, brown, (375, 425), (425, 375), 7)
    pygame.draw.line (ekran, brown, (325, 125), (275, 25), 7)

    # crta zmije (8) na ploči
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
    pygame.draw.circle (ekran, green, (325, 75), 5) 

ploca()
pygame.display.update()

# z1 je zbroj brojeva dobivenih bacanjem kockice za prvog igrača, z2 drugog igrača    
z1 = 0
z2 = 0
t = 0
k = 0
while t == 0:
    pygame.time.delay (100)

    # izlazi iz igre ako se stisne x (ne radi!)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit (0)
            exit ()
            t = 1
    
    # prvi (za prvog igrača) i drugi (za drugog igrača) su brojevi generirani randomom (1 - 6) kao brojevi "dobiveni bacanjem kockice"
    prvi = random.randint(1, 6)
    drugi = random.randint(1, 6)

    # z1 i z2 se povećavaju za dobiveni broj
    z1 = z1 + prvi
    z2 = z2 + drugi
    zz = z2-drugi

    # z1 i z2 uvijek moraju biti manji ili jednaki od 100 (tada igra završava), ako su veći onda igrač ostaje na istoj poziciji
    if z1 > 100:
        z1 -= prvi
    if z2 > 100:
        z2 -= drugi
    
    
    # određuje pozicije igrača u slučaju da stanu na polje u kojem je dno ljestvi ili glava zmije
    if z1 == 6:
        poz1 = '6 -> 24'
        z1 = 24
    elif z1 == 13:
        poz1 = '13 -> 29'
        z1 = 29
    elif z1 == 20:
        poz1 = '20 -> 38'
        z1 = 38
    elif z1 == 27:
        poz1 = '27 -> 77'
        z1 = 77
    elif z1 == 33:
        poz1 = '33 -> 69'
        z1 = 69
    elif z1 == 59:
        poz1 = '59 -> 82'
        z1 = 82
    elif z1 == 74:
        poz1 = '74 -> 95'
        z1 = 95
    elif z1 == 71:
        poz1 = '71 -> 91'
        z1 = 91
        
    elif z1 == 18:
        poz1 = '18 -> 5'
        z1 = 5
    elif z1 == 32:
        poz1 = '32 -> 11'
        z1 = 11
    elif z1 == 47:
        poz1 = '47 -> 14'
        z1 = 14
    elif z1 == 73:
        poz1 = '73 -> 37'
        z1 = 37
    elif z1 == 63:
        poz1 = '63 -> 40'
        z1 = 40
    elif z1 == 99:
        poz1 = '99 -> 78'
        z1 = 78
    elif z1 == 87:
        poz1 = '87 -> 84'
        z1 = 84
    elif z1 == 89:
        poz1 = '89 -> 70'
        z1 = 70
    else:
        poz1 = str(z1)




    if z2 == 6:
        poz2 = '6 -> 24'
        z2 = 24
    elif z2 == 13:
        poz2 = '13 -> 29'
        z2 = 29
    elif z2 == 20:
        poz2 = '20 -> 38'
        z2 = 38
    elif z2 == 27:
        poz2 = '27 -> 77'
        z2 = 77
    elif z2 == 33:
        poz2 = '33 -> 69'
        z2 = 69
    elif z2 == 59:
        poz2 = '59 -> 82'
        z2 = 82
    elif z2 == 74:
        poz2 = '74 -> 95'
        z2 = 95
    elif z2 == 71:
        poz2 = '71 -> 91'
        z2 = 91
        
    elif z2 == 18:
        poz2 = '18 -> 5'
        z2 = 5
    elif z2 == 32:
        poz2 = '32 -> 11'
        z2 = 11
    elif z2 == 47:
        poz2 = '47 -> 14'
        z2 = 14
    elif z2 == 73:
        poz2 = '73 -> 37'
        z2 = 37
    elif z2 == 63:
        poz2 = '63 -> 40'
        z2 = 40
    elif z2 == 99:
        poz2 = '99 -> 78'
        z2 = 78
    elif z2 == 87:
        poz2 = '87 -> 84'
        z2 = 84
    elif z2 == 89:
        poz2 = '89 -> 70'
        z2 = 70
    else:
        poz2 = str(z2)

    # pojavljuje se gumb na kojem piše broj koji je dobiven bacanjem kockice i konačna pozicija prvog igrača; pritiskom gumba igrač se pomiče
    start = tkinter.Tk()    
    B = tkinter.Button(start, text ="PRVI IGRAČ: " + str(prvi) + '  POZICIJA: ' + poz1 + '\n' + "(pritisni da bi odigrao/la)", command = close_start)
    B.pack()
    start.mainloop()

    # crta se ploča i pozicije igrača nakon pomaka prvog igrača
    ploca()
    if k == 1:
        pygame.draw.circle (ekran, (255, 255, 255), (pozicije2 [zz]), 15)

    pygame.draw.circle (ekran, (0, 0, 0), (pozicije [z1]), 15)
    pygame.display.update()


    # pojavljuje se gumb na kojem piše broj koji je dobiven bacanjem kockice i konačna pozicija drugog igrača; pritiskom gumba igrač se pomiče
    start = tkinter.Tk()    
    B = tkinter.Button(start, text ="DRUGI IGRAČ: " + str(drugi) + '  POZICIJA: ' + poz2 + '\n' + "(pritisni da bi odigrao/la)", command = close_start)
    B.pack()
    start.mainloop()

    # crta se ploča i pozicije igrača nakon pomaka drugog igrača
    ploca()
    pygame.draw.circle (ekran, (0, 0, 0), (pozicije [z1]), 15)
    pygame.draw.circle (ekran, (255, 255, 255), (pozicije [z2]), 15) 
    pygame.display.update()

    # u trenutku kada prvi ili drugi igrač dostigne polje 100 igra se završava te se pojavljuje prozor s proglašenjem pobjednika; pritiskom na gumb izlazi se iz igre
    if z1 == 100:
        start = tkinter.Tk()    
        B = tkinter.Button(start, text ="POBJEDNIK JE PRVI IGRAČ!" + '\n' + "(pritisni za izlaz iz igre)", command = close_start)
        B.pack()
        start.mainloop()
        t += 1 # završava se while petlja
    if z2 == 100:
        start = tkinter.Tk()    
        B = tkinter.Button(start, text ="POBJEDNIK JE DRUGI IGRAČ!" + '\n' + "(pritisni za izlaz iz igre)", command = close_start)
        B.pack()
        start.mainloop()
        t +=1 # završava se while petlja

    k = 1



pygame.display.quit()
pygame.quit()

    



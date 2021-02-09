"""
--> Spymania 2D SenseHat Game <--
Contribuitori:
David Ghergut
Mihai Pangratie
"""
#Aici importam toate modulele de python de care avem nevoie in tot programul (Here we import all the python modules that we need in the whole program)
from sense_emu import SenseHat
from time import sleep
import collections
#from playsound import playsound
from pygame import *
import threading
#from time import clock

#VARIABILE GLOBALE (GLOBAL VARIABLES):
sense = SenseHat()
is_playable = [0, 0, 0, 0, 0]
#levels = {0:"Storyline", 1:"Level 1", 2:"Level 2", 3:"Level 3", 4:"Level 4", 5:"Level 5 -> Boss Fight"}

#CULORI pentru SenseHat (COLOURS for the SenseHat):
black = [0, 0, 0]
cyan = [0, 255, 255]
blue = [0, 0, 255]
darker_blue = [0, 102, 204]
red = [255, 0, 0]
gold = [255, 215, 0]
green = [0, 255, 0]
white = [255, 255, 255]
purple = [128, 0, 128]
orange = [255, 140, 0]
saddlebrown = [139, 69, 19]
coral = [255, 160, 122]
grey = [58, 59, 60]
toxicgreen = [97, 222, 42]
darkgreen = [0, 100, 0]
pink = [255, 113, 181]
yellow = [255, 255, 0]
darkbrown = [101, 67, 33]

#Aceasta functie va afisa imaginea de sfarsit a tuturor nivelelor (This function will print the ending image for all the levels)
imagine_de_sfarsit_bucata_1 = [
    black, black, black, black, black, black, black, black,
    black, black, black, black, black, black, black, black,
    black, black, blue, cyan, blue, cyan, black, black,
    black, black, cyan, red, gold, blue, black, black,
    black, black, blue, gold, red, cyan, black, black,
    black, black, cyan, blue, cyan, blue, black, black,
    black, black, black, black, black, black, black, black,
    black, black, black, black, black, black, black, black,
]
def afisare_imagine_de_sfarsit_de_nivel_1():
    angles = [0, 90, 180, 270, 0, 90, 180, 270, 0]
    sense.set_pixels(imagine_de_sfarsit_bucata_1)
    for rotation in angles:
        sense.set_rotation(rotation)
        sleep(0.5)
    sense.clear()

#Aceasta functie va afisa a doua imagine de sfarsit a tuturor nivelelor (This function will print the second ending image for all the levels)

imagine_de_sfarsit_bucata_2_etapa_1 = [
    black, black, black, black, black, black, black, black,
    black, blue, blue, black, black, green, green, black,
    black, black, blue, blue, green, green, black, black,
    black, black, black, blue, green, black, black, black,
    black, black, black, red, gold, black, black, black,
    black, black, red, red, gold, gold, black, black,
    black, red, red, black, black, gold, gold, black,
    black, black, black, black, black, black, black, black,
]
imagine_de_sfarsit_bucata_2_etapa_2 = [
    black, black, black, black, black, black, black, black,
    black, blue, blue, black, black, green, green, black,
    black, black, blue, blue, green, green, black, black,
    black, black, black, white, white, black, black, black,
    black, black, black, white, white, black, black, black,
    black, black, red, red, gold, gold, black, black,
    black, red, red, black, black, gold, gold, black,
    black, black, black, black, black, black, black, black,
]
imagine_de_sfarsit_bucata_2_etapa_3 = [
    black, black, black, black, black, black, black, black,
    black, blue, blue, black, black, green, green, black,
    black, black, blue, white, white, green, black, black,
    black, black, white, white, white, white, black, black,
    black, black, white, white, white, white, black, black,
    black, black, red, white, white, gold, black, black,
    black, red, red, black, black, gold, gold, black,
    black, black, black, black, black, black, black, black,
]
imagine_de_sfarsit_bucata_2_etapa_4 = [
    blue, blue, black, black, black, black, green, green,
    black, blue, blue, white, white, green, green, black,
    black, white, white, white, white, white, white, black,
    black, white, white, white, white, white, white, black,
    black, white, white, white, white, white, white, black,
    black, white, white, white, white, white, white, black,
    black, red, red, white, white, gold, gold, black,
    red, red, black, black, black, black, gold, gold,
]
imagine_de_sfarsit_bucata_2_etapa_5 = [
    blue, blue, white, white, white, white, green, green,
    blue, white, white, white, white, white, white, green,
    white, white, white, white, white, white, white, white,
    white, white, white, white, white, white, white, white,
    white, white, white, white, white, white, white, white,
    white, white, white, white, white, white, white, white,
    red, white, white, white, white, white, white, gold,
    red, red, white, white, white, white, gold, gold,
]
imagine_de_sfarsit_bucata_2_etapa_6 = [
    white, white, white, white, white, white, white, white,
    white, white, white, white, white, white, white, white,
    white, white, white, white, white, white, white, white,
    white, white, white, white, white, white, white, white,
    white, white, white, white, white, white, white, white,
    white, white, white, white, white, white, white, white,
    white, white, white, white, white, white, white, white,
    white, white, white, white, white, white, white, white,
]
def afisare_imagine_de_sfarsit_de_nivel_2():
    sense.set_pixels(imagine_de_sfarsit_bucata_2_etapa_1)
    sleep(0.5)
    sense.set_pixels(imagine_de_sfarsit_bucata_2_etapa_2)
    sleep(0.5)
    sense.set_pixels(imagine_de_sfarsit_bucata_2_etapa_3)
    sleep(0.5)
    sense.set_pixels(imagine_de_sfarsit_bucata_2_etapa_4)
    sleep(0.5)
    sense.set_pixels(imagine_de_sfarsit_bucata_2_etapa_5)
    sleep(0.5)
    sense.set_pixels(imagine_de_sfarsit_bucata_2_etapa_6)
    sleep(0.5)
    sense.clear()
    

#IMAGINE PENTRU NIVEL INACCESIBIL (IMAGE FOR AN INACCESIBLE LEVEL)
def locked():
    lock_image = [
        black, black, black, black, black, black, black, black,
        black, red, red, red, red, red, red, black,
        black, red, red, black, black, black, red, black,
        black, red, black, red, black, black, red, black,
        black, red, black, black, red, black, red, black,
        black, red, black, black, black, red, red, black,
        black, red, red, red, red, red, red, black,
        black, black, black, black, black, black, black, black,
    ]
    sense.set_pixels(lock_image)
    sleep(1)
    ENTERING_MAIN_MENU()

#IMAGINE PENTRU NIVEL ACCESIBIL (IMAGE FOR AN ACCESSIBLE LEVEL)
def unlocked():
    unlock_image = [
        black, black, black, black, black, black, black, black,
        black, black, green, green, green, green, black, black,
        black, green, green, green, green, green, green, black,
        black, green, green, green, green, green, green, black,
        black, green, green, green, green, green, green, black,
        black, green, green, green, green, green, green, black,
        black, black, green, green, green, green, black, black,
        black, black, black, black, black, black, black, black,
    ]
    sense.set_pixels(unlock_image)
    sleep(1)
    ENTERING_MAIN_MENU()
    
#FUNCTIE PENTRU STORYLINE (FUNCTION FOR THE STORYLINE)
def storyline_level_1():
    fire1 = [
        black, black, black, black, black, black, black, black,
        black, black, black, black, black, black, black, black,
        black, black, black, red, red, black, black, black,
        black, black, black, red, orange, red, black, black,
        black, black, red, orange, yellow, orange, red, black,
        black, red, orange, yellow, yellow, orange, red, black,
        black, darkbrown, darkbrown, yellow, yellow, darkbrown, darkbrown, black,
        black, black, darkbrown, darkbrown, darkbrown, darkbrown, black, black,
    ]
    fire2 = [
        black, black, black, black, black, black, black, black,
        black, black, black, black, red, black, black, black,
        black, black, black, red, red, red, black, black,
        black, black, black, red, orange, red, black, black,
        black, black, red, orange, yellow, orange, red, black,
        black, red, orange, yellow, yellow, orange, red, black,
        black, darkbrown, darkbrown, yellow, yellow, darkbrown, darkbrown, black,
        black, black, darkbrown, darkbrown, darkbrown, darkbrown, black, black,
    ]
    fire3 = [
        black, black, black, black, black, black, black, black,
        black, black, black, black, black, red, black, black,
        black, black, black, black, red, red, red, black,
        black, black, black, red, orange, orange, red, black,
        black, black, red, orange, yellow, orange, red, black,
        black, red, orange, yellow, yellow, orange, red, black,
        black, darkbrown, darkbrown, yellow, yellow, darkbrown, darkbrown, black,
        black, black, darkbrown, darkbrown, darkbrown, darkbrown, black, black,
    ]
    fire4 = [
        black, black, black, black, black, black, red, black,
        black, black, black, black, black, red, red, black,
        black, black, black, black, red, black, black, black,
        black, black, black, red, orange, red, black, black,
        black, black, red, orange, yellow, orange, red, black,
        black, red, orange, yellow, yellow, orange, red, black,
        black, darkbrown, darkbrown, yellow, yellow, darkbrown, darkbrown, black,
        black, black, darkbrown, darkbrown, darkbrown, darkbrown, black, black,
    ]
    fire5 = [
        black, black, black, black, black, black, red, black,
        black, black, black, black, black, black, black, black,
        black, black, black, red, red, black, black, black,
        black, black, black, red, orange, red, black, black,
        black, black, red, orange, yellow, orange, red, black,
        black, red, orange, yellow, yellow, orange, red, black,
        black, darkbrown, darkbrown, yellow, yellow, darkbrown, darkbrown, black,
        black, black, darkbrown, darkbrown, darkbrown, darkbrown, black, black,
    ]
    """
    #AICI SCRIEM STORYLINE-UL PENTRU PRIMUL NIVEL (HERE WE WRITE THE STORYLINE FOR THE FIRST LEVEL)
    text1 = ""
    storyline1 = text1.split(' ')
    for word in storyline1:
        print(word)
    """
    for i in range(5):
        sense.set_pixels(fire1)
        sleep(0.5)
        sense.set_pixels(fire2)
        sleep(0.5)
        sense.set_pixels(fire3)
        sleep(0.5)
        sense.set_pixels(fire4)
        sleep(0.5)
        sense.set_pixels(fire5)
        sleep(0.5)
    #sleep(5)
    sense.clear()
    #sleep(1)

def storyline_level_2():
    field1 = [
        gold, gold, cyan, white, white, cyan, cyan, cyan,
        gold, cyan, cyan, cyan, cyan, cyan, white, white,
        cyan, white, white, cyan, cyan, cyan, cyan, cyan,
        green, green, green, green, green, green, green, green,
        green, green, green, green, blue, green, green, green,
        green, red, green, green, darkgreen, green, purple, green,
        green, darkgreen, green, green, green, green, darkgreen, green,
        green, green, green, green, green, green, green, green,
    ]
    field2 = [
        gold, gold, cyan, cyan, white, white, cyan, cyan,
        gold, cyan, cyan, cyan, cyan, white, white, cyan,
        cyan, cyan, white, white, cyan, cyan, cyan, cyan,
        green, green, green, green, green, green, green, green,
        green, green, green, green, blue, green, green, green,
        green, red, green, green, darkgreen, green, purple, green,
        green, darkgreen, green, green, green, green, darkgreen, green,
        green, green, green, green, green, green, green, green,
    ]
    field3 = [
        gold, gold, cyan, cyan, cyan, white, white, cyan,
        gold, cyan, cyan, cyan, white, white, cyan, cyan,
        cyan, cyan, cyan, white, white, cyan, cyan, cyan,
        green, green, green, green, green, green, green, green,
        green, green, green, green, blue, green, green, green,
        green, red, green, green, darkgreen, green, purple, green,
        green, darkgreen, green, green, green, green, darkgreen, green,
        green, green, green, green, green, green, green, green,
    ]
    field4 = [
        gold, gold, cyan, cyan, cyan, cyan, white, white,
        gold, cyan, cyan, white, white, cyan, cyan, cyan,
        cyan, cyan, cyan, cyan, white, white, cyan, cyan,
        green, green, green, green, green, green, green, green,
        green, green, green, green, blue, green, green, green,
        green, red, green, green, darkgreen, green, purple, green,
        green, darkgreen, green, green, green, green, darkgreen, green,
        green, green, green, green, green, green, green, green,
    ]
    field5 = [
        gold, gold, cyan, cyan, cyan, cyan, cyan, white,
        gold, cyan, white, white, cyan, cyan, cyan, cyan,
        cyan, cyan, cyan, cyan, cyan, white, white, cyan,
        green, green, green, green, green, green, green, green,
        green, green, green, green, blue, green, green, green,
        green, red, green, green, darkgreen, green, purple, green,
        green, darkgreen, green, green, green, green, darkgreen, green,
        green, green, green, green, green, green, green, green,
    ]
    """
    #AICI SCRIEM STORYLINE-UL PENTRU AL DOILEA NIVEL (HERE WE WRITE THE STORYLINE FOR THE SECOND LEVEL)
    text2 = ""
    storyline2 = text2.split(' ')
    for word in storyline2:
        print(word)
    """
    for i in range(5):
        sense.set_pixels(field1)
        sleep(0.5)
        sense.set_pixels(field2)
        sleep(0.5)
        sense.set_pixels(field3)
        sleep(0.5)
        sense.set_pixels(field4)
        sleep(0.5)
        sense.set_pixels(field5)
        sleep(0.5)
    #sleep(5)
    sense.clear()
    #sleep(1)
    
def storyline_level_3():
    castle1 = [
        black, red, black, black, black, black, red, black,
        red, red, red, black, black, red, red, red,
        grey, black, grey, black, black, grey, black, grey,
        grey, grey, grey, grey, grey, grey, grey, grey,
        grey, grey, grey, grey, grey, grey, grey, grey,
        grey, grey, grey, saddlebrown, saddlebrown, grey, grey, grey,
        grey, grey, grey, saddlebrown, saddlebrown, grey, grey, grey,
        grey, grey, grey, saddlebrown, saddlebrown, grey, grey, grey,
    ]
    castle2 = [
        black, red, black, black, black, black, red, black,
        red, red, red, black, black, red, red, red,
        grey, black, grey, black, black, grey, black, grey,
        grey, grey, grey, grey, grey, grey, grey, grey,
        grey, grey, grey, grey, grey, grey, grey, grey,
        grey, grey, grey, black, black, grey, grey, grey,
        grey, grey, grey, saddlebrown, saddlebrown, grey, grey, grey,
        grey, grey, grey, saddlebrown, saddlebrown, grey, grey, grey,
    ]
    castle3 = [
        black, red, black, black, black, black, red, black,
        red, red, red, black, black, red, red, red,
        grey, black, grey, black, black, grey, black, grey,
        grey, grey, grey, grey, grey, grey, grey, grey,
        grey, grey, grey, grey, grey, grey, grey, grey,
        grey, grey, grey, black, black, grey, grey, grey,
        grey, grey, grey, black, black, grey, grey, grey,
        grey, grey, grey, saddlebrown, saddlebrown, grey, grey, grey,
    ]
    castle4 = [
        black, red, black, black, black, black, red, black,
        red, red, red, black, black, red, red, red,
        grey, black, grey, black, black, grey, black, grey,
        grey, grey, grey, grey, grey, grey, grey, grey,
        grey, grey, grey, grey, grey, grey, grey, grey,
        grey, grey, grey, black, black, grey, grey, grey,
        grey, grey, grey, black, black, grey, grey, grey,
        grey, grey, grey, black, black, grey, grey, grey,
    ]
    castle5 = [
        black, red, black, black, black, black, red, black,
        red, red, red, black, black, red, red, red,
        grey, black, grey, black, black, grey, black, grey,
        grey, red, grey, grey, grey, grey, red, grey,
        red, red, red, grey, grey, red, red, red,
        grey, red, grey, black, black, grey, red, grey,
        grey, grey, grey, black, black, grey, grey, grey,
        grey, grey, grey, black, black, grey, grey, grey,
    ]
    """
    #AICI SCRIEM STORYLINE-UL PENTRU AL TREILEA NIVEL (HERE WE WRITE THE STORYLINE FOR THE THIRD LEVEL)
    text3 = ""
    storyline3 = text3.split(' ')
    for word in storyline3:
        print(word)
    """
    for i in range(5):
        sense.set_pixels(castle1)
        sleep(0.5)
        sense.set_pixels(castle2)
        sleep(0.5)
        sense.set_pixels(castle3)
        sleep(0.5)
        sense.set_pixels(castle4)
        sleep(0.5)
        sense.set_pixels(castle5)
        sleep(0.5)
    #sleep(5)
    sense.clear()
    #sleep(1)

def storyline_level_4_and_5():
    boss1 = [
        red, black, black, black, black, black, black, red,
        red, red, black, black, black, black, red, red,
        black, red, red, red, red, red, red, black,
        black, red, blue, black, black, blue, red, black,
        red, black, gold, blue, blue, gold, black, red,
        red, toxicgreen, black, black, black, black, toxicgreen, red,
        black, toxicgreen, toxicgreen, toxicgreen, toxicgreen, toxicgreen, red, black,
        black, toxicgreen, red, red, red, toxicgreen, black, black,
    ]
    boss2 = [
        red, black, black, black, black, black, black, red,
        red, red, black, black, black, black, red, red,
        black, red, red, red, red, red, red, black,
        black, red, blue, black, black, blue, red, black,
        red, black, gold, blue, blue, gold, black, red,
        red, toxicgreen, black, black, black, black, toxicgreen, red,
        black, red, toxicgreen, toxicgreen, toxicgreen, toxicgreen, red, black,
        black, toxicgreen, red, red, red, red, black, black,
    ]
    boss3 = [
        red, black, black, black, black, black, black, red,
        red, red, black, black, black, black, red, red,
        black, red, red, red, red, red, red, black,
        black, red, blue, black, black, blue, red, black,
        red, black, gold, blue, blue, gold, black, red,
        red, toxicgreen, black, black, black, black, toxicgreen, red,
        black, red, toxicgreen, toxicgreen, toxicgreen, toxicgreen, red, black,
        black, black, red, red, red, red, black, black,
    ]
    boss4 = [
        red, black, black, black, black, black, black, red,
        red, red, black, black, black, black, red, red,
        black, red, red, red, red, red, red, black,
        black, red, blue, black, black, blue, red, black,
        red, black, gold, blue, blue, gold, black, red,
        red, toxicgreen, black, black, black, black, toxicgreen, red,
        black, toxicgreen, toxicgreen, toxicgreen, toxicgreen, toxicgreen, red, black,
        black, black, red, red, red, red, black, black,
    ]
    boss5 = [
        red, black, black, black, black, black, black, red,
        red, red, black, black, black, black, red, red,
        black, red, red, red, red, red, red, black,
        black, red, blue, black, black, blue, red, black,
        red, black, gold, blue, blue, gold, black, red,
        red, toxicgreen, black, black, black, black, toxicgreen, red,
        black, toxicgreen, toxicgreen, toxicgreen, toxicgreen, toxicgreen, red, black,
        black, black, red, red, red, toxicgreen, black, black,
    ]
    """
    #AICI SCRIEM STORYLINE-UL PENTRU AL PATRULEA SI AL CINCILEA NIVEL (HERE WE WRITE THE STORYLINE FOR THE FOURTH AND THE FIFTH LEVEL)
    text4_5 = ""
    storyline4_5 = text4_5.split(' ')
    for word in storyline4_5:
        print(word)
    """
    for i in range(5):
        sense.set_pixels(boss1)
        sleep(0.5)
        sense.set_pixels(boss2)
        sleep(0.5)
        sense.set_pixels(boss3)
        sleep(0.5)
        sense.set_pixels(boss4)
        sleep(0.5)
        sense.set_pixels(boss5)
        sleep(0.5)
    #sleep(5)
    sense.clear()
    #sleep(1)
    
def Storyline():
    storyline_level_1()
    storyline_level_2()
    storyline_level_3()
    storyline_level_4_and_5()
    afisare_imagine_de_sfarsit_de_nivel_1()
    afisare_imagine_de_sfarsit_de_nivel_2()
    is_playable[0] = 1
    ENTERING_MAIN_MENU()

#FUNCTIE DE INTRARE IN MAIN MENU (ENTERING MAIN MENU FUNCTION)

entering_image_1 = [
    black, black, black, saddlebrown, saddlebrown, black, black, black,
    black, black, black, black, black, black, black, black,
    grey, grey, black, black, black, black, purple, purple,
    black, black, black, black, black, black, black, black,
    gold, orange, black, black, black, black, darkbrown, orange,
    black, black, black, black, black, black, black, black,
    red, red, black, black, black, black, cyan, cyan,
    black, black, black, coral, coral, black, black, black,
]

entering_image_2 = [
    black, black, black, saddlebrown, saddlebrown, black, black, black,
    black, black, saddlebrown, blue, blue, saddlebrown, black, black,
    grey, grey, black, black, black, black, purple, purple,
    black, black, black, black, black, black, black, black,
    gold, orange, black, black, black, black, darkbrown, orange,
    black, black, black, black, black, black, black, black,
    red, red, black, black, black, black, cyan, cyan,
    black, black, black, coral, coral, black, black, black,
]

entering_image_3 = [
    black, black, black, saddlebrown, saddlebrown, black, black, black,
    black, black, black, black, black, black, black, black,
    grey, grey, black, blue, blue, black, purple, purple,
    black, black, black, black, black, black, black, black,
    gold, orange, black, black, black, black, darkbrown, orange,
    black, black, black, black, black, black, black, black,
    red, red, black, black, black, black, cyan, cyan,
    black, black, black, coral, coral, black, black, black,
]

reset = [
    black, black, black, saddlebrown, saddlebrown, black, black, black,
    black, black, black, black, black, black, black, black,
    grey, grey, black, black, black, black, purple, purple,
    black, black, black, black, black, black, black, black,
    gold, orange, black, black, black, black, darkbrown, orange,
    black, black, black, black, black, black, black, black,
    red, red, black, black, black, black, cyan, cyan,
    black, black, black, coral, coral, black, black, black,
]
def ENTERING_MAIN_MENU():
    sense.set_pixels(entering_image_1)
    sleep(0.65)
    sense.set_pixels(entering_image_2)
    sleep(0.65)
    sense.set_pixels(entering_image_3)
    
#FUNCTIE DE AFISARE A CONTROALELOR (FUNCTION FOR CONTROLS)

def Controls():
    print("CONTROLS:")
    print("Blue -> Vector (you)")
    print("Brown -> doors that lead to exit")
    print("Purple -> Storyline")
    print("Darkbrown & Orange -> Level 1")
    print("Cyan -> Level 2")
    print("Grey -> Level 3")
    print("Gold & orange -> Level 4")
    print("Red -> Level 5 (Boss fight)")
    ENTERING_MAIN_MENU()

#FUNCTIE PENTRU NIVELUL 1 (LEVEL 1 FUNCTION)

def Level1():
    image_level1 = [
        black, black, black, black, grey, black, red, black,
        black, pink, gold, black, grey, black, red, red,
        black, black, black, black, grey, black, black, black,
        grey, grey, grey, black, black, grey, blue, blue,
        black, gold, blue, black, black, black, black, black,
        black, black, blue, black, black, blue, blue, blue,
        black, gold, blue, black, black, blue, saddlebrown, black,
        grey, black, blue, black, black, blue, black, black,
    ]
    sense.set_pixels(image_level1)
    sleep(5)
    is_playable[1] = 1
    afisare_imagine_de_sfarsit_de_nivel_1()
    afisare_imagine_de_sfarsit_de_nivel_2()
    ENTERING_MAIN_MENU()

#FUNCTIE DE MAIN MENU (MAIN MENU FUNCTION):

def MAIN_MENU():
    sense.show_message("Welcome", text_colour = blue, scroll_speed = 0.05)
    sense.show_message("to", text_colour = gold, scroll_speed = 0.05)
    sense.show_message("Spymania!", text_colour = green, scroll_speed = 0.05)
    sleep(0.5)
    sense.show_message("Press joystick to continue!", text_colour = darker_blue, scroll_speed = 0.05)
    event1 = sense.stick.wait_for_event(emptybuffer = True)
    #ZONA DE SELECTARE A NIVELULUI DE JOC (THE LEVEL SELECTION ZONE)
    if event1.action == "pressed":
        sense.show_message("Choose the level you want to play!", text_colour = coral, scroll_speed = 0.05)
        ok1 = False
        ok2 = False
        pixel1_x = 2
        pixel1_y = 3
        pixel2_x = 2
        pixel2_y = 4
        ENTERING_MAIN_MENU()
        #playsound('/home/pi/Desktop/Spymania/mainmenu.mp3')
        position = 0;
        #INITIALIZAM FISIERUL MP3 PENTRU A FI RULAT
        #mixer.init()
        #mixer.music.load("/home/pi/Desktop/Spymania/mainmenu.mp3")
        #mixer.music.set_volume(0.7)
        #clock = time.Clock()
        #clock.tick(10)
        #while mixer.music.get_busy():
        #    clock.tick(10)
        while ok1 == False:   
            event2 = sense.stick.wait_for_event(emptybuffer = True)
            if event2.action == "pressed" and event2.direction == "middle":
                if pixel1_y == 3 and pixel1_x == 0 and pixel2_y == 4 and pixel2_x == 0:
                    #mixer.music.stop()
                    sense.show_message("exit? -> up!", text_colour = red, scroll_speed = 0.04)
                    sense.show_message("resume? -> down!", text_colour = green, scroll_speed = 0.04)
                    event9 = sense.stick.wait_for_event(emptybuffer = True)
                    if event9.action == "pressed" and event9.direction == "up":
                        ok1 = True
                        sense.show_message("Thank", text_colour = blue, scroll_speed = 0.05)
                        sense.show_message("you", text_colour = gold, scroll_speed = 0.05)
                        sense.show_message("for", text_colour = red, scroll_speed = 0.05)
                        sense.show_message("playing", text_colour = purple, scroll_speed = 0.05)
                        sense.show_message("Spymania!", text_colour = green, scroll_speed = 0.05)
                        return
                    elif event9.action == "pressed" and event9.direction == "down":
                        sense.show_message("Choose the level you want to play!", text_colour = cyan, scroll_speed = 0.05)
                        ENTERING_MAIN_MENU()
                        #mixer.music.play()
                        #playsound('/home/pi/Desktop/Spymania/mainmenu.mp3')
                        pixel1_x = 2
                        pixel1_y = 3
                        pixel2_x = 2
                        pixel2_y = 4
                        event2 = sense.stick.wait_for_event(emptybuffer = True)
                elif pixel1_y == 6 and pixel1_x == 2 and pixel2_y == 7 and pixel2_x == 2:
                    #mixer.music.stop()
                    Storyline()
                    pixel1_x = 2
                    pixel1_y = 3
                    pixel2_x = 2
                    pixel2_y = 4
                elif pixel1_y == 6 and pixel1_x == 4 and pixel2_y == 7 and pixel2_x == 4:
                    #mixer.music.stop()
                    if is_playable[0] == 1:
                        Level1()
                        #unlocked()
                    else:
                        locked()
                    pixel1_x = 2
                    pixel1_y = 3
                    pixel2_x = 2
                    pixel2_y = 4
                elif pixel1_y == 6 and pixel1_x == 6 and pixel2_y == 7 and pixel2_x == 6:
                    #mixer.music.stop()
                    if is_playable[1] == 1:
                        #Level2()
                        unlocked()
                    else:
                        locked()
                    pixel1_x = 2
                    pixel1_y = 3
                    pixel2_x = 2
                    pixel2_y = 4
                elif pixel1_y == 0 and pixel1_x == 2 and pixel2_y == 1 and pixel2_x == 2:
                    #mixer.music.stop()
                    if is_playable[2] == 1:
                        #Level3()
                        unlocked()
                    else:
                        locked()
                    pixel1_x = 2
                    pixel1_y = 3
                    pixel2_x = 2
                    pixel2_y = 4
                elif pixel1_y == 0 and pixel1_x == 4 and pixel2_y == 1 and pixel2_x == 4:
                    #mixer.music.stop()
                    if is_playable[3] == 1:
                        #Level4()
                        unlocked()
                    else:
                        locked()
                    pixel1_x = 2
                    pixel1_y = 3
                    pixel2_x = 2
                    pixel2_y = 4
                elif pixel1_y == 0 and pixel1_x == 6 and pixel2_y == 1 and pixel2_x == 6:
                    #mixer.music.stop()
                    if is_playable[4] == 1:
                        #Level5()
                        unlocked()
                    else:
                        locked()
                    pixel1_x = 2
                    pixel1_y = 3
                    pixel2_x = 2
                    pixel2_y = 4
                elif pixel1_y == 3 and pixel1_x == 7 and pixel2_y == 4 and pixel2_x == 7:
                    Controls()
                    pixel1_x = 2
                    pixel1_y = 3
                    pixel2_x = 2
                    pixel2_y = 4
            if event2.action == "pressed" and event2.direction != "middle":
                pixels = sense.get_pixels()
                if pixel1_y == 3 and pixel1_x == 1 and pixel2_y == 4 and pixel2_x == 1:
                    sense.set_pixels(entering_image_2)
                else:
                    sense.set_pixels(reset)
                sense.set_pixel(pixel1_y, pixel1_x, black)
                sense.set_pixel(pixel2_y, pixel2_x, black)
                if pixels[3] == black:
                    sense.set_pixel(3, 0, saddlebrown)
                if pixels[4] == black:
                    sense.set_pixel(4, 0, saddlebrown)
                if pixels[16] == black:
                    sense.set_pixel(0, 2, grey)
                if pixels[17] == black:
                    sense.set_pixel(1, 2, grey)
                if pixels[22] == black:
                    sense.set_pixel(6, 2, purple)
                if pixels[23] == black:
                    sense.set_pixel(7, 2, purple)
                if pixels[32] == black:
                    sense.set_pixel(0, 4, gold)
                if pixels[33] == black:
                    sense.set_pixel(1, 4, orange)
                if pixels[38] == black:
                    sense.set_pixel(6, 4, darkbrown)
                if pixels[39] == black:
                    sense.set_pixel(7, 4, orange)
                if pixels[48] == black:
                    sense.set_pixel(0, 6, red)
                if pixels[49] == black:
                    sense.set_pixel(1, 6, red)
                if pixels[54] == black:
                    sense.set_pixel(6, 6, cyan)
                if pixels[55] == black:
                    sense.set_pixel(7, 6, cyan)
                if pixels[59] == black:
                    sense.set_pixel(3, 7, coral)
                if pixels[60] == black:
                    sense.set_pixel(4, 7, coral)
                if event2.direction == "up" and pixel1_x > 0 and pixel2_x > 0:
                    pixel1_x = pixel1_x - 1
                    pixel2_x = pixel2_x - 1
                elif event2.direction == "down" and pixel1_x < 7 and pixel2_x < 7:
                    pixel1_x = pixel1_x + 1
                    pixel2_x = pixel2_x + 1
                elif event2.direction == "left" and pixel1_y > 0 and pixel2_y > 0:
                    pixel1_y = pixel1_y - 1
                    pixel2_y = pixel2_y - 1
                elif event2.direction == "right" and pixel1_y < 7 and pixel2_y < 7:
                    pixel1_y = pixel1_y + 1
                    pixel2_y = pixel2_y + 1
                sense.set_pixel(pixel1_y, pixel1_x, blue)
                sense.set_pixel(pixel2_y, pixel2_x, blue)
            
    #La finalul programului, dezactivam toate led-urile aprinse de pe SenseHat (At the end of the program, we clear the SenseHat)
    sense.clear()
    
#Aici apelam toate functiile pe care le-am creat astfel incat jocul sa poata rula (Here we call all the functions we need in order for the game to load)
    
MAIN_MENU()

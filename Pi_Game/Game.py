"""
--> Spymania 2D SenseHat Game <--
Contribuitori:
David Ghergut
Mihai Pangratie
"""
#Aici importam toate modulele de care avem nevoie
from sense_hat import SenseHat
#from playsound import playsound
from time import sleep
#playsound('audio.mp3')

sense = SenseHat()
#CULORI pentru SenseHat:
black = (0, 0, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
gold = (255, 215, 0)
green = (0, 255, 0)
white = (255, 255, 255)
#Aceasta functie va afisa imaginea de sfarsit al primului nivel
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

#Aceasta functie va afisa a doua imagine de sfarsit al primului nivel
"""
imagine_de_sfarsit_bucata_2 = [
        
]
def afisare_imagine_de_sfarsit_de_nivel_2():

"""
#Functie de MAIN MENU:
def MAIN_MENU():
    sense.show_message("Welcome", text_colour = blue, scroll_speed = 0.06)
    sense.show_message("to", text_colour = gold, scroll_speed = 0.06)
    sense.show_message("Spymania!", text_colour = green, scroll_speed = 0.06)
    sleep (0.5)
    sense.show_message("Press the joystick in the middle to continue!", text_colour = white, scroll_speed = 0.06)
    event1 = sense.stick.wait_for_event()
    """
    ok = False
    while ok == False:
        if event1.action == "pressed" or event1.direction == "middle":
            ok = True
            break
        sense.show_message("Press the joystick in the middle to continue!", text_colour = white, scroll_speed = 0.06)
        sleep (0.5)
    """
    #ZONA DE SELECTARE A NIVELULUI DE JOC
    if ok == True:
        sense.show_message("Choose the level you want to play!", text_colour = cyan, scroll_speed = 0.06)
        event2 = sense.stick.wait_for_event()
        ok1 = False
        position = 0;
        while ok1 == False:
            if event2.action == "pressed" and event2.direction == "left" and position == 0:
                position = 0
            elif event2.action == "pressed" and event2.direction == "right" and position == 4:
                position = 4
            elif event2.action == "pressed" and event2.direction == "right" and position < 4:
                position += 1
            elif event2.action == "pressed" and event2.direction == "left" and position > 1:
                position -= 1
            if (position == 0):
                #event3 = sense.stick.wait_for_event()
                #ok2 = False 
                #while event3.action != "pressed":
                    sense.show_message("Storyline", text_colour = gold, scroll_speed = 0.06)
                    #sleep(0.5)
            elif (position == 1):
                sense.show_message("Level 1", text_colour = gold, scroll_speed = 0.06)
            elif (position == 2):
                sense.show_message("Level 2", text_colour = gold, scroll_speed = 0.06)
            elif (position == 3):
                sense.show_message("Level 3", text_colour = gold, scroll_speed = 0.06)
            elif (position == 4):
                sense.show_message("Level 4 -> Boss Fight", text_colour = gold, scroll_speed = 0.06)    
    sense.clear()

#Aici apelam toate functiile pe care le-am creat

afisare_imagine_de_sfarsit_de_nivel_1()
#MAIN_MENU()
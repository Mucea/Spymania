"""
--> Spymania 2D SenseHat Game <--
Contribuitori:
David Ghergut
Mihai Pangratie
"""
#Aici importam toate modulele de python de care avem nevoie in tot programul (Here we import all the python modules that we need in the whole program)
from sense_hat import SenseHat
#from playsound import playsound
from time import sleep
#playsound('audio.mp3')

#VARIABILE GLOBALE (GLOBAL VARIABLES):
sense = SenseHat()
is_playable = [1, 1, 0, 0, 0, 0]
levels = {0:"Storyline", 1:"Level 1", 2:"Level 2", 3:"Level 3", 4:"Level 4", 5:"Level5 -> Boss Fight"}

#CULORI pentru SenseHat (COLOURS for the SenseHat):
black = (0, 0, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
gold = (255, 215, 0)
green = (0, 255, 0)
white = (255, 255, 255)
purple = (128, 0, 128)

#Aceasta functie va afisa imaginea de sfarsit al primului nivel (This function will print the ending image for the first level)
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

#Aceasta functie va afisa a doua imagine de sfarsit al primului nivel (This function will print the second ending image for the first level)
"""
imagine_de_sfarsit_bucata_2 = [
        
]
def afisare_imagine_de_sfarsit_de_nivel_2():

"""

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
    
    
#FUNCTIE DE MAIN MENU (MAIN MENU FUNCTION):
def MAIN_MENU():
    sense.show_message("Welcome", text_colour = blue, scroll_speed = 0.05)
    sense.show_message("to", text_colour = gold, scroll_speed = 0.05)
    sense.show_message("Spymania!", text_colour = green, scroll_speed = 0.05)
    sleep(0.5)
    sense.show_message("Press the joystick in the middle to continue to the level selection zone!", text_colour = white, scroll_speed = 0.05)
    event1 = sense.stick.wait_for_event(emptybuffer = True)
    """
    ok = False
    while ok == False:
        if event1.action == "pressed" and event1.direction == "middle":
            ok = True
            break
        sense.show_message("Press the joystick in the middle to continue!", text_colour = white, scroll_speed = 0.06)
        sleep (0.5)
    """
    #IN CAZUL UNEI DORINTE NEPREVAZUTE DE A IESI DIN JOC (IN CASE OF A SUDDEN WISH FOR EXITING THE GAME)
    if event1.action == "pressed" and event1.direction != "middle":
        sense.show_message("Are you sure you want to exit the game? If yes, press the joystick upwards!", text_colour = red, scroll_speed = 0.04)
        sense.show_message("If you want to resume, press the joystick downwards!", text_colour = green, scroll_speed = 0.04)
        event10 = sense.stick.wait_for_event(emptybuffer = True)
        if event10.action == "pressed" and event10.direction == "up":
            ok1 = True
            sense.show_message("Thank", text_colour = blue, scroll_speed = 0.05)
            sense.show_message("you", text_colour = gold, scroll_speed = 0.05)
            sense.show_message("for", text_colour = red, scroll_speed = 0.05)
            sense.show_message("playing!", text_colour = purple, scroll_speed = 0.05)
            sense.show_message("Spymania!", text_colour = green, scroll_speed = 0.05)
            return
        elif event10.action == "pressed" and event10.direction != "up":
            sense.show_message("Press the joystick in the middle to continue to the level selection zone!", text_colour = white, scroll_speed = 0.05)
            event1 = sense.stick.wait_for_event(emptybuffer = True)
    #ZONA DE SELECTARE A NIVELULUI DE JOC (THE LEVEL SELECTION ZONE)
    elif event1.action == "pressed" and event1.direction == "middle":
        sense.show_message("Choose the level you want to play!", text_colour = cyan, scroll_speed = 0.05)
        ok1 = False
        position = 0;
        while ok1 == False:
            #print(position)
            sense.show_message(levels[position], text_colour = gold, scroll_speed = 0.05)
            event2 = sense.stick.wait_for_event(emptybuffer = True)
            #IN CAZUL UNEI DORINTE NEPREVAZUTE DE A IESI DIN JOC (IN CASE OF A SUDDEN WISH FOR EXITING THE GAME)
            if event2.action == "pressed" and event2.direction == "up":
                sense.show_message("Are you sure you want to exit the game? If yes, press the joystick upwards!", text_colour = red, scroll_speed = 0.04)
                sense.show_message("If you want to resume, press the joystick downwards!", text_colour = green, scroll_speed = 0.04)
                event9 = sense.stick.wait_for_event(emptybuffer = True)
                if event9.action == "pressed" and event9.direction == "up":
                    ok1 = True
                    sense.show_message("Thank", text_colour = blue, scroll_speed = 0.05)
                    sense.show_message("you", text_colour = gold, scroll_speed = 0.05)
                    sense.show_message("for", text_colour = red, scroll_speed = 0.05)
                    sense.show_message("playing", text_colour = purple, scroll_speed = 0.05)
                    sense.show_message("Spymania!", text_colour = green, scroll_speed = 0.05)
                    break
                elif event9.action == "pressed" and event9.direction == "down":
                    sense.show_message("Choose the level you want to play!", text_colour = cyan, scroll_speed = 0.05)
                    event2 = sense.stick.wait_for_event(emptybuffer = True)
            if event2.action == "pressed" and event2.direction == "left" and position == 0:
                position = 0
            elif event2.action == "pressed" and event2.direction == "right" and position == 5:
                position = 4
            elif event2.action == "pressed" and event2.direction == "right" and position < 5:
                position += 1
            elif event2.action == "pressed" and event2.direction == "left" and position > 0:
                position -= 1
            elif (position == 0 and event2.action == "pressed" and event2.direction == "middle"):
                #sense.show_message("Storyline", text_colour = gold, scroll_speed = 0.06)
                sense.show_message("Want to see the Storyline? -> press the joystick in the middle", text_colour = green, scroll_speed = 0.04)                
                sense.show_message("exit? -> press the joystick in any other way", text_colour = red, scroll_speed = 0.04)
                event3 = sense.stick.wait_for_event(emptybuffer = True)
                if event3.action == "pressed" and event3.direction == "middle":    
                    if is_playable[position] == 1: 
                        #Storyline()
                        unlocked()
                    else:
                        locked()
                elif event3.action == "pressed" and event3.direction != "middle":
                    continue
            elif (position == 1 and event2.action == "pressed" and event2.direction == "middle"):
                #sense.show_message("Level 1", text_colour = gold, scroll_speed = 0.06)
                sense.show_message("Want to play level 1? -> press the joystick in the middle", text_colour = green, scroll_speed = 0.04)                
                sense.show_message("exit? -> press the joystick in any other way", text_colour = red, scroll_speed = 0.04)
                event4 = sense.stick.wait_for_event(emptybuffer = True)
                if event4.action == "pressed" and event4.direction == "middle":    
                    if is_playable[position] == 1:
                        #Level_1()
                        unlocked()
                    else:
                        locked()
                elif event4.action == "pressed" and event4.direction != "middle":
                    continue
            elif (position == 2 and event2.action == "pressed" and event2.direction == "middle"):
                #sense.show_message("Level 2", text_colour = gold, scroll_speed = 0.06)
                sense.show_message("Want to play level 2? -> press the joystick in the middle", text_colour = green, scroll_speed = 0.04)                
                sense.show_message("exit? -> press the joystick in any other way", text_colour = red, scroll_speed = 0.04)
                event5 = sense.stick.wait_for_event(emptybuffer = True)
                if (event5.action == "pressed" and event5.direction == "middle"):    
                    if is_playable[position] == 1: 
                        #Level_2()
                        unlocked()
                    else:
                        locked()
                elif event5.action == "pressed" and event5.direction != "middle":
                    continue
            elif (position == 3 and event2.action == "pressed" and event2.direction == "middle"):
                #sense.show_message("Level 3", text_colour = gold, scroll_speed = 0.06)
                sense.show_message("Want to play level 3? -> press the joystick in the middle", text_colour = green, scroll_speed = 0.04)                
                sense.show_message("exit? -> press the joystick in any other way", text_colour = red, scroll_speed = 0.04)
                event6 = sense.stick.wait_for_event(emptybuffer = True)
                if (event6.action == "pressed" and event6.direction == "middle"):    
                    if is_playable[position] == 1: 
                        #Level_3()
                        unlocked()
                    else:
                        locked()
                elif event6.action == "pressed" and event6.direction != "middle":
                    continue
            elif (position == 4 and event2.action == "pressed" and event2.direction == "middle"):
                #sense.show_message("Level 4", text_colour = gold, scroll_speed = 0.06)
                sense.show_message("Want to play level 4? -> press the joystick in the middle", text_colour = green, scroll_speed = 0.04)                
                sense.show_message("exit? -> press the joystick in any other way", text_colour = red, scroll_speed = 0.04)
                event7 = sense.stick.wait_for_event(emptybuffer = True)
                if (event7.action == "pressed" and event7.direction == "middle"):    
                    if is_playable[position] == 1: 
                        #Level_4()
                        unlocked()
                    else:
                        locked()
                elif event7.action == "pressed" and event7.direction != "middle":
                    continue
            elif (position == 5 and event2.action == "pressed" and event2.direction == "middle"):
                #sense.show_message("Level 5 -> Boss Fight", text_colour = gold, scroll_speed = 0.06)
                sense.show_message("Want to play level 5 (Boss Fight)? -> press the joystick in the middle", text_colour = green, scroll_speed = 0.04)                
                sense.show_message("exit? -> press the joystick in any other way", text_colour = red, scroll_speed = 0.04)
                event8 = sense.stick.wait_for_event(emptybuffer = True)
                if (event8.action == "pressed" and event8.direction == "middle"):    
                    if is_playable[position] == 1: 
                        #Level_5()
                        unlocked()
                    else:
                        locked()
                elif event8.action == "pressed" and event8.direction != "middle":
                    continue
    #La finalul programului, dezactivam toate led-urile aprinse de pe SenseHat (At the end of the program, we clear the SenseHat)
    sense.clear()

#Aici apelam toate functiile pe care le-am creat astfel incat jocul sa poata rula (Here we call all the functions we need in order for the game to load)

#afisare_imagine_de_sfarsit_de_nivel_1()
MAIN_MENU()

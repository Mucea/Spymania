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
levels = {0:"Storyline", 1:"Level 1", 2:"Level 2", 3:"Level 3", 4:"Level 4", 5:"Level 5 -> Boss Fight"}

#CULORI pentru SenseHat (COLOURS for the SenseHat):
black = (0, 0, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
darker_blue = (0, 102, 204)
red = (255, 0, 0)
gold = (255, 215, 0)
green = (0, 255, 0)
white = (255, 255, 255)
purple = (128, 0, 128)
orange = (255, 140, 0)
saddlebrown = (139, 69, 19)
coral = (255, 160, 122)
grey = (58, 59, 60)
toxicgreen = (97, 222, 42)
darkgreen = (0, 100, 0)

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
    
#FUNCTIE PENTRU STORYLINE (FUNCTION FOR THE STORYLINE)
def storyline_level_1():
    tree = [
         black, green, green, green, green, green, green, black,
         black, green, green, green, green, green, green, black,
         black, green, green, green, green, green, green, black,
         black, green, green, green, green, green, green, black,
         black, green, green, green, green, green, green, black,
         black, black, black, saddlebrown, saddlebrown, black, black, black,
         black, black, black, saddlebrown, saddlebrown, black, black, black,
         black, black, black, saddlebrown, saddlebrown, black, black, black,
    ]
    sense.set_pixels(tree)
    """
    #AICI SCRIEM STORYLINE-UL PENTRU PRIMUL NIVEL (HERE WE WRITE THE STORYLINE FOR THE FIRST LEVEL)
    text1 = ""
    storyline1 = text.split(' ')
    for word in storyline1:
        print(word)
    """
    sleep(5)
    sense.clear()
    #sleep(1)

def storyline_level_2():
    field = [
        gold, gold, cyan, white, white, cyan, cyan, cyan,
        gold, cyan, cyan, cyan, cyan, cyan, white, white,
        cyan, white, white, cyan, cyan, cyan, cyan, cyan,
        green, green, green, green, green, green, green, green,
        green, green, green, green, blue, green, green, green,
        green, red, green, green, darkgreen, green, purple, green,
        green, darkgreen, green, green, green, green, darkgreen, green,
        green, green, green, green, green, green, green, green,
    ]
    sense.set_pixels(field)
    sleep(5)
    sense.clear()
def storyline_level_3():
    castle = [
        black, red, black, black, black, black, red, black,
        red, red, red, black, black, red, red, red,
        grey, black, grey, black, black, grey, black, grey,
        grey, grey, grey, grey, grey, grey, grey, grey,
        grey, grey, grey, grey, grey, grey, grey, grey,
        grey, grey, grey, saddlebrown, saddlebrown, grey, grey, grey,
        grey, grey, grey, saddlebrown, saddlebrown, grey, grey, grey,
        grey, grey, grey, saddlebrown, saddlebrown, grey, grey, grey,
    ]
    sense.set_pixels(castle)
    """
    #AICI SCRIEM STORYLINE-UL PENTRU AL DOILEA NIVEL (HERE WE WRITE THE STORYLINE FOR THE SECOND LEVEL)
    text2 = ""
    storyline2 = text.split(' ')
    for word in storyline2:
        print(word)
    """
    sleep(5)
    sense.clear()
    #sleep(1)

def storyline_level_4_and_5():
    boss = [
        red, black, black, black, black, black, black, red,
        red, red, black, black, black, black, red, red,
        black, red, red, red, red, red, red, black,
        black, red, blue, black, black, blue, red, black,
        red, black, gold, blue, blue, gold, black, red,
        red, toxicgreen, black, black, black, black, toxicgreen, red,
        black, toxicgreen, toxicgreen, toxicgreen, toxicgreen, toxicgreen, red, black,
        black, toxicgreen, red, red, red, toxicgreen, black, black,
    ]
    sense.set_pixels(boss)
    """
    #AICI SCRIEM STORYLINE-UL PENTRU AL TREILEA NIVEL (HERE WE WRITE THE STORYLINE FOR THE THIRD LEVEL)
    text3 = ""
    storyline3 = text.split(' ')
    for word in storyline3:
        print(word)
    """
    sleep(5)
    sense.clear()
    #sleep(1)
def Storyline():
    """
    text = "Spymania is a SenseHat-centred game where Vector the soldier needs to get all the papers in order to find the grand boss who stole a very big and expensive treasure."
    storyline = text.split(' ')
    for word in storyline:
        #sense.show_message(word, text_colour = saddlebrown, scroll_speed = 0.04)
        print(word)
    """
    storyline_level_1()
    storyline_level_2()
    storyline_level_3()
    storyline_level_4_and_5()
    afisare_imagine_de_sfarsit_de_nivel_1()
    afisare_imagine_de_sfarsit_de_nivel_2()
    
#FUNCTIE DE MAIN MENU (MAIN MENU FUNCTION):
def MAIN_MENU():
    sense.show_message("Welcome", text_colour = blue, scroll_speed = 0.05)
    sense.show_message("to", text_colour = gold, scroll_speed = 0.05)
    sense.show_message("Spymania!", text_colour = green, scroll_speed = 0.05)
    sleep(0.5)
    sense.show_message("Press the joystick in the middle to continue!", text_colour = darker_blue, scroll_speed = 0.05)
    event1 = sense.stick.wait_for_event(emptybuffer = True)
    #IN CAZUL UNEI DORINTE NEPREVAZUTE DE A IESI DIN JOC (IN CASE OF A SUDDEN WISH FOR EXITING THE GAME)
    if event1.action == "pressed" and event1.direction != "middle":
        sense.show_message("exit? -> up!", text_colour = red, scroll_speed = 0.04)
        sense.show_message("resume? -> down!", text_colour = green, scroll_speed = 0.04)
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
            sense.show_message("Press the joystick in the middle to continue!", text_colour = darker_blue, scroll_speed = 0.05)
            event1 = sense.stick.wait_for_event(emptybuffer = True)
    #ZONA DE SELECTARE A NIVELULUI DE JOC (THE LEVEL SELECTION ZONE)
    elif event1.action == "pressed" and event1.direction == "middle":
        sense.show_message("Choose the level you want to play!", text_colour = coral, scroll_speed = 0.05)
        ok1 = False
        position = 0;
        while ok1 == False:
            sense.show_message(levels[position], text_colour = gold, scroll_speed = 0.05)
            event2 = sense.stick.wait_for_event(emptybuffer = True)
            #IN CAZUL UNEI DORINTE NEPREVAZUTE DE A IESI DIN JOC (IN CASE OF A SUDDEN WISH FOR EXITING THE GAME)
            if event2.action == "pressed" and event2.direction == "up":
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
                    break
                elif event9.action == "pressed" and event9.direction == "down":
                    sense.show_message("Choose the level you want to play!", text_colour = cyan, scroll_speed = 0.05)
                    event2 = sense.stick.wait_for_event(emptybuffer = True)
            """
            if event2.action == "pressed" and event2.direction == "left" and position == 0:
                position = 0
            elif event2.action == "pressed" and event2.direction == "right" and position == 5:
                position = 5
            elif event2.action == "pressed" and event2.direction == "right" and position < 5:
                position += 1
            elif event2.action == "pressed" and event2.direction == "left" and position > 0:
                position -= 1
            elif (position == 0 and event2.action == "pressed" and event2.direction == "middle"):
                sense.show_message("see storyline? -> press middle", text_colour = green, scroll_speed = 0.04)                
                sense.show_message("exit? -> press any other way", text_colour = red, scroll_speed = 0.04)
                event3 = sense.stick.wait_for_event(emptybuffer = True)
                if event3.action == "pressed" and event3.direction == "middle":    
                    if is_playable[position] == 1: 
                        Storyline()
                    else:
                        locked()
                elif event3.action == "pressed" and event3.direction != "middle":
                    continue
            elif (position == 1 and event2.action == "pressed" and event2.direction == "middle"):
                sense.show_message("see storyline? -> press middle", text_colour = green, scroll_speed = 0.04)                
                sense.show_message("exit? -> press any other way", text_colour = red, scroll_speed = 0.04)
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
                sense.show_message("see storyline? -> press middle", text_colour = green, scroll_speed = 0.04)                
                sense.show_message("exit? -> press any other way", text_colour = red, scroll_speed = 0.04)
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
                sense.show_message("see storyline? -> press middle", text_colour = green, scroll_speed = 0.04)                
                sense.show_message("exit? -> press any other way", text_colour = red, scroll_speed = 0.04)
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
                sense.show_message("see storyline? -> press middle", text_colour = green, scroll_speed = 0.04)                
                sense.show_message("exit? -> press any other way", text_colour = red, scroll_speed = 0.04)
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
                sense.show_message("see storyline? -> press middle", text_colour = green, scroll_speed = 0.04)                
                sense.show_message("exit? -> press any other way", text_colour = red, scroll_speed = 0.04)
                event8 = sense.stick.wait_for_event(emptybuffer = True)
                if (event8.action == "pressed" and event8.direction == "middle"):    
                    if is_playable[position] == 1: 
                        #Level_5()
                        unlocked()
                    else:
                        locked()
                elif event8.action == "pressed" and event8.direction != "middle":
                    continue
            """
            
    #La finalul programului, dezactivam toate led-urile aprinse de pe SenseHat (At the end of the program, we clear the SenseHat)
    sense.clear()

#Aici apelam toate functiile pe care le-am creat astfel incat jocul sa poata rula (Here we call all the functions we need in order for the game to load)
    
#MAIN_MENU()
Storyline()

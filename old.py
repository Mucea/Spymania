"""
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
#IN CAZUL UNEI DORINTE NEPREVAZUTE DE A IESI DIN JOC (IN CASE OF A SUDDEN WISH FOR EXITING THE GAME)
    """
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
    """
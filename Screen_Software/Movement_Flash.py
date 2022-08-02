import pygame

pygame.init()

"""
This program will run on joystick inputs if a joystick is plugged in. If no joystick is found it will use mouse inputs.
When movement or button inputs are found it will flash the screen white for 1 second before returning to black.s
"""

# If there is a joystick, run this code. Otherwise run alternative code for mouse controls.
if(pygame.joystick.get_count()>0):
    # get joystick, start event listener, grab focus
    stick = pygame.joystick.Joystick(0)
    pygame.event.pump()
    pygame.display.init()
    pygame.event.set_grab(True)
    # Open window, 800x800 resolution.
    window = pygame.display.set_mode((800,800)) # 0, 0, fullscreen
    # set mouse cursor
    cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
    pygame.mouse.set_cursor(cursor)

    # initialize variables
    prevMouse = (0,0)
    currentMouse = (0, 0)
    deadZone = 0.01
    # game loop
    going = True
    pygame.time.Clock().tick(90)
    while going:
        # Read from event queue
        event = pygame.event.poll()
        # uncomment if you want to the screen to react to joystick motion.
        #
        # if event.type == pygame.JOYAXISMOTION:
        #     if stick.get_axis(0) > deadZone or stick.get_axis(0) < -deadZone or stick.get_axis(1) > deadZone or stick.get_axis(1) < -deadZone: #0.1 is the deadzone im applying to deal with jitter
        #         window.fill((255,255,255))
        #         pygame.display.flip()
        #         pygame.time.wait(1000)
        #
        #     window.fill((0,0,0))
        #     pygame.display.flip()

        # if there is a joystick button pushed. Flash the screen white (255,255,255) ,wait 1 second, then go back to black (0,0,0)
        if event.type == pygame.JOYBUTTONDOWN:
            window.fill((255,255,255))
            pygame.display.flip()
            pygame.time.wait(1000)
            window.fill((0,0,0))
            pygame.display.flip()

        # Process quit button being clicked to end game loop
        if event.type == pygame.QUIT:
            going = False
        # process escape key being pressed to end game loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                going = False

else:
    #Run the loop for mouse instead of joystick
    #start event reader and grab focus
    pygame.event.pump()
    pygame.display.init()
    pygame.event.set_grab(True)
    #open window at default resolution 800x800
    window = pygame.display.set_mode((800,800)) # 0, 0, fullscreen
    # set game cursor
    cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
    pygame.mouse.set_cursor(cursor)

    # Initialize variables
    prevMouse = (0,0)
    currentMouse = (0, 0)
    deadZone = 0.1
    # game loop
    going = True
    pygame.time.Clock().tick(90)
    while going:
        # start event listener
        event = pygame.event.poll()

        # uncomment if you want to the screen to react to mouse motion.
        #
        # if event.type == pygame.MOUSEMOTION:
        #     window.fill((255,255,255))
        #     pygame.display.flip()
        #     pygame.time.wait(1000)
        #     window.fill((0,0,0))
        #     pygame.display.flip()


        # Listen for mouse button being pressed. If pressed fills screen with white (255,255,255) then wait 1 second and return to black (0,0,0)
        if event.type==pygame.MOUSEBUTTONDOWN:

            window.fill((255,255,255))
            pygame.display.flip()
            pygame.time.wait(1000)

            window.fill((0,0,0))
            pygame.display.flip()
        # process quit button being clicked and end game loop
        if event.type == pygame.QUIT:
            going = False
        # Process escape button being pressed and end game loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                going = False

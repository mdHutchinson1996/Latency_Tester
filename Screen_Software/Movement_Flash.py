import pygame

pygame.init()

if(pygame.joystick.get_count()>0):
    stick = pygame.joystick.Joystick(0)
    print(stick.get_name())
    pygame.event.pump()
    pygame.display.init()
    pygame.event.set_grab(True)

    window = pygame.display.set_mode((800,800)) # 0, 0, fullscreen

    cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
    pygame.mouse.set_cursor(cursor)


    prevMouse = (0,0)
    currentMouse = (0, 0)
    deadZone = 0.01
    going = True
    pygame.time.Clock().tick(90)
    while going:

        event = pygame.event.poll()

        if event.type == pygame.JOYAXISMOTION:
            if stick.get_axis(0) > deadZone or stick.get_axis(0) < -deadZone or stick.get_axis(1) > deadZone or stick.get_axis(1) < -deadZone: #0.1 is the deadzone im applying to deal with jitter
                window.fill((255,255,255))
                pygame.display.flip()
                pygame.time.wait(1000)

            window.fill((0,0,0))
            pygame.display.flip()

        if event.type == pygame.JOYBUTTONDOWN:
            window.fill((255,255,255))
            pygame.display.flip()
            pygame.time.wait(1000)
            window.fill((0,0,0))
            pygame.display.flip()

        if event.type == pygame.QUIT:
            going = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                going = False

else:
    print("Mouse")
    pygame.event.pump()
    pygame.display.init()
    pygame.event.set_grab(True)

    window = pygame.display.set_mode((800,800)) # 0, 0, fullscreen

    cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
    pygame.mouse.set_cursor(cursor)


    prevMouse = (0,0)
    currentMouse = (0, 0)
    deadZone = 0.1
    going = True
    pygame.time.Clock().tick(90)
    while going:

        event = pygame.event.poll()

        if event.type == pygame.MOUSEMOTION or event.type==pygame.MOUSEBUTTONDOWN:

            window.fill((255,255,255))
            pygame.display.flip()
            pygame.time.wait(1000)

            window.fill((0,0,0))
            pygame.display.flip()

        if event.type == pygame.QUIT:
            going = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                going = False

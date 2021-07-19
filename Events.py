def event():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                print('up')
            if event.key == pygame.K_DOWN:
                print('down')
            if event.key == pygame.K_LEFT:
                print('left')
            if event.key == pygame.K_RIGHT:
                print('right')

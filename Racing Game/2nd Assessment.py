# Import and initialize the pygame library
import pygame
import random
from time import sleep

pygame.init()

# Set up the screen width and height
PadWidth = 400
PadHeight = 600

# Set up the colours
Grey = (128,128,128)
White = (255,255,255)
Red = (255,0,0)
Black = (0,0,0)

Surface = pygame.display.set_mode((PadWidth, PadHeight))    # Set up the drawing window
pygame.display.set_caption("Motorcycle Racing Game")    # Set up the caption of window
LoadPlayer = pygame.image.load("Player.png")    # Load player image

# Set up the size of Player
PlayerWidth = 25
PlayerHeight = 60

# Load the musics that will be used
pygame.mixer_music.load("BGM.mp3")
pygame.mixer_music.load("boom.wav")
pygame.mixer_music.load("Engine.wav")

# Create the list of cars
CarsPicture = ["car1.png", "car2.png", "car3.png", "car4.png", "car5.png", "car6.png", "car7.png", "car8.png"]

# Define Player
def Player(x,y):
    Surface.blit(LoadPlayer, (x,y))

# Define to pause between the game
def Pause():

    # Set up the size of x and y
    x = PadWidth/2
    y = PadHeight/2

    pause = True    # Variable to keep the main loop
    while pause:    # Pause is start
        for event in pygame.event.get():    # If any input is given
            if event.type == pygame.QUIT:   # If quit input is given
                pygame.quit()   # The window is closed
                quit()

            # If the user press C, the user will exit 'while'
            if event.type == pygame.KEYDOWN:    # If input is Keydown
                if event.key == pygame.K_c:     # If input is C
                    pause = False   # Break out 'while'

        FontA = pygame.font.SysFont("comicsansms", 35, True, False)     # Set up font (style, size , bold and italic)
        TextA = FontA.render("Pause", True, Black)      # Set up the text input (text, antialias, colour)
        Surface.blit(TextA, [x-50, y-65])   # Set up the position of text
        FontB = pygame.font.SysFont("comicsansms", 15, True, False)     # Set up font (style, size , bold and italic)
        TextB = FontB.render("Press C to continue",True, Black)     # Set up the text input (text, antialias, colour)
        Surface.blit(TextB, [x-70, y+30])   # Set up the position of text
        pygame.display.update()     # Update the display

# Define the main screen before playing the game
def MainMenu():

    # Set up the size of x and y
    x = PadWidth/2
    y = PadHeight/2

    Main = True     # Variable to keep the main loop
    while Main:     # Main screen is start
        for event in pygame.event.get():    # If any input is given
            if event.type == pygame.QUIT:   # If quit input is given
                pygame.quit()   # Package is stop
                quit()      # The window is closed

            if event.type == pygame.KEYDOWN:    # If input is keydown
                if event.key == pygame.K_SPACE:     # If input is spacebar
                    Main = False    # Break out main screen

        Surface.fill(Black)     # fill
        FontA = pygame.font.SysFont("comicsansms", 35, True, False)     # Set up font (style, size , bold and italic)
        TextA = FontA.render("Motorcycle Gallop", True, Red)    # Set up the text input (text, antialias, colour)
        Surface.blit(TextA, [x-145, y-100])     # Set up the position of text
        FontB = pygame.font.SysFont("comicsansms", 20, True, False)     # Set up font (style, size , bold and italic)
        TextB = FontB.render("Press Spacebar to start", True, White)    # Set up the text input (text, antialias, colour)
        Surface.blit(TextB, [x-115, y+40])      # Set up the position of text
        pygame.display.update()     # Update the display

# Define crash to end the game
def Crashed():

    # Set up the size of x and y
    x = PadWidth/2
    y = PadHeight/2

    pygame.mixer.music.stop()   # All music is stop
    pygame.mixer.music.load("boom.wav")     # Music is loaded
    pygame.mixer.music.play()   # Play the music
    sleep(1)    # Stop for a second
    FontA = pygame.font.SysFont("comicsansms", 35, True, False)     # Set up font (style, size , bold and italic)
    TextA= FontA.render("Boom!", True, Red)      # Set up the text input (text, antialias, colour)
    Surface.blit(TextA, [x-43,y-120])      # Set up the position of text
    FontB = pygame.font.SysFont("comicsansms", 20, True, False)     # Set up font (style, size , bold and italic)
    TextB = FontB.render("Press R to restart", True, White)    # Set up the text input (text, antialias, colour)
    Surface.blit(TextB, [x - 90, y+100])        # Set up the position of text
    pygame.display.update()     # Update the display

    Crash = True    # Variable to keep the main loop
    while Crash:    # Main loop
        for event in pygame.event.get():    # If any input is given
            if event.type == pygame.QUIT:   # If quit input is given
                pygame.quit()   # The package is stop
                quit()      # The window is closed

            if event.type == pygame.KEYDOWN:    # If input is keydown
                if event.key == pygame.K_r:     # If key is r
                    Crash = False   # Break out the main loop

    StartGame()     # Replay the game
    pygame.quit()
    quit()
# Define starting game
def StartGame():

    # Set up the size of x and y
    x=PadWidth/2
    y=PadHeight/2 + 230

    # Set up the size of MoveX and MoveY
    MoveX = 0
    MoveY = 0

    OnGame = True   # variable to keep the main loop

    # Set up to create cars coming player
    RandomCars = pygame.image.load(random.choice(CarsPicture))      # Load random image of cars
    CarWidth = 35
    CarHeight = 86
    CarsX = random.randrange(0, PadWidth - CarWidth)
    CarsY = 0
    CarsSpeed = 2

    pygame.mixer.music.load("BGM.mp3")      # load the music
    pygame.mixer.music.play(-1)     # Repeat the music until the window is closed

    # Set up to create lanes on the road
    ChangeLane = []
    LaneWidth = 10
    LaneHeight = 50
    Separation = 15
    TheNumberOfLanes = 10
    ChangeLaneX = (PadWidth - LaneWidth) / 2
    ChangeLaneY = -20

    score = 0   # Score variable

    for j in range(TheNumberOfLanes):
        ChangeLane.append([ChangeLaneX, ChangeLaneY])
        ChangeLaneY += LaneHeight + Separation

    while OnGame:   # Ongame loop
        score += 1      # Score is increased
        for event in pygame.event.get():    # If any input is given
            if event.type == pygame.QUIT:   # If quit input is given
                OnGame = False  # Break out Ongame loop

            if event.type == pygame.KEYDOWN:    # If the input is Keydown
                if event.key == pygame.K_LEFT:      # If the input is key left
                    MoveX -= 1      # Move player to the left side
                if event.key == pygame.K_RIGHT:     # If the input is key right
                    MoveX += 1      # Move player to the right side
                if event.key == pygame.K_p:     # If the input is key p
                    Pause()     # Load Pause() function
            if event.type == pygame.KEYUP:      # If the input is keyup
                MoveX = 0   # Stay at the point

        x += MoveX      # Moving of player

        # Set up the limitation of the screen to do not move out motorcycle
        if x < 0:
            x = 0
        elif x > PadWidth - PlayerWidth:
            x = PadWidth - PlayerWidth

        Surface.fill(Grey)      # Fill the background into grey

        CarsY += CarsSpeed      # Car comes from top of the window to the bottom of that

        if CarsY > PadHeight:
            RandomCars = pygame.image.load(random.choice(CarsPicture))  # Load random images of cars list
            # Size of the cars
            CarWidth = 35
            CarHeight = 86
            CarsX = random.randrange(0, PadWidth - CarWidth)    # The X position that cars come
            CarsY = 0   # The Y position that cars come

        for j in range(TheNumberOfLanes):
            pygame.draw.rect(Surface, White, [ChangeLane[j][0], ChangeLane[j][1], LaneWidth, LaneHeight])   # Draw square
            ChangeLane[j][1] += 2   # Move the lanes from top to bottom as the speed is 2
            if ChangeLane[j][1] > PadHeight:    # If all lanes move outside of the screen
                ChangeLane[j][1] = -5 - LaneHeight     # repeat

        Player(x, y)    # Display the player on the screen

        FontB = pygame.font.SysFont("comicsansms", 15, True, Black)     # set up font (style, size , bold and italic)
        ScoreText = FontB.render("Score: " +str(score), True, Black)    # set up the text input (text, antialias, colour)
        Surface.blit(ScoreText, (20, 20))       # set up the position of text

        Surface.blit(RandomCars, (CarsX, CarsY))    # Load random cars and the position

        # Set up the condition that the player crashes to cars
        if y < CarsY + CarHeight:
            if (CarsX + CarWidth > x and CarsX + CarWidth < x + PlayerWidth) or (CarsX > x and CarsX < x + PlayerWidth):
                Crashed()

        pygame.display.update()     # update the display

MainMenu()      # Start main screen
StartGame()     # Start game
pygame.quit()
quit()
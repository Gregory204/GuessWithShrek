import pygame
import sys
import random
import time
import ButtonClass as BC

def invisible_countdown(seconds):
    # wait a bit before game automatically closes
    while seconds > 0:
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        time.sleep(1)  # pauses countdown for 1 second to act like actual countdown
        seconds -= 1

def countdown(seconds):
    # Once countdown stops roses begins
    roses.stop()
    while seconds > 0:
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # each second gets a new screen fill
        screen.fill(black)
        font = pygame.font.Font(None, 78)
        text = font.render(f"{seconds}...", True, white)
        text_rect = text.get_rect(center=(width // 2, height // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        time.sleep(1)  # pauses countdown for 1 second to act like actual countdown
        seconds -= 1
    pygame.display.flip()

def display_text_lose(text, y_offset=0):
    # Image for mad shrek
    dissapointed_shrek = pygame.image.load('4480368-MUboXjAewy1d49V8.jpg')
    dissapointed_shrek = pygame.transform.scale(dissapointed_shrek, (1200, 800))
    dissapointed_shrek_rect = dissapointed_shrek.get_rect(center=(width // 2, height // 2))
    screen.blit(dissapointed_shrek, dissapointed_shrek_rect)

    font = pygame.font.Font(None, 36)
    # RAHHHHHH
    lose_sound = pygame.mixer.Sound('fnaf_6_jumpscare_sound_mp3_66038.mp3')
    lose_sound.play().set_volume(0.3)
    # GIT OUT ME SWAMP
    shrek_MAD = pygame.mixer.Sound('Shrek_Scream.wav')
    shrek_MAD.play().set_volume(0.3)

    text_surface = font.render(text, True, (255, 0, 0)).convert_alpha()
    text_rect = text_surface.get_rect(center=(width // 2, height // 2 + 200))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

def display_text(text, y_offset=0):
    font = pygame.font.Font(None, 36)

    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect(center=(width // 2, height // 2 + y_offset))
    screen.blit(text_surface, text_rect)
def display_text_win(text, y_offset=0):
    happy_shrek = pygame.image.load('images-5.jpeg')
    happy_shrek = pygame.transform.scale(happy_shrek, (1200, 800))
    happy_shrek_rect = happy_shrek.get_rect(center=(width // 2, height // 2))
    screen.blit(happy_shrek, happy_shrek_rect)

    suprised_shrek = pygame.mixer.Sound('Squico_yolo_blow.wav')
    suprised_shrek.play(-1)
    font = pygame.font.Font(None, 36)

    text_surface = font.render(text, True, (0, 0, 255))
    text_rect = text_surface.get_rect(center=(width // 2, height // 2 + y_offset))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()


pygame.init()
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Can You Guess?")
Icon = pygame.image.load('4480368-MUboXjAewy1d49V8.jpg')
pygame.display.set_icon(Icon)
white = (255, 255, 255)
black = (0, 0, 0)
roses = pygame.mixer.Sound('Roses_Erect_2024.wav')
roses.play(-1).set_volume(0.08)

x = random.randrange(1, 5)
y = random.randrange(6, 11)
correct_answer = random.randrange(x, y)

start = pygame.image.load('green-start-button-on-transparent-background-free-png.webp').convert_alpha()
exit = pygame.image.load('pngimg.com - exit_PNG29.png').convert_alpha()
instructions = pygame.image.load('INSTRUCTIONS-button.png').convert_alpha()
# play_again = pygame.image.load('playAgainButton2x.png').convert_alpha()

start_button = BC.Button(0, 100, start, 0.4)
exit_button = BC.Button(1000, 100, exit, 0.1)
instructions_button = BC.Button(600, 550, instructions, 0.6)
# play_again_button = BC.Button(800, 650, play_again, 1)

swamp = pygame.image.load('david-gomez-cienaga-artstation.png')
swamp = pygame.transform.scale(swamp, (width, height))
swamp_rect = swamp.get_rect(center=(width//2, height//2))
screen.blit(swamp, swamp_rect)

state = "input"
menu_state = "main"
game_state = "idle"
user_input = ""
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if menu_state == "main":
        swamp = pygame.image.load('david-gomez-cienaga-artstation.png')
        swamp = pygame.transform.scale(swamp, (width, height))
        swamp_rect = swamp.get_rect(center=(width // 2, height // 2))
        screen.blit(swamp, swamp_rect)

        if start_button.draw(screen):
            game_started = True
            menu_state = "game"
        elif exit_button.draw(screen):
            run = False
        elif instructions_button.draw(screen):
            menu_state = "instructions"

    elif menu_state == "instructions":

        swamp = pygame.image.load('david-gomez-cienaga-artstation.png')
        swamp = pygame.transform.scale(swamp, (width, height))
        swamp_rect = swamp.get_rect(center=(width // 2, height // 2))
        screen.blit(swamp, swamp_rect)

        display_text("Its just a counting game all you have to do is guess"
                 " the number from a range of small to big ez pz")
        display_text('press backspace/delete to return to main menu', y_offset=50)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    menu_state = "main"

    elif menu_state == "game":
        swamp = pygame.image.load('david-gomez-cienaga-artstation.png')
        swamp = pygame.transform.scale(swamp, (1200, 800))
        swamp_rect = swamp.get_rect(center=(width // 2, height // 2))
        screen.blit(swamp, swamp_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # pygame.KEYDOWN is a constant representing the event type that occurs when a key on the keyboard is pressed down
                if state == "input":
                    if event.key == pygame.K_RETURN:
                        if user_input.isdigit():
                            if x <= int(user_input) <= y:
                                user_number = int(user_input)
                                if user_number == correct_answer:
                                    state = "win"
                                else:
                                    state = "lose"
                            else:
                                user_input = ""
                                display_text("Not in range dude...")  # displays error
                                pygame.display.flip()
                                pygame.time.wait(2000)  # wait for user to see error message
                                display_text(" " * 50)  # gets rid of error message
                                pygame.display.flip()
                        else:
                            user_input = ""
                            display_text("Invalid input. Please enter a number.")
                            pygame.display.flip()
                            pygame.time.wait(2000)  # wait for error to clear
                            display_text(" " * 50)
                            pygame.display.flip()
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    elif event.key in (pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9):
                        user_input += event.unicode

        if state == "input":
            display_text(f"Enter a number from {x} to {y}:", -50)
            display_text(user_input)

        elif state == "error":
            state = "result"

        elif state == "win":
            countdown(3)
            menu_state = "win"
            display_text_win("Congratulations...You beat me challenger!")
            display_text("Game will close in 20 seconds Automatically...", y_offset=200)
            pygame.display.flip()
            invisible_countdown(20)
            pygame.quit()
            sys.exit()

        elif state == "lose":
            countdown(3)
            menu_state = "lose"
            display_text_lose(f"Did you really think that was the answer? PFFFFFF"
                                  f" You lost good game buddy >:)")
            display_text("Game will close in 10 seconds Automatically...", y_offset=300)
            pygame.display.flip()
            invisible_countdown(10)
            pygame.quit()
            sys.exit()

    pygame.display.update()

pygame.quit()
sys.exit()

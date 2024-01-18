import random
import time
import sys
import pygame

# input numbers
# error messages flashing

pygame.init()
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Can You Guess?")
Icon = pygame.image.load('chimp.png')
pygame.display.set_icon(Icon)
white = (255, 255, 255)
black = (0, 0, 0)
game_state = "idle"

class Button:
    def __init__(self):
        pass

def start():
    # Starting Screen
    swamp = pygame.image.load('david-gomez-cienaga-artstation.png')
    swamp = pygame.transform.scale(swamp, (width, height))
    swamp_rect = swamp.get_rect(center=(width // 2, height // 2))
    screen.blit(swamp, swamp_rect)

     # Sound Track for Game
    roses = pygame.mixer.Sound('Roses_Erect_2024.wav')
    roses.play()

    # Text for beginning game
    display_text("Press Enter To Play: ", 100)
    display_text("Press X For Instructions: ", 200)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        # If user hits return key or enter key they start the game
            elif event.key == pygame.K_RETURN:  # == enter key
                game_state = "start"
            elif event.key == pygame.K_x:
                game_state = "instructions"

    # Press Enter (ReturnKey to start game)
    # soundtrack = fnf music, max redden
    # have a press key that starts the game
    # have a key that shows instructions
    # we need a overlaying background for the game so its not just a white screen


'''
Needed after user loses or wins
def play_again():

'''


def invisible_countdown(seconds):
    while seconds > 0:
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        time.sleep(1)  # pauses countdown for 1 second to act like actual countdown
        seconds -= 1


def countdown(seconds):
    while seconds > 0:
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(black)
        font = pygame.font.Font(None, 78)
        text = font.render(f"{seconds}...", True, white)
        text_rect = text.get_rect(center=(width // 2, height // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        time.sleep(1)  # pauses countdown for 1 second to act like actual countdown
        seconds -= 1
        # countdown fnf, shrek noise,

    screen.fill(white)
    pygame.display.flip()


def display_text(text, y_offset=0):
    font = pygame.font.Font(None, 36)

    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect(center=(width // 2, height // 2 + y_offset))
    screen.blit(text_surface, text_rect)


def display_text_lose(text, y_offset=0):
    dissapointed_shrek = pygame.image.load('4480368-MUboXjAewy1d49V8.jpg')
    dissapointed_shrek = pygame.transform.scale(dissapointed_shrek, (1200, 800))
    dissapointed_shrek_rect = dissapointed_shrek.get_rect(center=(width // 2, height // 2))
    screen.blit(dissapointed_shrek, dissapointed_shrek_rect)
    font = pygame.font.Font(None, 36)
    lose_sound = pygame.mixer.Sound('fnaf_6_jumpscare_sound_mp3_66038.mp3')
    lose_sound.play()

    text_surface = font.render(text, True, (255, 0, 0)).convert_alpha()
    text_rect = text_surface.get_rect(center=(width // 2, height // 2 + 200))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()


def display_error_message(message, y_offset=0):
    font = pygame.font.Font(None, 36)

    text_surface = font.render(message, True, (255, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2, height // 2 + y_offset))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()




'''
def lose_game():

def win_game():
    win_sound = pygame.mixer.Sound('win_sound_effect.mp3')
    background images (shrek celebration) 
    # sound effect kiss, win music
    Shrek Besito
'''


def display_text_win(text, y_offset=0):
    happy_shrek = pygame.image.load('images-5.jpeg')
    happy_shrek = pygame.transform.scale(happy_shrek, (1200, 800))
    happy_shrek_rect = happy_shrek.get_rect(center=(width // 2, height // 2))
    screen.blit(happy_shrek, happy_shrek_rect)
    font = pygame.font.Font(None, 36)

    text_surface = font.render(text, True, (0, 0, 255))
    text_rect = text_surface.get_rect(center=(width // 2, height // 2 + y_offset))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()


# def win_game():
def main():
    x = random.randrange(1, 50)
    y = random.randrange(50, 100)
    correct_answer = random.randrange(x, y)

    state = "input"
    user_input = ""
    error_message = ""

    while True:
        bog = pygame.image.load('Game_Background_190.png')
        bog = pygame.transform.scale(bog, (1200, 800))
        bog_rect = bog.get_rect(center=(width // 2, height // 2))
        screen.blit(bog, bog_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # pygame.KEYDOWN is a constant representing the event type that occurs when a key on the keyboard is pressed down
                if state == "input":
                    if event.key == pygame.K_RETURN:
                        try:
                            user_int = int(user_input)
                            if x <= user_int <= y:
                                state = "error"
                            error_message = "Not in range dude..."

                        except ValueError:
                            error_message = "I don't think that's a number ;-;"
                        user_input = ""
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                        error_message = ""
                    elif event.unicode.isdigit():
                        user_input += event.unicode
                        error_message = ""

        if state == "input":
            display_text(f"Enter a number from {x} to {y}:", -50)
            display_text(user_input)
            if error_message:
                display_error_message(error_message, 50)

        elif state == "error":
            '''
            display_text("Looks like we ran into a problem. "  # doesn't work currently
                         "1. You aren't in range."
                         "2. You entered a letter or symbol silly goose.")
            '''
            state = "result"

        elif state == "result":
            countdown(3)
            if user_input == str(correct_answer):
                display_text_win("Congratulations...You beat me challenger!")
                invisible_countdown(7)
            else:
                display_text_lose(f"Did you really think that was the answer? PFFFFFF"
                                  f" You lost good game buddy >:)")
                invisible_countdown(5)
            pygame.quit()
            sys.exit()

        pygame.display.update()
        # Ask the player if they wannna play again
        display_text("Do you want to play again")
        display_text("Press y for yes")
        display_text("Press N for no")
        pygame.display.update()
        play_again = None
        while play_again is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        play_again = True
                    elif event.key == pygame.K_n:
                        play_again = False

        if not play_again:
            break




if __name__ == "__main__":
    main()

'''
def main():
    x = random.randrange(1, 50)
    y = random.randrange(50, 100)
    correct_answer = random.randrange(x, y)

    while True:
        user_number = input(f"Enter a number from {x} to {y}:\n")
        if user_number.isdigit() and x <= int(user_number) <= y:
            break
        else:
            print("Looks like we ran into a problem. 1. You aren't in range. "
                  "\n2. You entered in a letter or symbol silly goose.\n")

    while True:
        if user_number == correct_answer:
            countdown(3)
            print("Congratulations...You beat me challenger!\n")
            break
        else:
            countdown(3)
            print(f"\nDid you really think the answer was {user_number} PFFFFFF\n"
                  f"You lost good game buddy >:)")
            break



if __name__ == '__main__':
    main()

Old Display Function (possible not needed)
def display_text(text, y_offset=0):
    font = pygame.font.Font(None, 36)

    fit_text = ""
    max_width = width - 40
    for word in text.split():
        line = fit_text + word + " "
        if font.size(line)[0] < max_width:
            fit_text += "\n" + word + " "

    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect(center=(width // 2, height // 2 + y_offset))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

'''


import pygame
import sys
from random import randint, choice
from wavl import WAVL
from nltk.corpus import words
from typing import Any
import itertools

def tokenize(word: Any) -> str:
    new = ""
    for i in word:
        if i not in "[]\'":
            new += i
    return new.lower()

def load_data(wavl: WAVL) -> None:
    # f = open(path, 'rt')
    # f = open(path)
    # dic = json.load(f)
    # dic = csv.reader(f)
    dic = words.words()
    # i, j = 0, 0
    for word in dic:
        # i+= 1
        word = tokenize(word)
        if not wavl.search(word):
            # j += 1
            wavl.insert(word)
    # print(i, j)

def search(wavl: WAVL) -> None:
    query = input("What word u want to search: ")
    while (query != "q"):
        print(wavl.search(query))
        query = input("What word u want to search: ")

def alphabet_generator() -> list:
    alpha = ""
    vowels = "aeiou"
    tier1 = "aeionprst"
    tier2 = "ubcdfghlmv"
    tier3 = "jkqwxyz"
    common = "nprst"
    medium = "bcdfghlmv"
    rare = "jkqwxyz"
    abc = "bcdfghjklmnpqrstvwxyz"

    for i in range(8):
        a = randint(0, 9)
        if a in [0, 4, 8, 9]:
            alpha += choice(tier1)
        else:
            if a in [1, 2, 3, 7]:
                alpha += choice(tier2)
            elif a in [5, 6]:
                alpha += choice(tier3)
            # else:
            #     alpha.append(rare[randint(0, 6)])
            # alpha.append(vowels[randint(0, 4)])
    return alpha

def word_check(word: str, done: list, wavl: WAVL) -> bool:
    if wavl.search(word):
        wavl.remove(word)
        done.append(word)
        return True
    return False

def getallperms(letters: str): #letters is a string of letters
    lst = []
    for i in range(3,len(letters)+1):
        perms = list(itertools.permutations(letters,i))
        lst = lst + perms
    return lst #lst is list of tuples, each tuple is a permuatation

def truewords(perms): #perms is permutations list from getallperms function
    permutations = []
    for perm in perms:
        permutations.append("".join(perm))
    foundlst = list(set(permutations).intersection(set(x.lower() for x in words.words())))
    # print(len(foundlst))
    # print(foundlst)
    if len(foundlst) >= 49:
        return True, len(foundlst)
    return False, len(foundlst)

# def main():
#     print("Loading data...")
#     wavl = WAVL()
#     load_data('urbandict-csv.csv', wavl)
#     print("Loaded data successfully")
#     while True:
#         alph = alphabet_generator()
#         print(alph)
#         perm = getallperms(alph)
#         run, _length = truewords(perm)
#         while not run:
#             alph = alphabet_generator()
#             print(alph)
#             perm = getallperms(alph)
#             run, _length = truewords(perm)
#         done = list()
#         points = 0
#         word = input()
#         while word != "q":
#             if word_check(word, done, wavl):
#                 points += 5
#                 print("Valid entry", points)
#             else:
#                 if word in done:
#                     print("Duplicate entry not allowed")
#                 else:
#                     print("Invalid word", points)
#             word = input()
#         for i in done:
#             wavl.insert(i)
wavl = WAVL()
load_data(wavl)
alph = alphabet_generator() # generating random sequence
print(alph)
perm = getallperms(alph)
run, _length = truewords(perm)
while not run:
    alph = alphabet_generator()
    print(alph)
    perm = getallperms(alph)
    run, _length = truewords(perm)
pygame.init()

# Constants

WIDTH, HEIGHT = 800, 600

#score
score_value=0
font_score = pygame.font.Font("assets/FreeSansBold.otf", 16)
textX = 10
textY = 7


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load("assets/white.jpg")
BACKGROUND_RECT = BACKGROUND.get_rect(center=(166, 220))
#ICON = pygame.image.load("src/Icon.png")

pygame.display.set_caption("Guess The Word")
#pygame.display.set_icon(ICON)

GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"
OUTLINE = "#d3d6da" #For empty letter
WHITE = (255,255,255)
FILLED_OUTLINE = "#878a8c" #For letter we have typed

CORRECT_WORD = "coder" #Correct Guess (u.l)
string1=""
string2=""
ALPHABET = []
letter_used=""

string1 = alph[:4]
string2 = alph[4:8]
done = list()
points = 0

ALPHABET.append(string1)
ALPHABET.append(string2)
# ALPHABET.append(alph)

#Fonts
GUESSED_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 40)
AVAILABLE_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 38)

#Screen and background display
SCREEN.fill("white")
SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
pygame.display.update()

#The letter being typed in the box
LETTER_X_SPACING = 55
LETTER_Y_SPACING = 100
LETTER_SIZE = 50

# Global variables

guesses_count = 0 #Guesses we have done, max is 6

# guesses is a 2D list that will store guesses. A guess will be a list of letters.
# The list will be iterated through and each letter in each guess will be drawn on the screen.
guesses = [[]] * 6 #Each list is one guess

current_guess = []
current_guess_string = ""
current_letter_bg_x = 200 #Where the next letter will be drawn on the x-axis

# Indicators is a list storing all the Indicator object. An indicator is that button thing with all the letters you see.
indicators = [] #Keyboard list

game_result = "" #W:win, L:Lost, Empty: Continue with the game


class Letter:
    def __init__(self, text, bg_position):
        # Initializes all the variables, including text, color, position, size, etc.
        self.bg_color = "white"
        self.text_color = "black"
        self.bg_position = bg_position
        self.bg_x = bg_position[0] #To get the x and y from our background position
        self.bg_y = bg_position[1]
        self.bg_rect = (bg_position[0], self.bg_y, LETTER_SIZE-3, LETTER_SIZE+5)
        self.text = text
        self.text_position = (self.bg_x + 23.5, self.bg_position[1] + 26) #has an offset of 34 and 36
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.text_position)

    def draw(self):
        # Puts the letter and text on the screen at the desired positions.
        pygame.draw.rect(SCREEN, self.bg_color, self.bg_rect)
        pygame.draw.rect(SCREEN, FILLED_OUTLINE, self.bg_rect, 3)
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        SCREEN.blit(self.text_surface, self.text_rect)
        pygame.display.update()

    def delete(self):
        # Fills the letter's spot with the default square, emptying it.
        pygame.draw.rect(SCREEN, "white", self.bg_rect)
        #pygame.draw.rect(SCREEN, OUTLINE, self.bg_rect, 3)
        pygame.display.update()


class Indicator:
    def __init__(self, x, y, letter):
        # Initializes variables such as color, size, position, and letter.
        self.x = x
        self.y = y
        self.text = letter
        self.rect = (self.x, self.y, 60, 60)
        self.bg_color = OUTLINE

    def draw(self):
        # Puts the indicator and its text on the screen at the desired position.
        pygame.draw.rect(SCREEN, self.bg_color, self.rect)
        self.text_surface = AVAILABLE_LETTER_FONT.render(self.text, True, "white")
        self.text_rect = self.text_surface.get_rect(center=(self.x + 30, self.y + 30))
        SCREEN.blit(self.text_surface, self.text_rect)
        pygame.display.update()


# Drawing the indicators on the screen.

indicator_x, indicator_y = 260, 300
# index = 0
for i in range(2):
    for letter in ALPHABET[i]:
        # index += 1
        new_indicator = Indicator(indicator_x, indicator_y, letter)
        indicators.append(new_indicator)
        new_indicator.draw()
        indicator_x += 68
        # if index == 4:
        #     break
    indicator_y += 75
    if i == 0:
        indicator_x = 260
    elif i == 1:
        indicator_x = 80

#Goes through each of the letter in our guess and checks whether they should be green, yellow or grey
def check_guess(guess_to_check):
    # Goes through each letter and checks if it should be green, yellow, or grey.
    global current_guess, current_guess_string,current_letter_bg_x
    current_letter_bg_x = 110
    guess_to_check[i].draw()
    pygame.display.update()
    print(current_guess_string)
    '''
    global current_guess, current_guess_string, guesses_count, current_letter_bg_x, game_result
    game_decided = False
    for i in range(5):
        lowercase_letter = guess_to_check[i].text.lower()
        if lowercase_letter in CORRECT_WORD:
            if lowercase_letter == CORRECT_WORD[i]:
                guess_to_check[i].bg_color = GREEN
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = GREEN
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                if not game_decided:
                    game_result = "W"
            else:
                guess_to_check[i].bg_color = YELLOW
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = YELLOW
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                game_result = ""
                game_decided = True
        else:
            guess_to_check[i].bg_color = GREY
            for indicator in indicators:
                if indicator.text == lowercase_letter.upper():
                    indicator.bg_color = GREY
                    indicator.draw()
            guess_to_check[i].text_color = "white"
            game_result = ""
            game_decided = True
        guess_to_check[i].draw()
        pygame.display.update()

    guesses_count += 1
    current_guess = []
    current_guess_string = ""
    current_letter_bg_x = 110

    if guesses_count == 6 and game_result == "":
        game_result = "L"
'''
#Puts Play Again text on the screen
def play_again():
    # Puts the play again text on the screen.
    pygame.draw.rect(SCREEN, "white", (10, 600, 1000, 600))
    play_again_font = pygame.font.Font("assets/FreeSansBold.otf", 40)
    play_again_text = play_again_font.render("Press ENTER to Play Again!", True, "black")
    play_again_rect = play_again_text.get_rect(center=(WIDTH / 2, 700))
    word_was_text = play_again_font.render(f"The word was {CORRECT_WORD}!", True, "black")
    word_was_rect = word_was_text.get_rect(center=(WIDTH / 2, 650))
    SCREEN.blit(word_was_text, word_was_rect)
    SCREEN.blit(play_again_text, play_again_rect)
    pygame.display.update()


def reset():
    # Resets all global variables to their default states.
    global guesses_count, CORRECT_WORD, guesses, current_guess, current_guess_string, game_result
    SCREEN.fill("white")
    SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
    guesses_count = 0
    # CORRECT_WORD = random.choice(WORDS)
    guesses = [[]] * 6
    current_guess = []
    current_guess_string = ""
    game_result = ""
    pygame.display.update()
    for indicator in indicators:
        indicator.bg_color = OUTLINE
        indicator.draw()

def reset_2():
    global guesses_count, CORRECT_WORD, guesses, current_guess, current_guess_string, game_result
    SCREEN.fill(WHITE, (0, 0, SCREEN.get_width()// 2, SCREEN.get_height()))
    #SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
    pygame.display.flip()
    guesses_count = 0
    # CORRECT_WORD = random.choice(WORDS)
    guesses = [[]] * 6
    current_guess = []
    current_guess_string = ""
    game_result = ""
    #pygame.display.update()
    for indicator in indicators:
        indicator.bg_color = OUTLINE
        indicator.draw()


#Allows us to type on the screen
def create_new_letter():
    # Creates a new letter and adds it to the guess.
    global current_guess_string, current_letter_bg_x
    current_guess_string += key_pressed
    new_letter = Letter(key_pressed, (current_letter_bg_x, guesses_count * 100 + LETTER_Y_SPACING))
    current_letter_bg_x += LETTER_X_SPACING
    guesses[guesses_count].append(new_letter)
    current_guess.append(new_letter)
    for guess in guesses:
        for letter in guess:
            letter.draw()


def delete_letter():
    # Deletes the last letter from the guess.
    global current_guess_string, current_letter_bg_x
    guesses[guesses_count][-1].delete()
    guesses[guesses_count].pop()
    current_guess_string = current_guess_string[:-1]
    current_guess.pop()
    current_letter_bg_x -= LETTER_X_SPACING

def score_show(x,y):
    score_disp = font_score.render("Score: " + str(score_value),True,(83,134,139))
    SCREEN.blit(score_disp,(x,y)) #Displaying score on the screen after render

while True:

    score_show(textX, textY)  # Calling score function
    if game_result != "":
        play_again()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: #The enter key
                if game_result != "": #If the game has finished
                    reset()
                else:
                    current_guess_string = current_guess_string.lower()
                    if len(current_guess_string) <= 8: #(and current_guess_string.lower() in WORDS) #Checking if our guess is a valid word.
                        # check_guess(current_guess) #Store the word (Minimum 8 words)
                        valid_word = word_check(current_guess_string, done, wavl)
                        if valid_word:
                            score_value += 5
                            print(score_value)
                            if points >= 25:
                                game_result = "W"
                        else:
                            if current_guess_string in done:
                                print("Duplicate entry not allowed")
                            else:
                                print("Invalid word")
                        # score_value += 1
                        reset_2()
                        #Remove the word from screen after storing, to give space for new words
            elif event.key == pygame.K_BACKSPACE: #Deleting a letter
                if len(current_guess_string) > 0:
                    letter_used = letter_used.replace(letter_used[-1],"")
                    delete_letter()
            else:
                key_pressed = event.unicode.upper()
                if key_pressed in string1.upper() or key_pressed in string2.upper() and key_pressed != "": #Only the words on keyboard should be in this string
                    if len(current_guess_string) <= 8 and key_pressed not in letter_used:
                        letter_used += key_pressed
                        create_new_letter()

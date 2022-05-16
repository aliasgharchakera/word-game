import pygame as pg


pg.init() #Initiating pygame
screen = pg.display.set_mode((640, 480)) #Game Window


#TextBox
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('floralwhite')
FONT = pg.font.Font(None, 32)

#score
score_value=0
font_score = pg.font.Font('freesansbold.ttf',16)
textX = 10
textY = 10


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)

def score_show(x,y):
    score_disp = font_score.render("Score:" + str(score_value),True,(255,255,255))
    screen.blit(score_disp,(x,y)) #Displaying score on the screen after render


def main():
    clock = pg.time.Clock() #Measuring our runtime
    #input_box1 = InputBox(100, 100, 140, 32)
    input_box2 = InputBox(210, 300, 140, 32)
    input_boxes = [input_box2]
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT: #Checking whether the player ended the game
                done = True

            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen.fill((255, 51, 51)) #Background Color
        for box in input_boxes:
            box.draw(screen)

        score_show(textX, textY) #Calling score function

        pg.display.flip()
        clock.tick(30) #We have 30 framespersec

if __name__ == '__main__':
    main()
    pg.quit()
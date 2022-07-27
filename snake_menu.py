import pygame_menu
from pygame_menu.examples import create_example_window
from snake.main import Snake
from typing import Tuple, Any
import json

#Constant
WINDOW_SIZE = (1080, 720)
SCORES = []

surface = create_example_window('Interactive Snake', WINDOW_SIZE)

# Functions
def start_the_game() -> None:
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """
    global user_name
    print(f'{user_name.get_value()}, Do the job here!')

    Snake.run(f'{user_name.get_value()}')

def show_highscores():
    fileData = 0
    with open('snake/highscore.json', 'r') as f:
        fileData = json.load(f)
        f.close()
    return fileData

SCORES = show_highscores()

# Styling
font = pygame_menu.font.FONT_OPEN_SANS_BOLD


mytheme = pygame_menu.Theme(title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
                            title_font=pygame_menu.font.FONT_OPEN_SANS_BOLD,
                            title_font_size=100, 
                            title_font_color=(255,255,255), 
                            title_offset=(345,0),
                            )

myimage = pygame_menu.baseimage.BaseImage(
    image_path="design/dungeon.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)
mytheme.background_color = myimage 

start = pygame_menu.baseimage.BaseImage(
    image_path="design/button_resume.png",
    
)

start = pygame_menu.baseimage.BaseImage(
    image_path="design/button_resume.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)

exit = pygame_menu.baseimage.BaseImage(
    image_path="design/button_exit.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)

score = pygame_menu.baseimage.BaseImage(
    image_path="design/button_score.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)

back = pygame_menu.baseimage.BaseImage(
    image_path="design/button_return.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)

menu = pygame_menu.Menu(
    height=WINDOW_SIZE[1],
    theme=mytheme,
    title='Mooove',
    width=WINDOW_SIZE[0]
)

score_menu = pygame_menu.Menu(
    height=WINDOW_SIZE[1],
    theme=mytheme,
    title='Highscores',
    width=WINDOW_SIZE[0]
)

for m in SCORES['highscores']:
    score_menu.add.label(m['username'] + ' - ' + str(m['score']), align=pygame_menu.locals.ALIGN_CENTER, font_color=(255,255,255), font_size=24)
score_menu.add.vertical_margin(30)
score_menu.add.button('                ', pygame_menu.events.BACK, background_color=exit, font_size=48, margin=(0,10))

user_name = menu.add.text_input('Name: ', default='Saul Goodman', maxchar=15, font_color=(255,255,255), font_size=24, margin=(0,20))
menu.add.button('                ', start_the_game, background_color=start, font_size=48, margin=(0,10))
menu.add.button('                ', score_menu, background_color=score, font_size=48, margin=(0,10))
menu.add.button('                ', pygame_menu.events.EXIT, background_color=exit, font_size=48, margin=(0,10))


if __name__ == '__main__':
    menu.mainloop(surface)
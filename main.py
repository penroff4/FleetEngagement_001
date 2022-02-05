import pygame
import sys
import logging
import pandas
import json

from button import Button
from inputbox import InputBox


############################## LOGGING VARS ####################################
logging.basicConfig(
    filename="LogFleetEngagement.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)

############################## PYGAME VARS #####################################
pygame.init()

FPS = 30
CLOCK = pygame.time.Clock()

SCREEN_HEIGHT = 1280
SCREEN_WIDTH = 720

SCREEN = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))

BACKGROUND = pygame.image.load("./assets/Background.png")

############################## FLEET ENGAGEMENT VARS ###########################

# var controls logic for initiating air related segments of combat
# if false, air interactions not allowed and/or skipped
AIR_ALLOWED = False

NAVAL_ATTACK_TABLE = pandas.read_csv(
        "./tables/navalAttackTablePivoted.csv")

COMBAT_METHODS_LIST = [
    'AIR',
    'FLEET',
    'NONE',
]

with open("./tables/nations.json") as json_file:
    NATIONS_DICT_LIST = json.load(json_file)

############################## GLOBAL METHODS ##################################

def get_font(size):
    return pygame.font.Font("./assets/font.ttf", size)

############################## GLOBAL MENU METHODS #############################

def choose_nations(engagement):
    """shows player nations they can choose to play as"""

    logging.info("beginning choose_nations(engagement)")

    player_count = 0
    
    for combatant in engagement.combatants_list:

        logging.info("player {} choosing combatant nation".format(combatant.short_designation_str))

        player_count = player_count + 1

        next_player = False
    
        while next_player is False:

            logging.info("beginning choose_nations(engagement) while next_player is False for combatant {}".format(combatant.short_designation_str))

            pygame.display.set_caption("Choose Nations")

            SCREEN.blit(BACKGROUND, (0,0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            # place holder, should progamatically indicate the desired player
            PLAYER_TITLE = get_font(50).render("Player {}...".format(player_count), True, "White")
            PLAYER_TITLE_RECT = PLAYER_TITLE.get_rect(center=(640,50))

            MENU_TEXT = get_font(50).render("Choose your nation", True, "White")
            MENU_RECT = MENU_TEXT.get_rect(center=(640,100))

            SCREEN.blit(PLAYER_TITLE, PLAYER_TITLE_RECT)
            SCREEN.blit(MENU_TEXT, MENU_RECT)
        
            GERMANY_BUTTON      = Button(
                image=pygame.image.load(NATIONS_DICT_LIST['Germany']['Flag']), 
                pos=(350,420), text_input="", font=get_font(30), 
                base_color="#d7fcd4", hovering_color="White")
            
            GERMANY_TEXT = get_font(30).render("Germany", True, "White")
            GERMANY_TEXT_RECT = GERMANY_TEXT.get_rect(center=(350,370))

            SCREEN.blit(GERMANY_TEXT, GERMANY_TEXT_RECT)
            
            ITALY_BUTTON        = Button(
                image=pygame.image.load(NATIONS_DICT_LIST['Italy']['Flag']), 
                pos=(650,420), text_input="", font=get_font(30), 
                base_color="#d7fcd4", hovering_color="White")
            
            ITALY_TEXT = get_font(30).render("Italy", True, "White")
            ITALY_TEXT_RECT = ITALY_TEXT.get_rect(center=(650,370))

            SCREEN.blit(ITALY_TEXT, ITALY_TEXT_RECT)
                
            JAPAN_BUTTON        = Button(
                image=pygame.image.load(NATIONS_DICT_LIST['Japan']['Flag']), 
                pos=(950,420), text_input="", font=get_font(30), 
                base_color="#d7fcd4", hovering_color="White")
            
            JAPAN_TEXT = get_font(30).render("Japan", True, "White")
            JAPAN_TEXT_RECT = JAPAN_TEXT.get_rect(center=(950,370))

            SCREEN.blit(JAPAN_TEXT, JAPAN_TEXT_RECT)
            
            COMMONWEALTH_BUTTON = Button(
                image=pygame.image.load(NATIONS_DICT_LIST['Commonwealth']['Flag']), 
                pos=(350,540), text_input="", font=get_font(30), 
                base_color="#d7fcd4", hovering_color="White")

            COMMONWEALTH_TEXT = get_font(30).render("Commonwealth", True, "White")
            COMMONWEALTH_TEXT_RECT = COMMONWEALTH_TEXT.get_rect(center=(350,490))

            SCREEN.blit(COMMONWEALTH_TEXT, COMMONWEALTH_TEXT_RECT)        
            
            FRANCE_BUTTON       = Button(
                image=pygame.image.load(NATIONS_DICT_LIST['France']['Flag']), 
                pos=(650,540), text_input="", font=get_font(30), 
                base_color="#f6fa00", hovering_color="White")
            FRANCE_TEXT = get_font(30).render("France", True, "White")
            FRANCE_TEXT_RECT = FRANCE_TEXT.get_rect(center=(650,490))

            SCREEN.blit(FRANCE_TEXT, FRANCE_TEXT_RECT)        
            
            RUSSIA_BUTTON       = Button(
                image=pygame.image.load(NATIONS_DICT_LIST['Russia']['Flag']), 
                pos=(950,540), text_input="", font=get_font(30), 
                base_color="#d7fcd4", hovering_color="White")
            RUSSIA_TEXT = get_font(30).render("Russia", True, "White")
            RUSSIA_TEXT_RECT = RUSSIA_TEXT.get_rect(center=(950,490))

            SCREEN.blit(RUSSIA_TEXT, RUSSIA_TEXT_RECT)        
            
            USA_BUTTON          = Button(
                image=pygame.image.load(NATIONS_DICT_LIST['United States']['Flag']), 
                pos=(650,300), text_input="", font=get_font(30), 
                base_color="#d7fcd4", hovering_color="White")

            USA_TEXT = get_font(30).render("USA", True, "White")
            USA_TEXT_RECT = USA_TEXT.get_rect(center=(650,250))

            SCREEN.blit(USA_TEXT, USA_TEXT_RECT)        

            buttons_list = [
                {'button': GERMANY_BUTTON,      'nation': 'Germany'},
                {'button': ITALY_BUTTON,        'nation': 'Italy'},
                {'button': JAPAN_BUTTON,        'nation': 'Japan'},
                {'button': COMMONWEALTH_BUTTON, 'nation': 'Commonwealth'}, 
                {'button': FRANCE_BUTTON,       'nation': 'France'}, 
                {'button': RUSSIA_BUTTON,       'nation': 'Russia'}, 
                {'button': USA_BUTTON,          'nation': 'United States'}
            ]

            for button in buttons_list:
                button['button'].changeColor(MENU_MOUSE_POS)
                button['button'].update(SCREEN)

            events = pygame.event.get()

            for event in events:

                if event.type == pygame.QUIT:
                    logging.info("event.type triggered pygame.QUIT")
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    for button in buttons_list:

                        if button['button'].checkForInput(MENU_MOUSE_POS):
                            
                            logging.info("combatant {} choose {}".format(combatant.short_designation_str, button['nation']))
                            logging.info("setting combatant {} nation_str, national_adjective_str, flag_str attributes".format(combatant.short_designation_str))
                            
                            combatant.nation_str = button['nation']
                            combatant.national_adjective_str = NATIONS_DICT_LIST[combatant.nation_str]['Adjective']
                            combatant.flag_str = NATIONS_DICT_LIST[combatant.nation_str]['Flag']
                            
                            next_player = True

            pygame.display.update()

def choose_fleet_comp(engagement):
    """ask per player how many task forces in their fleet"""

    logging.info("setting choose_fleet_comp(engagement) combatant_count to zero")
    combatant_count = 0
    
    for combatant in engagement.combatants_list:

        logging.info("beginning fleet_comp for combatant {}".format(combatant.short_designation_str))

        combatant_count = combatant_count + 1

        next_combatant = False
    
        while next_combatant is False:

            logging.info("beginning while next_combatant is False")

            pygame.display.set_caption("Determine number of Taskforces")

            SCREEN.blit(BACKGROUND, (0,0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            logging.info("setting PLAYER_TITLE, PLAYER_TITLE_RECT")
            
            PLAYER_TITLE = get_font(50).render("Player {}...".format(combatant_count), True, "White")
            PLAYER_TITLE_RECT = PLAYER_TITLE.get_rect(center=(640,50))

            logging.info("setting MENU_TEXT, MENU_RECT")
            MENU_TEXT = get_font(30).render("Enter number of Taskforces", True, "White")
            MENU_RECT = MENU_TEXT.get_rect(center=(640,150))

            PLAYER_INPUT_RECT = InputBox(
                510,370, 140, 32, get_font(12), 
                pygame.Color(0,0,0), pygame.Color(255,255,0), text='')

            logging.info("blit-ing MENU_TEXT, MENU_RECT")
            SCREEN.blit(PLAYER_TITLE, PLAYER_TITLE_RECT)
            SCREEN.blit(MENU_TEXT, MENU_RECT)

            events = pygame.event.get()
            
            for event in events:

                if event.type == pygame.QUIT:
                    logging.info("event.type triggered pygame.QUIT")
                    pygame.quit()
                    sys.exit()

                PLAYER_INPUT_RECT.handle_event(event)
            
            PLAYER_INPUT_RECT.update()
            PLAYER_INPUT_RECT.draw(SCREEN)
        
            logging.info("pygame.display.update()")
            pygame.display.flip()

def main_menu(engagement):

    while True:

        logging.info("beginning main_menu() while True")

        pygame.display.set_caption("Menu")
        
        SCREEN.blit(BACKGROUND, (0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(75).render("FLEET ENGAGEMENT", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("./assets/Play Rect.png"), 
                             pos=(640,250), text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        QUIT_BUTTON = Button(image=pygame.image.load("./assets/Quit Rect.png"), 
                             pos=(640,450), text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    logging.info("MENU_MOUSE_POS MOUSBUTTONDOWN triggered choose_nations(engagement)")
                    choose_nations(engagement)

                    # if combatants have nations assigned, call fleet comp
                    logging.info("Confirming all combatants have nation assigned")
                    combatant_has_nation_count = 0

                    for combatant in engagement.combatants_list:
                        logging.info("Confirming combatant {} has nation assigned".format(combatant.short_designation_str))

                        if combatant.nation_str in list(NATIONS_DICT_LIST.keys()):
                            logging.info("Combatant {} has nation {} assigned, matches NATIONS_LIST".format(combatant.short_designation_str, combatant.nation_str))
                            combatant_has_nation_count = combatant_has_nation_count + 1

                        else:
                            logging.info("Combatant {} does not have nation from NATIONS_LIST assigned.  Has {} assigned instead".format(combatant.short_designation_str, combatant.nation_str))
                    
                    if combatant_has_nation_count == len(engagement.combatants_list):
                        logging.info("All combatants have proper nations assigned")
                        logging.info("Executing choose_fleet_comp(engagement)")
                        choose_fleet_comp(engagement)
                
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    logging.info("MENU_MOUSE_POS MOUSBUTTONDOWN triggered QUIT_BUTTON's pygame.quit()")
                    pygame.quit()
                    sys.exit()

        #pygame.display.update()
        pygame.display.flip()

############################## CLASSES #########################################

class Combatant(object):
    """i.e. a player, or nation; handles combatant details"""
    def __init__(self, short_designation):
        self.short_designation_str = short_designation
        self.nation_str = None
        self.national_adjective_str = None
        self.flag_str = None
        self.fleet_composition_list = []
        self.round_search_results_int = 0
        self.search_rolls_list = []
        self.withdrawal_decision_bool = None
        self.allocated_search_results_list = []


class FleetEngagement(object):
    """
    a fleet engagement between two nationalities, 
    generates TFs as well as ship composition of those TFs
    """

    def __init__(self):

        sideA = Combatant("sideA")
        sideB = Combatant("sideB")

        self.combatants_list = [
            sideA,
            sideB
        ]

############################## IF __MAIN__ #####################################
if __name__ == "__main__":
    
    logging.info("FleetEngagement.py executed as __main__")
    
    logging.info("Instantiating Fleet Engagement object")
    engagement = FleetEngagement()
    
    while True:
        logging.info("calling main_menu")
        main_menu(engagement)

        CLOCK.tick(FPS)
import pygame
import sys
import logging
import pandas

from button import Button

logging.basicConfig(
    filename="LogFleetEngagement.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)

############################## PYGAME VARS #####################################
pygame.init()

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

COMBATANT_NATIONS_FLAGS_DICT = {
        "GERMANY":"./assets/awaw_images/german/German_Marker_Flag.png",
        "UNITED STATES":"./assets/awaw_images/usa/US_Marker_Flag.png",
        "ITALY":"./assets/awaw_images/italy/Italy_Marker_Flag.png",
        "JAPAN":"./assets/awaw_images/japan/Japan_Marker_Flag.png",
        "COMMONWEALTH":"./assets/awaw_images/commonwealth/Brit_Marker_Flag.png",
        "FRANCE":"./assets/awaw_images/france/France_Marker_Flag.png",
        "RUSSIA":"./assets/awaw_images/russia/Russia_Marker_Flag.png",
    }

NATIONAL_ADJECTIVES_DICT = {
        "GERMANY": "GERMAN",
        "UNITED STATES": "AMERICAN",
        "ITALY": "ITALIAN",
        "JAPAN": "JAPANESE",
        "COMMONWEALTH": "COMMONWEALTH",
        "FRANCE": "FRENCH",
        "RUSSIA": "RUSSIAN",
    }

############################## GLOBAL METHODS ##################################

def get_font(size):
    return pygame.font.Font("./assets/font.ttf", size)
         
def choose_combatants(engagement):
    """shows player nations they can choose to play as"""

    player_count = 0
    
    for combatant in engagement.combatants_list:

        player_count = player_count + 1

        next_player = False
    
        while next_player is False:

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
                image=pygame.image.load(COMBATANT_NATIONS_FLAGS_DICT['GERMANY']), 
                pos=(350,420), text_input="", font=get_font(30), 
                base_color="#d7fcd4", hovering_color="White")
            
            GERMANY_TEXT = get_font(30).render("Germany", True, "White")
            GERMANY_TEXT_RECT = GERMANY_TEXT.get_rect(center=(350,370))

            SCREEN.blit(GERMANY_TEXT, GERMANY_TEXT_RECT)
            
            ITALY_BUTTON        = Button(
                image=pygame.image.load(COMBATANT_NATIONS_FLAGS_DICT['ITALY']), 
                pos=(650,420), text_input="", font=get_font(30), 
                base_color="#d7fcd4", hovering_color="White")
            
            ITALY_TEXT = get_font(30).render("Italy", True, "White")
            ITALY_TEXT_RECT = ITALY_TEXT.get_rect(center=(650,370))

            SCREEN.blit(ITALY_TEXT, ITALY_TEXT_RECT)
                
            JAPAN_BUTTON        = Button(
                image=pygame.image.load(COMBATANT_NATIONS_FLAGS_DICT['JAPAN']), 
                pos=(950,420), text_input="", font=get_font(30), 
                base_color="#d7fcd4", hovering_color="White")
            
            JAPAN_TEXT = get_font(30).render("Japan", True, "White")
            JAPAN_TEXT_RECT = JAPAN_TEXT.get_rect(center=(950,370))

            SCREEN.blit(JAPAN_TEXT, JAPAN_TEXT_RECT)
            
            COMMONWEALTH_BUTTON = Button(
                image=pygame.image.load(COMBATANT_NATIONS_FLAGS_DICT['COMMONWEALTH']), 
                pos=(350,540), text_input="", font=get_font(30), 
                base_color="#d7fcd4", hovering_color="White")

            COMMONWEALTH_TEXT = get_font(30).render("Commonwealth", True, "White")
            COMMONWEALTH_TEXT_RECT = COMMONWEALTH_TEXT.get_rect(center=(350,490))

            SCREEN.blit(COMMONWEALTH_TEXT, COMMONWEALTH_TEXT_RECT)        
            
            FRANCE_BUTTON       = Button(
                image=pygame.image.load(COMBATANT_NATIONS_FLAGS_DICT['FRANCE']), 
                pos=(650,540), text_input="", font=get_font(30), 
                base_color="#f6fa00", hovering_color="White")
            FRANCE_TEXT = get_font(30).render("France", True, "White")
            FRANCE_TEXT_RECT = FRANCE_TEXT.get_rect(center=(650,490))

            SCREEN.blit(FRANCE_TEXT, FRANCE_TEXT_RECT)        
            
            RUSSIA_BUTTON       = Button(
                image=pygame.image.load(COMBATANT_NATIONS_FLAGS_DICT['RUSSIA']), 
                pos=(950,540), text_input="", font=get_font(30), 
                base_color="#d7fcd4", hovering_color="White")
            RUSSIA_TEXT = get_font(30).render("Russia", True, "White")
            RUSSIA_TEXT_RECT = RUSSIA_TEXT.get_rect(center=(950,490))

            SCREEN.blit(RUSSIA_TEXT, RUSSIA_TEXT_RECT)        
            
            USA_BUTTON          = Button(
                image=pygame.image.load(COMBATANT_NATIONS_FLAGS_DICT['UNITED STATES']), 
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
                {'button': USA_BUTTON,          'nation': 'USA'}
            ]

            for button in buttons_list:
                button['button'].changeColor(MENU_MOUSE_POS)
                button['button'].update(SCREEN)

            events = pygame.event.get()

            for event in events:

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    for button in buttons_list:
                        if button['button'].checkForInput(MENU_MOUSE_POS):
                            combatant.nationality = button['nation']
                            next_player = True
                            #choose_combatants(engagement)
                    # for button in button_list:
                        # if button.checkForInput(MENU_MOUSE_POS):
                            # log player's choice of combatant

            pygame.display.update()

def choose_fleet_comp(engagement):
    """ask per player how many task forces in their fleet"""

    player_count = 0
    
    for combatant in engagement.combatants_list:

        player_count = player_count + 1

        next_player = False
    
        while next_player is False:

            pygame.display.set_caption("Determine number of Taskforces")

            SCREEN.blit(BACKGROUND, (0,0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            # place holder, should progamatically indicate the desired player
            PLAYER_TITLE = get_font(50).render("Player {}...".format(player_count), True, "White")
            PLAYER_TITLE_RECT = PLAYER_TITLE.get_rect(center=(640,50))

            MENU_TEXT = get_font(50).render("Choose your nation", True, "White")
            MENU_RECT = MENU_TEXT.get_rect(center=(640,100))

            SCREEN.blit(PLAYER_TITLE, PLAYER_TITLE_RECT)
            SCREEN.blit(MENU_TEXT, MENU_RECT)

def main_menu(engagement):
    while True:
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

        #for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    choose_combatants(engagement)
                
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

############################## CLASSES #########################################

class Combatant(object):
    """i.e. a player, or nation; handles combatant details"""
    def __init__(self, short_designation):
        self.short_designation_str = short_designation
        self.nationality_str = None
        self.national_adjective_str = None
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
    
    engagement = FleetEngagement()
    
    while True:
        main_menu(engagement)
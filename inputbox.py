import pygame

class InputBox(object):

    def __init__(self, x, y, width, height, font, color_inactive, color_active, text=''):
        """color_inactive and color_active should be pygame.Color() objects, font should be pygame.font.Font() object"""
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color_inactive
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False
        self.color_active = color_active
        self.color_inactive = color_inactive
        self.font = font

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect
            if self.rect.collidepoint(event.pos):
                # Toggle the active var
                self.active = not self.active
            else:
                self.active = False

            # Change the current color of the input box
            self.color = self.color_active if self.active else self.color_inactive

        if event.type == pygame.KEYDOWN:

            if self.active:
            
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
            
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
            
                else:
                    self.text += event.unicode
            
                #re-render the text
                self.txt_surface = self.font.render(self.text, True, self.color)
    
    def update(self):
        # resize the box if the text is too long
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # blit the text
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # blit the rect
        pygame.draw.rect(screen, self.color, self.rect, 2)


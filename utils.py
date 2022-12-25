import pygame

class button():
    def __init__(self, screen, text, x, y, tamx, tamy, col):
        self.tamt = (tamx + tamy) * 0.25
        button_font = pygame.font.SysFont('arialcursiva', int(self.tamt))
        self.text = text
        button_text = button_font.render(self.text, False, (255, 255, 255,))
        self.screen = screen
        self.x = x
        self.y = y
        self.tamx = tamx
        self.tamy = tamy
        rect = button_text.get_rect(center =(x+tamx/2 , y+tamy/2))
        self.col = col
        pygame.draw.rect(self.screen, col, (x, y, tamx, tamy), border_radius = 5)
        self.screen.blit(button_text, rect)
    
    def check(self):
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        if mouseX >= self.x and mouseX <= self.x+self.tamx:
            if mouseY >= self.y and mouseY <= self.y+self.tamy:
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    return True
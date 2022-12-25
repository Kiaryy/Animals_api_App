import pygame
from event_handler import event_handler
from image_handler import image_handler
from utils import button

def main():
    pygame.init()
    width, height = 800,600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Animals!!!")
    clock = pygame.time.Clock()
    image = image_handler(screen)
    img = image.get_cat()

    while True:
        screen.fill((255, 150, 100))
        
        image.draw_img(img)
        
        new_cat = button(screen, "Cat!",400-50, image.img_to_draw.get_height() +50, 100, 50, (0, 255, 0))
        if new_cat.check():
            img = image.get_cat()
        
        new_dog = button(screen, "Dog!",400-200, image.img_to_draw.get_height() +50, 100, 50, (255, 0, 0))
        if new_dog.check():
            img = image.get_dog()
        
        new_fox = button(screen, "Fox!",400+100, image.img_to_draw.get_height() +50, 100, 50, (0, 0, 255))
        if new_fox.check():
            img = image.get_fox()
        
        event_handler()
        
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
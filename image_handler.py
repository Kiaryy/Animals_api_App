import pygame, requests, sys, io
from tkinter import messagebox

class image_handler:
    def __init__(self, screen):
        self.screen = screen
        
        self.cat_url = 'https://api.thecatapi.com/v1/images/search'
        
        self.dog_url = 'https://dog.ceo/api/breeds/image/random'
        
        self.fox_url = "https://randomfox.ca/floof/"
        
        #Check for internet connection when starting
        try:
            requests.get('https://www.google.com/')
        except requests.ConnectionError:
            messagebox.showerror('Connection Error', "Error: You don't have a stable connection and the program couldn't start.\nRestart your wifi and try again.")
            pygame.quit()
            sys.exit()
    
    def get_cat(self):
        try:
            r = requests.get(self.cat_url) 
        except requests.ConnectionError:
            messagebox.showerror('Connection Error', "Error: You don't have a stable connection and the image couldn't load.\nRestart your wifi and try again.")
            pygame.quit()
            sys.exit()
        
        response_dict = r.json()
        response = requests.get(response_dict[0]['url'])
        img_data = response.content
        
        return img_data
    
    def get_dog(self):
        try:
            r = requests.get(self.dog_url)   
        except requests.ConnectionError:
            messagebox.showerror('Connection Error', "Error: You don't have a stable connection and the image couldn't load.\nRestart your wifi and try again.")
            pygame.quit()
            sys.exit()
        
        response_dict = r.json()
        response = requests.get((response_dict['message']))
        img_data = response.content
        
        return img_data
    
    def get_fox(self):
        try:
            r = requests.get(self.fox_url)   
        except requests.ConnectionError:
            messagebox.showerror('Connection Error', "Error: You don't have a stable connection and the image couldn't load.\nRestart your wifi and try again.")
            pygame.quit()
            sys.exit()
        
        response_dict = r.json()
        response = requests.get((response_dict['image']))
        img_data = response.content
        
        return img_data
    
    def draw_img(self, img_data):
        img = io.BytesIO(img_data)
        self.img_to_draw = pygame.image.load(img)
        if self.img_to_draw.get_width() + self.img_to_draw.get_height() > 700:
            while self.img_to_draw.get_width() + self.img_to_draw.get_height() > 700:
                self.img_to_draw = pygame.transform.scale(self.img_to_draw,(self.img_to_draw.get_width()*.8, self.img_to_draw.get_height()*0.8))
        
        self.screen.blit(self.img_to_draw, (400- self.img_to_draw.get_width()/2, 20))

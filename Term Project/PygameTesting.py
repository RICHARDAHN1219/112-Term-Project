import pygame
#Taken from https://www.simplifiedpython.net/pygame-sprite-animation-tutorial/
#Will be used for different images to be implemented inside my game
 
SIZE = WIDTH, HEIGHT = 600, 400 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white') #The background colod of our window
FPS = 10 #Frames per second
 
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
 
        self.hitImages = []
        #All images below taken from volleyball challenge game default sprite
        #https://www.youtube.com/watch?v=09JQShQtTfI&t=148s&ab_channel=PryszardAndroidiOSGameplays
        self.hitImages.append(pygame.image.load('images/hit1.png')) 
        self.hitImages.append(pygame.image.load('images/hit2.png'))
        self.hitImages.append(pygame.image.load('images/hit3.png'))
        self.hitImages.append(pygame.image.load('images/hit4.png'))
        self.hitImages.append(pygame.image.load('images/hit5.png'))
        self.hitImages.append(pygame.image.load('images/hit6.png'))
        self.hitImages.append(pygame.image.load('images/hit7.png'))
        self.hitImages.append(pygame.image.load('images/hit8.png'))

        self.walkImages = []
        self.walkImages.append(pygame.image.load('images/walk1.png'))
        self.walkImages.append(pygame.image.load('images/walk2.png'))
        self.walkImages.append(pygame.image.load('images/walk3.png'))
        self.walkImages.append(pygame.image.load('images/walk4.png'))
        self.walkImages.append(pygame.image.load('images/walk5.png'))
        self.walkImages.append(pygame.image.load('images/walk6.png'))
        self.walkImages.append(pygame.image.load('images/walk7.png'))
        self.walkImages.append(pygame.image.load('images/walk8.png'))

        self.index = 0
 
        self.image = self.hitImages[self.index]
 
        self.rect = pygame.Rect(5, 5, 150, 198)

    def update(self):
        self.index += 1
 
        if self.index >= len(self.hitImages):
            self.index = 0
        
        self.image = self.hitImages[self.index]


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)
    #my_group2 = pygame.sprite.Group(my_sprite2)
    clock = pygame.time.Clock()
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
        my_group.update()
        screen.fill(BACKGROUND_COLOR)
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(10)
 
if __name__ == '__main__':
    main()
 
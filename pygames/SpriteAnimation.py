import os
import pygame


# Loads all images in directory (must only contain images)
def load_images(path):
    
    # count = 0

    images = []

    # images = {} 
    
    for filename in os.listdir(path):
        # count += 1

        if filename.endswith('.jpg'):
            # path_new = os.path.join(path, filename)
            # key = filename[:-4]
            # images[key] = pygame.image.load(path_new).convert()

            path_new = os.path.join(path, filename)
            image = pygame.image.load(path_new).convert()
            images.append(image)
            
            # print(str(count))
    
    print(str(len(images)))  
    return images # list of images 
###


class SpriteAnimation(pygame.sprite.Sprite):

    # position - x & y coordinates
    # images - images from load_image function
    def __init__(self, position, images):
        
        super(SpriteAnimation, self).__init__()

        size = (images[0].get_size()[0] , images[0].get_size()[1] ) #size of images

        self.index = 0 
        self.image = images[self.index]
        self.rect = pygame.Rect(position, size)

    def update(self,images):

        self.index += 1

        # go back to image 1 when last image is reached
       
        if self.index >= len(images): 
            self.index = 0

        self.image = images[self.index] 

        
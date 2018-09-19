import pygame
from SpriteAnimation import *


WHITE = (255, 255, 255, 255)


def main():

	#pygame setup
	pygame.init()
	clock = pygame.time.Clock()
	SCREENSIZE = (1000,1000) # set to background size
	screen = pygame.display.set_mode(SCREENSIZE)



	img = pygame.image.load("images/pixelated_samoyed.jpg")

	# This image will always be on the bottom left corner of screen - using SCREENSIZE
	# height X width
	# img_pos = ( (SCREENSIZE[0]-SCREENSIZE[0]), (SCREENSIZE[1] - img.get_size()[1]) )

	img_pos = ( 0,0 )

	background_images = load_images("images/Orbitals_Background_Sprite")

	background_sprite = SpriteAnimation((0,0),background_images)

	background_group = pygame.sprite.Group(background_sprite)

	running = True
	while running:

		# background_images = load_images("Images/Orbitals_Background_Sprite")

		#check if window was closed
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False


		#draw graphics to screen
		screen.fill(WHITE)

		# sprite
		background_group.update(background_images)
		background_group.draw(screen)

		# blit image onto screen surface
		screen.blit(img,img_pos)

		pygame.display.flip()
		clock.tick(30)

	pygame.quit()


if __name__ == '__main__':
    main()

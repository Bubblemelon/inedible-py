import pygame


WHITE = (255, 255, 255, 255)


def main():

	#pygame setup
	pygame.init()
	clock = pygame.time.Clock()
	screenSize = (500,500)
	screen = pygame.display.set_mode(screenSize)


	img = pygame.image.load("/Users/CherylFong/Desktop/Github/inedible-py/Images/pixelated_samoyed.jpg")
	
	# This image will always be on the bottom left corner of screen - using screenSize
	img_pos = ( (screenSize[0]-screenSize[0]), (screenSize[1] - img.get_size()[1]) )

	running = True
	while running:

		#check if window was closed
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		
		#draw graphics to screen
		screen.fill(WHITE)
		
		# blit image onto screen surface
		screen.blit(img,img_pos)

		# sprite
		
		
		pygame.display.flip()
		clock.tick(30)

	pygame.quit()


if __name__ == '__main__':
    main()
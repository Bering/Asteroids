import pygame
from game_object import GameObject

class Player(GameObject):
	def __init__(self):
		super().__init__("player.png", 300, 300, 0, 0)

	def events(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
				self.rotate_left()
			elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
				self.rotate_right()
			elif event.key == pygame.K_SPACE:
				self.fire()

	def rotate_left(self):
		pass

	def rotate_right(self):
		pass

	def fire(self):
		pass

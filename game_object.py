import os
import pygame

class GameObject:

	def __init__(self, image, x, y, vx, vy):
		image_file = os.path.join("images", image)
		self.surface = pygame.image.load(image_file).convert_alpha()
		self.rect = self.surface.get_rect().move(x, y)
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.is_dead = False

	def events(self, event):
		pass

	def update(self, delta_time):
		self.x += self.vx
		self.y += self.vy
		self.rect.center = (self.x, self.y)

	def render(self, surface, rect):
		surface.blit(self.surface, self.rect)

	def collision(self, other_game_object):
		pass

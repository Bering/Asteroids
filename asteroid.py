import pygame
import random
from game_object import GameObject

class Asteroid(GameObject):
	def __init__(self, size):
		self.size = size
		if size == 3:
			image = "asteroid_big.png"
		elif size == 2:
			image = "asteroid_small.png"
		else:
			image = "asteroid_tiny.png"

		side = random.randrange(4)
		if side == 0:
			y = 0
			x =random.randrange(600)
			vx = random.uniform(-1.0, 1.0)
			vy = random.uniform(0.1, 1.0)
		elif side == 1:
			x = 600
			y = random.randrange(600)
			vx = random.uniform(-1.0, -0.1)
			vy = random.uniform(-1.0, 1.0)

		elif side == 2:
			x = random.randrange(600)
			y = 600
			vx = random.uniform(-1.0, 1.0)
			vy = random.uniform(-1.0, -0.1)
		else:
			x = 0
			y = random.randrange(600)
			vx = random.uniform(0.1, 1.0)
			vy = random.uniform(-1.0, 1.0)

		super().__init__(image, x, y, vx, vy)
		self.unrotated_surface = self.surface
		self.rotation_speed = random.randint(-1, 1)
		self.angle = random.randint(0, 359)

	def update(self, delta_time):
		self.angle = self.clamp_angle(self.angle + self.rotation_speed)
		self.surface = pygame.transform.rotate(self.unrotated_surface, self.angle)
		new_rect = self.surface.get_rect()
		new_rect.center = self.rect.center
		self.rect = new_rect
		super().update(delta_time)

	def clamp_angle(self, angle):
		while angle >= 360:
			angle -= 360
		while angle < 0:
			angle += 360
		return angle

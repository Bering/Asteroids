import pygame
import random
from game_object import GameObject

class Asteroid(GameObject):
	def __init__(self, size):
		if size == 3:
			image = "asteroid_big.png"
		elif size == 2:
			image = "asteroid_small.png"
		else
			image = "asteroid_tiny.png"

		vx = vy = 0
		while vx == vy == 0:
			if random.randint(0, 1) == 0:
				x = 0
				vx = random.uniform(0.1, 1.0)
			else:
				x = 600
				vx = random.uniform(-1.0, -0.1)

			if random.randint(0, 1) == 0:
				y = 0
				vy = random.uniform(0.1, 1.0)
			else:
				y = 600
				vy = random.uniform(-1.0, -0.1)

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

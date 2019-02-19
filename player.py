import pygame
from game_object import GameObject

class Player(GameObject):
	def __init__(self):
		super().__init__("player.png", 300, 300, 0, 0)
		self.unrotated_surface = self.surface
		self.rotation_speed = 0
		self.angle = 0

	def events(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
				self.rotate_left()
			elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
				self.rotate_right()
			elif event.key == pygame.K_SPACE:
				self.fire()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
				self.rotate_none()
			elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
				self.rotate_none()
			elif event.key == pygame.K_SPACE:
				self.fire_hold()

	def rotate_left(self):
		self.rotation_speed = 5

	def rotate_right(self):
		self.rotation_speed = -5

	def rotate_none(self):
		self.rotation_speed = 0

	def fire(self):
		pass

	def fire_hold(self):
		pass

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

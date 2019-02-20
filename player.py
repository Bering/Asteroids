import math
import pygame
from game_object import GameObject
from bullet import Bullet

class Player(GameObject):
	def __init__(self, app):
		super().__init__("player.png", 300, 300, 0, 0)
		self.unrotated_surface = self.surface
		self.rotation_speed = 0
		self.angle = 0
		self.app = app
		self.fire_sound = pygame.mixer.Sound("Sounds/fire.ogg")

	def events(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
				self.rotate_left()
			elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
				self.rotate_right()
			elif event.key == pygame.K_UP or event.key == pygame.K_KP8:
				self.forward()
			elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
				self.backwards()
			elif event.key == pygame.K_SPACE:
				self.fire()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
				self.rotate_none()
			elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
				self.rotate_none()

	def rotate_left(self):
		self.rotation_speed = 5

	def rotate_right(self):
		self.rotation_speed = -5

	def rotate_none(self):
		self.rotation_speed = 0

	def forward(self):
		self.vx -= math.sin(math.radians(self.angle))
		self.vy -= math.cos(math.radians(self.angle))

	def backwards(self):
		self.vx += math.sin(math.radians(self.angle))
		self.vy += math.cos(math.radians(self.angle))

	def fire(self):
		self.app.game_objects.append(Bullet(self))
		self.fire_sound.play()

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

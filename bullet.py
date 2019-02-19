from game_object import GameObject
import math

class Bullet(GameObject):
	def __init__(self, player):
		x = player.rect.center[0] + math.sin(math.radians(player.angle+180)) * 10
		y = player.rect.center[1] + math.cos(math.radians(player.angle+180)) * 10
		vx = math.sin(math.radians(player.angle+180)) * 5
		vy = math.cos(math.radians(player.angle+180)) * 5
		super().__init__("bullet.png", x, y, vx, vy)

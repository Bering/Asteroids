from game_object import GameObject
import math

class Bullet(GameObject):
	def __init__(self, player):
		x = player.rect.center[0] + math.cos(player.angle) * 16
		y = player.rect.center[1] + math.sin(player.angle) * 16
		vx = math.cos(player.angle) * 5
		vy = math.sin(player.angle) * 5
		super().__init__("bullet.png", x, y, vx, vy)

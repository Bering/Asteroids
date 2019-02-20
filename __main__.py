import pygame
from game_object import GameObject
from player import Player
from bullet import Bullet
from asteroid import Asteroid

class Application:

	def __init__(self):
		pygame.init()
		pygame.display.set_caption("Asteroid Alpha 0.1")
		self.surface = pygame.display.set_mode((600, 600))
		self.rect = self.surface.get_rect()
		self.game_objects = []

		self.player = Player(self)
		self.game_objects.append(self.player)

	def run(self):
		self.quit = False
		self.clock = pygame.time.Clock()
		pygame.time.set_timer(pygame.USEREVENT, 2000)

		while(not self.quit):
			self.clock.tick(60)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit = True
				elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
					self.quit = True
				elif event.type == pygame.USEREVENT:
					self.game_objects.append(Asteroid(3))
				else:
					for go in self.game_objects:
						go.events(event)

			for go in self.game_objects:
				go.update(self.clock.get_time())
				self.remove_if_out_of_frame(go)

			for go in self.game_objects:
				for ogo in self.game_objects:
					if ogo == go: continue
					if not go.rect.colliderect(ogo.rect): continue
					# TODO: circle collider
					self.collision(go, ogo)

			self.game_objects = [go for go in self.game_objects if not go.is_dead]

			self.surface.fill((0, 0, 0))
			for go in self.game_objects:
				go.render(self.surface, self.rect)
			pygame.display.flip()

	def on_quit(self):
		self.quit = True

	def remove_if_out_of_frame(self, game_object):
		minx = 0 - game_object.rect.width
		maxx = self.rect.width + game_object.rect.width
		miny = 0 - game_object.rect.height
		maxy = self.rect.height + game_object.rect.height
		
		if game_object.rect.center[0] < minx \
		or game_object.rect.center[0] > maxx \
		or game_object.rect.center[1] < miny \
		or game_object.rect.center[1] > maxy:
			game_object.is_dead = True

	def collision(self, go, ogo):
		if not isinstance(go, Asteroid):
			return

		if isinstance(ogo, Asteroid):
			return

		if isinstance(ogo, Player):
			# TODO: Proper death screen
			print("You are dead!")
			self.quit = True
			return

		go.is_dead = True
		ogo.is_dead = True
		
		if go.size > 1:
			a = Asteroid(go.size - 1)
			a.x = go.rect.center[0]
			a.y = go.rect.center[1]
			self.game_objects.append(a)

			a = Asteroid(go.size - 1)
			a.x = go.rect.center[0]
			a.y = go.rect.center[1]
			self.game_objects.append(a)

print("Asteroid alpha0")
app = Application()
app.run()

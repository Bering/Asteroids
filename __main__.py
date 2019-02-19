import pygame

class Application:

	def __init__(self):
		pygame.init()
		pygame.display.set_caption("Asteroid Alpha 0.1")
		self.surface = pygame.display.set_mode((600, 600))
		self.rect = self.surface.get_rect()
		self.game_objects = []

	def run(self):
		self.quit = False
		self.clock = pygame.time.Clock()

		while(not self.quit):
			self.clock.tick(60)

			for event in pygame.event.get():
				if (event.type == pygame.QUIT):
					self.screens.change_to("Quit")

			for go in self.game_objects:
				go.update(self.clock.get_time())

			self.surface.fill((0, 0, 0))
			for go in self.game_objects:
				go.render(self.surface, self.rect)
			pygame.display.flip()

	def on_quit(self):
		self.quit = True

print("Asteroid alpha0")
app = Application()
app.run()

import pygame
import random
from game_object import GameObject
from player import Player
from bullet import Bullet
from asteroid import Asteroid

class Application:

	def __init__(self):
		pygame.mixer.pre_init(44100, -16, 1, 512)
		pygame.init()
		pygame.display.set_caption("Asteroid Alpha 0.1")
		self.surface = pygame.display.set_mode((600, 600))
		self.rect = self.surface.get_rect()
		self.font = pygame.font.Font("Fonts/OpenSansRegular.ttf", 20)
		self.game_objects = []

		self.player = Player(self)
		self.game_objects.append(self.player)
		self.is_game_over = False
		self.score = 0

		# TODO: Your program should test that pygame.mixerpygame module for loading and playing sounds is available and intialized before using it.
		pygame.mixer.music.load("Sounds/zYnthetic - Abandon v3.ogg")
		pygame.mixer.music.set_volume(0.01)
		pygame.mixer.music.play(-1, 31)

		self.impact_sounds = [
			pygame.mixer.Sound("Sounds/hit1.ogg"),
			pygame.mixer.Sound("Sounds/hit2.ogg"),
			pygame.mixer.Sound("Sounds/hit3.ogg")
		]

		self.death_sound = pygame.mixer.Sound("Sounds/death.ogg")

	def run(self):
		self.quit = False
		self.clock = pygame.time.Clock()
		pygame.time.set_timer(pygame.USEREVENT, 2000)

		while(not self.quit):
			self.clock.tick(60)

			for event in pygame.event.get():
				self.handle_event(event)

			self.update(self.clock.get_time())

			self.render(self.surface, self.rect)

	def handle_event(self, event):
		if event.type == pygame.QUIT:
			self.quit = True
		elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
			self.quit = True
		elif event.type == pygame.USEREVENT:
			self.game_objects.append(Asteroid(3))
		else:
			for go in self.game_objects:
				go.events(event)

	def update(self, delta_time):
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
		
		if self.player.is_dead:
			self.game_over()

	def render(self, surface, rect):
		surface.fill((0, 0, 0))

		score_surface = self.font.render(
			"Score: " + str(self.score),
			True,
			(255, 255, 255)
		)
		score_rect = score_surface.get_rect()
		score_rect.topright = rect.topright
		surface.blit(score_surface, score_rect)

		for go in self.game_objects:
			go.render(surface, rect)

		if self.is_game_over:
			text_surface = self.font.render(
				"You are dead!",
				True,
				(255, 255, 255)
			)
			text_rect = text_surface.get_rect()
			text_rect.center = rect.center
			surface.blit(text_surface, text_rect)

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
			ogo.is_dead = True
			self.game_over()
			return

		go.is_dead = True
		ogo.is_dead = True
		self.score += 4 - go.size

		sound_index = random.randrange(len(self.impact_sounds))
		self.impact_sounds[sound_index].play()
		
		if go.size > 1:
			a = Asteroid(go.size - 1)
			a.x = go.rect.center[0]
			a.y = go.rect.center[1]
			self.game_objects.append(a)

			a = Asteroid(go.size - 1)
			a.x = go.rect.center[0]
			a.y = go.rect.center[1]
			self.game_objects.append(a)

	def game_over(self):
		# TODO: Proper death screen
		if self.is_game_over == False:
			self.death_sound.play()
			self.is_game_over = True

print("Asteroid alpha0")
app = Application()
app.run()

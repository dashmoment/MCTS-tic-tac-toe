import pygame as pyg


#Basic color pad
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)


class game_engine:

	def __init__(self):
		pyg.init()
		self.screen = pyg.display.set_mode((600,600))
		self.display = pyg.display.set_caption("tic tac toe")
		self.clock = pyg.time.Clock()
		self.font = pyg.font.SysFont('Arial', 48)
		self.isExecute = True
		self.player = 'o'
		self.chessboard = [ [0,0,0],
						    [0,0,0],
						    [0,0,0] ]


	def update(self):

		for e in pyg.event.get():
			if e.type == pyg.QUIT:
				self.isExecute = False
			elif e.type == pyg.MOUSEBUTTONDOWN:
				self.play(e.pos)

		
		

	def draw(self):

		self.screen.fill((30,30,30))
		pyg.draw.line(self.screen, GREEN, [0,   0], [600, 0], 5)
		pyg.draw.line(self.screen, GREEN, [0, 200], [600, 200], 5)
		pyg.draw.line(self.screen, GREEN, [0, 400], [600, 400], 5)
		pyg.draw.line(self.screen, GREEN, [0, 600], [600, 600], 5)
		pyg.draw.line(self.screen, GREEN, [0, 0], [0, 600], 5)
		pyg.draw.line(self.screen, GREEN, [200, 0], [200, 600], 5)
		pyg.draw.line(self.screen, GREEN, [400, 0], [400, 600], 5)
		pyg.draw.line(self.screen, GREEN, [600, 0], [600, 600], 5)

		#Draw play statue

		for i in range(3):
			for j in range(3):

				cx = i*200 + 100
				cy = j*200 + 100

				if self.chessboard[i][j] == 1:
					pyg.draw.circle(self.screen, WHITE, [cx, cy], 40)	
				elif self.chessboard[i][j] == 2:
					pyg.draw.line(self.screen, RED, [cx -30, cy - 30], [cx + 30, cy + 30], 5)
					pyg.draw.line(self.screen, RED, [cx + 30, cy- 30], [cx - 30, cy + 30], 5)

		pyg.display.update()

		results = self.judge_winner()

		if results:
			start_ticks=pyg.time.get_ticks()

			while True:

				self.screen.fill((30,30,30))
				seconds=(pyg.time.get_ticks()-start_ticks)/1000
				input_box = pyg.Rect(160, 250, 200, 200)
				txt_surface = self.font.render("Winner is: {}".format(results), True, RED)
				self.screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
				pyg.display.update()

				if seconds > 3: 
					self.chessboard = [ [0,0,0],
						    [0,0,0],
						    [0,0,0] ]
					break 




	def judge_winner(self):

		for player in [1, 2]:
            # Check for winning horizontal lines
			for row in range(3):
				accum = 0
				for col in range(3):
					if self.chessboard[row][col] == player:
						accum += 1
				if accum == 3:
					return player

		# Check for winning vertical lines
			for col in range(3):
				accum = 0
				for row in range(3):
					if self.chessboard[row][col] == player:
						accum += 1
				if accum == 3:
					return player		

			# Check for winning diagonal lines (there are 2 possibilities)
			option1 = [self.chessboard[0][0],
			           self.chessboard[1][1],
			           self.chessboard[2][2]]
			option2 = [self.chessboard[2][0],
			           self.chessboard[1][1],
			           self.chessboard[0][2]]
			if all(marker == player for marker in option1) \
			        or all(marker == player for marker in option2):
				return player

        # Check for ties, defined as a board arrangement in which there are no
        # open board positions left and there are no winners (note that the
        # tie is not being detected ahead of time, as could potentially be
        # done)
		accum = 0
		for row in range(3):
			for col in range(3):
				if self.chessboard[row][col] == 0:
					accum += 1
		if accum == 0:
			return 'Tie'



	def play(self, location):

		loc_x = location[0]//200
		loc_y = location[1]//200
		cx = (loc_x - 1)*200 + 100
		cy = (loc_y - 1)*200 + 100

		if self.chessboard[loc_x][loc_y] == 0:

			if self.player == "o":
				
				self.chessboard[loc_x][loc_y] = 1
				self.player = "x"

			elif self.player == "x":

				self.chessboard[loc_x][loc_y] = 2
				self.player = "o"


	def engine_mainlooep(self):

		while self.isExecute:
			self.update()
			self.draw()
			self.clock.tick(60)
		pyg.quit()


b_end = game_engine()
b_end.engine_mainlooep()

import numpy as np

player_list = ['o','x']

def change_player(cuurent_player):

	for i in range(2):
		if player_list[i] != cuurent_player:
			return player_list[i]

def judge_winner(chessboard):

		for player in [1, 2]:
            # Check for winning horizontal lines
			for row in range(3):
				accum = 0
				for col in range(3):
					if chessboard[row][col] == player:
						accum += 1
				if accum == 3:
					return player

		# Check for winning vertical lines
			for col in range(3):
				accum = 0
				for row in range(3):
					if chessboard[row][col] == player:
						accum += 1
				if accum == 3:
					return player		

			# Check for winning diagonal lines (there are 2 possibilities)
			option1 = [chessboard[0][0],
			           chessboard[1][1],
			           chessboard[2][2]]
			option2 = [chessboard[2][0],
			           chessboard[1][1],
			           chessboard[0][2]]
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



class tree_node:
	def __init__(self, state):
		self.state = state
		self.value = 0
		self.visits = 0
		self.father = None
		self.child = []
		self.level = 0

class MCTS:

	def __init__(self, state, player, level):

		self.playroot = self.tree_node(state) 
		self.root = self.playroot
		self.root.level = level
		self.player = player


	def clac_UCB(self, node): #Calculate upper confidence bound

		UCB = node.value/(node.visits + 0.01) + np.sqrt(node.father.visits)/(node.visits + 0.01)
		return UCB

	def legal_move(self, node):

		states_list = []
		state = node.state

		for i in range(len(state)):
			for j in range(len(state[0])):
				if state[i][j] == 0:

					tmp = state
					tmp[i][j] = self.player
					c_node = tree_node(tmp)
					c_node.father(node)
					c_node.level = node.level + 1
					c_node.player = change_player(node.player)
				
					states_list.append(c_node)
		return 	states_list				

	def locate_root(self, state, level):

		if self.root.level != level - 1:
			assert "Level loacate error"
			return
		else:
			for node in self.root.child:
				if node.state == state: 
					self.root = node
					return 

		assert "child node not found"

	def selection(self):

		self.head = self.root

		while True:

			if len(self.head.child) > 0: 

				maxq_node = self.head.child[0]

				for i in range(1,len(self.head.child)):
					if self.clac_UCB(self.head.child[i]) > self.clac_UCB(maxq_node):
						maxq_node = self.head.child[i]

				self.head = maxq_node
				self.head.father.visits += 1
				self.head.visits += 1
			else:
				self.head = self.head
				self.head.father.visits += 1
				self.head.visits += 1
				break

	def expand(self):

		if len(self.head.child) == 0: 

			moves = self.legal_move(self.head)

			if len(moves) > 0:
				self.head.child = moves
			else: #reach tree end
				return self.head

		maxq_node = self.head.child[0]

		for i in range(1,len(self.head.child)):
			if self.clac_UCB(self.head.child[i]) > self.clac_UCB(maxq_node):
				maxq_node = self.head.child[i]

		self.head = maxq_node
		self.head.father.visits += 1
		self.head.visits += 1


	def simulation(self):

		def move_one_step(state, current_player):

			for i in range(state):
					for j in range(state[0]):
						if state[i][j] == 0:
							new_state =  state
							current_player = change_player(current_player)
							new_state[i][j] = current_player 
							state = new_state
							return state, current_player


		state = self.head.state
		current_player = self.head.player


		while True:

			status = judge_winner(state)

			if status != 'Tie':
				if status != current_player: return -1
				elif status == current_player: return 1
			else:
				new_state, current_player = move_one_step(state, current_player)
				if new_state == state: return 0
				else: state = new_state


	def backprob(self, reward):
		while self.head != None:
			self.head.value += reward
			self.head = self.head.father





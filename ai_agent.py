import MCTS

class ai_agent:
	def __init__(self, state, player, level, timelimit = 0.5):

		self.tree = MCTS(state, player, level)

	def move(self, state):

		level = 0
		for i in range(state):
			for j in range(state[0]):
				if state[i][j] != 0:
					level += 1

		self.tree.locate_root(state, level)

		while time < timelimit:

			self.tree.selection()
			self.tree.expand()
			r = self.tree.simulation()
			self.tree.backprob(r)

		maxq_node = self.tree.root.child[0]
		for i in range(1,len(self.tree.root.child)):
			if self.tree.clac_UCB(self.tree.head.child[i]) > self.tree.clac_UCB(maxq_node):
					maxq_node = self.tree.head.child[i]

		return maxq_node.state

	def transversal_tree(self):

		tree_level = {}
		tree_level[0] = root.value
		stack = [(root,0)]

		while len(stack) > 0:

			node, level = stack.pop(0)

			try:
				tree_level[level+1] += list([c_node.child[i].value for c_node in node.child])
			except:
				tree_level[level+1] = list([c_node.child[i].value for c_node in node.child])

			[stack.append((c_node,level+1)) for c_node in node.child]



chessboard = [ [0,0,0],
			   [0,0,0],
			   [0,0,0] ]
player = "o"

agent = ai_agent(chessboard, player, 0)
chessboard = ai_agent.move(state)
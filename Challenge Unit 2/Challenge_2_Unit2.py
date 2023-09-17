class Player:
	def play(self):
		print("The player is playing cricket")


class Batsman(Player):
	def play(self):
		print("The batsman is batting")


class Bowler(Player):
	def play(self):
		print("The bowler is bowling")


player1 = Player()
player1.play()

player2 = Batsman()
player2.play()

player3 = Bowler()
player3.play()
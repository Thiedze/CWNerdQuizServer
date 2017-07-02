class Player():

	def __init__(self, startAddress, name, playerId):
		self.playerId = playerId
		self.name = name
		self.buzzerAddress = startAddress
		self.points = 0
		
	def dump(self):
		return {
			"id": self.playerId,
			"name": self.name,
			"buzzerAddress": self.buzzerAddress,
			"points": self.points
			}
		

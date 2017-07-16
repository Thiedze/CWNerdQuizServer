class Player():

	startAddresses = [
			{
				"buzzerAddress" : "1,0,0",
				"yellowAddress" : "2,0,0",
				"greenAddress" : "4,0,0",
				"orangeAddress" : "8,0,0",
				"blueAddress" : "16,0,0"
			},
			{
				"buzzerAddress" : "32,0,0",
				"yellowAddress" : "64,0,0",
				"greenAddress" : "128,0,0",
				"orangeAddress" : "0,1,0",
				"blueAddress" : "0,2,0"
			},
			{
				"buzzerAddress" : "0,4,0",
				"yellowAddress" : "0,8,0",
				"greenAddress" : "0,16,0",
				"orangeAddress" : "0,32,0",
				"blueAddress" : "0,64,0"
			},
			{
				"buzzerAddress" : "0,128,0",
				"yellowAddress" : "0,0,8",
				"greenAddress" : "0,0,4",
				"orangeAddress" : "0,0,2",
				"blueAddress" : "0,0,1"
			}
		]

	def __init__(self, startAddress, name, playerId):
		self.playerId = playerId
		self.name = name
		self.points = 0
		self.setControllerAddresses(startAddress)

	def setControllerAddresses(self, startAddress):
		self.buzzerAddress = startAddress
		
		for address in Player.startAddresses:
			if address["buzzerAddress"].replace(" ", "") == startAddress.replace(" ", ""):
				self.blueAddress = address["blueAddress"]
				self.orangeAddress = address["orangeAddress"]
				self.greenAddress = address["greenAddress"]
				self.yellowAddress = address["yellowAddress"]
		
	def dump(self):
		return {
			"id": self.playerId,
			"name": self.name,
			"buzzerAddress": self.buzzerAddress,
			"points": self.points
			}
		

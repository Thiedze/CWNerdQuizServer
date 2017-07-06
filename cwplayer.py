class Player():

	startAddresses = [
			{
				"buzzerAddress" : "1,0,240",
				"yellowAddress" : "2,0,240",
				"greenAddress" : "4,0,240",
				"orangeAddress" : "8,0,240",
				"blueAddress" : "16,0,240"
			},
			{
				"buzzerAddress" : "32,0,240",
				"yellowAddress" : "64,0,240",
				"greenAddress" : "128,0,240",
				"orangeAddress" : "0,1,240",
				"blueAddress" : "0,2,240"
			},
			{
				"buzzerAddress" : "0,4,240",
				"yellowAddress" : "0,8,240",
				"greenAddress" : "0,16,240",
				"orangeAddress" : "0,32,240",
				"blueAddress" : "0,64,240"
			},
			{
				"buzzerAddress" : "0,128,240",
				"yellowAddress" : "0,1,241",
				"greenAddress" : "0,2,241",
				"orangeAddress" : "0,4,241",
				"blueAddress" : "0,8,241"
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
		

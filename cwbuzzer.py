import sys

import pywinusb.hid as hid


class Buzzer():
	
	def __init__(self):
		self.device = None
		self.initControllerBuffer = [0x00] * 8
		self.device = None
		self.device = (hid.HidDeviceFilter (vendor_id=0x054c , product_id=0x1000).get_devices())[0]
		self.device.open()
		self.report = self.device.find_output_reports()
		self.device.set_raw_data_handler(self.handleInput)
		print("server: %s" % self.report)
		
	def setWebSocket(self, webSocket):
		self.webSocket = webSocket
		
	def getInput(self):
		if len(self.input) > 0:
			self.input.popleft()
		else:
			return None
		
	def handleInput(self, data):
		print("server send: %s" % data)
		self.webSocket.write_message("[{0},{1},{2}]".format(data[3], data[4], data[5] - 240).encode('utf-8'))
		
	def initBuzzer(self):
		try:
			print("server: Buzzer initBuzzer")
			self.report[0].set_raw_data(self.initControllerBuffer)
			self.report[0].send()
		except:
			print("server: Unexpected error:", sys.exc_info()[0])
			raise
		return
		

from time import sleep
from msvcrt import kbhit

import pywinusb.hid as hid

class Buzzer():
	
	def __init__(self):
		self.device = None
		self.initControllerBuffer = [0x00]*8
		self.ledOnBuffer = [0xFF]*8
		self.ledOnBuffer[0] = 0x00;
		self.ledOnBuffer[1] = 0x00;
		self.device = None
		self.device = (hid.HidDeviceFilter (vendor_id =0x054c , product_id = 0x1000).get_devices())[0]
		self.device.open()
		self.report = self.device.find_output_reports()
		self.device.set_raw_data_handler(self.handleInput)
	
	def setWebsocket(self, websocket):
		self.websocket = websocket
		
	def handleInput(self, data):
		self.websocket.sendMessage("[{0},{1},{2}]".format(data[3], data[4], data[5] - 240).encode('utf-8'), False)
		
	def initBuzzer(self):
		print("Pairing Buzzer")
		self.report[0].set_raw_data(self.initControllerBuffer)
		self.report[0].send()
		#self.report[0].set_raw_data(self.ledOnBuffer)
		#self.report[0].send()
		return
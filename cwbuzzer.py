from time import sleep
from msvcrt import kbhit
import asyncio
import websockets
import sys

import pywinusb.hid as hid

class Buzzer():
	
	def __init__(self):
		self.device = None
		self.initControllerBuffer = [0x00]*8
		self.ledOnBuffer = [0xFF]*8
		self.ledOnBuffer[0] = 0x00;
		self.device = None
		self.device = (hid.HidDeviceFilter (vendor_id =0x054c , product_id = 0x1000).get_devices())[0]
		self.device.open()
		self.report = self.device.find_output_reports()
		self.device.set_raw_data_handler(self.handleInput)
		self.input = list()
		print(self.report)
		
	def getInput(self):
		if len(self.input) > 0:
			self.input.popleft()
		else:
			return None
		
	def handleInput(self, data):
		print(data)
		self.input.append("[{0},{1},{2}]".format(data[3], data[4], data[5] - 240).encode('utf-8'))
		
	def initBuzzer(self):
		try:
			print("Buzzer initBuzzer")
			self.report[0].set_raw_data(self.initControllerBuffer)
			self.report[0].send()
		except:
			print("Unexpected error:", sys.exc_info()[0])
			raise
		return
		
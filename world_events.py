"""

Author: Yathi

Changelog:
15th April: Seperated the world events to world_events.py. Basic if-else block for now. 

"""

class world_event:
	def __init__(self, name, desire, dc, pw, agent, patient):
		self.name = name
		self.desire = desire   	#Desirability
		self.dc = dc			#Degree of certainity
		self.pw = pw			#Praiseworthiness
		self.agent = agent		#The person doing the event
		self.patient = patient	#The resource affected by the event
		#self.sayHello()

	def sayHello(self):
		print '\nHello' , self.name

	def hinder(self):
		if self.dc > 1:
			self.dc -= 2
		else:
			self.dc = 0
			self.patient = None

	def stop(self):
		self.dc = 0
		self.patient = None
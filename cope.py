#from npc import *


"""
class action(object):
	""""""
	This is the object for the possible actions if a resource is threatened. 
	Each action will have prerquisite and if it is satisfied then that action is going to be taken. 
	Each action will have an affect on the event as well.
	""""""
	def __init__(self, name, prerquisite):
		super(action, self).__init__()
		self.name = name
		self.prerquisite = prerquisite

	def possible(self, char):
		if char.self.prerquisite:
			print "Can attack"
			return True
		else:
			return False


attack = action("attack", npc.hasWeapon)
run = action("run", npc.safeDistance)
hide = action("hide", None)
		

attack = action("attack", npc.hasWeapon)
run = action("run", npc.safeDistance)
hide = action("hide", None)"""

resourceSet = {
"health": ["attack", "hide", "run"], 
"xbox": ["protect xbox"], 
"money": ["hide", "try to protect"], 
"house": ["try to protect", "creative solution"], 
"cat": ["protect cat"], 
"child" : ["protect child"]}
		
"""

Author: Yathi

Description:
	The Base NPC class from which both Humans and Critters are derived
	We could have other kinds of NPCs also derived from this base class!

Changelog:
15th April 2014: Seperated the npcs into npc.py.

"""

from random import randint
from cope import *


class npc(object):
	def __init__(self, name):
		self.name = name
		self.curiousityAction = ["Look", "Hear"]
		self.impResources = ["health"]
		self.sayHello()
	#Test method
	def sayHello(self):
		print "\n" , self.name , "welcomes you!"
	#The curiousity action
	def curious(self):
		return randAction(self.curiousityAction)
	def cope(self, world_event):
		#print "Entered coping"
		for x in world_event.patient:
			if x in self.impResources:
				return randAction(resourceSet[x])
	def setImpResource(self, x):
		#print "setting imp resource to " , x
		self.impResources = x

#The class for the animals in the game.
class critters2(npc):
	"""docstring for critters2"""
	def __init__(self,name):
		super(critters2, self).__init__(name)
		self.curiousityAction = ["Sniffs around", "Goes to event slowly and sees", "Pricks ears and tries to listen"]
		#self.name = name

#The class for humans
class human2(npc):
	"""docstring for human2"""
	def __init__(self, name):
		super(human2, self).__init__(name)
		self.curiousityAction = ["Looks around", "Asks neighbour if they noticed anything", "Becomes silent and tries to hear"]

#The method to pick a random action from an array of possible actions
def randAction(j):
    return j[randint(0, len(j) -1 )]
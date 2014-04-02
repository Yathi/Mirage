from random import randint
import pygraphviz as pgv
import time

actionSet = ["run", "attack", "hide", "try to protect", "creative solution"]
resourceSet = {"health": ["run","hide", "attack"], "xbox": ["protect xbox"],
"money":["hide", "try to protect"], "house": ["try to protect", "creative solution"], "cat": ["protect cat"], "child" : ["protect child"]}
threatenedResource = ["health", "xbox"]
actionImplementSet = {'attack': ['umbrella', 'fist', 'fire-The']}

#extinguisher Class for all the world Events
class world_event:
	def __init__(self, name, desire, dc, pw, agent, patient):
		self.name = name
		self.desire = desire
		self.dc = dc
		self.pw = pw
		self.agent = agent
		self.patient = patient
		#self.sayHello()

	def sayHello(self):
		print '\nHello' , self.name


"""
	The Base NPC class from which both Humans and Critters are derived
	We could have other kinds of NPCs also derived from this base class!
"""
class npc(object):
	def __init__(self, name):
		self.name = name
		self.curiousityAction = ["Look", "Hear"]
		self.impResources = ["health"]
		self.sayHello()
	#Test method
	def sayHello(self):
		print "\n" , self.name , "welomes you!"
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

def checkResources(resourceSet):
    for x in threatenedResource:
        print randAction(resourceSet[x])

def emote(world_event):
	#print "the disirability is " , world_event.desire
	#print "the dc is " , world_event.dc
	if world_event.desire > 0:
		if world_event.dc == 1:
			return "Joy"
		elif world_event.dc > 0 and world_event.dc < 1:
			return "Hope"
		elif world_event.dc == 0:
			return "Dissapointment"
	elif world_event.desire < 0:
		if world_event.dc == 1:
			return "Distress"
		elif world_event.dc > 0 and world_event.dc < 1:
			return "Fear"
		elif world_event.dc == 0:
			return "Relief"

#The MAIN Program Loop

G = pgv.AGraph(strict = False, directed = True)
#G.graph_attr['label'] = "Mirage"
G.node_attr['shape'] = 'oval'

#The characters
girl = "Random Girl"
doggie = "Doggie"
dragon = "Dragon"
child = "Child"
dad = "Dad"

#The events
bird = "Bird_Incoming"
fire = "Fire"
alien = "Alien_Invasion"

while True:
	print "\n" + girl
	print doggie
	print dragon
	print child
	print dad
	select_char = int(raw_input("\nSelect your character : "))

	#should create a object of the class here
	if select_char == 1:
		char = human2("Jill")
	elif select_char == 2:
		char = critters2("Doggie")
	elif select_char == 3:
		char = critters2("Smaug")
	elif select_char == 4:
		char = human2("Child")
		char.setImpResource(["cat", "health"])
	elif select_char == 5:
		char = human2("Dad")
		char.setImpResource(["child", "health"])
	else:
		break #This breaks out of the While loop if some other event is selected.

	G.add_node(char.name, color = 'aquamarine3')
	
	#stupid sleep timer to be removed
	time.sleep(1)


	#Present a list of possible events
	print "\n" + bird
	print fire
	print alien
	current_event = int(raw_input("\nSelect the event you would like : "))
	if current_event == 1:
		event = world_event(bird, -0.4, 0.6, 0, "default", ["health"])  #Could work on maybe making these values dynamically generated
	elif current_event == 2:
		event = world_event(fire, -0.8, 1, 0, "default", ["health"])
	elif current_event == 3:
		event = world_event(alien, -0.5, 0.8, 0, "default", ["health"])
	else:
		break



	G.add_node(event.name, color = 'darkorchid4')
	#Have the curiosity event of the object here
	curious_action = char.curious() #Storing this so that the value does not change when we put the value in graph
	print "\n" + curious_action
	G.add_node(curious_action, color = 'gold4')
	G.add_edge(char.name, curious_action)
	G.add_edge(event.name, curious_action)
	raw_input("\nPress any key to proceed ")
	print "\n" , char.name , " finds out that there is a ", event.name , " and he/she is in " , emote(event)
	G.add_node(emote(event), color = 'darkseagreen')
	G.add_edge(curious_action, emote(event))
	
	#sleep timer to be removed
	time.sleep(1)
	raw_input("\nPress any key to proceed ")

	possible_actions = []
	#code to print all possible coping actions
	for resource in event.patient:
		if resource in char.impResources:
			for x in resourceSet[resource]:
				G.add_node(x, color = 'deepskyblue4')
				possible_actions.append(x)

	print possible_actions
	G.subgraph(nbunch = possible_actions, name='Possible Actions', style = 'filled', color = 'gray9', label = 'cluster label', rank = 'same')



	#Have the coping action here
	coping_action = char.cope(event) #again coping is stored so that it is calculated once for one run
	print "\n" , char.name , " is trying to " , coping_action
	G.add_edge(emote(event), coping_action)
	time.sleep(2)
	G.layout(prog = 'dot')
	G.draw('model.png')
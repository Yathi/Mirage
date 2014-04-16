"""

Author: Yathi

Description:
	The main file to run mirage. The code runs only in python2x for now because pygraphviz is not supported in python 3
	Keep running emote and cope till resource in not threatened. 


Changelog:
15th April 2014: Created the file and seperated all the other modules to their own files. 

"""

from emotion import * #These imports have to be changed to import only the needed classes. 
from world_events import *
from npc import human2
from cope import *
import pygraphviz as pgv
import os


bird = "Bird Incoming"
setStop = False

def show_emotion(char, event, current_node):
	raw_input("\nPress any key to proceed ")
	print "\n" , char.name , " finds out that there is a ", event.name , " and he/she is in " , emote(event)

	#Graph for emotion
	#G.add_node(emote(event), color = 'darkseagreen')
	#G.add_edge(current_node, emote(event))

def show_actions(possible_actions, affected_resource):
	"""
	This is to show all the possible actions which are possible to save the particular resource. 
	"""
	print "\n The possible actions to protect ", affected_resource, ":"
	i = 1
	for action in possible_actions:
		print "\n", i , action
		i += 1

def suggest_action(possible_actions, char):
	"""
	This shows the best action as determined by the model.
	"""
	if char.hasWeapon:
		if "attack" in possible_actions:
			return "attack"
	elif char.safeDistance:
		if "hide" in possible_actions:
			return "hide"
	else:
		if "run" in possible_actions:
			return "run"

def attack(char, event):
	if char.hasWeapon:
		event.stop()
		setStop = True
	else:
		print "Without a weapon " , char.name , " could not do much!"

def hide(char, event):
	if char.safeDistance:
		event.hinder()
	else:
		print "\n" , char.name , " is not far enough to hide safely...."

def run(char, event):
	char.safeDistance = True
	print "\n" , char.name, " is at a safer distance now."



def start():
	print("Welcome to Mirage!")
	print("Jill is roleplaying with her friend")
	char = human2("Jill")
	#The Graph code
	G.add_node(char.name, color = 'aquamarine3')

	raw_input("\nPress any key to proceed ")
	event = world_event(bird, -0.4, 0.6, 0, "default", ["health"])


	G.add_node(event.name, color = 'darkorchid4')
	#Have the curiosity event of the object here
	curious_action = char.curious() #Storing this so that the value does not change when we put the value in graph
	print "\n" + curious_action

	#Lines for curious action
	G.add_node(curious_action, color = 'gold4', shape = 'box')
	G.add_edge(char.name, curious_action)
	G.add_edge(event.name, curious_action)

	#curious action notices event.
	notice_event = "Notice: " + event.name
	G.add_node(notice_event)
	G.add_edge(curious_action, notice_event)

	current_node = notice_event #This is defined seperately so that when multiple instances of emote are called this can change. 
	while True:
		show_emotion(char, event, current_node)

		possible_actions = [] #This will store all the possible actions
		#code to print all possible coping actions
		#print "\nThe event patient is ", event.patient

		for resource in event.patient:
			if resource in char.impResources:
				affected_resource = resource #This is the important resource for the npc which is threatened by the event. 
				for x in resourceSet[affected_resource]:
					G.add_node(x, color = 'deepskyblue4', shape = 'box')
					possible_actions.append(x)


		show_actions(possible_actions, affected_resource)
		print "\n The action suggested by the system is : ", suggest_action(possible_actions, char) 

		try:
			action_num = int(raw_input("\n Please select an action number:"))
		except ValueError:
			print "\nPlease enter a number next time"
			continue


		if action_num == 1:
			attack(char, event)
		elif action_num == 2:
			hide(char, event)
		elif action_num == 3:
			run(char, event)
		else:
			break


		#print "\nThe event patient is ", event.patient
		#print "\nThe event dc is ", event.dc

		if event.patient == None:
			break

		try:
			choice = int(raw_input("\n You see an Umbrella on the floor. Pick it up? 1 - Yes, 2 - No \n : "))	
		except ValueError:
			print "\nPlease enter a number next time"
			continue


		if choice == 1:
			char.hasWeapon = True


	print "\nEveryone is safe now! Except for the poor bird!"







	G.subgraph(nbunch = possible_actions, name='cluster1', style = 'filled', color = '', label = 'Possible Actions', rank = 'same')

	#coping_action = char.cope(event) #again coping is stored so that it is calculated once for one run
	#print "\n" , char.name , " is trying to " , coping_action
	#G.add_edge(emote(event), coping_action)



	#The code to output the graph
	G.layout(prog = 'dot')
	G.draw('model.png')
	os.system('open model.png')




#START OF THE PROGRAM

G = pgv.AGraph(strict = False, directed = True) 
#G.graph_attr['label'] = "Mirage"
G.node_attr['shape'] = 'oval'

start()
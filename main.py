"""

Author: Yathi

Description:
	The main file to run mirage. The code runs only in python2x for now because pygraphviz is not supported in python 3
	Keep running emote and cope till resource in not threatened. 


Changelog:
15th April 2014: Created the file and seperated all the other modules to their own files. 

"""

from emotion import *
from world_events import *
from npc import human2
from cope import *
import pygraphviz as pgv
import os


bird = "Bird Incoming"

def show_emotion(char, event, current_node):
	raw_input("\nPress any key to proceed ")
	print "\n" , char.name , " finds out that there is a ", event.name , " and he/she is in " , emote(event)

	#Graph for emotion
	G.add_node(emote(event), color = 'darkseagreen')
	G.add_edge(current_node, emote(event))


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
	current_node = notice_event
	show_emotion(char, event, current_node)

	possible_actions = []
	#code to print all possible coping actions
	for resource in event.patient:
		if resource in char.impResources:
			for x in resourceSet[resource]:
				G.add_node(x, color = 'deepskyblue4', shape = 'box')
				possible_actions.append(x)

	print possible_actions
	G.subgraph(nbunch = possible_actions, name='cluster1', style = 'filled', color = '', label = 'Possible Actions', rank = 'same')

	coping_action = char.cope(event) #again coping is stored so that it is calculated once for one run
	print "\n" , char.name , " is trying to " , coping_action
	G.add_edge(emote(event), coping_action)



	#The code to output the graph
	G.layout(prog = 'dot')
	G.draw('model.png')
	os.system('open model.png')




#START OF THE PROGRAM

G = pgv.AGraph(strict = False, directed = True) 
#G.graph_attr['label'] = "Mirage"
G.node_attr['shape'] = 'oval'

start()
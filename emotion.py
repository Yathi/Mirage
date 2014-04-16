"""

Author: Yathi

Changelog:
15th April: Seperated the emotion to emotion.py. Basic if-else block for now. 

"""

def emote(world_event):
	"""
	This is the function used to get the emotion of the NPC based on the properties of the world event. For now it is a fixed set of if else conditions. 
	"""
	#print "the disirability is " , world_event.desire
	#print "the dc is " , world_event.dc
	if world_event.desire > 0:
		if world_event.dc == 1:
			return "Joy"
		elif world_event.dc < 1:
			if world_event.dc > 0.6: 
				return "High Hope"
			elif world_event.dc > 0.3:
				return "Hope"
			elif world_event.dc > 0:
				return "Mild Hope"

		elif world_event.dc == 0:
			return "Dissapointment"
	elif world_event.desire < 0:
		if world_event.dc == 1:
			return "Distress"
		elif world_event.dc < 1:
			if world_event.dc > 0.6:
				return "High Fear"
			elif world_event.dc > 0.3:
				return "Fear"
			elif world_event.dc > 0:
				return "Mild Fear"
		elif world_event.dc == 0:
			return "Relief"
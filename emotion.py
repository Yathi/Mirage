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
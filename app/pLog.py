# pLog.py : Nick Palumbo

def clearLog():
	open('../logs/running.log','w').close()

def writeToLog(message):
	log = open('../logs/running.log','a')
	log.write(message + "\n")
	log.close

def getPreviousErrorSettings():
	try:
		log = open('../logs/running.log','r')
		for line in log:
			print log
	except:
		print("No log found, starting first run.")
	return 0, 0

def writeErrorToLog():
	log = open('../logs/running.log','a')
	log.write("----------------------------------------------\n")
	log.write("There was an error when running pRun.\n")
	log.write("----------------------------------------------\n")
	log.close()

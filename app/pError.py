# pError.py : Nick Palumbo

errorAddress = "" # address that caused error
errorRadius = "" # radius that caused error
errorX = "" # cell X to start on
errorY = "" # cell Y to start on


def setError(address,radius,x,y):
	global errorAddress
	global errorRadius
	global errorX
	global errorY
	errorAddress = address
	errorRadius = radius
	errorY = str(x)
	errorX = str(y)

def printError(given_error):
	print("----------------------------------------------")
	print("There was an error when running: " + str(given_error) + ".")
	print("----------------------------------------------")
	if errorAddress != "":
		print("Address: " + errorAddress)
		print("Radius: " + errorRadius)
		print("x: " + errorX)
		print("y: " + errorY)
	else:
		print("No addresses were looked up yet..")
	print("----------------------------------------------")

def saveError():
	log = open('../logs/errors.log','w')
	log.write("[errorAddress,errorRadius,errorX,errorY]")
	log.write(errorAddress + "\n")
	log.write(errorRadius + "\n")
	log.write(errorX + "\n")
	log.write(errorY + "\n")
	log.close()

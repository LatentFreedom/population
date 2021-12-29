# System
import time
# Installed
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# Local
import app, Excel, Error, Log, Location


# put the given radius in the input box
def putRadius(driver,radius):
	# clear input box
	radius_input = "document.getElementById('radiusinputmi').value = " + radius + ";"
	driver.execute_script(radius_input)
	driver.execute_script("ftn_radius_change('miles');")

# put the given address in the input box
def putAddress(driver,address):
	address_input = "document.getElementById('tb_searchlocation').value = " + "\"\"" + ";"
	driver.execute_script(address_input)

	try:
		ele = driver.find_element(By.ID, "tb_searchlocation")
		ele.send_keys(address)
		time.sleep(2)
		ele.send_keys(Keys.DOWN)
		ele.send_keys(Keys.RETURN)
		return(True)
	except:
		return(False)

def getPopulation(driver):
	driver.execute_script("ftn_findPopulation();")
	output = driver.find_element(By.ID, "div_output")
	text = output.text
	while text == "Please Wait...":
		output = driver.find_element(By.ID, "div_output")
		text = output.text
	population = text.split()[8]
	population = population.split(',')
	pop = ""
	for i in population:
		pop += i
	return pop

### Input functions
def waitForInt(ta, s):
	while True:
		try:
			ta = int(ta)
			return ta
		except:
			print(s + " must be an integer.")
			ta = raw_input(s + ": ")

def getRadiusArray():
	ra = raw_input("Enter radiuses to be used [ex. : 1 2 3 4]: ")
	ra = ra.split(' ')
	print("radiuses to use: " + str(ra))
	cont = raw_input('Use the above radiuses? (y/n): ')
	if cont == 'y':
		return ra
	else:
		getRadiusArray()

def continueLookup(address_array,data,url):
	driver = startDriver()
	radius_array = data[0]
	x = data[1]
	y = data[2]
	continueGetAddressPopulations(driver,address_array,radius_array,url,x,y)

def continueGetAddressPopulations(driver,address_array,radius_array,url,lastX,lastY):
	continuedX = 0
	if lastX > 0:
		continuedX = lastX-1
	for x in range(continuedX,len(radius_array)): # x+1 = x in excel sheet
		driver.get(url)
		for y in range(0,len(address_array)): # y+1 = y in excel sheet
			address = address_array[y].address
			populationError.setError(address,radius_array[x],x+1,y+1)
			putRadius(driver,radius_array[x])
			success = putAddress(driver,address)
			if success:
				population = app(driver)
				message = "Address: {0:38} | radius: {1:4} | population: {2:10}".format(address,radius_array[x],population)
				print(message)
				populationLog.writeToLog(message)
				populationExcel.updatePopulationForAddress(radius_array[x],y+1,population)
			else:
				message = "Address: {0:38} | radius: {1:q4} | population: {2:10}".format(address,radius_array[x],"NULL")
				print(message)
				populationLog.writeToLog(message)
				populationExcel.updatePopulationForAddress(radius_array[x],y+1,"ERROR")


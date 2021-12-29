# System
import time
# Installed
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
# Local
import Excel, Helpers, Error, Log

def startDriver(headless=False):
	if headless:
		fireFoxOptions = Options()
		fireFoxOptions.headless = True
		return webdriver.Firefox(options=fireFoxOptions)
	else:
		return webdriver.Firefox()

def getAddressPopulations(driver,locations,radius_array,url):
	for x in range(0,len(radius_array)): # x+1 = x in excel sheet
		driver.get(url)
		for y in range(0,len(locations)): # y+1 = y in excel sheet
			address = locations[y].address
			Error.setError(address,radius_array[x],x+1,y+1)
			Helpers.putRadius(driver,radius_array[x])
			success = Helpers.putAddress(driver,address)
			if success:
				time.sleep(2)
				population = Helpers.getPopulation(driver)
				message = "Address: {0:38} | radius: {1:4} | population: {2:10}".format(address,radius_array[x],population)
				print(message)
				Log.writeToLog(message)
				Excel.updatePopulationForAddress(radius_array[x],y+1,population)
			else:
				message = "Address: {0:38} | radius: {1:4} | population: {2:10}".format(address,radius_array[x],"NULL")
				print(message)
				Log.writeToLog(message)
				Excel.updatePopulationForAddress(radius_array[x],y+1,"ERROR")

def main():
	url = "https://www.freemaptools.com/find-population.htm"
	Log.clearLog()
	try:
		locations = Excel.makeLocationArray()
		radius_array = ['1','2']
		# radius_array = Helpers.getRadiusArray()
		driver = startDriver(True)
		driver.get(url)
		getAddressPopulations(driver,locations,radius_array,url)
		driver.quit()
	except Exception as e:
		Error.printError(e)
		Error.saveError()

if __name__ == "__main__":
	main()

'''
hadError, data = populationLog.getPreviousErrorSettings()
if hadError:
	total_addresses = data[0]
	locations = populationExcel.makeAddressArray(total_addresses)
	populationHelpers.continueLookup(locations,data,url)
	driver.quit()
	return(0)
'''

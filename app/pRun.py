# pRun.py : Nick Palumbo

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pExcel, pHelpers, pError, pLog

def startDriver():
    return webdriver.Firefox()

def getAddressPopulations(driver,locations,radius_array,url):
	for x in range(0,len(radius_array)): # x+1 = x in excel sheet
		driver.get(url)
		for y in range(0,len(locations)): # y+1 = y in excel sheet
			address = locations[y].address
			pError.setError(address,radius_array[x],x+1,y+1)
			pHelpers.putRadius(driver,radius_array[x])
			success = pHelpers.putAddress(driver,address)
			if success:
				time.sleep(2)
				population = pHelpers.getPopulation(driver)
				message = "Address: {0:38} | radius: {1:4} | population: {2:10}".format(address,radius_array[x],population)
				print(message)
				pLog.writeToLog(message)
				pExcel.updatePopulationForAddress(radius_array[x],y+1,population)
			else:
				message = "Address: {0:38} | radius: {1:4} | population: {2:10}".format(address,radius_array[x],"NULL")
				print(message)
				pLog.writeToLog(message)
				pExcel.updatePopulationForAddress(radius_array[x],y+1,"ERROR")

def main():
	url = "https://www.freemaptools.com/find-population.htm"
	pLog.clearLog()
	# try:
	locations = pExcel.makeLocationArray()
	radius_array = ['1','2']#pHelpers.getRadiusArray()
	driver = startDriver()
	driver.get(url)
	getAddressPopulations(driver,locations,radius_array,url)
	driver.quit()
	# except Exception as e:
	# 	pError.printError(e)
	# 	pError.saveError()

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

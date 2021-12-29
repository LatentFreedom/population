# System
import random
# Installed
import xlrd
from xlrd import open_workbook
import xlutils
from xlutils.copy import copy
# Local
import Location

#WORKBOOK

# create an workbook that will be used to read from
workbookRead = xlrd.open_workbook('population.xls')
worksheet_addresses_read = workbookRead.sheet_by_name('Addresses')

# create a workbook that will be used to write to
workbook = open_workbook("population.xls")
workbookWrite = copy(workbook)
worksheet_addresses_write = workbookWrite.get_sheet(0)

#  GET
def makeLocationArray():
	locations = []
	i = 1
	while worksheet_addresses_read.cell(i,0).value:
		address = worksheet_addresses_read.cell(i,0).value
		locations.append(Location.Location(address,0,i))
		i += 1

	return locations

# UPDATE
def updatePopulationForAddress(radius,y,population):
	x = int(radius)
	worksheet_addresses_write.write(y,x,int(population))
	workbookWrite.save('population.xls')

# Population Scraping
Scrape population information from **[https://www.freemaptools.com/find-population.htm](https://www.freemaptools.com/find-population.htm)**.
* Import location information and radius from excel worksheet.
* Save population information to excel worksheet from site data.

## Note
This program is very simple and the radius values are hard coded but the function `Helpers.getRadiusArray()` can be uncommented to take an array of radius values as user input. The hardcoded values right now are `[1,2]`.

## Firefox
`geckodriver` required in path before running. You can find geckodriver at **[https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)**

## Excel Workbook
- **Workbook Name**: population.xls
- **Worksheet Name**: Addresses

Column `A` will have the addresses that will be read into the program. The following columns `B+` will be the population data given the desired radius in miles. View the given `population.xls` for an example of what the worksheet should look like.
```
        A            B         C          D
-----------------------------------------------
| address       |    1    |    3    |    5    |
-----------------------------------------------
| givenAddress1 | pop@r=1 | pop@r=3 | pop@r=5 |
-----------------------------------------------
```

## Run program
1. Make sure excel workbook `population.xls` has been made.
2. Add `geckdriver` to `PATH`
```
export PATH=$PATH=/Path/to/geckodriver/
```
3. Install needed libraries with `pip`.
```
pip install -r requirements.txt
```
4. run with `python app.py`
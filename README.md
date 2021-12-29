# Population Scraping
Scrape population information from **[https://www.freemaptools.com/find-population.htm](https://www.freemaptools.com/find-population.htm)**.
* Import location information and radius from excel worksheet.
* Save population information to excel worksheet from site data.

## Firefox
`geckodriver` required in path before running. You can find geckodriver at **[https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)**

## EXCEL Workbook Naming:
- **Workbook Name**: population.xls
- **Tab Name**: Addresses

## EXCEL Workbook Format
```
     A          B        C          D
-----------------------------------------
| address | pop@r=1 | pop@r=3 | pop@r=5 |
-----------------------------------------
```

## Run program
1. Make sure excel workbook `population.xls` has been made.
2. Add `geckdriver` to `PATH`
3. Install needed libraries with `pip install -r requirements.txt`
3. run with `python app.py`
# This is the official copy for grading picks
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pygsheets
import pandas as pd

# The ID and range of a sample spreadsheet.

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
gc = gspread.authorize(credentials)
gc1 = pygsheets.authorize(service_file='client_secret.json')

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
wks = gc.open_by_key('IDofWorksheet')
# name of worksheet
sheet = wks.worksheet("Week xx")

sh = gc1.open_by_key('IDofWorksheet')
wks1 = sh[xx]

# grab all data into list of lists
ExcelSheetFirstRead = sheet.get_all_values()
print(ExcelSheetFirstRead)
# Step 1:
# Build unique list and populate I2:j2

d1 = pd.DataFrame()
uniqueList = []

for row in ExcelSheetFirstRead[1:]:
    if row[1] not in uniqueList:
        uniqueList.append(row[1])
    if row[2] not in uniqueList:
        uniqueList.append(row[2])
    if row[3] not in uniqueList:
        uniqueList.append(row[3])

d1['Team'] = uniqueList
wks1.set_dataframe(d1, (1, 9))

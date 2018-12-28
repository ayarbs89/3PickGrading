# This is the official copy for grading picks
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# The ID and range of a sample spreadsheet.

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
gc = gspread.authorize(credentials)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
wks = gc.open_by_key('ID')
sheet = wks.worksheet("Week 17")

# grab all data into list of lists
ExcelSheet = sheet.get_all_values()

# Step 1:
# Build unique list and populate I2:j2
uniqueList = []

for row in ExcelSheet[1:]:
    if row[1] not in uniqueList:
        uniqueList.append(row[1])
    if row[2] not in uniqueList:
        uniqueList.append(row[2])
    if row[3] not in uniqueList:
        uniqueList.append(row[3])

print(uniqueList)

# create dictionary for the spread from list of lists(excel sheet)
spread = {}
for i in ExcelSheet[1:]:
    if i[8] != "" and i[9] != "":
        spread[i[8]] = float(i[9])
#print(spread)

# build players pick list
picks = []
# build the Players picks list
for row in ExcelSheet[1:]:
    # picks[row[1], row[2], row[3], row[4]]
    picks.append(row[0:5])
# print(picks)

# Step 3 grade: compare spread{} to picks[] and write out # in picks list
for p in picks:
    score = float(p[4])
    score += float(spread[p[1]])
    score += float(spread[p[2]])
    score += float(spread[p[3]])
    p[4] = score
#print(picks)

# update spreadsheet with this info




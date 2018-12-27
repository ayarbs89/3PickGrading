#This is the official copy for grading picks
import gspread
from oauth2client.service_account import ServiceAccountCredentials



# The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '1YhJdB8q0lgLi9lyRZ8CcUSI_1g66xCxJvNC5BVRVv_o'
# SAMPLE_RANGE_SPREAD = 'Week 16!I:J'

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
gc = gspread.authorize(credentials)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
#sheet = 'week 16'
wks = gc.open_by_key('1YhJdB8q0lgLi9lyRZ8CcUSI_1g66xCxJvNC5BVRVv_o')
sheet = wks.worksheet("Week 16")
#Spread_Dictionary =
ExcelSheet = sheet.get_all_values()
d = {}

for i in ExcelSheet[1:]:
    if( i[8] != "" and i[9] != "" ):
        d[i[8]] = float(i[9])
    # for cell in line:
    #     d[cell[1]] = cell[3]
print(d)
    #spread.__getitem__(row.items())

#print(spread)


# for cols in Spread_Dictionary:
#     spread[cols[8]] = cols[9]
#for cell in Spread_Dictionary

#print(ExcelSheet)



#def main():
    #"""Shows basic usage of the Sheets API.
    #Prints values from a sample spreadsheet.
    #"""
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    # scope = ['https://www.googleapis.com/auth/spreadsheets']
    # creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    # client = gspread.authorize(creds)
    #
    # # Find a workbook by name and open the first sheet
    # # Make sure you use the right name here.
    # sheet1 = 'week 16'
    # sheet = client.open("20183Pick Standings").week16
    # list_of_hashes = sheet.get_all_records()
    # print (list_of_hashes)


#if __name__ == '__main__':
   # main()



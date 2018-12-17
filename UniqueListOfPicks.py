#This is the official copy for getting all the unique picks
import csv

picks = []
with open('C:\\UniquePicks.csv') as UniquePicks:
    Unique_csv_reader = csv.reader(UniquePicks, delimiter=',')

    # build the Players picks list
    for row in Unique_csv_reader:
        if row not in picks:
            picks.append(row)

        #
        #     print (row)


print(picks)

with open('C:\\UniquePicksOutput.csv', 'w') as UniquePicksOutput:
    Grades_csv_writer = csv.writer(UniquePicksOutput, lineterminator='\n')
    Grades_csv_writer.writerows(picks)

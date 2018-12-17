#This is the official copy for grading picks
import csv
spread = {}
with open('C:\\Spread_csv.csv') as Spread_csv:
    Spread_csv_reader = csv.reader(Spread_csv, delimiter=',')
    # build the Spread Dictionary - dont get this actually
    for row in Spread_csv_reader:
        spread[row[0]] = row[1]

picks = []
with open('C:\\Picks1.csv') as players_file:
    Players_csv_reader = csv.reader(players_file, delimiter=',')

    # build the Players picks list
    for row in Players_csv_reader:
        picks.append(row)

    # for row in Players_csv_reader:
    #     score = row[int(4)]
    #     values = [row[0], row[1], row[2], row[3], score]
    #     picks.append(values)
        # picks.append(row)

for p in picks:
    score = float(p[4])
    score += float(spread[p[1]])
    score += float(spread[p[2]])
    score += float(spread[p[3]])
    p[4] = score
    print (score)
print (picks)
        #Grades_csv.w
        #Grades_csv.write("\n")
with open('C:\\grades.csv', 'w') as Grades_csv:
    Grades_csv_writer = csv.writer(Grades_csv, lineterminator='\n')
    Grades_csv_writer.writerows(picks)


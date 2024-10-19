import json
import csv

replacement_pair=[['<br>',' '],['<br/>',' '],['Mr','Mr.'],['Dr','Dr.'],['T S Eliot','T. S. Eliot'],['le Carré','Le Carré'],['Le Carre','Le Carré']]
with open('white.csv','r') as csvfile:
    csvreader=csv.reader(csvfile)
    whitelist=[row for row in csvreader]

whitelist=whitelist[0]

string_records=[] #This collects all the strings
with open('litclock_annotated.csv', 'r') as csvfile:
  # Create a reader object
  csv_reader = csv.reader(csvfile,delimiter='|')
  for row in csv_reader:
    indicator=False
    row[3]=(row[3]).rstrip()
    row[4]=(row[4]).rstrip() 
    newrow=row
    for cell in replacement_pair:
        newrow=[newcell.replace(cell[0],cell[1]) for newcell in newrow]      
    for string in whitelist:
        findbool=any(string in cell for cell in newrow)
        if findbool:
            #print(f"Found '{string}' in row: {row}")
            indicator=True
    if indicator:
        string_records.append(newrow)

with open('litclock_annotated_br2.csv', 'r') as csvfile:
  # Create a reader object
  csv_reader = csv.reader(csvfile,delimiter='|')
  for row in csv_reader:
    indicator=False
    duplicate=True
    row[3]=(row[3]).rstrip()
    row[4]=(row[4]).rstrip()  
    newrow=row
    for cell in replacement_pair:
        newrow=[newcell.replace(cell[0],cell[1]) for newcell in newrow]     
    for string in whitelist:
        findbool=any(string in cell for cell in newrow)
        if findbool:
            #print(f"Found '{string}' in row: {row}")
            indicator=True
    if indicator:
        for circlerow in string_records:
            if (circlerow[1]==newrow[1])&(circlerow[2]==newrow[2])&(circlerow[4]==newrow[4]):
                duplicate=False
        if duplicate:
            string_records.append(newrow)


with open('Fx9.csv', 'r') as csvfile:
  # Create a reader object
  csv_reader = csv.reader(csvfile,delimiter='|')
  for row in csv_reader:
    indicator=False
    duplicate=True
    row[3]=(row[3]).rstrip()
    row[4]=(row[4]).rstrip()
    newrow=row
    for cell in replacement_pair:
        newrow=[newcell.replace(cell[0],cell[1]) for newcell in newrow]    
    for string in whitelist:
        findbool=any(string in cell for cell in newrow)
        if findbool:
            #print(f"Found '{string}' in row: {row}")
            indicator=True
    if indicator:
        for circlerow in string_records:
            if (circlerow[1]==newrow[1])&(circlerow[2]==newrow[2])&(circlerow[4]==newrow[4]):
                duplicate=False
        if duplicate:
            string_records.append(newrow)

with open('litclock_annotated_ver.csv', 'r') as csvfile:
  # Create a reader object
  csv_reader = csv.reader(csvfile,delimiter='|')
  for row in csv_reader:
    indicator=False
    duplicate=True
    row[3]=(row[3]).rstrip()
    row[4]=(row[4]).rstrip() 
    newrow=row
    for cell in replacement_pair:
        newrow=[newcell.replace(cell[0],cell[1]) for newcell in newrow]      
    for string in whitelist:
        findbool=any(string in cell for cell in newrow)
        if findbool:
            #print(f"Found '{string}' in row: {row}")
            indicator=True
    if indicator:
        for circlerow in string_records:
            if (circlerow[1]==newrow[1])&(circlerow[2]==newrow[2])&(circlerow[4]==newrow[4]):
                duplicate=False
        if duplicate:
            string_records.append(newrow)

sorted_data = sorted(string_records, key=lambda x: x[0])


with open('lit_full.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerows(sorted_data)




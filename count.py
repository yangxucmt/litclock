import json
import csv


with open('./data/white.csv','r') as csvfile:
    csvreader=csv.reader(csvfile)
    whitelist=[row for row in csvreader]

whitelist=whitelist[0]
json_records=[]

with open('./data/lit_full.csv', 'r') as csvfile:
  # Create a reader object
  csv_reader = csv.reader(csvfile,delimiter='|')
  for row in csv_reader:
    indicator=False
    for string in whitelist:
        findbool=any(string in cell for cell in row)
        if findbool:
            #print(f"Found '{string}' in row: {row}")
            indicator=True
    if indicator:
        quote_time=row[1]
        quote=row[2]
        quotetemp=quote.lower()
        start_index=quotetemp.find(quote_time.lower())
        quote_first=quote[:start_index]
        quote_last=quote[start_index+len(quote_time):]
        data={
            'time': row[0],
            'quote_first': quote_first,
            'quote_time_case': quote_time, 
            'quote_last': quote_last, 
            'title': row[3],
            'author': row[4]
             }
        json_records.append(data)

with open('./data/added.csv', 'r') as csvfile:
  # Create a reader object
  csv_reader = csv.reader(csvfile,delimiter='|')
  for row in csv_reader:
    indicator=True
    if indicator:
        quote_time=row[1]
        quote=row[2]
        start_index=quote.find(quote_time)
        quote_first=quote[:start_index]
        quote_last=quote[start_index+len(quote_time):]
        data={
            'time': row[0],
            'quote_first': quote_first,
            'quote_time_case': quote_time, 
            'quote_last': quote_last, 
            'title': row[3],
            'author': row[4]
             }
        json_records.append(data)


timelist=[]
timeindicator=0
for hour in range(6,24):  # Loop from 0 to 23 for the hours
    for minute in range(60):  # Loop from 0 to 59 for the minutes
        # Format the hour and minute to ensure two digits
        indicator=False  
        for item in json_records:
            if item['time'] ==f'{hour:02d}:{minute:02d}':
                indicator=True
        if not(indicator):
            timeindicator+=1
            timelist.append(f'{hour:02d}:{minute:02d}')

with open('remaining.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    for item in timelist:
        writer.writerow([item])


print(timeindicator)


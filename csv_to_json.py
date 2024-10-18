import json
import csv


stringlist=['Tolkien','Proust','David Foster Wallace','Virginia Woolf','George Eliot','Jerome K Jerome','Ian McEwan','Philip K Dick','Shakespeare','Fyodor','Victor Hugo','Wilde','Melville','Henry Miller','T.S. Eliot','Graham Greene', 'Chekhov','Huxley','Julian Barnes','Agatha','Leo Tolstoy','Dostoyevsky','Keigo Higashino','Raymond Chandler','Margaret Atwood','Primo Levi','Jules Verne','John le Carré','Félicien de Saulcy','Maya Angelou','Isaac Bashevis','Wislawa Szymborska','Ray Bradbury','Sylvia Plath','Gabriel García Márquez','Jane Austen','G.K. Chesterton','Sinclair Lewis','Roald Dahl','John Updike','George Orwell']
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


with open('./docs/full.json', 'w') as f:
    json.dump(json_records, f,ensure_ascii=False,indent=2)

timeindicator=0
for hour in range(24):  # Loop from 0 to 23 for the hours
    for minute in range(60):  # Loop from 0 to 59 for the minutes
        # Format the hour and minute to ensure two digits
        json_timerecord=[]  
        for item in json_records:
            if item['time'] ==f'{hour:02d}:{minute:02d}':
                json_timerecord.append(item)
        if json_timerecord:
            timeindicator+=1
            with open(f'./docs/times/{hour:02d}_{minute:02d}.json', 'w') as f:
                    json.dump(json_timerecord, f,ensure_ascii=False,indent=2)

print(timeindicator)


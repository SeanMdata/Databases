import numpy as np
import random
import os.path
import datetime

np.random.seed(1)

first_names = ['Sean', 'Matt', 'Daniel', 'Keith', 'Lex', 'John', 'Tyler']
last_names = ['Grouse', 'Hawk', 'Eagle', 'Luther', 'Lion', 'Tiger', 'Bear']

# Create Memebers Data
with open(os.path.join('/Users/sean/Documents/University_of_denver/comp_3421/Assignment_4/', 'members_data.csv'), 'w') as outfile:
	nummembers = 25000
	for i in range(1,nummembers+1):
		outString = ''
		outString += str(i)   # primary key memberid
		outString += ','
		outString += ''.join(random.choice(first_names) + ' ' + random.choice(last_names))
		outString += ','
		phone_num = str(random.randint(100000000, 999999999))
		outString += f'{phone_num}'
		outString += ','
		email = ''.join(random.choice(first_names) + random.choice(last_names)+ str(random.randint(1,99)) + '@gmail.com')
		outString += f'{email}'
		outString += ','
		memberstatus = random.choice(['active', 'inactive'])
		outString += f'{memberstatus}'
		outString += "\n"
		outfile.write(outString)

# # create the Locations data
with open(os.path.join('/Users/sean/Documents/University_of_denver/comp_3421/Assignment_4/', 'location_data.csv'), 'w') as outfile:
	numlocations = 1000
	for i in range(1,numlocations+1):
		outString = ''
		outString += str(i) #LocationID
		outString += ','
		outString += f'{random.randint(1,25000)}' # memberid (change this to num of members generated)
		outString += ','
		street_names = ['Red', 'King', 'beale', 'university']
		street_modifiers = ['Ave', 'Parkway', 'Street', 'Circle']
		outString += f'{random.randint(1000,9999)} {random.choice(street_names)} {random.choice(street_modifiers)}'
		outString += ','
		cities = ['denver', 'lakewood','englewood', 'fort collins']
		outString += random.choice(cities)
		outString += ','
		states = ['Colorado', 'New Mexico', 'California']
		outString += random.choice(states)
		outString += "\n"
		outfile.write(outString)



# create the Classes data
with open(os.path.join('/Users/sean/Documents/University_of_denver/comp_3421/Assignment_4/', 'classes_data.csv'), 'w') as outfile:
	numClasses = 475
	for i in range(1,numClasses+1):
		outString = ''
		outString += str(i) #Class ID
		outString += ','
		outString += f'{random.randint(1,25000)}' # memberid (change this to num of members generated)
		outString += ','
		days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
		outString += random.choice(days_of_week) #which day of week class is
		outString += ','
		outString += str(random.randrange(30,123,30))
		outString += ','
		class_group = ['Bodybuilders', 'Powerlifters', 'Cardio', 'Jazzercise']
		outString += random.choice(class_group)
		outString += "\n"
		outfile.write(outString)

# Generate Equipment Data
with open(os.path.join('/Users/sean/Documents/University_of_denver/comp_3421/Assignment_4/', 'equipment_data.csv'), 'w') as outfile:
	numequipment = 7000
	for i in range(1,numequipment+1):
		outString = ''
		outString += str(i)
		outString += ','
		outString += str(random.randint(1,1000)) #LocationID change to # of locations
		outString += ','
		manufacture = ['HammerStrength', 'Rogue', 'NordicTrack', 'Bowflex']
		outString += random.choice(manufacture)
		outString += ','
		start_date = datetime.date(2022, 1,1)
		end_date = datetime.date(2023,1,1)
		days_between = (end_date - start_date).days
		rand_num_days = random.randrange(days_between)
		outString += f'{start_date + datetime.timedelta(days = rand_num_days)}'
		outString += '\n'
		outfile.write(outString)

# Generate Hold Data
with open(os.path.join('/Users/sean/Documents/University_of_denver/comp_3421/Assignment_4/', 'hold_data.csv'), 'w') as outfile:
	numhold = 950
	for i in range(1,numhold+1):
		outString = ''
		outString += str(random.randint(1,475))
		outString += ','
		outString += str(random.randint(1,1000))
		outString += '\n'
		outfile.write(outString)


# Generate Own Data
with open(os.path.join('/Users/sean/Documents/University_of_denver/comp_3421/Assignment_4/', 'own_data.csv'), 'w') as outfile:
	numowned = 7000
	for i in range(1,numowned+1):
		outString = ''
		outString += str(random.randint(1, 1000))
		outString += ','
		outString += str(random.randint(1,7000))
		outString += '\n'
		outfile.write(outString)
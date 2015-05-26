from bs4 import BeautifulSoup
import sqlite3
import urllib2

url = "http://pokemondb.net/pokedex/national"
response = urllib2.urlopen(url)
html_doc = response.read() 

# the source code for the Wiki page
soup = BeautifulSoup(html_doc)
# the table that holds all of the Pokemon 
pokemon = soup.find_all('span', attrs={"class": "infocard-tall"})

db = sqlite3.connect(':memory:')
cursor = db.cursor() 

cursor.execute('''CREATE TABLE pokemon(id PRIMARY KEY, name TEXT, num TEXT)''')
db.commit() 

for i in range(0, 151):
	name = str(pokemon[i].find("a", attrs={"class": "ent-name"}).contents[0].encode("ascii", "ignore"))
	num = pokemon[i].find("small").text 
	print num
	cursor.execute('''INSERT INTO pokemon(name, num) VALUES(?, ?)''', (name, num))

print "Successfully compiled database."
db.commit()

# main logic
print "Welcome to the First Generation National Pokedex Number Finder! Type help for instructions, or quit to exit."
run = True 
while run: 
	response = raw_input("pokedb> ")
	response = response.strip().lower()

	if response == "help":
		print "Enter the name of a Pokemon, and the program will find the National Pokedex number for that Pokemon."
	elif response == '' or response == None:
		print "Invalid input. Try again."
	elif response == "quit":
		print "Ending session..."
		db.close() 
		run = False
	else:
		cursor.execute('''SELECT name, num FROM pokemon WHERE name = ?''', (response.capitalize(),))
		found = cursor.fetchone() 
		if found == None:
			print "No matches found."
		else:
			print "%s's National Pokedex Number: %s" % (response, found[1]) 





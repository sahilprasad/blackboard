import sqlite3 

db = sqlite3.connect(':memory:')
cursor = db.cursor() 

cursor.execute('''
	CREATE TABLE contacts(id INTEGER PRIMARY KEY, name TEXT,
		phone TEXT, email TEXT)
''')

db.commit() 

def add():
	name = raw_input("Name: ")
	phone = raw_input("Phone: ")
	email = raw_input("Email: ")
	cursor.execute('''
		INSERT INTO contacts (name, phone, email)
		VALUES(?, ?, ?)
	''', (name, phone, email))
	db.commit() 
	print "%s was added to the address book." % name 

def print_contacts():
	print "------------CONTACTS------------------------"
	print "ID", "Name", "Phone", "Email"
	cursor.execute('''SELECT id, name, phone, email FROM contacts''')
	count = 0 
	for row in cursor:
		count += 1
		print row[0], row[1], row[2], row[3]

	print "Contacts in address book: %d" % count 

def delete():
	print_contacts() 
	delete_possible = False
	while not delete_possible:
		x = raw_input("Enter the id of the contact you wish to delete, or pass to stop: ")
		if x.strip() == "pass":
			delete_possible = True
			break
		try:
			iden = int(x)
			cursor.execute('''SELECT id, name FROM contacts WHERE id = ?''',
				(iden,))
			found = cursor.fetchone() 
			if found == None:
				print "That person does not exist in the address book. Try again..."
			else:
				cursor.execute('''DELETE FROM contacts WHERE id = ?''',
					(iden,))
				print "%s was deleted from the address book." % found[1]
				delete_possible = True
		except ValueError:
			print "Invalid input. Try again..."

def update():
	print_contacts()
	x = raw_input("Enter the id of the contact you wish to update: ")
	try:
		iden = int(x)
		cursor.execute('''SELECT id, name, phone, email FROM contacts where id = ?''',
			(iden,))
		found = cursor.fetchone() 
		if found == None:
			print "That person does not exist in the address book. Try again..."
		else:
			field = raw_input("Indicate which field you wish to update by typing name, phone, or email.\n")
			field_ = field.strip().lower() 
			if field_ == "name":
				new_value = raw_input("New name: ")
				cursor.execute('''UPDATE contacts SET name = ? WHERE id = ?''', (new_value, iden))
			elif field_ == "phone":
				new_value = raw_input("New phone: ")
				cursor.execute('''UPDATE contacts SET phone = ? WHERE id = ?''', (new_value, iden))
			elif field_ == "email":
				new_value = raw_input("New email: ")
				cursor.execute('''UPDATE contacts SET email = ? WHERE id = ?''', (new_value, iden))
			else:
				raise ValueError

			db.commit() 

			print "%s's %s attribute has been updated." % (found[1], field_)

	except ValueError:
		print "Invalid input. Try again..."

keep_asking = True
while keep_asking:
	action = raw_input("Type add, delete, update, or print to perform" +
	 "actions on the address book, or exit to quit the program.\n")
	action_ = action.strip().lower() 
	if action_ == "add":
		add()
	elif action_ == "delete":
		delete() 
	elif action_ == "update":
		update()
	elif action_ == "print":
		print_contacts() 
	elif action_ == "exit" or action_ == None:
		print "Good day! Ending session..."
		keep_asking = False 
	else:
		print "Input not recognized. Try again."


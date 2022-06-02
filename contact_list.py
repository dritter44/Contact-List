class ContactList():
	def __init__(self, name, contacts):
		self.name = name
		self.contacts = contacts#.sort(key=lambda item: item.get("name"))				#sort by contacts name: friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
	
	#create method to call static method of contacts
	def sorted_contacts(self):
		return self.list_sorted(self.contacts)
	
	#create a static method to sort the list by name
	@staticmethod
	def list_sorted(list_of_contacts):
		list_of_contacts.sort(key=lambda item: item.get("name"))
		return list_of_contacts


	#method 1 - `add_contact({})` should add a new contact to the list, while keeping the list sorted
	def add_contact(self, new_contact):
		self.contacts.append(new_contact)
		return self.list_sorted(self.contacts)
	
	#method 2: `remove_contact('Alice')` should remove a contact from the list by name.
	def remove_contact(self,contact):
		self.contacts = list(filter(lambda i: i['name'] != contact, self.contacts))
		return self.list_sorted(self.contacts)

	# method 3`find_shared_contacts(ContactList)` should accept another contact list as an argument, 
	# and then return a new list of dictionaries to indicate all the contacts that appear in both lists (exact same name and phone number).
	#friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
	#work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

	#study this method and figure out what the fuck happened
	def shared_contacts(self, new_list):
		shared_dict = []
		shared_dict = [value for value in self.contacts if value in new_list]
		return shared_dict

	



friends = ContactList('Friends',[{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'},{'name':'Aly', 'number':'111-1111'},{'name':'Dan', 'number':'345-5555'}])
work_buddies = ContactList('Work Buddies', [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}])
#print(friends.contacts)
#print(friends.sorted_contacts())
#print(friends.remove_contact('Alice'))
print(friends.shared_contacts(work_buddies.contacts))

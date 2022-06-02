def list_sorted(list_of_contacts):
	#list_of_contacts = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'},{'name':'Aly', 'number':'111-1111'},{'name':'Dan', 'number':'345-5555'}]
    list_of_contacts.sort(key=lambda item: item.get("name"))
    return list_of_contacts

print(list_sorted([{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'},{'name':'Aly', 'number':'111-1111'},{'name':'Dan', 'number':'345-5555'}]))
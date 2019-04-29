'''JavaScript OBject Notation '''
import json


people_string = '''
{
	"people":[
	{
		"name": "John Smith",
		"phone":"615-555-7164",
		"emails":["johnsmith@bogusemail.com","john.smith@work-place.com"],
		"has_license": false

	},{
		"name": "Jane Doe",
		"phone": "560-555-5153",
		"emails": null,
		"has_license": true
	}]
}
'''
###########################################################

data = json.loads(people_string)
# print(data)


###########################################################
# python treated array as list
'''
for person in data['people']:
	print(person['name'])


###########################################################
# delete the phone key of person
# convert python dict object to json 
# parameters: indent=2, sort_keys=True
# loads stands for load strings

data = json.loads(people_string) 

for person in data['people']:
	del person['phone'] 

new_string = json.dumps(data, indent=2, sort_keys=True) 

print(new_string)
'''

###########################################################
# open the json file
# dump it into json file

'''
with open('./snippets/states.json') as f:
	data = json.load(f)

for state in data['states']:
	# print(state['name'], state['abbreviation'])
	del state['area_codes']

with open('new_state.json', 'w') as f:
	json.dump(data, f, indent=2)

'''
############################################################

from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
	source = response.read()

print(source)
















'''
JSON			Python
object			dict
array			list
string			str
number (int)	int
number (real)	float
true			True
false			False
null			None
'''
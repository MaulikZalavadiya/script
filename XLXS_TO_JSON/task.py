import json 
  
state = open('Sheet1.json',) 
all_data = open('data1.json')
  
state1 = json.load(state)
all_data1 = json.load(all_data)

result = {}
final_result = {}
for i in state1:
	state2 = i['STATE']
	result.update({state2:set()})
	# import pdb;pdb.set_trace()
	for j in all_data1:
		if j['STATE'] == i['STATE']:
			# pass
			result[state2].update({j['DISTRICT']})
			result[state2].update({j['TALUK']})

for key, value in result.items():
	# import pdb;pdb.set_trace()
	final_result.update({key: list(value)})
    # ids.append(person_id)
    # first_names.add(details['first'])
    # last_names.add(details['last'])
import pdb;pdb.set_trace()
json_object = json.dumps(final_result)
# print(json_object)  
# print(result)  
with open('result1.json', 'w') as outfile:
    json.dump(json_object, outfile)

state.close()
all_data.close()

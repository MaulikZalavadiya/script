import pandas as pd

data = pd.read_excel('All india pincode.xlsx', skiprows=[0])

newData = data.drop_duplicates()
state = newData['STATE']
di = newData.to_dict()



distict = newData['DISTRICT']
taluka = newData['TALUK']
# import pdb;pdb.set_trace()
state = state.drop_duplicates()
distict = distict.drop_duplicates()

newData.to_excel("FileWithoutDuplicateValues1.xlsx", index=False)
state.to_excel('state.xlsx', index=False)
# distict.to_excel('distict.xlsx', index=False)
# taluka.to_excel('taluka.xlsx', index=False)

# convert json from excel using excel2json
from excel2json import convert_from_file


convert_from_file('state.xlsx')

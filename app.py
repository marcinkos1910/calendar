from generate_data import GenerateData
from user import User
from meeting import Meeting
from pprint import pp


data = GenerateData.load_data()
# pp(data)
print(20 * '_')
meeting = data['meetings'][0]
pp(meeting)
print(20 * '_')
owner = User(**meeting['owner'][0])
print(owner)
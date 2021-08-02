from datetime import datetime
from my_calendar import Calendar
from generate_data import GenerateData
from user import User
from meeting import Meeting
from pprint import pp

from workshop import Workshop

data = GenerateData.load_data()

m = Calendar()

for meeting in data['meetings']:
    owner = User(**meeting['owner'][0])
    member_list = []
    for member in meeting['members']:
        member_list.append(User(**member))
    start_date = datetime.strptime(meeting['start_date'], '%Y-%m-%d %H:%M:%S.%f')
    m.add_event(Meeting(meeting['title'], start_date, int(meeting['duration']), meeting['localization'], owner, member_list))


for workshop in data['workshop']:
    owner = User(**workshop['owner'][0])
    trainer = User(**workshop['trainer'][0])
    start_date = datetime.strptime(workshop['start_date'], '%Y-%m-%d %H:%M:%S.%f')
    m.add_event(Workshop(workshop['title'], start_date, int(workshop['duration']), workshop['localization'], owner, trainer))

# pp(str(m))
# pp(repr(m))
# print(m == eval(repr(m)))
for item in m:
    print(item)


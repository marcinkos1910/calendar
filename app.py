from datetime import datetime

from generate_data import GenerateData
from user import User
from meeting import Meeting
from pprint import pp

from workshop import Workshop

data = GenerateData.load_data()


m = []
for meeting in data['meetings']:
    owner = User(**meeting['owner'][0])
    member_list = []
    for member in meeting['members']:
        member_list.append(User(**member))
    start_date = datetime.strptime(meeting['start_date'], '%Y-%m-%d %H:%M:%S.%f')
    m.append(Meeting(meeting['title'], start_date, int(meeting['duration']), meeting['localization'], owner, member_list))


for workshop in data['workshop']:
    owner = User(**workshop['owner'][0])
    trainer = User(**workshop['trainer'][0])
    start_date = datetime.strptime(workshop['start_date'], '%Y-%m-%d %H:%M:%S.%f')
    m.append(Workshop(workshop['title'], start_date, int(workshop['duration']), workshop['localization'], owner, trainer))

pp(m)




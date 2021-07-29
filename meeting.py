from datetime import datetime
from event import Event
from user import User


class Meeting(Event):

    def __init__(self, title, start_date, duration, localization, owner, members):
        super().__init__(title, start_date, duration, localization, owner)
        self.members = members

    @property
    def members(self):
        return self._members

    @members.setter
    def members(self, new_members):
        for new_member in new_members:
            if not isinstance(new_member, User):
                raise TypeError(f'Incorrect member type: {new_member}')
            self._members = new_members


owner = User("Marcin", "K", "a+@a.pl")
m = Meeting(title="browarek", start_date=datetime(2021, 5, 5), duration=60, localization="Krakow", owner="Marcin",
            members=['Ala', 'John', 'Ula'])

print(m)
print(repr(m))
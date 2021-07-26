from event import Event


class Meeting(Event):

    def __init__(self, title, start_date, duration, localization, owner, members):
        super().__init__(title, start_date, duration, localization, owner)
        self.members = members


m = Meeting(title="browarek", start_date="2021-05-05", duration=60, localization="Krakow", owner="Marcin",
            members=['Ala', 'John', 'Ula'])

print(m)
print(repr(m))
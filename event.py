class Event:
    def __init__(self, title, start_date, duration, localization, owner, members):
        self.title = title
        self.start_date = start_date
        self.duration = duration
        self.localization = localization
        self.owner = owner
        self.members = members

    def __str__(self):
        return f'{type(self).__name__}: title: {self.title}, start_date: {self.start_date},' \
                f'duration: {self.duration}, members: {self.members}'

    def __repr__(self):
        return f'{type(self).__name__}(title="{self.title}", start_date="{self.start_date}",' \
                f'duration="{self.duration}", localization="{self.localization}", owner="{self.owner}"members="{self.members}")'


e = Event(title="browarek", start_date="2021-05-05", duration=50, localization="Krakow", owner="Marcin", members=[])
print(e)
print(repr(e))
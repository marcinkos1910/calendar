from datetime import datetime, timedelta

from user import User


class Event:
    def __init__(self, title, start_date, duration, localization, owner):
        self.title = title
        self.start_date = start_date
        self.duration = duration
        self.localization = localization
        self.owner = owner

    def __str__(self):
        return f'{type(self).__name__}: title: {self.title}, start_date: {self.start_date},' \
                f'duration: {self.duration}, localization: {self.localization}, owner: {self.owner}'

    def __repr__(self):
        return f'{type(self).__name__}(title="{self.title}", start_date="{self.start_date}",' \
                f'duration="{self.duration}", localization="{self.localization}", owner="{self.owner}")'

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        if not isinstance(new_owner, User):
            raise TypeError(f'Incorrect user type: {new_owner}')
        self._owner = new_owner

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, new_date):
        if new_date < datetime.now() + timedelta(minutes=float(10)):
            raise ValueError(f'You can assign events only 10min from now: {new_date}')
        self._start_date = new_date

    @property
    def duration(self):
        return f'{self._duration} minutes'

    @duration.setter
    def duration(self, value):
        if value <= 10:
            raise ValueError(f'Event has to last more than 10 min: {value}')
        self._duration = value


e = Event(title="browarek", start_date=datetime(2021, 7, 27), duration=12, localization="Krakow", owner="Marcin")
# e.start_date = datetime(2022, 8, 29)
# e.duration = 15
# print(e.duration)
# print(e)
# print(repr(e))

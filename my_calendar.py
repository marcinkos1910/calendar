from event import Event


class Calendar:

    def __init__(self, events=None):
        self.events = events

    @property
    def events(self):
        return self._events

    @events.setter
    def events(self, new_events):
        if new_events is not None:
            for event in new_events:
                if not isinstance(event, Event):
                    raise TypeError(f'{event} is not valid type')
        self._events = new_events or []

    def add_event(self, event):
        if not isinstance(event, Event):
            raise TypeError(f'{event} is not valid type')
        self.events.append(event)

    def __str__(self):
        return f'{type(self).__name__} has {len(self.events)} events.'

    def __repr__(self):
        return f'{type(self).__name__}(events={self.events})'



from event import Event


class Workshop(Event):
    def __init__(self, title, start_date, duration, localization, owner, trainer):
        super().__init__(title, start_date, duration, localization, owner)
        self.trainer = trainer

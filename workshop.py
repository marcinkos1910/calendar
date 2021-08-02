from event import Event
from user import User


class Workshop(Event):
    def __init__(self, title, start_date, duration, localization, owner, trainer):
        super().__init__(title, start_date, duration, localization, owner)
        self.trainer = trainer

    @property
    def trainer(self):
        return self._trainer

    @trainer.setter
    def trainer(self, new_trainer):
        if not isinstance(new_trainer, User):
            raise TypeError(f'Incorrect trainer format: {new_trainer}')
        self._trainer = new_trainer

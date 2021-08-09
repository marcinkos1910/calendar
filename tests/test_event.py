from datetime import datetime, timedelta
import unittest

from event import Event
from user import User


class TestEvent(unittest.TestCase):
    def setUp(self) -> None:
        self.title = "test"
        self.start_date = datetime.now()  + timedelta(minutes=20)
        self.duration = 30
        self.localization = "krakow"
        self.owner = User("ala", "a", "a@a.pl")
        self.e = Event(self.title, self.start_date, self.duration, self.localization, self.owner)

    # def test(self): - fake test to check setUp
    #     pass

    def test_init(self):
        self.assertIsInstance(self.e, Event)
        self.assertTrue(hasattr(self.e, "title"))
        self.assertTrue(hasattr(self.e, "start_date"))
        self.assertTrue(hasattr(self.e, "duration"))
        self.assertTrue(hasattr(self.e, "localization"))
        self.assertTrue(hasattr(self.e, "owner"))
        self.assertEqual(self.title, self.e.title)
        self.assertEqual(self.localization, self.e.localization)

    def test_get_start_date(self):
        self.assertEqual(self.start_date, self.e.start_date)

    def test_incorrect_start_date(self):
        date = datetime.now() + timedelta(minutes=2)

        with self.assertRaises(ValueError) as context:
            self.e.start_date = date
        self.assertTrue(f'You can assign events only 10min from now: {date}' in str(context.exception) )

    def test_get_duration(self):
        self.assertEqual(f'{self.duration} minutes', self.e.duration)

    def test_set_invalid_duration(self):
        val = 3

        with self.assertRaises(ValueError) as context:
            self.e.duration = val
        self.assertTrue(f'Event has to last more than 10 min: {val}', str(context.exception))
from django.test import TestCase

from .models import (
    Organisation,
    Person,
    Epitome,
    EpitomeCategory,
    EpitomeInstance,
    Skill,
    Interest,
    ProgrammingLanguage,
    Rating,
    OutofTen,
    RatingInstance,
)

class SimpleTestCase(TestCase):
	def test_addition(self):
		self.assertEqual(1 + 1, 2)

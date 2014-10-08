from random import randint

from django.core.management.base import BaseCommand

from ...factories import RatingInstanceFactory1, RatingInstanceFactory2

class Command(BaseCommand):
	help = 'Creates instances of the organisation model'

	def handle(self, *args, **options):
		for i in range(3):
			skill_rating_instance = RatingInstanceFactory1()
			print 'Rating Instance: {}'.format(skill_rating_instance)

		for i in range(3):
			interest_rating_instance = RatingInstanceFactory2()
			print 'Rating Instance: {}'.format(interest_rating_instance)
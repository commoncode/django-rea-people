from random import randint

from django.core.management.base import BaseCommand

from ...fixtures import make_objects
from ...models import RatingInstance, Person

class Command(BaseCommand):
	help = 'Creates instances of the organisation model'

	def handle(self, *args, **options):
		make_objects()
		print RatingInstance.objects.all()
		print Person.objects.all()
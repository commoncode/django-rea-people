from random import randint

from django.core.management.base import BaseCommand

from ...factories import OrganisationFactory

class Command(BaseCommand):
	help = 'Creates instances of the organisation model'

	def handle(self, *args, **options):
		for i in range(3):
			organisation = OrganisationFactory()
			print 'Organisation: {}'.format(organisation)
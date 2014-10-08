from django.utils import timezone

import factory

from .models import (Organisation, Person, EpitomeInstance, Epitome,
Skill, Interest, Rating, OutofTen, RatingInstance)

class OrganisationFactory(factory.DjangoModelFactory):
	class Meta:
		model = Organisation

	name = "N/A"
	number = "N/A"
	interest_in_courses = "N/A"


class PersonFactory(factory.DjangoModelFactory):
	class Meta:
		model = Person

	name = ""
	email = factory.LazyAttribute(lambda obj: '%s@gmail.com' % obj.name )
	position = "N/A"
	organisation = factory.SubFactory(OrganisationFactory)


class SkillFactory(factory.DjangoModelFactory):
	class Meta:
		model = Skill
	name = "Django"
	name_plural = "Djangos"
	text = "Django is my skill yo"
	slug = "skill_django"


class InterestFactory(factory.DjangoModelFactory):
	class Meta:
		model = Interest
	name = "Django"
	name_plural = "Djangos"
	text = "Wanna learn some Django"
	slug = "interest_django"


class EpitomeInstanceFactory(factory.DjangoModelFactory):
	class Meta:
		model = EpitomeInstance

	person = factory.SubFactory(PersonFactory)
	epitome = factory.SubFactory(InterestFactory)


class OutofTenFactory(factory.DjangoModelFactory):
	class Meta:
		model = OutofTen

	name = "Self Rated"


class RatingInstanceFactory(factory.DjangoModelFactory):
	class Meta:
		model = RatingInstance

	rating = factory.SubFactory(OutofTenFactory)
	epitome_instance = factory.SubFactory(EpitomeInstanceFactory)
	value = factory.Sequence(lambda n: '%d' % (n + 3))
	created_at = timezone.now()
	text = "this is self rating for my interest level in django"
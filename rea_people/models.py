from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from entropy import base
from polymorphic import PolymorphicModel
from rea import models as rea_models

CONTENT_MODELS =  ['skill', 'interest',]


# Create your models here.
class Organisation(rea_models.Agent):
    address = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    interest_in_courses = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Person(rea_models.Agent):
    email = models.EmailField()
    position = models.CharField(max_length=50)
    organisation = models.ForeignKey('Organisation', blank=True, null=False)
    user = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return self.name

class Epitome(rea_models.REAObject, base.NameMixin, base.SlugMixin, base.TextMixin):
    pass

class EpitomeCategory(base.NameMixin, base.SlugMixin, base.TextMixin):
    content_type = models.ForeignKey(ContentType, limit_choices_to={'model__in': CONTENT_MODELS },)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

class EpitomeInstance(models.Model):
    person = models.ForeignKey('Person', related_name='people')
    epitome = models.ForeignKey('Epitome')

class Skill(Epitome):
    pass

class Interest(Epitome):
    pass

class ProgrammingLanguage(models.Model):
    language = models.CharField(max_length=100)


class Rating(PolymorphicModel):
    name = models.CharField(max_length=100)
    def validate(self, value):
        try:
            int(value)
            return True
        except:
            return False

    def __unicode__(self):
        return self.name


class OutofTen(Rating):
    def validate(self, value):
        try:
            int(value)
            return value <=10 and value > 0
        except:
            return False

    def printable(self, value):
        if value:
            return 'THUMPS UP!'
        else:
            return 'THUMBS DOWN!'

class RatingInstance(base.CreatedMixin, base.TextMixin):
    rating = models.ForeignKey('Rating')
    epitome_instance = models.ForeignKey('EpitomeInstance')
    value = models.TextField()

    # text
    # created_at
    # created_by ??

    def clean(self):
        if not self.rating.validate(self.value):
            raise ValidationError

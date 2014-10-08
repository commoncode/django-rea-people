# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import entropy.base


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rea', '0001_initial'),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Epitome',
            fields=[
                ('reaobject_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='rea.REAObject')),
                ('name', models.CharField(max_length=1024)),
                ('name_plural', models.CharField(max_length=1024, blank=True)),
                ('text', models.TextField(default=b'', blank=True)),
                ('slug', models.SlugField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('rea.reaobject', entropy.base.BaseSlugMixin, models.Model),
        ),
        migrations.CreateModel(
            name='EpitomeCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024)),
                ('name_plural', models.CharField(max_length=1024, blank=True)),
                ('text', models.TextField(default=b'', blank=True)),
                ('slug', models.SlugField(max_length=255)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
            bases=(entropy.base.BaseSlugMixin, models.Model),
        ),
        migrations.CreateModel(
            name='EpitomeInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('epitome_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='rea_people.Epitome')),
            ],
            options={
                'abstract': False,
            },
            bases=('rea_people.epitome',),
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('agent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='rea.Agent')),
                ('address', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=10)),
                ('interest_in_courses', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('rea.agent',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('agent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='rea.Agent')),
                ('email', models.EmailField(max_length=75)),
                ('position', models.CharField(max_length=50)),
                ('organisation', models.ForeignKey(to='rea_people.Organisation', blank=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('rea.agent',),
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OutofTen',
            fields=[
                ('rating_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='rea_people.Rating')),
            ],
            options={
                'abstract': False,
            },
            bases=('rea_people.rating',),
        ),
        migrations.CreateModel(
            name='RatingInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(default=b'', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('value', models.TextField()),
                ('created_by', models.ForeignKey(related_name=b'rea_people_ratinginstance_created_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('epitome_instance', models.ForeignKey(to='rea_people.EpitomeInstance')),
                ('rating', models.ForeignKey(to='rea_people.Rating')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('epitome_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='rea_people.Epitome')),
            ],
            options={
                'abstract': False,
            },
            bases=('rea_people.epitome',),
        ),
        migrations.AddField(
            model_name='rating',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name=b'polymorphic_rea_people.rating_set', editable=False, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='epitomeinstance',
            name='epitome',
            field=models.ForeignKey(to='rea_people.Epitome'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='epitomeinstance',
            name='person',
            field=models.ForeignKey(related_name=b'people', to='rea_people.Person'),
            preserve_default=True,
        ),
    ]

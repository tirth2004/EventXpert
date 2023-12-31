# Generated by Django 4.2.7 on 2023-11-06 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(help_text='Enter the Event Name', max_length=100)),
                ('event_date', models.DateField()),
                ('venue', models.CharField(help_text='Enter Venue', max_length=150)),
                ('description', models.TextField(help_text='Enter Description of Event')),
                ('category', models.ManyToManyField(help_text='Select category for this event', to='management.category')),
            ],
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-05 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('WAITING', 'Waiting'), ('COMPLETED', 'Completed'), ('FAILED', 'Failed'), ('FETCH_IDS', 'Fetch IDs'), ('FETCH_MATCH_LISTS', 'Fetch match lists'), ('FETCH_MATCHES', 'Fetch matches')], default='WAITING', max_length=20)),
            ],
        ),
    ]

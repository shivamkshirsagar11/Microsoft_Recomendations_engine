# Generated by Django 2.2.1 on 2022-05-29 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0014_auto_20220529_0905'),
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastmovie', models.TextField(default=None, max_length=255)),
                ('what_action_performed', models.TextField(default=None, max_length=255)),
            ],
        ),
    ]

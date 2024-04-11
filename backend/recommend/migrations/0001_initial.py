# Generated by Django 4.2.7 on 2023-11-29 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City', models.CharField(max_length=255)),
                ('Place', models.CharField(max_length=255)),
                ('Ratings', models.FloatField()),
                ('Distance', models.CharField(max_length=255)),
                ('Place_desc', models.TextField()),
            ],
        ),
    ]
# Generated by Django 4.1.7 on 2023-03-28 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alpa_crudedjango_system', '0003_rename_age_people_age_rename_email_people_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='idnum',
            field=models.IntegerField(default=3),
        ),
    ]
# Generated by Django 4.0.3 on 2022-03-31 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_surveyquestion_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyquestionalternative',
            name='order',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]

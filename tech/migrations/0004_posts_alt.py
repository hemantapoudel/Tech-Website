# Generated by Django 3.0.4 on 2020-09-30 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0003_auto_20200917_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='alt',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
    ]

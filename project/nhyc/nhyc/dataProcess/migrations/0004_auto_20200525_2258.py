# Generated by Django 3.0.5 on 2020-05-25 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataProcess', '0003_auto_20200518_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseinfo',
            name='houseNumber',
            field=models.CharField(max_length=19, primary_key=True, serialize=False),
        ),
    ]
# Generated by Django 3.0.5 on 2020-05-26 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataProcess', '0006_auto_20200526_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='costrecord',
            name='costRecordId',
        ),
        migrations.AddField(
            model_name='costrecord',
            name='id',
            field=models.IntegerField(auto_created=True, db_index=True, default=0, editable=False, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]

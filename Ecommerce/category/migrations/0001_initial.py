# Generated by Django 4.1.1 on 2022-09-10 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('Idcat', models.AutoField(primary_key=True, serialize=False)),
                ('namecat', models.CharField(max_length=50)),
            ],
        ),
    ]

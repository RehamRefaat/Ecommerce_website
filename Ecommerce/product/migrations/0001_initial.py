# Generated by Django 4.1.1 on 2022-09-10 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Idpro', models.AutoField(primary_key=True, serialize=False)),
                ('namepro', models.CharField(max_length=50)),
                ('catid', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
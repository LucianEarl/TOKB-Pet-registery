# Generated by Django 3.0.7 on 2020-06-25 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=150)),
                ('species', models.CharField(choices=[('Dog', (('Mutt', 'Mutt'), ('Dalmatian', 'Dalmatian'), ('German Shepherd', 'German Shepherd'), ('Corgie', 'Corgie'), ('Beagle', 'Beagle'), ('Husky', 'Husky'))), ('Cat', (('Housecat', 'Housecat'), ('Sphynx', 'Sphynx'), ('Siamese', 'Siamese'), ('Bengal', 'Bengal'), ('Maine Coon', 'Maine Coon'), ('Ragdoll', 'Ragdoll'))), ('Parrot', (('Cockatoo', 'Cockatoo'), ('Indian Ringneck', 'Indian Ringneck'), ('Macaw', 'Macaw'), ('Galah', 'Galah'), ('Cockatiel', 'Cockatiel'), ('Conure', 'Conure'))), ('Snake', (('Anaconda', 'Anaconda'), ('Rattlesnake', 'Rattlesnake'), ('Cobra', 'Cobra'), ('Asp', 'Asp'), ('Python', 'Python'), ('Sea Snake', 'Sea Snake')))], max_length=20)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=7)),
                ('colour', models.CharField(choices=[('Brown', 'Brown'), ('Black', 'Black'), ('White', 'White'), ('Orange', 'Orange'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('Blue', 'Blue')], max_length=10)),
                ('eye_colour', models.CharField(choices=[('Brown', 'Brown'), ('Black', 'Black'), ('White', 'White'), ('Orange', 'Orange'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('Blue', 'Blue')], max_length=10)),
                ('markings', models.CharField(max_length=250)),
                ('missing', models.BooleanField()),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

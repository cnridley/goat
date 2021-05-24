# Generated by Django 3.2.3 on 2021-05-24 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featureCategory', models.CharField(blank=True, max_length=254, null=True)),
                ('feautureTitle', models.CharField(blank=True, max_length=254, null=True)),
                ('featureDesc', models.CharField(blank=True, max_length=254, null=True)),
                ('featureImage', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
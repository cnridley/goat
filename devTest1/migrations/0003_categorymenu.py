# Generated by Django 3.2.3 on 2021-05-24 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devTest1', '0002_insights'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
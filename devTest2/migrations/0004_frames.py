# Generated by Django 3.2.3 on 2021-05-25 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devTest2', '0003_breadcrumbs'),
    ]

    operations = [
        migrations.CreateModel(
            name='frames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frameHeader', models.CharField(blank=True, max_length=254, null=True)),
                ('frameInfo', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]

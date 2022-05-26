# Generated by Django 4.0.3 on 2022-04-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Name')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Comment')),
            ],
        ),
    ]

# Generated by Django 2.2.1 on 2019-11-19 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Names')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Phone Contact')),
                ('email', models.EmailField(max_length=254, verbose_name='E-Mail')),
                ('city', models.CharField(blank=True, max_length=25, verbose_name='City')),
                ('country', models.CharField(blank=True, max_length=25, verbose_name='Country')),
                ('title', models.CharField(max_length=30, verbose_name='Title')),
                ('message', models.TextField(verbose_name='Message')),
            ],
        ),
    ]

# Generated by Django 3.1.4 on 2021-07-10 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='John Doe', max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=300)),
                ('date_of_birth', models.DateTimeField()),
                ('sex', models.CharField(default='Unknown', max_length=6)),
            ],
        ),
    ]
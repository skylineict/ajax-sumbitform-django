# Generated by Django 3.2.6 on 2021-09-04 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uplaod_img', models.ImageField(upload_to='uplaods')),
                ('email', models.CharField(max_length=40)),
                ('username', models.CharField(max_length=30)),
                ('full_name', models.CharField(max_length=30)),
                ('joindate', models.DateField()),
            ],
        ),
    ]

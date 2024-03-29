# Generated by Django 2.2.2 on 2019-07-06 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainImagesNotCancer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/not_cancer')),
            ],
        ),
        migrations.CreateModel(
            name='TrainImagesOfCancer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/cancer')),
            ],
        ),
        migrations.DeleteModel(
            name='UserImage',
        ),
    ]

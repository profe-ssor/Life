# Generated by Django 4.1.3 on 2022-11-16 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_system', '0008_chatroom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]

# Generated by Django 2.2.1 on 2019-06-17 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0003_auto_20190617_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='city',
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AlterField(
            model_name='matches',
            name='player_of_the_match',
            field=models.CharField(default=None, max_length=164),
        ),
        migrations.AlterField(
            model_name='matches',
            name='result',
            field=models.CharField(default=None, max_length=164),
        ),
        migrations.AlterField(
            model_name='matches',
            name='team1',
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AlterField(
            model_name='matches',
            name='team2',
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AlterField(
            model_name='matches',
            name='toss_decision',
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AlterField(
            model_name='matches',
            name='toss_winner',
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AlterField(
            model_name='matches',
            name='umpire1',
            field=models.CharField(default=None, max_length=164),
        ),
        migrations.AlterField(
            model_name='matches',
            name='umpire2',
            field=models.CharField(default=None, max_length=164),
        ),
        migrations.AlterField(
            model_name='matches',
            name='umpire3',
            field=models.CharField(default=None, max_length=164),
        ),
        migrations.AlterField(
            model_name='matches',
            name='venue',
            field=models.CharField(default=None, max_length=164),
        ),
        migrations.AlterField(
            model_name='matches',
            name='winner',
            field=models.CharField(default=None, max_length=164),
        ),
    ]

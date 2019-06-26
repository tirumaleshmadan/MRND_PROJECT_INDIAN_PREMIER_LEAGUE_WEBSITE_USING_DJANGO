# Generated by Django 2.2.1 on 2019-06-17 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0007_auto_20190617_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deliveries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.IntegerField()),
                ('inning', models.IntegerField()),
                ('batting_team', models.CharField(blank=True, max_length=164, null=True)),
                ('bowling_team', models.CharField(blank=True, max_length=164, null=True)),
                ('over', models.IntegerField()),
                ('ball', models.IntegerField()),
                ('batsman', models.CharField(blank=True, max_length=164, null=True)),
                ('non_striker', models.CharField(blank=True, max_length=164, null=True)),
                ('bowler', models.CharField(blank=True, max_length=164, null=True)),
                ('is_super_over', models.IntegerField()),
                ('wide_runs', models.IntegerField()),
                ('bye_runs', models.IntegerField()),
                ('legbye_runs', models.IntegerField()),
                ('noball_runs', models.IntegerField()),
                ('penalty_runs', models.IntegerField()),
                ('batsman_runs', models.IntegerField()),
                ('extra_runs', models.IntegerField()),
                ('total_runs', models.IntegerField()),
                ('player_dismissed', models.CharField(blank=True, max_length=164, null=True)),
                ('dismissal_kind', models.CharField(blank=True, max_length=164, null=True)),
                ('fielder', models.CharField(blank=True, max_length=164, null=True)),
            ],
        ),
    ]
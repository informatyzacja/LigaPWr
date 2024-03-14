# Generated by Django 5.0 on 2024-03-10 21:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligapwr', '0008_calculate_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportranking',
            name='draws',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sportranking',
            name='loses',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sportranking',
            name='maches',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sportranking',
            name='wins',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='team_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='match_team_one_set', to='ligapwr.team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_two',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='match_team_two_set', to='ligapwr.team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='winner_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='match_winner_team_set', to='ligapwr.team'),
        ),
    ]

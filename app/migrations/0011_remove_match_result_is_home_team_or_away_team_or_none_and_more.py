# Generated by Django 5.0 on 2024-01-16 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_match_result_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='match',
            name='result_is_home_team_or_away_team_or_none',
        ),
        migrations.AlterField(
            model_name='match',
            name='result',
            field=models.CharField(blank=True, choices=[(models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='app.team'), None), (models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_matches', to='app.team'), None), ('Draw', 'Draw'), ('Canceled', 'Canceled')], max_length=50, null=True),
        ),
        migrations.AddConstraint(
            model_name='match',
            constraint=models.CheckConstraint(check=models.Q(('result', models.F('home_team_id')), ('result', models.F('away_team_id')), ('result', 'Draw'), ('result', 'Canceled'), _connector='OR'), name='result_is_home_team_or_away_team_or_draw_or_canceled'),
        ),
    ]

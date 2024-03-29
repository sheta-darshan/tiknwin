# Generated by Django 5.0 on 2024-01-16 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_match_result'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='match',
            name='result_is_home_team_or_away_team_or_draw_or_canceled',
        ),
        migrations.AlterField(
            model_name='match',
            name='result',
            field=models.CharField(blank=True, choices=[('home_1', 'India (Home)'), ('away_1', 'India (Away)'), ('home_2', 'Australia (Home)'), ('away_2', 'Australia (Away)'), ('home_3', 'Pakistan (Home)'), ('away_3', 'Pakistan (Away)'), ('home_4', 'New Zealand (Home)'), ('away_4', 'New Zealand (Away)'), ('home_5', 'England (Home)'), ('away_5', 'England (Away)'), ('home_6', 'Argentina (Home)'), ('away_6', 'Argentina (Away)'), ('home_7', 'Austria (Home)'), ('away_7', 'Austria (Away)'), ('home_8', 'Belgium (Home)'), ('away_8', 'Belgium (Away)'), ('home_9', 'Brazil (Home)'), ('away_9', 'Brazil (Away)'), ('home_10', 'Boston Celtics (Home)'), ('away_10', 'Boston Celtics (Away)'), ('home_11', 'Brooklyn Nets (Home)'), ('away_11', 'Brooklyn Nets (Away)'), ('home_12', 'New York Knicks (Home)'), ('away_12', 'New York Knicks (Away)'), ('Draw', 'Draw'), ('Canceled', 'Canceled')], default='', max_length=50),
        ),
        migrations.AddConstraint(
            model_name='match',
            constraint=models.CheckConstraint(check=models.Q(('result__startswith', 'home_'), ('result__startswith', 'away_'), ('result', 'Draw'), ('result', 'Canceled'), _connector='OR'), name='result_is_home_team_or_away_team_or_draw_or_canceled'),
        ),
    ]

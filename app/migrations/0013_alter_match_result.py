# Generated by Django 5.0 on 2024-01-16 13:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_match_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='result',
            field=models.CharField(blank=True, choices=[(models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='app.team'), None), (models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_matches', to='app.team'), None), ('Draw', 'Draw'), ('Canceled', 'Canceled')], max_length=50, null=True),
        ),
    ]

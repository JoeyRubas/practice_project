# Generated by Django 3.0.6 on 2020-06-09 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0007_delete_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='vote',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='practice.Candidate'),
        ),
    ]
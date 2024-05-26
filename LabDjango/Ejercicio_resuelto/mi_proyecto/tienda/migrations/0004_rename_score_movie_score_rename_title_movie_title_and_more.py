# Generated by Django 5.0.6 on 2024-05-25 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_remove_movie_genre_remove_movie_release_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='score',
            new_name='Score',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='title',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='votes',
            new_name='Votes',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='year',
            new_name='Year',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='id',
        ),
        migrations.AddField(
            model_name='movie',
            name='MovieID',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
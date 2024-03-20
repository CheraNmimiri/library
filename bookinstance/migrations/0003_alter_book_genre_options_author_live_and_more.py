# Generated by Django 5.0.3 on 2024-03-12 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookinstance', '0002_book_genre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book_genre',
            options={'verbose_name': 'Set genre'},
        ),
        migrations.AddField(
            model_name='author',
            name='live',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, help_text='Enter The date of death of the author', null=True),
        ),
    ]
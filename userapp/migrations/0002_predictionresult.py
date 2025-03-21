# Generated by Django 4.2.7 on 2025-01-17 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredictionResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('predicted_class', models.IntegerField()),
                ('image_url', models.URLField()),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='pdf_reports/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'predictionresult',
            },
        ),
    ]

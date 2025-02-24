# Generated by Django 5.1.6 on 2025-02-21 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('status', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=180)),
                ('latitude', models.DecimalField(decimal_places=11, max_digits=21)),
                ('longitude', models.DecimalField(decimal_places=11, max_digits=21)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Restaurante',
                'verbose_name_plural': 'Restaurantes',
                'ordering': ['name'],
            },
        ),
    ]

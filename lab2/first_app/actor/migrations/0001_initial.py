# Generated by Django 4.0.4 on 2022-06-05 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Actor')),
                ('gender', models.PositiveIntegerField()),
                ('age', models.PositiveIntegerField()),
                ('nationality', models.CharField(choices=[('eg', 'Egyptian'), ('ksa', 'Saudi Arabian'), ('kwait', 'Kuwait Citizen')], max_length=6)),
            ],
        ),
    ]

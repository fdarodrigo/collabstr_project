# Generated by Django 4.2.13 on 2024-06-28 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('platform', models.CharField(choices=[('Instagram', 'Instagram'), ('TikTok', 'TikTok'), ('User Generated Content', 'User Generated Content')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creators.creator')),
            ],
        ),
    ]

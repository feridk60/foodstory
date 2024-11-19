# Generated by Django 5.0.7 on 2024-11-16 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='sliders-image/')),
                ('describtion', models.TextField()),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliders',
            },
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
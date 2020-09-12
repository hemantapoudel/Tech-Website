# Generated by Django 3.0.4 on 2020-09-12 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tech.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('feature_image', models.ImageField(upload_to='Images')),
                ('image1', models.ImageField(blank=True, upload_to='Images')),
                ('first_paragraph', models.TextField()),
                ('h1', models.CharField(max_length=500)),
                ('image2', models.ImageField(blank=True, upload_to='Images')),
                ('paragraph1', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tech.Category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tech.Subcategory')),
            ],
        ),
    ]

# Generated by Django 5.1.6 on 2025-02-22 08:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('featured_image', models.ImageField(upload_to='uploads/%Y/%m/%d')),
                ('short_description', models.TextField(max_length=500)),
                ('blog_body', models.TextField(max_length=2000)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (0, 'Published')], default=0)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categories')),
            ],
        ),
    ]

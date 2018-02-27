# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-27 17:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20180227_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_item', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('adder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='exam.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='likeditem',
            name='Users',
        ),
        migrations.RemoveField(
            model_name='likeditem',
            name='item_name',
        ),
        migrations.AddField(
            model_name='likeditem',
            name='liked_by',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='LikedItems', to='exam.User'),
        ),
        migrations.AddField(
            model_name='likeditem',
            name='item',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='LikedItems', to='exam.AddedItem'),
        ),
    ]

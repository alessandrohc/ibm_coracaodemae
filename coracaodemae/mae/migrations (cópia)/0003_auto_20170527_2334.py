# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 23:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mae', '0002_auto_20170527_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.TextField(verbose_name='post')),
            ],
        ),
        migrations.RemoveField(
            model_name='mae',
            name='about_me',
        ),
        migrations.RemoveField(
            model_name='mae',
            name='access_token',
        ),
        migrations.RemoveField(
            model_name='mae',
            name='blog_url',
        ),
        migrations.RemoveField(
            model_name='mae',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='mae',
            name='facebook_name',
        ),
        migrations.RemoveField(
            model_name='mae',
            name='facebook_open_graph',
        ),
        migrations.RemoveField(
            model_name='mae',
            name='facebook_profile_url',
        ),
        migrations.RemoveField(
            model_name='mae',
            name='foto_mae',
        ),
        migrations.RemoveField(
            model_name='mae',
            name='fotos_casa',
        ),
        migrations.RemoveField(
            model_name='mae',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='mae',
            name='image',
        ),
        migrations.RemoveField(
            model_name='mae',
            name='new_token_required',
        ),
        migrations.RemoveField(
            model_name='mae',
            name='raw_data',
        ),
        migrations.RemoveField(
            model_name='mae',
            name='website_url',
        ),
        migrations.AddField(
            model_name='imagens',
            name='mae',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mae.Mae'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mae',
            name='foto_mae_gd',
            field=models.ImageField(default=1, upload_to='uploads', verbose_name='Foto da Mãe grande'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mae',
            name='foto_mae_pq',
            field=models.ImageField(default=1, upload_to='uploads', verbose_name='Foto da Mãe Pequena'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mae',
            name='ibm_verificado_mulher',
            field=models.BooleanField(default=1, verbose_name='API da IBM verificou se eh mulher.'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mae',
            name='facebook_id',
            field=models.IntegerField(default=1, verbose_name='Facebook ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='mae',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mae.Mae'),
        ),
        migrations.AddField(
            model_name='friends',
            name='mae',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mae.Mae'),
        ),
    ]

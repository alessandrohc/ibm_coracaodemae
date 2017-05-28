# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 18:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Filho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome')),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=1, verbose_name='Sexo')),
                ('crianca_especial', models.BooleanField(verbose_name='É criança com cuidados especiais')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('alergico', models.CharField(blank=True, max_length=250, verbose_name='Alergias')),
                ('doencas', models.TextField(blank=True, verbose_name='Doenças')),
                ('escola', models.CharField(blank=True, max_length=50, verbose_name='Escola')),
                ('cep_escola', models.IntegerField(blank=True, null=True, verbose_name='Cep Escola')),
                ('natacao', models.BooleanField(verbose_name='Faz natação')),
                ('cep_natacao', models.IntegerField(blank=True, null=True, verbose_name='Cep Natação')),
                ('judo', models.BooleanField(verbose_name='Faz judo')),
                ('cep_judo', models.IntegerField(blank=True, null=True, verbose_name='Cep judo')),
                ('bale', models.BooleanField(verbose_name='Faz bale')),
                ('cep_bale', models.IntegerField(blank=True, null=True, verbose_name='Cep bale')),
                ('ingles', models.BooleanField(verbose_name='Faz ingles')),
                ('cep_ingles', models.IntegerField(blank=True, null=True, verbose_name='Cep ingles')),
            ],
        ),
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Mae',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', models.TextField(blank=True, null=True)),
                ('facebook_id', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('access_token', models.TextField(blank=True, help_text='Facebook token for offline access', null=True)),
                ('facebook_name', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook_profile_url', models.TextField(blank=True, null=True)),
                ('website_url', models.TextField(blank=True, null=True)),
                ('blog_url', models.TextField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female')], max_length=1, null=True)),
                ('raw_data', models.TextField(blank=True, null=True)),
                ('facebook_open_graph', models.NullBooleanField(help_text='Determines if this user want to share via open graph')),
                ('new_token_required', models.BooleanField(default=False, help_text='Set to true if the access token is outdated or lacks permissions')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='images/facebook_profiles/%Y/%m/%d')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='E-mail')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome')),
                ('foto_mae', models.ImageField(upload_to='uploads', verbose_name='Foto da Mãe')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('logradouro', models.CharField(max_length=25, verbose_name='Logradouro')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('cep', models.IntegerField(verbose_name='CEP')),
                ('aceita_crianca_especial', models.BooleanField(verbose_name='Aceita crianças especiais')),
                ('idade_minima_crianca', models.IntegerField(verbose_name='Idade mínima da criança')),
                ('idade_maxima_crianca', models.IntegerField(verbose_name='Idade maxima da criança')),
                ('facebook', models.CharField(max_length=250, verbose_name='Link do Facebook')),
                ('telefone', models.IntegerField(verbose_name='Telefone')),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor/Hora')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('disponivel_segunda', models.BooleanField(verbose_name='Segunda')),
                ('disponivel_terca', models.BooleanField(verbose_name='Terça')),
                ('disponivel_quarta', models.BooleanField(verbose_name='Quarta')),
                ('disponivel_quinta', models.BooleanField(verbose_name='Quinta')),
                ('disponivel_sexta', models.BooleanField(verbose_name='Sexta')),
                ('disponivel_sabado', models.BooleanField(verbose_name='Sábado')),
                ('disponivel_domingo', models.BooleanField(verbose_name='Domingo')),
                ('disponivel_hora_inicio', models.TimeField(blank=True, verbose_name='Hora inicio')),
                ('disponivel_hora_fim', models.TimeField(blank=True, verbose_name='Hora fim')),
                ('fotos_casa', models.ManyToManyField(blank=True, to='mae.Imagens', verbose_name='Fotos da casa')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='filho',
            name='mae',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mae.Mae'),
        ),
    ]

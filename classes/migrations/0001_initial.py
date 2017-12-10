# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 05:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='강의 제목')),
                ('short_discription', models.CharField(blank=True, max_length=100, null=True, verbose_name='요약 설명')),
                ('class_code', models.CharField(max_length=20, unique=True, verbose_name='학수번호')),
                ('credit', models.IntegerField(default=3, verbose_name='시수')),
                ('major', models.CharField(max_length=20, verbose_name='전공')),
            ],
        ),
        migrations.CreateModel(
            name='RegisterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.IntegerField(default=1, verbose_name='분반')),
                ('day', models.CharField(default='mon', max_length=20, verbose_name='요일 및 시간')),
                ('class_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.ClassModel', verbose_name='과목')),
                ('prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='교수자')),
                ('student', models.ManyToManyField(to='student.StudentModel')),
            ],
        ),
    ]

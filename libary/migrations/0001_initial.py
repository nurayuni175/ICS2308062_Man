# Generated by Django 5.1 on 2024-08-27 07:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=100)),
                ('author', models.TextField(max_length=100)),
                ('published_year', models.IntegerField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('student_name', models.TextField(max_length=100)),
                ('student_phone', models.CharField(max_length=100)),
                ('student_email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('borrow_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('borrow_date', models.DateField(max_length=100)),
                ('return_date', models.DateField(max_length=100)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libary.book')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libary.student')),
            ],
        ),
    ]

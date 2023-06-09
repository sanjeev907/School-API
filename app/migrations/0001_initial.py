# Generated by Django 4.1.7 on 2023-03-28 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=150)),
                ('Name', models.CharField(max_length=150)),
                ('City', models.CharField(max_length=150)),
                ('Pincode', models.IntegerField()),
                ('Password', models.CharField(max_length=100)),
                ('Otp', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Grade', models.CharField(max_length=150)),
                ('Username', models.CharField(max_length=150)),
                ('Password', models.CharField(max_length=150)),
                ('School_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.school')),
            ],
        ),
    ]

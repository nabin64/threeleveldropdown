# Generated by Django 4.1.5 on 2023-03-23 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.district')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.local')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.province')),
            ],
        ),
    ]

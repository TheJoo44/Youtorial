# Generated by Django 3.0 on 2020-03-20 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200320_0119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='user',
        ),
        migrations.AddField(
            model_name='video',
            name='tutorial',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main_app.Tutorial'),
            preserve_default=False,
        ),
    ]

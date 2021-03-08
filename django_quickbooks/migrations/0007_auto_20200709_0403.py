# Generated by Django 3.0.7 on 2020-07-09 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_quickbooks', '0006_auto_20200526_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='realm',
            name='schema_name',
            field=models.CharField(default='default', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='qbdtask',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

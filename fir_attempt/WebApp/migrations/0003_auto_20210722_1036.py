# Generated by Django 3.2.5 on 2021-07-22 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_auto_20210722_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cost',
            name='Web_ID',
        ),
        migrations.AddField(
            model_name='cost',
            name='Course_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='WebApp.course'),
        ),
        migrations.AlterField(
            model_name='cost',
            name='Teach_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='WebApp.teacher'),
        ),
    ]
# Generated by Django 3.1.4 on 2021-03-30 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_auto_20210330_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='leads.agent'),
        ),
    ]

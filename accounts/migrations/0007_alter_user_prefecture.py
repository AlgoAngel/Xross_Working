# Generated by Django 4.0.6 on 2023-06-03 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customAdmin', '0001_initial'),
        ('accounts', '0006_employer_google_map_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='prefecture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customAdmin.prefecture'),
        ),
    ]

# Generated by Django 4.0.6 on 2023-05-31 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_employer_company_url_employer_facebook_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userskill',
            name='skill',
        ),
        migrations.RemoveField(
            model_name='userskill',
            name='user',
        ),
        migrations.DeleteModel(
            name='JobHistory',
        ),
        migrations.DeleteModel(
            name='UserSkill',
        ),
    ]

# Generated by Django 3.0.5 on 2020-07-26 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_faq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='content',
            field=models.TextField(blank=True, max_length=375, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(max_length=60, null=True),
        ),
    ]

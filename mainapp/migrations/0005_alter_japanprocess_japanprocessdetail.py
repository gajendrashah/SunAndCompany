# Generated by Django 5.1.1 on 2024-10-22 03:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_japanabout_japandocument_japanprocess'),
    ]

    operations = [
        migrations.AlterField(
            model_name='japanprocess',
            name='japanProcessDetail',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]

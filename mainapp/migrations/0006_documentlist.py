# Generated by Django 5.1.1 on 2024-10-25 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_japanprocess_japanprocessdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='documentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploadDocument', models.ImageField(upload_to='docimg')),
                ('docName', models.CharField(max_length=200)),
            ],
        ),
    ]

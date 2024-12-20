# Generated by Django 5.1.1 on 2024-10-02 03:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutdetail', models.TextField()),
                ('mission', models.TextField()),
                ('vision', models.TextField()),
                ('msgFounder', models.TextField()),
                ('bulletPoint', models.TextField()),
                ('yrexperiance', models.IntegerField()),
                ('founderName', models.CharField(max_length=200)),
                ('founderimage', models.ImageField(upload_to='founder')),
                ('firstimage', models.ImageField(upload_to='aboutone')),
                ('secondimage', models.ImageField(upload_to='abouttwo')),
            ],
        ),
        migrations.CreateModel(
            name='blogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('commentBlog', models.CharField(max_length=200)),
                ('rateBlog', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='centralProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shotrDescription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='clientReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewName', models.CharField(max_length=200)),
                ('reviewImage', models.ImageField(upload_to='reviewimage')),
                ('reviewProfession', models.CharField(max_length=200)),
                ('reviewReview', models.TextField()),
                ('reviewStart', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='customSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleDesc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='featureItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_feature', models.CharField(max_length=200)),
                ('description_feature', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='imageSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageup', models.ImageField(null=True, upload_to='sayImag')),
                ('title', models.CharField(max_length=200)),
                ('sub_title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='latestNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('blogImg', models.ImageField(upload_to='blogImage')),
            ],
        ),
        migrations.CreateModel(
            name='listProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleProcess', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='phoneNo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='proofJapan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docTitle', models.CharField(max_length=200)),
                ('docDesc', models.CharField(max_length=200)),
                ('docImage', models.ImageField(null=True, upload_to='proofImageJapan')),
            ],
        ),
        migrations.CreateModel(
            name='proofNepal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docTitle', models.CharField(max_length=200)),
                ('docDesc', models.CharField(max_length=200)),
                ('docImage', models.ImageField(null=True, upload_to='proofImageNepal')),
            ],
        ),
        migrations.CreateModel(
            name='serviceHeading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortDescription', models.TextField()),
                ('serviceHeadImage', models.ImageField(upload_to='servicehead')),
            ],
        ),
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleService', models.CharField(max_length=200)),
                ('serviceDescription', models.TextField()),
                ('serviceTitleImage', models.ImageField(upload_to='serviceImage')),
            ],
        ),
        migrations.CreateModel(
            name='sncFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.CharField(max_length=200)),
                ('feature_image', models.ImageField(upload_to='featureimage')),
            ],
        ),
        migrations.CreateModel(
            name='supportList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userSupport', models.ImageField(upload_to='Support_image')),
                ('userName', models.CharField(max_length=200)),
                ('userProfession', models.CharField(max_length=200)),
                ('userFacebook', models.URLField()),
                ('userInstagram', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='vacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacanciesImage', models.ImageField(upload_to='vacancy')),
                ('countryName', models.CharField(max_length=200)),
                ('interviewLocation', models.TextField()),
                ('lotNo', models.IntegerField()),
                ('approvalDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='basicInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.phoneno')),
            ],
        ),
        migrations.CreateModel(
            name='vacanciesWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200)),
                ('noOfVacancyMale', models.IntegerField()),
                ('noOfVacancyFemale', models.IntegerField()),
                ('salery', models.IntegerField()),
                ('food', models.BooleanField()),
                ('accomodation', models.BooleanField()),
                ('transportaion', models.BooleanField()),
                ('overtime', models.CharField(max_length=200)),
                ('vacanciesSlect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.vacancies')),
            ],
        ),
    ]

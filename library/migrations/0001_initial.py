# Generated by Django 4.0.6 on 2022-07-11 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_book', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Categories')),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='book_covers')),
                ('author', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('pdf', models.FileField(upload_to='pdfs')),
                ('recommended_books', models.BooleanField(default=False)),
                ('fiction_books', models.BooleanField(default=False)),
                ('business_books', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(related_name='books', to='library.category')),
            ],
        ),
    ]
# Generated by Django 4.1.4 on 2023-02-12 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال/غیرفعال')),
                ('is_deleted', models.BooleanField(verbose_name='حذف شده')),
                ('description', models.TextField(db_index=True, verbose_name='توضیحات')),
                ('short_description', models.CharField(db_index=True, max_length=360, null=True, verbose_name='خلاصه توضیحات')),
                ('slug', models.SlugField(blank=True, default='', max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, verbose_name='عنوان')),
                ('url_title', models.CharField(max_length=300, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(verbose_name='فعال/غیرفعال')),
                ('is_deleted', models.BooleanField(verbose_name='حذف شده')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='ProductTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(db_index=True, max_length=40, verbose_name='عنوان')),
                ('is_deleted', models.BooleanField(verbose_name='حذف شده')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.product')),
            ],
            options={
                'verbose_name': 'تگ',
                'verbose_name_plural': 'تگ ها',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='product_module.productcategory', verbose_name='دسته بندی'),
        ),
    ]

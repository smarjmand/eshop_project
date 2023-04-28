from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class ProductCategory(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان', db_index=True)
    url_title = models.CharField(max_length=300, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال')
    is_deleted = models.BooleanField(verbose_name='حذف شده')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


#-------------------------------------------------
class ProductBrand(models.Model):
    title = models.CharField(
        max_length=500,
        verbose_name='نام برند',
        db_index=True
    )
    is_active = models.BooleanField(blank=True, verbose_name='فعال/غیرفعال')
    class Meta:
        verbose_name ='برند'
        verbose_name_plural = 'برند ها'
    def __str__(self):
        return self.title


#-------------------------------------------------
class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    price = models.IntegerField(verbose_name='قیمت')
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    is_deleted = models.BooleanField(verbose_name='حذف شده')
    description = models.TextField(verbose_name='توضیحات', db_index=True)
# add image field to this model :
    image = models.ImageField(
        upload_to='images/products',
        null=True,
        blank=True,
        verbose_name='تصویر محصول'
    )
    short_description = models.CharField(
        max_length=360,
        null=True,
        verbose_name='خلاصه توضیحات',
        db_index=True
    )
    brand = models.ForeignKey(
        ProductBrand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    slug = models.SlugField(
        default="",
        null=False,
        blank=True,
        max_length=200,
        unique=True
    )

    category = models.ManyToManyField(ProductCategory,verbose_name='دسته بندی')

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural ="محصولات"


#-------------------------------------------------
class ProductTag(models.Model):
    caption = models.CharField(max_length=40, verbose_name='عنوان', db_index=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(verbose_name='حذف شده')
    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'
    def __str__(self):
        return self.caption

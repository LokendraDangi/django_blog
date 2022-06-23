from asyncio.windows_events import NULL
from django.db import models
from django.utils.text import slugify

# Create your models here.

# create Category Model
class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now = true => adds current timestamp whenever data is updated
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


#create Post Model
class Post(models.Model):
    #options for Status 
    ACTIVE = 'active'
    DEACTIVE = 'deactive'

    CHOICES_STATUS =(
        (ACTIVE, 'active'),
        (DEACTIVE, 'deactive'),
        )
    # foreign key 
    category_id = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    # unique constraint and length constraint
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    intro = models.CharField(max_length=150)
    body = models.TextField()
    # auto_now_add=True  => adds current timestamp of machine when data is created
    created_at = models.DateTimeField(auto_now_add=True)
    # ImageField is from Pillow Package 
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)

    def __str__(self):
        return self.title
    # to auto generate slug  
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

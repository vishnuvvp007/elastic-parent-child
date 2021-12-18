from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description=models.CharField(max_length=100,blank=False,null=False)
    # meta=models.JSONField()
    status = models.BooleanField(default=False)   
    published=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'categories'

    # new
    def type_to_string(self):
        if self.type == 'UN':
            return 'Unspecified'
        elif self.type == 'TU':
            return 'Tutorial'
        elif self.type == 'RS':
            return 'Research'




ARTICLE_TYPES = [
    ('UN', 'Unspecified'),
    ('TU', 'Tutorial'),
    ('RS', 'Research'),
    ('RW', 'Review'),
]


class Group(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
    categories = models.ManyToManyField(to=Category, blank=True, related_name='categories')
    code = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=2, choices=ARTICLE_TYPES, default='UN')
    # description=models.CharField(max_length=100,blank=False,null=False)
    # meta=models.JSONField()
    status = models.BooleanField(default=False)  
    published=models.DateTimeField(auto_now_add=True)

class Variant(models.Model):
    Variantsframeworkid=models.ForeignKey(Group, on_delete=models.CASCADE,null=True,blank=True)
    code = models.CharField(max_length=100,null=True,blank=True)
    Name = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    # meta = models.JSONField(null=True,blank=True)
    # status = models.BooleanField(default=True,null=True,blank=True)
    # features = models.JSONField(null=True,blank=True)
    # values = models.JSONField(null=True,blank=True)
    # barcode = models.CharField(max_length=50,null=True,blank=True)
    # price = models.CharField(max_length=100,null=True,blank=True)
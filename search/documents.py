from django.contrib.auth.models import User
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import *

@registry.register_document
class CategoryDocument(Document):
    id = fields.IntegerField()

    class Index:
        name = 'category'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Category
        fields = [
            'name',
            'description',
        ]

@registry.register_document
class ArticleDocument(Document):
    categories = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'name': fields.TextField(),
        'description': fields.TextField(),
    })
    # type = fields.TextField(attr='type_to_string')

    class Index:
        name = 'groups'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Group
        fields = [
            'code',
            'name',
            'status',
        ]
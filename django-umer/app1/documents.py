# from django_elasticsearch_dsl import (
#     Document ,
#     fields,
#     Index,
# )
# from .models import Post

# PUBLISHER_INDEX = Index('post')

# PUBLISHER_INDEX.settings(
#     number_of_shards=1,
#     number_of_replicas=1
# )
# @PUBLISHER_INDEX.doc_type
# class PostDocument(Document):
#     id = fields.IntegerField(attr='id')
#     fielddata=True
#     Post_Textfield = fields.TextField(
#         fields={
#             'raw':{
#                 'type': 'keyword',
#             }
#         }
#     )
#     content = fields.TextField(
#         fields={
#             'raw': {
#                 'type': 'keyword',

#             }
#         },
#     )
#     image_Field = fields.TextField(
#         fields={
#             'raw': {
#                 'type': 'keyword',
#             }
#         }
#     )

#     views = fields.IntegerField()
#     Featured = fields.BooleanField()
#     Top = fields.BooleanField()
#     like = fields.IntegerField()
#     Comment = fields.IntegerField()
#     isPremium = fields.BooleanField()
#     scheduling_date_time = fields.DateField()

#     class Django(object):
#         model = Post

#     def prepare_image_Field(self, instance):
#         if instance.image_Field:
#             return instance.image_Field.url
#         return None

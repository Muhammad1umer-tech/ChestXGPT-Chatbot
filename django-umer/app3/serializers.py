from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import *
from .models import Post_test
# class NewsDocumentSerializer(DocumentSerializer):
#     class Meta(object):
#         """Meta options."""
#         model = Post_test
#         document = PostDocument
#         fields = (
#             'Post_Textfield',
#             'content',
#         )
#         def get_location(self, obj):
#             """Represent location value."""
#             try:
#                 return obj.location.to_dict()
#             except:
#                 return {}

# from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
# from django.http import JsonResponse
# from .models import Post_test
# import json
# import requests
# from elasticsearch.helpers import BulkIndexError
# from django_elasticsearch_dsl_drf.filter_backends import (
#     FilteringFilterBackend,
#     CompoundSearchFilterBackend,
# )
# from .serializers import *
# from .documents import *

# def generate_random_data():
#     url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-04-30&sortBy=publishedAt&apiKey=1daf34b622844488b1561b8ba68d575f'
#     r = requests.get(url)
#     payload = json.loads(r.text)
#     count = 1
#     for data in payload.get('articles'):
#         print(count)
#         try:
#             Post_test.objects.create(
#                 Post_Textfield = data.get('title'),
#                 content = data.get('description')
#             )
#         except BulkIndexError as e:
#             print("Bulk indexing failed:")
#             for error in e.errors:
#                 print(error)

# def index(request):
#     generate_random_data()
#     return JsonResponse({'status' : 200})
# class PublisherDocumentView(DocumentViewSet):
#     document = PostDocument
#     serializer_class = NewsDocumentSerializer
#     lookup_field = 'first_name'
#     fielddata=True
#     filter_backends = [
#         FilteringFilterBackend,
#         CompoundSearchFilterBackend,
#     ]
#     search_fields = (
#         'Post_Textfield',
#         'content',
#     )
#     multi_match_search_fields = (
#        'Post_Textfield',
#         'content',
#     )
#     filter_fields = {
#        'Post_Textfield' : 'Post_Textfield',
#         'content' : 'content',
#     }

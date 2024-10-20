from django.db import models

class Post_test(models.Model):
    Post_Textfield = models.TextField(max_length=100)
    content = models.TextField(max_length=200)

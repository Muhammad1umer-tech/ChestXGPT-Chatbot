"""
I made consumers to implement websockets
"""
import json
import jwt
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from app1 import models
from app1.views import decode_access_token_arg
from django.forms.models import model_to_dict
class ChatConsumer(WebsocketConsumer):
    """
    I made consumers to implement websockets
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_name = None
        self.room_group_name = None
        self.id = 0
        self.all_users_group_name = 'all_users_group'
    def connect(self):
        """
        when websocket is connect from the frontend. This function will run
        """
        # self.room_name = 'test_consumer'
        # self.room_group_name = 'test_consumer_group'

        self.room_name = 'w'
        access_token = self.scope['query_string'].decode(
            "utf-8").split('=')[1].split('/')[0]
        user_instance = model_to_dict(decode_access_token_arg(access_token))

        if(user_instance['is_superuser'] == True or user_instance['is_creator'] == True):
            self.all_users_group_name = 'admin_group'
            print("admin consumers")
        else:
            self.all_users_group_name = 'all_users_group'

        self.id = str(user_instance['id'])
        self.room_group_name = 'test_consumer_group_' + str(user_instance['id'])

        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)
        async_to_sync(self.channel_layer.group_add)(self.all_users_group_name, self.channel_name)
        print("Connect  consumers", self.all_users_group_name)


        self.accept()

    def disconnect(self, code):
        """
        when websocket is disconnect from the frontend. This function will run
        """
        print("disconnect  consumers")
        _ = code

    def send_post_notification(self, event):
        """
        in signal.py, when models update. this function will run and send notification
        for Post
        """
        print("send_notification post", self.all_users_group_name)
        value = event.get('value')
        # notification = models.Notification(notification=value)
        # notification.save()
        self.send(text_data=value)

    # def receive(self, text_data, bytes_data=None):
    #     """
    #     we can receive the data coming from the frontend
    #     it takes the access token, decode the user_id that like the post
    #     retrieve the user who posted th post and send the notification to him/her.

    #     """
    #     _ = bytes_data
    #     text_data = json.loads(text_data)
    #     # print(text_data)
    #     access_token = jwt.decode(text_data['access'],
    #     verify=False,
    #     options={'verify_signature': False})
    #     user_id = access_token['user_id']
    #     like_instance = models.Like.objects.filter(Post_id=text_data['post_id'],
    #     user_id=user_id)
    #     # print("like_instance", like_instance)
    #     if len(like_instance)>=1:
    #         user_instance = models.CustomUser.objects.get(pk=user_id)
    #         post_instance = models.Post.objects.get(pk=text_data['post_id'])
    #         notification = user_instance.username + text_data['notification']
    #         notification += post_instance.Post_Textfield
    #         models.Notification.objects.create(notification=notification,
    #         post_id=post_instance,
    #         to_user=post_instance.user_id,
    #         is_post_notification=False)
    #         self._send_notification_like(notification, post_instance.user_id)
    #     else:
    #         self.send(text_data=json.dumps({'status': "Already like the post"}))

    # def _send_notification_like(self, notification, to_user_id):
    #     """
    #     in signal.py, when models update. this function will run and send notification
    #     for like
    #     """
    #     async_to_sync(self.channel_layer.group_send)(
    #         self.room_group_name,{
    #         'type': 'send_notification',
    #         'value': notification
    #         })
    #     # print(f"Notification sent to user {to_user_id}")
    #     self.send(text_data=json.dumps(
    #     {'status': f"Notification sent to user {to_user_id}"}))

    def send_notification(self, event):
        """
        it send the notiication
        """
        print("send_notification", self.id)
        value = event.get('value')
        self.send(text_data=value)

    def send_comment_notification(self, event):
        """
        it send the notiication
        """
        print("send_notification comment", self.id)
        value = json.loads(event.get('value'))
        print("value", value)
        Post_intance = models.Post.objects.get(pk=value['Post'])
        user_id = 0
        if value['reply'] == True:
            user_id = models.CustomUser.objects.get(pk=value['user_id'])
        else:
            user_id = Post_intance.user_id
        models.Notification.objects.create(notification=value['message'],
        post_id=Post_intance,

        to_user=user_id,

        is_post_notification=False)
        self.send(text_data=value['message'][0])

    def send_like_notification(self, event):
        """
        it send the notiication
        """
        print("send_notification Like", self.id)
        value = json.loads(event.get('value'))
        print("value", value)
        # {'id': 719, 'user_id': 1, 'comment_id': None, 'Post_id': 18}
        Post_intance = models.Post.objects.get(pk=value['Post_id'])
        models.Notification.objects.create(notification=value['message'],
        to_user=Post_intance.user_id,
        post_id=Post_intance,
        is_post_notification=False)

        self.send(text_data=value['message'][0])
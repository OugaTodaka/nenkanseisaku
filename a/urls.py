from django.urls import path
from . import views

app_name = 'a'

urlpatterns = [
    path("",views.index, name='index'),
    path("post/",views.post, name='post'),
    path("<int:tweet_id>/reply/",views.reply,name='reply'),
    path("<int:tweet_id>/good/",views.good,name='good'),
    path("<int:tweet_id>/reply/rep_send/",views.reply_send,name='reply_send'),
]
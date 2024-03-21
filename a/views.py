from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Tweet,Reply
from django.utils import timezone

def index(request):
    tweet_list = Tweet.objects.all().order_by('-pub_date')
    reply_list = Reply.objects.all()
    context ={
        'tweet_list':tweet_list,
        'reply_list':reply_list,
        'user':request.user,
    }
    template = loader.get_template("a/index.html")
    return HttpResponse(template.render(context, request))

def post(request):
    name = request.user.username
    message = request.POST['message']
    tweet = Tweet(name=name,message=message,pub_date=timezone.now())
    tweet.save()
    return HttpResponseRedirect(reverse('a:index'))

def reply(request,tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    context = {
        'tweet':tweet
    }
    template = loader.get_template("a/reply.html")
    return HttpResponse(template.render(context,request))

def reply_send(request,tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    name = request.user.username
    rep = request.POST['rep']
    hensin = Reply(tweet=tweet,name=name,rep=rep,pub_date=timezone.now())
    hensin.save()
    return HttpResponseRedirect(reverse('a:index'))

def good(request,tweet_id):
    tweet =Tweet.objects.get(id=tweet_id)
    tweet.good += 1
    tweet.save()
    return HttpResponseRedirect(reverse('a:index'))

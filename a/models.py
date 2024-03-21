from django.db import models

class Tweet(models.Model):
    name = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    good = models.IntegerField(default=0)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.message

class Reply(models.Model):
    tweet = models.ForeignKey(Tweet,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    rep = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
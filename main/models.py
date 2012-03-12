from django.db import models
from django.contrib.auth.models import User

class Fact(models.Model):
    title = models.CharField(max_length=256)
    details = models.TextField(default="",blank=True,null=True)
    user = models.ForeignKey(User)
    source_name = models.CharField(max_length=256,default="")
    source_url = models.CharField(max_length=256,default="",blank=True,null=True)
    added = models.DateTimeField(auto_now_add=True,editable=False)

class Tag(models.Model):
    name = models.CharField(max_length=256)

    def get_absolute_url(self):
        return "/tag/%d/" % self.id

class FactTag(models.Model):
    fact = models.ForeignKey(Fact)
    tag = models.ForeignKey(Tag)

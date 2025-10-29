from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Community(models.Model):
    community_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='communities_created')
    members = models.ManyToManyField(User, related_name='joined_communities', blank=True)
    banner = models.ImageField(upload_to='community_banners/', null=True, blank=True)
    logo = models.ImageField(upload_to='community_logos/', null=True, blank=True)

    def total_members(self):
        return self.members.count()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='posts',  null=True, blank=True,)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

